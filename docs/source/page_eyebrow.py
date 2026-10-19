"""Split a bilingual reader-page title into an English eyebrow plus a Chinese h1.

Every top-level reader page is titled "中文 English" (科研方向 Research,
学术成果 Academic Outputs, …). Rendering both halves as one h1 makes them compete
for the same weight and, on a 390px screen, wraps the heading onto two lines
before any body text appears. The homepage already uses the opposite pattern —
English eyebrow, Chinese heading — so this hook applies it to the reader pages
without touching the RST titles: anchors, sidebar labels and search results all
keep the bilingual string.
"""
from __future__ import annotations

import re

HEADERLINK = re.compile(r'<a class="headerlink".*?</a>', re.S)
H1 = re.compile(r"<h1>(.*?)</h1>", re.S)
# A CJK head, then a trailing run of Latin words separated by one space.
BILINGUAL = re.compile(
    r"^(?P<cn>.*?[\u4e00-\u9fff])\s+(?P<en>[A-Za-z][A-Za-z0-9 &/.,\-·]*)$"
)


def split_bilingual_title(label: str) -> tuple[str, str] | None:
    """Return ``(chinese, ENGLISH)`` for "中文 English", else ``None``."""
    match = BILINGUAL.match(label.strip())
    if not match:
        return None
    chinese = match.group("cn").strip()
    english = match.group("en").strip()
    if not chinese or not english:
        return None
    return chinese, english.upper()


def rewrite_first_heading(body: str) -> str:
    """Move the English half of the first h1 into a ``page-eyebrow`` line."""
    match = H1.search(body)
    if not match:
        return body
    inner = match.group(1)
    link = HEADERLINK.search(inner)
    label = inner[: link.start()] if link else inner
    parts = split_bilingual_title(label)
    if not parts:
        return body
    chinese, english = parts
    anchor = link.group(0) if link else ""
    replacement = f'<p class="page-eyebrow">{english}</p><h1>{chinese}{anchor}</h1>'
    return body[: match.start()] + replacement + body[match.end() :]


def _rewrite_page_body(app, pagename, templatename, context, doctree):
    body = context.get("body")
    if not body:
        return
    rewritten = rewrite_first_heading(body)
    if rewritten != body:
        context["body"] = rewritten


def setup(app):
    app.connect("html-page-context", _rewrite_page_body)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
