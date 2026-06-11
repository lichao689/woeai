# ref-zhao2026-BS Cover Brief

Status: draft

## Article Signal

- Title category: `数值风洞`
- Article title: `数值风洞 | 我们如何用预计算 CFD 数据库加速城市微尺度风环境预测`
- Target readers: wind engineering researchers, prospective students,
  engineering software users, and technical collaborators.
- Core idea: turn repeated urban microscale CFD calculations into a
  precomputed, callable database for faster wind-environment prediction.
- Visual avoids: generic city skyline, decorative abstract tech wallpaper,
  distorted text, title text embedded in the image, unrelated laboratory scenes.

## Size And Crop Notes

- Current default: `900 x 383 px`, about `2.35:1`, for the first article cover.
- Current safety assumption: keep the main subject centered, because thumbnails
  and share surfaces may crop toward a square or 5:4 shape.
- Evidence checked on 2026-06-09:
  - Canva's public WeChat size page lists WeChat Official Account cover as
    `900 x 383 px` and describes the cover crop ratio as `2.35:1`.
  - A 2026 public size guide also lists first-cover `900 x 383 px`, ratio
    `2.35:1`, and a central safe area assumption.
- Treat these as current design guidance, not permanent platform truth. Recheck
  WeChat backend or current documentation before hard-coding future dimensions.

## Candidate Concepts

### Candidate A: Urban Wind Database

Use a dense city-block scene viewed from above at an oblique angle, with
semi-transparent wind streamlines crossing the blocks and a subtle data-grid
layer underneath. The center of the image should show the most legible urban
blocks and streamlines. The edges can be quieter and more atmospheric for crop
safety.

Prompt direction:

> A technically credible editorial cover image for a WeChat article about urban
> microscale wind prediction using a precomputed CFD database, oblique aerial
> view of dense city blocks, subtle CFD wind streamlines, data grid overlays,
> clean scientific visualization, modern Chinese academic research magazine
> style, deep blue and white with restrained cyan accents, no text, no logo,
> central subject, wide 2.35:1 composition.

Best for:

- Explaining the article's core topic at a glance.
- Readers who respond to city-scale wind-environment imagery.

Risk:

- Can become generic if the data-grid layer is too decorative.

### Candidate B: Block-Based CFD Workflow

Show several square city blocks as modular tiles connected into a database-like
matrix. Wind streamlines enter from one side, pass through representative
blocks, and become clean data cards or contour layers on the other side.

Prompt direction:

> A wide scientific cover showing block-based CFD workflow for urban wind
> environment prediction, modular square city blocks arranged as a database
> matrix, wind streamlines entering from the left, contour-map data layers
> emerging on the right, precise engineering visualization, elegant academic
> magazine cover, neutral white background with blue steel accents, no text, no
> logo, central visual focus, 2.35:1 aspect ratio.

Best for:

- Making the method contribution visible, not just the application.
- A future WOEAI visual family for `数值风洞` articles.

Risk:

- Too abstract if city geometry is not recognizable.

### Candidate C: WebGIS Engineering Application

Show a clean desktop/WebGIS-like map surface with colored wind-speed contours
over city blocks and a few unobtrusive measurement points. The scene should
feel like engineering decision support, not a software advertisement.

Prompt direction:

> A refined engineering decision-support cover for a WeChat article, WebGIS map
> surface showing urban wind-speed contours over simplified city blocks,
> measurement station markers, subtle CFD airflow field, high-end academic
> engineering software aesthetic, calm blue gray palette with focused color
> contours, no text, no logo, centered composition, wide 2.35:1 crop.

Best for:

- Showing the practical value of the paper.
- Connecting the paper to WOEAI engineering software and platform work.

Risk:

- Could look like a generic dashboard if visual hierarchy is weak.

## Current Selected Cover

- Previous v1 source image: `removed during 2026-06-11 slimming cleanup (cover-generated-v1-source.png)`
- Previous v1 cover: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-v1.png)`
- Current v2 cover: `wechat/assets/public-safe/ref-zhao2026-BS/cover-wechat-900x383-v2.png`
- Current final size: `900 x 383 px`
- Local v2 batch preview:
  `wechat/.local/cover-previews/batch-2026-06-10-v2-quality-board.html`
- Backend preview: pending.

## Recommendation

The v2 cover adopts Candidate B: block-based CFD results becoming a
precomputed database. It uses the short Chinese hook `数值风洞 / 把风场预先算好`
instead of repeating the full title. The local batch preview is recorded at
`wechat/.local/cover-previews/batch-2026-06-10-v2-quality-board.html`.
