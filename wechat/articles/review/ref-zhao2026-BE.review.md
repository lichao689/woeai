---
publication_ref: ref-zhao2026-BE
zotero_key: RLAA46YB
doi: 10.1016/j.buildenv.2026.114811
research_family: 建筑结构抗风
subdirection: 数值风洞与湍动入流
publication_mode: first_publish
wechat_status: ready_to_publish
wechat_draft_media_id: OW4ZgzIulHGwsx2YUygityZj6g6Gb7xQ5DECKFvJTTvjKmO-nwhwlO-v7iUt8HF2
wechat_draft_created_at: 2026-06-10T20:06:05+08:00
wechat_draft_updated_at: 2026-06-10T20:06:05+08:00
wechat_author: Zhao Peisheng
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

# ref-zhao2026-BE 发布说明

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/ref-zhao2026-BE.md`
- RTD 配套页: `docs/source/paper-notes/ref-zhao2026-BE.rst`
- 微信草稿作者字段: `Zhao Peisheng`

## RTD 转换记录

- 内容母版: `wechat/articles/draft-public-safe/ref-zhao2026-BE.md`
- 正式转换命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2026-BE`
- 同步检查命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2026-BE --check`
- RTD 顶部封面: not included in this scoped package
- 转换规则: 正文措辞、公式、正文图片和延伸阅读链接来自 Markdown；平台字段来自本 review note。微信底部“阅读原文”默认留空，只有人工明确指定目标时才写入 front matter。

## 证据来源

- DOI: https://doi.org/10.1016/j.buildenv.2026.114811
- Zotero: `RLAA46YB`
- PDF child: `AEY7UUGE`
- PDF 状态: user-confirmed local imported-file PDF; 25 pages; `pdftotext` and `pdfimages` usable
- 摘要来源: Zotero Desktop Local API `abstractNote` was checked; PDF abstract was used to restore the metric values missing from the Zotero text.
- PDF / 作者稿: author-confirmed WOEAI/user-authored paper; original PDF figures may be used for this article package.

## 源文件获取记录

- Zotero key: `RLAA46YB`
- Zotero 元数据: checked via Zotero Desktop Local API
- Zotero 附件记录: checked via Zotero Desktop Local API
- PDF 附件记录: `AEY7UUGE`, `application/pdf`, `linkMode=imported_file`
- 非 PDF 附件记录: one imported-url HTML child was present and was not used for body evidence or figure extraction
- 本地 PDF 附件: exists and readable
- PDF 选择优先级: author manuscript > publisher version of record > OA platform PDF > preprint > other
- 已选 PDF 类型: Zotero local imported-file journal pre-proof PDF for the author paper
- 低优先级选择原因: not applicable; only one PDF-like Zotero attachment was used, and no web/preprint PDF was selected
- PDF 来源类型: Zotero local attachment; author-confirmed WOEAI/user-authored paper
- PDF 私有存放: Zotero private attachment plus ignored `wechat/.local/ref-zhao2026-BE/` working copy; no PDF committed to this public repository
- Zotero Web API `/file`: not attempted; local PDF was available
- 网页 PDF 下载: not used
- 网页 PDF 批准记录: not applicable
- 摘要依据: PDF abstract on `PDF file page 3`; Zotero `abstractNote` checked but missing metric tokens
- 正文证据依据: paper PDF body, figures, conclusion, and public publication metadata
- 图片依据: PDF embedded images extracted with `pdfimages -png -p`
- 私有信息边界: no absolute private file path, credential, cookie, raw API payload, or downloaded PDF content is recorded here

## 关键事实证据定位记录

- 摘要:
  - 文章使用: 中文摘要为 PDF abstract 的忠实翻译，并附英文原摘要。
  - 证据位置: `PDF file page 3`, Abstract.
- 核心结论: 论文提出从高分辨率 GF-7 立体卫星影像到 CFD 可用城市几何的快速重建框架。
  - 证据位置: `PDF file page 5`, Section 2 and Fig. 1.
- 核心结论: GF-7 多光谱与前后视全色立体影像经过正射校正、融合和本地数据集构建后，用于建筑轮廓与高度建模。
  - 证据位置: `PDF file page 6`, Section 2.1 and Fig. 2.
- 核心结论: RS-Mamba building footprint extraction reached Precision 0.9602, Recall 0.9166, F1-score 0.9379, and IoU 0.9178 on the reported test data.
  - 证据位置: `PDF file page 9`, Section 2.2.3.
- 核心结论: DSM-Net disparity estimation, forward intersection, point-cloud generation, and DSM projection support the building-height estimation chain.
  - 证据位置: `PDF file page 12`, Section 2.3.2 and Fig. 8.
- 核心结论: Contour simplification, regularization, and LoD1 extrusion turn remote-sensing outputs into simulation-oriented geometry.
  - 证据位置: `PDF file page 13`, Sections 3.1-3.2; `PDF file page 14`, Figs. 9-10.
- 核心结论: UAV-LiDAR validation yielded `R2 = 0.91`, `MAE = 2.72 m`, and `RMSE = 4.09 m`; DSM-Net also outperformed SGM and MGM in the reported building-height comparison.
  - 证据位置: `PDF file page 17`, Section 4.2-4.3 and Eqs. 17-19; `PDF file page 19`, Fig. 14.
- 核心结论: The framework mitigates GF-7 tailing effects and supports numerical stability for high-fidelity urban wind environment simulation, while limitations remain for dense urban-village adhesion and simplified vegetation representation.
  - 证据位置: `PDF file page 18`, Conclusion item iv and limitations; `PDF file page 19`, continuation below Fig. 14.
- 关键图:
  - Fig. 1 `Overall workflow of the proposed framework`: `PDF file page 5`; used as article Figure 1.
  - Fig. 2 `The MUX and PAN dataset of GF-7`: `PDF file page 6`; used as article Figure 2.
  - Fig. 10 `Local views of 3D building geometries`: `PDF file page 14`; used as article Figure 10.
  - Fig. 14 `Comparison of different algorithms for DSM generation and building height estimation`: `PDF file page 19`; used as article Figure 14.
- 关键公式:
  - Paper Eq. (13), EVI for vegetation extraction: `PDF file page 13`; referenced conceptually in the article but not reproduced as a display formula.
  - Paper Eqs. (17)-(19), `R2`, `RMSE`, and `MAE` validation metrics: `PDF file page 17`; article uses the metric names and reported values, not the full equations.
  - Article formulas are inline explanatory notation for `R^2`, `MAE`, `RMSE`, `1 m`, `0.68 m`, and related quantities; no editorial-only display formula is introduced.
- 页码审计依据: PDF file pages were audited using local private PDF renders/text extraction under ignored `wechat/.local/ref-zhao2026-BE/`; no absolute private source PDF path is recorded.

## 图片使用记录

1. 图 1: 所提出框架的整体流程
   - 用途: 方法总览首图
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2026-BE/fig-01-workflow.png`
   - 来源/版权: PDF embedded image; author-confirmed WOEAI/user-authored paper
   - 抽取方式: `pdfimages -png -p`
   - 公众号图名: 图 1 所提出框架的整体流程
   - 公众号说明: 框架把建筑轮廓提取、视差估计、点云生成、DSM 投影和 LoD1 几何建模连接起来。
   - 移动端预览: pending WeChat backend mobile preview
