---
name: wechat-cover
description: Generate, repair or review WOEAI WeChat paper covers; maintain cover briefs, prompts and design rules. Includes exact badge measurement, evidence-grounded illustrations and crop diagnostics.
---

# WeChat Cover

Create an article-specific horizontal cover, then verify the actual final image.
A prompt describes intent; it is never acceptance evidence.

## Required context

Read `AGENTS.md`, `CONTEXT.md`, and
[references/cover-standards.md](references/cover-standards.md) before every brief,
prompt, generation, repair or review. The standards own the design contract.
For an actual cover also read the target article and its audited evidence review;
use `wechat-paper` for article production and backend delivery permissions.

A skill/specification/template maintenance request does not authorize image
regeneration, article changes, a WeChat update or publication. Preserve existing
assets and historical approvals; record migration pending rather than marking
old images compliant. Old three-category article prefixes in `wechat/STYLE.md`
and historical briefs need separate migration; do not copy them into new covers.

## Workflow and gates

1. **Evidence brief.** Use `wechat/templates/cover-brief.md`. Record the exact
   secondary direction from the registry, research question, real geometry,
   baseline/change, key evidence and limitations. Trace every visible scientific
   object or comparison to a source section/figure. If an essential source is
   absent, report the gap instead of inventing a plausible scene.
2. **Execution mode.** Default to `image-gen`; use `prompt-only` only when the
   user explicitly requests prompts without generation. Guidance maintenance
   does neither. No extra mode-confirmation question is needed.
3. **Exact words.** Apply the confirmation gate below before new generation or
   complete prompts. An authorized repair may reuse unchanged confirmed words;
   it must not reopen settled wording or silently rewrite it.
4. **Composition brief.** Plan a wide editorial composition with a clear focal
   hierarchy and useful empty space. Positions are flexible, badge size is not.
   Use the horizontal space; a center-square diagnostic is not a design grid.
   Prefer one explanatory relationship over cramming the whole paper into a box.
5. **Produce.** For a new design round, generate three directions (scene, method,
   application) inside the shared contract with confirmed text in the image.
   If the user selected a direction or requested one local repair, work on that
   candidate instead of generating three unnecessary variants. For prompt-only,
   follow the output format below without generating images or previews.
6. **Inspect final pixels.** Export exactly 900 × 383 and inspect the decoded
   final file after any crop/resize/repair, not an earlier source or chat preview.
   Check exact words, science, composition, contrast and all fixed invariants.
   Run the badge measurement gate in the standards: record actual outer and ink
   bounds, file hash, method and result. An unmeasured or oversized badge fails
   even when the prompt specified the correct size. Nominal font size is not
   glyph ink height. Never claim font verification from a box measurement.
7. **Preview.** Run the helper from the repository root:

   ```bash
   python3 .agents/skills/wechat-cover/scripts/cover_preview.py \
     wechat/assets/public-safe/<publication_ref>/<cover-file>.png \
     --label "候选 A"
   ```

   Inspect full/wide/mobile views first. Center-square and 5:4 crops diagnose
   information loss only; they neither prove WeChat's current behavior nor
   require all scientific content to fit a center square. Verify the actual
   backend crop controls and mobile result only within authorized backend work.
8. **Record and deliver.** Record the selected file/hash, exact text, evidence
   anchors, measured dimensions/badge, visual review, rejected reasons, actual
   generation/edit tools and backend state separately. Keep experiments and
   detailed reports in ignored storage; public reviews contain only public-safe
   results. A failed candidate may be shown only as a clearly labelled failure,
   never as the corrected final cover.
9. **Checks.** Run `python3 scripts/check-public-safe-content.py` and
   `git diff --check`; run relevant tests for helper changes. Run an offline
   `wechat_draft.py dry-run` only when the authorized draft workflow needs to
   consume the selected asset. No credentials or live calls for skill work.

## Mandatory cover-text confirmation

