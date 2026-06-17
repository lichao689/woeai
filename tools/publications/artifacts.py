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


# This script is invoked by absolute path (check-docs.sh, agents, direct calls),
# so the repo root is not guaranteed to be on sys.path. Make the local ``woeai``
# package importable regardless of how the entry point is launched.
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

LATEST_MARKER = "GENERATED LATEST PAPER NOTES"

# Research taxonomy is a single source of truth in woeai.publications.
# Importing here (rather than re-declaring) is exactly what collapses the
# former byte-for-byte copy across this file and two others.
from woeai.publications import (  # noqa: E402
    RESEARCH_FAMILY_ORDER,
    RESEARCH_SUBDIRECTION_ORDER,
)
from woeai.wechat.backlog import BacklogPaper, parse_backlog_papers  # noqa: E402,F401


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
        for path in (self.rtd_path,):
            if not path.exists():
                paths.append(path)
        return paths


def repo_relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def parse_markdown_title(article_path: Path, fallback: str) -> str:
    if not article_path.exists():
        return fallback
    for raw in article_path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("# "):
            return raw[2:].strip()
    return fallback


def parse_rst_title(rtd_path: Path, fallback: str) -> str:
    if not rtd_path.exists():
        return fallback
    lines = rtd_path.read_text(encoding="utf-8").splitlines()
    for idx, raw in enumerate(lines[:-1]):
        title = raw.strip()
        underline = lines[idx + 1].strip()
        if not title or title.startswith(".. "):
            continue
        if len(underline) >= len(title) and set(underline) <= {"=", "-", "~", "^"}:
            return title
    return fallback


def select_artifact_title(article_path: Path, rtd_path: Path, fallback: str) -> str:
    rtd_title = parse_rst_title(rtd_path, fallback)
    # New full RTD pages are independent 论文精解 pages. When their public title
    # already says so, keep RTD navigation anchored to that page title instead
    # of replacing it with the compact WeChat article title.
    if "论文精解" in rtd_title:
        return rtd_title
    return parse_markdown_title(article_path, rtd_title)


def load_artifacts(root: Path) -> list[PublicationArtifact]:
    backlog_path = root / "wechat/backlog/selected-papers.yml"
    artifacts: list[PublicationArtifact] = []
    papers = parse_backlog_papers(backlog_path)
    if not papers and not backlog_path.exists():
        raise RuntimeError(f"Missing backlog: {backlog_path}")
    for paper in papers:
        publication_ref = paper.publication_ref
        article_path = root / f"wechat/articles/draft-public-safe/{publication_ref}.md"
        review_path = root / f"wechat/articles/review/{publication_ref}.review.md"
        rtd_path = root / f"docs/source/paper-notes/{publication_ref}.rst"
        title = select_artifact_title(article_path, rtd_path, paper.title or publication_ref)
        artifacts.append(
            PublicationArtifact(
                publication_ref=publication_ref,
                title=title,
                research_family=paper.research_family,
                subdirection=paper.subdirection,
                original_year=paper.original_year,
                wechat_status=paper.wechat_status,
                order=paper.order,
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
        "以下页面为 RTD 论文精解页面，按二级科研方向归集。同一子方向内，按论文发表时间倒序排列。",
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


PAPER_NOTES_FRAGMENT_PATH = Path("docs/source/_paper-notes-fragment.rst")


def render_paper_notes_fragment(root: Path) -> str:
    """Render the whole paper deep-dive fragment file owned by this tool.

    The fragment is included by Publications.rst via ``.. include::``. It holds
    the generated toctree, the 论文精解 heading, and the generated
    area. Owning it as a standalone file means the Zotero generator can
    overwrite Publications.rst wholesale without clobbering this content.
    """
    toctree = render_paper_notes_toctree(root)
    area = render_paper_notes_area(root)
    parts: list[str] = []
    if toctree:
        parts.append(toctree.rstrip("\n"))
        parts.append("")
    parts.append("论文精解")
    parts.append("--------")
    parts.append("")
    parts.append(area.rstrip("\n"))
    parts.append("")
    return "\n".join(parts)


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
    changed: list[dict[str, str]] = []
    blocks = generated_blocks(root)

    # index.rst keeps its marker block (single writer, no contention).
    index_path = root / "docs/source/index.rst"
    text = index_path.read_text(encoding="utf-8")
    updated, found = replace_marker_block(text, LATEST_MARKER, blocks[LATEST_MARKER])
    if not found:
        raise RuntimeError(f"Missing marker block {LATEST_MARKER} in {repo_relative(index_path, root)}")
    if updated != text:
        index_path.write_text(updated, encoding="utf-8")
        changed.append({"path": repo_relative(index_path, root), "marker": LATEST_MARKER})

    # The paper-notes fragment is a standalone file owned solely by this tool.
    # Publications.rst includes it; the Zotero generator no longer needs to
    # preserve marker blocks when it overwrites Publications.rst.
    fragment_path = root / PAPER_NOTES_FRAGMENT_PATH
    fragment = render_paper_notes_fragment(root)
    if not fragment_path.exists() or fragment_path.read_text(encoding="utf-8") != fragment:
        fragment_path.write_text(fragment, encoding="utf-8")
        changed.append({"path": repo_relative(fragment_path, root), "marker": "PAPER_NOTES_FRAGMENT"})

    return changed


def check_generated_blocks(root: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    blocks = generated_blocks(root)

    # index.rst marker block.
    index_path = root / "docs/source/index.rst"
    text = index_path.read_text(encoding="utf-8")
    current = current_marker_body(text, LATEST_MARKER)
    if current is None:
        problems.append({"kind": "missing_marker", "path": repo_relative(index_path, root), "marker": LATEST_MARKER})
    elif current != blocks[LATEST_MARKER]:
        problems.append({"kind": "out_of_sync", "path": repo_relative(index_path, root), "marker": LATEST_MARKER})

    # Paper-notes fragment file.
    fragment_path = root / PAPER_NOTES_FRAGMENT_PATH
    expected = render_paper_notes_fragment(root)
    if not fragment_path.exists():
        problems.append({"kind": "missing_fragment", "path": repo_relative(fragment_path, root)})
    elif fragment_path.read_text(encoding="utf-8") != expected:
        problems.append({"kind": "out_of_sync", "path": repo_relative(fragment_path, root), "marker": "PAPER_NOTES_FRAGMENT"})

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
