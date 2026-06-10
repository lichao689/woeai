# WOEAI WeChat Cover Standards

## Current Default

- Default first-cover size: `900 x 383 px`.
- Default ratio: about `2.35:1`.
- Treat this as current design guidance, not a permanent platform contract.
  Recheck the WeChat backend or current documentation before hard-coding future
  dimensions.

## Crop Safety

Keep the main visual subject in the center. The local preview checks:

- full `2.35:1` cover,
- center square crop,
- `5:4` share-card-like crop,
- small thumbnail,
- approximate center safe area.

These are first-pass checks only. The final approval surface is the WeChat
backend mobile preview.

## Candidate Concepts

Generate at least three directions for each paper:

1. Research scene: the physical or engineering system.
2. Method: the model, simulation, database, algorithm, or workflow.
3. Engineering impact: how the work supports decisions, platforms, or practice.

For each direction, consider two cover families:

- no-text editorial visual,
- short-text editorial visual.

Short text may be produced either directly by image generation or by
programmatic overlay. Direct image-generation text is an experiment, not an
automatic approval path.

## Text Policy

Use cover text only when it improves click appeal and remains readable as a
thumbnail.

User confirmation is required before generating any cover candidate that may
contain text, or before committing to a no-text direction. The agent should
offer exactly five concrete cover-text combinations plus one custom-text
option. The five generated combinations should each be ready to use on the
cover. The selected option becomes the source of truth for image-generation
prompts and deterministic text overlays.

Preferred structure:

- category tag: `数值风洞`, `结构抗风`, or `漂浮风电`;
- main hook: 8-14 Chinese characters;
- optional subtitle only if the small-thumbnail preview stays readable.

Do not repeat the full article title. Let the WeChat title field carry the
complete wording.

Reject direct image-generation text when:

- any Chinese character is wrong, distorted, missing, or hard to read;
- contrast is too low on the full cover or thumbnail;
- text competes with the main visual subject;
- fake UI labels, fake map labels, or misleading claims appear.

## Title Category Cues

`数值风洞`:

- urban blocks,
- CFD grids,
- wind streamlines,
- turbulence or inflow,
- contour fields,
- validation points,
- database or WebGIS layers.
- visual-data-to-CFD geometry workflows.

`结构抗风`:

- high-rise structures,
- wind pressure and load paths,
- vibration control,
- monitoring data,
- optimization,
- structural response.
- GNN nodes or response prediction cues.

`漂浮风电`:

- floating offshore wind platforms,
- wind-wave-current loading,
- mooring and coupled response,
- platform structure,
- offshore environment,
- system-level optimization.
- structural feasibility or cost/response tradeoff cues.

## Quality Rubric

Score each candidate from 1 to 5:

- article specificity,
- main-subject clarity,
- click appeal,
- engineering credibility,
- small-thumbnail readability,
- crop safety,
- text quality, when text is present.

Use these scores to compare candidates; do not average them blindly. A cover
with unreadable text, generic AI wallpaper, or a weak main subject should be
rejected even if its dimensions and file size pass.

## Prompt Template

Use English prompts for image generation unless the tool performs better in
Chinese for a specific case.

```text
A technically credible editorial cover image for a WOEAI WeChat article about
<paper topic>. Show <main visual subject>. Include <method or data cue>.
Use a clean modern academic engineering magazine style, restrained blue/white
palette with subtle accent color, central subject, wide 2.35:1 composition.
No text, no logo, no watermark, no people unless needed.
```

Add article-specific avoids:

- no generic city skyline,
- no decorative abstract technology wallpaper,
- no distorted Chinese text,
- no unrelated lab scene,
- no private partner or project branding.
- no fake software UI, fake map label, or fake publication claim.

## Review Note Fields

Record cover information in `wechat/articles/review/<publication_ref>.review.md`
or a paired cover brief:

- cover status,
- candidate count,
- selected candidate ID,
- user-confirmed cover text choice,
- selected text mode: `none`, `image-gen-text`, or `programmatic-overlay`,
- rejected candidate reasons,
- source candidate path,
- final cover path,
- dimensions,
- generation tool,
- prompt or design brief,
- quality scores,
- local crop preview path,
- backend preview state.
