---
publication_ref: ref-zhao2026-BS
doi: 10.1007/s12273-025-1379-7
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
wechat_cover_image: wechat/assets/public-safe/ref-zhao2026-BS/cover-wechat-900x383-v2.png
rtd_cover_image: wechat/assets/public-safe/ref-zhao2026-BS/cover-wechat-900x383-v2.png
---

# ref-zhao2026-BS 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-zhao2026-BS.md`
- RTD正文: `docs/source/paper-notes/ref-zhao2026-BS.rst`
- 封面素材: `wechat/assets/public-safe/ref-zhao2026-BS/cover-wechat-900x383-v2.png`
- 论文图 1 所提出框架的工作流程: `wechat/assets/public-safe/ref-zhao2026-BS/fig-01-workflow.png`
- 论文图 2 深圳建筑分块划分示意图: `wechat/assets/public-safe/ref-zhao2026-BS/fig-02-block-division.png`
- 论文图 21 气象自动站的位置与观测环境: `wechat/assets/public-safe/ref-zhao2026-BS/fig-21-stations.png`
- 论文图 25 WebGIS 中风速与风压数据的可视化展示: `wechat/assets/public-safe/ref-zhao2026-BS/fig-25-webgis.png`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 未完成，缺项详见下文
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1007/s12273-025-1379-7
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 25；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `8d71e47664aa4cae4cac628a49aa72cd4f89648143db298eb617db2d95e6501a`

## 关键事实证据定位记录

- 摘要和题名：PDF file page 1；中文摘要逐段对应原文。
- 1 km × 1 km区块：PDF file page 3 Section 2、PDF file page 5 Fig.2及Section 3.3.1。
- 4Hmax建议及3Hmax可选：PDF file page 14 Tables 2–4和PDF file page 24结论；限文中深圳算例。
- 公共界面取平均：PDF file page 15 Section 3.5.1；过渡区减少差异，但不保证两块严格相等。
- 风速比误差公式：PDF file page 17式（9），不是编辑添加的解释式。原E为带符号相对误差，不擅加绝对值。
- PA参考站筛选及样本量：PDF file page 18 Section 4.2、Table 7；11 m/s下90°和120°分别26、22个十分钟样本。
- 分风向误差：PDF file page 19 Section 4.3、Figs.22–23；90°低于17%，120°低于20%，指平均风速比比较。
- 几何变化重算受影响区块及周边、单区块CFD约27小时及数据处理/写入另约4小时：PDF file page 20 Section 5.2。
- WebGIS应用：PDF file pages 21–23 Sections 5.3–5.4、Fig.25；植被、公交站等小型设施省略：PDF file page 24。

### 当前选图与公式

- 原Fig.1：PDF file page 4；已重新比对现有公开素材、原图及中文说明。
- 原Fig.2：PDF file page 5；已重新比对现有公开素材、原图及中文说明。
- 原Fig.21：PDF file page 18；已重新比对现有公开素材、原图及中文说明。
- 原Fig.25：PDF file page 22；已重新比对现有公开素材、原图及中文说明。

- 原式（9）：PDF file page 17；当前使用的符号、符号方向与条件已核对。

## 当前事实修正与完整度

### 2026-10-05 重建审计结果

### 阅读范围与当前复核

- PDF file pages 1–3：摘要、引言及框架；4–8：建模、WRF、CFD与数值设置；9–14：网格与过渡区；14–16：区块拼接；17–20：实测验证；20–23：数据库及应用；23–24：结论；24–25：参考文献。无附录。
- 本次重建以已完成逐页全文阅读的保留结论为起点，重新抽取现存全文、计算PDF校验值，并重新回查上述证据页、现有选图和公式。没有复用已丢失文件的旧指纹或旧验收状态。
- 图像核对范围是现有导读采用的原图及相关量化证据，不宣称所有原图逐一完成全文译制；微信后台手机预览未执行。

### RTD独立事实修正

1. 将两渠道“平均风速误差”修正为风速比相对误差，补PA参考站、26/22样本范围，避免把局部高风速验证写成全域精度保证。
2. 明确式（9）的原文身份，纠正旧review误记为编辑式的问题。
3. 补充公共界面平均处理，以及3Hmax/4Hmax建议的案例边界。
4. 把几何变更后直接复用的暗示改为受影响区块及周边重算，并补充27+4小时前期成本。
5. 移除AI/数字孪生性能已获本文验证的暗示，补充中性边界层和行人高度小型设施省略限制。

### 公众号独立事实核对

- 公众号源稿直接对照原论文摘要、方法、结果、图题、公式及限制，逐项执行与上述问题对应的修正；未由RTD转换生成，也未用公众号覆盖RTD。
- 忠实中文摘要保留原论文报告值；需要限定的统计单位、样本、网格、频率或适用条件在正文中明确。原文内部冲突不擅自统一。

### 原文疑点

- PDF file page 19 Table 8部分风速与参考点风速不能直接复算出同表风速比；导读未复制这些表值，保留待作者澄清。
- PDF file page 19分风向正文为17%/20%，PDF file page 20汇总又称三个站低于17%；导读采用分风向描述，不暗中统一原文。
- PDF file pages 10、14、16–17部分正文称湍流强度，而Figs.13–15、20图题称湍动能；未把这两种量混用于所选图说明。
- PDF file page 7顶部边界“symmetric (no-slip)”以及PDF file page 8式（2）中的黏度符号/密度因子存在需要作者校对之处；当前导读未据此新增模型公式。

### 忠实度与完整度分别判定

- 现有导读文本事实及所用图/公式已重新对照并修正；原文疑点按页定位保留，图像后台可读性仍需预览。
- RTD仍为历史选择性导读，尚缺完整1–6节、26幅图、11张表、式（1）–（11）和完整参考文献；全文完整度为false，仍需按原文顺序扩写，不能因事实审计通过改称全文精解完成。
- 当前本地修訂未自动更新微信后台；无新增上传、发布、提交或推送。历史转换、预览及检查日志不能充当当前构建结果。
