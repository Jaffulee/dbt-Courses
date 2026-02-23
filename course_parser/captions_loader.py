from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .io_utils import list_json_files, read_json


@dataclass(frozen=True)
class CaptionChunk:
    text: str


@dataclass(frozen=True)
class CaptionsForMedia:
    hashed_id: str
    media_name: str | None
    chunks: list[CaptionChunk]


def _extract_media_objects(payload: Any) -> list[dict[str, Any]]:
    """
    Attempt to find media objects in a Wistia-like JSON.
    Supports shapes like:
      - {"media": {...}}
      - {"media": [{...}, {...}]}
      - {"results": [{"media": {...}}, ...]}
      - nested dict/list content where a dict has "hashedId"
    """
    media: list[dict[str, Any]] = []

    def walk(x: Any) -> None:
        if isinstance(x, dict):
            if "media" in x:
                m = x["media"]
                if isinstance(m, dict):
                    media.append(m)
                elif isinstance(m, list):
                    for it in m:
                        if isinstance(it, dict):
                            media.append(it)
            # heuristic: treat any dict with hashedId as a media object
            if "hashedId" in x and isinstance(x.get("hashedId"), str):
                media.append(x)
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for it in x:
                walk(it)

    walk(payload)

    # de-dup by hashedId when present
    by_id: dict[str, dict[str, Any]] = {}
    for m in media:
        hid = m.get("hashedId")
        if isinstance(hid, str):
            by_id[hid] = m
    return list(by_id.values())


def _extract_caption_texts(media_obj: dict[str, Any]) -> list[str]:
    """
    Extract caption text from typical caption structures.
    """
    out: list[str] = []

    captions = media_obj.get("captions")

    # captions might be list of dicts with "text"
    if isinstance(captions, list):
        for c in captions:
            if isinstance(c, dict):
                t = c.get("text")
                if isinstance(t, str) and t.strip():
                    out.append(t.strip())

    # sometimes captions might be dict keyed by language
    if isinstance(captions, dict):
        for v in captions.values():
            if isinstance(v, list):
                for c in v:
                    if isinstance(c, dict):
                        t = c.get("text")
                        if isinstance(t, str) and t.strip():
                            out.append(t.strip())

    return out


def load_captions_index(captions_root: Path, slug_subdir_name: str = "slug") -> dict[str, CaptionsForMedia]:
    """
    Load captions JSON files and index captions by hashedId.

    Args:
        captions_root: Directory containing captions json files plus a 'slug' folder.
        slug_subdir_name: Name of folder to exclude (contains slug json).

    Returns:
        Dict mapping hashedId -> CaptionsForMedia
    """
    all_files = list_json_files(captions_root, recursive=True)

    caption_files: list[Path] = []
    for p in all_files:
        # exclude slug folder
        if slug_subdir_name in {part.lower() for part in p.parts}:
            continue
        caption_files.append(p)

    index: dict[str, CaptionsForMedia] = {}

    for path in caption_files:
        payload = read_json(path)
        media_objects = _extract_media_objects(payload)

        for m in media_objects:
            hid = m.get("hashedId")
            if not isinstance(hid, str) or not hid.strip():
                continue

            name = m.get("name") if isinstance(m.get("name"), str) else None
            texts = _extract_caption_texts(m)

            if not texts:
                continue

            chunks = [CaptionChunk(text=t) for t in texts]
            index[hid] = CaptionsForMedia(hashed_id=hid, media_name=name, chunks=chunks)

    return index