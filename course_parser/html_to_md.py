from __future__ import annotations

import html
import re


# --- Helpers ---------------------------------------------------------------

_PRE_BLOCK_RE = re.compile(r"<pre[^>]*>(.*?)</pre\s*>", re.IGNORECASE | re.DOTALL)
_CODE_BLOCK_RE = re.compile(r"<code[^>]*>(.*?)</code\s*>", re.IGNORECASE | re.DOTALL)

# <a href="...">text</a>
_ANCHOR_RE = re.compile(
    r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a\s*>',
    re.IGNORECASE | re.DOTALL,
)

# If href is a placeholder / broken / meaningless, drop the URL but keep the text.
# (These are the exact kinds of things in your excerpt: (first), (.), (**), (.**), etc.)
_BAD_HREF_RE = re.compile(
    r"""^(
        \#|
        first|
        learn|
        \.|
        \*\*|
        \.\*\*|
        javascript:void\(0\)|
        javascript:void\(0\);|
        $
    )$""",
    re.IGNORECASE | re.VERBOSE,
)

# Later: convert any stray [text](first) or [text](.) into just text
_BAD_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((first|learn|\.|\#|\*\*|\.\*\*)\)", re.IGNORECASE)

# Turn code-ish lines into fenced blocks when they look like SQL.
_SQL_LINE_RE = re.compile(
    r"^\s*(select|with|from|where|join|left join|right join|inner join|group by|order by|having|union|create|insert|update|delete)\b",
    re.IGNORECASE,
)


def _strip_tags(text: str) -> str:
    """Remove any remaining HTML tags."""
    return re.sub(r"<[^>]+>", "", text)


def _collapse_ws(s: str) -> str:
    s = re.sub(r"\r\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def _html_inline_to_md(s: str) -> str:
    """
    Convert inline-ish HTML to markdown-ish text (no <pre>/<code> here).
    """
    s = html.unescape(s)

    # Remove images entirely
    s = re.sub(r"<img[^>]*>", "", s, flags=re.IGNORECASE)

    # Headings
    s = re.sub(r"</h1\s*>", "\n\n", s, flags=re.IGNORECASE)
    s = re.sub(r"<h1[^>]*>", "# ", s, flags=re.IGNORECASE)
    s = re.sub(r"</h2\s*>", "\n\n", s, flags=re.IGNORECASE)
    s = re.sub(r"<h2[^>]*>", "## ", s, flags=re.IGNORECASE)
    s = re.sub(r"</h3\s*>", "\n\n", s, flags=re.IGNORECASE)
    s = re.sub(r"<h3[^>]*>", "### ", s, flags=re.IGNORECASE)
    s = re.sub(r"</h4\s*>", "\n\n", s, flags=re.IGNORECASE)
    s = re.sub(r"<h4[^>]*>", "#### ", s, flags=re.IGNORECASE)

    # Paragraphs / line breaks
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.IGNORECASE)
    s = re.sub(r"</p\s*>", "\n\n", s, flags=re.IGNORECASE)
    s = re.sub(r"<p[^>]*>", "", s, flags=re.IGNORECASE)

    # Strong/em
    s = re.sub(r"</strong\s*>", "**", s, flags=re.IGNORECASE)
    s = re.sub(r"<strong[^>]*>", "**", s, flags=re.IGNORECASE)
    s = re.sub(r"</b\s*>", "**", s, flags=re.IGNORECASE)
    s = re.sub(r"<b[^>]*>", "**", s, flags=re.IGNORECASE)
    s = re.sub(r"</em\s*>", "*", s, flags=re.IGNORECASE)
    s = re.sub(r"<em[^>]*>", "*", s, flags=re.IGNORECASE)
    s = re.sub(r"</i\s*>", "*", s, flags=re.IGNORECASE)
    s = re.sub(r"<i[^>]*>", "*", s, flags=re.IGNORECASE)

    # Lists (simple; no nesting)
    s = re.sub(r"</li\s*>", "\n", s, flags=re.IGNORECASE)
    s = re.sub(r"<li[^>]*>", "- ", s, flags=re.IGNORECASE)
    s = re.sub(r"</ul\s*>", "\n", s, flags=re.IGNORECASE)
    s = re.sub(r"<ul[^>]*>", "\n", s, flags=re.IGNORECASE)
    s = re.sub(r"</ol\s*>", "\n", s, flags=re.IGNORECASE)
    s = re.sub(r"<ol[^>]*>", "\n", s, flags=re.IGNORECASE)

    # Links: do them properly here (before stripping tags)
    def _anchor_sub(m: re.Match[str]) -> str:
        href = (m.group(1) or "").strip()
        inner_html = m.group(2) or ""
        text = _strip_tags(inner_html)
        text = html.unescape(text).strip()

        if not text:
            return ""

        # Drop URL if it is clearly placeholder/broken
        if _BAD_HREF_RE.match(href):
            return text

        return f"[{text}]({href})"

    s = _ANCHOR_RE.sub(_anchor_sub, s)

    # Remove any remaining tags
    s = _strip_tags(s)

    # If any broken MD links slipped through, remove the URL but keep the label
    s = _BAD_MD_LINK_RE.sub(r"\1", s)

    return s


def _looks_like_sql(code_text: str) -> bool:
    lines = [ln for ln in code_text.splitlines() if ln.strip()]
    if not lines:
        return False
    # If any non-empty line starts with common SQL keywords, call it SQL.
    return any(_SQL_LINE_RE.match(ln) for ln in lines[:10])


# --- Main converter --------------------------------------------------------


def html_to_markdown(maybe_html: str | None) -> str:
    """
    Convert a small subset of HTML to Markdown.
    Designed for ThoughtIndustries-style bodies in your JSON.

    Improvements:
      - Proper <a href="">text</a> conversion (and removal of placeholder/broken hrefs)
      - Converts <pre><code>...</code></pre> and <code>...</code> to fenced/inline code

    Args:
        maybe_html: HTML string or None.

    Returns:
        Markdown text (no surrounding commentary).
    """
    if not maybe_html:
        return ""

    s = html.unescape(maybe_html)

    # 1) Pull out <pre> blocks first so we don't destroy code formatting
    pre_blocks: list[str] = []

    def _pre_sub(m: re.Match[str]) -> str:
        inner = m.group(1) or ""
        inner = html.unescape(inner)

        # If there is a <code> inside, extract its content; otherwise use inner
        code_m = _CODE_BLOCK_RE.search(inner)
        if code_m:
            code_inner = code_m.group(1) or ""
        else:
            code_inner = inner

        # Strip tags but preserve text/newlines
        code_text = _strip_tags(code_inner)
        code_text = html.unescape(code_text)

        # Normalize newlines inside code
        code_text = re.sub(r"\r\n", "\n", code_text).strip("\n")

        lang = "sql" if _looks_like_sql(code_text) else ""
        fence = f"```{lang}\n{code_text}\n```"
        pre_blocks.append(fence)
        return f"@@PRE_BLOCK_{len(pre_blocks) - 1}@@"

    s = _PRE_BLOCK_RE.sub(_pre_sub, s)

    # 2) Convert remaining inline content, including links
    s = _html_inline_to_md(s)

    # 3) Convert any remaining <code>...</code> outside <pre> into inline code
    # At this point tags are stripped, so we can only do a best-effort if any placeholders remain.
    # However, ThoughtIndustries often has <code> in bodies; we handle it by re-running on original
    # segments would be more complex. Instead, support a conservative inline-code pattern:
    # If the original had <code>, it would have been stripped already; so handle it earlier by:
    # (We do a second pass on the original string before stripping tags for <code> not in <pre>.)

    # To do that, we re-process the original again only for <code> not inside <pre>:
    # Simple approach: replace <code> blocks in the original (with <pre> removed) into tokens.
    s2 = html.unescape(maybe_html)
    s2 = _PRE_BLOCK_RE.sub("", s2)  # remove pre blocks entirely
    code_spans: list[str] = []

    def _code_sub(m: re.Match[str]) -> str:
        inner = m.group(1) or ""
        inner = html.unescape(inner)
        text = _strip_tags(inner)
        text = html.unescape(text).strip()
        if not text:
            return ""
        # backticks inside: escape by using double backticks if needed
        if "`" in text:
            wrapped = f"``{text}``"
        else:
            wrapped = f"`{text}`"
        code_spans.append(wrapped)
        return f"@@CODE_SPAN_{len(code_spans) - 1}@@"

    s2 = _CODE_BLOCK_RE.sub(_code_sub, s2)

    # Now convert s2 (which has @@CODE_SPAN@@ tokens) into md-ish text the same way,
    # and then use it to patch tokens into our output. This keeps span content.
    s2_md = _html_inline_to_md(s2)

    # If the token stream exists, prefer it for code-span tokens by replacing them in the final output.
    # We do token replacement by mapping positions: easiest is just to replace tokens in s2_md
    # and then fall back to replacing in s.
    for i, span in enumerate(code_spans):
        token = f"@@CODE_SPAN_{i}@@"
        # Replace token in whichever string contains it.
        if token in s:
            s = s.replace(token, span)
        if token in s2_md and token not in s:
            # If our main conversion lost the token entirely, merge by replacing in s2_md and use that.
            s2_md = s2_md.replace(token, span)

    # 4) Restore <pre> blocks tokens in s
    for i, fence in enumerate(pre_blocks):
        s = s.replace(f"@@PRE_BLOCK_{i}@@", fence)

    # 5) Final normalize
    s = _collapse_ws(s)

    return s