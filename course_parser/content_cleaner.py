from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .html_to_md import html_to_markdown as _html_to_markdown


@dataclass(frozen=True)
class CleanOptions:
    """
    Wrapper options for course content cleaning.

    Notes:
    - This keeps the interface you already started using:
        from course_parser.content_cleaner import html_to_markdown
        body_md = html_to_markdown(topic.get("body", ""))
    - Extend this later if you want per-topic behaviors (e.g. keep URLs, keep images).
    """
    drop_placeholder_links: bool = True  # currently handled inside html_to_md
    normalize_whitespace: bool = True    # currently handled inside html_to_md


def html_to_markdown(raw_html: str | None, options: Optional[CleanOptions] = None) -> str:
    """
    Public wrapper around html_to_md.html_to_markdown.

    Args:
        raw_html: HTML (or None) from slug payload.
        options: Reserved for future behavior flags.

    Returns:
        Markdown string.
    """
    _ = options or CleanOptions()
    return _html_to_markdown(raw_html)