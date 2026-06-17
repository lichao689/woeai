---
publication_ref: ref-tang2025-JBE
zotero_key: 4BCF65NB
doi: 10.1016/j.jobe.2025.112131
research_family: 建筑结构抗风
subdirection: 高层建筑抗风与优化
publication_mode: first_publish
wechat_status: ready_to_publish
wechat_author: Tang Ao
source_checked: true
abstract_checked: true
copyright_checked: true
public_safety_checked: true
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
body_images_upload_approved: true
rtd_page_checked: true
rtd_cover_image: wechat/assets/public-safe/ref-tang2025-JBE/cover-wechat-900x383-v2.png
---

# ref-tang2025-JBE 发布说明

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/ref-tang2025-JBE.md`
- RTD 配套页: `docs/source/paper-notes/ref-tang2025-JBE.rst`
- 封面简报: `wechat/articles/review/ref-tang2025-JBE.cover-brief.md`
- 微信草稿作者字段: `Tang Ao`

## RTD 转换记录

- 内容母版: `wechat/articles/draft-public-safe/ref-tang2025-JBE.md`
- 正式转换命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-tang2025-JBE`
- 同步检查命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-tang2025-JBE --check`
- RTD 顶部封面: `wechat/assets/public-safe/ref-tang2025-JBE/cover-wechat-900x383-v2.png`
- 转换规则: 正文措辞、正文图片、公式语义和延伸阅读链接来自 Markdown；封面图等平台字段留给 review note 或后续发布记录。微信底部 `content_source_url` 默认使用当前论文 RTD 解读页（`https://woeai.readthedocs.io/zh-cn/latest/paper-notes/ref-tang2025-JBE.html`）。
- 导航状态: 已由 controller/final integration task 挂入 `docs/source/Research.rst` 和首页最新学术进展。

## 微信草稿箱记录

- 草稿状态: updated via official WeChat draft API, pending WeChat backend preview
- 草稿 media_id: `OW4ZgzIulHGwsx2YUygitzV-5rs25MciHekeZ4Rfet5yiGHDm5jr6R6ne4pgKe5n`
- 更新时间: `2026-06-10T21:14:39+08:00`
- 更新说明: 使用 `academic-clean` 主题和 `mathjax-svg` 公式渲染路线重新提交，封面使用 v2 短文字封面。
- 发布状态: not published; final publication remains manual in the WeChat backend

## 证据来源

- DOI: https://doi.org/10.1016/j.jobe.2025.112131
- Zotero: `4BCF65NB`
- PDF attachment key: `G2D6USRE`
- 摘要来源: Zotero Local API `abstractNote` and PDF abstract; 中文摘要为英文原摘要的忠实翻译，公众号正文与 RTD 页不再保留英文原摘要（2026-06-11 规则更新）。
- PDF / 作者稿: local Zotero imported PDF attachment exists; PDF body and embedded images were used for article evidence and body figures.
- 公开网站记录: `docs/source/Publications.rst` contains `ref-tang2025-JBE` as paper `[63]`; `docs/source/StructuralWindEngineering.rst` lists it under `高层建筑抗风与优化`.

## 源文件获取记录

- Zotero key: `4BCF65NB`
- Zotero 元数据: checked via Zotero Desktop Local API artifact
- Zotero 附件记录: checked via Zotero Desktop Local API artifact; PDF attachment and HTML attachment records exist
- 本地 PDF 附件: exists
- PDF 附件候选: single PDF-like attachment in checked child records
- PDF 选择优先级: author manuscript > publisher version of record > OA platform PDF > preprint > other
- 已选 PDF 类型: Zotero local imported PDF attachment, treated as the usable paper PDF for this WOEAI/user-authored article
- 低优先级选择原因: not applicable; no web, preprint, or lower-priority substitute source was used
- PDF 来源类型: Zotero local attachment
- PDF 私有存放: Zotero private attachment and ignored local working artifacts under `wechat/.local/ref-tang2025-JBE/`
- Zotero Web API `/file`: not needed
- 网页 PDF 下载: not used
- 网页 PDF 批准记录: not applicable
- 摘要依据: Zotero `abstractNote` and PDF abstract on PDF file page 1
- 正文证据依据: PDF body, Zotero metadata, and public WOEAI publication record
- 图片依据: PDF embedded figures extracted from the local paper PDF and copied into public-safe body JPG assets
- 私有信息边界: no absolute private file path, credential, cookie, raw API payload, raw downloaded PDF content, or private preview URL is recorded here

