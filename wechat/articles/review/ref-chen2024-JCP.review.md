---
publication_ref: ref-chen2024-JCP
zotero_key: Y76UWP9R
doi: 10.1016/j.jcp.2023.112706
research_family: 建筑结构抗风
subdirection: 数值风洞与湍动入流
publication_mode: first_publish
wechat_status: ready_to_publish
wechat_draft_media_id: OW4ZgzIulHGwsx2YUygit8jZYVoX9eNK1vrIQKOcGi8CkjVV77kRKQEP6OlmtkpH
wechat_draft_created_at: 2026-06-10T20:04:58+08:00
wechat_draft_updated_at: 2026-06-10T20:04:58+08:00
wechat_author: Chen Lingwei
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

# ref-chen2024-JCP 发布说明

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/ref-chen2024-JCP.md`
- RTD 配套页: `docs/source/paper-notes/ref-chen2024-JCP.rst`
- 微信草稿作者字段: `Chen Lingwei`

## RTD 转换记录

- 内容母版: `wechat/articles/draft-public-safe/ref-chen2024-JCP.md`
- 正式转换命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-chen2024-JCP`
- 同步检查命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-chen2024-JCP --check`
- RTD 顶部封面: not set for this package; body figures are inserted in the article flow
- 转换规则: 正文措辞、正文图片、公式语义和延伸阅读链接来自 Markdown；平台字段来自 review note。微信底部 `content_source_url` 默认使用当前论文 RTD 解读页（`https://woeai.readthedocs.io/zh-cn/latest/paper-notes/ref-chen2024-JCP.html`）。
- 导航状态: shared integration files were intentionally not modified in this worker task. Existing public record already contains `ref-chen2024-JCP` in `docs/source/Publications.rst`, `docs/source/PublicationsByResearch.rst`, `docs/data/publication-research-map.json`, and the building structural wind direction page.

## 证据来源

- DOI: https://doi.org/10.1016/j.jcp.2023.112706
- Zotero: `Y76UWP9R`
- PDF attachment key: `XQVFX5D7`
- 摘要来源: Zotero Desktop Local API `abstractNote` and PDF abstract; 中文摘要为英文原摘要的忠实翻译，公众号正文同时保留英文原摘要。
- PDF / 作者稿: Zotero local imported PDF attachment exists; the selected local publisher-record PDF was used for article evidence and body figures.
- 公开网站记录: `docs/source/Publications.rst` contains `ref-chen2024-JCP` as paper `[50]`; `docs/source/PublicationsByResearch.rst` maps it under `建筑结构抗风 / 数值风洞与湍动入流`; `docs/source/BuildingStructuralWindResistance.rst` lists it under `数值风洞与湍动入流`.

## 源文件获取记录

- Zotero key: `Y76UWP9R`
- Zotero 元数据: checked via Zotero Desktop Local API
- Zotero 附件记录: checked via Zotero Desktop Local API; one PDF attachment record and one HTML attachment record exist
- 本地 PDF 附件: exists
- PDF 附件候选: one PDF-like Zotero local imported attachment, key `XQVFX5D7`, content type `application/pdf`, link mode `imported_file`
- PDF 选择优先级: author manuscript > publisher version of record > OA platform PDF > preprint > other
- 已选 PDF 类型: Zotero local imported publisher-record PDF, treated as the usable paper PDF for this WOEAI/user-authored article
- 低优先级选择原因: not applicable; no web, preprint, or lower-priority substitute source was used
- PDF 来源类型: Zotero local attachment
- PDF 私有存放: Zotero private attachment and ignored local working artifacts under `wechat/.local/ref-chen2024-JCP/`
- Zotero Web API `/file`: not needed
- 网页 PDF 下载: not used
- 网页 PDF 批准记录: not applicable
- 摘要依据: Zotero `abstractNote` and PDF abstract on PDF file page 1
- 正文证据依据: PDF body, Zotero metadata, and public WOEAI publication record
- 图片依据: PDF embedded figures extracted from the local paper PDF and copied into public-safe body PNG assets
- 私有信息边界: no absolute private file path, credential, cookie, raw API payload, raw downloaded PDF content, or private preview URL is recorded here

## 关键事实证据定位记录

- 摘要:
  - 文章使用: 中文摘要忠实翻译英文摘要，并附英文原摘要。
  - 证据位置: Zotero `abstractNote`; PDF file page 1 abstract.
