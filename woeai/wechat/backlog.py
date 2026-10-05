"""Registry-backed, legacy-compatible WeChat selected-paper readers.

The CSL registry owns workflow state. YAML parsing remains only for older
standalone fixtures/checkouts that have no registry, never as a fallback for
an invalid registry or a stale generated view.
"""

from __future__ import annotations

import json
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
    wechat_status: str = ""


_ITEM_RE = re.compile(r"\s*-\s+publication_ref:\s+(\S+)\s*$")


def find_registry_root(backlog_path: Path) -> Path | None:
    """Find the registry in an ancestor, even if its generated view is absent."""
    path = backlog_path.resolve()
    for candidate in (path, *path.parents):
        if (candidate / "docs/data/publications.json").is_file():
            return candidate
    return None


def _string_value(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, (bool, list, dict)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def _registry_backlog_items(backlog_path: Path) -> list[dict[str, str]] | None:
    root = find_registry_root(backlog_path)
    if root is None:
        return None
    from woeai.publications.registry import backlog_row, load_registry

    selected = []
    for index, record in enumerate(load_registry(root)):
        custom = record.get("custom", {})
        wechat = custom.get("wechat", {})
        if wechat.get("selected") is not True:
            continue
        # Legacy metadata is for compatibility, never authority. Private remote
        # identifiers must not leak through the public backlog interface.
        item = {
            key: _string_value(value)
            for key, value in wechat.get("legacy_backlog", {}).items()
            if "media_id" not in key.lower() and "mediaid" not in key.lower()
        }
        item.update({key: _string_value(value) for key, value in backlog_row(record).items()})
        order = wechat.get("selection_order", custom.get("order", 0))
        selected.append((order, index, item))
    return [item for _, _, item in sorted(selected, key=lambda row: row[:2])]


def _unquote(value: str) -> str:
    return value.strip().strip('"').strip("'")


def _parse_original_year(value: str) -> int:
    try:
        return int(value or "0")
    except ValueError:
        return 0


def _build_backlog_paper(current: dict[str, str] | None, order: int) -> BacklogPaper | None:
    if not current or not current.get("publication_ref"):
        return None
    return BacklogPaper(
        publication_ref=current.get("publication_ref", ""),
        title=current.get("title", ""),
        research_family=current.get("research_family", ""),
        subdirection=current.get("subdirection", ""),
        original_year=_parse_original_year(current.get("original_year", "0")),
        latest_published_url=current.get("latest_published_url", ""),
        order=order,
        wechat_status=current.get("wechat_status", ""),
    )


def parse_backlog_papers(backlog_path: Path) -> list[BacklogPaper]:
    """Read selected registry records, or a standalone legacy YAML-ish list.

    Returns an empty list if the file does not exist.
    """
    items = _registry_backlog_items(backlog_path)
    if items is not None:
        return [
            paper for order, item in enumerate(items)
            if (paper := _build_backlog_paper(item, order)) is not None
        ]
    if not backlog_path.exists():
        return []
    papers: list[BacklogPaper] = []
    current: dict[str, str] | None = None
    order = -1

    for raw in backlog_path.read_text(encoding="utf-8").splitlines():
        item_match = _ITEM_RE.match(raw)
        if item_match:
            paper = _build_backlog_paper(current, order)
            if paper is not None:
                papers.append(paper)
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
    paper = _build_backlog_paper(current, order)
    if paper is not None:
        papers.append(paper)
    return papers


def read_backlog_item(backlog_path: Path, publication_ref: str) -> dict[str, str]:
    """Return a string-valued compatibility dict for one selected paper."""
    items = _registry_backlog_items(backlog_path)
    if items is not None:
        return next((item for item in items if item["publication_ref"] == publication_ref), {})
    if not backlog_path.exists():
        return {}
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
    items = _registry_backlog_items(backlog_path)
    if items is not None:
        return [item["publication_ref"] for item in items]
    if not backlog_path.exists():
        return []
    refs: list[str] = []
    for raw in backlog_path.read_text(encoding="utf-8").splitlines():
        match = _ITEM_RE.match(raw)
        if match:
            refs.append(match.group(1))
    return refs


def rank_against_target(paper: BacklogPaper, target: BacklogPaper) -> tuple[int, int, int]:
    """Sort key: prefer same subdirection, then newer year, then backlog order.

    Used by both the RTD related-links builder and the WeChat related-papers
    builder to rank sibling papers. Previously duplicated inline as a
    ``candidate_rank`` closure in both scripts.
    """
    same_subdirection = paper.subdirection == target.subdirection
    return (0 if same_subdirection else 1, -paper.original_year, paper.order)
