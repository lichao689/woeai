---
publication_ref: ref-zhao2025-SCS
zotero_key: V6PLJENN
doi: 10.1016/j.scs.2025.106237
research_family: 建筑结构抗风
subdirection: 数值风洞与湍动入流
publication_mode: first_publish
wechat_status: reviewing
wechat_author: WOEAI
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

# ref-zhao2025-SCS 发布说明

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/ref-zhao2025-SCS.md`
- RTD 配套页: `docs/source/paper-notes/ref-zhao2025-SCS.rst`
- 封面简报: `wechat/articles/review/ref-zhao2025-SCS.cover-brief.md`
- 微信草稿作者字段: `WOEAI`

## RTD 转换记录

- 内容母版: `wechat/articles/draft-public-safe/ref-zhao2025-SCS.md`
- 正式转换命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2025-SCS`
- 同步检查命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2025-SCS --check`
- RTD 顶部封面: not selected in this worker task; final cover image to be generated separately from the cover brief
- 转换规则: 正文措辞、正文图片、公式语义和延伸阅读链接来自 Markdown；封面图等平台字段留给 review note 或后续发布记录。微信底部 `content_source_url` 默认留空。

## 证据来源

- DOI: https://doi.org/10.1016/j.scs.2025.106237
- Zotero: `V6PLJENN`
- PDF attachment key: `8DSM76PX`
- 摘要来源: Zotero Local API `abstractNote` and PDF abstract; 中文摘要为英文原摘要的忠实翻译，公众号正文同时保留英文原摘要。
- PDF / 作者稿: local Zotero imported PDF attachment exists; PDF body and embedded images were used for article evidence and body figures.
- 公开网站记录: `docs/source/Publications.rst` contains `ref-zhao2025-SCS` as paper `[60]`; `docs/source/BuildingStructuralWindResistance.rst` lists it under `数值风洞与湍动入流`.

## 源文件获取记录

- Zotero key: `V6PLJENN`
- Zotero 元数据: checked via Zotero Desktop Local API artifact
- Zotero 附件记录: checked via Zotero Desktop Local API artifact; PDF attachment and HTML attachment records exist
- 本地 PDF 附件: exists
- PDF 附件候选: single PDF-like attachment in checked child records
- PDF 选择优先级: author manuscript > publisher version of record > OA platform PDF > preprint > other
- 已选 PDF 类型: Zotero local imported PDF attachment, treated as the usable paper PDF for this WOEAI/user-authored article
- 低优先级选择原因: not applicable; no web, preprint, or lower-priority substitute source was used
- PDF 来源类型: Zotero local attachment
- PDF 私有存放: Zotero private attachment and ignored local working artifacts under `wechat/.local/ref-zhao2025-SCS/`
- Zotero Web API `/file`: not needed
- 网页 PDF 下载: not used
- 网页 PDF 批准记录: not applicable
- 摘要依据: Zotero `abstractNote` and PDF abstract on PDF file page 1
- 正文证据依据: PDF body, Zotero metadata, and public WOEAI publication record
- 图片依据: PDF embedded figures extracted from the local paper PDF and converted into public-safe body PNG assets
- 私有信息边界: no absolute private file path, credential, cookie, raw API payload, raw downloaded PDF content, or private preview URL is recorded here

## 关键事实证据定位记录

- 摘要:
  - 文章使用: 中文摘要忠实翻译英文摘要，并附英文原摘要。
  - 证据位置: Zotero `abstractNote`; PDF file page 1 abstract.
- 核心结论: 本文框架由场景分块、改进 3DGS/GaussianPro、点云语义分离、屋面轮廓提取和几何模型生成组成。
  - 证据位置: PDF file page 3, Section 2 `Method`, Fig. 1.
- 核心结论: 本文方法相对 COLMAP 的点云精度平均提高约 `12%`，生成速度明显更快；结论概括为密集建筑点云生成速度比传统方法快 `2`-`3` 倍。
  - 证据位置: PDF file page 10, Section 3.1, Table 2; PDF file page 22, Section 5.
- 核心结论: 几何模型达到 LoD2 和 LoD2.5，屋面细节保留较好，几何规则性有利于 CFD 网格划分。
  - 证据位置: PDF file page 11, Section 3.2; PDF file page 14, Fig. 18.
- 核心结论: CFD 验证采用 $k$-$\omega$ SST RANS 模型、三套网格和 GCI 分析，速度/压力场最大 GCI 为 `3.76%`，湍流量最大 GCI 为 `4.89%`。
  - 证据位置: PDF file pages 12-15, Sections 4.1.1-4.1.3, Table 3.
- 核心结论: 行人舒适度评估使用气象站数据、Weibull 分布、POT 方法和 CFD 风速比，结果中多数监测点为 I/II 类，少数点位为 III/IV 类。
  - 证据位置: PDF file pages 16-19, Sections 4.2.1-4.2.4, Table 6.
- 核心结论: WebGIS 展示将建筑几何、CFD 风场数据、插值和地图平台连接起来，论文将其表述为初步探索。
  - 证据位置: PDF file pages 19-21, Section 4.3, Figs. 32-34.
- 关键图:
  - Fig. 1 `Overall workflow of the algorithm framework`: PDF file page 3; used as article Figure 1; asset `wechat/assets/public-safe/ref-zhao2025-SCS/fig-01-workflow.png`.
  - Fig. 14 `Dense point cloud of selected buildings`: PDF file page 10; used as article Figure 14; asset `wechat/assets/public-safe/ref-zhao2025-SCS/fig-14-dense-point-cloud.png`.
  - Fig. 18 `The results of the geometric model reconstruction`: PDF file page 14; used as article Figure 18; asset `wechat/assets/public-safe/ref-zhao2025-SCS/fig-18-geometry-reconstruction.png`.
  - Fig. 25 `Velocity magnitude at 2 m in the study area`: PDF file page 18; used as article Figure 25; asset `wechat/assets/public-safe/ref-zhao2025-SCS/fig-25-velocity-magnitude.png`.
  - Fig. 34 `The interpolation results of the wind field`: PDF file page 21; used as article Figure 34; asset `wechat/assets/public-safe/ref-zhao2025-SCS/fig-34-webgis-interpolation.png`.
- 关键公式:
  - 文章未使用论文中的重要原始编号公式作为展示公式。
  - 行文使用的 $H_{\mathrm{max}}$、$k$-$\omega$ SST、GCI、$2\,\mathrm{m}$、$7.9$ million、$16.8$ million、$37.9$ million、$12\%$、$3.76\%$ 等变量或数值来自 PDF Sections 3.1, 4.1.1-4.1.3 and Table 3.
  - 论文原始公式 Eq. (14)-Eq. (21) are not reproduced in the current article body.
- 页码口径: evidence locations use PDF file page numbers, not journal printed page numbers or article pagination.

## 图片使用记录

1. 图 1: 算法框架总体流程
   - 用途: 方法总览首图
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2025-SCS/fig-01-workflow.png`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: extracted PDF embedded image converted to PNG public-safe asset
   - 公众号图名: 图 1 算法框架总体流程
   - 公众号说明: 展示从无人机影像、场景分块、改进 GaussianPro 到建筑模型生成的完整路径。
   - 移动端预览: pending WeChat backend mobile preview
