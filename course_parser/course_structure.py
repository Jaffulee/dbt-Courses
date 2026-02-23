from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .slug_loader import CoursePayload, Lesson, TopicContent
from .captions_loader import CaptionsForMedia


@dataclass(frozen=True)
class RenderTopic:
    type: str
    title: str | None
    body_md: str
    captions_md: str  # already formatted for markdown (or "")
    asset: str | None = None


@dataclass(frozen=True)
class RenderLesson:
    section_title: str
    lesson_title: str
    lesson_slug: str | None
    topics: list[RenderTopic]


def _captions_to_md(c: CaptionsForMedia) -> str:
    # No commentary: just text blocks. Keep simple.
    lines: list[str] = []
    for chunk in c.chunks:
        if chunk.text.strip():
            lines.append(chunk.text.strip())
    return "\n\n".join(lines).strip()


def build_render_lessons(
    payload: CoursePayload,
    captions_index: dict[str, CaptionsForMedia],
) -> list[RenderLesson]:
    """
    Build a fully ordered render-ready structure:
    Section order -> lesson order -> topic order.

    Video topics will include captions if available.
    """
    lessons_out: list[RenderLesson] = []

    for section in payload.sections:
        section_title = section.title

        for lesson_id in section.lesson_ids:
            lesson: Lesson | None = payload.lessons_by_id.get(lesson_id)
            if lesson is None:
                continue

            render_topics: list[RenderTopic] = []
            for tref in lesson.topics:
                tcontent: TopicContent | None = payload.topics_by_id.get(tref.id)
                if tcontent is None:
                    continue

                # Prefer topic title if present, otherwise none
                topic_title = tcontent.title.strip() if isinstance(tcontent.title, str) else None
                body_md = (tcontent.body_md or "").strip()

                captions_md = ""
                if tcontent.type == "video" and tcontent.asset:
                    cap = captions_index.get(tcontent.asset)
                    if cap:
                        captions_md = _captions_to_md(cap)

                render_topics.append(
                    RenderTopic(
                        type=tcontent.type,
                        title=topic_title,
                        body_md=body_md,
                        captions_md=captions_md,
                        asset=tcontent.asset,
                    )
                )

            lessons_out.append(
                RenderLesson(
                    section_title=section_title,
                    lesson_title=lesson.title,
                    lesson_slug=lesson.slug,
                    topics=render_topics,
                )
            )

    return lessons_out