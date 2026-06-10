---
publication_ref: ref-zhao2026-BS
zotero_key: CGKPKZ8I
doi: 10.1007/s12273-025-1379-7
research_family: 建筑结构抗风
subdirection: 数值风洞与湍动入流
publication_mode: first_publish
wechat_status: ready_to_publish
wechat_draft_media_id: OW4ZgzIulHGwsx2YUygit8W5lJ84JuQVMz4NFRpBMgLqu_P2CwMhp5uLAs3CfZau
wechat_draft_created_at: 2026-06-09T12:31:43+08:00
wechat_draft_updated_at: 2026-06-10T02:50:06+08:00
wechat_author: Zhao Peisheng
rtd_cover_image: wechat/assets/public-safe/ref-zhao2026-BS/cover-wechat-900x383-v2.png
source_checked: true
abstract_checked: true
copyright_checked: true
public_safety_checked: true
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
body_images_upload_approved: true
rtd_page_checked: true
---

# ref-zhao2026-BS 发布说明

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/ref-zhao2026-BS.md`
- RTD 配套页: `docs/source/paper-notes/ref-zhao2026-BS.rst`
- 微信草稿作者字段: `Zhao Peisheng`

## RTD 转换记录

- 内容母版: `wechat/articles/draft-public-safe/ref-zhao2026-BS.md`
- 正式转换命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2026-BS`
- 同步检查命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2026-BS --check`
- RTD 顶部封面: `wechat/assets/public-safe/ref-zhao2026-BS/cover-wechat-900x383-v2.png`
- 转换规则: 正文措辞、公式、正文图片和延伸阅读链接来自 Markdown；封面图等平台字段来自本 review note。微信底部“阅读原文”默认留空，只有人工明确指定目标时才写入 front matter。

## 微信草稿箱记录

- 草稿状态: updated via official WeChat draft API, pending WeChat backend preview
- 草稿 media_id: `OW4ZgzIulHGwsx2YUygit8W5lJ84JuQVMz4NFRpBMgLqu_P2CwMhp5uLAs3CfZau`
- 创建时间: `2026-06-09T12:31:43+08:00`
- 更新时间: `2026-06-10T21:14:24+08:00`
- 更新说明: 使用 `academic-clean` 主题和 `mathjax-svg` 公式渲染路线重新提交，封面切换为 v2 短文字封面。
- 阅读原文: 默认留空；读者侧链接放在正文 `延伸阅读` 中。
- 发布状态: not published; final publication remains manual in the WeChat backend

## 证据来源

- DOI: https://doi.org/10.1007/s12273-025-1379-7
- Zotero: `CGKPKZ8I`
- 摘要来源: Zotero Local API `abstractNote`; 中文摘要为英文原摘要的忠实翻译，公众号正文同时保留英文原摘要。
- PDF / 作者稿: 用户确认其为论文作者，可以直接使用该论文 PDF 中的图片；本稿图片已从 PDF 内嵌图片条带抽取并拼接为正文素材。

## 源文件获取记录

- Zotero key: `CGKPKZ8I`
- Zotero 元数据: checked via Zotero Desktop Local API
- Zotero 附件记录: checked via Zotero Desktop Local API
- 本地 PDF 附件: exists
- PDF 附件候选: not fully enumerated in this review note; used the available Zotero local paper PDF already checked for this article
- PDF 选择优先级: author manuscript > publisher version of record > OA platform PDF > preprint > other
- 已选 PDF 类型: Zotero local paper PDF; treated as the article's usable paper PDF for body evidence and figure extraction
- 低优先级选择原因: not applicable; no lower-priority web/preprint source was used
- PDF 来源类型: Zotero local attachment; author-confirmed WOEAI/user-authored paper
- PDF 私有存放: Zotero private attachment / local private working copy; no PDF committed to this public repository
- Zotero Web API `/file`: not needed
- 网页 PDF 下载: not used
- 网页 PDF 批准记录: not applicable
- 摘要依据: Zotero `abstractNote`, with faithful Chinese translation and original English abstract kept in the public article
- 正文证据依据: paper PDF body and public publication metadata
- 图片依据: PDF embedded figures extracted from the paper PDF
- 私有信息边界: no absolute private file path, credential, cookie, raw API payload, or downloaded PDF content is recorded here

## 关键事实证据定位记录

- 摘要:
  - 文章使用: 中文摘要为英文原摘要的忠实翻译，并附英文原摘要。
  - 证据位置: Zotero Desktop Local API `abstractNote`; PDF abstract location: `pending PDF page audit`.
- 核心结论: 预计算 CFD 数据库将中尺度气象输入、微尺度 CFD 计算和数据库组织连接起来，用于快速城市微尺度风环境预测。
  - 证据位置: PDF file page 04, Fig. 1; paper workflow and WRF/CFD/database discussion around Sections 3.2-3.3.
- 核心结论: 深圳研究区域按 `1 km x 1 km` 区块组织，并以区块模拟结果构建可调用数据库。
  - 证据位置: PDF file page 05, Fig. 2; Section 3.3.1 text on block division and computational domain.
- 核心结论: 验证部分使用气象自动站数据、90°/120°主风向和不同风速阈值，`11 m/s` 阈值用于高风速条件比较。
  - 证据位置: PDF file page 18, Fig. 21 and Table 7; validation discussion below Fig. 21.
- 核心结论: WebGIS 平台展示风速和风压数据，使预计算 CFD 数据库进入可视化和工程沟通场景。
  - 证据位置: PDF file page 22, Fig. 25; text above Section 5.4 describing Cesium/WebGIS visualization.
- 关键图:
  - Fig. 1 `Workflow of the proposed framework`: PDF file page 04; used as article Figure 1.
  - Fig. 2 `Schematic diagram of block division of buildings in Shenzhen`: PDF file page 05; used as article Figure 2.
  - Fig. 21 `Locations and observation environment of meteorological automatic stations`: PDF file page 18; used as article Figure 21.
  - Fig. 25 `Visual representation of wind speed and wind pressure data on WebGIS`: PDF file page 22; used as article Figure 25.
- 关键公式:
  - Article formula `E = (K_CFD - K_m) / K_m x 100%`: editorial explanatory formula added in the WeChat article to explain wind-speed-ratio relative error. It is not recorded here as a numbered paper equation. The paper evidence it explains is the field-validation comparison around PDF file page 18 and the subsequent validation discussion.
  - Paper Eq. (10) on PDF file page 22 is visible in the source page but is not used in the current WeChat article body.
- 页码审计依据: local ignored PDF file page renders under `wechat/.local/ref-zhao2026-BS/pdf-pages/` were used only for evidence-location audit; no absolute private source PDF path is recorded.

## 封面图

- 封面状态: selected v2 cover from upgraded batch cover workflow; existing WeChat draft still needs a live API update before backend preview changes
- 封面素材: `wechat/assets/public-safe/ref-zhao2026-BS/cover-wechat-900x383-v2.png`
- 生成原图: `wechat/.local/cover-candidates/batch-2026-06-10/ref-zhao2026-BS-v2-imagegen.png`
- 尺寸: final `900 x 383 px`
- 生成方式: image-gen public-safe candidate selected after upgraded batch `wechat-cover` comparison
- 设计意图: 用模块化城市区块、风场流线、数据网格和数据库层表达“城市微尺度风环境 + 预计算 CFD 数据库 + 快速调用”。
- 文字策略: short embedded Chinese hook; category tag `数值风洞`; hook `把风场预先算好`
- 本地裁剪预览: `wechat/.local/cover-previews/batch-2026-06-10-v2-quality-board.html`
- 批量候选联系表: `wechat/.local/cover-candidates/batch-2026-06-10/contact-sheet-v2.png`
- 裁剪预览结果: passed local ratio, file-size, small-thumbnail, and text-quality checks (`900 x 383 px`, ratio delta `0.0`)
- 微信后台预览: pending live draft update and WeChat backend mobile preview

## 图片使用记录

首次 API 实操策略: upload all four approved body images and replace their local Markdown paths with WeChat image URLs in the submitted HTML.

1. 图 1: 所提出框架的工作流程
   - 用途: 方法总览首图
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2026-BS/fig-01-workflow.png`
   - 来源/版权: paper PDF embedded images; author confirmed usable
   - API 实操: approved for upload in first live draft test
   - 公众号图名: 图 1 所提出框架的工作流程
   - 公众号说明: 将城市微尺度风场计算前置，并面向快速预测和工程应用调用。
   - 移动端预览: pending WeChat backend mobile preview
