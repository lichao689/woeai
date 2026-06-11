---
publication_ref: ref-yang2025-JBE
zotero_key: YZ2D62NB
doi: 10.1016/j.jobe.2025.113635
research_family: 建筑结构抗风
subdirection: 高层建筑抗风与优化
publication_mode: first_publish
wechat_status: ready_to_publish
wechat_draft_media_id: OW4ZgzIulHGwsx2YUygit6lI0lhxR21qVyY_pQ7LoFA4ixT5LPZCBp8tyxGpfQBv
wechat_draft_created_at: 2026-06-10T20:05:09+08:00
wechat_draft_updated_at: 2026-06-11T16:42:02+08:00
wechat_author: Yang Junhui
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

# ref-yang2025-JBE 发布说明

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/ref-yang2025-JBE.md`
- RTD 配套页: `docs/source/paper-notes/ref-yang2025-JBE.rst`
- 微信草稿作者字段: `Yang Junhui`

## RTD 转换记录

- 内容母版: `wechat/articles/draft-public-safe/ref-yang2025-JBE.md`
- 正式转换命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-yang2025-JBE`
- 同步检查命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-yang2025-JBE --check`
- RTD 顶部封面: not set for this package; body figures are inserted in the article flow
- 转换规则: 正文措辞、正文图片、公式语义和延伸阅读链接来自 Markdown；平台字段来自 review note。微信底部 `content_source_url` 默认使用当前论文 RTD 解读页（`https://woeai.readthedocs.io/zh-cn/latest/paper-notes/ref-yang2025-JBE.html`）。
- 导航状态: `docs/source/Research.rst` should list this page under `建筑结构抗风 / 高层建筑抗风与优化` in `学术进展 Academic Progress`.

## 证据来源

- DOI: https://doi.org/10.1016/j.jobe.2025.113635
- Zotero: `YZ2D62NB`
- PDF attachment key: `XF4GB5L9`
- 摘要来源: Zotero Desktop Local API `abstractNote` and PDF abstract; 中文摘要为英文原摘要的忠实翻译，公众号正文同时保留英文原摘要。
- PDF / 作者稿: Zotero local imported PDF attachment exists; the selected local publisher-record PDF was used for article evidence and body figures.
- 公开网站记录: `docs/source/Publications.rst` contains `ref-yang2025-JBE` as paper `[67]`; `docs/data/publication-research-map.json` maps it to `建筑结构抗风 / 高层建筑抗风与优化`.

## 源文件获取记录

- Zotero key: `YZ2D62NB`
- Zotero 元数据: checked via Zotero Desktop Local API
- Zotero 附件记录: checked via Zotero Desktop Local API; one PDF attachment record and one HTML attachment record exist
- 本地 PDF 附件: exists
- PDF 附件候选: one PDF-like Zotero local imported attachment, child key `XF4GB5L9`
- PDF 选择优先级: author manuscript > publisher version of record > OA platform PDF > preprint > other
- 已选 PDF 类型: Zotero local imported publisher-record PDF, treated as the usable paper PDF for this WOEAI/user-authored article
- 低优先级选择原因: not applicable; no web, preprint, or lower-priority substitute source was used
- PDF 来源类型: Zotero local attachment
- PDF 私有存放: Zotero private attachment and ignored local working artifacts under `wechat/.local/ref-yang2025-JBE/`
- Zotero Web API `/file`: not needed
- 网页 PDF 下载: not used
- 网页 PDF 批准记录: not applicable
- 摘要依据: Zotero `abstractNote` and PDF abstract on PDF file page 1
- 正文证据依据: PDF body, Zotero metadata, and public WOEAI publication record
- 图片依据: PDF embedded figures and page-render crops extracted from the local paper PDF and copied into public-safe body JPG assets
- 私有信息边界: no absolute private file path, credential, cookie, raw API payload, raw downloaded PDF content, or private preview URL is recorded here

## 关键事实证据定位记录

- 摘要:
  - 文章使用: 中文摘要忠实翻译英文摘要，并附英文原摘要。
  - 证据位置: Zotero `abstractNote`; PDF file page 1 abstract.
- 核心结论: 结构位移和人体对加速度的感知是二维矢量过程，只关注一维主轴方向响应会显著低估建筑实际极值响应。
  - 证据位置: PDF file page 1 abstract; PDF file pages 2-3, Section 1.
- 核心结论: 楼面角点响应由中心点平动响应和扭转响应共同决定，二维合成响应可由 $A(t)=\sqrt{X^2(t)+Y^2(t)}$ 表示。
  - 证据位置: PDF file pages 6-7, Section 2.2, Fig. 1, Eqs. (22)-(24).
