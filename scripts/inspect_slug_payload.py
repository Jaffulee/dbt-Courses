from __future__ import annotations

from pathlib import Path

from course_parser.io_utils import read_json
from course_parser.slug_loader import load_slug_payload


def main() -> None:
    slug_path = Path(r"response\refactoring SQL for modularity\slug\refactoring SQL for modularity.json")
    payload = load_slug_payload(read_json(slug_path))

    print("Course title:", payload.course_title)
    print("Course slug:", payload.course_slug)
    print("Sections:", len(payload.sections))
    print("Lessons:", len(payload.lessons_by_id))
    print("Topics:", len(payload.topics_by_id))
    print()

    # Print ordered syllabus outline (section -> lessons)
    for s in payload.sections:
        print(f"SECTION: {s.title} ({s.id})")
        for lid in s.lesson_ids:
            lesson = payload.lessons_by_id.get(lid)
            if not lesson:
                print(f"  LESSON: <missing> {lid}")
                continue
            print(f"  LESSON: {lesson.title} ({lesson.id}) topics={len(lesson.topics)}")

            # sample first 2 topics
            for tref in lesson.topics[:2]:
                tc = payload.topics_by_id.get(tref.id)
                if not tc:
                    print(f"    TOPIC: {tref.type} {tref.id} <missing content>")
                    continue

                snippet = (tc.body_md[:120] + "...") if tc.body_md and len(tc.body_md) > 120 else (tc.body_md or "")
                print(f"    TOPIC: {tc.type} title={tc.title!r} asset={tc.asset!r}")

                if snippet.strip():
                    snippet_clean = snippet.replace("\n", " ")
                    print(f"      BODY SNIP: {snippet_clean}")
        print()


if __name__ == "__main__":
    main()