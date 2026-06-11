---
publication_ref: ref-he2025-POF
zotero_key: ES37XMDV
doi: 10.1063/5.0293483
research_family: 建筑结构抗风
subdirection: 高层建筑抗风与优化
publication_mode: first_publish
wechat_status: ready_to_publish
wechat_draft_media_id: OW4ZgzIulHGwsx2YUygit_URZtdG9CUJHpFtft1WHn9eoCX1ezjDpnpA7TQCx7Wp
wechat_draft_created_at: 2026-06-10T20:05:23+08:00
wechat_draft_updated_at: 2026-06-10T20:05:23+08:00
wechat_author: He Xin
source_checked: true
abstract_checked: true
copyright_checked: true
public_safety_checked: true
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
body_images_upload_approved: true
rtd_page_checked: true
wechat_backend_preview_checked: false
---

# ref-he2025-POF 发布说明

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/ref-he2025-POF.md`
- RTD 配套页: `docs/source/paper-notes/ref-he2025-POF.rst`
- 微信草稿作者字段: `He Xin`

## RTD 转换记录

- 内容母版: `wechat/articles/draft-public-safe/ref-he2025-POF.md`
- 正式转换命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-he2025-POF`
- 同步检查命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-he2025-POF --check`
- RTD 顶部封面: not set for this package; body figures are inserted in the article flow
- 转换规则: 正文措辞、正文图片、公式语义和延伸阅读链接来自 Markdown；平台字段来自 review note。微信底部 `content_source_url` 默认使用当前论文 RTD 解读页（`https://woeai.readthedocs.io/zh-cn/latest/paper-notes/ref-he2025-POF.html`）。
- 导航状态: `docs/source/Research.rst` should list this page under `建筑结构抗风 / 高层建筑抗风与优化` in `学术进展 Academic Progress`.

## 证据来源

- DOI: https://doi.org/10.1063/5.0293483
- Zotero: `ES37XMDV`
- PDF attachment key: `TE9SXHTY`
- 摘要来源: Zotero Desktop Local API `abstractNote` and PDF abstract; 中文摘要为英文原摘要的忠实翻译，公众号正文同时保留英文原摘要。
- PDF / 作者稿: Zotero attachment record has `linkMode=imported_url`; controller and local verification confirmed a valid local Zotero storage PDF exists, has 19 pages, starts with `%PDF-`, supports `pdftotext`, and has extractable images. The selected local PDF was used for article evidence and body figures.
- 公开网站记录: `docs/source/Publications.rst` contains `ref-he2025-POF` as paper `[68]`; `docs/data/publication-research-map.json` maps Zotero key `ES37XMDV` to `建筑结构抗风 / 高层建筑抗风与优化`.

## 源文件获取记录

- Zotero key: `ES37XMDV`
- Zotero 元数据: checked via Zotero Desktop Local API
- Zotero 附件记录: checked via Zotero Desktop Local API; one PDF attachment record and one HTML attachment record exist
- 本地 PDF 附件: exists
- PDF 附件候选: one PDF-like Zotero attachment, child key `TE9SXHTY`, `contentType=application/pdf`, `linkMode=imported_url`; a local Zotero storage PDF is available and was used
- PDF 选择优先级: author manuscript > publisher version of record > OA platform PDF > preprint > other
- 已选 PDF 类型: Zotero local storage PDF from the `imported_url` attachment record, treated as the usable paper PDF for this WOEAI/user-authored article
- 低优先级选择原因: not applicable; no web, preprint, or lower-priority substitute source was used
- PDF 来源类型: Zotero local attachment storage
- PDF 私有存放: Zotero private attachment and ignored local working artifacts under `wechat/.local/ref-he2025-POF/`
- Zotero Web API `/file`: not needed
- 网页 PDF 下载: not used
- 网页 PDF 批准记录: not applicable
- 摘要依据: Zotero `abstractNote` and PDF abstract on PDF file page 1
- 正文证据依据: PDF body, Zotero metadata, and public WOEAI publication record
- 图片依据: PDF embedded figures extracted from the local paper PDF and copied into public-safe body assets
- 私有信息边界: no absolute private file path, credential, cookie, raw API payload, raw downloaded PDF content, or private preview URL is recorded here

## 关键事实证据定位记录

- 摘要:
  - 文章使用: 中文摘要忠实翻译英文摘要，并附英文原摘要。
  - 证据位置: Zotero `abstractNote`; PDF file page 1 abstract.
- 核心结论: 本文提出 implanted pole TLD，立柱可扰动多方向液体运动、增强耗能，并为大型水箱提供支撑和抵抗晃荡力。
  - 证据位置: PDF file page 1 abstract; PDF file pages 1-2, Section I.
