"""Author-name handling, student-first-author detection, and corresponding-author
detection for WOEAI publication rendering.

This module reads Degree Thesis Data (``docs/data/degree-theses.json``) to decide
which first authors are Student First Authors and which authors are corresponding
authors. It was previously inlined in ``scripts/update-publications-from-zotero.py``.

Design notes
------------
- ``load_degree_thesis_data`` and ``load_student_author_names`` keep their
  ``functools.lru_cache`` so repeated calls during one render pass do not re-read
  the JSON. The data path is resolved relative to the repo root, computed from
  this module's own location, so callers do not pass paths.
- Author-name normalisation (``normalize_author_name``) strips punctuation and
  case so that ``"Li Chao"``, ``"li chao"`` and ``"李朝"`` can be compared.
"""

from __future__ import annotations

import functools
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

from woeai.publications.textutils import (
    CORRESPONDING_AUTHOR_LABELS,
    DEGREE_THESIS_GROUPS,
    GROUP_LEADER_AUTHOR_NAMES,
    ZoteroError,
    creator_display_name,
    creator_csl_display_name,
    normalize_author_name,
    rst_escape,
    split_extra_tokens,
)

# Repo root: woeai/publications/authors.py -> parents[2]
_REPO_ROOT = Path(__file__).resolve().parents[2]
_DEGREE_THESES_PATH = _REPO_ROOT / "docs/data/degree-theses.json"


