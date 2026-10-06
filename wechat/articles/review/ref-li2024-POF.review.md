---
publication_ref: ref-li2024-POF
doi: 10.1063/5.0194006
wechat_status: awaiting_review
wechat_author: Li Chao
source_checked: true
facts_checked: true
abstract_checked: true
body_images_upload_approved: true
copyright_checked: true
public_safety_checked: true
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
wechat_backend_preview_checked: false
rtd_page_checked: false
rtd_coverage_status: complete_pending_independent_review
wechat_cover_image: wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v2.png
rtd_cover_image: wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v2.png
---

# ref-li2024-POF 原文核验记录

## 当前核验结果

- RTD 已由原论文独立重写为全文中文译稿：原文 I–IV 节、公式（1）–（57）、图 1–11、表 I–II、参考文献 1–60 均已收入。作者自查完成；独立复核与整站发布验收尚未完成，不据此提前标记最终 verified。
- 公众号仍是独立导读，未以其正文代替 RTD 全文，当前未执行微信后台预览或更新。
- 图 1–11 已逐张与 PDF 页像素核对，并逐张打开最终资产检查。旧图 7 遗漏的四个子图标签已恢复。
- 原封面保持不变，RTD 开头已补“精简版微信公众号文章：待发布”，随后紧接封面。

## 正文与公开素材

- 公众号正文：`wechat/articles/draft-public-safe/ref-li2024-POF.md`
- RTD 全文：`docs/source/paper-notes/ref-li2024-POF.rst`
- 封面：`wechat/assets/public-safe/ref-li2024-POF/cover-wechat-900x383-v2.png`
- RTD 图像均位于 `wechat/assets/public-safe/ref-li2024-POF/`，具体见下表。
- 公众号既有选图路径 `fig3-vprfg-flowchart.png`、`fig4-von-karman-energy-spectrum.jpg`、`fig7-q-criterion-isosurfaces.jpg`、`fig9-decaying-box-energy-spectra.jpg` 已同步替换为校准资产，不改公众号正文。

## 源文件获取记录

- DOI：https://doi.org/10.1063/5.0194006
- 来源：用户授权、确认作者拥有复用权限的期刊出版版 PDF；题名、作者、期刊及 DOI 与公开学术成果条目一致。
- 当前可用来源为出版版；本次未取得更高优先级作者稿。PDF 保存在私有源文件存储中，未进入公开仓库。
- 已使用现存获准 PDF，不另行抓取网页 PDF，不调用私人凭据或重新下载附件。
- 总文件页数：15。PDF file page 1 为出版封面；原文文章及参考文献位于 PDF file pages 2–15。以下页码均为文件物理页码。
- 当前核验副本 SHA-256：`855a45aad06339d34c5f411f2a075eb1b8bf1acc903dccfb695ca273bdbe05c3`。
- 当前核验副本与历史原始副本的字节等价性未建立；不将两者哈希混同，也不猜测差异原因。
- 摘要、正文、公式、图表、参考文献均直接以该 PDF 为来源；公开网页或公众号导读未用于补造正文。

## 关键事实证据定位记录

- 题名、作者、五组单位、通讯作者注、投稿/录用/在线发表日期及摘要：PDF file page 2。未见单列关键词表、符号表、缩写表或修回日期，正文中所有符号及缩写定义已随段落翻译。
- 文献综述及研究范围：PDF file pages 2–4，Section I；保留前驱/循环/合成方法分类以及 SRFM、WAWS、RFG、SCEM、SEM 各变体的文献链。
- HIT 的 CSD、能谱、Reynolds 应力、PSD、相关与相干关系：PDF file page 4，Section II.A，式（1）–（13）。这些统计量来自同一目标 HIT 谱的相容关系，不可彼此独立任意指定。
- 矢量势及旋度：PDF file page 5，Section II.B，式（14）–（23）；连续式（17）与离散式（18）均完整转写。
- 频率符号与相位方向：PDF file page 6，式（24）–（31）。正号时间相位必须配套式（25）的负频率号；Taylor 平移方向保留为 t−τ 与 x+Uτ。
- 统计推导：PDF file pages 7–8，Section II.D，式（32）–（48），保留全部积分、矩阵、概率分布及谱段极限步骤。
- 算法：PDF file pages 8–9，Section II.E，11 个步骤、式（49）–（51）；有限域、网格与时间步限制可表示波数范围，增加谱段数不能补回截谱区间外的能量。
- von Kármán 验证：PDF file pages 9–10，Section III.A，128³/256³/384³ 网格，N=5000，0.2π m 立方域，σiso=0.25 m/s，κe=40√(5/12) m⁻¹，时间序列与三组点距均保留。
- 衰减盒湍流：PDF file pages 9–11，Section III.B；CBC 实验参考时刻为 U₀t/M=42、98、171，LES 相对时刻为 0、0.28、0.66 s；保留求解器、模型、周期边界、离散格式、黏度及时间步设置。
- C1/C3 采用式（17），C2/C4 采用式（18）：PDF file page 10，Table I；全部四工况及网格、时间步已转为可编辑中文表。
- 面通量守恒与单元中心速度散度不同：PDF file pages 10–11，式（54）–（55）、Table II；表内全部 24 个数值已核对，特别保留 C3 初始标准差 10.5。
- C4 初始能量偏高、离散式改变初始统计：PDF file pages 11–13，Figs. 7–11；没有将全部工况概括为同样准确。
- 空间相关参照由目标/实验参考谱推算：PDF file page 11，式（57）及 Figs. 10–11 的相关段落，不描述为独立直接测量的空间相关数据。
- 当前限于 HIT、任意非均匀各向异性三维空间 CSD 的构造尚待研究：PDF file pages 11–14，Section IV。