- 核心结论: OpenFOAM 两相流求解器通过耦合 level set 与 VOF 方法形成 CLS-VOF 路线，以提高自由液面捕捉精度并减弱伪流问题。
  - 证据位置: PDF file pages 2-4, Section II.A-C, Figs. 1-2.
- 核心结论: 立柱阻塞率定义为 $H=a/B$，论文通过液深比、立柱阻塞率和激励幅值分析液体波高、晃荡力和阻尼变化。
  - 证据位置: PDF file page 6, Section III, Eq. (11), Fig. 9, Table I.
- 核心结论: 随着阻塞率 $H$ 增大，液体晃荡能量显著下降，自由液面上升受限，响应趋向线性；立柱尖角处产生小涡并增加能量耗散。
  - 证据位置: PDF file pages 6-9, Section III.A, Figs. 10-14.
- 核心结论: 随着激励幅值 $A$ 增大，波高和晃荡力峰值显著上升，自由液面会出现破碎和波形叠加，同时等效阻尼比提高。
  - 证据位置: PDF file pages 8-10, Section III.B, Figs. 15-18.
- 核心结论: 结构-TLD 双向耦合数值模型通过 OpenFOAM 二次开发实现，结构运动方程与流体晃荡力实时交换；模型能降低建模复杂度和计算时间。
  - 证据位置: PDF file pages 10-11, Section IV.A, Eqs. (12)-(13), Fig. 19.
- 核心结论: 双向耦合数值模型与试验数据吻合，结构位移响应和液体晃荡响应平均相对误差分别为 `5.26%` and `13.91%`；计算时间从 `5218 s` 降至 `4632 s`。
  - 证据位置: PDF file pages 11-12, Section IV.B, Figs. 20-22.
- 核心结论: 在单自由度框架结构验证中，内部立柱提高 TLD 耗能效率，使结构顶部最大位移响应降低 `85.2%`。
  - 证据位置: PDF file page 12, Section IV.C, Fig. 23.
- 核心结论: CAARC 建筑高度为 `182.88 m`，平面尺寸为 `45.72 m x 30.48 m`；论文采用 `1:200` 缩尺测压试验数据和六个风向角。
  - 证据位置: PDF file pages 11-13, Section V.A, Fig. 24.
- 核心结论: `10` 年重现期风荷载下，植入式立柱 TLD 将 `Ax` 从 `0.3163` 降至 `0.2398 m/s^2`，`Ay` 从 `0.4683` 降至 `0.3902 m/s^2`，`Dx` 从 `0.2443` 降至 `0.203 m`，`Dy` 从 `0.4184` 降至 `0.3457 m`。
  - 证据位置: PDF file pages 12-13, Section V.B, Fig. 25.
- 核心结论: 立柱阻塞率增大时，减振率 `g` 提高，但增长速度逐渐放缓；阻塞过大时会抑制液体往复运动并降低新增收益。
  - 证据位置: PDF file pages 12-15, Section V.C, Fig. 26, Table III.
- 核心结论: 调谐比 $X=\omega_{\mathrm{TLD}}/\omega_s$ 是 TLD 减振效率关键参数；在 `65%` tuning range 内，植入式立柱 TLD 有较好鲁棒性，`5 degree` 风向最优调谐比为 `0.978`，`90 degree` 风向最优调谐比为 `0.946`。
  - 证据位置: PDF file pages 13-16, Section V.E, Eq. (15), Figs. 29-31.
- 核心边界: 本文主要研究矩形立柱 TLD，后续可扩展到圆形、流线型和菱形等不同立柱形状，并研究不同风向下的立柱布置优化。
  - 证据位置: PDF file pages 16-17, Section VI final paragraph.
