"""Shared review metadata and one canonical current cover for both channels."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Literal

# Repo root: woeai/wechat/review.py -> parents[2]
_REPO_ROOT = Path(__file__).resolve().parents[2]



def parse_title(markdown_text: str) -> str:
    """Extract the H1 title from a markdown article's text.

    Raises RuntimeError if no ``# `` heading is present. Callers that read
    from a path should read the text then call this; it stays pure (no I/O)
    so it is trivially testable.
    """
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise RuntimeError("Markdown article is missing an H1 title")


def parse_front_matter(review_path: Path) -> dict[str, str]:
    """Parse the YAML-ish ``---`` front matter of a review note.

    Returns an empty dict if the file does not exist or has no front matter.
    """
    if not review_path.exists():
        return {}
    lines = review_path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    result: dict[str, str] = {}
    for raw in lines[1:]:
        if raw.strip() == "---":
            break
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def resolve_repo_path(value: str) -> Path:
    """Resolve a path that may be absolute or repo-relative."""
    path = Path(value).expanduser()
    if path.is_absolute():
        return path.resolve()
    return (_REPO_ROOT / path).resolve()


def find_review_cover(
    review_path: Path, *, channel: Literal["rtd", "wechat"] = "rtd", root: Path | None = None
) -> Path | None:
    """Return the one current public cover; channel is retained for caller compatibility.

    Historical channel fields and prose are audit context, never fallback selectors.
    """
    front = parse_front_matter(review_path)
    value = front.get("cover_image")
    if not value:
        return None
    ref = front.get("publication_ref", "")
    expected = f"wechat/assets/public-safe/{ref}/cover.png"
    if not re.fullmatch(r"ref-[A-Za-z0-9_-]+", ref) or value != expected:
        raise ValueError("Cover must use the paper's canonical public path")
    if front.get("wechat_cover_image") or front.get("rtd_cover_image"):
        raise ValueError("Retired channel cover selectors must be removed")
    base = (root or _REPO_ROOT).resolve()
    cover = base / expected
    if cover.resolve() != cover or not cover.is_file():
        raise ValueError("Canonical cover is missing or redirected")
    return cover
