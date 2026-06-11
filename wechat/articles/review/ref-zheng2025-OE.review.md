---
publication_ref: ref-zheng2025-OE
zotero_key: 5W2SZJUT
doi: 10.1016/j.oceaneng.2025.121336
research_family: 海上漂浮风电
subdirection: 浮式混凝土平台结构设计
publication_mode: first_publish
wechat_status: ready_to_publish
wechat_draft_media_id: OW4ZgzIulHGwsx2YUygityiCBgxLgEDIa8y3uhHf7kDdBisslbMb3Gm3dZwSx5n-
wechat_draft_created_at: 2026-06-10T20:05:35+08:00
wechat_draft_updated_at: 2026-06-10T20:05:35+08:00
wechat_author: Zheng Shunyun
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

# ref-zheng2025-OE 发布说明

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/ref-zheng2025-OE.md`
- RTD 配套页: `docs/source/paper-notes/ref-zheng2025-OE.rst`
- 微信草稿作者字段: `Zheng Shunyun`

## RTD 转换记录

- 内容母版: `wechat/articles/draft-public-safe/ref-zheng2025-OE.md`
- 正式转换命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zheng2025-OE`
- 同步检查命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zheng2025-OE --check`
- RTD 顶部封面: not set for this package; body figures are inserted in the article flow
- 转换规则: 正文措辞、正文图片、公式语义和延伸阅读链接来自 Markdown；平台字段来自 review note。微信底部 `content_source_url` 默认使用当前论文 RTD 解读页（`https://woeai.readthedocs.io/zh-cn/latest/paper-notes/ref-zheng2025-OE.html`）。
- 导航状态: shared integration files were intentionally not modified in this worker task. Existing public record already contains `ref-zheng2025-OE` in `docs/source/Publications.rst` and the floating offshore wind direction page.

## 证据来源

- DOI: https://doi.org/10.1016/j.oceaneng.2025.121336
- Zotero: `5W2SZJUT`
- PDF attachment keys: `Y95L65C5`, `3PC68U8X`
- 摘要来源: Zotero Desktop Local API `abstractNote` and PDF abstract; 中文摘要为英文原摘要的忠实翻译，公众号正文同时保留英文原摘要。
- PDF / 作者稿: Zotero local imported PDF attachments exist; the selected local publisher-record PDF was used for article evidence and body figures.
- 公开网站记录: `docs/source/Publications.rst` contains `ref-zheng2025-OE` as paper `[65]`; `docs/source/FloatingOffshoreWindEnergy.rst` lists it under `浮式混凝土平台结构设计`.

## 源文件获取记录

- Zotero key: `5W2SZJUT`
- Zotero 元数据: checked via Zotero Desktop Local API
- Zotero 附件记录: checked via Zotero Desktop Local API; two PDF attachment records and one HTML attachment record exist
- 本地 PDF 附件: exists
- PDF 附件候选: two PDF-like Zotero local imported attachments; both match the same title, DOI metadata, page count, and file size class
- PDF 选择优先级: author manuscript > publisher version of record > OA platform PDF > preprint > other
- 已选 PDF 类型: Zotero local imported publisher-record PDF, treated as the usable paper PDF for this WOEAI/user-authored article
- 低优先级选择原因: not applicable; no web, preprint, or lower-priority substitute source was used
- PDF 来源类型: Zotero local attachment
- PDF 私有存放: Zotero private attachment and ignored local working artifacts under `wechat/.local/ref-zheng2025-OE/`
- Zotero Web API `/file`: not needed
- 网页 PDF 下载: not used
- 网页 PDF 批准记录: not applicable
- 摘要依据: Zotero `abstractNote` and PDF abstract on PDF file page 1
- 正文证据依据: PDF body, Zotero metadata, and public WOEAI publication record
- 图片依据: PDF embedded figures extracted from the local paper PDF and copied into public-safe body JPG assets
- 私有信息边界: no absolute private file path, credential, cookie, raw API payload, raw downloaded PDF content, or private preview URL is recorded here

## 关键事实证据定位记录

- 摘要:
  - 文章使用: 中文摘要忠实翻译英文摘要，并附英文原摘要。
  - 证据位置: Zotero `abstractNote`; PDF file page 1 abstract.
- 核心结论: 研究对象为三角形半潜式 `10 MW` 风机平台，平台由三根立柱和底部浮筒组成，风机位于其中一根立柱上，四根悬链线系泊线约束平台运动。
  - 证据位置: PDF file page 3, Section 2.2, Fig. 1, Tables 2-3.
- 核心结论: 数值模型包括 ANSYS AQWA 水动力模型、OpenF2A 耦合动力模型和 ANSYS APDL 有限元模型；模型试验用于验证 RAO 结果。
  - 证据位置: PDF file pages 4-5, Section 2.3, Figs. 2-7.
