---
publication_ref: ref-zhou2023-AE
zotero_key: 3LWVP7B7
doi: 10.1016/j.apenergy.2023.121941
research_family: 海上漂浮风电
subdirection: 浮式风机系统一体化分析与优化
publication_mode: first_publish
wechat_status: ready_to_publish
wechat_draft_media_id: OW4ZgzIulHGwsx2YUygit3v-ltteGzLECE5trkxPCiv7it5Ua6pXtFs6644WW5te
wechat_draft_created_at: 2026-06-10T20:05:45+08:00
wechat_draft_updated_at: 2026-06-10T20:05:45+08:00
wechat_author: Zhou Shengtao
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

# ref-zhou2023-AE 发布说明

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/ref-zhou2023-AE.md`
- RTD 配套页: `docs/source/paper-notes/ref-zhou2023-AE.rst`
- 微信草稿作者字段: `Zhou Shengtao`

## RTD 转换记录

- 内容母版: `wechat/articles/draft-public-safe/ref-zhou2023-AE.md`
- 正式转换命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhou2023-AE`
- 同步检查命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhou2023-AE --check`
- RTD 顶部封面: none
- 转换规则: 正文措辞、正文图片、公式语义和延伸阅读链接来自 Markdown；微信底部 `content_source_url` 默认留空。
- 导航状态: planned for `docs/source/Research.rst` under `海上漂浮风电 / 浮式风机系统一体化分析与优化`.

## 证据来源

- DOI: https://doi.org/10.1016/j.apenergy.2023.121941
- Zotero: `3LWVP7B7`
- PDF attachment key: `G792HSAZ`
- 摘要来源: Zotero Desktop Local API `abstractNote` and PDF abstract; 中文摘要为英文原摘要的忠实翻译，公众号正文同时保留英文原摘要。
- PDF / 作者稿: Zotero child `G792HSAZ`, `application/pdf`, `linkMode=imported_url`; controller verified a local storage PDF exists, is valid `%PDF-`, has 20 pages, `pdftotext` works, and `pdfimages` lists images. This worker also used the local storage PDF for evidence and figure extraction.
- 公开网站记录: `docs/source/Publications.rst` contains `ref-zhou2023-AE` as paper `[48]`; `docs/source/FloatingOffshoreWindEnergy.rst` lists it under `浮式风机系统一体化分析与优化`.

## 源文件获取记录

- Zotero key: `3LWVP7B7`
- Zotero 元数据: checked via Zotero Desktop Local API
- Zotero 附件记录: checked via Zotero Desktop Local API; PDF attachment `G792HSAZ` and HTML attachment records exist
- 本地 PDF 附件: exists
- PDF 附件候选: single PDF-like attachment in checked child records
- PDF 选择优先级: author manuscript > publisher version of record > OA platform PDF > preprint > other
- 已选 PDF 类型: Zotero local imported PDF attachment, treated as the usable paper PDF for this WOEAI/user-authored article
- 低优先级选择原因: not applicable; no web, preprint, or lower-priority substitute source was used
- PDF 来源类型: Zotero local attachment
- PDF 私有存放: Zotero private attachment and ignored local working artifacts under `wechat/.local/ref-zhou2023-AE/`
- Zotero Web API `/file`: not needed
- 网页 PDF 下载: not used
- 网页 PDF 批准记录: not applicable
- 摘要依据: Zotero `abstractNote` and PDF abstract on PDF file page 1
- 正文证据依据: PDF body, Zotero metadata, and public WOEAI publication record
- 图片依据: PDF page-render crops from the local paper PDF copied into public-safe body JPG assets
- 私有信息边界: no absolute private file path, credential, cookie, raw API payload, raw downloaded PDF content, or private preview URL is recorded here

## 关键事实证据定位记录

- 摘要:
  - 文章使用: 中文摘要忠实翻译英文摘要，并附英文原摘要。
  - 证据位置: Zotero `abstractNote`; PDF file page 1 abstract.
- 核心结论: 本文提出基于长期动力优化的浮式风机下部结构评估方法，用 ROM、Kriging 代理模型和 NSGA-II 多目标优化寻找长期动力性能与制造成本之间的 Pareto 折中。
  - 证据位置: PDF file page 1 abstract; PDF file pages 6-9, Sections 3.2-4.3.
- 核心结论: ROM 使用八自由度描述平台/塔架动力响应，并通过与 OpenFAST 的验证对比支持早期设计阶段快速仿真。
  - 证据位置: PDF file pages 3-4, Section 2.1, Fig. 1; PDF file pages 10-12, Section 5.1, Figs. 9-16, Table 4.
- 核心结论: 长期海况数据相较简化海况数据能够捕捉风浪失配影响，并影响 Pareto 设计和长期疲劳判断。
  - 证据位置: PDF file pages 15-16, Section 5.4.1, Figs. 18-20.
- 核心结论: 在本文案例中，方形半潜式相较 Y 形半潜式更有望作为详细设计输入；相同制造成本水平下，方形概念的塔底疲劳大多低 `30%` 至 `50%`。
  - 证据位置: PDF file page 1 abstract; PDF file pages 17-18, Sections 5.4.2 and 6, Fig. 23.
- 核心结论: 水动力性能是两类构型疲劳差异的主要原因，RAO 和 QTF 对比用于解释平台运动与系泊疲劳差异。
  - 证据位置: PDF file pages 18-19, Section 5.5, Figs. 25-27.
- 核心边界: ROM 与 OpenFAST 验证仍存在误差；低于额定风速时误差约 `10%`，更严苛海况下可增至 `10%` 至 `25%`，主要来自气动阻尼、控制器动态效应和线性黏性阻力近似。
  - 证据位置: PDF file pages 17-18, Section 6 conclusions.
- 关键图:
  - Fig. 1 `Definition of degrees of freedom and global coordinate system`: PDF file page 3; used as article Figure 1; asset `wechat/assets/public-safe/ref-zhou2023-AE/fig-01-dof-coordinate.jpg`.
  - Fig. 7 `Platform configuration and mooring layout of the investigated FWTs`: PDF file page 8; used as article Figure 7; asset `wechat/assets/public-safe/ref-zhou2023-AE/fig-07-platform-mooring-layout.jpg`.
  - Fig. 19 `Comparison of the Pareto fronts obtained by two different environmental inputs`: PDF file page 15; used as article Figure 19; asset `wechat/assets/public-safe/ref-zhou2023-AE/fig-19-pareto-environmental-inputs.jpg`.
  - Fig. 23 `Comparison of the Pareto fronts between the square-shaped and Y-shaped substructure`: PDF file page 17; used as article Figure 23; asset `wechat/assets/public-safe/ref-zhou2023-AE/fig-23-pareto-substructures.jpg`.
  - Fig. 25 `Comparison of the platform motion RAO between the two substructure concepts under 135 degree wave direction`: PDF file page 18; used as article Figure 25; asset `wechat/assets/public-safe/ref-zhou2023-AE/fig-25-rao-comparison.jpg`.
- 关键公式:
  - 文章使用: inline indicators `$TC$`, `$D_{\mathrm{TwrBs}}$`, `$D_{\mathrm{Frld}}$`, `$25$` years, percentages, and ROM/RAO quantities.
  - 证据位置: PDF file pages 1, 3, 8, 15, 17-18.
  - 文章未使用复制自论文的展示公式；公式均为正文指标或单位的 editorial explanatory notation, pointing to the paper's definitions and results above.
- 页码口径: evidence locations use PDF file page numbers, not journal printed page numbers or article pagination.

## 图片使用记录

1. 图 1: 自由度和全局坐标系定义
   - 用途: 开篇动力分析坐标和自由度说明
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhou2023-AE/fig-01-dof-coordinate.jpg`
   - 来源/版权: paper PDF page-render crop; WOEAI/user-authored paper workflow scope
   - 抽取方式: rendered PDF file page 3 and cropped with local tooling
   - 公众号图名: 图 1 自由度和全局坐标系定义
   - 公众号说明: 展示用于快速动力分析的运动自由度、全局坐标、来流方向和系泊线布置。
   - 移动端预览: pending WeChat backend mobile preview
