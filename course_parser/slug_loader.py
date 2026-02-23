from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .html_to_md import html_to_markdown


@dataclass(frozen=True)
class TopicRef:
    id: str
    type: str  # video / text / pdfViewer / quiz / etc.


@dataclass(frozen=True)
class Lesson:
    id: str
    title: str
    slug: str | None
    section_id: str
    topics: list[TopicRef]


@dataclass(frozen=True)
class Section:
    id: str
    title: str
    lesson_ids: list[str]


@dataclass(frozen=True)
class TopicContent:
    id: str
    type: str
    title: str | None
    lesson_id: str | None
    body_md: str
    asset: str | None  # e.g. videos.asset hashedId for Wistia join


@dataclass(frozen=True)
class CoursePayload:
    course_title: str
    course_slug: str | None
    course_description_md: str
    sections: list[Section]
    lessons_by_id: dict[str, Lesson]
    topics_by_id: dict[str, TopicContent]


def _index_by_id(items: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for it in items:
        _id = it.get("id")
        if isinstance(_id, str):
            out[_id] = it
    return out


def load_slug_payload(slug_json: dict[str, Any]) -> CoursePayload:
    """
    Parse the 'slug' JSON into an ordered course structure and topic content map.

    Ordering:
      - Sections are in the order they appear in slug_json["sections"].
      - Lessons inside a section are in the order section["lessons"].

    Args:
        slug_json: Parsed JSON dict.

    Returns:
        CoursePayload ready for rendering.
    """
    course = slug_json.get("course") or {}
    course_title = str(course.get("title") or "").strip()
    course_slug = course.get("slug")
    course_description_md = html_to_markdown(course.get("description"))

    sections_raw = slug_json.get("sections") or []
    lessons_raw = slug_json.get("lessons") or []

    videos_raw = slug_json.get("videos") or []
    texts_raw = slug_json.get("texts") or []
    pdfs_raw = slug_json.get("pdfViewers") or []
    quizzes_raw = slug_json.get("quizzes") or []

    lessons_by_id: dict[str, Lesson] = {}
    for l in lessons_raw:
        lid = l.get("id")
        if not isinstance(lid, str):
            continue
        topics = []
        for t in (l.get("topics") or []):
            tid = t.get("id")
            ttype = t.get("type")
            if isinstance(tid, str) and isinstance(ttype, str):
                topics.append(TopicRef(id=tid, type=ttype))
        lessons_by_id[lid] = Lesson(
            id=lid,
            title=str(l.get("title") or "").strip(),
            slug=(l.get("slug") if isinstance(l.get("slug"), str) else None),
            section_id=str(l.get("section") or "").strip(),
            topics=topics,
        )

    sections: list[Section] = []
    for s in sections_raw:
        sid = s.get("id")
        if not isinstance(sid, str):
            continue
        lesson_ids = [x for x in (s.get("lessons") or []) if isinstance(x, str)]
        sections.append(Section(id=sid, title=str(s.get("title") or "").strip(), lesson_ids=lesson_ids))

    topics_by_id: dict[str, TopicContent] = {}

    def add_topic(items: list[dict[str, Any]], ttype: str) -> None:
        for it in items:
            tid = it.get("id")
            if not isinstance(tid, str):
                continue
            title = it.get("title") if isinstance(it.get("title"), str) else None
            lesson_id = it.get("lesson") if isinstance(it.get("lesson"), str) else None
            body_md = html_to_markdown(it.get("body"))
            asset = it.get("asset") if isinstance(it.get("asset"), str) else None
            topics_by_id[tid] = TopicContent(
                id=tid,
                type=ttype,
                title=title,
                lesson_id=lesson_id,
                body_md=body_md,
                asset=asset,
            )

    add_topic(videos_raw, "video")
    add_topic(texts_raw, "text")
    add_topic(pdfs_raw, "pdfViewer")
    add_topic(quizzes_raw, "quiz")

    return CoursePayload(
        course_title=course_title,
        course_slug=course_slug if isinstance(course_slug, str) else None,
        course_description_md=course_description_md,
        sections=sections,
        lessons_by_id=lessons_by_id,
        topics_by_id=topics_by_id,
    )