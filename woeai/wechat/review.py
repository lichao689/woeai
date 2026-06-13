"""Review-note parsing shared across WeChat article tools.

The review note (``wechat/articles/review/<ref>.review.md``) carries
front-matter metadata and a 封面素材 cover reference. Parsing these was
duplicated across ``markdown_to_rtd.py`` and ``wechat_draft.py`` with drifting
contracts (one returned None for a missing cover, the other raised); both now
import from here and apply their own error policy on top.
"""

from __future__ import annotations

import re
from pathlib import Path

# Repo root: woeai/wechat/review.py -> parents[2]
_REPO_ROOT = Path(__file__).resolve().parents[2]

_COVER_RE = re.compile(r"-\s+封面素材:\s+`([^`]+)`")
_COVER_FRONT_MATTER_KEYS = ("rtd_cover_image", "wechat_cover_image", "cover_image")


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


def find_review_cover(review_path: Path) -> Path | None:
    """Find the cover image for a review note.

    Checks front-matter keys (rtd_cover_image / wechat_cover_image /
    cover_image) first, then falls back to the 封面素材 line. Returns None if
    no cover is recorded. Callers that require a cover should raise on None.
    """
    front = parse_front_matter(review_path)
    for key in _COVER_FRONT_MATTER_KEYS:
        if front.get(key):
            return resolve_repo_path(front[key])
    if not review_path.exists():
        return None
    text = review_path.read_text(encoding="utf-8")
    match = _COVER_RE.search(text)
    if match:
        return resolve_repo_path(match.group(1))
    return None
