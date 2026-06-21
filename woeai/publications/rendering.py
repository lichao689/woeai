"""Citation rendering for WOEAI publication entries.

Composes the ``[N] ...`` rendered citation line from a Zotero ``bib`` string by
applying a fixed sequence of emphasis markers: bold the journal title and
metric values, mark the Student First Author, bold the group leader, and mark
corresponding authors. This was previously inlined in
``scripts/update-publications-from-zotero.py``.
"""

from __future__ import annotations

import re
from typing import Any

from woeai.publications.authors import (
    mark_corresponding_authors,
    mark_student_first_author,
)
from woeai.publications.textutils import (
    METRIC_LABELS,
    journal_initialism,
    rst_escape,
    strip_bib_html,
)


def bold_group_leader(value: str) -> str:
    value = re.sub(r"(?<!\*)\bLi Chao\b(?!\*)", "**Li Chao**", value)
    value = value.replace("李朝", "**李朝**")
    return value


def bold_journal_title(value: str, item: dict[str, Any]) -> str:
    journal = item["data"].get("publicationTitle")
    if not journal:
        return value
    escaped_journal = rst_escape(str(journal))
    marker = f"[J]. {escaped_journal}"
    if marker not in value:
        return value
    return value.replace(marker, f"[J]. **{escaped_journal}**", 1)


def bold_metric_values(value: str) -> str:
    labels = "|".join(re.escape(label) for label in METRIC_LABELS)
    pattern = re.compile(rf"(?P<label>{labels}):\s*(?P<metric>.+?)(?=\.\s*(?:{labels}):|\.$)")

    def replace(match: re.Match[str]) -> str:
        metric = match.group("metric").strip()
        return f"{match.group('label')}: **{metric}**"

    return pattern.sub(replace, value)


def rendered_entry(item: dict[str, Any], number: int) -> str:
    text = strip_bib_html(item.get("bib") or "")
    text = rst_escape(text)
    text = bold_journal_title(text, item)
    text = bold_metric_values(text)
    text = mark_student_first_author(text, item)
    text = bold_group_leader(text)
    text = mark_corresponding_authors(text, item)
    return f"[{number}] {text}"


def paper_deep_dive_citation_link_text(
    publication_year: int, title: str, journal_initialism_text: str = ""
) -> str:
    title = title.strip()
    journal_initialism_text = (journal_initialism_text or "").strip()
    prefix = str(publication_year) if publication_year > 0 else ""
    if journal_initialism_text:
        prefix = f"{prefix} {journal_initialism_text}".strip()
    if not prefix:
        return title
    return f"{prefix} | {title}"
