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
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


# This script is invoked by absolute path, so the repo root is not guaranteed
# to be on sys.path. Make the local ``woeai`` package importable regardless of
# how the entry point is launched.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from woeai.publications import (  # noqa: E402
    RESEARCH_FAMILY_ORDER,
    RESEARCH_SUBDIRECTION_ORDER,
)

PUBLICATIONS_PATH = ROOT / "docs/source/Publications.rst"
PUBLICATIONS_BY_RESEARCH_PATH = ROOT / "docs/source/PublicationsByResearch.rst"
RESEARCH_MAP_PATH = ROOT / "docs/data/publication-research-map.json"
SNAPSHOT_PATH = ROOT / "docs/superpowers/source-packets/2026-06-publications-zotero-snapshot.json"
DEGREE_THESES_PATH = ROOT / "docs/data/degree-theses.json"
TEACHING_PATH = ROOT / "docs/source/Teaching.rst"
TEACHING_DATA_PATH = ROOT / "docs/data/teaching.json"

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

# Constants and pure text helpers now live in woeai.publications.textutils.
# Re-exported here so the module's public surface (used by tests via
# self.updater.<name>) stays unchanged during the Stage 1 migration.
from woeai.publications.textutils import (  # noqa: E402,F401
    CHINESE_INITIALS,
    CORRESPONDING_AUTHOR_LABELS,
    DEGREE_THESIS_GROUPS,
    EARLIER_PUBLICATIONS_TITLE,
    EARLY_PUBLICATION_CUTOFF_YEAR,
    GROUP_LEADER_AUTHOR_NAMES,
    JOURNAL_INITIALISM_OVERRIDES,
    METRIC_LABELS,
    PINYIN_SURNAMES,
    chinese_initialism,
    contains_cjk,
    creator_csl_display_name,
    creator_display_name,
    extract_year,
    normalize_author_name,
    normalize_doi,
    normalize_title,
    parse_date,
    rst_escape,
    slug,
    split_extra_tokens,
    strip_bib_html,
)
from woeai.publications.authors import (  # noqa: E402,F401
    corresponding_author_display_names,
    explicit_corresponding_author_tokens,
    has_corresponding_author_flag,
    iter_current_student_authors,
    iter_student_records,
    load_degree_thesis_data,
    load_student_author_names,
    mark_corresponding_authors,
    mark_student_first_author,
    rendered_author_variants,
    student_first_author_display,
    student_record_variants,
)
from woeai.publications.rendering import (  # noqa: E402,F401
    bold_group_leader,
    bold_journal_title,
    bold_metric_values,
    paper_deep_dive_citation_link_text,
    rendered_entry,
)

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

TEACHING_PUBLICATION_KEYS = {
    "KT6UR5JW",
}
TEACHING_PUBLICATION_TITLE_KEYWORDS = (
    "教学改革",
    "教改",
    "课程思政",
    "思政建设",
    "思想政治教育",
)


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


def iter_degree_theses(group_key: str) -> list[dict[str, Any]]:
    payload = load_degree_thesis_data()
    theses = payload.get("theses", {})
    if not isinstance(theses, dict):
        return []
    rows = theses.get(group_key, [])
    if not isinstance(rows, list):
        raise ZoteroError(f"Degree thesis group {group_key} must be a list.")
    indexed = [(index, record) for index, record in enumerate(rows) if isinstance(record, dict)]
    indexed.sort(key=lambda pair: (parse_date(str(pair[1].get("date") or "")), pair[0]))
    return [record for _index, record in indexed]


def render_degree_thesis_line(record: dict[str, Any]) -> str:
    name_cn = str(record.get("name_cn") or "").strip()
    name_en = str(record.get("name_en") or "").strip()
    date = str(record.get("date") or "").strip()
    thesis_type = str(record.get("thesis_type") or "").strip()
    title = str(record.get("title") or "").strip()
    destination = str(record.get("destination") or "").strip()
    display_name = f"{name_cn}({name_en})" if name_cn and name_en else name_cn or name_en
    if not all([display_name, date, thesis_type, title]):
        raise ZoteroError(f"Incomplete degree thesis record: {record!r}")
    line = f"- {rst_escape(display_name)}，{rst_escape(date)}，{rst_escape(thesis_type)}：{rst_escape(title)}"
    if destination:
        line += f"；去向：{rst_escape(destination)}"
    return line + "。"


