#!/usr/bin/env python3
"""Check public content for secrets, private backend data, and layout issues."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCAN_ROOTS = [ROOT / "wechat", ROOT / "docs/source/paper-notes", ROOT / "docs/data", ROOT / "project/research", ROOT / "project/plans"]
# Explicit user approval covers exactly this 17-record, two-field snapshot.
# Future mapping changes require fresh approval and a reviewed digest update.
APPROVED_DRAFT_MAP_SHA256 = "8605522556f090dd0d49acc34ca800af802e827b91aa266dc35fdb26e928a7a2"

SECRET_PATTERNS = [
    ("appsecret", re.compile(r"(?i)appsecret['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9_-]{8,}")),
    ("access_token", re.compile(r"(?i)access_token['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{12,}")),
    ("refresh_token", re.compile(r"(?i)refresh_token['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{12,}")),
    ("zotero_api_key", re.compile(r"(?i)zotero[-_ ]?api[-_ ]?key['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{8,}")),
    ("wechat_token_or_secret", re.compile(r"(?i)wechat[-_ ]?(token|secret)['\"]?\s*[:=]\s*['\"]?[A-Za-z0-9_.-]{8,}")),
]
# Backend identifiers are private operational data even though they are not
# credentials. Match labelled values rather than arbitrary opaque strings so
# public Zotero citation keys and explanatory mentions remain valid.
BACKEND_FIELD = (
    r"(?:[a-z0-9]+_)*(?:media_id|draft_id|publish_id|"
    r"backend_response|api_response|wechat_response|draft_response|publish_response|cover_response)"
)
BACKEND_VALUE_PATTERN = re.compile(
    rf"(?<![a-z0-9_])(?P<field>{BACKEND_FIELD})(?![a-z0-9_])"
    r"[`'\"*]*[ \t]*"
    r"(?:(?P<assignment>[:=：])\s*(?:[>|][+-]?\s*)?|"
    r"(?P<prose>is\b|was\b|为|是)\s*|(?=[`'\"]))"
    r"(?P<quote>[`'\"]*)"
    r"(?P<value>[^\s`'\"，。；,;<>]+)",
    re.I,
)
BACKEND_EMPTY_VALUES = {"null", "none", "nil", "redacted", "[redacted]", "{}", "[]", "~"}
BACKEND_FIELD_DESCRIPTION = re.compile(r"optional\s+(?:existing\s+)?draft\b", re.I)


def private_backend_matches(text: str):
    for match in BACKEND_VALUE_PATTERN.finditer(text):
        value = match.group("value")
        if value.lower() in BACKEND_EMPTY_VALUES:
            continue
        # Existing workflow documentation describes this optional field. This
        # narrow prose exception must not permit quoted identifier values.
        if not match.group("quote") and BACKEND_FIELD_DESCRIPTION.match(text, match.start("value")):
            continue
        # In prose, ordinary words ("media_id is returned") explain the field.
        # Quoted values and opaque identifiers instead record an actual value.
        if match.group("prose") and not match.group("quote"):
            if not re.search(r"[0-9_+/=-]", value):
                continue
        if value[0].isascii() and (value[0].isalnum() or value[0] in "{[_-/+"):
            yield match


# Public bibliographic item keys are intentional citation locators. Only
# attachment/child labels identify private Zotero source records.
PRIVATE_SOURCE_PATTERNS = [
    ("attachment_identifier", re.compile(
        r"(?i:(?:\b(?:zotero[ _-]+|pdf[ _-]+)?attachment(?:[ _-]+(?:keys?|ids?))?|"
        r"\bzotero[ _-]+child(?:[ _-]+(?:keys?|ids?))?|\battach_key))"
        r"[`'\"*]*\s*[:=：]?\s*[\[`'\"]*"
        r"(?-i:[A-Z0-9]{8})(?![A-Za-z0-9_])"
    )),
    ("attachment_identifier", re.compile(
        r"(?i:\bZotero (?:Desktop )?Local API children\s*[:：]\s*(?:passed\s*)?)"
        r"[([`'\" ]*(?-i:[A-Z0-9]{8})(?![A-Za-z0-9_])"
    )),
    ("local_source_path", re.compile(
        r"(?<![A-Za-z0-9])(?:file://)?"
        r"(?:/(?:Users|home|root|tmp|workspace|mnt|private|var|Volumes)/|~/|[A-Za-z]:[\\/])"
        r"[^\s`\"'<>]*?\.(?:pdf|txt)(?![A-Za-z0-9])", re.I
    )),
    ("library_operational_identifier", re.compile(
        r"(?i:\b(?:library[ _-]+(?:(?:file|folder|asset)[ _-]+)?ids?|"
        r"(?:file|folder|asset)[ _-]+ids?))"
        r"[`'\"*]*\s*[:=：]\s*[`'\"]*"
        r"(?:[A-Za-z0-9_-]{8,})(?![A-Za-z0-9_-])"
    )),
    ("library_operational_identifier", re.compile(
        r"\bsediment://file[_-][A-Za-z0-9_-]+", re.I
    )),
]


def private_attachment_table_lines(text: str):
    """Check attachment columns without flagging bibliographic key columns."""
    columns: list[int] = []
    for line_no, line in enumerate(text.splitlines(), 1):
        if "|" not in line:
            columns = []
            continue
        cells = line.strip().strip("|").split("|")
        headers = [index for index, cell in enumerate(cells) if re.search(
            r"^\s*[`*]*(?:(?:pdf|zotero)[ _-]+)?(?:attachment|child)(?:[ _-]+(?:keys?|ids?))?[`*]*\s*$", cell, re.I
        )]
        if headers:
            columns = headers
            continue
        if any(index < len(cells) and re.search(r"(?<![A-Za-z0-9_])[A-Z0-9]{8}(?![A-Za-z0-9_])", cells[index])
               for index in columns):
            yield line_no


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
# Review notes have a stricter public contract than the bibliography/registry:
# retain current scientific evidence, not internal citation or draft history.
REVIEW_FORBIDDEN_PATTERNS = [
    ("review_zotero_identifier", re.compile(
        r"(?i:\bzotero_(?:key|item_key|item_id)[`'\"]*\s*[:=：])|"
        r"(?i:\bZotero(?:[ _-]+(?:item|citation))?(?:[ _-]+(?:key|id))?)"
        r"[`'\"*]*\s*[:=：]?\s*[`'\"]*[A-Z0-9]{8}(?![A-Za-z0-9_])|"
        r"zotero://[^\s`'\"]+", re.M
    )),
    ("review_draft_history", re.compile(r"\bwechat_draft_(?:created|updated)_at\b", re.I)),
    ("review_preview_field", re.compile(
        r"\b(?:local_)?(?:preview_(?:html|file)(?:_path)?|preview_path|html_preview(?:_path)?|local_html_path|offline_html(?:_path)?)"
        r"[`'\"]*\s*[:=：]", re.I
    )),
    ("review_private_path", re.compile(
        r"(?<![A-Za-z0-9])(?:file://)?"
        r"(?:/(?:Users|home|root|tmp|workspace|mnt|private|var|Volumes)/|~/|[A-Za-z]:[\\/]|"
        r"(?:wechat/)?\.local/|wechat-preview-html/)"
        r"[^\s`'\"<>]+", re.I
    )),
]


REVIEW_READY_FLAGS = (
    "formula_preview_checked",
    "figure_preview_checked",
    "cover_image_checked",
    "wechat_backend_preview_checked",
)


def stale_review_ready_lines(text: str) -> list[int]:
    """Readiness is a current front-matter claim, not a forbidden prose word."""
    front = re.match(r"\A---[ \t]*\r?\n(?P<body>.*?)^---[ \t]*$", text, re.M | re.S)
    if front is None:
        return []
    body = front.group("body")
    ready = list(re.finditer(
        r"^wechat_status:[ \t]*(['\"]?)ready_to_publish\1[ \t]*(?:#.*)?$", body, re.M
    ))
    if not ready:
        return []
    for flag in REVIEW_READY_FLAGS:
        values = re.findall(rf"^{flag}:[ \t]*(.*)$", body, re.M)
        # Missing, duplicated, or non-boolean flags cannot establish readiness.
        if len(values) != 1 or not re.fullmatch(r"true[ \t]*(?:#.*)?", values[0], re.I):
            return [text.count("\n", 0, front.start("body") + match.start()) + 1 for match in ready]
    return []


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
    # Scientific nomenclature can follow the conclusion in the source paper.
    # Keep a narrow exact-title exception; declarations remain disallowed.
    return (
        title.startswith("附录")
        or title.lower().startswith("appendix")
        or title in {"符号与缩写", "符号表", "缩写表"}
        or title.lower() == "nomenclature"
    )


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
    approved_draft_map = False
    if path.resolve() == (ROOT / "wechat/data/draft-map.json").resolve():
        approved_draft_map = hashlib.sha256(path.read_bytes()).hexdigest() == APPROVED_DRAFT_MAP_SHA256
        if not approved_draft_map:
            findings.append("wechat/data/draft-map.json:1: unapproved public draft mapping")
    for label, pattern in SECRET_PATTERNS:
        for match in pattern.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            rel = path.relative_to(ROOT).as_posix()
            findings.append(f"{rel}:{line_no}: possible secret pattern ({label})")
    for match in private_backend_matches(text):
        if approved_draft_map and match.group("field").lower() == "wechat_draft_media_id":
            continue
        line_no = text.count("\n", 0, match.start()) + 1
        rel = path.relative_to(ROOT).as_posix()
        # Never print the matched value, including for backend response blobs.
        field = match.group("field").lower()
        findings.append(f"{rel}:{line_no}: private backend data ({field})")
    for label, pattern in PRIVATE_SOURCE_PATTERNS:
        for match in pattern.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            rel = path.relative_to(ROOT).as_posix()
            findings.append(f"{rel}:{line_no}: private source locator ({label})")
    for line_no in private_attachment_table_lines(text):
        rel = path.relative_to(ROOT).as_posix()
        findings.append(f"{rel}:{line_no}: private source locator (attachment_identifier)")
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
        for line_no in stale_review_ready_lines(text):
            findings.append(f"{rel}:{line_no}: review readiness lacks current preview approvals (review_stale_ready)")
        for label, pattern in REVIEW_FORBIDDEN_PATTERNS:
            for match in pattern.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                findings.append(
                    f"{rel}:{line_no}: review contains private or obsolete workflow content ({label})"
                )
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
