"""Parse associated paper figures without changing their text or image sources."""
from dataclasses import dataclass
import re


IMAGE = re.compile(r"!\[(.*?)\]\((.*?)\)")
CAPTION = re.compile(r"(?:论文图|图|Figure|Fig\.)\s*(\d+)(?!\d)(.*)")
BOUNDARY = re.compile(r"^(?:#{1,6}\s|!\[|\$\$|:::|`{3,}|~{3,}|[-*+]\s|\d+[.)]\s)")


@dataclass(frozen=True)
class FigureGroup:
    start: int
    end: int
    number: str
    alt: str
    source: str
    title: str
    guide: str


def paragraph_at(lines: list[str], start: int) -> tuple[str, int, int]:
    while start < len(lines) and not lines[start].strip():
        start += 1
    end = start
    while end < len(lines) and lines[end].strip() and not BOUNDARY.match(lines[end].strip()):
        end += 1
    return " ".join(line.strip() for line in lines[start:end]), start, end


def parse_figure_groups(text: str) -> tuple[list[FigureGroup], list[str]]:
    """Return figure blocks and line-numbered diagnostics; offsets are zero-based."""
    lines = text.splitlines()
    groups = []
    findings = []
    index = 0
    in_math = False
    fence = ""
    while index < len(lines):
        stripped = lines[index].strip()
        code_fence = re.match(r"(`{3,}|~{3,})", stripped)
        if fence:
            if code_fence and code_fence[1][0] == fence[0] and len(code_fence[1]) >= len(fence):
                fence = ""
            index += 1
            continue
        if not in_math and code_fence:
            fence = code_fence[1]
            index += 1
            continue
        if stripped == "$$":
            in_math = not in_math
            index += 1
            continue
        if in_math:
            index += 1
            continue
        image = IMAGE.fullmatch(lines[index].strip())
        caption = CAPTION.fullmatch(image[1]) if image else None
        if caption:
            title, _, title_end = paragraph_at(lines, index + 1)
            guide, _, end = paragraph_at(lines, title_end)
            if title != image[1]:
                findings.append(f"line {index + 1}: figure {caption[1]} missing title matching image alt")
            elif not guide:
                findings.append(f"line {index + 1}: figure {caption[1]} missing guide paragraph")
            else:
                groups.append(FigureGroup(index, end, caption[1], *image.groups(), title, guide))
                index = end
                continue
        opener = re.fullmatch(r"::: figure ([1-9]\d*)", lines[index].strip())
        if not opener:
            if lines[index].strip().startswith("::: figure"):
                findings.append(f"line {index + 1}: figure opener requires a positive original number")
            elif lines[index].strip() == ":::":
                findings.append(f"line {index + 1}: unexpected closing :::")
            index += 1
            continue
        end = index + 1
        while end < len(lines) and lines[end].strip() != ":::":
            end += 1
        if end == len(lines):
            findings.append(f"line {index + 1}: figure {opener[1]} missing closing :::")
            break
        blocks = re.split(r"\n\s*\n", "\n".join(lines[index + 1:end]).strip())
        image = IMAGE.fullmatch(blocks[0]) if blocks else None
        if len(blocks) != 3 or not image:
            findings.append(f"line {index + 1}: figure {opener[1]} requires image, title and guide paragraphs")
        elif any(BOUNDARY.match(line.strip()) for line in blocks[1].splitlines()):
            findings.append(f"line {index + 1}: figure {opener[1]} requires a plain title paragraph")
        elif any(BOUNDARY.match(line.strip()) for line in blocks[2].splitlines()):
            findings.append(f"line {index + 1}: figure {opener[1]} requires a plain guide paragraph")
        else:
            groups.append(FigureGroup(index, end + 1, opener[1], *image.groups(),
                                      " ".join(blocks[1].splitlines()), " ".join(blocks[2].splitlines())))
        index = end + 1
    for group in groups:
        prefix = f"line {group.start + 1}: figure {group.number}"
        caption = CAPTION.fullmatch(group.title)
        if not caption or not caption[2].strip(" .:：、"):
            findings.append(f"{prefix} missing title with original figure number")
        elif caption[1] != group.number:
            findings.append(f"{prefix} title number does not match original number")
        if group.alt != group.title:
            findings.append(f"{prefix} image alt must exactly match title")
        if not group.guide or any(BOUNDARY.match(line.strip()) for line in group.guide.splitlines()):
            findings.append(f"{prefix} missing guide paragraph (headings, lists, images and display math are not guides)")
    return groups, findings