2. 图 2: GF-7 的 MUX 与 PAN 数据集
   - 用途: 展示卫星影像数据源
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2026-BE/fig-02-gf7-dataset.png`
   - 来源/版权: PDF embedded image; author-confirmed WOEAI/user-authored paper
   - 抽取方式: `pdfimages -png -p`
   - 公众号图名: 图 2 GF-7 的 MUX 与 PAN 数据集
   - 公众号说明: GF-7 多光谱与全色影像提供了城市尺度覆盖和局部建筑细节。
   - 移动端预览: pending WeChat backend mobile preview
3. 图 10: 三维建筑几何的局部视图
   - 用途: 展示 LoD1 几何重建结果
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2026-BE/fig-10-local-geometry.png`
   - 来源/版权: PDF embedded image; author-confirmed WOEAI/user-authored paper
   - 抽取方式: `pdfimages -png -p`
   - 公众号图名: 图 10 三维建筑几何的局部视图
   - 公众号说明: 局部结果展示了规则化后的 LoD1 城市几何。
   - 移动端预览: pending WeChat backend mobile preview
4. 图 14: 不同 DSM 生成与建筑高度估计算法的比较
   - 用途: 展示验证与算法对比
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-zhao2026-BE/fig-14-dsm-comparison.png`
   - 来源/版权: PDF embedded image; author-confirmed WOEAI/user-authored paper
   - 抽取方式: `pdfimages -png -p`
   - 公众号图名: 图 14 不同 DSM 生成与建筑高度估计算法的比较
   - 公众号说明: DSM-Net 的高度曲线更接近 LiDAR 参考结果。
   - 移动端预览: pending WeChat backend mobile preview

## 公式检查

- 使用公式: yes, inline notation only
- 呈现方式: Markdown LaTeX for inline quantities and metrics
- 微信公式渲染路线: default API renderer should use `mathjax-svg`; this article still needs final WeChat backend mobile preview before publication
- RTD 呈现方式: Sphinx MathJax inline roles generated by `markdown_to_rtd.py`
- 行内变量/量纲: formula markup applied to `R^2`, `MAE`, `RMSE`, `1 m`, and `0.68 m`
- 固定公式小节: not used
- 移动端预览: pending WeChat backend mobile preview

## 封面图

- 封面状态: regenerated with image-gen-text; WeChat draft updated; pending WeChat backend mobile preview
- 候选数量: 3 concept directions documented in `wechat/articles/review/ref-zhao2026-BE.cover-brief.md`; 1 selected image-gen-text cover exported
- 选中候选: `cover-wechat-900x383-imagegen-v1`
- 文字模式: image-gen-text
- 生成工具: Codex image generation tool
- 图像生成场景: 卫星影像到 CFD 可用城市建筑几何、DSM、城市风环境
- 要求文字: `数值风洞 / 卫星转几何 / 城市CFD建模`
- 备用封面: `wechat/assets/public-safe/ref-zhao2026-BE/cover-wechat-900x383-v1.png`
- 封面素材: `wechat/assets/public-safe/ref-zhao2026-BE/cover-wechat-900x383-imagegen-v1.png`
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
- [x] Reader-facing Markdown has no YAML front matter, editor notes, or private paths.
- [x] Reader-facing Markdown has no separate `卷期页码` field.
- [x] Reader-facing Markdown uses direct Markdown hyperlinks under `延伸阅读`.
- [x] Figure captions use a Chinese figure-title line translated from the paper figure title plus a separate Chinese explanatory line.

## 发布前任务

- [x] 用 Zotero Desktop Local API 核对作者、期刊、年份、DOI、摘要和附件记录。
- [x] 用本地 PDF 核对英文摘要、正文证据、关键图、关键公式和页码。
- [x] 从 PDF 抽取并放入 public-safe 正文图片。
- [x] 由公众号正文转换生成 RTD 配套页，保持标题、正文、图片、DOI 和延伸阅读链接一致。
- [ ] 主线程挂入方向页、首页或 backlog 状态。
- [ ] 公众号后台手机预览正文、公式、封面和图片。
- [x] 已生成公众号首图封面并记录封面素材；微信后台手机预览 pending。

## 检查记录

- image extraction: `pdfimages -png -p` from Zotero local PDF working copy
- RTD conversion: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2026-BE`
- RTD sync check: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-zhao2026-BE --check`
- public-safety: scoped check for `ref-zhao2026-BE` article and review note
- markdown whitespace: scoped `git diff --check --` on assigned text paths and public-safe asset directory
- docs-check: `PYTHON_BIN=/opt/homebrew/bin/python3.12 ./scripts/check-docs.sh` passed after main-thread shared navigation integration