- 关键图:
  - Fig. 9 `Illustrative diagram of the implanted pole TLD model`: PDF file page 6; used as article Figure 9; asset `wechat/assets/public-safe/ref-he2025-POF/fig-09-implanted-pole-tld-model.jpg`.
  - Fig. 14 `The free surface velocity contour map illustrates the impact of the implanted pole on liquid oscillation`: PDF file page 9; used as article Figure 14; asset `wechat/assets/public-safe/ref-he2025-POF/fig-14-pole-flow-mechanism.jpg`.
  - Fig. 17 `The nonlinear oscillation characteristics under large excitation amplitude`: PDF file page 10; used as article Figure 17; asset `wechat/assets/public-safe/ref-he2025-POF/fig-17-large-amplitude-nonlinear-sloshing.jpg`.
  - Fig. 18 `The energy dissipation efficiency of the implanted pole TLD at different excitation amplitudes`: PDF file page 10; used as article Figure 18; asset `wechat/assets/public-safe/ref-he2025-POF/fig-18-energy-dissipation-excitation-amplitude.png`.
  - Fig. 22 `The contrast of free surface capture`: PDF file page 12; used as article Figure 22; asset `wechat/assets/public-safe/ref-he2025-POF/fig-22-free-surface-validation.jpg`.
  - Fig. 24 `Schematic of the pressure measurement experiment for the CAARC model`: PDF file page 13; used as article Figure 24; asset `wechat/assets/public-safe/ref-he2025-POF/fig-24-caarc-wind-tunnel-model.jpg`.
  - Fig. 26 `The comparison of the mitigation ratio g at different H`: PDF file page 14; used as article Figure 26; asset `wechat/assets/public-safe/ref-he2025-POF/fig-26-mitigation-ratio-pole-obstruction.png`.
  - Fig. 29 `The comparison of the mitigation ratio g under different X`: PDF file page 16; used as article Figure 29; asset `wechat/assets/public-safe/ref-he2025-POF/fig-29-mitigation-ratio-tuning.png`.
- 关键公式:
  - 文章使用: paper formula `$H=a/B$` for pole obstruction ratio.
  - 证据位置: PDF file page 6, Section III, Eq. (11).
  - 文章使用: editorial explanatory/public-facing notation `$\Omega=\omega_{\mathrm{TLD}}/\omega_s$` for tuning ratio; PDF uses its own symbol `X` for the same ratio, so the article notation is not labeled as a paper-original formula.
  - 证据位置: PDF file page 13, Section V.E, Eq. (15).
  - 文章使用: editorial explanatory/public-facing notation $\eta$ for mitigation ratio; PDF uses paper-original `g=1-R/Ro` for the same damping-performance metric.
  - 证据位置: PDF file page 12, Section V.C, Eq. (14), Figs. 26, 28-29.
  - 文章使用: inline variables and quantities `$h/L$`, `$H$`, `$A$`, `$\zeta$`, `$182.88\,\mathrm{m}$`, `$45.72\,\mathrm{m}$`, `$30.48\,\mathrm{m}$`, acceleration and displacement response values, and tuning ratios.
  - 证据位置: PDF file pages 6-16, Sections III-VI.
- 页码口径: evidence locations use PDF file page numbers, not journal printed page numbers or article pagination.

## 图片使用记录

1. 图 9: 植入式立柱 TLD 模型示意
   - 用途: 开篇说明研究对象和立柱阻塞率定义
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-he2025-POF/fig-09-implanted-pole-tld-model.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 9 植入式立柱 TLD 模型示意
   - 公众号说明: 展示立柱布置方式和阻塞率定义。
   - 移动端预览: pending WeChat backend mobile preview
2. 图 14: 自由液面速度云图说明植入式立柱对液体振荡的影响
   - 用途: 说明立柱产生小涡和阻塞效应的耗能机制
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-he2025-POF/fig-14-pole-flow-mechanism.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 14 自由液面速度云图说明植入式立柱对液体振荡的影响
   - 公众号说明: 显示液体分离、小涡和立柱阻塞效应。
   - 移动端预览: pending WeChat backend mobile preview
3. 图 17: 大幅激励下的非线性振荡特征
   - 用途: 说明自由液面破碎和波形叠加
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-he2025-POF/fig-17-large-amplitude-nonlinear-sloshing.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 17 大幅激励下的非线性振荡特征
   - 公众号说明: 展示大幅输入下自由液面破碎和波形叠加。
   - 移动端预览: pending WeChat backend mobile preview
4. 图 18: 不同激励幅值下植入式立柱 TLD 的能量耗散效率
   - 用途: 说明激励幅值和等效阻尼比的关系
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-he2025-POF/fig-18-energy-dissipation-excitation-amplitude.png`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 18 不同激励幅值下植入式立柱 TLD 的能量耗散效率
   - 公众号说明: 显示激励幅值提高时等效阻尼比整体上升。
   - 移动端预览: pending WeChat backend mobile preview
5. 图 22: 自由液面捕捉结果对比
   - 用途: 说明双向耦合数值模型与试验对比
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-he2025-POF/fig-22-free-surface-validation.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 22 自由液面捕捉结果对比
   - 公众号说明: 比较试验自由液面和数值模型预测结果。
   - 移动端预览: pending WeChat backend mobile preview
6. 图 24: CAARC 模型测压试验示意
   - 用途: 说明高层建筑风荷载输入和风向角设置
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-he2025-POF/fig-24-caarc-wind-tunnel-model.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 24 CAARC 模型测压试验示意
   - 公众号说明: 展示缩尺模型和风向角布置。
   - 移动端预览: pending WeChat backend mobile preview
7. 图 26: 不同立柱阻塞率下减振率对比
   - 用途: 说明阻塞率与减振效率的关系
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-he2025-POF/fig-26-mitigation-ratio-pole-obstruction.png`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 26 不同立柱阻塞率下减振率对比
   - 公众号说明: 显示阻塞率增大时减振率提高但增幅放缓。
   - 移动端预览: pending WeChat backend mobile preview