## 图像校准与完整覆盖

所有原图均在获准 PDF 内重新定位。矢量图通过页面渲染裁切保留矢量文字；完整嵌入位图直接无损提取，不重绘科学内容，不修改曲线、坐标或数据。每张最终图均单独打开检查；未以拼图总览替代逐图验收。

| 原图 | 源页 | RTD 资产文件 | 校准方式与完整性 |
| --- | --- | --- | --- |
| Fig. 1 | PDF file page 6 | `fig01-energy-spectrum-discretization.png` | 324 dpi 渲染裁切；完整能谱、两坐标轴及 κ₁/κ₂/κN−1/κN 标签 |
| Fig. 2 | PDF file page 6 | `fig02-wavenumber-vector.png` | 324 dpi 渲染裁切；完整球面、三个轴、波矢及极角/方位角标签 |
| Fig. 3 | PDF file page 8 | `fig3-vprfg-flowchart.png` | 324 dpi 渲染裁切；所有流程框、箭头、框内公式及末端速度式完整，无邻近正文/图题 |
| Fig. 4 | PDF file page 9 | `fig04-von-karman-energy-spectrum.png` | 804×578 原生位图像素；两坐标轴、刻度、单位、完整图例保留 |
| Fig. 5 | PDF file page 10 | `fig05-temporal-spectra.png` | 1990×568 原生位图像素；u/v/w 三子图、全部坐标轴与图例完整 |
| Fig. 6 | PDF file page 10 | `fig06-spatial-coherence.png` | 1992×527 原生位图像素；三组点距标签、相干实部纵轴、频率横轴完整 |
| Fig. 7 | PDF file page 12 | `fig07-q-criterion-complete.png` | 432 dpi 渲染裁切，2148×2502；保留位图外的 PDF 文本层（a）–（d）、工况/网格/Q 阈值以及四个色标，排除右侧图题 |
| Fig. 8 | PDF file page 12 | `fig08-tke-decay.png` | 824×553 原生位图像素；实验与 C1–C4 图例、动能/时间坐标完整 |
| Fig. 9 | PDF file page 13 | `fig09-decaying-box-energy-spectra.png` | 1988×529 原生位图像素；42/98/171 三时刻子图、图例与单位完整 |
| Fig. 10 | PDF file page 13 | `fig10-longitudinal-spatial-correlation.png` | 1983×524 原生位图像素；纵向相关系数三子图、时间标签、图例完整 |
| Fig. 11 | PDF file page 13 | `fig11-transverse-spatial-correlation.png` | 1987×525 原生位图像素；横向相关系数三子图、时间标签、图例完整 |

- 原图 7 的旧素材仅含嵌入位图，因此丢失 PDF 外置子图文字。本次使用完整图域渲染修复；公众号旧 JPG 路径也使用同一校准图域。
- 图 7 上排 C1/C2 为 128³、Q=500，下排 C3/C4 为 256³、Q=2000；差异还涉及式（17）/（18），不能仅归因于网格分辨率。
- 图中英文关键文字在中文图注中说明：Target、Expt.、grid、component、case 以及流程框内容。原图内像素保持原样。
- 图 4/9 的旧 JPG 路径直接恢复 PDF 原生 JPEG 字节；RTD PNG 是同一解码像素的无损副本。图 7 旧 JPG 从完整校准图域高质量导出。

## 全文覆盖自查

