"""WOEAI research taxonomy - the single source of truth.

CONTEXT.md locks the public Research Family taxonomy: exactly two first-level
families, a fixed set of second-level subdirections, a fixed order. Before this
module existed, the same constants were copied byte-for-byte across three files
(``scripts/update-publications-from-zotero.py``, ``tools/publications/artifacts.py``,
``tests/test_publications_research_view.py``). Every site must now import from
here so the taxonomy cannot drift.
"""

from __future__ import annotations

RESEARCH_FAMILY_ORDER = ("建筑结构抗风", "海上漂浮风电")
RESEARCH_SUBDIRECTION_ORDER = {
    "建筑结构抗风": ("数值风洞与湍动入流", "高层建筑抗风与优化"),
    "海上漂浮风电": (
        "浮式风机系统一体化分析与优化",
        "浮式混凝土平台结构设计",
        "数值风浪流水池",
    ),
}
