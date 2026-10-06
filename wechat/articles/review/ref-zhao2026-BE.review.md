---
publication_ref: ref-zhao2026-BE
doi: 10.1016/j.buildenv.2026.114811
wechat_status: awaiting_review
wechat_author: Zhao Peisheng
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
wechat_cover_image: wechat/assets/public-safe/ref-zhao2026-BE/cover-wechat-900x383-imagegen-v1.png
rtd_cover_image: wechat/assets/public-safe/ref-zhao2026-BE/cover-wechat-900x383-imagegen-v1.png
---

# ref-zhao2026-BE 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-zhao2026-BE.md`
- RTD正文: `docs/source/paper-notes/ref-zhao2026-BE.rst`
- 封面素材: `wechat/assets/public-safe/ref-zhao2026-BE/cover-wechat-900x383-imagegen-v1.png`
- 论文图 1 所提出框架的整体流程: `wechat/assets/public-safe/ref-zhao2026-BE/fig-01-workflow.png`
- 论文图 2 GF-7 的 MUX 与 PAN 数据集: `wechat/assets/public-safe/ref-zhao2026-BE/fig-02-gf7-dataset.png`
- 论文图 10 三维建筑几何的局部视图: `wechat/assets/public-safe/ref-zhao2026-BE/fig-10-local-geometry.png`
- 论文图 14 不同 DSM 生成与建筑高度估计算法的比较: `wechat/assets/public-safe/ref-zhao2026-BE/fig-14-dsm-comparison.png`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 2026-10-06 已完成重建并通过独立原文覆盖审校，详见下方本轮记录
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1016/j.buildenv.2026.114811
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 17；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `103c778b7a10e8a4320a74d2db9b0259dec7a072fe6419c27a52338010410b73`

## 关键事实证据定位记录

- 当前为17页正式版，替代旧25页预校样定位；以下文件页码不得与旧版本混用。
- 摘要、题名、作者与DOI：PDF file page 1；符号表：PDF file page 2。
- GF-7数据与流程：PDF file pages 2–4 Sections 2、2.1，Figs.1–3。
- Precision/Recall/F1/IoU＝0.9602/0.9166/0.9379/0.9178：PDF file page 5 Section 2.2.3；按原文报告值列示，IoU定义疑点见下。
- 双尺度视差估计和1 m DSM：PDF file pages 6–8 Section 2.3；轮廓规则化和LoD1：PDF file pages 8–9 Sections 3.1–3.2。
- 东莞建筑区域逐像素高度比较R²＝0.91、MAE＝2.72 m、RMSE＝4.09 m：PDF file page 11 Fig.13、PDF file page 12 Section 4.2及式（17）–（19）；图13的N＝214616是像素数。
- 145栋建筑逐栋高度MAE＝2.27/6.28/3.27 m（DSM-Net/SGM/MGM）：PDF file page 11 Fig.14(e)、PDF file page 13 Section 4.3。
- EVI及简化植被棱柱：PDF file page 10；冠层源项：PDF file page 12；城中村粘连与植被粗化边界：PDF file page 13结论。
- 正文没有列出完整风场实测误差或网格收敛结果，几何精度不能替代CFD风速/风压验证。

### 当前选图与公式

- 原Fig.1：PDF file page 3；已重新比对现有公开素材、原图及中文说明。
- 原Fig.2：PDF file page 4；已重新比对现有公开素材、原图及中文说明。
- 原Fig.10：PDF file page 9；已重新比对现有公开素材、原图及中文说明。
- 原Fig.14：PDF file page 11；已重新比对现有公开素材、原图及中文说明。

- 当前导读没有单独展示原编号公式；行内量名与报告值按上述证据核对。

## 当前事实修正与完整度

### 2026-10-05 重建审计结果

### 阅读范围与当前复核

- PDF file pages 1–2：摘要、符号表、引言；2–7：方法、训练、视差；8–10：几何和植被重建；11–13：验证及结论；14–16：附录A；16：附录B补充材料入口；16–17：参考文献。
- 本次重建以已完成逐页全文阅读的保留结论为起点，重新抽取现存全文、计算PDF校验值，并重新回查上述证据页、现有选图和公式。没有复用已丢失文件的旧指纹或旧验收状态。
- 图像核对范围是现有导读采用的原图及相关量化证据，不宣称所有原图逐一完成全文译制；微信后台手机预览未执行。

### RTD独立事实修正

