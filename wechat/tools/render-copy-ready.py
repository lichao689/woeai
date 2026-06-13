#!/usr/bin/env python3
"""Render a WOEAI WeChat Markdown article to a copy-ready local HTML page.

This is intentionally a small WOEAI-specific renderer. It covers the article
shape used in `wechat/articles/draft-public-safe/`: headings, paragraphs,
lists, images with following captions, bold text, links, inline math, and
display math. Math output defaults to MathJax SVG pre-rendering; the
lightweight renderer is only a limited fallback for selected LaTeX patterns.
The output is a local HTML file with inline styles, so copying from the browser
into the WeChat Official Account editor has a better chance of keeping the
layout.
"""

from __future__ import annotations

import argparse
import base64
import html
import mimetypes
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


WECHAT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = WECHAT_ROOT.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

DEFAULT_ARTICLE = WECHAT_ROOT / "articles/draft-public-safe/ref-zhao2026-BS.md"
DEFAULT_OUTPUT = WECHAT_ROOT / ".local/exports/ref-zhao2026-BS.academic-clean.html"
MATHJAX_SVG_SCRIPT = WECHAT_ROOT / "tools/render_mathjax_svg.cjs"

from woeai.wechat.options import (  # noqa: E402,F401
    AVAILABLE_MATH_RENDERERS,
    AVAILABLE_THEMES,
    DEFAULT_MATH_RENDERER,
    DEFAULT_THEME,
    validate_math_renderer,
    validate_theme,
)


BASE_STYLES = {
    "article": (
        "max-width:677px;margin:0 auto;padding:24px 18px 44px;"
        "font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;"
        "font-size:16px;line-height:1.86;color:#1f2933;background:#ffffff;"
    ),
    "h1": (
        "margin:0 0 18px;padding:0 0 16px;border-bottom:2px solid #23486f;"
        "font-size:25px;line-height:1.36;color:#0f2d52;font-weight:700;"
    ),
    "h2": (
        "margin:34px 0 15px;padding:0 0 0 12px;border-left:4px solid #2f6f9f;"
        "font-size:20px;line-height:1.38;color:#153a63;font-weight:700;"
    ),
    "h3": (
        "margin:25px 0 12px;font-size:17px;line-height:1.45;"
        "color:#24364b;font-weight:700;"
    ),
    "p": "margin:0 0 16px;",
    "ul": "margin:0 0 18px;padding-left:20px;",
    "ol": "margin:0 0 18px;padding-left:22px;",
    "li": "margin:0 0 8px;",
    "a": (
        "color:#0f5f95;text-decoration:underline;text-underline-offset:3px;"
        "font-weight:600;word-break:break-word;"
    ),
    "student_first_author": (
        "text-decoration:underline;text-underline-offset:3px;"
        "text-decoration-thickness:1px;"
    ),
    "img": "display:block;width:100%;height:auto;margin:22px auto 8px;",
    "caption": (
        "margin:0 0 24px;padding-left:10px;border-left:3px solid #c3d6e4;"
        "font-size:13px;line-height:1.68;color:#59636f;"
    ),
    "caption_title": (
        "margin:0;padding:10px 12px 4px;background:#f4f8fb;"
        "font-size:15px;line-height:1.55;text-align:center;font-style:italic;"
        "color:#1f3c56;font-weight:500;"
    ),
    "caption_body": (
        "margin:0 0 24px;padding:0 12px 10px 12px;background:#f4f8fb;"
        "font-size:13px;line-height:1.7;text-align:center;color:#586879;"
    ),
    "math_inline": (
        "font-family:'Times New Roman',Georgia,serif;letter-spacing:0;"
        "white-space:nowrap;font-size:1.02em;"
    ),
    "formula": (
        "margin:18px 0;padding:16px;text-align:center;overflow-x:auto;"
        "border:1px solid #d4dee8;background:#f7fafc;color:#18344f;"
        "font-family:'Times New Roman',Georgia,serif;font-size:18px;line-height:1.5;"
    ),
    "button": (
        "position:sticky;top:0;z-index:10;display:flex;gap:10px;align-items:center;"
        "justify-content:center;padding:12px;background:#eef3f7;border-bottom:1px solid #d7dce2;"
        "font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;"
    ),
}