## 关键事实证据定位记录

- 摘要:
  - 文章使用: 中文摘要忠实翻译英文摘要，不附英文原摘要。
  - 证据位置: Zotero `abstractNote`; PDF file page 1 abstract.
- 核心结论: 本文提出高层建筑结构响应预测的 GNN 训练与应用框架，以结构图表示节点、构件和楼层连接关系，并把风荷载信息纳入节点特征。
  - 证据位置: PDF file page 3, Section 2.1, Fig. 1, Eq. (2).
- 核心结论: 参数化建模、自动分析程序、有限元分析和 PyTorch Geometric 数据转换共同生成结构图数据集；初始高层数据通过不同基本风压扩展到 `2994` 组，并结合超高层数据形成 `4194` 个结构数据集。
  - 证据位置: PDF file pages 5-6, Sections 2.2.2-2.2.3, Figs. 3-5.
- 核心结论: TBGNN 包含编码器、消息传递层、楼层特征融合层和解码器；楼层特征融合提高验证集结构响应预测表现。
  - 证据位置: PDF file pages 8-11, Sections 2.3.1-3.1, Figs. 6-9, Table 6.
- 核心结论: 加入楼层特征融合后，TBGNN 在验证集上的准确率由约 `84%` 提高到约 `92%`。
  - 证据位置: PDF file page 11, Section 3.1, Table 6.
- 核心结论: 楼层数是影响模型外推表现的重要因素；当楼层数超出训练数据范围时，预测误差随超出程度增加。
  - 证据位置: PDF file pages 12-13, Section 3.3, Figs. 12-15.
- 核心结论: TBGNN 对不同基本风压下的结构响应变化具有敏感性。
  - 证据位置: PDF file page 14, Section 3.4, Fig. 16.
- 核心结论: TBGNN-TL 在 CAARC 标准高层建筑不同构件尺寸情景下验证；迁移学习改善测试集响应预测表现，并能跟踪构件尺寸变化。
  - 证据位置: PDF file pages 15-17, Sections 4.1-4.2, Table 7, Figs. 17-19.
- 核心结论: 在论文测试环境下，人工修改模型加 FEA、参数化修改模型加 FEA、参数化修改模型加 TBGNN 的单次总时间约为 `3min13s`、`1min40s` 和 `17.33s`，论文据此报告约 `90%` 时间节约。
  - 证据位置: PDF file page 17, Section 4.3, Table 8.
- 核心结论: 当前框架聚焦钢筋混凝土框架结构静力响应；剪力墙、框架-核心筒、墙单元和动态荷载需要后续扩展或结合时序模型。
  - 证据位置: PDF file page 18, Section 5.
- 关键图:
  - Fig. 1 `Structural graph of building structural model (Different colors indicate various standard floors)`: PDF file page 3; used as article Figure 1; asset `wechat/assets/public-safe/ref-tang2025-JBE/fig-01-structural-graph.jpg`.
  - Fig. 4 `Data generation`: PDF file page 6; used as article Figure 4; asset `wechat/assets/public-safe/ref-tang2025-JBE/fig-04-data-generation.jpg`.
  - Fig. 6 `TBGNN architecture`: PDF file page 8; used as article Figure 6; asset `wechat/assets/public-safe/ref-tang2025-JBE/fig-06-tbgnn-architecture.jpg`.
  - Fig. 8 `Transfer learning for super-tall building`: PDF file page 9; used as article Figure 8; asset `wechat/assets/public-safe/ref-tang2025-JBE/fig-08-transfer-learning.jpg`.
  - Fig. 9 `Regression performance on the validation set`: PDF file page 11; used as article Figure 9; asset `wechat/assets/public-safe/ref-tang2025-JBE/fig-09-regression-performance.jpg`.
  - Fig. 16 `Displacements and inter-story drifts under various basic wind pressures`: PDF file page 14; used as article Figure 16; asset `wechat/assets/public-safe/ref-tang2025-JBE/fig-16-wind-pressure-sensitivity.jpg`.
  - Fig. 19 `Comparison of predicted and true values for different sections of CAARC building`: PDF file page 17; used as article Figure 19; asset `wechat/assets/public-safe/ref-tang2025-JBE/fig-19-caarc-comparison.jpg`.