2. 图 14: 选定建筑的密集点云
   - 用途: 展示 3DGS 点云生成结果
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2025-SCS/fig-14-dense-point-cloud.png`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: extracted PDF embedded image converted to PNG public-safe asset
   - 公众号图名: 图 14 选定建筑的密集点云
   - 公众号说明: 从初始化点、splat 渲染、高斯椭球到最终点云展示 3DGS 建筑细节生成过程。
   - 移动端预览: pending WeChat backend mobile preview
3. 图 18: 几何模型重建结果
   - 用途: 展示点云到 CFD 几何模型的转换结果
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2025-SCS/fig-18-geometry-reconstruction.png`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: extracted PDF embedded image converted to PNG public-safe asset
   - 公众号图名: 图 18 几何模型重建结果
   - 公众号说明: 将建筑点云、平面轮廓、几何模型和整体场景并列展示。
   - 移动端预览: pending WeChat backend mobile preview
4. 图 25: 研究区域 2 m 高度处的速度幅值
   - 用途: 展示 CFD 风场应用结果
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2025-SCS/fig-25-velocity-magnitude.png`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: extracted PDF embedded image converted to PNG public-safe asset
   - 公众号图名: 图 25 研究区域 2 m 高度处的速度幅值
   - 公众号说明: 连接建筑几何重建与行人高度风环境分析。
   - 移动端预览: pending WeChat backend mobile preview
5. 图 34: 风场插值结果
   - 用途: 展示 WebGIS 应用探索
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2025-SCS/fig-34-webgis-interpolation.png`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: extracted PDF embedded image converted to PNG public-safe asset
   - 公众号图名: 图 34 风场插值结果
   - 公众号说明: 展示风场数据进入地图平台和工程沟通语境的初步效果。
   - 移动端预览: pending WeChat backend mobile preview

## 公式检查

- 使用公式: yes, inline mathematical notation only; no paper numbered equation is reproduced as a display formula
- 呈现方式: Markdown LaTeX source; default WeChat API rendering is MathJax SVG with `data-formula` metadata
- 微信公式渲染路线: `mathjax-svg` unless a fallback reason is recorded
- RTD 呈现方式: Sphinx math roles generated by `wechat/tools/markdown_to_rtd.py`
- 行内变量/量纲: formula markup applied to $H_{\mathrm{max}}$, $k$-$\omega$ SST, $2\,\mathrm{m}$, mesh counts, percentages, LoD descriptors where appropriate
- 移动端预览: pending WeChat backend mobile preview

## 封面图

- 封面状态: not generated in this worker task
- 封面简报: `wechat/articles/review/ref-zhao2025-SCS.cover-brief.md`
- 设计方向: urban buildings with wind-field overlay; Gaussian point-cloud reconstruction to clean building geometry; visual-data-to-simulation-ready model workflow
- 文字策略: no embedded text; rely on the WeChat article title
- 尺寸建议: first-article cover target `900 x 383 px`, core visual centered for crop safety
- 预览状态: pending cover generation and WeChat backend preview

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
- [ ] 由 controller/final integration task 将 RTD 配套页挂入相关科研方向页的 `学术进展 Academic Progress`。
- [ ] 生成并选择最终封面图。
- [ ] 公众号后台手机预览正文、公式和图片。
- [ ] 发布后回填 `latest_published_url` 和 `wechat_status`。

## 检查记录

- figure extraction: `sips` conversion from local extracted PDF embedded images to public-safe PNG assets
- rtd-generation: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2025-SCS`)
- rtd-sync-check: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2025-SCS --check`)
- public-safety: passed (`python3 scripts/check-public-safe-content.py`)
- whitespace: passed (`git diff --check -- wechat/articles/draft-public-safe/ref-zhao2025-SCS.md wechat/articles/review/ref-zhao2025-SCS.review.md wechat/articles/review/ref-zhao2025-SCS.cover-brief.md docs/source/paper-notes/ref-zhao2025-SCS.rst wechat/assets/public-safe/ref-zhao2025-SCS`)
