---
publication_ref: ref-wang2024-ES
zotero_key: 3HGIR6QR
doi: 10.1016/j.engstruct.2024.118742
research_family: 建筑结构抗风
subdirection: 数值风洞与湍动入流
publication_mode: first_publish
wechat_status: ready_to_publish
wechat_draft_media_id: OW4ZgzIulHGwsx2YUygit-ACT--HuP4rk1XuYJrtqGaEQoGRxYPTqZbfxf59vBFo
wechat_draft_created_at: 2026-06-10T20:06:35+08:00
wechat_draft_updated_at: 2026-06-10T20:06:35+08:00
wechat_author: Wang Jinghan
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

# ref-wang2024-ES 发布说明

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/ref-wang2024-ES.md`
- RTD 配套页: `docs/source/paper-notes/ref-wang2024-ES.rst`
- 微信草稿作者字段: `Wang Jinghan`

## RTD 转换记录

- 内容母版: `wechat/articles/draft-public-safe/ref-wang2024-ES.md`
- 正式转换命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-wang2024-ES`
- 同步检查命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-wang2024-ES --check`
- RTD 顶部封面: not set for this package; body figures are inserted in the article flow
- 转换规则: 正文措辞、正文图片、公式语义和延伸阅读链接来自 Markdown；平台字段来自 review note。微信底部 `content_source_url` 默认使用当前论文 RTD 解读页（`https://woeai.readthedocs.io/zh-cn/latest/paper-notes/ref-wang2024-ES.html`）。
- 导航状态: shared integration files were intentionally not modified in this worker task. Main-thread integration should update `docs/source/Research.rst`, `docs/source/index.rst`, and `wechat/backlog/selected-papers.yml` as needed.

## 证据来源

- DOI: https://doi.org/10.1016/j.engstruct.2024.118742
- Zotero: `3HGIR6QR`
- PDF attachment key: `WAPF8PVL`
- 摘要来源: Zotero Desktop Local API `abstractNote` and PDF abstract; 中文摘要为英文原摘要的忠实翻译，公众号正文与 RTD 页不再保留英文原摘要（2026-06-11 规则更新）。
- PDF / 作者稿: Zotero attachment record is `linkMode=imported_url`, but the selected evidence file was the valid local Zotero storage PDF associated with attachment `WAPF8PVL`; no web PDF download was used.
- 公开网站记录: `docs/source/Publications.rst` contains `ref-wang2024-ES` as paper `[55]`; `docs/source/PublicationsByResearch.rst` maps it under `建筑结构抗风 / 数值风洞与湍动入流`; the assigned worker scope did not modify integration pages.

## 源文件获取记录

- Zotero key: `3HGIR6QR`
- Zotero 元数据: checked via Zotero Desktop Local API
- Zotero 附件记录: checked via Zotero Desktop Local API; one PDF attachment record and one HTML attachment record exist
- PDF 附件候选: PDF child `WAPF8PVL`, content type `application/pdf`, link mode `imported_url`
- 本地 PDF 状态: local Zotero storage PDF exists and was validated with `pdfinfo` as 22 pages; `pdftotext` and `pdfimages` succeeded
- PDF 选择优先级: author manuscript > publisher version of record > OA platform PDF > preprint > other
- 已选 PDF 类型: local Zotero storage PDF associated with the imported-url PDF attachment; treated as the usable publisher-record paper PDF for this WOEAI/user-authored article
- 低优先级选择原因: not applicable; no web, preprint, or lower-priority substitute source was used
- PDF 来源类型: local Zotero storage PDF; attachment record itself is `imported_url`
- PDF 私有存放: Zotero private attachment and ignored local working artifacts under `wechat/.local/ref-wang2024-ES/`
- Zotero Web API `/file`: not needed and not attempted because the local Zotero storage PDF was valid
- 网页 PDF 下载: not used
- 网页 PDF 批准记录: not applicable
- 摘要依据: Zotero `abstractNote` and PDF abstract on PDF file page 1
- 正文证据依据: PDF body, Zotero metadata, and public WOEAI publication record
- 图片依据: PDF embedded figures extracted from the local paper PDF and copied into public-safe body image assets
- 私有信息边界: no absolute private file path, credential, cookie, raw API payload, raw downloaded PDF content, or private preview URL is recorded here

## 关键事实证据定位记录

- 摘要:
  - 文章使用: 中文摘要忠实翻译英文摘要，不附英文原摘要。
  - 证据位置: Zotero `abstractNote`; PDF file page 1 abstract.
- 核心结论: 论文提出 controllable weak recycling (CWR) 方法，将反馈比例控制引入 weak recycling 的重缩放过程，并结合 SECD 模型生成粗糙地表上的湍流 ABL 风场。
  - 证据位置: PDF file page 1 abstract; PDF file page 4 Fig. 3; PDF file page 9 and PDF file page 10, Section 2.2.