2. 图 7: 所研究浮式风机的平台构型与系泊布置
   - 用途: 两类设计概念和系泊参数说明
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhou2023-AE/fig-07-platform-mooring-layout.jpg`
   - 来源/版权: paper PDF page-render crop; WOEAI/user-authored paper workflow scope
   - 抽取方式: rendered PDF file page 8 and cropped with local tooling
   - 公众号图名: 图 7 所研究浮式风机的平台构型与系泊布置
   - 公众号说明: 展示方形半潜式和 Y 形半潜式两类构型，以及平台和系泊参数如何进入优化设计空间。
   - 移动端预览: pending WeChat backend mobile preview
3. 图 19: 不同环境输入得到的 Pareto 前沿对比
   - 用途: 长期海况对优化结果的影响
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhou2023-AE/fig-19-pareto-environmental-inputs.jpg`
   - 来源/版权: paper PDF page-render crop; WOEAI/user-authored paper workflow scope
   - 抽取方式: rendered PDF file page 15 and cropped with local tooling
   - 公众号图名: 图 19 不同环境输入得到的 Pareto 前沿对比
   - 公众号说明: 展示简化海况和长期海况下，制造成本与疲劳指标之间的 Pareto 关系变化。
   - 移动端预览: pending WeChat backend mobile preview