def render_current_student_line(record: dict[str, Any]) -> str:
    name_cn = str(record.get("name_cn") or "").strip()
    name_en = str(record.get("name_en") or "").strip()
    status = str(record.get("status") or "在读").strip()
    display_name = f"{name_cn}({name_en})" if name_cn and name_en else name_cn or name_en
    if not all([display_name, status]):
        raise ZoteroError(f"Incomplete current student record: {record!r}")
    return f"- {rst_escape(display_name)}，{rst_escape(status)}。"


def student_training_section() -> str:
    """Render the numbered H3 subsections (2.1/2.2) of the student-training area.

    Each entry in ``DEGREE_THESIS_GROUPS`` becomes a numbered subsection title
    such as ``2.1 博士生 PhD Students``. The PhD subsection is followed by the
    current doctoral students (在读). This produces only the H3 subsections; the
    enclosing ``2 学生培养 Student Training`` H2 heading is emitted by
    ``build_teaching_rst`` so the section can be reassembled in one place.
    """
    sections: list[str] = []
    for index, (group_key, group_title) in enumerate(DEGREE_THESIS_GROUPS, start=1):
        numbered_title = f"2.{index} {group_title}"
        sections.extend([numbered_title, _underline(numbered_title, "~"), ""])
        records = iter_degree_theses(group_key)
        if not records:
            raise ZoteroError(f"Degree thesis group {group_key} has no records.")
        for record in records:
            sections.append(render_degree_thesis_line(record))
        if group_key == "phd":
            for record in iter_current_student_authors():
                sections.append(render_current_student_line(record))
        sections.append("")
    return "\n".join(sections).rstrip()


def _underline(title: str, char: str, minimum: int = 12) -> str:
    """Return an RST underline of ``char`` matching ``title`` display width.

    CJK characters occupy two columns, so use display width, not character
    count, to avoid Sphinx 'Title underline too short' warnings.
    """
    width = sum(2 if ord(c) >= 0x2E80 else 1 for c in title)
    return char * max(width, minimum)


def load_teaching_courses() -> dict[str, list[dict[str, Any]]]:
    """Read docs/data/teaching.json and return course rows keyed by group."""
    payload = json.loads(TEACHING_DATA_PATH.read_text(encoding="utf-8"))
    courses = payload.get("courses", {})
    if not isinstance(courses, dict):
        raise ZoteroError("teaching.json must contain a 'courses' object.")
    result: dict[str, list[dict[str, Any]]] = {}
    for group_key in ("undergraduate", "graduate"):
        rows = courses.get(group_key, [])
        if not isinstance(rows, list):
            raise ZoteroError(f"teaching.json courses.{group_key} must be a list.")
        validated: list[dict[str, Any]] = []
        for row in rows:
            if not isinstance(row, dict):
                raise ZoteroError(f"teaching.json courses.{group_key} entry must be an object.")
            required = ("title_cn", "major", "term", "period")
            if not all(str(row.get(field) or "").strip() for field in required):
                raise ZoteroError(f"Incomplete teaching course record: {row!r}")
            validated.append(row)
        result[group_key] = validated
    return result


def courses_subsection(title: str, rows: list[dict[str, Any]]) -> str:
    """Render a course H3 subsection as plain body lines with bold titles."""
    sections = [title, _underline(title, "~"), ""]
    for row in rows:
        title_cn = str(row["title_cn"]).strip()
        title_en = str(row.get("title_en") or "").strip()
        head = f"**{title_cn} {title_en}**".strip()
        major = str(row["major"]).strip()
        term = str(row["term"]).strip()
        hours = row.get("hours")
        period = str(row["period"]).strip()
        line = f"{head}，{major}，{term}"
        if hours:
            line += f"，{hours}学时"
        line += f"，{period}。"
        sections.append(line)
        sections.append("")
    return "\n".join(sections).rstrip()