For new words, present exactly five concrete combinations plus a custom option:
`secondary direction | main hook / subtitle`. Use the five approved directions
and text budgets in the standards. Derive hooks from audited article wording.
Offer varied scene/method/engineering/reader/finding emphasis, not five abstract
modes. Wait for an explicit selection; silence or a generic "continue" is not
text approval. For custom words resolve the exact badge, hook and subtitle.
Include a subtitle unless the user explicitly selects a no-subtitle variant.

Record `cover_text_confirmation: user-confirmed`, `confirmed_cover_text`,
`confirmed_text_mode: image-gen-text`, `cover_execution_mode`, verified journal
and year, and a short public-safe confirmation note. Reusing confirmed text for
an explicitly requested repair needs no redundant five-option question.
Changing text, omitting a line or changing the rendering route needs the
applicable user approval. Do not use a text-free or post-render overlay fallback
unless the user explicitly authorizes that change; do not claim such a composite
was generated entirely by the image tool.

## Authorized exception for the 2026-10-14 migration batch

This exception is limited to the user-authorized batch of 17 existing covers and
27 new paper covers. It is not a standing exception for later projects or batches.
For this batch only, the user explicitly authorized source-grounded editorial
selection and independent review of the main hook and subtitle without repeating
the five-option question. Scientifically ambiguous meaning still requires a
specific question rather than an invented interpretation.

Engineering illustrations must still use built-in image generation. The user
also authorized deterministic typesetting of the text and direction badge for
this batch. Record `cover_text_confirmation: batch-authorized-editorial-selection`
and `confirmed_text_mode: authorized-deterministic-typesetting`, exact final
wording, actual illustration and typesetting tools, source anchors, final asset
hash, independent review and the unchanged badge measurement gates. Do not claim
a composite was generated entirely by the image tool. Preserve already approved
words and assets unless a correction is required and independently checked.

This exception does not authorize publication, backend updates, changing other
channels' selected covers, or any remote action beyond separately granted scope.
Local image review does not constitute actual WeChat mobile preview acceptance.
The default confirmation and rendering rules continue to apply outside this batch.

## Bounded repairs

Before a repair, list the defect and all invariants that must survive. Keep the
source candidate and review the new final file independently; "only changed the
badge" is not evidence that the title, science or palette survived unchanged.
Remeasure the badge and repeat the full acceptance checklist after every edit.

For the same unresolved problem, allow at most two generation/edit attempts,
including local fixes. Record attempt count and measured failure each time. At
that limit, stop repeating the same prompt and change strategy: simplify or
recompose the scientific scene within approved wording, or ask for the specific
permission needed for a different rendering route. Do not keep generating,
silently increase tolerance, blame text length for a geometry failure, or mark
the best of several failures as passed. Tool success is not cover acceptance.

## Prompt-only output

After text confirmation, make the three complete prompts the main output:
`提示词 1｜研究场景`, `提示词 2｜方法机制`, `提示词 3｜工程应用`.
Start with one short line confirming the words. Each prompt is standalone, with
canvas, fixed badge contract, flexible horizontal composition, typography,
category colors, exact words, verified journal/year, evidence-grounded science
and exclusions. No placeholders, "same as above" or source-file dependencies.
The prompt must say final raster measurements are still required; a prompt-only
result has no measured image and cannot pass visual acceptance.

Use English instructions with exact Chinese strings by default, or Chinese
instructions when requested. Follow the current channel's text/file format rules;
do not require fenced blocks. Put any file/check summary after the prompts.

## Tool truthfulness and acceptance

- Name the tool actually used and distinguish generation, local image editing,
  export/resize and measurement. Promise only parameters the tool supports.
- Image-generation size instructions are targets, not guaranteed exact output.
  If a tool returns only a displayed image without a readable file, report that
  measurement/export is blocked; do not invent a file or claim dimensions checked.
- Measure actual pixels; never use nominal font size, image dimensions, a model's
  description, or the requested badge rectangle as measured badge geometry.
- Local preview success, automated geometry pass and human visual review are
  separate. No score average can override a failed invariant.
- Set `cover_image_checked: true` only after an actual WeChat backend mobile
  preview. Local QA never sets backend acceptance, even for an unchanged size.