- 关键公式:
  - 文章使用: $G=(V,E,F)$ as graph representation of tall-building structures.
  - 证据位置: PDF file page 3, Section 2.1, Fig. 1; not a numbered equation in the paper body.
  - 文章使用: $w_k=\beta_z \mu_s \mu_z w_0$ as floor wind-load calculation used in node features.
  - 证据位置: PDF file page 3, Section 2.1, Eq. (2).
  - 文章使用: $\Delta_{wx}$, $\Delta_{wy}$, $\delta_{wx}$, $\delta_{wy}$, and $n_1$ as model target outputs.
  - 证据位置: PDF file page 10, Table 5.
  - 文章使用: $182.88\,\mathrm{m} \times 45.72\,\mathrm{m} \times 30.48\,\mathrm{m}$ for CAARC dimensions and inline time quantities from Table 8.
  - 证据位置: PDF file page 15, Section 4.2; PDF file page 17, Table 8.
- 页码口径: evidence locations use PDF file page numbers, not journal printed page numbers or article pagination.

## 图片使用记录

1. 图 1: 建筑结构模型的结构图表示（不同颜色表示不同标准层）
   - 用途: 开篇方法图
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-tang2025-JBE/fig-01-structural-graph.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 论文图 1 建筑结构模型的结构图表示（不同颜色表示不同标准层）
   - 公众号说明: 展示节点、边和楼层关系如何组成结构图。
   - 移动端预览: pending WeChat backend mobile preview
2. 图 4: 数据生成
   - 用途: 方法流程说明
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-tang2025-JBE/fig-04-data-generation.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 论文图 4 数据生成
   - 公众号说明: 展示参数化建模、有限元分析和结构图数据集转换流程。
   - 移动端预览: pending WeChat backend mobile preview
3. 图 6: TBGNN 架构
   - 用途: 模型结构说明
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-tang2025-JBE/fig-06-tbgnn-architecture.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 论文图 6 TBGNN 架构
   - 公众号说明: 展示编码器、消息传递、楼层特征融合和解码器之间的关系。
   - 移动端预览: pending WeChat backend mobile preview
4. 图 8: 面向超高层建筑的迁移学习
   - 用途: 说明 TBGNN-TL 扩展路径
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-tang2025-JBE/fig-08-transfer-learning.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 论文图 8 面向超高层建筑的迁移学习
   - 公众号说明: 展示由高层数据预训练参数迁移到超高层结构数据训练的过程。
   - 移动端预览: pending WeChat backend mobile preview
5. 图 9: 验证集回归性能
   - 用途: 性能对比证据
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-tang2025-JBE/fig-09-regression-performance.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 论文图 9 验证集回归性能
   - 公众号说明: 对比加入楼层特征融合前后的多种 GNN 模型预测散点。
   - 移动端预览: pending WeChat backend mobile preview
6. 图 16: 不同基本风压下的位移和层间位移
   - 用途: 风荷载敏感性证据
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-tang2025-JBE/fig-16-wind-pressure-sensitivity.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 论文图 16 不同基本风压下的位移和层间位移
   - 公众号说明: 展示模型对不同基本风压输入的响应预测。
   - 移动端预览: pending WeChat backend mobile preview
7. 图 19: CAARC 建筑不同截面工况下预测值与真实值对比
   - 用途: CAARC 验证证据
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-tang2025-JBE/fig-19-caarc-comparison.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 论文图 19 CAARC 建筑不同截面工况下预测值与真实值对比
   - 公众号说明: 展示同一拓扑下不同构件尺寸情景的层间位移预测。
   - 移动端预览: pending WeChat backend mobile preview

## 公式检查

- 使用公式: yes; two short display formulas and several inline mathematical variables/quantities
- 呈现方式: Markdown LaTeX source; default WeChat API rendering is MathJax SVG with `data-formula` metadata
- 微信公式渲染路线: `mathjax-svg` unless a fallback reason is recorded
- RTD 呈现方式: Sphinx math roles/directives generated by `wechat/tools/markdown_to_rtd.py`
- 行内变量/量纲: formula markup applied to $V$, $E$, $F$, $w_k$, $\beta_z$, $\mu_s$, $\mu_z$, $w_0$, $\Delta_{wx}$, $\Delta_{wy}$, $\delta_{wx}$, $\delta_{wy}$, $n_1$, percentages, dimensions, and time quantities
- 移动端预览: pending WeChat backend mobile preview