def fetch_teaching_reform_items() -> list[dict[str, Any]]:
    """Fetch teaching-reform publications from Zotero, newest first.

    Selects every journalArticle that ``is_teaching_publication`` flags as a
    teaching-reform paper (by key or title keyword). These papers live in the
    Zotero My Publications library but are deliberately excluded from the
    chronological and research-direction academic-output pages; they surface
    here on the Teaching page instead. Results are sorted newest-first.
    """
    all_items = paginated("/items/top", {"include": "data"})
    keys = [
        item["key"]
        for item in all_items
        if item["data"].get("itemType") == "journalArticle" and is_teaching_publication(item)
    ]
    if not keys:
        raise ZoteroError("No Zotero teaching-reform items found.")

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
        if item["data"].get("itemType") == "journalArticle" and is_teaching_publication(item)
    ]
    enriched.sort(
        key=lambda item: (
            -parse_date(item["data"].get("date"))[0],
            -parse_date(item["data"].get("date"))[1],
            -parse_date(item["data"].get("date"))[2],
            normalize_title(item["data"].get("title")),
        )
    )
    return enriched


def render_teaching_reform_line(item: dict[str, Any]) -> str:
    """Render a teaching-reform publication line without the ``[N]`` number."""
    text = strip_bib_html(item.get("bib") or "")
    text = rst_escape(text)
    text = bold_journal_title(text, item)
    text = bold_group_leader(text)
    text = mark_corresponding_authors(text, item)
    # ``[N]`` is stripped by strip_bib_html already, but rendered_entry adds one;
    # teaching-reform entries do not participate in publication numbering, so
    # guard against any leading bracketed number here.
    text = re.sub(r"^\[\d+\]\s*", "", text)
    return text


def build_teaching_rst(teaching_reform_items: list[dict[str, Any]]) -> str:
    """Assemble the full Teaching page RST."""
    courses = load_teaching_courses()
    page_title = "教育教学 Teaching"
    teaching_title = "1 教学工作 Teaching"
    training_title = "2 学生培养 Student Training"
    undergraduate_title = "1.1 本科生 Undergraduate"
    graduate_title = "1.2 研究生 Graduate"
    reform_numbered_title = "1.3 教改探索 Teaching Reform Exploration"
    sections: list[str] = [
        page_title,
        _underline(page_title, "="),
        "",
        teaching_title,
        _underline(teaching_title, "-"),
        "",
        courses_subsection(undergraduate_title, courses["undergraduate"]),
        "",
        courses_subsection(graduate_title, courses["graduate"]),
        "",
        reform_numbered_title,
        _underline(reform_numbered_title, "~"),
        "",
    ]
    for item in teaching_reform_items:
        sections.append(render_teaching_reform_line(item))
        sections.append("")
    sections.extend(
        [
            training_title,
            _underline(training_title, "-"),
            "",
            student_training_section(),
        ]
    )
    return "\n".join(sections).rstrip() + "\n"


