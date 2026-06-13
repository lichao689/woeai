"""Backlog parsing for WOEAI WeChat paper articles.

Parses ``wechat/backlog/selected-papers.yml`` into typed ``BacklogPaper``
records. Previously this parsing was duplicated (with drifting fields) across
``wechat/tools/markdown_to_rtd.py`` and ``wechat/tools/wechat_draft.py``; both
now import from here.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BacklogPaper:
    """One selected-paper row from the backlog.

    The superset of fields both consumers need. ``latest_published_url`` is
    only used by the WeChat draft path; the RTD converter ignores it.
    """

    publication_ref: str
    title: str
    research_family: str
    subdirection: str
    original_year: int
    latest_published_url: str
    order: int


_ITEM_RE = re.compile(r"\s*-\s+publication_ref:\s+(\S+)\s*$")


def _unquote(value: str) -> str:
    return value.strip().strip('"').strip("'")


def parse_backlog_papers(backlog_path: Path) -> list[BacklogPaper]:
    """Parse the backlog YAML-ish list into BacklogPaper records.

    Returns an empty list if the file does not exist.
    """
    if not backlog_path.exists():
        return []
    papers: list[BacklogPaper] = []
    current: dict[str, str] | None = None
    order = -1

    def finish() -> None:
        if not current or not current.get("publication_ref"):
            return
        try:
            original_year = int(current.get("original_year", "0") or "0")
        except ValueError:
            original_year = 0
        papers.append(
            BacklogPaper(
                publication_ref=current.get("publication_ref", ""),
                title=current.get("title", ""),
                research_family=current.get("research_family", ""),
                subdirection=current.get("subdirection", ""),
                original_year=original_year,
                latest_published_url=current.get("latest_published_url", ""),
                order=order,
            )
        )

    for raw in backlog_path.read_text(encoding="utf-8").splitlines():
        item_match = _ITEM_RE.match(raw)
        if item_match:
            finish()
            order += 1
            current = {"publication_ref": item_match.group(1)}
            continue
        if current is None or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        if key.startswith("-"):
            continue
        current[key] = _unquote(value)
    finish()
    return papers


def read_backlog_item(backlog_path: Path, publication_ref: str) -> dict[str, str]:
    """Return the raw key:value dict for a single backlog item."""
    item: dict[str, str] = {}
    in_item = False
    target_re = re.compile(r"\s*-\s+publication_ref:\s+" + re.escape(publication_ref) + r"\s*$")
    for raw in backlog_path.read_text(encoding="utf-8").splitlines():
        if target_re.match(raw):
            in_item = True
            item["publication_ref"] = publication_ref
            continue
        if in_item and _ITEM_RE.match(raw):
            break
        if in_item and ":" in raw:
            key, value = raw.split(":", 1)
            item[key.strip()] = _unquote(value)
    return item


def read_backlog_publication_refs(backlog_path: Path) -> list[str]:
    """Return just the publication_ref values in order."""
    refs: list[str] = []
    for raw in backlog_path.read_text(encoding="utf-8").splitlines():
        match = _ITEM_RE.match(raw)
        if match:
            refs.append(match.group(1))
    return refs
