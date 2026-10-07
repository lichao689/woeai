"""Strict reader for the user-approved minimal public draft correspondence table."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate field in draft mapping")
        result[key] = value
    return result


def load_public_draft_mapping(path: Path, known_refs: set[str]) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    rows = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    if not isinstance(rows, list):
        raise ValueError("Public draft mapping must be an array")
    records: dict[str, dict[str, Any]] = {}
    targets: set[str] = set()
    for record in rows:
        if (
            not isinstance(record, dict)
            or set(record) != {"publication_ref", "wechat_draft_media_id"}
            or not isinstance(record["publication_ref"], str)
            or record["publication_ref"] not in known_refs
            or not isinstance(record["wechat_draft_media_id"], str)
            or re.fullmatch(r"[A-Za-z0-9_-]{1,512}", record["wechat_draft_media_id"]) is None
        ):
            raise ValueError("Invalid public draft mapping schema or publication reference")
        ref = record["publication_ref"]
        target = record["wechat_draft_media_id"]
        if ref in records or target in targets:
            raise ValueError("Duplicate publication reference or draft identifier")
        targets.add(target)
        records[ref] = record
    return records
