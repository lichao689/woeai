---
publication_ref: ref-tang2026-RE
zotero_key: XM44D697
doi: 10.1016/j.renene.2025.124336
research_family: 建筑结构抗风
subdirection: 数值风洞与湍动入流
publication_mode: first_publish
wechat_status: ready_to_publish
wechat_draft_media_id: OW4ZgzIulHGwsx2YUygit6A53AJWyrorKmAWHqdk-vEKHhAuk3dKwB_lrzFO9PkI
wechat_draft_created_at: 2026-06-10T20:06:25+08:00
wechat_draft_updated_at: 2026-06-11T16:41:36+08:00
wechat_author: Tang Lingxiao
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

# ref-tang2026-RE 发布说明

## 正文文件

- 公众号正文: `wechat/articles/draft-public-safe/ref-tang2026-RE.md`
- RTD 配套页: `docs/source/paper-notes/ref-tang2026-RE.rst`
- 微信草稿作者字段: `Tang Lingxiao`

## RTD 转换记录

- 内容母版: `wechat/articles/draft-public-safe/ref-tang2026-RE.md`
- 正式转换命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-tang2026-RE`
- 同步检查命令: `python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-tang2026-RE --check`
- 转换规则: 正文措辞、公式、正文图片和延伸阅读链接来自 Markdown；封面图、微信底部 `content_source_url` 等平台字段留给 review note、backlog 或后续发布记录。
- 导航状态: 未在本任务中编辑 `docs/source/Research.rst`、`docs/source/index.rst` 或 `wechat/backlog/selected-papers.yml`；待主线程统一集成。

## 证据来源

- DOI: https://doi.org/10.1016/j.renene.2025.124336
- Zotero: `XM44D697`
- PDF attachment key: `EQT752AQ`
- 摘要来源: Zotero Local API `abstractNote` and PDF abstract; 中文摘要为英文原摘要的忠实翻译，公众号正文与 RTD 页不再保留英文原摘要（2026-06-11 规则更新）。
- PDF / 作者稿: Zotero child record is `application/pdf` with `linkMode=imported_url`; the article evidence and figures use the valid local Zotero storage PDF for that child record, not a web-downloaded PDF.
- 公开网站记录: `docs/source/Publications.rst` contains `ref-tang2026-RE` as paper `[69]`; `docs/source/StructuralWindEngineering.rst` lists it under `数值风洞与湍动入流`.

## 源文件获取记录

- Zotero key: `XM44D697`
- Zotero 元数据: checked via Zotero Desktop Local API
- Zotero 附件记录: checked via Zotero Desktop Local API; PDF child `EQT752AQ` is `application/pdf`, `linkMode=imported_url`; HTML child `7C32GAAV` is `text/html`, `linkMode=imported_url`
- 本地 PDF 附件: exists and was verified from local Zotero storage; `pdfinfo` reports 24 PDF file pages, `pdftotext` OK, `pdfimages` OK
- PDF 附件候选: single PDF-like attachment in checked child records
- PDF 选择优先级: author manuscript > publisher version of record PDF > OA platform PDF > preprint > other
- 已选 PDF 类型: local Zotero storage PDF corresponding to PDF child `EQT752AQ`; attachment record is `imported_url`, but the file used for article evidence and figures is the local Zotero storage PDF
- 低优先级选择原因: not applicable; no web, preprint, or lower-priority substitute source was used
- PDF 来源类型: Zotero local storage PDF for imported-url attachment record; WOEAI/user-authored paper workflow scope
- PDF 私有存放: Zotero private attachment and ignored local extraction artifacts under `wechat/.local/ref-tang2026-RE/`; no PDF committed to this public repository
- Zotero Web API `/file`: not attempted; not needed because the local Zotero storage PDF was available and valid
- 网页 PDF 下载: not used
- 网页 PDF 批准记录: not applicable
- 摘要依据: Zotero `abstractNote` and PDF abstract on PDF file page 1
- 正文证据依据: PDF body, Zotero metadata, and public WOEAI publication record
- 图片依据: PDF embedded figures extracted from the local Zotero storage PDF and copied into public-safe body image assets
- 私有信息边界: no absolute private file path, credential, cookie, raw API payload, raw downloaded PDF content, or private preview URL is recorded here

## 关键事实证据定位记录

- 摘要:
  - 文章使用: 中文摘要忠实翻译英文摘要，不附英文原摘要。
  - 证据位置: Zotero `abstractNote`; PDF file page 1 abstract.
- 核心结论: 本文提出 WTT-SRST，用低时间分辨率风场快照重建高时间分辨率湍流演化，并用公式 `q(t_HR)=F_t(q(t_LR))` 表达 TSR-TF 映射任务。
  - 证据位置: PDF file page 6, Fig. 6 and Section 2.2 task overview, Eq. (12).
- 核心结论: Sparse Window-based Attention 使用 Stride-based Sparse Operation，stride 控制稀疏采样；计算复杂度随 `s^2` 出现在分母中，体现效率-精度折中。
  - 证据位置: PDF file pages 3-5, Figs. 1 and 3, Eqs. (2)-(5), Section 2.1.1.
- 核心结论: Relative Physical-informed Loss / Relative Physics-informed Loss 将不可压缩 Navier-Stokes 方程相关残差纳入训练损失，以增强生成风场的物理一致性。
  - 证据位置: PDF file pages 5-6, Section 2.1.3, Eqs. (6)-(11).
- 核心结论: 训练和测试结果显示，WTT-SRST 相比线性插值和 WTSR-ST 在统计误差上更低，并能较好复现湍流振幅、非均匀性和能量传递特征。
  - 证据位置: PDF file pages 10-14, Section 4.1, Figs. 9-15, Table 6; PDF file pages 15-18, Section 4.2, Figs. 16-20, Table 7.
- 核心结论: 功率谱和相干函数用于检查低频大尺度特征和高频瞬态细节；插值快照数量和 stride 增大会带来一定高频退化。
  - 证据位置: PDF file pages 13-15, Sections 4.1.2 and 4.2, Figs. 14-15 and 19-20.
- 核心结论: 单个 Sparse Window-based Attention Block 在 `s=2` 和 `s=4` 时显存占用为 `359.92 MB` 和 `250.35 MB`，低于 Swin-Transformer Block 的 `1225.26 MB`; 结论部分给出其约为后者的 `29.37%` 和 `20.43%`。
  - 证据位置: PDF file page 20, Table 8; PDF file page 19, Conclusions text.
- 核心结论: 所提出的稀疏注意力架构将参数量减少 `19.50%`，GPU 资源消耗降低约 `70%`。
  - 证据位置: PDF file page 20, Table 9; PDF file page 19, Conclusions text.
- 核心结论: WTT-SRST with `s=2` 将训练时间缩短 `32.92%`，计算能耗降低 `32.89%`; 更大的 stride 进一步降低能耗但会影响性能。
  - 证据位置: PDF file pages 21-22, Section 4.7 and Table 11; PDF file page 1 abstract.
- 核心结论: RPL 消融实验显示，相对连续性和相对动量项共同加入时效果最好，统计指标下降到原值的 `74-88%`。
  - 证据位置: PDF file pages 20-21, Section 4.5, Figs. 22-23; PDF file page 19, Conclusions text.
- 核心结论: 全尺度风场评估显示，随着插值快照增多细节会变模糊，但模型仍能表征空间非均匀性和流动结构。
  - 证据位置: PDF file page 21, Section 4.6, Fig. 24; PDF file page 22, Table 10.
- 关键图:
  - Fig. 6 `Temporal super-resolution procedure for the wind field snapshots`: PDF file page 6; used as article Figure 6; asset `wechat/assets/public-safe/ref-tang2026-RE/fig-06-temporal-super-resolution.jpg`.
  - Fig. 1 `Illustration of Stride-based Sparse Operation`: PDF file page 3; used as article Figure 1; asset `wechat/assets/public-safe/ref-tang2026-RE/fig-01-stride-sparse-operation.jpg`.
  - Fig. 4 `(a) The detailed structure of the proposed WTT-SRST...`: PDF file page 4; used as article Figure 4; asset `wechat/assets/public-safe/ref-tang2026-RE/fig-04-wtt-srst-framework.jpg`.
  - Fig. 14 `Power spectra density results of the fluctuating velocities`: PDF file page 14; used as article Figure 14; asset `wechat/assets/public-safe/ref-tang2026-RE/fig-14-power-spectra.jpg`.
  - Fig. 24 `Visual representation of the generated wind field at 3:45 a.m.`: PDF file page 21; used as article Figure 24; asset `wechat/assets/public-safe/ref-tang2026-RE/fig-24-generated-wind-field.jpg`.
- 关键公式:
  - 文章使用: $q(t_{\mathrm{HR}})=F_t(q(t_{\mathrm{LR}}))$ as the temporal super-resolution mapping.
  - 证据位置: PDF file page 6, Eq. (12).
  - 文章使用: $\Omega_{\mathrm{SPW\text{-}MSA}} = 4hwc^2 + 4(L^2/s^2)hwc$ as the computational-complexity expression for SPW-MSA.
  - 证据位置: PDF file page 5, Eq. (5).
  - 文章使用: RPL as an explanatory concept rather than reproducing the full Navier-Stokes residual formula.
  - 证据位置: PDF file pages 5-6, Eqs. (6)-(11).
- 页码口径: evidence locations use PDF file page numbers, not journal printed page numbers or article pagination.

## 图片使用记录

1. 图 6: 风场快照的时间超分辨率流程
   - 用途: 开篇任务图
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-tang2026-RE/fig-06-temporal-super-resolution.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: extracted with `pdfimages -all` from local Zotero storage PDF
   - 公众号图名: 论文图 6 风场快照的时间超分辨率流程
   - 公众号说明: 展示由低时间分辨率输入快照重建高时间分辨率风场序列的任务设定。
   - 移动端预览: pending WeChat backend mobile preview
2. 图 1: 基于步长的稀疏操作示意图
   - 用途: 解释 Sparse Window-based Attention 的计算节省机制
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-tang2026-RE/fig-01-stride-sparse-operation.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: extracted with `pdfimages -all` from local Zotero storage PDF
   - 公众号图名: 论文图 1 基于步长的稀疏操作示意图
   - 公众号说明: 展示如何通过步长采样和特征融合降低注意力计算量。
   - 移动端预览: pending WeChat backend mobile preview
3. 图 4: 所提出 WTT-SRST 的详细结构与各模块架构
   - 用途: 方法框架说明
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-tang2026-RE/fig-04-wtt-srst-framework.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: extracted with `pdfimages -all` from local Zotero storage PDF
   - 公众号图名: 论文图 4 所提出 WTT-SRST 的详细结构与各模块架构
   - 公众号说明: 展示编码-解码、skip connection 和稀疏窗口注意力模块之间的关系。
   - 移动端预览: pending WeChat backend mobile preview
4. 图 14: 脉动速度的功率谱密度结果
   - 用途: 物理一致性与频谱证据
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-tang2026-RE/fig-14-power-spectra.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: extracted with `pdfimages -all` from local Zotero storage PDF
   - 公众号图名: 论文图 14 脉动速度的功率谱密度结果
   - 公众号说明: 用频域结果检查重建风场是否保留湍流能量分布。
   - 移动端预览: pending WeChat backend mobile preview
5. 图 24: 凌晨 3:45 生成风场的可视化表示
   - 用途: 全尺度风场评估图
   - 图片状态: inserted in reader-facing Markdown
   - 素材文件: `wechat/assets/public-safe/ref-tang2026-RE/fig-24-generated-wind-field.jpg`
   - 来源/版权: paper PDF embedded figure; WOEAI/user-authored paper workflow scope
   - 抽取方式: extracted with `pdfimages -all` from local Zotero storage PDF
   - 公众号图名: 论文图 24 凌晨 3:45 生成风场的可视化表示
   - 公众号说明: 展示全尺度风场应用中重建结果与参考结果的空间结构对比。
   - 移动端预览: pending WeChat backend mobile preview

## 公式检查

- 使用公式: yes; two short display formulas and several inline mathematical variables/quantities
- 呈现方式: Markdown LaTeX source; default WeChat API rendering should be MathJax SVG with `data-formula` metadata
- 微信公式渲染路线: `mathjax-svg` unless a fallback reason is recorded
- RTD 呈现方式: Sphinx math roles/directives generated by `wechat/tools/markdown_to_rtd.py`
- 行内变量/量纲: formula markup applied to $q(t_{\mathrm{HR}})$, $q(t_{\mathrm{LR}})$, $F_t$, $h$, $w$, $c$, $L$, $s$, GPU memory quantities, percentages, and energy/time metrics
- 移动端预览: pending WeChat backend mobile preview

## 封面图

- 封面状态: regenerated locally with image-gen-text v5 publication metadata line; uploaded to the existing WeChat draft; pending WeChat backend mobile preview
- 候选数量: 3 image-gen-text v5 publication-line candidates generated in this round; 1 selected image-gen-text cover exported for draft update
- 选中候选: `cover-wechat-900x383-imagegen-v5-b-pub-line-no-dot`
- 出版信息行: `Renewable Energy · 2026`
- 出版信息行样式: subtitle-below semi-bold deep-blue text line; no leading dot, no icon, no badge, no capsule, no button-like outline
- 文字模式: image-gen-text
- 生成工具: Codex image generation tool
- 图像生成场景: 城市风能高时间分辨率风场重建、稀疏快照、WTT-SRST、物理一致性与工程应用
- 要求文字: `数值风洞 / 稀疏快照补全风场 / 看见湍流时间细节`
- 备用封面: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-v1.png)`
- 上一版草稿封面候选: `wechat/assets/public-safe/ref-tang2026-RE/cover-wechat-900x383-imagegen-v2.png`
- 候选 A: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-imagegen-v2-a-research-scene.png)`
- 候选 B: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-imagegen-v2-b-method.png)`
- 候选 C: `removed during 2026-06-11 slimming cleanup (cover-wechat-900x383-imagegen-v2-c-engineering-impact.png)`
- v5 候选 A: `wechat/assets/public-safe/ref-tang2026-RE/cover-wechat-900x383-imagegen-v5-a-pub-line-no-dot.png`
- v5 候选 B: `wechat/assets/public-safe/ref-tang2026-RE/cover-wechat-900x383-imagegen-v5-b-pub-line-no-dot.png`
- v5 候选 C: `wechat/assets/public-safe/ref-tang2026-RE/cover-wechat-900x383-imagegen-v5-c-pub-line-no-dot.png`
- 封面素材: `wechat/assets/public-safe/ref-tang2026-RE/cover-wechat-900x383-imagegen-v5-b-pub-line-no-dot.png`
- 尺寸: `900 x 383 px`
- 本地裁剪预览: `wechat/.local/cover-previews/cover-preview.html`
- 质量评分: article_specificity=5, main_subject_clarity=5, click_appeal=5, engineering_credibility=4, thumbnail_readability=5, crop_safety=4, text_quality=5
- 未采用候选原因: v5A 出版信息行更安静但略小；v5C 画面平衡但小图可读性略弱；v5B 的 `Renewable Energy · 2026` 最清楚且没有抢主标题层级。
- 审核状态: local visual text check and crop preview passed; WeChat backend mobile preview pending
- 草稿状态: existing WeChat draft updated with `cover-wechat-900x383-imagegen-v5-b-pub-line-no-dot.png` at 2026-06-11T16:41:36+08:00; WeChat backend mobile preview not yet checked.
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

