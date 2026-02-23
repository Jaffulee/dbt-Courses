from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import re

from .course_structure import RenderLesson


def _slugify_anchor(text: str) -> str:
    """
    GitHub-style-ish anchor slugification.
    """
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)   # remove punctuation
    s = re.sub(r"\s+", "-", s)       # spaces -> hyphens
    s = re.sub(r"-{2,}", "-", s)
    return s


def _make_unique_anchors(headings: list[str]) -> dict[str, str]:
    """
    Given headings, return mapping heading -> unique anchor.
    If duplicates exist, append -2, -3, etc.
    """
    seen: dict[str, int] = {}
    out: dict[str, str] = {}
    for h in headings:
        base = _slugify_anchor(h)
        n = seen.get(base, 0) + 1
        seen[base] = n
        out[h] = base if n == 1 else f"{base}-{n}"
    return out


@dataclass(frozen=True)
class CourseMarkdownResult:
    markdown: str
    toc_markdown: str


def render_full_course_markdown(
    course_title: str,
    course_description_md: str,
    lessons: list[RenderLesson],
    source_slug_json_path: str,
    source_captions_dir: str,
) -> CourseMarkdownResult:
    """
    Render a full course markdown including nested ToC and all content.

    Output rules:
      - No commentary in the main content.
      - Small metadata footer only.
    """
    # Build headings list for anchors
    # H2: Section title
    # H3: Lesson title (prefixed by section to reduce collisions)
    section_headings: list[str] = []
    lesson_headings: list[str] = []

    for l in lessons:
        if l.section_title not in section_headings:
            section_headings.append(l.section_title)
        lesson_headings.append(f"{l.section_title} / {l.lesson_title}")

    anchors = _make_unique_anchors(section_headings + lesson_headings)

    # Build ToC (nested)
    toc_lines: list[str] = []
    toc_lines.append("## Contents\n")

    current_section: str | None = None
    for l in lessons:
        if l.section_title != current_section:
            current_section = l.section_title
            sec_anchor = anchors[l.section_title]
            toc_lines.append(f"- [{l.section_title}](#{sec_anchor})")
        lesson_key = f"{l.section_title} / {l.lesson_title}"
        les_anchor = anchors[lesson_key]
        toc_lines.append(f"  - [{l.lesson_title}](#{les_anchor})")

    toc_md = "\n".join(toc_lines).strip()

    # Build content
    out: list[str] = []
    out.append(f"# {course_title}".strip())
    out.append("")
    if course_description_md.strip():
        out.append(course_description_md.strip())
        out.append("")

    out.append(toc_md)
    out.append("")

    rendered_sections: set[str] = set()

    for l in lessons:
        if l.section_title not in rendered_sections:
            rendered_sections.add(l.section_title)
            sec_anchor = anchors[l.section_title]
            out.append(f"## {l.section_title}")
            out.append(f"<a id=\"{sec_anchor}\"></a>")
            out.append("")

        lesson_key = f"{l.section_title} / {l.lesson_title}"
        les_anchor = anchors[lesson_key]
        out.append(f"### {l.lesson_title}")
        out.append(f"<a id=\"{les_anchor}\"></a>")
        out.append("")

        for t in l.topics:
            # Topic heading level kept modest for later concatenation stability
            if t.title:
                out.append(f"#### {t.title}")
                out.append("")
            # Body first
            if t.body_md.strip():
                out.append(t.body_md.strip())
                out.append("")
            # Captions appended when present
            if t.captions_md.strip():
                label = "Extracted captions from video:"
                if t.title:
                    label = f"Extracted captions from video: {t.title}"
                out.append(label)
                out.append("")
                out.append(t.captions_md.strip())
                out.append("")
            # If this topic is a PDF viewer, include the asset link explicitly
            if t.type.lower() == "pdfviewer" and t.asset:
                link_text = t.title.strip() if t.title else "Open PDF"
                out.append(f"[{link_text} (PDF)]({t.asset})")
                out.append("")
                out.append("The above link may not work due to insufficient permissions via accessing content in an s3 bucket. In this case, please access the content directly via the course itself.")
                out.append("")

    # Metadata footer (small)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    out.append("---")
    out.append("")
    out.append("### Metadata")
    out.append("")
    out.append(f"- Course: {course_title}")
    out.append(f"- Generated (UTC): {generated_at}")
    out.append(f"- Source slug JSON: {source_slug_json_path}")
    out.append(f"- Source captions dir: {source_captions_dir}")

    return CourseMarkdownResult(markdown="\n".join(out).strip() + "\n", toc_markdown=toc_md + "\n")