- 核心结论: CWR 在本文算例中可简化为仅使用比例项，参数研究中 `K_P=-80.0` 是适当调整；城市地形算例中平均风速和湍流强度整体 MARE 保持在 `10%` 以下。
  - 证据位置: PDF file page 13, Eq. (20); PDF file page 15, Section 3.3.1.
- 核心结论: 在乡村、郊区和城市三类粗糙地形中，CWR 生成的 ABL 风场满足目标平均风速和纵向湍流强度，并沿流向保持自持性。
  - 证据位置: PDF file page 18, Sections 4.1-4.2, Fig. 13.
- 核心结论: 生成风谱与各向异性 von-Kármán 谱总体一致，并在惯性子区呈现 `-5/3` 斜率；高频能量损失与 LES 数值耗散和网格分辨率有关。
  - 证据位置: PDF file page 17 and PDF file page 18, Section 3.3.2 and Section 4.2.
- 核心结论: 将 CWR 提取的风速时程用于高层建筑主域后，平均和脉动风压与 TPU 风洞试验结果总体吻合；迎风面和背风面脉动风压偏差小于 `20%`，侧面最大偏差约 `30%`。
  - 证据位置: PDF file page 20, Section 5.4; PDF file page 19, Fig. 21; PDF file page 21, concluding remark (4).
- 核心边界: SECD 模型会在近地面区域放大湍流强度，阻力系数仍依赖试算；CWR 尚未控制湍流相干性，导致建筑侧面脉动风压仍有较大偏差。
  - 证据位置: PDF file page 21, final limitation paragraph.
- 关键图:
  - Fig. 3 `The schematic use of the CWR method to obtain specified turbulent ABL flows`: PDF file page 4; used as article Figure 3; asset `wechat/assets/public-safe/ref-wang2024-ES/fig-03-cwr-schematic.jpg`.
  - Fig. 13 `Instantaneous vorticity of the turbulent ABL flow over various rough terrains`: PDF file page 12; used as article Figure 13; asset `wechat/assets/public-safe/ref-wang2024-ES/fig-13-rough-terrain-vorticity.jpg`.
  - Fig. 19 `Mean wind field and flow structures around the building`: PDF file page 17; used as article Figure 19; asset `wechat/assets/public-safe/ref-wang2024-ES/fig-19-building-flow-structures.jpg`.
  - Fig. 21 `Contour of wind pressure coefficients at the building's surfaces`: PDF file page 19; used as article Figure 21; asset `wechat/assets/public-safe/ref-wang2024-ES/fig-21-wind-pressure-contours.jpg`.
- 关键公式:
  - 文章使用: original paper formula `\lambda^n(z)=K_P\left[I_{\mathrm{re}}^n(z)-I_{\mathrm{tar}}(z)\right]`, summarizing the proportional controller used in the simplified CWR setup.
  - 证据位置: PDF file page 13, Eq. (20).
  - 文章使用: inline variables and quantities including `$I_{\mathrm{re}}^n(z)$`, `$I_{\mathrm{tar}}(z)$`, `$K_P$`, `$K_P=-80.0$`, `$Q=200$`, and `$-5/3$`.
  - 证据位置: PDF file page 12, PDF file page 13, PDF file page 19, and PDF file page 20, Eqs. (20), (25), and (26).
- 页码口径: evidence locations use PDF file page numbers, not journal printed page numbers or article pagination.

## 图片使用记录

1. 图 3: CWR 方法获得指定湍流大气边界层风场的示意图
   - 用途: 开篇说明方法如何把反馈控制、SECD 模型、提取面和主计算域连接起来
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-wang2024-ES/fig-03-cwr-schematic.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 图像复核: visually verified against PDF file page 4 / Fig. 3 and local extracted image inventory
   - 公众号图名: 论文图 3 CWR 方法获得指定湍流大气边界层风场的示意图
   - 公众号说明: 展示 CWR 如何在辅助域中通过反馈控制和 SECD 模型生成目标 ABL 风场，并向主域输出入口速度时程。
   - 移动端预览: pending WeChat backend mobile preview
2. 图 13: 不同粗糙地形下湍流大气边界层风场的瞬时涡量
   - 用途: 展示三类粗糙地形下生成湍流结构的自持发展
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-wang2024-ES/fig-13-rough-terrain-vorticity.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 图像复核: visually verified against PDF file page 12 / Fig. 13 and local extracted image inventory
   - 公众号图名: 论文图 13 不同粗糙地形下湍流大气边界层风场的瞬时涡量
   - 公众号说明: 展示 CWR 生成的涡结构在乡村、郊区和城市粗糙地形中沿流向发展。
   - 移动端预览: pending WeChat backend mobile preview