- 核心结论: SRSS、ERF 和 CPF 方法没有充分考虑方向响应相关性，CDC 方法在二维矢量响应极值计算中最准确，RPA 方法可以量化一维分量响应和二维矢量响应的相关及角度关系。
  - 证据位置: PDF file pages 9-12, Section 3.1, Figs. 2-5; PDF file page 22, conclusion item 1.
- 核心结论: 随机信号算例中，SRSS、ERF、CPF、RPA、CDC 的代表性误差分别包括约 `25.76%`, `-7.18%`, `4.40%`, `-2.54%`, and `0.61%`; 参数扫描中 CDC 最大偏差约 `4%`。
  - 证据位置: PDF file pages 9-12, Section 3.1, Figs. 3-5.
- 核心结论: 对本文高层建筑模型，位移响应可主要考虑前 `3` 阶振型；加速度响应高阶振型贡献更明显，建议考虑前 `11` 阶振型。
  - 证据位置: PDF file pages 15-16, Section 3.2.3, Figs. 12-13; PDF file page 22, conclusion item 2.
- 核心结论: 风向角和宽深比会显著影响二维矢量响应极值；建筑主轴应尽量避免与当地主导风向一致，以降低较大横风向响应。
  - 证据位置: PDF file pages 19-20, Section 3.3.1, Figs. 18-19; PDF file page 23, conclusion item 3.
- 核心结论: 当宽深比不小于 `2:1` 时，只考虑中心点主轴方向响应极值可能造成约 `19%` 以上偏差；角点位置应作为舒适度和二维矢量响应评估重点。
  - 证据位置: PDF file pages 20-21, Section 3.3.1, Table 4, Fig. 20; PDF file page 23, conclusion item 4.
- 核心结论: 较大的扭转周期比会增大主轴方向与二维矢量方向极值偏差，不利于结构设计，应在设计中尽量避免。
  - 证据位置: PDF file pages 21-23, Section 3.3.2, Fig. 21, conclusion item 5.
- 核心边界: 结论基于稳态高斯随机过程、文中高层建筑模型、风洞试验风荷载数据、PI 方法和给定宽深比/扭转周期比工况；不同结构体系或非高斯/非线性响应需要重新核验。
  - 证据位置: PDF file pages 6-8, Section 2.2 assumptions and methods; PDF file pages 12-23, Sections 3-4.
- 关键图:
  - Fig. 1 `Building principal axes and wind direction`: PDF file page 6; used as article Figure 1; asset `wechat/assets/public-safe/ref-yang2025-JBE/fig-01-building-principal-axes-wind-direction.jpg`.
  - Fig. 3 `Results and errors of the 2D vectorial response extreme value synthesis`: PDF file page 10; used as article Figure 3; asset `wechat/assets/public-safe/ref-yang2025-JBE/fig-03-method-error-random-signals.jpg`.
  - Fig. 5 `Error of extreme value of 2D vectorial response with different σX/σY and ρXY`: PDF file page 12; used as article Figure 5; asset `wechat/assets/public-safe/ref-yang2025-JBE/fig-05-error-correlation-map.jpg`.
  - Fig. 17 `FE models of the building frame`: PDF file page 18; used as article Figure 17; asset `wechat/assets/public-safe/ref-yang2025-JBE/fig-17-width-depth-fe-models.jpg`.
  - Fig. 18 `Extreme values of principal-axis response and combined response at the top corners of buildings with different width-to-depth ratios`: PDF file page 20; used as article Figure 18; asset `wechat/assets/public-safe/ref-yang2025-JBE/fig-18-width-depth-wind-direction-response.jpg`.
  - Fig. 20 `Ratio of principal-axis response at the center point to combined response at the top corner point of buildings with different width-to-depth ratios`: PDF file page 21; used as article Figure 20; asset `wechat/assets/public-safe/ref-yang2025-JBE/fig-20-center-corner-response-ratio.jpg`.
- 关键公式:
  - 文章使用: paper formula `$A(t)=\sqrt{X^2(t)+Y^2(t)}$` for 2D vectorial response timescale.
  - 证据位置: PDF file page 7, Section 2.2, Eq. (24).
  - 文章使用: inline variables `$X(t)$`, `$Y(t)$`, `$A(t)$`, `$C$`, `$\rho_{XY}$`, `$\sigma_X/\sigma_Y$`, `$1:1$`, `$2:1$`, `$3:1$`, `$45^\circ$`, and percentage quantities used in method and engineering explanations.
  - 证据位置: PDF file pages 6-23, Sections 2.2-4, Figs. 1-21, Table 4.
