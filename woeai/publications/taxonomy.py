"""WOEAI research taxonomy - the single source of truth.

CONTEXT.md locks the public Research Family taxonomy: exactly two first-level
families, a fixed set of second-level subdirections, a fixed order. Before this
module existed, the same constants were copied byte-for-byte across three files
(``scripts/update-publications-from-zotero.py``, ``tools/publications/artifacts.py``,
``tests/test_publications_research_view.py``). Every site must now import from
here so the taxonomy cannot drift.
"""

from __future__ import annotations

RESEARCH_FAMILY_ORDER = ("工程结构抗风", "海上漂浮风电")
RESEARCH_SUBDIRECTION_ORDER = {
    "工程结构抗风": ("数值风洞", "结构抗风"),
    "海上漂浮风电": (
        "一体化分析",
        "混凝土浮体",
        "数值水池",
    ),
}
