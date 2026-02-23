from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def read_json(path: str | Path) -> Any:
    """
    Read and parse JSON from a file.

    Raises:
        ValueError: if the JSON cannot be parsed (includes the file path).
    """
    p = Path(path)
    try:
        with p.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in file: {p} ({e})") from e


def ensure_dir(path: Path) -> None:
    """
    Ensure a directory exists.

    Args:
        path: Directory path.
    """
    path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, text: str) -> None:
    """
    Write UTF-8 text to a file, creating parent directories if needed.

    Args:
        path: File path.
        text: File contents.
    """
    ensure_dir(path.parent)
    path.write_text(text, encoding="utf-8")


def list_json_files(root: Path, recursive: bool = True) -> list[Path]:
    """
    List .json files under a directory.

    Args:
        root: Directory to scan.
        recursive: If True, scan recursively.

    Returns:
        List of JSON file paths.
    """
    pattern = "**/*.json" if recursive else "*.json"
    return sorted([p for p in root.glob(pattern) if p.is_file()])