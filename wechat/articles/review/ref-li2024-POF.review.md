---
publication_ref: ref-li2024-POF
zotero_key: 2YG78T62
doi: 10.1063/5.0194006
research_family: 建筑结构抗风
subdirection: 数值风洞与湍动入流
publication_mode: first_publish
wechat_status: ready_to_publish
wechat_author: Li Chao
source_checked: true
abstract_checked: true
copyright_checked: true
public_safety_checked: true
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
body_images_upload_approved: true
rtd_page_checked: true
rtd_cover_image: wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v2.png
---

# ref-li2024-POF 发布说明

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/ref-li2024-POF.md`
- RTD 配套页: `docs/source/paper-notes/ref-li2024-POF.rst`
- 微信草稿作者字段: `Li Chao`

## RTD 转换记录

- 内容母版: `wechat/articles/draft-public-safe/ref-li2024-POF.md`
- 正式转换命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-li2024-POF`
- 同步检查命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-li2024-POF --check`
- RTD 顶部封面: `wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v2.png`
- 转换规则: 正文措辞、公式、正文图片和延伸阅读链接来自 Markdown；封面图等平台字段来自 review note 或后续 cover integration。微信底部“阅读原文”默认使用当前论文 RTD 解读页（`https://woeai.readthedocs.io/zh-cn/latest/paper-notes/ref-li2024-POF.html`）；只有人工明确指定其他目标或留空时才写入 front matter 覆盖默认值。

## 微信草稿箱记录

- 草稿状态: updated via official WeChat draft API, pending WeChat backend preview
- 草稿 media_id: `OW4ZgzIulHGwsx2YUygitxOm-FaRJOc1RnchrVP-Vi-lmkVFUH1xSKpmSCuw4SG7`
- 更新时间: `2026-06-10T21:14:49+08:00`
- 更新说明: 使用 `academic-clean` 主题和 `mathjax-svg` 公式渲染路线重新提交，封面使用 v2 短文字封面。
- 发布状态: not published; final publication remains manual in the WeChat backend

## 证据来源

- DOI: https://doi.org/10.1063/5.0194006
- Zotero: `2YG78T62`
- 摘要来源: Zotero Desktop Local API `abstractNote` and PDF abstract; 中文摘要为英文原摘要的忠实翻译，公众号正文同时保留英文原摘要。
- PDF / 作者稿: Zotero attachment key `RIVR33QT`; attachment record mode is `imported_url`, but a local PDF exists in Zotero private storage and was used as the evidence source for body claims and figure extraction.
- WOEAI 网站记录: `docs/source/Publications.rst` anchor `ref-li2024-POF`; research placement checked against `docs/source/BuildingStructuralWindResistance.rst`.

## 源文件获取记录

- Zotero key: `2YG78T62`
- Zotero 元数据: checked via Zotero Desktop Local API / local controller export
- Zotero 附件记录: checked via Zotero Desktop Local API / local controller export; PDF attachment key `RIVR33QT`, content type `application/pdf`, link mode `imported_url`
- 本地 PDF 附件: exists
- PDF 附件候选: single PDF-like attachment plus an HTML attachment record
- PDF 选择优先级: author manuscript > publisher version of record > OA platform PDF > preprint > other
- 已选 PDF 类型: Zotero local paper PDF resolved from the `imported_url` attachment record; treated as the available publisher/version-of-record evidence source for this article
- 低优先级选择原因: no web, preprint, or lower-priority source was used; the important nuance is attachment mode `imported_url` while the local PDF file exists
- PDF 来源类型: Zotero local attachment; no web PDF download used
- PDF 私有存放: Zotero private attachment plus ignored local extraction artifacts under `wechat/.local/ref-li2024-POF/`; no PDF committed to this public repository
- Zotero Web API `/file`: not needed and not attempted because the local PDF exists
- 网页 PDF 下载: not used
- 网页 PDF 批准记录: not applicable
- 摘要依据: Zotero `abstractNote` and PDF abstract on `PDF file page 2`
- 正文证据依据: PDF body text and local PDF page renders
- 图片依据: PDF embedded images and page-render crop from the local PDF
- 私有信息边界: no absolute private file path, credential, cookie, raw API payload, or downloaded PDF content is recorded here

## 关键事实证据定位记录

- 摘要:
  - 文章使用: 中文摘要为英文原摘要的忠实翻译，并附英文原摘要。
  - 证据位置: Zotero Desktop Local API `abstractNote`; PDF abstract on `PDF file page 2`.
- 核心结论: VPRFG 先生成矢量势场，再由旋度生成脉动速度场，使均匀各向同性湍流满足无散条件。
  - 证据位置: `PDF file page 5`, Section II.B, Eqs. (15)-(17); conclusion restatement on `PDF file page 11`.
- 核心结论: 方法显式引入三维空间互谱密度和 Taylor 冻结假设，使生成湍流能够联系能谱、一维空间 PSD、时间 PSD、空间相干函数、湍动能和 Reynolds 应力。
  - 证据位置: `PDF file page 4`, Section II.A; `PDF file page 6`, Section II.C; `PDF file page 8`, Section II.D-E; conclusion on `PDF file page 12`.
