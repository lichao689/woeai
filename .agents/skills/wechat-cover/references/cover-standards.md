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
- approximate center safe area.

These are first-pass checks only. The final approval surface is the WeChat
backend mobile preview.

## Candidate Concepts

Generate at least three directions for each paper:

1. Research scene: the physical or engineering system.
2. Method: the model, simulation, database, algorithm, or workflow.
3. Engineering impact: how the work supports decisions, platforms, or practice.

## Title Category Cues

`数值风洞`:

- urban blocks,
- CFD grids,
- wind streamlines,
- turbulence or inflow,
- contour fields,
- validation points,
- database or WebGIS layers.

`结构抗风`:

- high-rise structures,
- wind pressure and load paths,
- vibration control,
- monitoring data,
- optimization,
- structural response.

`漂浮风电`:

- floating offshore wind platforms,
- wind-wave-current loading,
- mooring and coupled response,
- platform structure,
- offshore environment,
- system-level optimization.

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

## Review Note Fields

Record cover information in `wechat/articles/review/<publication_ref>.review.md`
or a paired cover brief:

- cover status,
- source candidate path,
- final cover path,
- dimensions,
- generation tool,
- prompt or design brief,
- local crop preview path,
- backend preview state.
