#!/usr/bin/env python3
"""Convert a WOEAI public-safe WeChat Markdown article to RTD RST.

The Markdown article is the public content master. This converter handles the
WOEAI article subset: headings, paragraphs, lists, body figures with a two-line
caption, inline/display math, strong text, and direct external links. Platform
metadata such as the RTD top cover is read from the article review note.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path


WECHAT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = WECHAT_ROOT.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
DEFAULT_REF = "ref-zhao2026-BS"
PUBLICATIONS_RST = REPO_ROOT / "docs/source/Publications.rst"
# RTD channel adaptations: the WeChat title-category prefix is stripped from
# the RTD page title, and the paragraph carrying the fixed WeChat closing
# sentence (anchored on this phrase) is skipped because the bottom 阅读原文
# entry it refers to does not exist on RTD.
TITLE_CATEGORY_PREFIX = re.compile(r"^(?:数值风洞|结构抗风|漂浮风电)\s*\|\s*")
CLOSING_SENTENCE_ANCHOR = "点击阅读原文"
DOI_TRUNCATE = re.compile(r"^(.*?https://doi\.org/\S+)")

from woeai.wechat.backlog import BacklogPaper, parse_backlog_papers, rank_against_target  # noqa: E402,F401
from woeai.wechat.review import (  # noqa: E402,F401
    find_review_cover,
    parse_front_matter as parse_review_front_matter,
    parse_title,
    resolve_repo_path,
)


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve())


def relative_path_for_rst(path: Path, rst_path: Path) -> str:
    return Path(os.path.relpath(path.resolve(), rst_path.parent.resolve())).as_posix()


def display_width(text: str) -> int:
    width = 0
    for char in text:
        width += 2 if ord(char) >= 0x2E80 else 1
    return width


def heading(text: str, marker: str) -> list[str]:
    return [text, marker * display_width(text), ""]


def strip_title_category_prefix(title: str) -> str:
    return TITLE_CATEGORY_PREFIX.sub("", title).strip()


def article_title_for_ref(publication_ref: str, article_dir: Path, fallback: str = "") -> str:
    article_path = article_dir / f"{publication_ref}.md"
    if article_path.exists():
        try:
            return parse_title(article_path.read_text(encoding="utf-8"))
        except RuntimeError:
            pass
    return fallback or publication_ref


def rtd_related_links(
    publication_ref: str,
    *,
    backlog_path: Path,
    notes_dir: Path,
    article_dir: Path,
    limit: int = 3,
) -> list[dict[str, str]]:
    papers = parse_backlog_papers(backlog_path)
    target = next((paper for paper in papers if paper.publication_ref == publication_ref), None)
    if target is None:
        return []

    candidates: list[BacklogPaper] = []
    for paper in papers:
        if paper.publication_ref == publication_ref:
            continue
        if paper.research_family != target.research_family:
            continue
        if not (notes_dir / f"{paper.publication_ref}.rst").exists():
            continue
        candidates.append(paper)
    return [
        {
            "publication_ref": paper.publication_ref,
            "title": article_title_for_ref(paper.publication_ref, article_dir, paper.title),
        }
        for paper in sorted(candidates, key=lambda p: rank_against_target(p, target))[:limit]
    ]


def escape_rtd_doc_label(value: str) -> str:
    return value.replace("`", "'")


def parse_publications_citation(publication_ref: str, publications_path: Path | None = None) -> str:
    """Return the Publications.rst citation paragraph truncated at the DOI.

    Returns an empty string when the anchor or paragraph is missing, so
    temporary or test articles without a Publications entry simply omit the
    citation section.
    """
    source = publications_path or PUBLICATIONS_RST
    if not source.exists():
        return ""
    lines = source.read_text(encoding="utf-8").splitlines()
    anchor = f".. _{publication_ref}:"
    idx = 0
    while idx < len(lines) and lines[idx].strip() != anchor:
        idx += 1
    if idx >= len(lines):
        return ""
    idx += 1
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    citation_lines: list[str] = []
    while idx < len(lines) and lines[idx].strip():
        citation_lines.append(lines[idx].strip())
        idx += 1
    citation = " ".join(citation_lines)
    if not citation:
        return ""
    match = DOI_TRUNCATE.match(citation)
    return match.group(1) if match else citation


def emit_citation_section(
    output: list[str],
    publication_ref: str,
    publications_path: Path | None = None,
) -> None:
    citation = parse_publications_citation(publication_ref, publications_path)
    if not citation:
        print(
            f"warning: no Publications citation anchor for {publication_ref}; "
            "RTD citation section omitted",
            file=sys.stderr,
        )
        return
    if output and output[-1] != "":
        output.append("")
    output.extend(heading("完整引用", "-"))
    output.append(citation)
    output.append("")
    output.append(f"收录信息见 :ref:`WOEAI 学术成果页对应条目 <{publication_ref}>`。")
    output.append("")


def emit_rtd_related_navigation(
    output: list[str],
    publication_ref: str,
    *,
    backlog_path: Path,
    notes_dir: Path,
    article_dir: Path,
) -> None:
    links = rtd_related_links(
        publication_ref,
        backlog_path=backlog_path,
        notes_dir=notes_dir,
        article_dir=article_dir,
    )
    if not links:
        return
    if output and output[-1] != "":
        output.append("")
    output.extend(heading("相关论文精解", "-"))
    for link in links:
        label = escape_rtd_doc_label(strip_title_category_prefix(link["title"]))
        output.append(f"- :doc:`{label} <{link['publication_ref']}>`")
    output.append("")


def markdown_image(line: str) -> tuple[str, str] | None:
    match = re.match(r"!\[(.*?)\]\((.*?)\)\s*$", line.strip())
    if not match:
        return None
    alt, src = match.groups()
    return alt, src


def resolve_markdown_path(markdown_path: Path, src: str) -> Path:
    if re.match(r"https?://", src):
        raise RuntimeError(f"RTD body images must be local public-safe files: {src}")
    return (markdown_path.parent / src).resolve()


def is_special_start(line: str) -> bool:
    stripped = line.strip()
    return (
        not stripped
        or stripped.startswith("#")
        or stripped == "$$"
        or bool(markdown_image(stripped))
        or bool(re.match(r"([-*]|\d+\.)\s+", stripped))
    )


def convert_inline(text: str) -> str:
    def link_repl(match: re.Match[str]) -> str:
        label, url = match.groups()
        return f"`{label} <{url}>`_"

    def math_repl(match: re.Match[str]) -> str:
        return f":math:`{match.group(1)}`"

    def student_first_author_repl(match: re.Match[str]) -> str:
        return f":student-first-author:`{match.group(1).strip()}`"

    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", link_repl, text)
    text = re.sub(r"\$([^$\n]+)\$", math_repl, text)
    text = re.sub(r"<u>(.+?)</u>", student_first_author_repl, text)
    text = re.sub(r"\*\*([^*]+?)\*\*", r"**\1**", text)
    text = re.sub(r"([^\s])(\*\*[^*]+?\*\*)", r"\1 \2", text)
    text = re.sub(r"(\*\*[^*]+?\*\*)([^\s，。,.!?；;：:）\)\\])", r"\1 \2", text)
    return text.strip()


def emit_paragraph(lines: list[str], output: list[str]) -> None:
    if not lines:
        return
    text = " ".join(line.strip() for line in lines)
    lines.clear()
    if CLOSING_SENTENCE_ANCHOR in text:
        return
    output.append(convert_inline(text))
    output.append("")


def consume_caption(lines: list[str], start: int) -> tuple[str, str, int]:
    idx = start
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx >= len(lines):
        raise RuntimeError("Figure is missing the Chinese figure-title line")
    title = lines[idx].strip()
    idx += 1
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx >= len(lines):
        raise RuntimeError(f"Figure '{title}' is missing the explanatory caption line")
    explanation = lines[idx].strip()
    idx += 1
    return title, explanation, idx


def emit_figure(
    output: list[str],
    markdown_path: Path,
    rst_path: Path,
    src: str,
    alt: str,
    title: str,
    explanation: str,
) -> None:
    image_path = resolve_markdown_path(markdown_path, src)
    if not image_path.exists():
        raise RuntimeError(f"Missing image: {repo_relative(image_path)}")
    output.extend(
        [
            f".. figure:: {relative_path_for_rst(image_path, rst_path)}",
            f"   :alt: {alt}",
            "   :align: center",
            "   :width: 100%",
            "   :class: paper-note-figure",
            "",
            f"   {convert_inline(title)}",
            "",
            f"   {convert_inline(explanation)}",
            "",
        ]
    )


def emit_cover(output: list[str], cover_path: Path | None, rst_path: Path, title: str) -> None:
    if cover_path is None:
        return
    if not cover_path.exists():
        raise RuntimeError(f"Missing cover image: {repo_relative(cover_path)}")
    output.extend(
        [
            f".. image:: {relative_path_for_rst(cover_path, rst_path)}",
            f"   :alt: {title}",
            "   :align: center",
            "   :width: 100%",
            "   :class: paper-note-cover",
            "",
        ]
    )


def convert_markdown_to_rst(
    markdown_path: Path,
    review_path: Path,
    rst_path: Path,
    backlog_path: Path | None = None,
) -> str:
    markdown_text = markdown_path.read_text(encoding="utf-8")
    lines = markdown_text.splitlines()
    title = strip_title_category_prefix(parse_title(markdown_text))
    publication_ref = markdown_path.stem
    output: list[str] = [
        f".. _paper-note-{publication_ref}:",
        "",
        ".. role:: student-first-author",
        "",
    ]
    output.extend(heading(title, "="))
    emit_cover(output, find_review_cover(review_path), rst_path, title)

    idx = 0
    if lines and lines[0].startswith("# "):
        idx = 1
    paragraph: list[str] = []
    while idx < len(lines):
        line = lines[idx]
        stripped = line.strip()
        if not stripped:
            emit_paragraph(paragraph, output)
            if output and output[-1] != "":
                output.append("")
            idx += 1
            continue
        if stripped.startswith("## "):
            emit_paragraph(paragraph, output)
            output.extend(heading(stripped[3:].strip(), "-"))
            idx += 1
            continue
        if stripped.startswith("### "):
            emit_paragraph(paragraph, output)
            output.extend(heading(stripped[4:].strip(), "~"))
            idx += 1
            continue
        image = markdown_image(stripped)
        if image:
            emit_paragraph(paragraph, output)
            alt, src = image
            fig_title, fig_explanation, idx = consume_caption(lines, idx + 1)
            emit_figure(output, markdown_path, rst_path, src, alt, fig_title, fig_explanation)
            continue
        if stripped == "$$":
            emit_paragraph(paragraph, output)
            idx += 1
            math_lines: list[str] = []
            while idx < len(lines) and lines[idx].strip() != "$$":
                math_lines.append(lines[idx].strip())
                idx += 1
            if idx >= len(lines):
                raise RuntimeError("Unclosed display math block")
            output.extend([".. math::", ""])
            output.extend(f"   {math_line}" for math_line in math_lines if math_line)
            output.append("")
            idx += 1
            continue
        if re.match(r"[-*]\s+", stripped):
            emit_paragraph(paragraph, output)
            content = re.sub(r"^[-*]\s+", "", stripped)
            output.append(f"- {convert_inline(content)}")
            idx += 1
            continue
        if re.match(r"\d+\.\s+", stripped):
            emit_paragraph(paragraph, output)
            number, content = stripped.split(".", 1)
            output.append(f"{number}. {convert_inline(content.strip())}")
            idx += 1
            continue
        paragraph.append(stripped)
        idx += 1

    emit_paragraph(paragraph, output)
    emit_citation_section(output, publication_ref)
    emit_rtd_related_navigation(
        output,
        publication_ref,
        backlog_path=backlog_path or WECHAT_ROOT / "backlog/selected-papers.yml",
        notes_dir=rst_path.parent,
        article_dir=markdown_path.parent,
    )
    return "\n".join(output).rstrip() + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publication-ref", default=DEFAULT_REF)
    parser.add_argument("--article", type=Path)
    parser.add_argument("--review", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("--check", action="store_true", help="Fail if the output file differs")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    article = args.article or WECHAT_ROOT / f"articles/draft-public-safe/{args.publication_ref}.md"
    review = args.review or WECHAT_ROOT / f"articles/review/{args.publication_ref}.review.md"
    output = args.output or REPO_ROOT / f"docs/source/paper-notes/{args.publication_ref}.rst"
    rst = convert_markdown_to_rst(article.resolve(), review.resolve(), output.resolve())
    if args.check:
        existing = output.read_text(encoding="utf-8") if output.exists() else ""
        if existing != rst:
            print(f"RTD companion page is out of sync: {repo_relative(output)}")
            return 1
        print(f"RTD companion page is in sync: {repo_relative(output)}")
        return 0
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rst, encoding="utf-8")
    print(repo_relative(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
