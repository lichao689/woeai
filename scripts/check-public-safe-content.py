#!/usr/bin/env python3
"""Check public WeChat content for obvious secret patterns."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCAN_ROOTS = [ROOT / "wechat"]

SECRET_PATTERNS = [
    ("appsecret", re.compile(r"(?i)appsecret['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9_-]{8,}")),
    ("access_token", re.compile(r"(?i)access_token['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{12,}")),
    ("refresh_token", re.compile(r"(?i)refresh_token['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{12,}")),
    ("zotero_api_key", re.compile(r"(?i)zotero[-_ ]?api[-_ ]?key['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{8,}")),
    ("wechat_token_or_secret", re.compile(r"(?i)wechat[-_ ]?(token|secret)['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{8,}")),
]
PUBLIC_DRAFT_FORBIDDEN_PATTERNS = [
    ("yaml_front_matter", re.compile(r"\A---\s*$", re.M)),
    ("pending_placeholder", re.compile(r"(?i)\bpending\b|待上传|待确认")),
    ("figure_plan", re.compile(r"计划配图")),
    ("pre_publish_checklist", re.compile(r"发布前人工复核项|发布前任务")),
]
TEXT_SUFFIXES = {".json", ".md", ".rst", ".txt", ".yaml", ".yml"}
TEXT_FILENAMES = {".env"}

IGNORED_DIR_NAMES = {
    ".local",
    "private",
    "review-notes",
    "wechat-preview-html",
    "source-images",
    "secrets",
}


def is_scannable_text_path(path: Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES or path.name.lower() in TEXT_FILENAMES


def should_skip(path: Path, root: Path) -> bool:
    return any(part in IGNORED_DIR_NAMES for part in path.relative_to(root).parts)


def is_reader_facing_draft(path: Path, root: Path) -> bool:
    parts = path.relative_to(root).parts
    return len(parts) >= 3 and parts[:3] == ("articles", "draft-public-safe", path.name)


def main() -> int:
    findings: list[str] = []
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if should_skip(path, root) or not path.is_file():
                continue
            if not is_scannable_text_path(path):
                continue
            text = path.read_text(encoding="utf-8")
            for label, pattern in SECRET_PATTERNS:
                for match in pattern.finditer(text):
                    line_no = text.count("\n", 0, match.start()) + 1
                    rel = path.relative_to(ROOT)
                    findings.append(f"{rel}:{line_no}: possible secret pattern ({label})")
            if is_reader_facing_draft(path, root):
                for label, pattern in PUBLIC_DRAFT_FORBIDDEN_PATTERNS:
                    for match in pattern.finditer(text):
                        line_no = text.count("\n", 0, match.start()) + 1
                        rel = path.relative_to(ROOT)
                        findings.append(f"{rel}:{line_no}: reader draft contains editor-only content ({label})")
    if findings:
        print("Public-safety check failed:", file=sys.stderr)
        for finding in findings:
            print(finding, file=sys.stderr)
        return 1
    print("Public-safety check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