3. 图 19: 建筑周围平均风场和流动结构
   - 用途: 展示 CWR 入流进入建筑主域后的典型绕流结构
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-wang2024-ES/fig-19-building-flow-structures.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 图像复核: visually verified against PDF file page 17 / Fig. 19 and local extracted image inventory
   - 公众号图名: 论文图 19 建筑周围平均风场和流动结构
   - 公众号说明: 展示主域中的流线、速度场和瞬时涡结构，帮助读者理解建筑绕流验证场景。
   - 移动端预览: pending WeChat backend mobile preview
4. 图 21: 建筑表面风压系数云图
   - 用途: 说明 CWR-LES 风压结果与 TPU 风洞试验数据的对应关系
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-wang2024-ES/fig-21-wind-pressure-contours.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: copied from local extracted PDF embedded image
   - 图像复核: visually verified against PDF file page 19 / Fig. 21 and local extracted image inventory
   - 公众号图名: 论文图 21 建筑表面风压系数云图
   - 公众号说明: 上排为 TPU 风洞试验数据库结果，下排为 LES 结果，用于比较平均与脉动风压系数分布。
   - 移动端预览: pending WeChat backend mobile preview

## 公式检查

- 使用公式: yes; one original paper display formula and inline mathematical quantities
- 呈现方式: Markdown LaTeX source; default WeChat API rendering is MathJax SVG with `data-formula` metadata
- 微信公式渲染路线: `mathjax-svg` unless a fallback reason is recorded
- RTD 呈现方式: Sphinx math roles/directives generated by `wechat/tools/markdown_to_rtd.py`
- 行内变量/量纲: formula markup applied to `$I_{\mathrm{re}}^n(z)$`, `$I_{\mathrm{tar}}(z)$`, `$K_P$`, `$K_P=-80.0$`, `$Q=200$`, and `$-5/3$`
- 移动端预览: pending WeChat backend mobile preview

## 封面图

- 封面状态: regenerated with image-gen-text; WeChat draft updated; pending WeChat backend mobile preview
- 候选数量: 3 concept directions documented in `wechat/articles/review/ref-wang2024-ES.cover-brief.md`; 1 selected image-gen-text cover exported
- 选中候选: `cover-wechat-900x383-imagegen-v1`
- 文字模式: image-gen-text
- 生成工具: Codex image generation tool
- 图像生成场景: CWR 可控弱循环入流湍流、反馈控制、粗糙地形 ABL、建筑风压 LES
- 要求文字: `数值风洞 / 入流自动收敛 / CWR湍流生成`
- 备用封面: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-v1.png)`
- 封面素材: `wechat/assets/public-safe/ref-wang2024-ES/cover-wechat-900x383-imagegen-v1.png`
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
- [x] 用 Zotero/PDF 摘要核对中文摘要，并按 2026-06-11 规则移除英文原摘要。
- [x] 从 PDF 抽取并导入可用正文图。
- [x] 由公众号正文转换生成 RTD 配套页，保持标题、正文、图片、DOI 和延伸阅读链接一致。
- [ ] 公众号后台手机预览正文、公式、封面和图片。
- [ ] 主线程集成 Research/index/backlog。
- [x] 微信公众号草稿已创建并回填 `wechat_status` 与草稿 media_id；正式发布后再回填 `latest_published_url`。

## 表达修订记录

- 2026-06-11: 按新表达规范完成批量修订——补入`三句话导读`和关键数字卡；删除英文摘要段，仅保留中文摘要；`研究问题`编号化；`关键发现`各小节首句回扣编号问题且加粗一句结论；图注改为`论文图 N`格式；`延伸阅读`前加入固定结尾块。开头策略：现实矛盾式。关键卡证据：比例控制、三类粗糙地形 MARE、谱一致性和建筑风压偏差均已在关键事实证据定位记录中标到 PDF file pages 11-21 及 Figs. 13、19、21。

## 检查记录

- Zotero metadata: passed via Zotero Desktop Local API
- PDF extraction: passed (`pdfinfo`, `pdftotext`, `pdfimages -list`, selected embedded images copied to public-safe assets)
- rtd-generation: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-wang2024-ES`)
- rtd-sync-check: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-wang2024-ES --check`)
- public-safety: passed (`python3 scripts/check-public-safe-content.py`)
- whitespace: passed (`git diff --check -- wechat/articles/draft-public-safe/ref-wang2024-ES.md wechat/articles/review/ref-wang2024-ES.review.md docs/source/paper-notes/ref-wang2024-ES.rst wechat/assets/public-safe/ref-wang2024-ES`)
- docs-build: passed (`./scripts/check-docs.sh`) after main-thread shared navigation integration
