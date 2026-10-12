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

## 系列规范迁移（2026-10-05）

- cover_design_contract: `WOEAI-cover-v2`
- 规范: [统一网格、字号、配色与裁切](../../../.agents/skills/wechat-cover/references/cover-standards.md)
- 本文方向: `数值风洞`，依据对应正文标题；仅用该方向固定色彩令牌，不另起画风
- 证据入口: [本文事实审阅](ref-zhao2026-BS.review.md)；生成前完成工程叙事证据卡
- 文字来源: 保留历史确认记录，旧请求文字不自动视为新一轮批准；缩短或改写须重新确认
- 科学元素: 选择一个已核实主对象；路线为已验证输入 → 方法 → 输出；潜在用途与结果分开
- 构图: 900 × 383 px；左文区 x=36–396；关键科学对象 x=420–620、y=56–276；底部三节点路线
- 历史复用限制: 既有提示词、概念和选图仅供溯源，不直接当新一轮完整提示词；重新按 v2 及审阅证据编写
- migration_status: specification-updated; existing-image-not-regenerated
- design_contract_checked: pending; 尺寸一致不证明旧图符合新布局、字级或科学对象裁切
- backend_preview_status: unchanged; 此次简报维护没有新增后台手机预览


## 2026-10-12 新规范生成轮次

- cover_execution_mode: image-gen
- cover_text_confirmation: user-confirmed
- confirmed_cover_text: 数值风洞 | 城市风场先算后查 / 分块 CFD 预计算数据库
- confirmed_text_mode: image-gen-text
- publication_metadata_line: Building Simulation · 2026
- confirmation_note: 用户同意推荐选项 1；所有文字保持确认原文。
- generation_tool: built-in image_gen
- 证据锚点：原 review 中 Fig. 1（PDF file page 4）分块计算与数据库流程；Fig. 2（page 5）城市区块；Fig. 25（page 22）查询展示。图像仅为机制示意，不复刻定量结果。
- 三个候选：研究场景、方法机制、工程应用；提示词要求统一网格、字体、配色及文字 0° 水平直立；实际符合情况以下方像素审阅为准。
- candidate_count: 3 概念 × 2 轮；另有研究场景候选的位置修正实验。
- selected_candidate_id: scene-placement-candidate（用户接受为本篇最终封面）
- final_export_dimensions: 900 × 383 px；仅等比例导出，未叠加或改写文字。
- local_preview: `wechat/.local/zhao-cover-latest/scene-placement-qa-crops.png`
- 文字与裁切：确认文字完整、水平直立；900 × 383、360 × 153、120 方形及 5:4 中对象可辨认。未据此宣称后台验收。
- 淘汰原因：首轮标题过大；第二轮场景文字整体偏低约 14 px；方法与应用候选副标题偏小，应用方案方形裁切后数据库特征较弱。
- 独立像素复核：位置修正稿仍不符合严格网格。约值：徽标 x32/y24（规范 x36/y28）；标题 x32/y77（x36/y84）；副标题 y194（y200）；期刊 y231（y238）；路线 y281–354（y290–359）；背景场景超出指定区域。
- design_contract_checked: failed-fixed-grid; exact-text-and-crop-local-check-passed
- approval_state: user-approved-layout-exception; 2026-10-12 用户查看实际图像并明确同意按此视觉更新该篇草稿。仅接受本图已记录偏差，系列规范不变。
- 科学边界：机制插画而非论文定量结果；树木仅作环境装饰，论文模型省略植被等小尺度设施，不声称模拟了植被。
- 新草稿封面上传：2026-10-12 官方 API 成功；保留旧 v2 及历史验收记录。
- 后台手机预览：未检查。旧 v2 与历史证据保留。

- approved_final_cover_path: `wechat/assets/public-safe/ref-zhao2026-BS/cover-wechat-900x383-20261012-scene.png`
- approved_final_sha256: `d61202ccb6d3448657ffc47dedbbeeb322b41fe903a9205a11c44fddaeb8cec6`
- backend_update_state: success; 官方回读核对新原图字节、派生封面视觉及原正文/设置；尚不视为后台手机预览。


### 2026-10-12 完整生成提示词

以下为生成输入，实际网格偏差以本次验收记录为准；提示词本身不证明成品符合。

#### scene

Create a polished Chinese engineering research WeChat cover, final composition at 900x383 (2.35:1), high-resolution raster. Precise restrained scientific editorial illustration, not neon/cyberpunk. Fixed layout expressed in final pixels: safe area x36-864 y24-359; integrated pale #EFF6FC text zone x36-396 with NO panel/card/divider; blue #0B6FD3 badge x36 y28 size128x40 radius6; exact white badge text "数值风洞" at24px bold upright. Main hook exact "城市风场先算后查" split as "城市风场" and "先算后查", x36 y84 width360 height108, 48px heavy sans-serif, lineheight54, #073B7A. Exact subtitle "分块 CFD 预计算数据库" x36 y200 24px #334155 single line. Exact journal line "Building Simulation · 2026" x36 y238, at least18px semibold #073B7A, can wrap at word boundary. Chinese Noto Sans/Source Han Sans style. All text is horizontal 0degree upright with NO italic, slant, perspective or distortions. ONLY these four text elements; no other words/numbers/labels. Scene x420-864 y28-280; important diagnostic object must remain inside x420-620 y56-276 for center-square crop. Bottom y290-359 three small pictorial nodes linked by two fine arrows: city block geometry -> precomputed CFD block tiles -> reusable data layers. No text in route. Blend scene into text background smoothly. Paper: Zhao et al. 2026 Building Simulation, urban microscale wind precomputed CFD database: city divided into square blocks with surrounding buffer, independently computed flow stored and queried. This is a conceptual illustration, NOT measured data or a claimed exact site. No fake quantitative curves, percentages, map labels, logos, watermark, decorative interface panels. Scientific palette subdued white/steelblue, small cyan flow cues only in scene. Prioritize crisp correct Chinese and journal spelling.
Research-scene variant: one square city CFD tile in oblique view dominates x470-610 with clearly visible building cores and a soft surrounding buffer; three neighboring tiles recede toward right, coordinated streamlines crossing them. A subtle data-layer stack far right connects the idea to reusable database. Not a generic skyline; square core and buffer are visibly diagnostic.