- 页码口径: evidence locations use PDF file page numbers, not journal printed page numbers or article pagination.

## 图片使用记录

1. 图 1: 建筑主轴和风向
   - 用途: 开篇说明二维矢量响应和角点响应的几何来源
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-yang2025-JBE/fig-01-building-principal-axes-wind-direction.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 1 建筑主轴和风向
   - 公众号说明: 展示楼面主轴、风向角和角点位置关系。
   - 移动端预览: pending WeChat backend mobile preview
2. 图 3: 二维矢量响应极值合成结果和误差
   - 用途: 方法误差直观比较
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-yang2025-JBE/fig-03-method-error-random-signals.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 3 二维矢量响应极值合成结果和误差
   - 公众号说明: 展示 SRSS、ERF、CDC、RPA 和 CPF 在随机信号算例中的极值估计差异。
   - 移动端预览: pending WeChat backend mobile preview
3. 图 5: 不同标准差比和相关系数下的二维矢量响应极值误差
   - 用途: 展示方法对相关性和标准差比的响应
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-yang2025-JBE/fig-05-error-correlation-map.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 5 不同标准差比和相关系数下的二维矢量响应极值误差
   - 公众号说明: 显示 CDC 和 RPA 能够更好反映 $\rho_{XY}$ 与 $\sigma_X/\sigma_Y$ 的变化。
   - 移动端预览: pending WeChat backend mobile preview
4. 图 17: 建筑框架有限元模型
   - 用途: 说明不同宽深比建筑模型
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-yang2025-JBE/fig-17-width-depth-fe-models.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 17 建筑框架有限元模型
   - 公众号说明: 展示 $1:1$、$2:1$ 和 $3:1$ 宽深比模型。
   - 移动端预览: pending WeChat backend mobile preview
5. 图 18: 不同宽深比建筑顶层角点的主轴响应和合成响应极值
   - 用途: 说明风向角和宽深比对二维极值的影响
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-yang2025-JBE/fig-18-width-depth-wind-direction-response.jpg`
   - 来源/版权: paper PDF page-render crop; WOEAI/user-authored paper workflow scope
   - 抽取方式: rendered PDF file page 20 and cropped to the figure body
   - 公众号图名: 图 18 不同宽深比建筑顶层角点的主轴响应和合成响应极值
   - 公众号说明: 比较不同宽深比模型在风向角变化下的位移和加速度极值。
   - 移动端预览: pending WeChat backend mobile preview
6. 图 20: 中心点主轴响应与角点合成响应之比
   - 用途: 说明只看中心点可能低估角点二维响应
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-yang2025-JBE/fig-20-center-corner-response-ratio.jpg`
   - 来源/版权: paper PDF page-render crop; WOEAI/user-authored paper workflow scope
   - 抽取方式: rendered PDF file page 21 and cropped to the figure body
   - 公众号图名: 图 20 中心点主轴响应与角点合成响应之比
   - 公众号说明: 比较楼面中心点主轴响应与顶层角点二维合成响应。
   - 移动端预览: pending WeChat backend mobile preview

## 公式检查

- 使用公式: yes; one paper display formula and inline mathematical quantities
- 呈现方式: Markdown LaTeX source; default WeChat API rendering is MathJax SVG with `data-formula` metadata
- 微信公式渲染路线: `mathjax-svg` unless a fallback reason is recorded
- RTD 呈现方式: Sphinx math roles/directives generated by `wechat/tools/markdown_to_rtd.py`
- 行内变量/量纲: formula markup applied to `$X(t)$`, `$Y(t)$`, `$A(t)$`, `$\rho_{XY}$`, `$\sigma_X/\sigma_Y$`, `$45^\circ$`, ratio labels, and percentage quantities
- 移动端预览: pending WeChat backend mobile preview

## 封面图

