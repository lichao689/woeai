#!/usr/bin/env python3
"""Check public WeChat content for obvious secret patterns."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCAN_ROOTS = [ROOT / "wechat", ROOT / "docs/source/paper-notes"]

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
    ("english_abstract", re.compile(r"\*\*英文摘要\*\*")),
]
PUBLIC_BODY_FORBIDDEN_PATTERNS = [
    ("english_abstract", re.compile(r"\*\*英文摘要\*\*")),
    # MathJax raises "\tag not allowed in split environment" for \tag inside
    # aligned/cases/bmatrix. Use \qquad (N) for equation numbering instead.
    ("latex_tag_in_math", re.compile(r"\\tag\{")),
]
RST_HEADING_MARKERS = set("=-~^`#*")
REVIEW_REQUIRED_SECTIONS = [
    "## 源文件获取记录",
    "## 关键事实证据定位记录",
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


def is_review_note(path: Path, root: Path) -> bool:
    parts = path.relative_to(root).parts
    return len(parts) >= 3 and parts[0] == "articles" and parts[1] == "review" and path.name.endswith(".review.md")


def is_rtd_paper_deep_dive(path: Path, root: Path) -> bool:
    return root == ROOT / "docs/source/paper-notes" and path.suffix.lower() == ".rst"


def rst_headings(text: str) -> list[tuple[str, int]]:
    lines = text.splitlines()
    headings: list[tuple[str, int]] = []
    for index, title in enumerate(lines[:-1]):
        stripped_title = title.strip()
        underline = lines[index + 1].strip()
        if not stripped_title or len(underline) < 3:
            continue
        if len(set(underline)) == 1 and underline[0] in RST_HEADING_MARKERS:
            headings.append((stripped_title, index + 1))
    return headings


def is_conclusion_heading(title: str) -> bool:
    return re.fullmatch(r"(?:\d+(?:\.\d+)*\s+)?结论", title) is not None


def is_allowed_post_conclusion_heading(title: str) -> bool:
    return title.startswith("附录") or title.lower().startswith("appendix")


def rtd_deep_dive_layout_findings(path: Path, text: str) -> list[str]:
    findings: list[str] = []
    rel = path.relative_to(ROOT).as_posix()
    lines = text.splitlines()
    wechat_line_index = next(
        (index for index, line in enumerate(lines) if line.startswith("精简版微信公众号文章")),
        None,
    )
    if wechat_line_index is None:
        return findings

    next_content_index = wechat_line_index + 1
    while next_content_index < len(lines) and not lines[next_content_index].strip():
        next_content_index += 1
    if (
        next_content_index >= len(lines)
        or not lines[next_content_index].lstrip().startswith(".. image::")
        or "cover-wechat" not in lines[next_content_index]
    ):
        findings.append(
            f"{rel}:{wechat_line_index + 1}: RTD paper deep-dive missing top WeChat cover image "
            "(top_wechat_cover)"
        )

    headings = rst_headings(text)
    conclusion_index = next((index for index, (title, _line_no) in enumerate(headings) if is_conclusion_heading(title)), None)
    if conclusion_index is None:
        return findings
    reference_index = next(
        (index for index in range(conclusion_index + 1, len(headings)) if headings[index][0] == "参考文献"),
        None,
    )
    if reference_index is None:
        findings.append(f"{rel}:{headings[conclusion_index][1]}: RTD paper deep-dive missing references after conclusion (missing_references_after_conclusion)")
        return findings
    for title, line_no in headings[conclusion_index + 1 : reference_index]:
        if is_allowed_post_conclusion_heading(title):
            continue
        findings.append(
            f"{rel}:{line_no}: RTD paper deep-dive has disallowed section between conclusion and references "
            f"(post_conclusion_section: {title})"
        )
    return findings


def scan_path(path: Path, root: Path) -> list[str]:
    findings: list[str] = []
    text = path.read_text(encoding="utf-8")
    for label, pattern in SECRET_PATTERNS:
        for match in pattern.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            rel = path.relative_to(ROOT).as_posix()
            findings.append(f"{rel}:{line_no}: possible secret pattern ({label})")
    if is_reader_facing_draft(path, root):
        for label, pattern in PUBLIC_DRAFT_FORBIDDEN_PATTERNS:
            for match in pattern.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                rel = path.relative_to(ROOT).as_posix()
                findings.append(f"{rel}:{line_no}: reader draft contains editor-only content ({label})")
    if is_rtd_paper_deep_dive(path, root):
        for label, pattern in PUBLIC_BODY_FORBIDDEN_PATTERNS:
            for match in pattern.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                rel = path.relative_to(ROOT).as_posix()
                findings.append(f"{rel}:{line_no}: RTD paper deep-dive contains editor-only content ({label})")
        findings.extend(rtd_deep_dive_layout_findings(path, text))
    if is_review_note(path, root):
        rel = path.relative_to(ROOT).as_posix()
        for section in REVIEW_REQUIRED_SECTIONS:
            if section not in text:
                label = section.replace("## ", "", 1)
                findings.append(f"{rel}:1: review note missing required section ({label})")
    return findings


def root_for_path(path: Path) -> Path | None:
    resolved = path.resolve()
    for root in SCAN_ROOTS:
        try:
            resolved.relative_to(root.resolve())
        except ValueError:
            continue
        return root
    return None


def collect_findings(paths: list[Path] | None = None) -> list[str]:
    findings: list[str] = []
    if paths is not None:
        for raw_path in paths:
            path = raw_path.resolve()
            root = root_for_path(path)
            if root is None or should_skip(path, root) or not path.is_file():
                continue
            if is_scannable_text_path(path):
                findings.extend(scan_path(path, root))
        return findings

    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if should_skip(path, root) or not path.is_file():
                continue
            if not is_scannable_text_path(path):
                continue
            findings.extend(scan_path(path, root))
    return findings


def main() -> int:
    findings = collect_findings()
    if findings:
        print("Public-safety check failed:", file=sys.stderr)
        for finding in findings:
            print(finding, file=sys.stderr)
        return 1
    print("Public-safety check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