@functools.lru_cache(maxsize=1)
def load_degree_thesis_data() -> dict[str, Any]:
    if not _DEGREE_THESES_PATH.exists():
        raise ZoteroError(f"Degree thesis data is missing: {_DEGREE_THESES_PATH}")
    try:
        payload = json.loads(_DEGREE_THESES_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ZoteroError(f"Degree thesis data is invalid JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise ZoteroError("Degree thesis data must be a JSON object.")
    if not isinstance(payload.get("student_authors", []), list):
        raise ZoteroError("Degree thesis data must contain a list at student_authors.")
    if not isinstance(payload.get("theses", {}), dict):
        raise ZoteroError("Degree thesis data must contain an object at theses.")
    return payload


def student_record_variants(record: dict[str, Any]) -> set[str]:
    leader_names = {normalize_author_name(name) for name in GROUP_LEADER_AUTHOR_NAMES}
    variants: set[str] = set()
    name_cn = str(record.get("name_cn") or "").strip()
    name_en = str(record.get("name_en") or "").strip()
    if name_cn:
        variants.add(name_cn)
    if name_en and normalize_author_name(name_en) not in leader_names:
        variants.add(name_en)
    aliases = record.get("aliases") or []
    if isinstance(aliases, list):
        for alias in aliases:
            alias_text = str(alias or "").strip()
            if alias_text and normalize_author_name(alias_text) not in leader_names:
                variants.add(alias_text)
    return variants


def iter_student_records() -> list[dict[str, Any]]:
    payload = load_degree_thesis_data()
    records: list[dict[str, Any]] = []
    for record in payload.get("student_authors", []):
        if isinstance(record, dict):
            records.append(record)
    theses = payload.get("theses", {})
    if isinstance(theses, dict):
        for group_key, _title in DEGREE_THESIS_GROUPS:
            for record in theses.get(group_key, []):
                if isinstance(record, dict):
                    records.append(record)
    return records


def iter_current_student_authors() -> list[dict[str, Any]]:
    payload = load_degree_thesis_data()
    records = payload.get("student_authors", [])
    if not isinstance(records, list):
        raise ZoteroError("Degree thesis data must contain a list at student_authors.")
    return [record for record in records if isinstance(record, dict)]


@functools.lru_cache(maxsize=1)
def load_student_author_names() -> set[str]:
    names: set[str] = set()
    for record in iter_student_records():
        for variant in student_record_variants(record):
            names.add(normalize_author_name(variant))
    return names


def student_first_author_display(item: dict[str, Any]) -> str | None:
    creators = item["data"].get("creators") or []
    if not creators:
        return None
    first_author = creators[0]
    variants = {
        creator_display_name(first_author),
        creator_csl_display_name(first_author),
    }
    student_names = load_student_author_names()
    if any(normalize_author_name(variant) in student_names for variant in variants):
        return creator_csl_display_name(first_author)
    return None


def mark_student_first_author(value: str, item: dict[str, Any]) -> str:
    first_author = student_first_author_display(item)
    if not first_author:
        return value
    escaped_author = rst_escape(first_author)
    pattern = re.compile(rf"^{re.escape(escaped_author)}(?=;|,)")
    return pattern.sub(f":student-first-author:`{escaped_author}`", value, count=1)


def has_corresponding_author_flag(item: dict[str, Any]) -> bool:
    extra = str(item.get("data", {}).get("extra") or "")
    if not extra:
        return False
    if re.search(r"(?:^|[、,，;；\s])_?通讯作者(?:$|[、,，;；\s])", extra):
        return True
    if re.search(r"\bcorresponding[-_ ]authors?\b", extra, flags=re.I):
        return True
    normalized_tokens = {token.casefold().lstrip("_#") for token in split_extra_tokens(extra)}
    return any(label in normalized_tokens for label in CORRESPONDING_AUTHOR_LABELS)


def explicit_corresponding_author_tokens(item: dict[str, Any]) -> list[str]:
    extra = str(item.get("data", {}).get("extra") or "")
    if not extra:
        return []
    tokens: list[str] = []
    for label in CORRESPONDING_AUTHOR_LABELS:
        pattern = re.compile(rf"{re.escape(label)}\s*[:：=]\s*(?P<names>[^\n\r]+)", re.I)
        for match in pattern.finditer(extra):
            raw_names = match.group("names")
            # Stop before Zotero tag-style separators when the next token is a private marker.
            raw_names = re.split(r"\s+[|]\s+|🏷️", raw_names, maxsplit=1)[0]
            tokens.extend(split_extra_tokens(raw_names))
    return [token for token in tokens if token and not token.startswith(("_", "#", "/"))]


def creator_name_index(item: dict[str, Any]) -> dict[str, str]:
    index: dict[str, str] = {}
    for creator in item.get("data", {}).get("creators") or []:
        csl_name = creator_csl_display_name(creator)
        for variant in {creator_display_name(creator), csl_name}:
            normalized = normalize_author_name(variant)
            if normalized:
                index[normalized] = csl_name
    return index


def corresponding_author_display_names(item: dict[str, Any]) -> list[str]:
    index = creator_name_index(item)
    names: list[str] = []
    for token in explicit_corresponding_author_tokens(item):
        normalized = normalize_author_name(token)
        if normalized in index:
            names.append(index[normalized])
        elif normalized:
            names.append(token)
    if not names and has_corresponding_author_flag(item):
        for leader_name in GROUP_LEADER_AUTHOR_NAMES:
            csl_name = index.get(normalize_author_name(leader_name))
            if csl_name:
                names.append(csl_name)
    seen: set[str] = set()
    unique_names: list[str] = []
    for name in names:
        normalized = normalize_author_name(name)
        if normalized and normalized not in seen:
            seen.add(normalized)
            unique_names.append(name)
    return unique_names


def rendered_author_variants(name: str, item: dict[str, Any]) -> list[str]:
    escaped_name = rst_escape(name)
    variants = [escaped_name]
    if normalize_author_name(name) in {normalize_author_name(raw) for raw in GROUP_LEADER_AUTHOR_NAMES}:
        variants.extend(["**Li Chao**", "**李朝**"])
    first_author = student_first_author_display(item)
    if first_author and normalize_author_name(first_author) == normalize_author_name(name):
        variants.append(f":student-first-author:`{rst_escape(first_author)}`")
    return variants


def mark_corresponding_authors(value: str, item: dict[str, Any]) -> str:
    names = corresponding_author_display_names(item)
    if not names:
        return value
    author_segment, separator, remainder = value.partition(",")
    for name in names:
        for variant in rendered_author_variants(name, item):
            pattern = re.compile(rf"({re.escape(variant)})(?!\\\*|\*)(?=\s*(?:;|,|$))")
            author_segment = pattern.sub(r"\1\\*", author_segment, count=1)
    return author_segment + separator + remainder