- 封面状态: regenerated with image-gen-text; user selected the second candidate for live draft update
- 候选数量: 3 concept directions documented in `wechat/articles/review/ref-yang2025-JBE.cover-brief.md`; 3 image-gen-text candidates generated in this round
- 选中候选: `cover-wechat-900x383-imagegen-v5b-pub-line-route`
- 用户确认封面文字: `结构抗风 | 楼层矢量极值 / 高层风振如何算准`
- cover_text_confirmation: user-confirmed
- confirmed_cover_text: `结构抗风 | 楼层矢量极值 / 高层风振如何算准`
- confirmed_text_mode: `image-gen-text`
- confirmation_note: confirmed in chat after 5+1 cover-text choice test; user selected v5 scheme B for draft cover update on 2026-06-11
- 文字模式: image-gen-text
- 生成工具: Codex image generation tool
- 图像生成场景: 高层建筑风致二维矢量响应、角点加速度、风向角、中心点与角点响应差异、CDC/RPA 等二维极值方法比较
- 要求文字: `结构抗风 | 楼层矢量极值 / 高层风振如何算准`
- 备用封面: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-v1.png)`
- 当前草稿封面更新前: `wechat/assets/public-safe/ref-yang2025-JBE/cover-wechat-900x383-imagegen-v2.png`
- 候选 A: `wechat/assets/public-safe/ref-yang2025-JBE/cover-wechat-900x383-imagegen-v5a-pub-line-route.png`
- 候选 B: `wechat/assets/public-safe/ref-yang2025-JBE/cover-wechat-900x383-imagegen-v5b-pub-line-route.png`
- 候选 C: `wechat/assets/public-safe/ref-yang2025-JBE/cover-wechat-900x383-imagegen-v5c-pub-line-route.png`
- 已废弃本地实验: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-v4.png)`; rejected because the post-generation text workflow was removed
- 封面素材: `wechat/assets/public-safe/ref-yang2025-JBE/cover-wechat-900x383-imagegen-v5b-pub-line-route.png`
- 尺寸: `900 x 383 px`
- 本地总览图: `wechat/.local/cover-previews/batch-10-imagegen-contact-sheet.png`
- 本地裁剪预览: `wechat/.local/cover-previews/ref-yang2025-JBE-imagegen-v5-cover-preview.html`
- 审核状态: user selected v5 scheme B; local crop preview passed; WeChat backend mobile preview not yet checked
- 草稿状态: existing WeChat draft updated with `cover-wechat-900x383-imagegen-v5b-pub-line-route.png` at 2026-06-11T16:42:02+08:00; WeChat backend mobile preview not yet checked.
- 注意: `cover_image_checked` remains `false` until the WeChat backend mobile preview is checked.

### 本轮 v5 重新生成候选

- cover_execution_mode: `image-gen`
- cover_text_confirmation: reused prior user-confirmed cover text from this review note and cover brief
- confirmed_cover_text: `结构抗风 | 楼层矢量极值 / 高层风振如何算准`
- confirmed_text_mode: `image-gen-text`
- publication metadata line: `Journal of Building Engineering · 2025`
- metadata style: subtitle-below semi-bold deep-blue text line; no leading dot, no icon, no badge, no capsule, no button-like outline
- candidate count: 3
- candidate A path: `wechat/assets/public-safe/ref-yang2025-JBE/cover-wechat-900x383-imagegen-v5a-pub-line-route.png`
- candidate B path: `wechat/assets/public-safe/ref-yang2025-JBE/cover-wechat-900x383-imagegen-v5b-pub-line-route.png`
- candidate C path: `wechat/assets/public-safe/ref-yang2025-JBE/cover-wechat-900x383-imagegen-v5c-pub-line-route.png`
- selected candidate: `cover-wechat-900x383-imagegen-v5b-pub-line-route.png`
- user selection: scheme B
- prompt scene: 高层建筑风致二维矢量响应、楼面角点合成矢量、风向角、中心点与角点响应差异、CDC/RPA 等二维极值方法比较
- bottom technical route strip: wind angle and tall-building plan -> correlated X/Y responses -> method comparison curves -> 2D vector extreme envelope -> center-to-corner engineering check
- dimensions: `900 x 383 px`
- local crop preview: `wechat/.local/cover-previews/ref-yang2025-JBE-imagegen-v5-cover-preview.html`
- approval state: user selected scheme B; local visual text check and crop preview passed; WeChat backend mobile preview pending
- draft state: existing WeChat draft updated with `cover-wechat-900x383-imagegen-v5b-pub-line-route.png` at 2026-06-11T16:42:02+08:00; WeChat backend mobile preview not yet checked.

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

- figure extraction: copied selected local extracted PDF embedded JPG images and page-render crops to public-safe asset names
- rtd-generation: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-yang2025-JBE`)
- rtd-sync-check: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-yang2025-JBE --check`)
- public-safety: passed (`python3 scripts/check-public-safe-content.py`)
- whitespace: passed (`git diff --check`)
- docs-build: passed (`./scripts/check-docs.sh`)
