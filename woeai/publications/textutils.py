"""Pure text-processing helpers and shared constants for publication rendering.

These functions have no data-source or network dependency - they transform
strings and authors. They are shared between the chronological and thematic
publication views and were previously inlined in
``scripts/update-publications-from-zotero.py``.
"""

from __future__ import annotations

import html
import re
import unicodedata
from typing import Any


class ZoteroError(RuntimeError):
    """Raised when the local Zotero API cannot provide required data."""


# Shared publication constants (single source of truth).
METRIC_LABELS = ("影响因子", "中科院分区", "引用次数")
GROUP_LEADER_AUTHOR_NAMES = ("Li Chao", "Chao Li", "李朝", "朝 李")
CORRESPONDING_AUTHOR_LABELS = ("通讯作者", "corresponding author", "corresponding authors")
EARLY_PUBLICATION_CUTOFF_YEAR = 2019
EARLIER_PUBLICATIONS_TITLE = "更早 Earlier"
DEGREE_THESIS_GROUPS = (
    ("phd", "博士学位论文 PhD Theses"),
    ("master", "硕士学位论文 Master Theses"),
)

PINYIN_SURNAMES = {
    "陈": "chen",
    "冯": "feng",
    "李": "li",
    "梁": "liang",
    "刘": "liu",
    "裴": "pei",
    "滕": "teng",
    "王": "wang",
    "肖": "xiao",
    "向": "xiang",
    "杨": "yang",
    "张": "zhang",
    "赵": "zhao",
    "郑": "zheng",
    "周": "zhou",
}

CHINESE_INITIALS = {
    "大": "D",
    "学": "X",
    "清": "Q",
    "华": "H",
    "报": "B",
    "自": "Z",
    "然": "R",
    "科": "K",
    "版": "B",
    "船": "C",
    "舶": "B",
    "工": "G",
    "程": "C",
    "业": "Y",
    "建": "J",
    "筑": "Z",
    "核": "H",
    "与": "Y",
    "太": "T",
    "阳": "Y",
    "能": "N",
    "技": "J",
    "术": "S",
    "力": "L",
    "抗": "K",
    "震": "Z",
    "加": "J",
    "固": "G",
    "改": "G",
    "造": "Z",
    "南": "N",
    "理": "L",
    "武": "W",
    "汉": "H",
}

JOURNAL_INITIALISM_OVERRIDES = {
    "Advances in Bridge Engineering": "ABE",
    "Applied Energy": "AE",
    "Applied Sciences": "AS",
    "Atmospheric Research": "AR",
    "Building and Environment": "BE",
    "Building Simulation": "BS",
    "Energies": "E",
    "Engineering Structures": "ES",
    "Environmental Fluid Mechanics": "EFM",
    "European Journal of Mechanics - B/Fluids": "EJMBF",
    "Journal of Building Engineering": "JBE",
    "Journal of Computational Physics": "JCP",
    "Journal of Renewable and Sustainable Energy": "JRSE",
    "Journal of Wind Engineering and Industrial Aerodynamics": "JWEIA",
    "Marine Structures": "MS",
    "Mathematical Problems in Engineering": "MPE",
    "Ocean Engineering": "OE",
    "Physics of Fluids": "POF",
    "Renewable Energy": "RE",
    "Ships and Offshore Structures": "SOS",
    "Structural Control and Health Monitoring": "SCHM",
    "Structures": "S",
    "Sustainable Cities and Society": "SCS",
    "Wind and Structures an International Journal": "WAS",
    "Wind and Structures An International Journal": "WAS",
    "大学": "DX",
    "清华大学学报（自然科学版）": "QHDXXB",
    "清华大学学报(自然科学版)": "QHDXXB",
    "船舶工程": "CBGC",
    "工业建筑": "GYJZ",
    "核科学与工程": "HKXYGC",
    "太阳能学报": "TYNXB",
    "科学技术与工程": "KXJSYGC",
    "工程力学": "GCLX",
    "工程抗震与加固改造": "GCKZYGJGZ",
    "华南理工大学学报(自然科学版)": "HNLGDXXB",
    "华南理工大学学报（自然科学版）": "HNLGDXXB",
    "武汉理工大学学报": "WHLGDXXB",
}


def extract_year(raw: str | None) -> int:
    match = re.search(r"(\d{4})", raw or "")
    return int(match.group(1)) if match else 0


def parse_date(raw: str | None) -> tuple[int, int, int]:
    if not raw:
        return (0, 0, 0)
    match = re.search(r"(\d{4})(?:[-/年.](\d{1,2}))?(?:[-/月.](\d{1,2}))?", raw)
    if not match:
        return (0, 0, 0)
    year = int(match.group(1))
    month = int(match.group(2)) if match.group(2) else 0
    day = int(match.group(3)) if match.group(3) else 0
    return (year, month, day)


def normalize_title(value: str | None) -> str:
    value = html.unescape(value or "").lower()
    value = re.sub(r"<[^>]+>", "", value)
    value = unicodedata.normalize("NFKC", value)
    value = re.sub(r"[^\w\u4e00-\u9fff]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def normalize_doi(value: str | None) -> str:
    if not value:
        return ""
    value = value.strip().lower()
    value = re.sub(r"^https?://(dx\.)?doi\.org/", "", value)
    return value.rstrip(". ")


def contains_cjk(value: str) -> bool:
    return any("\u4e00" <= char <= "\u9fff" for char in value)


def slug(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-")
    return value.lower() or "x"


def chinese_initialism(value: str) -> str:
    chars = []
    for char in value:
        if "\u4e00" <= char <= "\u9fff":
            chars.append(CHINESE_INITIALS.get(char, "X"))
    return "".join(chars) or "ZH"


def rst_escape(value: str) -> str:
    value = value.replace("\\", "\\\\")
    value = value.replace("*", "\\*")
    return value


def strip_bib_html(value: str) -> str:
    value = re.sub(r"<style.*?</style>", "", value, flags=re.S)
    value = re.sub(r"<[^>]+>", "", value)
    value = html.unescape(value)
    value = value.replace("\xa0", " ")
    value = " ".join(value.split())
    value = re.sub(r"^\[\d+\]\s*", "", value)
    value = value.replace(" 📊", "")
    value = re.sub(
        r"https://doi\.org/https?://doi\.org/",
        "https://doi.org/",
        value,
        flags=re.I,
    )
    return value


def split_extra_tokens(value: str | None) -> list[str]:
    return [token.strip() for token in re.split(r"[、,，;；\n\r]+", value or "") if token.strip()]