def old_publication_records() -> list[dict[str, str]]:
    if not PUBLICATIONS_PATH.exists():
        return []
    text = PUBLICATIONS_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        r"(?P<label_block>(?:^\.\. _ref-[^:]+:\n\n)+)(?P<entry>\[\d+\].+?)(?=\n\n(?:\.\. _ref-|\d{4}|更早|学位论文|\Z))",
        flags=re.M | re.S,
    )
    rows = []
    for match in pattern.finditer(text):
        entry = " ".join(match.group("entry").split())
        anchors = re.findall(r"^\.\. _(ref-[^:]+):$", match.group("label_block"), flags=re.M)
        doi_match = re.search(r"https?://doi\.org/([^\s.]+(?:\.[^\s.]+)*)", entry)
        title_match = re.search(r",\s*(.+?)\[J\]", entry)
        rows.append(
            {
                "anchor": anchors[0] if anchors else "",
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


def is_teaching_publication(item: dict[str, Any]) -> bool:
    data = item.get("data", {})
    title = str(data.get("title") or "")
    return item.get("key") in TEACHING_PUBLICATION_KEYS or any(
        keyword in title for keyword in TEACHING_PUBLICATION_TITLE_KEYWORDS
    )


def is_public_journal_paper(item: dict[str, Any]) -> bool:
    data = item.get("data", {})
    return (
        data.get("inPublications") is True
        and data.get("itemType") == "journalArticle"
        and not is_teaching_publication(item)
    )


def fetch_publication_items() -> list[dict[str, Any]]:
    all_items = paginated("/items/top", {"include": "data"})
    keys = [item["key"] for item in all_items if is_public_journal_paper(item)]
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

    enriched = [item for item in enriched if is_public_journal_paper(item)]
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


def load_research_map() -> dict[str, dict[str, str]]:
    if not RESEARCH_MAP_PATH.exists():
        raise ZoteroError(f"Publication research map is missing: {RESEARCH_MAP_PATH}")
    try:
        payload = json.loads(RESEARCH_MAP_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ZoteroError(f"Publication research map is invalid JSON: {exc}") from exc
    items = payload.get("items")
    if not isinstance(items, dict):
        raise ZoteroError("Publication research map must contain an object at items.")
    normalized: dict[str, dict[str, str]] = {}
    for key, value in items.items():
        if not isinstance(value, dict):
            raise ZoteroError(f"Publication research map entry for {key} must be an object.")
        normalized[str(key)] = {str(field): str(raw) for field, raw in value.items() if raw is not None}
    return normalized


def validate_research_map(items: list[dict[str, Any]], research_map: dict[str, dict[str, str]]) -> None:
    item_keys = {item["key"] for item in items}
    map_keys = set(research_map)
    errors: list[str] = []

    missing = [item for item in items if item["key"] not in research_map]
    if missing:
        errors.append("Missing publication research mapping:")
        errors.extend(
            f"- {item['key']} | {extract_year(item['data'].get('date'))} | {item['data'].get('title')}"
            for item in missing
        )

    unknown = sorted(map_keys - item_keys)
    if unknown:
        errors.append("Publication research map contains keys not in current Public Journal Papers:")
        errors.extend(f"- {key}" for key in unknown)

    for key in sorted(item_keys & map_keys):
        family = research_map[key].get("research_family", "")
        if family not in RESEARCH_FAMILY_ORDER:
            errors.append(f"{key} has invalid research_family: {family or '<missing>'}")
            continue
        subdirection = research_map[key].get("subdirection", "")
        if subdirection not in RESEARCH_SUBDIRECTION_ORDER[family]:
            errors.append(f"{key} has invalid subdirection for {family}: {subdirection or '<missing>'}")

    if errors:
        raise ZoteroError("\n".join(errors))


def build_lookup(items: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {item["key"]: item for item in items}


def ref_for(items_by_key: dict[str, dict[str, Any]], key_name: str, label: str) -> str:
    item = items_by_key[REPRESENTATIVE_KEYS[key_name]]
    return f":ref:`[{item['publication_number']}] {label} <{item['anchor']}>`"


def page_header(items_by_key: dict[str, dict[str, Any]]) -> str:
    return "\n".join(
        [
            ".. role:: student-first-author",
            "",
            "学术成果 Academic Outputs",
            "===============================",
            "",
            ".. container:: publication-view-banner",
            "",
            "   :doc:`按年份倒序浏览学术成果 Publications by Year <PublicationsByResearch>`：按发表年份倒序浏览完整期刊论文清单。",
            "",
            ".. toctree::",
            "   :hidden:",
            "   :maxdepth: 1",
            "",
            "   按年份倒序浏览 Publications by Year <PublicationsByResearch>",
            "",
            # Keep this no-op include as a guard against the old top-level
            # paper-notes toctree shape. Per-direction paper-note toctrees are
            # emitted under each research subdirection in build_publications_rst.
            ".. include:: _paper-notes-fragment.rst",
            "",
            "期刊论文 Journal Papers",
            "------------------------",
            "",
            "- :student-first-author:`学生第一作者` 表示该论文第一作者为团队在校或毕业学生。",
            "- 作者姓名后的 ``*`` 表示通讯作者。",
            "",
        ]
    )


def publication_anchor_targets(item: dict[str, Any]) -> list[str]:
    targets: list[str] = []
    old_anchor = item.get("old_anchor")
    if old_anchor and old_anchor != item["anchor"]:
        targets.append(str(old_anchor))
    targets.append(str(item["anchor"]))
    return targets


def _read_backlog_zotero_keys(backlog_path: Path) -> dict[str, str]:
    """Return publication_ref -> zotero_key from the backlog."""
    mapping: dict[str, str] = {}
    current_ref = ""
    for raw in backlog_path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*-\s+publication_ref:\s+(\S+)", raw)
        if m:
            current_ref = m.group(1)
            continue
        m = re.match(r"\s*zotero_key:\s+(\S+)", raw)
        if m and current_ref:
            mapping[current_ref] = m.group(1)
    return mapping


def load_deep_dive_titles() -> dict[str, tuple[str, str]]:
    """Return zotero_key -> (publication_ref, reader_title) for papers with deep-dives.

    The reader_title is read from the compact WeChat article H1 (which carries
    the direction-prefixed hook), with the direction prefix stripped.
    """
    backlog_path = ROOT / "wechat/backlog/selected-papers.yml"
    if not backlog_path.exists():
        return {}
    from woeai.wechat.backlog import parse_backlog_papers

    zotero_keys = _read_backlog_zotero_keys(backlog_path)
    key_map: dict[str, tuple[str, str]] = {}
    for paper in parse_backlog_papers(backlog_path):
        article_path = ROOT / f"wechat/articles/draft-public-safe/{paper.publication_ref}.md"
        title = paper.title
        if article_path.exists():
            try:
                from woeai.wechat.review import parse_title
                title = parse_title(article_path.read_text(encoding="utf-8"))
            except RuntimeError:
                pass
        if " | " in title:
            title = title.split(" | ", 1)[1]
        zotero_key = zotero_keys.get(paper.publication_ref)
        if zotero_key:
            key_map[zotero_key] = (paper.publication_ref, title)
    return key_map


def paper_deep_dive_toctree(
    items: list[dict[str, Any]],
    research_map: dict[str, dict[str, str]],
    deep_dive_titles: dict[str, tuple[str, str]],
    family: str,
    subdirection: str,
) -> list[str]:
    entries: list[str] = []
    for item in items:
        row = research_map[item["key"]]
        if row["research_family"] != family or row.get("subdirection") != subdirection:
            continue
        dd = deep_dive_titles.get(item["key"])
        if not dd:
            continue
        pub_ref, dd_title = dd
        entries.append(f"   {dd_title} <paper-notes/{pub_ref}>")
    if not entries:
        return []
    return [
        ".. toctree::",
        "   :hidden:",
        "   :maxdepth: 1",
        "",
        *entries,
        "",
    ]


def build_publications_rst(
    items: list[dict[str, Any]], research_map: dict[str, dict[str, str]]
) -> str:
    deep_dive_titles = load_deep_dive_titles()
    sections = [page_header({})]
    for family in RESEARCH_FAMILY_ORDER:
        sections.extend([family, "-" * 12, ""])
        for subdirection in RESEARCH_SUBDIRECTION_ORDER[family]:
            sections.extend([subdirection, "~" * 40, ""])
            sections.extend(
                paper_deep_dive_toctree(
                    items, research_map, deep_dive_titles, family, subdirection
                )
            )
            for item in items:
                row = research_map[item["key"]]
                if row["research_family"] != family or row.get("subdirection") != subdirection:
                    continue
                for anchor in publication_anchor_targets(item):
                    sections.extend([f".. _{anchor}:", ""])
                entry = rendered_entry(item, item["publication_number"])
                dd = deep_dive_titles.get(item["key"])
                if dd:
                    pub_ref, dd_title = dd
                    number = f"[{item['publication_number']}] "
                    year = extract_year(item["data"].get("date"))
                    link_text = paper_deep_dive_citation_link_text(year, dd_title)
                    dd_link = f":doc:`{link_text} <paper-notes/{pub_ref}>` "
                    entry = entry.replace(number, number + dd_link, 1)
                sections.extend([entry, ""])
    return "\n".join(sections).rstrip() + "\n"


def research_full_entry(item: dict[str, Any]) -> str:
    entry = rendered_entry(item, item["publication_number"])
    number = f"[{item['publication_number']}]"
    linked_number = f":ref:`{number} <{item['anchor']}>`"
    return entry.replace(number, linked_number, 1)


def build_publications_by_research_rst(items: list[dict[str, Any]]) -> str:
    sections = [
        ".. role:: student-first-author",
        "",
        "按年份倒序浏览学术成果 Publications by Year",
        _underline("按年份倒序浏览学术成果 Publications by Year", "="),
        "",
        ".. container:: publication-view-banner",
        "",
        "   :doc:`返回按研究方向浏览学术成果 <Publications>`：按研究方向浏览，方向内按发表年份倒序聚合。",
        "",
        "期刊论文 Journal Papers",
        "------------------------",
        "",
        "- :student-first-author:`学生第一作者` 表示该论文第一作者为团队在校或毕业学生。",
        "- 作者姓名后的 ``*`` 表示通讯作者。",
        "",
    ]
    current_section: int | None = None
    for item in items:
        data = item["data"]
        year = extract_year(data.get("date"))
        section_key = year if year >= EARLY_PUBLICATION_CUTOFF_YEAR else 0
        if section_key != current_section:
            current_section = section_key
            title = str(section_key) if section_key else EARLIER_PUBLICATIONS_TITLE
            sections.extend([title, "~" * 12, ""])
        sections.extend([research_full_entry(item), ""])
    return "\n".join(sections).rstrip() + "\n"


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


def snapshot(
    items: list[dict[str, Any]], old_anchor_map: dict[str, str], research_map: dict[str, dict[str, str]]
) -> dict[str, Any]:
    return {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "source_boundary": {
            "zotero_filter": {"inPublications": True, "itemType": "journalArticle"},
            "count": len(items),
            "degree_theses_data": str(DEGREE_THESES_PATH.relative_to(ROOT)),
            "teaching_data": str(TEACHING_DATA_PATH.relative_to(ROOT)),
        },
        "csl_style": {
            "id": CSL_STYLE_ID,
            "source_path": str(CSL_SOURCE_PATH),
            "installed_path": str(CSL_INSTALLED_PATH),
            "sha256": read_style_sha256(),
        },
        "anchor_rule": "ref-{first-author}{year}-{journal-initialism}; collisions append deterministic title token",
        "ordering": (
            "publication year desc, parsed date desc, normalized title asc; "
            f"years before {EARLY_PUBLICATION_CUTOFF_YEAR} grouped as {EARLIER_PUBLICATIONS_TITLE}"
        ),
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
                "student_first_author": student_first_author_display(item),
                "corresponding_authors": corresponding_author_display_names(item),
                "research_family": research_map[item["key"]].get("research_family"),
                "subdirection": research_map[item["key"]].get("subdirection"),
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
    research_map = load_research_map()
    validate_research_map(items, research_map)
    page = build_publications_rst(items, research_map)
    by_research_page = build_publications_by_research_rst(items)
    snap = snapshot(items, old_anchor_map, research_map)

    teaching_reform_items = fetch_teaching_reform_items()
    teaching_page = build_teaching_rst(teaching_reform_items)

    if args.dry_run:
        print(f"Would write {PUBLICATIONS_PATH}")
        print(f"Would write {PUBLICATIONS_BY_RESEARCH_PATH}")
        print(f"Would write {TEACHING_PATH}")
        print(f"Would write {SNAPSHOT_PATH}")
        print(f"Items: {len(items)}")
        print(f"Teaching-reform items: {len(teaching_reform_items)}")
        print(f"Anchor replacements: {len(old_anchor_map)}")
        for family in RESEARCH_FAMILY_ORDER:
            count = sum(1 for item in items if research_map[item["key"]]["research_family"] == family)
            print(f"{family}: {count}")
        return

    PUBLICATIONS_PATH.write_text(page, encoding="utf-8")
    PUBLICATIONS_BY_RESEARCH_PATH.write_text(by_research_page, encoding="utf-8")
    TEACHING_PATH.write_text(teaching_page, encoding="utf-8")
    SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_PATH.write_text(
        json.dumps(snap, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {PUBLICATIONS_PATH}")
    print(f"Wrote {PUBLICATIONS_BY_RESEARCH_PATH}")
    print(f"Wrote {TEACHING_PATH}")
    print(f"Wrote {SNAPSHOT_PATH}")
    print(f"Items: {len(items)}")
    print(f"Teaching-reform items: {len(teaching_reform_items)}")
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