- 核心结论: 增强 ESWL 方法同时考虑水压力、系泊导缆孔力和塔底载荷，并分别以 LTCLR 和 LTSCR 作为等效目标。
  - 证据位置: PDF file pages 9-11, Section 3.2, Figs. 10-12.
- 核心结论: 长期应力分量响应显示高应力集中在立柱-浮筒连接、塔底、系泊导缆孔和局部内部结构区域；ESWL 工况需要综合考虑水压力、系泊力和塔底载荷。
  - 证据位置: PDF file pages 11-12, Section 4.1, Fig. 13.
- 核心结论: 传统设计波方法在高应力区预测 LTSCR 的误差范围为 `-99.93%` to `28.58%`，多数应力分量最大值低于目标值，范围为 `-71.05%` to `6.75%`，不能直接用于半潜式浮式风机结构设计。
  - 证据位置: PDF file page 12, Section 4.2, Fig. 14.
- 核心结论: 基于 LTCLR 的方法筛选得到 `12` 个 ESWL 工况；高应力危险区域中，应力分量最大等效误差为 `27.80%` to `36.91%`，平均等效误差为 `17.88%` to `22.71%`。
  - 证据位置: PDF file pages 13-15, Section 4.3, Tables 8-10, Fig. 15.
- 核心结论: 基于 LTSCR 的方法筛选得到 `6` 个 ESWL 工况；高应力区保守率低于 `23.86%`，应力分量平均等效误差为 `5.06%` to `8.06%`。
  - 证据位置: PDF file pages 15-16, Section 4.4, Tables 11-13, Fig. 16.
- 核心结论: LTCLR 方法更适合初步设计，LTSCR 方法更适合最终详细设计和成本效率更高的结构设计。
  - 证据位置: PDF file pages 16-17, Section 4.5, Fig. 17; PDF file page 19, Section 5 conclusion item 3.
- 核心结论: 按 IEC 强度校核，允许材料强度为 `273.08 MPa`；传统标准方法、LTCLR 方法和 LTSCR 方法下平台最大 Von Mises 应力分别为 `187.20 MPa`, `252.14 MPa`, and `228.97 MPa`，均满足材料强度要求。
  - 证据位置: PDF file pages 17-18, Section 4.6, Eqs. (7)-(8), Figs. 18-19.
- 核心边界: 论文明确指出极端风荷载和极端波浪荷载之间的相关性尚未被充分考虑，后续需要进一步研究等效静力风荷载确定方法。
  - 证据位置: PDF file page 19, Section 5 final limitation paragraph.
- 关键图:
  - Fig. 1 `Delta-shaped semi-submersible 10-MW wind turbine system`: PDF file page 3; used as article Figure 1; asset `wechat/assets/public-safe/ref-zheng2025-OE/fig-01-delta-shaped-system.jpg`.
  - Fig. 7 `RAOs of delta-shaped semi-submersible wind turbine system`: PDF file page 7; used as article Figure 7; asset `wechat/assets/public-safe/ref-zheng2025-OE/fig-07-raos-validation.jpg`.
  - Fig. 12 `Workflow of ESWL methods based on LTSCRs and LTCLRs`: PDF file page 10; used as article Figure 12; asset `wechat/assets/public-safe/ref-zheng2025-OE/fig-12-eswl-workflow.jpg`.
  - Fig. 13a `The wave-induced LTSCRs on the semi-submersible platform of 10-MW wind turbine`: PDF file page 12; used as article Figure 13a; asset `wechat/assets/public-safe/ref-zheng2025-OE/fig-13a-ltscr-distribution.jpg`.
  - Fig. 19 `Comparison of the maximum Von-Mises stress under the load cases based on standard, LTSCRs and LTCLRs`: PDF file page 18; used as article Figure 19; asset `wechat/assets/public-safe/ref-zheng2025-OE/fig-19-von-mises-comparison.jpg`.
- 关键公式:
  - 文章使用: editorial explanatory formula `$A=R_Q/RAO_{\mathrm{max}}$`, summarizing the PDF method statement that wave amplitude is determined by the ratio of long term extreme target response to maximum RAO.
  - 证据位置: PDF file page 11, Section 3.2 method paragraph.
  - 文章使用: Von Mises and allowable strength values, including `273.08 MPa`, `187.20 MPa`, `252.14 MPa`, and `228.97 MPa`.
  - 证据位置: PDF file pages 17-18, Section 4.6, Eqs. (7)-(8), Figs. 18-19.
  - 文章使用: inline indicators `$10\,\mathrm{MW}$`, `$50$` years, `$273.08\,\mathrm{MPa}$`, and equivalent-method abbreviations LTCLR/LTSCR/ESWL.
  - 证据位置: PDF file pages 1, 3, 9-19.
- 页码口径: evidence locations use PDF file page numbers, not journal printed page numbers or article pagination.

## 图片使用记录