THEME_OVERRIDES = {
    "academic-clean": {},
    "engineering-note": {
        "article": (
            "max-width:677px;margin:0 auto;padding:24px 18px 44px;"
            "font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;"
            "font-size:16px;line-height:1.86;color:#162626;background:#fbfefd;"
        ),
        "h1": (
            "margin:0 0 18px;padding:0 0 14px;border-bottom:4px solid #13a08b;"
            "font-size:25px;line-height:1.36;color:#053b3c;font-weight:700;"
        ),
        "h2": (
            "margin:34px 0 15px;padding:9px 12px;border-left:5px solid #0f8f7a;"
            "background:#e6f6f3;font-size:20px;line-height:1.38;color:#063f44;font-weight:700;"
        ),
        "h3": (
            "margin:25px 0 12px;font-size:17px;line-height:1.45;"
            "color:#0b5c59;font-weight:700;"
        ),
        "caption": (
            "margin:0 0 24px;padding:10px 12px;background:#eef8f6;"
            "font-size:13px;line-height:1.68;color:#365d5b;"
        ),
        "caption_title": (
            "margin:0;padding:10px 12px 4px;background:#eef8f6;"
            "font-size:15px;line-height:1.55;text-align:center;font-style:italic;"
            "color:#064a46;font-weight:500;"
        ),
        "caption_body": (
            "margin:0 0 24px;padding:0 12px 10px 12px;background:#eef8f6;"
            "font-size:13px;line-height:1.7;text-align:center;color:#365d5b;"
        ),
        "formula": (
            "margin:18px 0;padding:16px;text-align:center;overflow-x:auto;"
            "border:1px solid #9dd8d0;background:#eefbf8;color:#043f42;"
            "font-family:'Times New Roman',Georgia,serif;font-size:18px;line-height:1.5;"
        ),
    },
    "recruitment-friendly": {
        "article": (
            "max-width:677px;margin:0 auto;padding:24px 18px 44px;"
            "font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;"
            "font-size:16px;line-height:1.86;color:#2f2a24;background:#fffdf9;"
        ),
        "h1": (
            "margin:0 0 18px;padding:0 0 14px;border-bottom:2px solid #c89452;"
            "font-size:25px;line-height:1.36;color:#58391f;font-weight:700;"
        ),
        "h2": (
            "margin:34px 0 15px;padding:0 0 0 14px;border-left:5px solid #d89c43;"
            "font-size:20px;line-height:1.38;color:#5b3519;font-weight:700;"
        ),
        "h3": (
            "margin:25px 0 12px;font-size:17px;line-height:1.45;"
            "color:#7a4b22;font-weight:700;"
        ),
        "caption": (
            "margin:0 0 24px;padding-left:10px;border-left:3px solid #ebc889;"
            "font-size:13px;line-height:1.68;color:#705d49;"
        ),
        "caption_title": (
            "margin:0;padding:10px 12px 4px;background:#fff8eb;"
            "font-size:15px;line-height:1.55;text-align:center;font-style:italic;"
            "color:#5b3519;font-weight:500;"
        ),
        "caption_body": (
            "margin:0 0 24px;padding:0 12px 10px 12px;background:#fff8eb;"
            "font-size:13px;line-height:1.7;text-align:center;color:#705d49;"
        ),
        "formula": (
            "margin:18px 0;padding:16px;text-align:center;overflow-x:auto;"
            "border:1px solid #ebd2ad;background:#fff8eb;color:#5b3b24;"
            "font-family:'Times New Roman',Georgia,serif;font-size:18px;line-height:1.5;"
        ),
    },
}


def theme_styles(theme: str) -> dict[str, str]:
    validate_theme(theme)
    return {**BASE_STYLES, **THEME_OVERRIDES[theme]}


_MATHJAX_SVG_CACHE: dict[tuple[str, bool], str] = {}


