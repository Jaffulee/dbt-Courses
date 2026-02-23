"""
inspect_json_keys.py

Reusable utility to inspect a JSON file and list all available "keys" (field paths),
including nested objects and arrays.

What it outputs:
- Dot/bracket paths such as:
    course.title
    sections[0].lessons[0]
    lessons[3].topics[2].type
    videos[0].body

This helps you see what fields exist so you can decide what to extract for
your course syllabus + captions pipeline.

Usage (PowerShell examples):
    python inspect_json_keys.py "response/refactoring SQL for modularity/slug/refactoring SQL for modularity.json"
    python inspect_json_keys.py "path/to/file.json" --max-items 10
    python inspect_json_keys.py "path/to/file.json" --out "json_paths.txt"
    python inspect_json_keys.py "response/refactoring SQL for modularity/slug/refactoring SQL for modularity.json" --out slug_keys.txt

Notes:
- Arrays are sampled up to --max-items items to avoid huge outputs.
- By default, paths include array indexes. If you prefer a wildcard style like
  videos[*].body, set --wildcards.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable, List, Set


def load_json(json_path: Path) -> Any:
    """
    Load JSON from disk.
    """
    return json.loads(json_path.read_text(encoding="utf-8"))


def iter_json_paths(
    obj: Any,
    prefix: str = "",
    *,
    max_items_per_list: int = 5,
    use_wildcards: bool = False,
) -> Iterable[str]:
    """
    Yield dot/bracket paths for all keys in a nested JSON-like structure.

    Parameters
    ----------
    obj:
        Parsed JSON value (dict/list/scalar)
    prefix:
        Current path prefix.
    max_items_per_list:
        Maximum list items to inspect per list.
    use_wildcards:
        If True, represent lists as [*] rather than [0], [1], etc.

    Yields
    ------
    str
        A path to a key/value.
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_prefix = f"{prefix}.{k}" if prefix else str(k)
            yield new_prefix
            yield from iter_json_paths(
                v,
                new_prefix,
                max_items_per_list=max_items_per_list,
                use_wildcards=use_wildcards,
            )

    elif isinstance(obj, list):
        if not obj:
            # Still yield the list location if it's empty
            return

        # Inspect at most N items
        n = min(len(obj), max_items_per_list)

        if use_wildcards:
            list_prefix = f"{prefix}[*]" if prefix else "[*]"
            yield list_prefix
            # sample first item only for structure discovery (common use-case)
            yield from iter_json_paths(
                obj[0],
                list_prefix,
                max_items_per_list=max_items_per_list,
                use_wildcards=use_wildcards,
            )
        else:
            for i in range(n):
                item_prefix = f"{prefix}[{i}]" if prefix else f"[{i}]"
                yield item_prefix
                yield from iter_json_paths(
                    obj[i],
                    item_prefix,
                    max_items_per_list=max_items_per_list,
                    use_wildcards=use_wildcards,
                )

    else:
        # scalar -> no further keys
        return


def collect_unique_paths(
    obj: Any,
    *,
    max_items_per_list: int,
    use_wildcards: bool,
) -> List[str]:
    """
    Collect and return sorted unique paths.
    """
    seen: Set[str] = set()
    for p in iter_json_paths(
        obj,
        prefix="",
        max_items_per_list=max_items_per_list,
        use_wildcards=use_wildcards,
    ):
        seen.add(p)

    return sorted(seen)


def main() -> int:
    parser = argparse.ArgumentParser(description="List nested key paths from a JSON file.")
    parser.add_argument("json_path", type=str, help="Path to the JSON file.")
    parser.add_argument(
        "--max-items",
        type=int,
        default=5,
        help="Max list items to inspect per array (default: 5).",
    )
    parser.add_argument(
        "--wildcards",
        action="store_true",
        help="Use [*] for lists instead of [0], [1], ...",
    )
    parser.add_argument(
        "--out",
        type=str,
        default="",
        help="Optional output file path. If omitted, prints to stdout.",
    )
    args = parser.parse_args()

    json_path = Path(args.json_path)
    if not json_path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path.resolve()}")

    payload = load_json(json_path)
    paths = collect_unique_paths(
        payload,
        max_items_per_list=args.max_items,
        use_wildcards=args.wildcards,
    )

    output_text = "\n".join(paths) + "\n"

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output_text, encoding="utf-8", newline="\n")
        print(f"Wrote {len(paths)} paths to: {out_path.resolve()}")
    else:
        print(output_text, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())