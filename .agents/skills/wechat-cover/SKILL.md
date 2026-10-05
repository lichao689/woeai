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
3. Resolve the execution mode before the cover-text confirmation gate. Use
   `prompt-only` only when the user explicitly asks to generate full prompts,
   only produce prompts, or avoid image generation. Otherwise use the default
   `image-gen` mode without asking a separate execution-mode question.
4. Run the mandatory cover-text confirmation gate below for both execution
   modes. Record the confirmed text choice in the cover brief or review note
   before generating images or writing prompt-only output.
5. If the execution mode is `prompt-only`, produce exactly three complete
   image-generation prompts for the research scene, method, and engineering
   impact directions, following the prompt-only response format below. Do not
   call an image-generation tool, create image files, run crop preview, or
   update a WeChat draft in this mode.
6. If the execution mode is `image-gen`, generate cover candidates only through
   the image-generation route with the confirmed cover text embedded in the
   image. Produce at least three image-gen-text candidates in each round. Reject
   any candidate with distorted, misspelled, incomplete, rewritten,
   low-contrast, or unreadable Chinese text.
7. Store public-safe cover outputs under
   `wechat/assets/public-safe/<publication_ref>/`. Keep private experiments
   under ignored local paths such as `wechat/.local/`.
8. Export exactly `900 x 383 px` under `WOEAI-cover-v2`. Measure dimensions;
   ratio alone is insufficient. Verify actual backend crops before release.
9. Run the crop preview helper:

   ```bash
   python .agents/skills/wechat-cover/scripts/cover_preview.py \
     wechat/assets/public-safe/<publication_ref>/<cover-file>.png \
     --label "候选 A" \
     --score article_specificity=4,click_appeal=5
   ```

   Treat this as a local first-pass comparison board. It checks dimensions,
   common crops, and small-thumbnail readability surfaces, but final approval
   still requires the WeChat backend mobile preview.
10. Update the review note with:
   - selected execution mode: `image-gen` or `prompt-only`,
   - candidate count or prompt count,
   - selected candidate ID, when applicable,
   - user-confirmed cover text choice,
   - selected text mode: `image-gen-text`,
   - prompt-only output count and complete prompt texts, when applicable,
   - rejected candidate reasons,
   - cover source or prompt,
   - generation tool,
   - source candidate path, when applicable,
   - final cover path, when applicable,
   - dimensions, when applicable,
   - local crop-preview path, when applicable,
   - approval state,
   - WeChat backend preview state.
11. Run the relevant checks:
   - `python scripts/check-public-safe-content.py`
   - `git diff --check`
   - `python wechat/tools/wechat_draft.py dry-run --publication-ref <ref>`
     when the draft API path should see the selected cover.

If all candidates in a round fail because the text is wrong, unreadable, or the
visual is not article-specific, retry once with the same confirmed text. If two
rounds fail, stop and ask the user to confirm shorter or clearer cover text.
Do not use no-text covers or post-generation text overlays as fallbacks.

## Execution Mode Rule

Before the cover-text confirmation gate, determine whether this run should
generate images or only produce full prompts. Do not ask a separate
execution-mode question.

Use the default `image-gen` mode unless the user explicitly requests
`prompt-only`.

- Choose `prompt-only` for requests such as "直接生成提示词",
  "只生成提示词", "给我完整提示词", or "不要生成图片".
- Choose `image-gen` for all other cover-generation requests, including
  "生成封面", "重新生成图片", "更新封面", "更新公众号草稿封面", or requests
  that simply name a paper and ask for a cover.

The execution-mode rule does not replace the mandatory cover-text confirmation
gate. Both modes still require the five cover-text options plus custom text
before image generation or prompt-only output.

## Prompt-Only Response Format

When the user replies with a cover-text option number in `prompt-only` mode,
the next user-facing answer must make the concrete prompts the main output.

- Start with one short line confirming the selected cover text.
- Then output exactly three complete prompts, labelled in Chinese as:
  `提示词 1｜研究场景`, `提示词 2｜方法机制`, and
  `提示词 3｜工程应用`.
