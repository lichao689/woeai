#!/usr/bin/env python3
"""Maintain generated public fragments for WOEAI Publication Artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]

LATEST_MARKER = "GENERATED LATEST PAPER NOTES"
TOCTREE_MARKER = "GENERATED PAPER NOTES TOCTREE"
AREA_MARKER = "GENERATED PAPER NOTES AREA"

RESEARCH_FAMILY_ORDER = ("建筑结构抗风", "海上漂浮风电")
RESEARCH_SUBDIRECTION_ORDER = {
    "建筑结构抗风": ("数值风洞与湍动入流", "高层建筑抗风与优化"),
    "海上漂浮风电": ("浮式风机系统一体化分析与优化", "浮式混凝土平台结构设计", "数值风浪流水池"),
}


@dataclass(frozen=True)
class PublicationArtifact:
    publication_ref: str
    title: str
    research_family: str
    subdirection: str
    original_year: int
    wechat_status: str
    order: int
    article_path: Path
    review_path: Path
    rtd_path: Path

    @property
    def is_public_complete(self) -> bool:
        return self.rtd_path.exists()

    @property
    def missing_paths(self) -> list[Path]:
        paths = []
        for path in (self.article_path, self.review_path, self.rtd_path):
            if not path.exists():
                paths.append(path)
        return paths


def repo_relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def unquote_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_backlog_items(backlog_path: Path) -> list[dict[str, str]]:
    if not backlog_path.exists():
        raise RuntimeError(f"Missing backlog: {backlog_path}")
    items: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    def finish() -> None:
        if current and current.get("publication_ref"):
            items.append(current.copy())

    for raw in backlog_path.read_text(encoding="utf-8").splitlines():
        item_match = re.match(r"\s*-\s+publication_ref:\s+(\S+)\s*$", raw)
        if item_match:
            finish()
            current = {"publication_ref": unquote_scalar(item_match.group(1))}
            continue
        if current is None or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        if key.startswith("-"):
            continue
        current[key] = unquote_scalar(value)
    finish()
    return items


def parse_markdown_title(article_path: Path, fallback: str) -> str:
    if not article_path.exists():
        return fallback
    for raw in article_path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("# "):
            return raw[2:].strip()
    return fallback


def int_or_zero(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        return 0


def load_artifacts(root: Path) -> list[PublicationArtifact]:
    backlog_path = root / "wechat/backlog/selected-papers.yml"
    artifacts: list[PublicationArtifact] = []
    for order, item in enumerate(parse_backlog_items(backlog_path)):
        publication_ref = item["publication_ref"]
        article_path = root / f"wechat/articles/draft-public-safe/{publication_ref}.md"
        review_path = root / f"wechat/articles/review/{publication_ref}.review.md"
        rtd_path = root / f"docs/source/paper-notes/{publication_ref}.rst"
        title = parse_markdown_title(article_path, item.get("title", publication_ref))
        artifacts.append(
            PublicationArtifact(
                publication_ref=publication_ref,
                title=title,
                research_family=item.get("research_family", ""),
                subdirection=item.get("subdirection", ""),
                original_year=int_or_zero(item.get("original_year", "0")),
                wechat_status=item.get("wechat_status", ""),
                order=order,
                article_path=article_path,
                review_path=review_path,
                rtd_path=rtd_path,
            )
        )
    return artifacts


def public_artifacts(root: Path) -> list[PublicationArtifact]:
    return [artifact for artifact in load_artifacts(root) if artifact.is_public_complete]


def sort_public_artifacts(artifacts: list[PublicationArtifact]) -> list[PublicationArtifact]:
    return sorted(artifacts, key=lambda artifact: (-artifact.original_year, artifact.order))


def render_latest_paper_notes(root: Path, limit: int = 10) -> str:
    lines = []
    for artifact in sort_public_artifacts(public_artifacts(root))[:limit]:
        lines.append(
            "- "
            f"{artifact.original_year} | {artifact.research_family} / {artifact.subdirection}: "
            f":doc:`{artifact.title} <paper-notes/{artifact.publication_ref}>`"
        )
    return "\n".join(lines) + ("\n" if lines else "")


def render_paper_notes_toctree(root: Path) -> str:
    artifacts = sort_public_artifacts(public_artifacts(root))
    if not artifacts:
        return ""
    lines = [
        ".. toctree::",
        "   :hidden:",
        "   :maxdepth: 1",
        "",
    ]
    lines.extend(f"   paper-notes/{artifact.publication_ref}" for artifact in artifacts)
    return "\n".join(lines) + "\n"


def rst_heading(title: str, marker: str) -> list[str]:
    width = 0
    for char in title:
        width += 2 if ord(char) >= 0x2E80 else 1
    return [title, marker * width, ""]


def render_paper_notes_area(root: Path) -> str:
    artifacts = sort_public_artifacts(public_artifacts(root))
    grouped: dict[tuple[str, str], list[PublicationArtifact]] = {}
    for artifact in artifacts:
        grouped.setdefault((artifact.research_family, artifact.subdirection), []).append(artifact)

    lines = [
        "以下页面由公众号论文正文转换为 RTD 配套页，按二级科研方向归集。同一子方向内，按论文发表时间倒序排列。",
        "",
    ]
    for family in RESEARCH_FAMILY_ORDER:
        family_has_items = any(key[0] == family for key in grouped)
        if not family_has_items:
            continue
        lines.extend(rst_heading(family, "~"))
        for subdirection in RESEARCH_SUBDIRECTION_ORDER[family]:
            items = grouped.get((family, subdirection), [])
            if not items:
                continue
            lines.extend(rst_heading(subdirection, "^"))
            for artifact in items:
                lines.append(f"- {artifact.original_year}: :doc:`{artifact.title} <paper-notes/{artifact.publication_ref}>`")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def artifact_integrity_problems(root: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    for artifact in public_artifacts(root):
        if artifact.original_year <= 0:
            problems.append(
                {
                    "kind": "missing_original_year",
                    "publication_ref": artifact.publication_ref,
                    "path": repo_relative(artifact.rtd_path, root),
                }
            )
        if artifact.research_family not in RESEARCH_FAMILY_ORDER:
            problems.append(
                {
                    "kind": "unknown_research_family",
                    "publication_ref": artifact.publication_ref,
                    "research_family": artifact.research_family,
                    "path": repo_relative(artifact.rtd_path, root),
                }
            )
            continue
        if artifact.subdirection not in RESEARCH_SUBDIRECTION_ORDER[artifact.research_family]:
            problems.append(
                {
                    "kind": "unknown_subdirection",
                    "publication_ref": artifact.publication_ref,
                    "research_family": artifact.research_family,
                    "subdirection": artifact.subdirection,
                    "path": repo_relative(artifact.rtd_path, root),
                }
            )
    return problems


def generated_blocks(root: Path) -> dict[str, str]:
    return {
        LATEST_MARKER: render_latest_paper_notes(root),
        TOCTREE_MARKER: render_paper_notes_toctree(root),
        AREA_MARKER: render_paper_notes_area(root),
    }


def marker_lines(marker: str, indent: str = "") -> tuple[str, str]:
    return f"{indent}.. BEGIN {marker}", f"{indent}.. END {marker}"


def replace_marker_block(text: str, marker: str, replacement: str) -> tuple[str, bool]:
    pattern = re.compile(
        rf"^(?P<indent>[ \t]*)\.\. BEGIN {re.escape(marker)}\n"
        rf".*?"
        rf"^(?P=indent)\.\. END {re.escape(marker)}\n?",
        re.M | re.S,
    )
    match = pattern.search(text)
    if not match:
        return text, False
    indent = match.group("indent")
    begin, end = marker_lines(marker, indent)
    body = replacement.rstrip("\n")
    if indent:
        body = "\n".join(f"{indent}{line}" if line else "" for line in body.splitlines())
    new_block = f"{begin}\n\n{body}\n\n{end}\n"
    return text[: match.start()] + new_block + text[match.end() :], True


def current_marker_body(text: str, marker: str) -> str | None:
    pattern = re.compile(
        rf"^(?P<indent>[ \t]*)\.\. BEGIN {re.escape(marker)}\n\n"
        rf"(?P<body>.*?)"
        rf"\n(?P=indent)\.\. END {re.escape(marker)}",
        re.M | re.S,
    )
    match = pattern.search(text)
    if not match:
        return None
    indent = match.group("indent")
    body = match.group("body")
    if indent:
        body = "\n".join(line.removeprefix(indent) for line in body.splitlines())
    return body.rstrip("\n") + ("\n" if body.strip() else "")


def write_generated_blocks(root: Path) -> list[dict[str, str]]:
    block_specs = [
        (root / "docs/source/index.rst", LATEST_MARKER),
        (root / "docs/source/Publications.rst", TOCTREE_MARKER),
        (root / "docs/source/Publications.rst", AREA_MARKER),
    ]
    blocks = generated_blocks(root)
    changed: list[dict[str, str]] = []
    for path, marker in block_specs:
        text = path.read_text(encoding="utf-8")
        updated, found = replace_marker_block(text, marker, blocks[marker])
        if not found:
            raise RuntimeError(f"Missing marker block {marker} in {repo_relative(path, root)}")
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed.append({"path": repo_relative(path, root), "marker": marker})
    return changed


def check_generated_blocks(root: Path) -> list[dict[str, str]]:
    block_specs = [
        (root / "docs/source/index.rst", LATEST_MARKER),
        (root / "docs/source/Publications.rst", TOCTREE_MARKER),
        (root / "docs/source/Publications.rst", AREA_MARKER),
    ]
    blocks = generated_blocks(root)
    problems: list[dict[str, str]] = []
    for path, marker in block_specs:
        text = path.read_text(encoding="utf-8")
        current = current_marker_body(text, marker)
        if current is None:
            problems.append({"kind": "missing_marker", "path": repo_relative(path, root), "marker": marker})
            continue
        if current != blocks[marker]:
            problems.append({"kind": "out_of_sync", "path": repo_relative(path, root), "marker": marker})
    return problems


def artifact_diagnostics(root: Path) -> list[dict[str, Any]]:
    diagnostics: list[dict[str, Any]] = []
    for artifact in load_artifacts(root):
        missing = [repo_relative(path, root) for path in artifact.missing_paths]
        if not missing:
            continue
        diagnostics.append(
            {
                "publication_ref": artifact.publication_ref,
                "wechat_status": artifact.wechat_status,
                "public_complete": artifact.is_public_complete,
                "missing": missing,
            }
        )
    return diagnostics


def summary(root: Path, problems: list[dict[str, str]] | None = None) -> dict[str, Any]:
    artifacts = load_artifacts(root)
    complete = [artifact for artifact in artifacts if artifact.is_public_complete]
    return {
        "artifact_count": len(artifacts),
        "public_complete_count": len(complete),
        "diagnostics": artifact_diagnostics(root),
        "problems": problems or [],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--check", action="store_true", help="Fail if generated marker blocks are out of sync")
    action.add_argument("--write", action="store_true", help="Rewrite generated marker blocks")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    if args.write:
        problems = artifact_integrity_problems(root)
        if problems:
            payload = summary(root, problems)
            payload["ok"] = False
            print(json.dumps(payload, ensure_ascii=False, indent=2))
            return 1
        changed = write_generated_blocks(root)
        payload = summary(root)
        payload.update({"ok": True, "changed": changed})
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    problems = artifact_integrity_problems(root) + check_generated_blocks(root)
    payload = summary(root, problems)
    payload["ok"] = not problems
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
