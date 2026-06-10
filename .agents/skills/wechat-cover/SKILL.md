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
3. Before generating or selecting any cover image, run the mandatory cover-text
   confirmation gate below. Record the confirmed text choice in the cover brief
   or review note before proceeding.
4. Generate cover candidates only through the image-generation route with the
   confirmed cover text embedded in the image. Produce at least three
   image-gen-text candidates in each round. Reject any candidate with
   distorted, misspelled, incomplete, rewritten, low-contrast, or unreadable
   Chinese text.
5. Store public-safe cover outputs under
   `wechat/assets/public-safe/<publication_ref>/`. Keep private experiments
   under ignored local paths such as `wechat/.local/`.
6. Export the chosen final cover to the current target ratio. The default first
   cover target is `900 x 383 px`, but verify current WeChat guidance before
   hard-coding a new standard.
7. Run the crop preview helper:

   ```bash
   python .agents/skills/wechat-cover/scripts/cover_preview.py \
     wechat/assets/public-safe/<publication_ref>/<cover-file>.png \
     --label "候选 A" \
     --score article_specificity=4,click_appeal=5
   ```

   Treat this as a local first-pass comparison board. It checks dimensions,
   common crops, and small-thumbnail readability surfaces, but final approval
   still requires the WeChat backend mobile preview.
8. Update the review note with:
   - candidate count,
   - selected candidate ID,
   - user-confirmed cover text choice,
   - selected text mode: `image-gen-text`,
   - rejected candidate reasons,
   - cover source or prompt,
   - generation tool,
   - source candidate path,
   - final cover path,
   - dimensions,
   - local crop-preview path,
   - approval state,
   - WeChat backend preview state.
9. Run the relevant checks:
   - `python scripts/check-public-safe-content.py`
   - `git diff --check`
   - `python wechat/tools/wechat_draft.py dry-run --publication-ref <ref>`
     when the draft API path should see the selected cover.

If all candidates in a round fail because the text is wrong, unreadable, or the
visual is not article-specific, retry once with the same confirmed text. If two
rounds fail, stop and ask the user to confirm shorter or clearer cover text.
Do not use no-text covers or post-generation text overlays as fallbacks.

## Mandatory Cover-Text Confirmation

Before any new cover-generation round, ask the user to choose the exact text
plan that may appear on the cover. Do this after extracting the brief and before
calling an image-generation tool or selecting a candidate. Do not infer
approval from silence or from a generic "continue".

Present exactly five concrete cover-text combinations plus one custom-text
option, then wait for the user's reply. The first five options should be ready
to use on the cover, not abstract text modes:

1. `category tag` + `8-14 character Chinese hook`.
2. `category tag` + an alternate `8-14 character Chinese hook`.
3. `category tag` + a more engineering-facing `8-14 character Chinese hook`.
4. `category tag` + a more reader-facing `8-14 character Chinese hook`.
5. `category tag` + a more method- or finding-focused `8-14 character Chinese hook`.
6. Custom cover text supplied by the user.

Use the article category from `wechat/STYLE.md` when suggesting category tags.
Each option should follow this structure:

`category tag | main hook / optional subtitle`

The category tag must be `数值风洞`, `结构抗风`, or `漂浮风电`. Derive hooks only
from public-safe article wording or the cover brief. Keep the main hook short,
preferably 6-12 Chinese characters. Include a subtitle only when it helps the
meaning and is likely to remain readable in the small-thumbnail preview. If the
user chooses custom text, ask for the exact category tag, hook, and optional
subtitle before continuing. If the user asks for a no-text cover, explain that
this skill requires confirmed cover text and ask them to choose or provide text.

Record the confirmed choice in the cover brief or review note with:

- `cover_text_confirmation: user-confirmed`,
- `confirmed_cover_text`,
- `confirmed_text_mode`: `image-gen-text`,
- `confirmation_note`: short public-safe note such as "confirmed in chat".

## Cover Quality Rules

- Make the visual specific to the article, not generic science decoration.
- Keep the main subject centered for square and share-card crops.
- Make the main subject recognizable in one second on a phone-sized thumbnail.
- Every final cover must include the confirmed cover text generated directly in
  the image. Prefer a category tag plus a short Chinese hook; do not repeat the
  full article title.
- Use paper figures as source inspiration only when they remain legible as a
  cover; do not use a detailed paper figure as the default cover.
- Score candidates for article specificity, main-subject clarity, click appeal,
  engineering credibility, small-thumbnail readability, crop safety, and text
  quality when text is present.
- Reject candidates that look like generic AI technology wallpaper, have a
  faint or tiny subject, depend on dense labels/formulas, or include fake UI/map
  labels or misleading publication claims.
- Do not include unconfirmed partner names, private project details, private
  preview URLs, raw WeChat API responses, credentials, or tokens.
- Do not mark `cover_image_checked: true` until the WeChat backend preview has
  actually been checked.

## Helper Script

Use `scripts/cover_preview.py` from the repository root. It outputs a local HTML
candidate comparison board under `wechat/.local/cover-previews/` and prints
dimension, ratio, file-size, label, and optional score metadata.