- Each prompt must be self-contained and directly usable in an image-generation
  tool. Do not use placeholders, ellipses, "see file", "same as above", or
  references that require the reader to inspect the repository.
- Do not put the prompts inside fenced code blocks by default, because long
  image prompts become horizontally clipped in chat UIs. Use normal wrapped
  paragraphs or block quotes. Use fenced code blocks only if the user
  explicitly asks for copy boxes.
- Put checks, file-write summaries, and review-note updates after the prompts,
  in one brief sentence. Do not lead with tooling status.
- Use Chinese headings and a Chinese one-line explanation for each direction;
  the prompt body may follow the prompt language rule below.

Default prompt language:

- Use an English prompt body for image-generation instructions, because most
  general image models follow composition, lighting, layout, and style cues more
  reliably in English.
- Keep all cover text strings in exact Chinese inside quotes, and repeat that
  they must remain crisp, unchanged, and not translated.
- If the user says the target image model is Chinese-first, or explicitly asks
  for Chinese prompts, write the prompt body in Chinese while preserving the
  same structure and exact quoted cover text.
- If unsure, use English prompt body plus exact Chinese cover text.

## Shared Series Design

Read [references/cover-standards.md](references/cover-standards.md) before every
brief, prompt, candidate or crop review. `WOEAI-cover-v2` is the single source for
900 × 383 output, grid, type scale, fixed category colors, text budgets and crop
acceptance. Do not invent a new style for each paper; candidate concepts change
the scientific emphasis inside the same system.

A request to improve skills or derived briefs is guidance maintenance, not image
generation. Preserve existing assets and confirmation/preview history; mark
migration pending. Use `wechat/templates/cover-brief.md` for new paired briefs.

## Mandatory Cover-Text Confirmation

Before any new cover-generation round or prompt-only output, ask the user to
choose the exact text plan that may appear on the cover. Do this after
extracting the brief and resolving the execution mode, and before calling an
image-generation tool, writing full prompts, or selecting a candidate. Do not
infer approval from silence or from a generic "continue".

Present exactly five concrete cover-text combinations plus one custom-text
option, then wait for the user's reply. The first five options should be ready
to use on the cover, not abstract text modes:

1. `category tag` + `6-12 character Chinese hook`.
2. `category tag` + an alternate `6-12 character Chinese hook`.
3. `category tag` + a more engineering-facing `6-12 character Chinese hook`.
4. `category tag` + a more reader-facing `6-12 character Chinese hook`.
5. `category tag` + a more method- or finding-focused `6-12 character Chinese hook`.
6. Custom cover text supplied by the user.

Use the article category from `wechat/STYLE.md` when suggesting category tags.
Each option should follow this structure:

`category tag | main hook / subtitle`

The category tag must be `数值风洞`, `结构抗风`, or `漂浮风电`. Derive hooks only
from public-safe article wording or the cover brief. Keep the main hook short,
preferably 6-12 full-width character equivalents, maximum 14. Include a short
subtitle by default for the
three-part cover-text system; omit it only when the user explicitly chooses a
no-subtitle variant for readability. If the user chooses custom text, ask for
the exact category tag, hook, and subtitle before continuing. If the user asks
for a no-text cover, explain that this skill requires confirmed cover text and
ask them to choose or provide text.

Record the confirmed choice in the cover brief or review note with:

- `cover_text_confirmation: user-confirmed`,
- `confirmed_cover_text`,
- `confirmed_text_mode`: `image-gen-text`,
- `cover_execution_mode`: `image-gen` or `prompt-only`,
- `publication_metadata_line`, when journal and year are available,
- `confirmation_note`: short public-safe note such as "confirmed in chat".

## Cover Quality Rules

- Make the visual specific to the article, not generic science decoration.
- Keep the diagnostic subject inside the contract crop core. A center square
  cannot retain the entire left title; assess subject survival separately.
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