- 核心结论: 以 von Karman 能谱为目标的数值算例显示，生成能谱整体贴近目标曲线，较高网格分辨率覆盖更宽波数范围。
  - 证据位置: `PDF file page 9`, Section III.A and Fig. 4.
- 核心结论: 衰减盒湍流 LES 与 Comte-Bellot and Corrsin 实验数据对比显示，采用 Eq. (17) 生成的流场在湍动能衰减、三维能谱和空间相关系数上具有较高一致性。
  - 证据位置: `PDF file page 11` through `PDF file page 13`, Section III.B, Figs. 7-11, conclusion text.
- 核心结论: 当前研究范围限定在均匀各向同性湍流，任意非均匀各向异性三维空间互谱密度构造仍需后续研究。
  - 证据位置: `PDF file page 13` and `PDF file page 14`, conclusion limitation paragraph.
- 关键图:
  - Fig. 3 `Flowchart of the VPRFG method`: `PDF file page 8`; used as article Figure 3.
  - Fig. 4 `Energy spectra of generated turbulence using the von Karman energy spectrum as target`: `PDF file page 9`; used as article Figure 4.
  - Fig. 7 `Iso-surfaces of the Q-criterion for different grids at the initial moment of U0 t/M = 42`: `PDF file page 12`; used as article Figure 7.
  - Fig. 9 `Energy spectra for decaying box turbulence`: `PDF file page 13`; used as article Figure 9.
- 关键公式:
  - Paper Eq. (15), `\mathbf{u}=\nabla\times\boldsymbol{\psi}`: `PDF file page 5`; used in article as the core vector-potential construction.
  - Paper Eq. (16), vector potential random summation: `PDF file page 5`; used in article with equivalent vector notation.
  - Paper Eq. (17), component-wise velocity generated from the vector potential field: `PDF file page 5`; summarized in the article as the implementation form behind the vector notation.
  - Paper Eq. (27), divergence-free proof: `PDF file page 6`; used in article as a display formula.
  - Paper Eq. (29), Taylor frozen-hypothesis transport relation: `PDF file page 6`; used in article as a display formula.
  - Paper Eq. (47), generated energy spectrum approaches the target spectrum: `PDF file page 8`; used in article as a display formula.
  - Paper Eq. (48), turbulent kinetic energy equals the integral/area of the spectrum: `PDF file page 8`; used in article as a display formula.
  - Editorial explanatory formulas: none; article formulas are paper-derived or equivalent vector notation for paper equations.
- 页码口径: PDF file page numbers are used, not journal printed page numbers or article pagination.
- 页码审计依据: local ignored PDF page renders and `paper.txt` extraction under the paper's `.local` workspace were used only for evidence-location audit; no absolute private source PDF path is recorded.

## 图片使用记录

1. 图 3: VPRFG 方法流程图
   - 用途: 方法流程说明
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-li2024-POF/fig3-vprfg-flowchart.png`
   - 来源/版权: paper PDF page-render crop; author/user paper scope treated as usable for this WOEAI article
   - 抽取方式: crop from `PDF file page 8` rendered page image because the flowchart is vector/page content rather than a clean standalone embedded raster
   - 公众号图名: 图 3 VPRFG 方法流程图
   - 公众号说明: 方法从目标平均速度、目标能谱、计算域和网格参数出发，生成波数、幅值、频率和相位，最后由矢量势场旋度得到脉动速度场。
   - 移动端预览: pending WeChat backend mobile preview
2. 图 4: 以 von Karman 能谱为目标生成湍流的能谱
   - 用途: 说明目标能谱满足能力
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-li2024-POF/fig4-von-karman-energy-spectrum.jpg`
   - 来源/版权: paper PDF embedded image; author/user paper scope treated as usable for this WOEAI article
   - 抽取方式: `pdfimages` embedded raster from `PDF file page 9`
   - 公众号图名: 图 4 以 von Karman 能谱为目标生成湍流的能谱
   - 公众号说明: 不同网格分辨率下生成能谱整体贴近目标曲线，高分辨率网格覆盖更宽波数范围。
   - 移动端预览: pending WeChat backend mobile preview