1. 图 1: 三角形半潜式 10 MW 风机系统
   - 用途: 开篇说明研究对象
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zheng2025-OE/fig-01-delta-shaped-system.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 1 三角形半潜式 10 MW 风机系统
   - 公众号说明: 展示平台、风机和系泊系统基本构型。
   - 移动端预览: pending WeChat backend mobile preview
2. 图 7: 三角形半潜式风机系统 RAO
   - 用途: 模型验证说明
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zheng2025-OE/fig-07-raos-validation.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 7 三角形半潜式风机系统 RAO
   - 公众号说明: 比较数值模拟与模型试验的响应幅值算子。
   - 移动端预览: pending WeChat backend mobile preview
3. 图 12: 基于 LTSCR 和 LTCLR 的 ESWL 方法流程
   - 用途: 方法流程说明
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zheng2025-OE/fig-12-eswl-workflow.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 12 基于 LTSCR 和 LTCLR 的 ESWL 方法流程
   - 公众号说明: 展示增强 ESWL 方法如何加入耦合动力分析和长期极值响应。
   - 移动端预览: pending WeChat backend mobile preview
4. 图 13a: 半潜式 10 MW 风机平台的波浪诱导 LTSCR
   - 用途: 长期应力危险区域说明
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zheng2025-OE/fig-13a-ltscr-distribution.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 13a 半潜式 10 MW 风机平台的波浪诱导 LTSCR
   - 公众号说明: 显示高应力区集中在局部危险区域。
   - 移动端预览: pending WeChat backend mobile preview
5. 图 19: 基于标准、LTSCR 和 LTCLR 工况的最大 Von Mises 应力对比
   - 用途: 方法精度和保守性对比
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zheng2025-OE/fig-19-von-mises-comparison.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 19 基于标准、LTSCR 和 LTCLR 工况的最大 Von Mises 应力对比
   - 公众号说明: 对比传统方法和增强方法对最大 Von Mises 应力的预测表现。
   - 移动端预览: pending WeChat backend mobile preview

## 公式检查

- 使用公式: yes; one editorial explanatory display formula and inline mathematical quantities
- 呈现方式: Markdown LaTeX source; default WeChat API rendering is MathJax SVG with `data-formula` metadata
- 微信公式渲染路线: `mathjax-svg` unless a fallback reason is recorded
- RTD 呈现方式: Sphinx math roles/directives generated by `wechat/tools/markdown_to_rtd.py`
- 行内变量/量纲: formula markup applied to `$10\,\mathrm{MW}$`, `$50$`, `$A$`, `$R_Q$`, `$RAO_{\mathrm{max}}$`, `$273.08\,\mathrm{MPa}$`, and stress quantities
- 移动端预览: pending WeChat backend mobile preview

## 封面图

- 封面状态: regenerated with image-gen-text; WeChat draft updated; pending WeChat backend mobile preview
- 候选数量: 3 concept directions documented in `wechat/articles/review/ref-zheng2025-OE.cover-brief.md`; 1 selected image-gen-text cover exported
- 选中候选: `cover-wechat-900x383-imagegen-v1`
- 文字模式: image-gen-text
- 生成工具: Codex image generation tool
- 图像生成场景: 半潜式浮式风机、海浪、等效静力波浪荷载、结构应力
- 要求文字: `漂浮风电 / 等效波浪荷载 / 半潜式风机`
- 备用封面: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-v1.png)`
- 封面素材: `wechat/assets/public-safe/ref-zheng2025-OE/cover-wechat-900x383-imagegen-v1.png`
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

- [x] 用 Zotero/PDF 核对作者、期刊、页码、DOI 和图题。
- [x] 用 Zotero/PDF 摘要补入中文摘要和英文原摘要。
- [x] 从 PDF 抽取并导入可用正文图。
- [x] 由公众号正文转换生成 RTD 配套页，保持标题、正文、图片、DOI 和延伸阅读链接一致。
- [ ] 公众号后台手机预览正文、公式、封面和图片。
- [x] 微信公众号草稿已创建并回填 `wechat_status` 与草稿 media_id；正式发布后再回填 `latest_published_url`。

## 检查记录

- figure extraction: copied selected local extracted PDF embedded JPG images to public-safe asset names
- rtd-generation: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zheng2025-OE`)
- rtd-sync-check: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zheng2025-OE --check`)
- taxonomy-correction: passed; current source data and public pages classify this paper as `海上漂浮风电 / 浮式混凝土平台结构设计`
- direction-consistency: passed; no current source-data or public-page binding remains between `ref-zheng2025-OE` / `5W2SZJUT` and the former subdirection
- wechat-dry-run: passed (`python wechat/tools/wechat_draft.py dry-run --publication-ref ref-zheng2025-OE`)
- wechat-preflight: passed (`python wechat/tools/wechat_draft.py preflight --publication-ref ref-zheng2025-OE`)
- public-safety: passed (`python3 scripts/check-public-safe-content.py`)
- whitespace: passed (`git diff --check`)
