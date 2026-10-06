---
publication_ref: ref-zhao2025-SCS
doi: 10.1016/j.scs.2025.106237
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
wechat_cover_image: wechat/assets/public-safe/ref-zhao2025-SCS/cover-wechat-900x383-v2.png
rtd_cover_image: wechat/assets/public-safe/ref-zhao2025-SCS/cover-wechat-900x383-v2.png
---

# ref-zhao2025-SCS 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-zhao2025-SCS.md`
- RTD正文: `docs/source/paper-notes/ref-zhao2025-SCS.rst`
- 封面素材: `wechat/assets/public-safe/ref-zhao2025-SCS/cover-wechat-900x383-v2.png`
- 论文图 1 算法框架总体流程: `wechat/assets/public-safe/ref-zhao2025-SCS/fig-01-workflow.png`
- 论文图 14 选定建筑的密集点云: `wechat/assets/public-safe/ref-zhao2025-SCS/fig-14-dense-point-cloud.png`
- 论文图 18 几何模型重建结果: `wechat/assets/public-safe/ref-zhao2025-SCS/fig-18-geometry-reconstruction.png`
- 论文图 25 研究区域 2 m 高度处的速度幅值: `wechat/assets/public-safe/ref-zhao2025-SCS/fig-25-velocity-magnitude.png`
- 论文图 34 风场插值结果: `wechat/assets/public-safe/ref-zhao2025-SCS/fig-34-webgis-interpolation.png`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 未完成，缺项详见下文
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1016/j.scs.2025.106237
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 24；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `c1dceebf21a54b93e7595851052191a2198f508bb4d0a55e1dc8eccb36765b08`

## 关键事实证据定位记录

- 摘要、题名、通讯标记：PDF file page 1，星号对应Xiaolu Wang；原摘要速度写3–5倍。
- 方法链：PDF file pages 3–8 Sections 2.1–2.3、Fig.1。
- 5栋代表建筑及平均精度12%：PDF file pages 9–11 Section 3.1、Tables 1–2；B4本方法Acc＝0.2168 m，高于COLMAP的0.1379 m。
- 结论速度2–3倍：PDF file page 22；不同方法的逐栋耗时在PDF file page 11 Table 2，不同基准不可合并成无条件加速比。
- LoD2/LoD2.5和立面细节限制：PDF file page 11 Section 3.2；SfM数小时至数天：PDF file page 12 Section 3.4。
- CFD设置与加密区参照距离：PDF file page 12 Section 4.1.1；植被棱柱及源项已纳入：PDF file page 13式（14）–（16）、PDF file page 18 Fig.24。
- 基础网格GCI：PDF file page 15 Table 3，U/p/k/ε＝3.51/3.76/4.89/4.70%；粗网格为5.20/5.57/7.24/6.96%，不能把3.76%写成所有网格最大误差。
- 行人舒适度：PDF file pages 16–19，30点中25与28为III类、23为IV类，其余I/II类；WebGIS：PDF file pages 19–22。

### 当前选图与公式

- 原Fig.1：PDF file page 3；已重新比对现有公开素材、原图及中文说明。
- 原Fig.14：PDF file page 11；已重新比对现有公开素材、原图及中文说明。
- 原Fig.18：PDF file page 14；已重新比对现有公开素材、原图及中文说明。
- 原Fig.25：PDF file page 18；已重新比对现有公开素材、原图及中文说明。
- 原Fig.34：PDF file page 22；已重新比对现有公开素材、原图及中文说明。

- 当前导读没有单独展示原编号公式；行内量名与报告值按上述证据核对。

## 当前事实修正与完整度

### 2026-10-05 重建审计结果

### 阅读范围与当前复核

- PDF file pages 1–2：摘要与引言；3–8：分块、3DGS、点云分离与几何算法；9–12：精度、效率、资源和限制；12–15：CFD与GCI；16–20：行人舒适度；19–22：WebGIS与结论；23–24：参考文献。无附录。
- 本次重建以已完成逐页全文阅读的保留结论为起点，重新抽取现存全文、计算PDF校验值，并重新回查上述证据页、现有选图和公式。没有复用已丢失文件的旧指纹或旧验收状态。
- 图像核对范围是现有导读采用的原图及相关量化证据，不宣称所有原图逐一完成全文译制；微信后台手机预览未执行。

### RTD独立事实修正

1. 两渠道作者行及RTD完整引用的通讯星号由Li Chao移至Wang Xiaolu；共享书目由主任务独立处理。
2. 12%限定为5栋平均，并补B4劣于COLMAP、完整性和召回不足的负面结果。
3. 原摘要3–5倍、结论2–3倍同时保留并明示基准不一；补SfM前期耗时，避免端到端加速夸大。
4. 将3.76%和4.89%限定为基础网格相应GCI，明确离散化指标不等于全部物理误差。
5. 改正植被“尚未纳入”的暗示，说明已采用简化棱柱和冠层源项，精细表达仍待改善。
6. 补加密区距离参照和未验证AI/数字孪生、风场实测精度的边界；图14/34定位更正为第11/22页。

### 公众号独立事实核对

- 公众号源稿直接对照原论文摘要、方法、结果、图题、公式及限制，逐项执行与上述问题对应的修正；未由RTD转换生成，也未用公众号覆盖RTD。
- 忠实中文摘要保留原论文报告值；需要限定的统计单位、样本、网格、频率或适用条件在正文中明确。原文内部冲突不擅自统一。

### 原文疑点

- 摘要速度3–5倍和结论2–3倍不一致，保留两处出处，不擅改原文。
- PDF file page 12称连续尺度比1.3，但同时列1.44/1.2/1 m和不同单元数，尺度定义需作者澄清。
- PDF file page 15称细/粗误差更小，选择基础网格的上下文却可能指细/基础；不照搬可疑比较句。
- PDF file page 16式（20）解释将θ称位置参数，Table 5部分k值为0；PDF file page 21将经验贝叶斯克里金和RBF-M并列命名，均保留为原文疑点而非新增实现依据。

### 忠实度与完整度分别判定

- 现有导读文本事实及所用图/公式已重新对照并修正；原文疑点按页定位保留，图像后台可读性仍需预览。
- RTD仍为历史选择性导读，尚缺完整1–5节、34幅图、6张表、式（1）–（21）和完整参考文献；全文完整度为false，仍需按原文顺序扩写，不能因事实审计通过改称全文精解完成。
- 当前本地修訂未自动更新微信后台；无新增上传、发布、提交或推送。历史转换、预览及检查日志不能充当当前构建结果。