#### method

Create a polished Chinese engineering research WeChat cover, final composition at 900x383 (2.35:1), high-resolution raster. Precise restrained scientific editorial illustration, not neon/cyberpunk. Fixed layout expressed in final pixels: safe area x36-864 y24-359; integrated pale #EFF6FC text zone x36-396 with NO panel/card/divider; blue #0B6FD3 badge x36 y28 size128x40 radius6; exact white badge text "数值风洞" at24px bold upright. Main hook exact "城市风场先算后查" split as "城市风场" and "先算后查", x36 y84 width360 height108, 48px heavy sans-serif, lineheight54, #073B7A. Exact subtitle "分块 CFD 预计算数据库" x36 y200 24px #334155 single line. Exact journal line "Building Simulation · 2026" x36 y238, at least18px semibold #073B7A, can wrap at word boundary. Chinese Noto Sans/Source Han Sans style. All text is horizontal 0degree upright with NO italic, slant, perspective or distortions. ONLY these four text elements; no other words/numbers/labels. Scene x420-864 y28-280; important diagnostic object must remain inside x420-620 y56-276 for center-square crop. Bottom y290-359 three small pictorial nodes linked by two fine arrows: city block geometry -> precomputed CFD block tiles -> reusable data layers. No text in route. Blend scene into text background smoothly. Paper: Zhao et al. 2026 Building Simulation, urban microscale wind precomputed CFD database: city divided into square blocks with surrounding buffer, independently computed flow stored and queried. This is a conceptual illustration, NOT measured data or a claimed exact site. No fake quantitative curves, percentages, map labels, logos, watermark, decorative interface panels. Scientific palette subdued white/steelblue, small cyan flow cues only in scene. Prioritize crisp correct Chinese and journal spelling.
Method variant: a single enlarged square core city block at x460-610 with a visibly wider transparent surrounding buffer ring, plus a small exploded stack of precomputed flow-field layers immediately behind/right. Two fine unlabelled arrows connect computed block to ordered data layers. Make independent block calculation plus stored reusable results the obvious visual, not just a city or decorative database cylinder.

#### application

Create a polished Chinese engineering research WeChat cover, final composition at 900x383 (2.35:1), high-resolution raster. Precise restrained scientific editorial illustration, not neon/cyberpunk. Fixed layout expressed in final pixels: safe area x36-864 y24-359; integrated pale #EFF6FC text zone x36-396 with NO panel/card/divider; blue #0B6FD3 badge x36 y28 size128x40 radius6; exact white badge text "数值风洞" at24px bold upright. Main hook exact "城市风场先算后查" split as "城市风场" and "先算后查", x36 y84 width360 height108, 48px heavy sans-serif, lineheight54, #073B7A. Exact subtitle "分块 CFD 预计算数据库" x36 y200 24px #334155 single line. Exact journal line "Building Simulation · 2026" x36 y238, at least18px semibold #073B7A, can wrap at word boundary. Chinese Noto Sans/Source Han Sans style. All text is horizontal 0degree upright with NO italic, slant, perspective or distortions. ONLY these four text elements; no other words/numbers/labels. Scene x420-864 y28-280; important diagnostic object must remain inside x420-620 y56-276 for center-square crop. Bottom y290-359 three small pictorial nodes linked by two fine arrows: city block geometry -> precomputed CFD block tiles -> reusable data layers. No text in route. Blend scene into text background smoothly. Paper: Zhao et al. 2026 Building Simulation, urban microscale wind precomputed CFD database: city divided into square blocks with surrounding buffer, independently computed flow stored and queried. This is a conceptual illustration, NOT measured data or a claimed exact site. No fake quantitative curves, percentages, map labels, logos, watermark, decorative interface panels. Scientific palette subdued white/steelblue, small cyan flow cues only in scene. Prioritize crisp correct Chinese and journal spelling.
Engineering-application variant: a crisp oblique city-block map at x430-670, one square block visibly selected and pulled slightly upward, with matching precomputed flow-field layer tiles returned beside it at x680-840. Subtle building forms and consistent airflow show queryable microscale wind fields, no screen/device/UI text, no warning icons or implication of validated forecasting. Center crop retains the selected square block and matching layer.

#### 最后位置修正输入

Make ONLY two precise layout corrections to this otherwise approved scientific cover, preserving every existing word, glyph appearance, font sizes, palette, and main scientific scene. Coordinate system is900x383: (1) Shift the ENTIRE left text group (blue badge, two-line title, subtitle, journal line) UP exactly14px final equivalent; do not change its x positions or scale. Thus badge top28, title top84, subtitle top200, journal top238. Text exact "数值风洞", "城市风场" newline "先算后查", "分块 CFD 预计算数据库", "Building Simulation · 2026". All horizontal upright. (2) The three bottom pictorial process nodes are too tall. Uniformly reduce the process diagram nodes to fit y290-354, keeping the two arrows and the whole sequence below the journal line and inside x36-864. Do not move the main city-block scene; keep visual scientific concept identical. No new words, no replacement typography, no watermark. Output2.35:1 landscape, same clean engineering editorial cover.