3. 图 7: 初始时刻不同网格的 Q 准则等值面
   - 用途: 展示生成湍流的三维涡结构
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-li2024-POF/fig7-q-criterion-isosurfaces.jpg`
   - 来源/版权: paper PDF embedded image; author/user paper scope treated as usable for this WOEAI article
   - 抽取方式: `pdfimages` embedded raster from `PDF file page 12`, resized to mobile/repo-friendly public asset
   - 公众号图名: 图 7 初始时刻不同网格的 Q 准则等值面
   - 公众号说明: Q 准则等值面展示生成湍流中的涡结构；网格分辨率提高后，小尺度结构更加丰富。
   - 移动端预览: pending WeChat backend mobile preview
4. 图 9: 衰减盒湍流能谱
   - 用途: 展示 LES 衰减盒湍流验证
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-li2024-POF/fig9-decaying-box-energy-spectra.jpg`
   - 来源/版权: paper PDF embedded image; author/user paper scope treated as usable for this WOEAI article
   - 抽取方式: `pdfimages` embedded raster from `PDF file page 13`
   - 公众号图名: 图 9 衰减盒湍流能谱
   - 公众号说明: 衰减盒湍流算例把 VPRFG 生成的初始场放入 LES 中检验，能谱随时间演化并与实验数据保持较好一致。
   - 移动端预览: pending WeChat backend mobile preview

## 公式检查

- 使用公式: yes
- 呈现方式: Markdown LaTeX formula embedded in the relevant narrative sections; default API renderer is `mathjax-svg` with source `data-formula` metadata, with `lightweight` HTML kept only as fallback
- 微信公式渲染路线: `mathjax-svg`; this article still needs final WeChat backend mobile preview before publication
- RTD 呈现方式: Sphinx MathJax through `.. math::` and `:math:` generated by `wechat/tools/markdown_to_rtd.py`
- 行内变量/量纲: formula markup applied to vector quantities, divergence-free condition, target/calculated spectra, wave numbers, grid sizes, and nondimensional validation times
- 文字性下标: use explicit roman text such as `\mathrm{avg}`, `\mathrm{C}`, and `\mathrm{T}` where abbreviations or word-like subscripts appear
- 固定公式小节: not used; formulas appear in `方法贡献` and `关键发现`
- 移动端预览: pending WeChat backend mobile preview

## 封面图

- 封面状态: selected v2 cover from upgraded batch cover workflow, pending WeChat backend preview
- 封面素材: `wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v2.png`
- 尺寸: `900 x 383 px`
- 生成方式: image-gen public-safe candidate selected after upgraded batch `wechat-cover` comparison
- 设计意图: 用入口边界、三维湍流涡结构和矢量势到无散湍流的抽象机制表达“VPRFG + 数值风洞入流控制”。
- 文字策略: short embedded Chinese hook; category tag `数值风洞`; hook `让湍流天然无散`
- 源候选图: `wechat/.local/cover-candidates/batch-2026-06-10/ref-li2024-POF-v2-imagegen.png`
- 本地裁剪预览: `wechat/.local/cover-previews/batch-2026-06-10-v2-quality-board.html`
- 批量候选联系表: `wechat/.local/cover-candidates/batch-2026-06-10/contact-sheet-v2.png`
- 裁剪预览结果: passed local ratio, file-size, small-thumbnail, and text-quality checks (`900 x 383 px`, ratio delta `0.0`)
- 微信后台预览: pending WeChat backend mobile preview

## 公开安全

- [x] No WeChat AppSecret, token, cookie, or credential appears.
- [x] No Zotero API key appears.
- [x] No private partner name appears.
- [x] No unconfirmed project status appears.
- [x] Reader-facing Markdown has no production notes, pending placeholders, or private paths.
- [x] Reader-facing Markdown uses direct Markdown hyperlinks under `延伸阅读`.
- [x] Figure captions use a Chinese figure-title line translated from the paper title plus a separate Chinese explanatory line.
- [x] The imported-url/local-PDF nuance is recorded without exposing absolute private paths.

## 发布前任务

- [x] 用 Zotero/local artifacts 核对作者、期刊、年份、DOI、摘要和附件记录。
- [x] 使用本地 PDF 证据审计正文、关键图和关键公式。
- [x] 导入已确认可用的正文图。
- [x] 由公众号正文转换生成 RTD 配套页，保持标题、正文、图片、公式、DOI 和延伸阅读链接一致。
- [x] 生成并本地审核公众号封面图。
- [x] 将 RTD 配套页挂入相关科研方向页的 `学术进展 Academic Progress`，归入 `建筑结构抗风 / 数值风洞与湍动入流`。
- [ ] 公众号后台手机预览正文、公式和图片。
- [ ] 发布后回填 `latest_published_url` 和 `wechat_status`。

## 检查记录

- cover-v2 generation: selected `wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v2.png` from upgraded batch `wechat-cover` image-gen workflow
- cover-v2 preview: passed (`python3 .agents/skills/wechat-cover/scripts/cover_preview.py -o wechat/.local/cover-previews/batch-2026-06-10-v2-quality-board.html ...`)
- RTD generate: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-li2024-POF`)
- RTD sync check: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-li2024-POF --check`)
- public-safety: passed (`python3 scripts/check-public-safe-content.py`)
- markdown whitespace: passed (`git diff --check -- wechat/articles/draft-public-safe/ref-li2024-POF.md wechat/articles/review/ref-li2024-POF.review.md wechat/articles/review/ref-li2024-POF.cover-brief.md docs/source/paper-notes/ref-li2024-POF.rst wechat/assets/public-safe/ref-li2024-POF`)