4. 图 23: 方形与 Y 形下部结构的 Pareto 前沿对比
   - 用途: 两类概念的核心优化结果比较
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhou2023-AE/fig-23-pareto-substructures.jpg`
   - 来源/版权: paper PDF page-render crop; WOEAI/user-authored paper workflow scope
   - 抽取方式: rendered PDF file page 17 and cropped with local tooling
   - 公众号图名: 图 23 方形与 Y 形下部结构的 Pareto 前沿对比
   - 公众号说明: 把两类概念放到同一成本和疲劳指标坐标系中比较，支持构型筛选判断。
   - 移动端预览: pending WeChat backend mobile preview
5. 图 25: 两类下部结构在 135 度波向下的平台运动 RAO 对比
   - 用途: 水动力机制解释
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhou2023-AE/fig-25-rao-comparison.jpg`
   - 来源/版权: paper PDF page-render crop; WOEAI/user-authored paper workflow scope
   - 抽取方式: rendered PDF file page 18 and cropped with local tooling
   - 公众号图名: 图 25 两类下部结构在 135 度波向下的平台运动 RAO 对比
   - 公众号说明: 通过 surge、sway、roll 和 pitch 响应幅值对比，解释长期疲劳差异背后的水动力原因。
   - 移动端预览: pending WeChat backend mobile preview

## 公式检查

- 使用公式: yes; inline mathematical variables/quantities only
- 呈现方式: Markdown LaTeX source; default WeChat API rendering is MathJax SVG with `data-formula` metadata
- 微信公式渲染路线: `mathjax-svg` unless a fallback reason is recorded
- RTD 呈现方式: Sphinx math roles generated by `wechat/tools/markdown_to_rtd.py`
- 行内变量/量纲: formula markup applied to `$TC$`, `$D_{\mathrm{TwrBs}}$`, `$D_{\mathrm{Frld}}$`, `$25$` years, `$30\%$ to `$50\%`, and error percentages
- 移动端预览: pending WeChat backend mobile preview

## 封面图

- 封面状态: regenerated with image-gen-text; WeChat draft updated; pending WeChat backend mobile preview
- 候选数量: 3 concept directions documented in `wechat/articles/review/ref-zhou2023-AE.cover-brief.md`; 1 selected image-gen-text cover exported
- 选中候选: `cover-wechat-900x383-imagegen-v1`
- 文字模式: image-gen-text
- 生成工具: Codex image generation tool
- 图像生成场景: 浮式风机下部结构优化、Pareto 前沿、长期动力响应
- 要求文字: `漂浮风电 / 长期动力优化 / 浮式下部结构`
- 备用封面: `wechat/assets/public-safe/ref-zhou2023-AE/cover-wechat-900x383-v1.png`
- 封面素材: `wechat/assets/public-safe/ref-zhou2023-AE/cover-wechat-900x383-imagegen-v1.png`
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
- [x] 用 Zotero/PDF 摘要补入中文摘要。
- [x] 从 PDF 裁切并导入可用正文图。
- [x] 由公众号正文转换生成 RTD 配套页，保持标题、正文、图片、DOI 和延伸阅读链接一致。
- [x] 将 RTD 配套页挂入 `docs/source/Research.rst` 对应科研方向的 `学术进展 Academic Progress`。
- [ ] 公众号后台手机预览正文、公式、封面和图片。
- [ ] 如需发布，另行生成并审核公众号封面图。

## 检查记录

- Zotero Local API metadata: passed (`3LWVP7B7`)
- Zotero Local API children: passed (`G792HSAZ`, `application/pdf`, `linkMode=imported_url`)
- PDF validation: passed (`pdfinfo`, `%PDF-`, 20 pages, `pdftotext`, `pdfimages -list`)
- figure extraction: rendered selected PDF pages and cropped selected figures into public-safe JPG assets
- visual asset check: local visual inspection completed for selected crops; WeChat backend mobile preview pending
- rtd-generation: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhou2023-AE`)
- rtd-sync-check: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhou2023-AE --check`)
- public-safety: passed (`python3 scripts/check-public-safe-content.py`)
- whitespace: passed (`git diff --check -- wechat/articles/draft-public-safe/ref-zhou2023-AE.md wechat/articles/review/ref-zhou2023-AE.review.md docs/source/paper-notes/ref-zhou2023-AE.rst docs/source/Research.rst wechat/assets/public-safe/ref-zhou2023-AE`)
- docs-build: passed (`./scripts/check-docs.sh`)
