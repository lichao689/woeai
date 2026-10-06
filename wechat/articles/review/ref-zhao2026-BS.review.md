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
- RTD全文覆盖: 2026-10-06 已完成作者侧逐段译制与图表校准；独立复核尚未完成，不能据此标为 verified
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

### 2026-10-05 历史重建审计结果（全文状态由后续记录替代）

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
- 2026-10-05 审计时 RTD 仍为历史选择性导读，尚缺完整1–6节、26幅图、11张表、式（1）–（11）和完整参考文献；该历史缺项由下述 2026-10-06 独立全文译制补齐。
- 当前本地修訂未自动更新微信后台；无新增上传、发布、提交或推送。历史转换、预览及检查日志不能充当当前构建结果。


## 2026-10-06 独立 RTD 全文译制与图像校准

### 完整覆盖范围

- 以授权出版版逐页原文为正文来源，保留摘要及1–6节顺序，共建立75个原始自然段／公式释义段／结论条目的逐段对应记录；原文跨页段落接续翻译，重复的引言内容也保留。未从公众号导读转换生成。
- 论文题名、全部8名作者及单位编号、5个作者单位、期刊卷期页码、收稿／修回／接受日期、4个关键词、通讯作者标记和邮箱均已保留。原文首页没有在线发表日期，未另行推断。
- 保留原图1–26、原表1–11，以及图26内嵌风险等级表。全部12张表均为可编辑中文 RST 表格；表10和表11的原合并单元格在展开时说明其共享关系。
- 式（1）–（11）全部使用可编辑 MathJax／RST 数学表达；图26的两条荷载公式和失效概率公式也补为可编辑公式。保持原编号，未使用公式截图或 tag 编号。
- 完整保留原文49条参考文献的顺序与可检索书目信息，正文55处作者—年份引用均链接到本页对应参考条目。
- 原文没有独立符号表、缩写表或附录；正文内的符号定义完整翻译。按项目要求排除致谢与利益冲突尾注，结论后直接接参考文献。
- 公众号正文与确认封面逐字节保持不变；仅将公众号已引用的4幅科学图别名同步为本次完整原生图像。未改注册表或就绪状态。

### 全部原图来源与范围

图像均来自同一授权出版版，采用原生嵌入图像提取；被PDF拆成连续水平条带的图，按页面纵向顺序拼回完整原图，不重采样原生像素。逐幅对照完整PDF源页和最终公开图片，检查所有分图、坐标轴、刻度、色标、图例、文字与外边界，无邻近正文、其他图或整体英文图题混入。本文26幅图未发现必须由独立矢量或文字叠层补回的元素。

| 原图 | 证据定位 | 公开素材 |
| --- | --- | --- |
| 1 | PDF file page 4 | `fig01.png` |
| 2 | PDF file page 5 | `fig02.png` |
| 3–4 | PDF file page 6 | `fig03.png`–`fig04.png` |
| 5 | PDF file page 7 | `fig05.png` |
| 6 | PDF file page 8 | `fig06.png` |
| 7–8 | PDF file page 9 | `fig07.png`–`fig08.png` |
| 9–10 | PDF file page 10 | `fig09.png`–`fig10.png` |
| 11–12 | PDF file page 11 | `fig11.png`–`fig12.png` |
| 13–14 | PDF file page 12 | `fig13.png`–`fig14.png` |
| 15 | PDF file page 13 | `fig15.png` |
| 16 | PDF file page 14 | `fig16.png` |
| 17–18 | PDF file page 15 | `fig17.png`–`fig18.png` |
| 19 | PDF file page 16 | `fig19.png` |
| 20 | PDF file page 17 | `fig20.png` |
| 21 | PDF file page 18 | `fig21.png` |
| 22–23 | PDF file page 19 | `fig22.png`–`fig23.png` |
| 24 | PDF file page 21 | `fig24.png` |
| 25 | PDF file page 22 | `fig25.png` |
| 26 | PDF file page 23 | `fig26.png` |

以上文件均位于 `wechat/assets/public-safe/ref-zhao2026-BS/`。图1、2、21、25的既有科学图别名同时更新为同一完整像素内容；封面不变。图题、重要英文标签、图例与分图说明均以可编辑中文置于对应图下。图13–15及20的原图题、正文和TI色标差异分别保留。

### 表格与公式定位

- 表1：PDF file page 7；表2–4：PDF file page 14；表5–6：PDF file page 16；表7：PDF file page 18；表8：PDF file page 19；表9–10：PDF file page 20；表11与图26内嵌表：PDF file page 23。
- 式（1）：PDF file page 3；式（2）–（4）：PDF file page 8；式（5）–（8）：PDF file page 13；式（9）：PDF file page 17；式（10）：PDF file page 22；式（11）及图26内嵌公式：PDF file page 23。
- 正文源页全部重新阅读并检查图面；其中公式以高倍页面渲染回查上下标、分数、指数与运算符，未用文本抽取猜测排印。