- 文件页 1：出版封面信息与文件页 2 重复，按原文章保留一次元信息；网页按钮、下载水印和出版商页脚不属于正文。
- 文件页 2：题名、作者、单位、通讯作者注、期刊日期及完整单段摘要均已翻译。
- I 引言：已翻译，PDF file pages 2–4，保留全部 7 个自然段及文内引用。
- II.A：已翻译，PDF file page 4，完整 13 式及公式前后定义。
- II.B：已翻译，PDF file pages 4–6，完整式（14）–（26）及随机参数定义。
- II.C：已翻译，PDF file page 6，无散与 Taylor 冻结假设两项证明完整。
- II.D.1–II.D.3：已翻译，PDF file pages 6–8，平均速度、三维 CSD、其他低维统计的推导文字和全部公式完整。
- II.E：已翻译，PDF file pages 8–9，11 步算法全部保留。
- III.A：已翻译，PDF file pages 9–10，目标参数、网格、点坐标、时长、时间步、谱公式及全部结果分析完整。
- III.B：已翻译，PDF file pages 9–13，全部设置、误差评价、四工况比较、衰减与相关分析完整。
- IV：已翻译，PDF file pages 11–14，完整 4 段结论及局限。
- 图：Fig. 1–11 全部收入，完整中文图题和必要的图内文字释义。
- 表：Table I–II 全部为中文可编辑 list-table，数值未改写。
- 公式：Eq. (1)–(57) 全部为可编辑数学标记，原编号以 `\qquad (N)` 保留。
- 引用：PDF file pages 14–15 的 60 条参考文献完整保留；正文引用连接到带原编号的参考文献，未用其他文章书目替换。
- 附录：原文无附录，不适用。
- 关键词、独立符号/缩写表：原文未设置，不适用；所有原文行内定义与首次缩写均已保留。
- 尾部：结论之后直接进入参考文献，再接“完整引用”及 Publications 锚点；按项目规范排除致谢、作者贡献/利益冲突、数据可用性等声明性尾注。
- 封面顺序正确；不存在私有绝对路径、遗漏占位或 `\tag{`。

## 原文差异与解释边界

- PDF file page 11 将衰减描述为 exponentially，而式（56）写成关于移位无量纲时间的幂律。全文忠实译出该措辞，并紧接明确译注；不将它悄悄改写为另一公式。
- 原文用“严格零散度”描述离散初场，但 Table II 实际值为浮点量级而非数学零。译文保留原段落，并通过明确译注区分连续恒等式、单元中心速度散度与面通量守恒。
- PDF file page 4 式（11）右端为 E(κ)/(2πκ²)，而同页式（1）的 Φuu 系数为 E(κ)/(4πκ²)。两处逐字保留；将其列作待独立复核的归一化一致性问题，不宣称已证明为排版错误，也不擅自改成 4π。
- PDF file page 11 对纵向与横向相关系数共同引用式（5）、（8）；Section II.A 中横向一维谱单列为式（6）。保留原文引用，未擅自更改计算方法。
- 参考文献 [45] 年份按 PDF 保留为 2023；其书目信息是本文原引用，未用其他页面记录覆盖。
- 统计逼近的谱段极限与有限波数范围应区分；理论连续无散不等于任意离散表示严格无散；当前验证对象始终限定为 HIT。

## 检查状态

- 已通过：公开内容安全扫描。
- 已通过：publication artifacts 只读一致性检查。
- 已通过：本篇 RST 的独立 Sphinx HTML 构建，启用 warnings-as-errors；两处标题下划线长度问题已修复后重跑，无警告。
- 已通过：57 个公式编号连续且不重复、11 幅正文图路径、两张可编辑表、60 个参考文献锚点与正文引用目标检查；封面未修改。
- 已通过：目标范围 `git diff --check`。
- 尚未执行：整站标准构建与部署，由批次集成阶段运行；独立科学/译文复核尚未完成。
- 尚未执行：微信后台手机预览及浏览器端 MathJax 最终显示检查；不借本次静态构建提升对应预览字段。


## 2026-10-06 独立原文复核结论

- 独立审校逐段逐句对照全部授权源页，逐式检查公式、逐值检查表格、逐条检查参考文献，并逐张对照最终图片与完整 PDF 原页。
- 全文内容与原图覆盖审核通过；原文内部差异继续保留，不把源文问题擅自改成译文结论。批次构建和部署独立验收，公众号后台状态未变。
- 复核发现并修复式（2）两项 Φ 的转写、表 II 数值残差译注及结论对式（17）“推导矢量势场”的原文指代；11 幅图逐像素对应原生解码或指定源页渲染，图 7 的外置子图标签完整。


### 2026-10-06 页面内联语法复核

- 对照最终生成 HTML 检查内联引用与公式，修正全角括号旁的 RST 角色边界，避免引用或公式源码以普通文字显示；所有公式及引用角色内部文本保持不变。
- 新增实际 Sphinx 渲染回归，覆盖当前全部已核验全文页面，并检查页面可见文本中不存在字面 :ref: 或 :math: 残留；参考文献链接目标保持有效。
