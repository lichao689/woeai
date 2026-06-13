"""Theme and math-renderer options for WOEAI WeChat article rendering.

The available themes and math renderers, plus their validators, were
duplicated (with drifting exception types) across ``render-copy-ready.py``
and ``wechat_draft.py``. Both now import from here.

Note: the two math renderers (``lightweight`` and ``mathjax-svg``) are
already two real adapters at a seam. The selection is currently a string
compare; a full renderer registry is a future option, but the immediate win
is making the allowed-values list a single source of truth.
"""

from __future__ import annotations

DEFAULT_THEME = "academic-clean"
AVAILABLE_THEMES = ("academic-clean", "engineering-note", "recruitment-friendly")
DEFAULT_MATH_RENDERER = "mathjax-svg"
AVAILABLE_MATH_RENDERERS = ("lightweight", "mathjax-svg")


def validate_theme(theme: str) -> str:
    if theme not in AVAILABLE_THEMES:
        options = ", ".join(AVAILABLE_THEMES)
        raise ValueError(f"Unsupported theme '{theme}'. Available themes: {options}")
    return theme


def validate_math_renderer(math_renderer: str) -> str:
    if math_renderer not in AVAILABLE_MATH_RENDERERS:
        options = ", ".join(AVAILABLE_MATH_RENDERERS)
        raise ValueError(
            f"Unsupported math renderer '{math_renderer}'. Available renderers: {options}"
        )
    return math_renderer