### 原文冲突与适用边界

1. PDF file page 1 的两个引言开头段落内容重复；PDF file page 2 的地形影响段内也有重复句。全文译文保留，没有压缩删除。
2. PDF file page 2 的模型名拼作 WALL，而 PDF file page 8 使用 WALE；正文中标注该拼写差异。
3. PDF file page 7 的顶部边界写成 symmetric (no-slip)，图4标注 Symmetry；没有自行改成无滑移或自由滑移条件。
4. PDF file page 8 式（2）印有ρ平方前因子，公式释义未定义ρ；式（4）括号内两项间未印运算符。均按图面保留，并注明须由作者澄清，不擅改为教科书公式。
5. PDF file page 8 正文说随机选30个点，而图6可见编号至29；没有补画或推断第30点。
6. PDF file pages 10、12–13、16–17 的正文称湍流强度，图13–15、20题名却称湍动能，色标为TI。不同表述分别保留。
7. PDF file page 19 表8的平均风速及统一列示参考点风速无法直接复算表内风速比；全文保留所有原数值，附复算示例揭示差异。
8. PDF file page 17 式（9）是原文带符号风速比相对误差；图22–23显示正误差幅值，原文未解释符号处理。没有把绝对值加入原公式。
9. PDF file page 19 分风向给17%／20%，PDF file page 20的概括段统一写17%且称平均风速误差。本页保留并说明冲突；PA站11 m/s筛选后90°／120°仅26／22个样本，不扩写成城市全域保证。
10. PDF file pages 20–21 的数据库更新要求受影响区块及周边重算；保留单区块CFD约27小时、处理和写入另约4小时的前期成本，以及高更新区域再划小子域的策略。
11. PDF file page 20 的24入流方向与 PDF file page 22 的12风压可视化方向分别保留，不将展示范围改写为数据库完整覆盖。
12. PDF file page 23 图26失效概率写为P(S<R)，而第5.4节正文描述为荷载超过抗力；保留该不等号与明确差异说明。风险等级表仅给符号阈值，不填造数值。
13. PDF file page 23 表11标题拼写Beauport且风速列未标单位；如实说明。参考文献中的规范编号JSJ/T 338按原文保留。
14. 第5节WebGIS、行人安全与结构荷载预警为展示及潜在应用流程；不宣称其真实预警准确率、AI代理模型或数字孪生性能得到验证。保留中性边界层、未考虑行人高度小型设施及LES内存需求限制。

### 当前检查与交付状态

- 独立本篇 Sphinx 内容诊断：通过 `-W --keep-going -E`，无警告；该诊断不是标准全站门禁。
- 全站内容诊断以命令行临时排除 sitemap 扩展后，最新 `-W --keep-going -E` 构建通过；没有修改共享配置，该诊断不替代标准门禁。公开安全检查、素材完整性检查和本篇差异空白检查通过。
- 实际全站诊断HTML检查：26个figure、27张图片（含封面）、12张可编辑表格、49个参考条目和55处引用链接；图片路径和全部引用目标可用，未出现字面量 `:math:`、`:ref:`、`:sup:` 或作者角色标记。
- MathJax SVG实际渲染：340个行内／块公式节点，13个展示公式块，无MathJax错误；编号公式为（1）–（11），另外两块用于图26内嵌公式。
- 标准 Sphinx 构建：当前运行被`sphinx_sitemap`的本地多进程通信初始化权限错误／EOFError阻断，未绕过限制，未改共享配置。整体`check-docs.sh`由批次集成检查另行承担。
- 全文源到译文清单、原图像素与来源范围清单、HTML与公式诊断记录保存在非公开工作存储；未把PDF、原始抽取全文、整页渲染或私有位置写入公开仓库。
- 独立内容复核尚未完成，`rtd_page_checked`仍为false；本文没有提交、推送、上传公众号或发布。微信后台手机预览和网站部署不属于本次作者侧检查结果。


## 2026-10-06 独立全文复核通过

- 25 页全文、26 幅源图、11 张原表与图 26 内嵌表、11 个编号公式与图内公式、49 条参考文献已完成独立逐页复核；作者单位、通讯脚注、全部引用和适用边界均保留。
- 每幅最终科学图分别与完整 PDF 原页核对，并独立重现源像素；已有选图别名经过复核，封面未改。
- 原文内部差异就近明确标注，不通过改数据、换图例或泛化结论掩盖差异。
- 最终诊断 Sphinx、实际 HTML 图像/引用/角色检查及 MathJax 渲染通过；标准门禁和部署由发布批次验证。
- 本结论取代上文的待独立审校状态，公众号后台预览及发布状态不变。

- 原生图 22(b)、23(b) 显示个别阈值/测站趋势与正文概括不同，已独立核实并在 4.3 节另列差异；未改变源图与原文译句。