- 核心结论: 论文提出 coherence-improved and mass-balanced random flow generation (CMRFG) 方法，用于 LES 入口湍流生成。
  - 证据位置: PDF file page 1 abstract; PDF file pages 11-15, Section 3.2.
- 核心结论: 单波传输分析显示，同时满足无散度条件、Taylor 冻结假设和入口质量平衡条件时，生成流场可避免非物理压力波动并在中心区域自持发展。
  - 证据位置: PDF file pages 4-9, Section 2; PDF file page 29, Section 6.
- 核心结论: 入口质量不平衡时，入口附近最大压力波动可达到动压的 `0.84` 倍，`X=2 m` 处人工压力波动仍可达到约 `15%` 动压。
  - 证据位置: PDF file pages 7-8, Section 2.3.2, Fig. 4.
- 核心结论: CMRFG 通过目标空间相干函数确定 $k_{2,n}$ 的概率密度，并通过波数周期修正满足入口质量平衡。
  - 证据位置: PDF file pages 11-15, Section 3.2, Fig. 7, Eqs. (48)-(55).
- 核心结论: 与 CIRFG 相比，CMRFG 生成的 Y 方向空间相干函数在不同空间间距下更接近目标值。
  - 证据位置: PDF file page 21, Section 4.4, Fig. 17.
- 核心结论: 各向异性湍流 LES 中，带质量平衡修正的 HA1 算例入口质量通量保持为 `1`，未修正 HA2 算例随时间波动；HA2 在 `x/M=30` 位置非期望压力波动约为 `12%` 动压，HA1 中心感兴趣区域脉动压力系数约为 `1.5%`。
  - 证据位置: PDF file pages 25-27, Section 5.2.3, Figs. 27-29.
- 核心结论: CMRFG 生成的各向异性湍流涡结构具有随机性并沿流向逐步衰减，速度标准差、湍流动能和空间谱总体与实验目标一致。
  - 证据位置: PDF file pages 26-29, Sections 5.2.4 and 6, Figs. 30-35.
- 核心边界: 论文聚焦均匀湍流；CMRFG 可扩展到非均匀湍流，但更真实的非均匀湍流空间相干函数确定仍需后续研究。
  - 证据位置: PDF file page 29, Section 6 final paragraph.
- 核心边界: 各向异性算例仍存在入口与侧边界交界处的局部非物理压力波动，与边界不相容有关。
  - 证据位置: PDF file page 27, Section 5.2.3; PDF file page 29, Section 6.
- 关键图:
  - Fig. 4 `Statistical fluctuations of flow fields for cases SW1 to SW4`: PDF file page 8; used as article Figure 4; asset `wechat/assets/public-safe/ref-chen2024-JCP/fig-04-statistical-flow-fluctuations.png`.
  - Fig. 7 `Flowchart of CMRFG method`: PDF file page 14; used as article Figure 7; asset `wechat/assets/public-safe/ref-chen2024-JCP/fig-07-cmrfg-workflow.png`.
  - Fig. 17 `Comparison of spatial coherence functions in Y-direction at different spatial separations`: PDF file page 21; used as article Figure 17; asset `wechat/assets/public-safe/ref-chen2024-JCP/fig-17-spatial-coherence-validation.png`.
  - Fig. 28 `Contour diagram of fluctuating pressure coefficient distributions`: PDF file page 25; used as article Figure 28; asset `wechat/assets/public-safe/ref-chen2024-JCP/fig-28-pressure-fluctuation-contours.png`.
  - Fig. 30 `Iso-surface of the Q-criterion (Q = 1000) coloured by the magnitude of the instantaneous velocity at the 8 s`: PDF file page 26; used as article Figure 30; asset `wechat/assets/public-safe/ref-chen2024-JCP/fig-30-q-criterion-vortices.png`.
- 关键公式:
  - 文章使用: editorial explanatory formula `\int_S u_1'(t)\,\mathrm{d}S = 0`, summarizing the inlet mass-balanced condition in Section 2.2.1.
  - 证据位置: PDF file page 5, Section 2.2.1, Eq. (8).
  - 文章使用: inline variables and quantities including `$k_{2,n}$`, `$S$`, `$u_1'$`, `$X=2\,\mathrm{m}$`, `$x/M=30$`, `$5.12\,\mathrm{m} \times 5.12\,\mathrm{m} \times 2.56\,\mathrm{m}$`, `$8\,\mathrm{s}$`.
  - 证据位置: PDF file pages 5, 7-8, 11-15, and 25-28.
