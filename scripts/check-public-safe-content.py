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
    if findings:
        print("Public-safety check failed:", file=sys.stderr)
        for finding in findings:
            print(finding, file=sys.stderr)
        return 1
    print("Public-safety check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
