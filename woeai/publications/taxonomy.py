"""WOEAI research taxonomy - the single source of truth.

CONTEXT.md locks the public Research Family taxonomy: exactly two first-level
families, a fixed set of second-level subdirections, a fixed order. Before this
module existed, the same constants were copied byte-for-byte across three files
(``scripts/update-publications-from-zotero.py``, ``tools/publications/artifacts.py``,
``tests/test_publications_research_view.py``). Every site must now import from
here so the taxonomy cannot drift.
"""

from __future__ import annotations

RESEARCH_FAMILY_ORDER = ("工程结构抗风", "海洋能源结构")
RESEARCH_SUBDIRECTION_ORDER = {
    "工程结构抗风": ("数值风洞", "结构抗风"),
    "海洋能源结构": (
        "一体化分析",
        "混凝土浮体",
        "数值水池",
    ),
}

# Display translations of the same taxonomy; these do not introduce categories.
RESEARCH_FAMILY_EN = {
    "工程结构抗风": "Structural Wind Engineering",
    "海洋能源结构": "Marine Energy Structures",
}
RESEARCH_SUBDIRECTION_EN = {
    "数值风洞": "Numerical Wind Tunnel",
    "结构抗风": "Structural Wind Resistance",
    "一体化分析": "Integrated Analysis",
    "混凝土浮体": "Concrete Floating Structures",
    "数值水池": "Numerical Wave Basin",
}