1. 分别修正两渠道的统计单位：2.72 m是建筑区域内逐像素MAE，2.27 m是145栋逐栋MAE；不是同一指标的下降。
2. 明确DSM-Net符号表展开为Dual-Scale Matching Network，同时保留摘要原用语并说明内部命名差异。
3. 四项分割指标标明为论文报告值，并显式提醒IoU原式疑点，未自行改写数据。
4. 补充几何精度不等于风场验证的适用边界。
5. 整体更新现行证据定位为17页正式版；旧25页版本只作历史说明。

### 公众号独立事实核对

- 公众号源稿直接对照原论文摘要、方法、结果、图题、公式及限制，逐项执行与上述问题对应的修正；未由RTD转换生成，也未用公众号覆盖RTD。
- 忠实中文摘要保留原论文报告值；需要限定的统计单位、样本、网格、频率或适用条件在正文中明确。原文内部冲突不擅自统一。

### 原文疑点

- PDF file page 5式（9）原图分母为TP+FP+FP，缺少通常定义中的FN；指标聚合口径未明确，不能将四指标强行按同一混淆矩阵推算并替换。
- PDF file page 1摘要称digital surface model network，PDF file page 2符号表称Dual-Scale Matching Network；明确保留差异。
- PDF file page 10植被EVI负区间及“地面减DSM”高度描述存在疑问，导读不照搬其阈值和差值方向。
- PDF file page 3融合分辨率0.65 m，PDF file page 13局限性写0.68 m；导读的0.68 m明确来自局限性，不统一两个数。
- 附录B仅提供补充材料链接，不凭链接补写未提供的材料正文。

### 忠实度与完整度分别判定

- 现有导读文本事实及所用图/公式已重新对照并修正；原文疑点按页定位保留，图像后台可读性仍需预览。
- RTD仍为历史选择性导读，尚缺完整1–5节、符号表、20幅图、Table 1、式（1）–（19）、附录A和52条参考文献；全文完整度为false，仍需按原文顺序扩写，不能因事实审计通过改称全文精解完成。
- 当前本地修訂未自动更新微信后台；无新增上传、发布、提交或推送。历史转换、预览及检查日志不能充当当前构建结果。


## 2026-10-06 全文重建与独立审校

- 已独立从 17 页出版版逐段逐句译制，未从公众号导读转换。题名、六名作者及四组单位、通讯脚注、出版日期、四条亮点、摘要、关键词与 19 项缩写均保留。
- 正文 Sections 1–5 的全部段落、方法论证、数值设置、结果与局限均已对应；19 个编号公式使用可编辑数学形式，Table 1 的七项参数、定义与数值均为可编辑中文表。
- Fig. 1–20 全部保留，图题、分图及关键图内文字均有中文对应；附录 A（PDF file page 14–16）的 Fig. 15–20 完整。
- PDF file page 16 的 Appendix B 仅提供补充数据 DOI 入口，按公开页面的补充材料尾注排除规则处理；没有伪造外链材料正文。
- 55 处文内引用组的顺序与原文一致；52 条参考文献独立逐字符核对，仅整理空白和换行。
- 图 1 / PDF file page 3；图 2–3 / page 4；图 4 / page 5；图 5–6 / page 6；图 7 / page 7；图 8 / page 8；图 9–10 / page 9；图 11–12 / page 10；图 13–14 / page 11；图 15–16 / page 14；图 17–18 / page 15；图 19–20 / page 16。
- 18 幅完整嵌入图无损提取原生像素；Fig. 11、13 的六个子图标题属于 PDF 矢量层，故采用 400 dpi 完整图域渲染，避免仅提取位图时漏掉标题。20 幅最终图均逐张打开并对照原页，坐标、图例、色标、分图及标签完整，无相邻正文或总图题残片；独立复核确认对应源像素/渲染像素一致。
- 四个既有公众号图路径同步为相同校准图像；封面未改，没有后台上传、预览或发布。
- 保留三种不同统计单位：Fig. 13 的 N=214616 为像素数；Fig. 14(e) 为 145 栋建筑；Fig. 20 为 83 栋建筑，对应本文方法 MAE=2.57 m 与 nDSM MAE=11.40 m，不与 Fig. 14 的逐栋统计混用。
- 原文差异均有明确说明：式（9）重复 FP、DSM-Net 名称、EVI 负区间与植被高度差值方向、0.65/0.68 m、式（2）与解释中的 D 帽号差异。未将几何精度当作已验证 CFD 风速/风压精度。
- 独立审校发现四条图内说明断尾，均已修复并复核；最终正文、公式、图表、引用与附录 A 覆盖通过，没有剩余来源缺口。
- 顶部保留短公众号链接后立即放原封面；结论之后为附录 A、参考文献、完整引用。指定排除的出版声明尾节未进入公开正文。
- 本记录为内容与图片验收；批次标准构建、CI 与部署另行验证，不以离线检查代替后台手机预览。
