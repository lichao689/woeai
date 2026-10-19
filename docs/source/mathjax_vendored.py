"""Point the vendored MathJax at the fonts that ship next to it.

Two problems had to be solved to vendor MathJax instead of pointing at
cdn.jsdelivr.net:

1. Sphinx's ``mathjax4_config`` is a *static* value. MathJax substitutes
   ``chtml.fontURL`` verbatim into the ``@font-face`` rules it injects into the
   page, so whatever is configured becomes a URL relative to the *document*.
   A relative fontURL therefore loads on a top-level page and 404s one
   directory deeper (every ``paper-notes/<ref>.html``).
2. The bundle ships with ``fontURL`` ``"@mathjax/mathjax-newcm-font/js/chtml/
   woff2"``, an import-map style path that MathJax resolves through
   ``config.loader.paths.fonts``. In a browser that defaults to a jsDelivr URL,
   which is useless for a self-hosted copy.

``pathto(..., 1)`` returns a root-relative path Sphinx recomputes per page
depth, so the config is injected per page with that value. It is appended to the
rendered body as an inline script: Sphinx loads MathJax with ``defer``, and
inline scripts always run before deferred ones, so the configuration is in place
before MathJax executes even though it appears later in the document.
"""
from __future__ import annotations

import re

# Sphinx renders math for MathJax as <span class="math notranslate nohighlight">.
# The trailing classes vary, so match the class attribute rather than a fixed
# string.
MATH_MARKUP = re.compile(r'class="math(?:\s[^"]*)?"')

MATHJAX_FONT_DIR = "_static/mathjax/fonts/woff2"


def mathjax_config(static_prefix: str) -> str:
    """Return the ``window.MathJax`` assignment for one page."""
    return 'window.MathJax = {"chtml": {"fontURL": "%s"}}' % static_prefix


def _configure_page(app, pagename, templatename, context, doctree):
    body = context.get("body")
    if not body or not MATH_MARKUP.search(body):
        return
    config = mathjax_config(context["pathto"](MATHJAX_FONT_DIR, 1))
    context["body"] = f"{body}<script>{config}</script>"


def setup(app):
    app.connect("html-page-context", _configure_page)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