2. 图 2: 深圳建筑分块划分示意图
   - 用途: 解释 `1 km x 1 km` 区块数据库
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2026-BS/fig-02-block-division.png`
   - 来源/版权: paper PDF embedded images; author confirmed usable
   - API 实操: approved for upload in first live draft test
   - 公众号图名: 图 2 深圳建筑分块划分示意图
   - 公众号说明: 城市区域被组织为可计算、可拼接、可入库的微尺度风场单元。
   - 移动端预览: pending WeChat backend mobile preview
3. 图 21: 气象自动站的位置与观测环境
   - 用途: 展示实测验证数据来源
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2026-BS/fig-21-stations.png`
   - 来源/版权: paper PDF embedded images; author confirmed usable
   - API 实操: approved for upload in first live draft test
   - 公众号图名: 图 21 气象自动站的位置与观测环境
   - 公众号说明: 用现场监测数据检验区块 CFD 数据库的预测能力。
   - 移动端预览: pending WeChat backend mobile preview
4. 图 25: WebGIS 中风速与风压数据的可视化展示
   - 用途: 展示 WebGIS 平台应用效果
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2026-BS/fig-25-webgis.png`
   - 来源/版权: paper PDF embedded images; author confirmed usable
   - API 实操: approved for upload in first live draft test
   - 公众号图名: 图 25 WebGIS 中风速与风压数据的可视化展示
   - 公众号说明: 让预计算 CFD 数据库具备查询、展示和工程沟通能力。
   - 移动端预览: pending WeChat backend mobile preview

## 公式检查

- 使用公式: yes
- 呈现方式: Markdown LaTeX formula embedded in the relevant findings section; default API renderer is `mathjax-svg` with source `data-formula` metadata, with `lightweight` HTML kept only as fallback
- 微信公式渲染路线: MathJax SVG route validated by 2026-06-10 single-article stress draft; this article still needs final WeChat backend mobile preview before publication
- RTD 呈现方式: Sphinx MathJax with `.. math::` and `:math:` roles
- 行内变量/量纲: formula markup applied to `X_L`, `R`, `H_{\mathrm{max}}`, block dimensions, wind-speed threshold, wind directions, and percentages
- 文字性下标: use explicit roman text such as `\mathrm{max}`, `\mathrm{CFD}`, and `\mathrm{m}` in WeChat/RTD formulas
- 固定公式小节: removed; formula appears only where needed in the validation discussion
- 移动端预览: pending WeChat backend mobile preview

## 公开安全

- [x] No WeChat AppSecret, token, cookie, or credential appears.
- [x] No Zotero API key appears.
- [x] No private partner name appears.
- [x] No unconfirmed project status appears.
- [x] Reader-facing Markdown has no production notes, pending placeholders, or private paths.
- [x] Reader-facing Markdown has no fixed `公式说明` section or `联系入口` section.
- [x] Reader-facing Markdown uses direct Markdown hyperlinks under `延伸阅读`; rendered HTML should show Chinese link text only.
- [x] Figure captions use a Chinese figure-title line translated from the paper title plus a separate Chinese explanatory line.

## 发布前任务

- [x] 用 Zotero/PDF 核对作者、期刊、页码、DOI、公式和图题。
- [x] 用 Zotero Local API `abstractNote` 补入中文摘要和英文原摘要。
- [x] 导入已确认可用的原始高清图。
- [x] 由公众号正文转换生成 RTD 配套页，保持标题、正文、图片、DOI 和延伸阅读链接一致。
- [x] 将 RTD 配套页挂入 `科研方向 Research` 页面的 `学术进展 Academic Progress`，归入 `建筑结构抗风 / 数值风洞与湍动入流`。
- [ ] 公众号后台手机预览正文、公式和图片。
- [ ] 发布后回填 `latest_published_url` 和 `wechat_status`。

## 检查记录

- image extraction: `pdfimages -all` from paper PDF, then `ffmpeg` vertical stitching of embedded image strips
- cover-v2 generation: selected `wechat/assets/public-safe/ref-zhao2026-BS/cover-wechat-900x383-v2.png` from upgraded batch `wechat-cover` image-gen workflow
- cover-v2 preview: passed (`python3 .agents/skills/wechat-cover/scripts/cover_preview.py -o wechat/.local/cover-previews/batch-2026-06-10-v2-quality-board.html ...`)
- public-safety: passed (`/opt/homebrew/bin/python3.12 scripts/check-public-safe-content.py`)
- markdown whitespace: passed (`git diff --check` on WeChat article-related files)
- image links: passed (4 Markdown image links resolve to local public-safe assets)
- docs-check: passed (`PYTHON_BIN=/opt/homebrew/bin/python3.12 ./scripts/check-docs.sh`)
