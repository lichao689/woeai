---
name: wechat-cover
description: Use when generating, improving, reviewing, or recording WOEAI WeChat Official Account cover images for paper articles, including cover briefs, image-generation prompts, candidate concepts, crop-safety previews, public-safe cover assets, and review-note cover metadata.
---

# WeChat Cover

Create WOEAI WeChat paper-article cover images that are content-aware,
public-safe, and suitable for WeChat crop behavior.

## Required Context

Read only what the task needs:

1. `AGENTS.md` for public-safety and WeChat API rules.
2. `wechat/STYLE.md` for current cover rules.
3. The target article in `wechat/articles/draft-public-safe/`.
4. The target review note in `wechat/articles/review/`.
5. `references/cover-standards.md` when choosing dimensions, writing prompts,
   or comparing candidate directions.

If the task is part of a full paper-article workflow, use `wechat-paper` for
the article and API path, then use this skill for the cover stage.

## Workflow

1. Extract the cover brief from the article:
   - title category,
   - article title,
   - abstract or core problem,
   - key method or finding,
   - target readers,
   - avoid list.
2. Create or update `wechat/articles/review/<publication_ref>.cover-brief.md`.
   Include at least three candidate concepts: research scene, method, and
   engineering impact.
3. Generate or select candidate images only from public-safe prompts and
   approved sources. Prefer no embedded text; generated Chinese text is usually
   too risky for a cover.
4. Store public-safe cover outputs under
   `wechat/assets/public-safe/<publication_ref>/`. Keep private experiments
   under ignored local paths such as `wechat/.local/`.
5. Export the chosen final cover to the current target ratio. The default first
   cover target is `900 x 383 px`, but verify current WeChat guidance before
   hard-coding a new standard.
6. Run the crop preview helper:

   ```bash
   python .agents/skills/wechat-cover/scripts/cover_preview.py \
     wechat/assets/public-safe/<publication_ref>/<cover-file>.png
   ```

   Treat this as a local first-pass check. Final approval still requires the
   WeChat backend mobile preview.
7. Update the review note with:
   - cover source or prompt,
   - generation tool,
   - source candidate path,
   - final cover path,
   - dimensions,
   - local crop-preview path,
   - approval state,
   - WeChat backend preview state.
8. Run the relevant checks:
   - `python scripts/check-public-safe-content.py`
   - `git diff --check`
   - `python wechat/tools/wechat_draft.py dry-run --publication-ref <ref>`
     when the draft API path should see the selected cover.

## Cover Quality Rules

- Make the visual specific to the article, not generic science decoration.
- Keep the main subject centered for square and share-card crops.
- Use paper figures as source inspiration only when they remain legible as a
  cover; do not use a detailed paper figure as the default cover.
- Do not include unconfirmed partner names, private project details, private
  preview URLs, raw WeChat API responses, credentials, or tokens.
- Do not mark `cover_image_checked: true` until the WeChat backend preview has
  actually been checked.

## Helper Script

Use `scripts/cover_preview.py` from the repository root. It outputs a local HTML
preview under `wechat/.local/cover-previews/` and prints dimension, ratio, and
file-size checks.
