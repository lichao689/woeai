"""Strict local-only draft correspondence; no public or generated-view fallback."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate field in private draft mapping")
        result[key] = value
    return result


def load_private_draft_mapping(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    records = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    if not isinstance(records, dict) or any(not isinstance(item, dict) for item in records.values()):
        raise ValueError("Private draft records must map publication references to objects")
    allowed = {"media_id", "wechat_draft_media_id", "created_at", "updated_at", "article_index", "app_id"}
    confirmed_targets: set[tuple[str, str, int]] = set()
    for ref, record in records.items():
        target = record.get("media_id", record.get("wechat_draft_media_id", ""))
        if (
            re.fullmatch(r"ref-[A-Za-z0-9_-]+", ref) is None
            or set(record) - allowed
            or any(not isinstance(value, str) for key, value in record.items() if key != "article_index")
            or not isinstance(target, str)
            or re.fullmatch(r"[A-Za-z0-9_-]{1,512}", target) is None
            or ("article_index" in record and (type(record["article_index"]) is not int or record["article_index"] < 0))
            or ("app_id" in record and re.fullmatch(r"wx[0-9a-f]{16}", record["app_id"]) is None)
            or ("media_id" in record and "wechat_draft_media_id" in record and record["media_id"] != record["wechat_draft_media_id"])
        ):
            raise ValueError("Invalid private draft mapping schema")
        if "app_id" in record and "article_index" in record:
            binding = (record["app_id"], target, record["article_index"])
            if binding in confirmed_targets:
                raise ValueError("Duplicate confirmed article target in private draft mapping")
            confirmed_targets.add(binding)
    return records