def render_mathjax_svg(src: str, *, display: bool) -> str:
    key = (src.strip(), display)
    if key in _MATHJAX_SVG_CACHE:
        return _MATHJAX_SVG_CACHE[key]
    if not MATHJAX_SVG_SCRIPT.exists():
        raise RuntimeError(f"Missing MathJax SVG helper: {MATHJAX_SVG_SCRIPT}")
    payload = {"formulas": [{"id": "formula", "tex": key[0], "display": display}]}
    try:
        proc = subprocess.run(
            ["node", str(MATHJAX_SVG_SCRIPT)],
            input=json_dumps(payload),
            text=True,
            capture_output=True,
            check=False,
            timeout=30,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("Missing node executable; MathJax SVG formula rendering requires Node.js") from exc
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError("MathJax SVG renderer timed out") from exc
    if proc.returncode != 0:
        message = proc.stdout.strip() or proc.stderr.strip()
        raise RuntimeError(f"MathJax SVG renderer failed: {message}")
    try:
        data = json_loads(proc.stdout)
    except ValueError as exc:
        raise RuntimeError(f"MathJax SVG renderer returned invalid JSON: {proc.stdout[:200]}") from exc
    if not data.get("ok"):
        raise RuntimeError(f"MathJax SVG renderer failed: {data.get('error', 'unknown error')}")
    items = data.get("items") or []
    if not items or "html" not in items[0]:
        raise RuntimeError("MathJax SVG renderer returned no formula HTML")
    result = str(items[0]["html"])
    _MATHJAX_SVG_CACHE[key] = result
    return result


def json_dumps(value: object) -> str:
    import json

    return json.dumps(value, ensure_ascii=False)


def json_loads(value: str) -> dict[str, object]:
    import json

    parsed = json.loads(value)
    if not isinstance(parsed, dict):
        raise ValueError("expected JSON object")
    return parsed


def styled(
    tag: str,
    content: str,
    style_key: str | None = None,
    styles: dict[str, str] | None = None,
    **attrs: str,
) -> str:
    active_styles = styles or theme_styles(DEFAULT_THEME)
    style = active_styles[style_key or tag]
    attr_parts = [f'style="{html.escape(style, quote=True)}"']
    for key, value in attrs.items():
        attr_parts.append(f'{key}="{html.escape(value, quote=True)}"')
    return f"<{tag} {' '.join(attr_parts)}>{content}</{tag}>"


def inline_image_src(markdown_file: Path, raw_src: str, embed_images: bool) -> str:
    parsed = urlparse(raw_src)
    if parsed.scheme in {"http", "https"}:
        return raw_src
    image_path = (markdown_file.parent / raw_src).resolve()
    if not embed_images:
        return image_path.as_uri()
    mime = mimetypes.guess_type(image_path.name)[0] or "image/png"
    data = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


def render_inline(
    text: str,
    styles: dict[str, str] | None = None,
    math_renderer: str = DEFAULT_MATH_RENDERER,
) -> str:
    active_styles = styles or theme_styles(DEFAULT_THEME)
    math_renderer = validate_math_renderer(math_renderer)
    placeholders: list[str] = []

    def store(value: str) -> str:
        placeholders.append(value)
        return f"\u0000{len(placeholders) - 1}\u0000"

    def render_escaped_markup(value: str) -> str:
        value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
        return value.replace(r"\*", "*")

    def math_repl(match: re.Match[str]) -> str:
        return store(render_inline_math(match.group(1), styles=active_styles, math_renderer=math_renderer))

    text = re.sub(r"\$([^$\n]+)\$", math_repl, text)

    def student_first_author_repl(match: re.Match[str]) -> str:
        inner = render_escaped_markup(html.escape(match.group(1).strip()))
        return store(
            '<span style="{}">{}</span>'.format(
                html.escape(active_styles["student_first_author"], quote=True),
                inner,
            )
        )

    text = re.sub(r"<u>(.+?)</u>", student_first_author_repl, text)

    def link_repl(match: re.Match[str]) -> str:
        label, href = match.groups()
        return store(
            '<a href="{}" style="{}">{}</a>'.format(
                html.escape(href, quote=True),
                html.escape(active_styles["a"], quote=True),
                html.escape(label),
            )
        )

    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", link_repl, text)
    escaped = html.escape(text)
    escaped = render_escaped_markup(escaped)

    for idx, value in enumerate(placeholders):
        escaped = escaped.replace(f"\u0000{idx}\u0000", value)
    return escaped


def render_inline_math(
    src: str,
    styles: dict[str, str] | None = None,
    math_renderer: str = DEFAULT_MATH_RENDERER,
) -> str:
    active_styles = styles or theme_styles(DEFAULT_THEME)
    math_renderer = validate_math_renderer(math_renderer)
    if math_renderer == "mathjax-svg":
        return render_mathjax_svg(src, display=False)
    src = src.strip()
    fragments: list[str] = []

    def store_fragment(value: str) -> str:
        fragments.append(value)
        return f"\u0001{len(fragments) - 1}\u0001"

    def normal_text(value: str) -> str:
        return store_fragment(f'<span style="font-style:normal;">{html.escape(value)}</span>')

    def simple_script(value: str) -> str:
        escaped = html.escape(value)
        if len(value) == 1 and value.isalpha():
            return f"<em>{escaped}</em>"
        return escaped

    src = src.replace(r"\,", " ")
    src = src.replace(r"\times", "×")
    src = src.replace(r"^\circ", "°")
    src = src.replace(r"\circ", "°")
    src = src.replace(r"\%", "%")
    src = re.sub(r"\\mathrm\{([^}]+)\}", lambda m: normal_text(m.group(1)), src)
    src = re.sub(r"\\(max|min|sin|cos|tan|log|ln)\b", lambda m: normal_text(m.group(1)), src)
    src = re.sub(
        r"([A-Za-z])_\{([^}]+)\}",
        lambda m: store_fragment(
            f'<em>{html.escape(m.group(1))}</em><sub>'
            f'{render_inline_math(m.group(2), styles=active_styles, math_renderer=math_renderer)}</sub>'
        ),
        src,
    )
    src = re.sub(
        r"([A-Za-z])_([A-Za-z0-9]+)",
        lambda m: store_fragment(f'<em>{html.escape(m.group(1))}</em><sub>{simple_script(m.group(2))}</sub>'),
        src,
    )
    src = re.sub(
        r"([A-Za-z])\^\{([^}]+)\}",
        lambda m: store_fragment(
            f'<em>{html.escape(m.group(1))}</em><sup>'
            f'{render_inline_math(m.group(2), styles=active_styles, math_renderer=math_renderer)}</sup>'
        ),
        src,
    )
    src = re.sub(
        r"([A-Za-z])\^([A-Za-z0-9]+)",
        lambda m: store_fragment(f'<em>{html.escape(m.group(1))}</em><sup>{simple_script(m.group(2))}</sup>'),
        src,
    )
    src = re.sub(r"\b([A-Za-z])\b", lambda m: f"<em>{m.group(1)}</em>", src)
    for _ in range(4):
        changed = False
        for idx, value in enumerate(fragments):
            token = f"\u0001{idx}\u0001"
            if token in src:
                src = src.replace(token, value)
                changed = True
        if not changed:
            break
    return f'<span style="{html.escape(active_styles["math_inline"], quote=True)}">{src}</span>'


def render_display_math(
    src: str,
    styles: dict[str, str] | None = None,
    math_renderer: str = DEFAULT_MATH_RENDERER,
) -> str:
    math_renderer = validate_math_renderer(math_renderer)
    compact = " ".join(line.strip() for line in src.strip().splitlines())
    if math_renderer == "mathjax-svg":
        return styled("div", render_mathjax_svg(compact, display=True), "formula", styles=styles)
    known = r"E = \frac{K_{\mathrm{CFD}} - K_{\mathrm{m}}}{K_{\mathrm{m}}} \times 100\%"
    if compact == known:
        return styled(
            "div",
            (
                '<span style="font-style:italic;">E</span>'
                '<span style="padding:0 8px;">=</span>'
                '<span style="display:inline-block;vertical-align:middle;text-align:center;">'
                '<span style="display:block;padding:0 8px;border-bottom:1px solid #18344f;">'
                '<span style="font-style:italic;">K</span><sub style="font-style:normal;">CFD</sub>'
                '<span style="padding:0 6px;">−</span>'
                '<span style="font-style:italic;">K</span><sub style="font-style:normal;">m</sub>'
                '</span>'
                '<span style="display:block;padding:3px 8px 0;">'
                '<span style="font-style:italic;">K</span><sub style="font-style:normal;">m</sub>'
                '</span>'
                '</span>'
                '<span style="padding:0 8px;">×</span>100%'
            ),
            "formula",
            styles=styles,
        )
    return styled("div", render_inline_math(compact, styles=styles, math_renderer=math_renderer), "formula", styles=styles)


def flush_paragraph(
    paragraph: list[str],
    output: list[str],
    styles: dict[str, str],
    math_renderer: str,
) -> None:
    if paragraph:
        output.append(
            styled(
                "p",
                render_inline(" ".join(paragraph), styles=styles, math_renderer=math_renderer),
                "p",
                styles=styles,
            )
        )
        paragraph.clear()


def flush_list(
    list_items: list[str],
    output: list[str],
    ordered: bool,
    styles: dict[str, str],
    math_renderer: str,
) -> None:
    if list_items:
        tag = "ol" if ordered else "ul"
        body = "".join(
            styled("li", render_inline(item, styles=styles, math_renderer=math_renderer), "li", styles=styles)
            for item in list_items
        )
        output.append(styled(tag, body, tag, styles=styles))
        list_items.clear()


def render_markdown(
    markdown_file: Path,
    embed_images: bool,
    include_title: bool = False,
    theme: str = DEFAULT_THEME,
    math_renderer: str = DEFAULT_MATH_RENDERER,
) -> str:
    styles = theme_styles(theme)
    math_renderer = validate_math_renderer(math_renderer)
    lines = markdown_file.read_text(encoding="utf-8").splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    ordered = False
    in_math = False
    math_lines: list[str] = []
    previous_was_image = False
    caption_explanation_pending = False

    for line in lines:
        stripped = line.strip()

        if in_math:
            if stripped == "$$":
                output.append(render_display_math("\n".join(math_lines), styles=styles, math_renderer=math_renderer))
                math_lines.clear()
                in_math = False
            else:
                math_lines.append(line)
            continue

        if stripped == "$$":
            flush_paragraph(paragraph, output, styles, math_renderer)
            flush_list(list_items, output, ordered, styles, math_renderer)
            in_math = True
            previous_was_image = False
            caption_explanation_pending = False
            continue

        if not stripped:
            flush_paragraph(paragraph, output, styles, math_renderer)
            flush_list(list_items, output, ordered, styles, math_renderer)
            continue

        image_match = re.match(r"!\[(.*?)\]\((.*?)\)", stripped)
        if image_match:
            flush_paragraph(paragraph, output, styles, math_renderer)
            flush_list(list_items, output, ordered, styles, math_renderer)
            alt, src = image_match.groups()
            output.append(
                f'<img src="{html.escape(inline_image_src(markdown_file, src, embed_images), quote=True)}" '
                f'alt="{html.escape(alt, quote=True)}" style="{html.escape(styles["img"], quote=True)}">'
            )
            previous_was_image = True
            caption_explanation_pending = False
            continue

        if stripped.startswith("# "):
            flush_paragraph(paragraph, output, styles, math_renderer)
            flush_list(list_items, output, ordered, styles, math_renderer)
            if include_title:
                output.append(
                    styled(
                        "h1",
                        render_inline(stripped[2:], styles=styles, math_renderer=math_renderer),
                        "h1",
                        styles=styles,
                    )
                )
            previous_was_image = False
            caption_explanation_pending = False
            continue

        if stripped.startswith("## "):
            flush_paragraph(paragraph, output, styles, math_renderer)
            flush_list(list_items, output, ordered, styles, math_renderer)
            output.append(
                styled(
                    "h2",
                    render_inline(stripped[3:], styles=styles, math_renderer=math_renderer),
                    "h2",
                    styles=styles,
                )
            )
            previous_was_image = False
            caption_explanation_pending = False
            continue

        if stripped.startswith("### "):
            flush_paragraph(paragraph, output, styles, math_renderer)
            flush_list(list_items, output, ordered, styles, math_renderer)
            output.append(
                styled(
                    "h3",
                    render_inline(stripped[4:], styles=styles, math_renderer=math_renderer),
                    "h3",
                    styles=styles,
                )
            )
            previous_was_image = False
            caption_explanation_pending = False
            continue

        unordered_match = re.match(r"[-*]\s+(.*)", stripped)
        ordered_match = re.match(r"\d+\.\s+(.*)", stripped)
        if unordered_match or ordered_match:
            flush_paragraph(paragraph, output, styles, math_renderer)
            this_ordered = bool(ordered_match)
            if list_items and ordered != this_ordered:
                flush_list(list_items, output, ordered, styles, math_renderer)
            ordered = this_ordered
            list_items.append((ordered_match or unordered_match).group(1))
            previous_was_image = False
            caption_explanation_pending = False
            continue

        flush_list(list_items, output, ordered, styles, math_renderer)
        if previous_was_image and re.match(r"^(Figure|Fig\.)\s*\d+|^图\s*\d+", stripped):
            output.append(
                styled(
                    "p",
                    render_inline(stripped, styles=styles, math_renderer=math_renderer),
                    "caption_title",
                    styles=styles,
                )
            )
            previous_was_image = False
            caption_explanation_pending = True
        elif caption_explanation_pending:
            output.append(
                styled(
                    "p",
                    render_inline(stripped, styles=styles, math_renderer=math_renderer),
                    "caption_body",
                    styles=styles,
                )
            )
            caption_explanation_pending = False
        else:
            paragraph.append(stripped)
            previous_was_image = False

    flush_paragraph(paragraph, output, styles, math_renderer)
    flush_list(list_items, output, ordered, styles, math_renderer)
    return "\n".join(output)


def render_page(article_html: str, title: str, theme: str = DEFAULT_THEME) -> str:
    styles = theme_styles(theme)
    button_style = styles["button"]
    button_inner_style = (
        "border:0;background:#23486f;color:#fff;padding:8px 14px;"
        "font-size:14px;border-radius:4px;cursor:pointer;"
    )
    note_style = "font-size:13px;color:#4b5563;"
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
</head>
<body style="margin:0;background:#eef1f4;">
  <div style="{html.escape(button_style, quote=True)}">
    <button id="copy" style="{html.escape(button_inner_style, quote=True)}">复制公众号正文</button>
    <span id="status" style="{html.escape(note_style, quote=True)}">复制后粘贴到公众号编辑器。若图片没带过去，再手动上传图片。</span>
  </div>
  <main id="article" style="{html.escape(styles["article"], quote=True)}">
{article_html}
  </main>
  <script>
    const button = document.getElementById('copy');
    const status = document.getElementById('status');
    button.addEventListener('click', async () => {{
      const article = document.getElementById('article');
      const html = article.outerHTML;
      const text = article.innerText;
      try {{
        if (navigator.clipboard && window.ClipboardItem) {{
          await navigator.clipboard.write([
            new ClipboardItem({{
              'text/html': new Blob([html], {{type: 'text/html'}}),
              'text/plain': new Blob([text], {{type: 'text/plain'}})
            }})
          ]);
        }} else {{
          const range = document.createRange();
          range.selectNode(article);
          const selection = window.getSelection();
          selection.removeAllRanges();
          selection.addRange(range);
          document.execCommand('copy');
          selection.removeAllRanges();
        }}
        status.textContent = '已复制。现在可以去公众号编辑器粘贴。';
      }} catch (error) {{
        const range = document.createRange();
        range.selectNode(article);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        status.textContent = '浏览器限制了自动复制：正文已选中，请按 Command+C。';
      }}
    }});
  </script>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("article", nargs="?", type=Path, default=DEFAULT_ARTICLE)
    parser.add_argument("-o", "--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--theme", default=DEFAULT_THEME, choices=AVAILABLE_THEMES)
    parser.add_argument("--math-renderer", default=DEFAULT_MATH_RENDERER, choices=AVAILABLE_MATH_RENDERERS)
    parser.add_argument(
        "--include-title",
        action="store_true",
        help="Render the Markdown H1 inside the body. The default is body-only for WeChat drafts.",
    )
    parser.add_argument("--no-embed-images", action="store_true")
    args = parser.parse_args()

    validate_theme(args.theme)
    validate_math_renderer(args.math_renderer)
    article = args.article.resolve()
    output = args.output.resolve()
    article_html = render_markdown(
        article,
        embed_images=not args.no_embed_images,
        include_title=args.include_title,
        theme=args.theme,
        math_renderer=args.math_renderer,
    )
    first_line = article.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_page(article_html, first_line, theme=args.theme), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