- [x] 用 Zotero Local API 核对作者、期刊、年份、DOI、摘要和附件记录。
- [x] 用本地 Zotero storage PDF 核对摘要、关键事实、公式、图题和页码。
- [x] 从 PDF 抽取并导入可用正文图。
- [x] 由公众号正文转换生成 RTD 配套页，保持标题、正文、图片、DOI 和延伸阅读链接一致。
- [ ] 由主线程将 RTD 配套页挂入相关科研方向页或首页最新学术进展。
- [ ] 公众号后台手机预览正文、公式、封面和图片。
- [x] 微信公众号草稿已创建并回填 `wechat_status` 与草稿 media_id；正式发布后再回填 `latest_published_url`。

## 表达修订记录

- 2026-06-11: 按新表达规范完成批量修订——补入`三句话导读`和关键数字卡；删除英文摘要段，仅保留中文摘要；`研究问题`编号化；`关键发现`各小节首句回扣编号问题且加粗一句结论；图注改为`论文图 N`格式；`延伸阅读`前加入固定结尾块。开头策略：场景式。关键卡证据：训练时间、能耗、注意力显存、参数量和 RPL 消融结果均已在关键事实证据定位记录中标到对应性能评估和消融实验页码。

## 检查记录

- Zotero metadata: checked via Zotero Desktop Local API
- Zotero children: checked via Zotero Desktop Local API
- PDF inspection: passed (`pdfinfo`, `pdftotext -layout`, `pdfimages -list`)
- figure extraction: selected embedded PDF JPG images copied from local ignored extraction artifacts to public-safe asset names
- rtd-generation: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-tang2026-RE`)
- rtd-sync-check: passed (`python3 wechat/tools/markdown_to_rtd.py --publication-ref ref-tang2026-RE --check`)
- public-safety: passed (`python3 scripts/check-public-safe-content.py`)
- whitespace: passed (`git diff --check -- wechat/articles/draft-public-safe/ref-tang2026-RE.md wechat/articles/review/ref-tang2026-RE.review.md docs/source/paper-notes/ref-tang2026-RE.rst wechat/assets/public-safe/ref-tang2026-RE`)
