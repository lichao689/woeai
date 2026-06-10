# WeChat Cover Workflow PRD

Status: ready-for-agent

## Goal

Create a repeatable WOEAI workflow for WeChat Official Account cover images
that can later be promoted into a dedicated `wechat-cover` skill.

The first phase stays inside this repository. It should improve cover quality
for real WOEAI paper articles without prematurely freezing a global workflow.

## Problem

Paper figures are usually unsuitable as WeChat covers. They may be too tall,
too detailed, too technical, or weak after WeChat cropping. A good cover needs
to attract technically literate readers while still matching WOEAI's research
voice.

The current article has a generated cover, but the cover workflow is not yet
systematic enough. We need a clearer process for:

- selecting the visual concept from the article content,
- generating several candidate covers,
- checking WeChat-friendly dimensions and crop safety,
- recording the prompt, source, and approval state,
- reusing lessons across multiple paper articles.

## Scope

Included:

- WeChat cover images for WOEAI paper articles.
- Cover generation from article title, title category, abstract, key figures,
  and engineering meaning.
- A local repeatable workflow using approved image generation tooling.
- Multi-candidate review before choosing a final cover.
- Public-safe asset storage under `wechat/assets/public-safe/<publication_ref>/`.
- Review-note fields for cover prompt, dimensions, source image, final image,
  approval state, and WeChat backend preview status.
- A path to promote the workflow into a global `wechat-cover` skill after it is
  proven on multiple articles.

Excluded for now:

- Automatic publication or mass-send.
- Browser automation that clicks publish in WeChat.
- Storing private WeChat preview URLs or raw API responses.
- Generated Chinese text inside cover images by default.
- A global Codex skill before the repo workflow has at least two or three
  successful examples.

## Working Assumptions

- Start from the current WOEAI cover target of `900 x 383 px`, about `2.35:1`.
- Before implementing a reusable generator, verify current WeChat cover-size
  guidance against WeChat's live platform or official documentation, because
  platform recommendations may change.
- Keep the main visual subject near the center so square-ish thumbnails remain
  usable after cropping.
- Prefer no embedded text. Let the WeChat title carry the words.
- The cover should be academically credible, visually modern, and linked to the
  article's actual content. It should not look like generic technology stock art.

## Candidate Directions

For each paper article, generate at least three candidate cover concepts:

1. Research-scene concept: shows the physical or engineering system.
2. Method concept: shows the modeling, simulation, database, or workflow idea.
3. Impact concept: shows the application value or engineering decision context.

For WOEAI's current title categories:

- `数值风洞`: wind-field streamlines, urban blocks, CFD grids, data layers,
  turbulence, validation points.
- `结构抗风`: high-rise structures, load paths, vibration control, wind pressure,
  monitoring or optimization.
- `漂浮风电`: floating platforms, offshore wind, coupled wind-wave-current loads,
  mooring, system response.

## Acceptance Criteria

- A command or documented process can produce at least three cover candidates
  from a selected article.
- The final cover is exported to a WeChat-ready raster image with the chosen
  target ratio and recorded dimensions.
- A square-crop or thumbnail-safety check is performed before approval.
- The review note records:
  - cover prompt or design brief,
  - generation tool,
  - source candidate path,
  - final cover path,
  - dimensions,
  - approval state,
  - WeChat backend preview state.
- The article dry-run lists the selected approved cover image.
- No private preview URL, credential, token, or raw WeChat API response is
  written to the repository.

## Promotion Rule

Promote this into a global `wechat-cover` skill only after the workflow has
worked on at least two or three WOEAI paper articles and the naming, dimensions,
review fields, and visual standards have stopped changing quickly.

## Open Decisions

- Whether to keep one WOEAI visual family for all covers or define separate
  cover families by title category.
- Whether to build a local preview board for cover candidates.
- Whether to add a small Python helper for crop checks and candidate contact
  sheets.
