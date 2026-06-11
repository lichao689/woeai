# WOEAI WeChat Themes

WOEAI maintains API renderer themes, used by
`wechat/tools/render-copy-ready.py` and `wechat/tools/wechat_draft.py` when
submitting HTML through the official WeChat draft API.

Current API renderer theme:

- `academic-clean`: default scholarly paper-explainer style.
- `engineering-note`: applied technical style for engineering readers and
  collaboration-facing articles.
- `recruitment-friendly`: warmer direction-introduction style for
  recruitment-facing articles.

Themes change presentation only. They must not change article facts, section
order, citations, formula semantics, image approval, or public-safety
boundaries.

Promote a future preview into production only after:

1. adding an API renderer theme name,
2. generating a local preview,
3. checking the WeChat backend mobile preview,
4. documenting the intended article type and usage.
