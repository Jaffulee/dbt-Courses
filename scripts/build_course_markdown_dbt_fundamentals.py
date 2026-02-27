from __future__ import annotations

from pathlib import Path

from course_parser.io_utils import read_json, write_text, ensure_dir
from course_parser.slug_loader import load_slug_payload
from course_parser.captions_loader import load_captions_index
from course_parser.course_structure import build_render_lessons
from course_parser.markdown_render import render_full_course_markdown


def main() -> None:
    course_dir = Path(r"response\dbt Fundamentals")
    slug_path = course_dir / "slug" / "dbt Fundamentals.json"

    # Output base
    out_dir = Path(r"dbt Scripts\dbt Fundamentals")
    ensure_dir(out_dir)

    slug_payload = load_slug_payload(read_json(slug_path))

    captions_index = load_captions_index(
        captions_root=course_dir,
        slug_subdir_name="slug",
    )

    lessons = build_render_lessons(
        payload=slug_payload,
        captions_index=captions_index,
    )

    result = render_full_course_markdown(
        course_title=slug_payload.course_title,
        course_description_md=slug_payload.course_description_md,
        lessons=lessons,
        source_slug_json_path=str(slug_path),
        source_captions_dir=str(course_dir),
    )

    out_path = out_dir / "dbt Fundamentals (dbt Studio).md"
    write_text(out_path, result.markdown)

    # Optional: also write ToC-only file for quick inspection
    toc_path = out_dir / "Contents.md"
    write_text(toc_path, result.toc_markdown)

    print("Wrote:", out_path)
    print("Wrote:", toc_path)
    print("Lessons rendered:", len(lessons))
    print("Captions indexed:", len(captions_index))


if __name__ == "__main__":
    main()