- 页码口径: evidence locations use PDF file page numbers, not journal printed page numbers or article pagination.

## 图片使用记录

1. 图 7: CMRFG 方法流程
   - 用途: 开篇说明方法生成流程
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-chen2024-JCP/fig-07-cmrfg-workflow.png`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 图像复核: visually verified against PDF file page 14 / Fig. 7 and local extracted image inventory; asset is the English CMRFG workflow figure
   - 公众号图名: 图 7 CMRFG 方法流程
   - 公众号说明: 展示 CMRFG 如何从目标谱、相关和相干函数生成质量平衡的入口湍流场。
   - 移动端预览: pending WeChat backend mobile preview
2. 图 4: 不同单波条件下的流场统计波动
   - 用途: 说明入口质量平衡对压力波动的影响
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-chen2024-JCP/fig-04-statistical-flow-fluctuations.png`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 4 不同单波条件下的流场统计波动
   - 公众号说明: 对比质量不平衡、质量通量修正和波数周期修正下的压力与速度统计波动。
   - 移动端预览: pending WeChat backend mobile preview
3. 图 17: 不同空间间距下的 Y 方向空间相干函数对比
   - 用途: 说明 CMRFG 对目标空间相干函数的匹配能力
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-chen2024-JCP/fig-17-spatial-coherence-validation.png`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 17 不同空间间距下的 Y 方向空间相干函数对比
   - 公众号说明: 展示 CMRFG 相比 CIRFG 更接近目标空间相干函数。
   - 移动端预览: pending WeChat backend mobile preview
4. 图 28: 脉动压力系数分布云图
   - 用途: 说明质量平衡修正对各向异性湍流 LES 压力污染的抑制
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-chen2024-JCP/fig-28-pressure-fluctuation-contours.png`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 28 脉动压力系数分布云图
   - 公众号说明: 对比带质量平衡修正与不带修正时计算域中的人工压力波动。
   - 移动端预览: pending WeChat backend mobile preview
5. 图 30: Q 准则等值面显示的瞬时涡结构
   - 用途: 展示 CMRFG 生成湍流在计算域内的空间发展
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-chen2024-JCP/fig-30-q-criterion-vortices.png`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 公众号图名: 图 30 Q 准则等值面显示的瞬时涡结构
   - 公众号说明: 展示随机涡结构随流向发展和衰减。
   - 移动端预览: pending WeChat backend mobile preview

## 公式检查

- 使用公式: yes; one editorial explanatory display formula and inline mathematical quantities
- 呈现方式: Markdown LaTeX source; default WeChat API rendering is MathJax SVG with `data-formula` metadata
- 微信公式渲染路线: `mathjax-svg` unless a fallback reason is recorded
- RTD 呈现方式: Sphinx math roles/directives generated by `wechat/tools/markdown_to_rtd.py`
- 行内变量/量纲: formula markup applied to `$k_{2,n}$`, `$S$`, `$u_1'$`, `$X=2\,\mathrm{m}$`, `$x/M=30$`, `$5.12\,\mathrm{m} \times 5.12\,\mathrm{m} \times 2.56\,\mathrm{m}$`, `$8\,\mathrm{s}$`
- 移动端预览: pending WeChat backend mobile preview

## 封面图

- 封面状态: regenerated with image-gen-text; WeChat draft updated; pending WeChat backend mobile preview
- 候选数量: 3 concept directions documented in `wechat/articles/review/ref-chen2024-JCP.cover-brief.md`; 1 selected image-gen-text cover exported
- 选中候选: `cover-wechat-900x383-imagegen-v1`
- 文字模式: image-gen-text
- 生成工具: Codex image generation tool
- 图像生成场景: LES 入流湍流生成、城市数值风洞、CFD 流线与方法流程
- 要求文字: `数值风洞 / 入流更连贯 / 守恒湍流生成`
- 备用封面: `wechat/assets/public-safe/ref-chen2024-JCP/cover-wechat-900x383-v1.png`
- 封面素材: `wechat/assets/public-safe/ref-chen2024-JCP/cover-wechat-900x383-imagegen-v1.png`
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

- Zotero metadata: passed via Zotero Desktop Local API
- PDF extraction: passed (`pdftotext`, `pdfimages -list`, selected embedded images copied to public-safe assets)
- rtd-generation: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-chen2024-JCP`)
- rtd-sync-check: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-chen2024-JCP --check`)
- public-safety: passed (`python3 scripts/check-public-safe-content.py`)
- whitespace: passed (`git diff --check`)
