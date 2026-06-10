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
4. Generate or select candidate images only from public-safe prompts and
   approved sources. Produce at least two candidate families when possible:
   no-text editorial visuals and short-text editorial visuals. Direct
   image-generation text is allowed as an experiment, but reject any candidate
   with distorted, misspelled, low-contrast, or unreadable text. Use
   deterministic programmatic text overlay when exact Chinese wording matters.
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
   - selected text mode: `none`, `image-gen-text`, or
     `programmatic-overlay`,
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

## Mandatory Cover-Text Confirmation

Before any new cover-generation round, ask the user to choose the exact text
plan that may appear on the cover. Do this after extracting the brief and before
calling an image-generation tool, selecting a candidate, or applying text
overlay. Do not infer approval from silence or from a generic "continue".

Present exactly five concrete cover-text combinations plus one custom-text
option, then wait for the user's reply. The first five options should be ready
to use on the cover, not abstract text modes:

1. `category tag` + `8-14 character Chinese hook`.
2. `category tag` + an alternate `8-14 character Chinese hook`.
3. `category tag` + a more engineering-facing `8-14 character Chinese hook`.
4. `category tag` + a more reader-facing `8-14 character Chinese hook`.
5. `category tag` + a more method- or finding-focused `8-14 character Chinese hook`.
6. Custom cover text supplied by the user.

Use the article category from `wechat/STYLE.md` when suggesting category tags,
and derive hooks only from public-safe article wording or the cover brief. A
short optional subtitle may be included only when it is needed for meaning and
is likely to remain readable in the small-thumbnail preview. If the user chooses
custom text, ask for the exact category tag, hook, and optional subtitle before
continuing. If the user asks for no text instead of choosing one of the six
options, confirm the no-text plan before continuing.

Record the confirmed choice in the cover brief or review note with:

- `cover_text_confirmation: user-confirmed`,
- `confirmed_cover_text`,
- `confirmed_text_mode`: `none`, `image-gen-text`, or
  `programmatic-overlay`,
- `confirmation_note`: short public-safe note such as "confirmed in chat".

## Cover Quality Rules

- Make the visual specific to the article, not generic science decoration.
- Keep the main subject centered for square and share-card crops.
- Make the main subject recognizable in one second on a phone-sized thumbnail.
- Use short cover text only when it improves click appeal and remains readable.
  Prefer a category tag plus an 8-14 character Chinese hook; do not repeat the
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

Use `scripts/cover_text_overlay.py` for deterministic text overlay when a
runtime with Pillow is available:

```bash
python .agents/skills/wechat-cover/scripts/cover_text_overlay.py \
  wechat/.local/cover-candidates/<publication_ref>/base.png \
  wechat/.local/cover-candidates/<publication_ref>/with-text.png \
  --category 数值风洞 \
  --hook 让城市风场更快可算
```

If system `python3` lacks Pillow, use the Codex bundled Python reported by
`codex_app.load_workspace_dependencies` instead of installing packages into the
repository.

If Pillow is unavailable, the script returns a JSON dependency error instead
of silently producing a low-quality cover.