## 封面图

- 封面状态: selected v2 cover from upgraded batch cover workflow, pending WeChat backend preview
- 封面简报: `wechat/articles/review/ref-tang2025-JBE.cover-brief.md`
- 封面素材: `wechat/assets/public-safe/ref-tang2025-JBE/cover-wechat-900x383-v2.png`
- 尺寸: `900 x 383 px`
- 生成方式: image-gen public-safe candidate selected after upgraded batch `wechat-cover` comparison
- 设计方向: tall-building structural frame under wind-response curves, graph nodes and edges, and GNN surrogate-model cue
- 文字策略: short embedded Chinese hook; category tag `结构抗风`; hook `高层响应快速预测`
- 源候选图: `wechat/.local/cover-candidates/batch-2026-06-10/ref-tang2025-JBE-v2-imagegen.png`
- 本地裁剪预览: `wechat/.local/cover-previews/batch-2026-06-10-v2-quality-board.html`
- 批量候选联系表: `wechat/.local/cover-candidates/batch-2026-06-10/contact-sheet-v2.png`
- 裁剪预览结果: passed local ratio, file-size, small-thumbnail, and text-quality checks (`900 x 383 px`, ratio delta `0.0`)
- 微信后台预览: pending WeChat backend mobile preview

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
- [x] 用 Zotero/PDF 摘要核对中文摘要，并按 2026-06-11 规则移除英文原摘要。
- [x] 从 PDF 抽取并导入可用正文图。
- [x] 由公众号正文转换生成 RTD 配套页，保持标题、正文、图片、DOI 和延伸阅读链接一致。
- [x] 由 controller/final integration task 将 RTD 配套页挂入相关科研方向页的 `学术进展 Academic Progress`。
- [x] 生成最终封面图。
- [x] 运行本地封面裁剪预览。
- [ ] 公众号后台手机预览正文、公式和图片。
- [ ] 发布后回填 `latest_published_url` 和 `wechat_status`。

## 表达修订记录

- 2026-06-11: 按新表达规范完成批量修订——补入`三句话导读`和关键数字卡；删除英文摘要段，仅保留中文摘要；`研究问题`编号化；`关键发现`各小节首句回扣编号问题且加粗一句结论；图注改为`论文图 N`格式；`延伸阅读`前加入固定结尾块。开头策略：具体数字式。关键卡证据：数据集规模、准确率提升、楼层数外推和 90% 时间节约均已在关键事实证据定位记录中标到 PDF file pages 8-18 及 Figs. 9、16、19。

## 检查记录

- figure extraction: copied selected local extracted PDF embedded JPG images to public-safe asset names
- cover-v2 generation: selected `wechat/assets/public-safe/ref-tang2025-JBE/cover-wechat-900x383-v2.png` from upgraded batch `wechat-cover` image-gen workflow
- cover-v2 preview: passed (`python3 .agents/skills/wechat-cover/scripts/cover_preview.py -o wechat/.local/cover-previews/batch-2026-06-10-v2-quality-board.html ...`)
- cover generation: generated `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-v1.png)` with local Python standard-library raster generator
- cover-preview: passed (`python .agents/skills/wechat-cover/scripts/cover_preview.py -o wechat/.local/cover-previews/ref-tang2025-JBE.cover-preview.html removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-v1.png)`)
- rtd-generation: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-tang2025-JBE`)
- rtd-sync-check: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-tang2025-JBE --check`)
- wechat-preflight: passed (`python3 wechat/tools/wechat_draft.py preflight --publication-ref ref-tang2025-JBE --theme academic-clean`)
- wechat-dry-run: passed (`python3 wechat/tools/wechat_draft.py dry-run --publication-ref ref-tang2025-JBE --theme academic-clean`)
- public-safety: passed (`python3 scripts/check-public-safe-content.py`)
- docs-check: passed (`./scripts/check-docs.sh`) after final batch navigation integration.
- whitespace: passed (`git diff --check -- ...` plus no-index whitespace check for the new Markdown/RST files)
