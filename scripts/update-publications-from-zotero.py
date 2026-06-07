#!/usr/bin/env python3
"""Generate the WOEAI publications page from local Zotero data.

This script is a maintenance tool. It reads the user's local Zotero API,
renders journal articles with the team CSL style, writes the static Sphinx RST
page, and records a JSON snapshot for review. ReadTheDocs builds the committed
RST only; it does not run this script.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS_PATH = ROOT / "docs/source/Publications.rst"
SNAPSHOT_PATH = ROOT / "docs/superpowers/source-packets/2026-06-publications-zotero-snapshot.json"

BASE_URL = "http://127.0.0.1:23119/api/users/0"
API_HEADERS = {"Zotero-API-Version": "3"}
API_LIMIT = 100

CSL_STYLE_ID = "http://www.zotero.org/styles/jm-chinese-std-gb-t-7714-2015-numeric-chinese-lcfav-01"
CSL_SOURCE_PATH = Path(
    "/Users/lichao/Drive/Myfiles/96 常用备份/SoftConfig/zotero/"
    "jm-chinese-std-gb-t-7714-2015-numeric-chinese-lcFav-01.csl"
)
CSL_INSTALLED_PATH = Path(
    "/Users/lichao/Zotero/styles/"
    "jm-chinese-std-gb-t-7714-2015-numeric-chinese-lcfav-01.csl"
)
CSL_SHA256 = "fde99536c18e025299488fe4f65cd6269172d2274e1b48e877e64b24cd52aef1"


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

REPRESENTATIVE_KEYS = {
    "urban_fast": "CGKPKZ8I",
    "urban_satellite": "RLAA46YB",
    "urban_temporal": "XM44D697",
    "urban_gaussian": "V6PLJENN",
    "tall_gnn": "4BCF65NB",
    "tall_extremes": "YZ2D62NB",
    "turbulence_vector": "2YG78T62",
    "turbulence_inflow": "Y76UWP9R",
    "structural_tld": "ES37XMDV",
    "tower_coupling": "UXCUW2AL",
    "offshore_concrete": "EMID6LAJ",
    "offshore_wave": "5W2SZJUT",
    "offshore_model": "TQ9RNRCC",
    "offshore_applied": "3LWVP7B7",
    "offshore_jacket": "5GPZ54VV",
}


class ZoteroError(RuntimeError):
    """Raised when the local Zotero API cannot provide required data."""


def request_json(path: str, params: dict[str, Any] | None = None) -> tuple[list[dict[str, Any]], dict[str, str]]:
    url = BASE_URL + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers=API_HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
            headers = {key.lower(): value for key, value in response.headers.items()}
    except urllib.error.HTTPError as exc:
        raise ZoteroError(f"Zotero API returned HTTP {exc.code} for {url}") from exc
    except urllib.error.URLError as exc:
        raise ZoteroError(f"Cannot reach Zotero local API at {BASE_URL}") from exc
    if not isinstance(payload, list):
        raise ZoteroError(f"Expected a list payload from {url}")
    return payload, headers


def paginated(path: str, params: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    query = dict(params or {})
    query.setdefault("limit", API_LIMIT)
    start = 0
    total: int | None = None
    rows: list[dict[str, Any]] = []
    while True:
        query["start"] = start
        page, headers = request_json(path, query)
        if total is None:
            raw_total = headers.get("total-results")
            total = int(raw_total) if raw_total and raw_total.isdigit() else len(page)
        rows.extend(page)
        start += len(page)
        if not page or start >= total:
            break
    return rows


def read_style_sha256() -> str | None:
    for path in (CSL_INSTALLED_PATH, CSL_SOURCE_PATH):
        if path.exists():
            return hashlib.sha256(path.read_bytes()).hexdigest()
    return None


def verify_style() -> None:
    digest = read_style_sha256()
    if digest != CSL_SHA256:
        raise ZoteroError(
            "Expected CSL style is not available or has changed. "
            f"Expected {CSL_SHA256}, got {digest or 'missing'}."
        )


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


def creator_display_name(creator: dict[str, Any]) -> str:
    if creator.get("name"):
        return str(creator["name"])
    return " ".join(part for part in [creator.get("firstName"), creator.get("lastName")] if part)


def creator_family_token(creator: dict[str, Any]) -> str:
    family = creator.get("lastName") or creator.get("name") or ""
    if not family and creator.get("firstName"):
        family = str(creator["firstName"])
    family = str(family).strip()
    if contains_cjk(family):
        first = family[0]
        return PINYIN_SURNAMES.get(first, f"zh{ord(first):x}")
    token = family.split()[-1] if family.split() else "unknown"
    return slug(token)


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


def journal_initialism(title: str | None) -> str:
    title = (title or "").strip()
    if title in JOURNAL_INITIALISM_OVERRIDES:
        return JOURNAL_INITIALISM_OVERRIDES[title]
    if contains_cjk(title):
        return chinese_initialism(title)
    words = re.findall(r"[A-Za-z0-9]+", title)
    if not words:
        return "J"
    return "".join(word[0].upper() for word in words)


def short_title_token(title: str | None) -> str:
    words = re.findall(r"[A-Za-z0-9]+", unicodedata.normalize("NFKD", title or ""))
    stop = {"a", "an", "and", "for", "in", "of", "on", "the", "to", "using", "with"}
    for word in words:
        if word.lower() not in stop and len(word) > 2:
            return slug(word)
    if contains_cjk(title or ""):
        return "t" + hashlib.sha1((title or "").encode("utf-8")).hexdigest()[:6]
    return "paper"


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


def rst_escape(value: str) -> str:
    value = value.replace("\\", "\\\\")
    value = value.replace("*", "\\*")
    return value


def bold_group_leader(value: str) -> str:
    value = re.sub(r"(?<!\*)\bLi Chao\b(?!\*)", "**Li Chao**", value)
    value = value.replace("李朝", "**李朝**")
    return value


def rendered_entry(item: dict[str, Any], number: int) -> str:
    text = strip_bib_html(item.get("bib") or "")
    text = rst_escape(text)
    text = bold_group_leader(text)
    return f"[{number}] {text}"


def old_publication_records() -> list[dict[str, str]]:
    if not PUBLICATIONS_PATH.exists():
        return []
    text = PUBLICATIONS_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        r"^\.\. _(?P<anchor>ref-[^:]+):\n\n(?P<entry>\[\d+\].+?)(?=\n\n(?:\.\. _ref-|\d{4}|更早|\Z))",
        flags=re.M | re.S,
    )
    rows = []
    for match in pattern.finditer(text):
        entry = " ".join(match.group("entry").split())
        doi_match = re.search(r"https?://doi\.org/([^\s.]+(?:\.[^\s.]+)*)", entry)
        title_match = re.search(r",\s*(.+?)\[J\]", entry)
        rows.append(
            {
                "anchor": match.group("anchor"),
                "doi": normalize_doi(doi_match.group(1) if doi_match else ""),
                "title": normalize_title(title_match.group(1) if title_match else ""),
            }
        )
    return rows


def assign_anchors(items: list[dict[str, Any]]) -> None:
    seen: dict[str, int] = {}
    for item in items:
        data = item["data"]
        creators = data.get("creators") or []
        first = creator_family_token(creators[0]) if creators else "unknown"
        year = extract_year(data.get("date"))
        journal = journal_initialism(data.get("publicationTitle"))
        base = f"ref-{first}{year}-{journal}"
        count = seen.get(base, 0)
        if count:
            anchor = f"{base}-{short_title_token(data.get('title'))}"
        else:
            anchor = base
        while anchor in seen:
            count += 1
            anchor = f"{base}-{short_title_token(data.get('title'))}-{count}"
        seen[base] = count + 1
        seen[anchor] = 1
        item["anchor"] = anchor


def fetch_publication_items() -> list[dict[str, Any]]:
    all_items = paginated("/items/top", {"include": "data"})
    keys = [
        item["key"]
        for item in all_items
        if item.get("data", {}).get("inPublications") is True
        and item.get("data", {}).get("itemType") == "journalArticle"
    ]
    if not keys:
        raise ZoteroError("No Zotero My Publications journalArticle items found.")

    enriched: list[dict[str, Any]] = []
    for index in range(0, len(keys), 50):
        chunk = keys[index : index + 50]
        params = {
            "itemKey": ",".join(chunk),
            "include": "data,bib",
            "style": CSL_STYLE_ID,
            "limit": 100,
        }
        enriched.extend(paginated("/items/top", params))

    enriched = [
        item
        for item in enriched
        if item.get("data", {}).get("inPublications") is True
        and item.get("data", {}).get("itemType") == "journalArticle"
    ]
    enriched.sort(
        key=lambda item: (
            -parse_date(item["data"].get("date"))[0],
            -parse_date(item["data"].get("date"))[1],
            -parse_date(item["data"].get("date"))[2],
            normalize_title(item["data"].get("title")),
        )
    )
    assign_anchors(enriched)
    total = len(enriched)
    for index, item in enumerate(enriched):
        item["publication_number"] = total - index
    return enriched


def build_lookup(items: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {item["key"]: item for item in items}


def ref_for(items_by_key: dict[str, dict[str, Any]], key_name: str, label: str) -> str:
    item = items_by_key[REPRESENTATIVE_KEYS[key_name]]
    return f":ref:`[{item['publication_number']}] {label} <{item['anchor']}>`"


def page_header(items_by_key: dict[str, dict[str, Any]]) -> str:
    highlights = [
        "- AI 与城市风模拟: "
        + "、".join(
            [
                ref_for(items_by_key, "urban_fast", "precomputed CFD database for urban microscale wind"),
                ref_for(items_by_key, "urban_satellite", "satellite-imagery urban geometry reconstruction"),
                ref_for(items_by_key, "urban_gaussian", "3D Gaussian Splatting building geometry"),
            ]
        )
        + "。",
        "- AI 与结构响应预测: "
        + "、".join(
            [
                ref_for(items_by_key, "tall_gnn", "graph neural networks for tall-building response"),
                ref_for(items_by_key, "tall_extremes", "2D vectorial response extremes"),
            ]
        )
        + "。",
        "- 数值风洞与入流湍流: "
        + "、".join(
            [
                ref_for(items_by_key, "turbulence_vector", "vector-potential random flow generation"),
                ref_for(items_by_key, "turbulence_inflow", "coherence-improved and mass-balanced inflow turbulence"),
            ]
        )
        + "。",
        "- 结构抗风: "
        + "、".join(
            [
                ref_for(items_by_key, "structural_tld", "implanted-pole tuned liquid damper"),
                ref_for(items_by_key, "tower_coupling", "tower-line coupling under strong winds"),
            ]
        )
        + "。",
        "- 海上风电: "
        + "、".join(
            [
                ref_for(items_by_key, "offshore_concrete", "reinforced-concrete semi-submersible platform optimization"),
                ref_for(items_by_key, "offshore_wave", "equivalent static wave loads for semi-submersible turbines"),
                ref_for(items_by_key, "offshore_applied", "floating wind turbine substructure optimization"),
            ]
        )
        + "。",
    ]
    return "\n".join(
        [
            "学术成果 Academic Outputs",
            "===============================",
            "",
            "阅读说明 Notes",
            "---------------",
            "",
            "- **Li Chao** / **李朝** 为便于阅读加粗显示。",
            "- 本页期刊论文按当前公开成果记录生成；影响因子、Q 分区、中科院分区和引用次数等指标仅在来源记录可用时显示。",
            "- Publication Numbers 为当前页面排序下的展示编号；方向页中的论文引用使用稳定锚点链接到本页对应条目。",
            "",
            "精选证据 Selected Highlights",
            "----------------------------",
            "",
            *highlights,
            "",
            "期刊论文 Journal Papers",
            "------------------------",
            "",
        ]
    )


def build_publications_rst(items: list[dict[str, Any]]) -> str:
    items_by_key = build_lookup(items)
    sections = [page_header(items_by_key)]
    current_year: int | None = None
    for item in items:
        data = item["data"]
        year = extract_year(data.get("date"))
        if year != current_year:
            current_year = year
            title = str(year) if year else "更早 Early"
            sections.extend([title, "~" * 12, ""])
        sections.extend(
            [
                f".. _{item['anchor']}:",
                "",
                rendered_entry(item, item["publication_number"]),
                "",
            ]
        )
    return "\n".join(sections).rstrip() + "\n"


def merge_old_anchors(items: list[dict[str, Any]]) -> dict[str, str]:
    old_rows = old_publication_records()
    by_doi = {row["doi"]: row["anchor"] for row in old_rows if row["doi"]}
    by_title = {row["title"]: row["anchor"] for row in old_rows if row["title"]}
    mapping: dict[str, str] = {}
    for item in items:
        data = item["data"]
        old_anchor = ""
        doi = normalize_doi(data.get("DOI"))
        title = normalize_title(data.get("title"))
        if doi and doi in by_doi:
            old_anchor = by_doi[doi]
        elif title and title in by_title:
            old_anchor = by_title[title]
        if old_anchor and old_anchor != item["anchor"]:
            mapping[old_anchor] = item["anchor"]
        item["old_anchor"] = old_anchor
    return mapping


def metrics_text(rendered: str) -> str:
    match = re.search(r"(影响因子:.+|中科院分区:.+|引用次数:.+)$", rendered)
    return match.group(1) if match else ""


def snapshot(items: list[dict[str, Any]], old_anchor_map: dict[str, str]) -> dict[str, Any]:
    return {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "source_boundary": {
            "zotero_filter": {"inPublications": True, "itemType": "journalArticle"},
            "count": len(items),
        },
        "csl_style": {
            "id": CSL_STYLE_ID,
            "source_path": str(CSL_SOURCE_PATH),
            "installed_path": str(CSL_INSTALLED_PATH),
            "sha256": read_style_sha256(),
        },
        "anchor_rule": "ref-{first-author}{year}-{journal-initialism}; collisions append deterministic title token",
        "ordering": "publication year desc, parsed date desc, normalized title asc",
        "old_anchor_map": old_anchor_map,
        "items": [
            {
                "zotero_key": item["key"],
                "publication_number": item["publication_number"],
                "anchor": item["anchor"],
                "old_anchor": item.get("old_anchor") or None,
                "year": extract_year(item["data"].get("date")),
                "date": item["data"].get("date"),
                "title": item["data"].get("title"),
                "publicationTitle": item["data"].get("publicationTitle"),
                "doi": item["data"].get("DOI"),
                "creators": [creator_display_name(creator) for creator in item["data"].get("creators") or []],
                "rendered": strip_bib_html(item.get("bib") or ""),
                "metrics": metrics_text(strip_bib_html(item.get("bib") or "")),
            }
            for item in items
        ],
    }


def write_outputs(args: argparse.Namespace) -> None:
    verify_style()
    items = fetch_publication_items()
    old_anchor_map = merge_old_anchors(items)
    page = build_publications_rst(items)
    snap = snapshot(items, old_anchor_map)

    if args.dry_run:
        print(f"Would write {PUBLICATIONS_PATH}")
        print(f"Would write {SNAPSHOT_PATH}")
        print(f"Items: {len(items)}")
        print(f"Anchor replacements: {len(old_anchor_map)}")
        return

    PUBLICATIONS_PATH.write_text(page, encoding="utf-8")
    SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_PATH.write_text(
        json.dumps(snap, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {PUBLICATIONS_PATH}")
    print(f"Wrote {SNAPSHOT_PATH}")
    print(f"Items: {len(items)}")
    print(f"Anchor replacements: {len(old_anchor_map)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Read Zotero and report without writing files")
    args = parser.parse_args()
    try:
        write_outputs(args)
    except ZoteroError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