8. 图 29: 不同调谐比下减振率对比
   - 用途: 说明调谐比和减振效率的关系
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-he2025-POF/fig-29-mitigation-ratio-tuning.png`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 29 不同调谐比下减振率对比
   - 公众号说明: 显示调谐比存在最优范围，偏离后减振率下降。
   - 移动端预览: pending WeChat backend mobile preview

## 公式检查

- 使用公式: yes; one paper-original display formula `$H=a/B$`, one editorial/public-facing tuning-ratio display notation `$\Omega=\omega_{\mathrm{TLD}}/\omega_s$`, editorial/public-facing mitigation-ratio notation `$\eta$`, and inline mathematical quantities
- 呈现方式: Markdown LaTeX source; default WeChat API rendering is MathJax SVG with `data-formula` metadata
- 微信公式渲染路线: `mathjax-svg` unless a fallback reason is recorded
- RTD 呈现方式: Sphinx math roles/directives generated by `wechat/tools/markdown_to_rtd.py`
- 行内变量/量纲: formula markup applied to `$h/L$`, `$H$`, `$A$`, `$\zeta$`, `$\eta$`, `$\Omega$`, structural response quantities, dimensional quantities, and percentage values
- 移动端预览: pending WeChat backend mobile preview

## 封面图

- 封面状态: regenerated with image-gen-text; WeChat draft updated; pending WeChat backend mobile preview
- 候选数量: 3 concept directions documented in `wechat/articles/review/ref-he2025-POF.cover-brief.md`; 1 selected image-gen-text cover exported
- 选中候选: `cover-wechat-900x383-imagegen-v1`
- 文字模式: image-gen-text
- 生成工具: Codex image generation tool
- 图像生成场景: 植入式立柱 TLD、水箱非线性晃荡、结构减振
- 要求文字: `结构抗风 / 晃荡更耗能 / 植入式立柱TLD`
- 备用封面: `wechat/assets/public-safe/ref-he2025-POF/cover-wechat-900x383-v1.png`
- 封面素材: `wechat/assets/public-safe/ref-he2025-POF/cover-wechat-900x383-imagegen-v1.png`
- 尺寸: `900 x 383 px`
- 本地总览图: `wechat/.local/cover-previews/batch-10-imagegen-contact-sheet.png`
- 本地裁剪预览: `wechat/.local/cover-previews/batch-10-imagegen-cover-preview.html`
- 审核状态: local visual text check and crop preview passed; WeChat backend mobile preview pending
- 草稿状态: existing WeChat draft has been live-updated to this regenerated cover; pending WeChat backend mobile preview and proofread
- 注意: `cover_image_checked` remains `false` until the WeChat backend mobile preview is checked.

## 公开安全

- [x] No WeChat AppSecret, token, cookie, or credential appears.
- [x] No Zotero API key appears.
- [x] No private partner name appears.
- [x] No unconfirmed project status appears.
- [x] Reader-facing Markdown has no YAML front matter, production notes, checklist, pending placeholders, or private paths.
- [x] Reader-facing Markdown uses direct Markdown hyperlinks under `延伸阅读`; no separate `阅读原文` body section is included.
- [x] Figure captions use a Chinese figure-title line translated from the original paper title plus a separate Chinese explanatory line.

## 发布前任务

- [x] 用 Zotero/PDF 核对作者、期刊、DOI 和图题。
- [x] 用 Zotero/PDF 摘要补入中文摘要和英文原摘要。
- [x] 从 PDF 抽取并导入可用正文图。
- [x] 由公众号正文转换生成 RTD 配套页，保持标题、正文、图片、DOI 和延伸阅读链接一致。
- [ ] 公众号后台手机预览正文、公式、封面和图片。
- [x] 微信公众号草稿已创建并回填 `wechat_status` 与草稿 media_id；正式发布后再回填 `latest_published_url`。

## 检查记录

- figure extraction: copied selected local extracted PDF embedded images to public-safe asset names
- visual verification: selected assets were inspected against original figure content before insertion
- rtd-generation: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-he2025-POF`)
- rtd-sync-check: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-he2025-POF --check`)
- public-safety: passed (`python3 scripts/check-public-safe-content.py`)
- whitespace: passed (`git diff --check`)
- docs-build: passed (`./scripts/check-docs.sh`)
