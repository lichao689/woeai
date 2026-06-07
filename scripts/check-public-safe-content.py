#!/usr/bin/env python3
"""Check public WeChat content for obvious secret patterns."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCAN_ROOTS = [ROOT / "wechat"]

SECRET_PATTERNS = [
    re.compile(r"(?i)appsecret\s*[:=]\s*['\"]?[A-Za-z0-9_-]{8,}"),
    re.compile(r"(?i)access_token\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{12,}"),
    re.compile(r"(?i)refresh_token\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{12,}"),
    re.compile(r"(?i)zotero[-_ ]?api[-_ ]?key\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{8,}"),
    re.compile(r"(?i)wechat[-_ ]?(token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{8,}"),
]

IGNORED_DIR_NAMES = {
    ".local",
    "private",
    "review-notes",
    "wechat-preview-html",
    "source-images",
    "secrets",
}


def should_skip(path: Path) -> bool:
    return any(part in IGNORED_DIR_NAMES for part in path.parts)


def main() -> int:
    findings: list[str] = []
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if should_skip(path) or not path.is_file():
                continue
            if path.suffix.lower() not in {".md", ".rst", ".yml", ".yaml", ".txt"}:
                continue
            text = path.read_text(encoding="utf-8")
            for pattern in SECRET_PATTERNS:
                for match in pattern.finditer(text):
                    line_no = text.count("\n", 0, match.start()) + 1
                    rel = path.relative_to(ROOT)
                    findings.append(f"{rel}:{line_no}: possible secret pattern")
    if findings:
        print("Public-safety check failed:", file=sys.stderr)
        for finding in findings:
            print(finding, file=sys.stderr)
        return 1
    print("Public-safety check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
