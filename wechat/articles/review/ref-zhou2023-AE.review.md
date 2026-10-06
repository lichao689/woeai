---
publication_ref: ref-zhou2023-AE
doi: 10.1016/j.apenergy.2023.121941
wechat_status: awaiting_review
wechat_author: Zhou Shengtao
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
wechat_cover_image: wechat/assets/public-safe/ref-zhou2023-AE/cover-wechat-900x383-imagegen-v1.png
rtd_cover_image: wechat/assets/public-safe/ref-zhou2023-AE/cover-wechat-900x383-imagegen-v1.png
---

# ref-zhou2023-AE 原文核验记录

## 正文与公开素材

- 公众号正文: `wechat/articles/draft-public-safe/ref-zhou2023-AE.md`
- RTD正文: `docs/source/paper-notes/ref-zhou2023-AE.rst`
- 封面素材: `wechat/assets/public-safe/ref-zhou2023-AE/cover-wechat-900x383-imagegen-v1.png`
- 论文图 1 自由度和全局坐标系定义: `wechat/assets/public-safe/ref-zhou2023-AE/fig-01-dof-coordinate.jpg`
- 论文图 7 所研究浮式风机的平台构型与系泊布置: `wechat/assets/public-safe/ref-zhou2023-AE/fig-07-platform-mooring-layout.jpg`
- 论文图 19 不同环境输入得到的 Pareto 前沿对比: `wechat/assets/public-safe/ref-zhou2023-AE/fig-19-pareto-environmental-inputs.jpg`
- 论文图 23 方形与 Y 形下部结构的 Pareto 前沿对比: `wechat/assets/public-safe/ref-zhou2023-AE/fig-23-pareto-substructures.jpg`
- 论文图 25 两类下部结构在 135 度波向下的平台运动 RAO 对比: `wechat/assets/public-safe/ref-zhou2023-AE/fig-25-rao-comparison.jpg`

## 当前核验结果

- 公众号: awaiting_review；当前稿件尚未完成后台手机预览
- RTD全文覆盖: 全文译稿与27幅原图已通过独立原文覆盖审校；构建与部署按批次验收
- 事实检查: 已核对所用事实；原文内部差异保留出处

## 源文件获取记录

- DOI: https://doi.org/10.1016/j.apenergy.2023.121941
- 来源: 用户授权的期刊出版版PDF，身份与论文题名、作者及DOI核对一致
- 文件页数: 20；以下PDF file page均为文件物理页码
- 当前核验副本SHA-256: `0339a5a26859683341f52de5ecc0c5fd517ab94e38840866dc5885ccf0420b8f`

## 关键事实证据定位记录

本节是本轮核对后的当前证据，页码均为PDF物理文件页序。


- 摘要与身份：PDF file page 1，题名、六位作者及DOI一致，中文摘要与原文方法和两构型比较对应。
- 方法：PDF file page 3 §2.1、Fig.1，八自由度为平台六刚体自由度+塔架两弯曲模态；Kriging与NSGA-II见PDF file page 7 §3.3–3.4及9 §4.4。
- 气动前置：PDF file page 4 §2.2，以OpenFAST预计算固定塔顶转子载荷和气动阻尼表，并进行控制器调谐；迭代可读表，不代表方法无翼型/控制器前置依赖。
- 数据：PDF file page 5 §3.1–3.2，2007–2018缅因湾观测经Nataf扩展25年；PDF file page 6 §3.2.2用MDA选择1000样本，不是连续25年实测。
- 优化：PDF file page 7–9 §4.1–4.3，10 MW、130 m水深、两类均钢结构；吃水/柱半径/柱距/线长/链径为五独立变量，锚点半径从属。制造成本不是全生命周期成本，损伤<1.5为宽松早期约束。
- SMD/LMD：PDF file page 12–13 §5.4.1及15 Fig.19。SMD结果的疲劳按长期模型重算；高成本塔底前沿接近、低成本LMD改善，导缆孔改善主要在高成本区，不能称全部指标和成本点均改善。
- 两构型：PDF file page 14 §5.4.2、PDF file page 17 Fig.23、PDF file page 19结论，同成本方形塔底疲劳大多低30%–50%；部分Y形系泊疲劳更低，涉及二阶慢漂、较粗链径及成本代价。
- OO-Star归属纠错：PDF file page 15 §5.4.2，约900万欧元成本的改进为Y形设计，DFrld/DTwrBs=0.119/0.136，较参考点低4.8%/32%，不是方形设计。参考比较模型改为钢平台、调整系泊并去除集中配重，见PDF file page 9 §5.1。
- 误差：PDF file page 10–11 §5.1.2，运动响应标准差多数工况约10%，部分高于额定风速达10%–25%，涉及气动阻尼和控制动态；强海况线性黏性阻力还会影响张力。PDF file page 17结论更概括，不能当作所有长期指标误差保证。
- 强度边界：PDF file page 7–9 §4.1–4.3及19 §6末段，未校核船体强度，内部加强钢材和成本可能低估。
- 图像：Fig.1/7/19/23/25分别位于PDF file page 3/8/15/17/18。图19旧裁剪残留英文图题、图23残留页脚，已忠实重新提取、检查图例/坐标完整。
- 公式指标：没有展示编号公式；TC见PDF file page 8 Eq.(17)，三目标见PDF file page 9 Eq.(18)，损伤见PDF file page 7 §3.4。

## 当前事实修正与完整度

### 2026-10-05 原文审校与完整度结论

- 原文共20页，已完整读审；本轮重新校验存续PDF并检查相关源图、公式、表格，重新建立既有两渠道改稿，不声称找回此前未保留的输出字节
- 当前事实与修改依据见上方已更新的现行证据段；RTD和公众号分别与原文对照，没有相互转换覆盖
- 原文覆盖清单：§1–6；Fig.1–27；Table1–5；Eq.(1)–(18)；45条参考文献，无附录
- 现有RTD为选读简介：五幅选图，无完整编号公式/表格/参考文献；尚未逐段保留全文、全部图表公式、文内引用和参考文献链，顶部也缺全文精解要求的精简版链接行
- 因此全文完整度未完成；原文全页已读、选图已核对不等于RTD全文精解完成
- 原文数值模拟未重新运行；未进行后台上传、更新或发布；新的离线检查结果以本轮执行记录为准

### 2026-10-05 离线验证（历史记录）

- 公共安全扫描、产物检查、原生图片/图题/链接目标检查及差异空白检查通过
- 本篇官方工具无提交dry-run通过，使用MathJax SVG；未执行凭据读取、上传或后台更新
- Sphinx标准总构建由整批统一执行；本子批次未重复启动共享构建，微信后台手机预览未执行


## 2026-10-06 全文译稿与原图校准记录

### 本轮范围与审核状态

- RTD直接依据获授权的出版版PDF逐段重建，不从公众号导读转换；保留稳定锚点和页面路径
- 已制备论文信息、作者与单位上标对应、4条研究亮点、完整摘要和关键词、§1–6全文、Eq.(1)–(18)、Fig.1–27、Table1–5及45条可回链参考文献；源文无独立符号表、无附录，符号定义均保留在原公式附近
- 五张表为可编辑中文表格；没有将表格或公式作为截图替代文本
- 结论后直接为参考文献及完整引用；按精解规范排除出版声明性尾注
- 顶部精简版链接行之后立即为既有封面；封面字节未修改
- 本轮为作者侧完成和自查，尚需独立全文审查；`rtd_page_checked`继续为false，不改注册表状态，不把诊断构建当成整站发布验收
- 原文数值模拟未重新运行；未执行公众号凭据访问、上传、后台草稿更新或发布

### 原文差异与事实边界

- PDF file page 2，§2称模型基于QuLAF并引用[11]，但参考文献中QuLAF对应[9]、[11]为多目标优化论文；译文保留原引用
- PDF file page 4，§2.2为9个桨距控制器，0.130–0.250 rad/s、间隔0.015 rad/s；PDF file page 11 §5.2及PDF file page 14 Table4却使用13个转子闭环特征频率。两处均原样保留，未擅改计算预算
- PDF file page 4 Eq.(9)写φX，PDF file page 5相位说明写φH；两种写法保留并明确说明
- PDF file page 7 Eq.(14)使用ψ的转置，紧随解释又称ψ为1×M向量；公式及原始维度叙述均保留
- PDF file page 9 Table2的涂装价格单位为$/m²，其余为€；没有自行换汇或修改成本式
- PDF file page 10 Table3中的周期与误差逐格保留，未依据显示的四舍五入周期重新计算或修正误差符号
- PDF file page 11 §5.1.2工况的Tp=7.80单位原文印为m；译文保留并指出其在其他位置定义为波峰周期
- PDF file page 15 §5.4.2及§5.5将参考设计和比较个体误引为Fig.20/22，实际标记位于PDF file page 17 Fig.21/23；原图号及区别均在译文中保留
- PDF file page 12–13与PDF file page 15 Fig.19：SMD最优样本的疲劳经长期模型重算后比较；高成本区塔底前沿近似重合，低成本LMD改善约10%，导缆孔改善则主要在高成本区；未扩大为所有指标均改善
- PDF file page 9 §5.1与PDF file page 15 §5.4.2：OO-Star比较对象使用钢制平台、调整系泊长度并取消集中配重；约900万欧元、0.119/0.136和4.8%/32%的改善属于Y形设计
- PDF file page 17–19结论中“无需翼型和控制器相关信息”沿原文保留；其方法边界由PDF file page 4 §2.2和PDF file page 11 §5.1.2明确：仍需预先生成或由制造商提供固定基础载荷与气动阻尼查找表，不能理解为完全没有气动及控制前置输入
- PDF file page 19末段：未校核船体强度，可能低估内部加强钢材；早期损伤<1.5不是最终设计验收标准；本算例的构型排序未外推为所有海域和平台的普遍结论

### 图像来源、裁剪和源图限制

- 所有图均由同一获授权PDF提取；完整嵌入图使用原始像素，含矢量或外置文字/面板标记的图采用300 dpi完整页面区域裁剪，没有AI重绘
- Fig.18与Fig.21的嵌入图不包含原文a/b设计域标签，故使用页面裁剪保留全部标签；Fig.1、2、3、4、7、9、20等同样保留完整矢量/文字叠加层
- 27幅最终PNG均已逐张与源页面比较，检查分图、坐标、刻度、图例、图内标记及边缘；所有裁剪排除相邻正文、英文总图题和页眉页脚
- PDF file page 12 Fig.11顶部第一/第四子图的最右刻度及机舱横向加速度单位存在源PDF内部截断；扩大裁剪无效，PyMuPDF和Poppler均复现。保留源图，并在中文图注补足可确认的指标和单位；不声称源图全部标签清晰
- PDF file page 13 Fig.13原始图例存在白色遮盖，两个渲染器均复现；曲线和线型完整，中文说明给出“实线非线性、虚线线性”。未重绘或猜测被遮盖像素
- 既有公众号选图路径Fig.1/7/19/23/25已以同一校准结果更新；只进行JPEG编码适配，图形与裁剪边界一致，封面未变

| 图号 | PDF file page | 提取方式 | 像素 | 公开素材SHA-256 |
|---|---:|---|---|---|
| 1 | 3 | 完整PDF区域300 dpi | 1951×1097 | `5598849efab304e7be965b898a5dc338573b02ec8fd3b7cbe869d9cf90ba36d0` |
| 2 | 4 | 完整PDF区域300 dpi | 1630×534 | `c883779f92b88186159e69413d9e639dc508d415164bfa48f84c397dcc4af68b` |
| 3 | 5 | 完整PDF区域300 dpi | 1689×555 | `ef0bfb7c46140ce829d640436cfb33d75f1eaa6aa6c01bc6d29e1f863fcbf05d` |
| 4 | 6 | 完整PDF区域300 dpi | 1951×917 | `0d5e6bff19c8c1e51ea4bf4932a2c8cb047f22b63ded2bcb64bb9db91d67da2f` |
| 5 | 6 | 原始嵌入像素 | 1028×882 | `2ec8bc7e49dff3bedbf089031adcd645844cd3d0bef7fcd6addee151f628afa0` |
| 6 | 6 | 原始嵌入像素 | 1675×496 | `0a4a5ee75f71b4b47f64bb830e0e77386253fe324cc5548739d2957648681584` |
| 7 | 8 | 完整PDF区域300 dpi | 1651×1050 | `890b6cc8c4d0ef869f7b2d3ce5ccc1a1b932160c14a4e2c843dec4fdf809abb2` |
| 8 | 8 | 完整PDF区域300 dpi | 1055×551 | `dd4907865af57c47646f8c4ffa3732f4ebe2ffacb7c9751555430701aa605d9c` |
| 9 | 10 | 完整PDF区域300 dpi | 1864×1926 | `dd39a87330ce1d6ac2c87be0817d9f29439f00d2f76c912c0ef90c6341f2dbab` |
| 10 | 11 | 完整PDF区域300 dpi | 1784×826 | `9a57f7c41080ce8a6b9a5c52396c582b00df0ec53e6c4cee92d20f478f3c9e96` |
| 11 | 12 | 完整PDF区域300 dpi | 2021×955 | `52869a0333516cdecd00423483467270565bf4f415293b8ed18c166e73fb7faa` |
| 12 | 12 | 完整PDF区域300 dpi | 1938×905 | `fe659057833c37f3b442db77fc2e8f3e18dfbd7866d6873abe07f3893982f6e7` |
| 13 | 13 | 完整PDF区域300 dpi | 1042×621 | `7568f35f4887a2bf2f5e1791a8813f1907a7798b32b9978e72d99876c0029d0b` |
| 14 | 13 | 完整PDF区域300 dpi | 1734×980 | `6dabc7f6ca2f6b7fa4aea57d9bd2dad37d2be975c308f216e39d54bec3b561fe` |
| 15 | 14 | 完整PDF区域300 dpi | 1947×547 | `d44b5b1ea235cc43f2db3c68ee3e13a84f94774f95dbc60817c1a8b79e7c7cdb` |
| 16 | 14 | 完整PDF区域300 dpi | 1930×417 | `e8b2ca83724f126a04c4c8d467c3ba894d0792b7d57e2c1e4d8c788ed48e1106` |
| 17 | 14 | 完整PDF区域300 dpi | 1042×805 | `5a4de669fb29960f572bdea9e5422d7007538e0b17d32c48d664f02e74d8e1bc` |
| 18 | 15 | 完整PDF区域300 dpi | 2155×1072 | `d5870ba4ec809413b0c431520a657cafe37a685d572e7cc6356578d91773bf1d` |
| 19 | 15 | 原始嵌入像素 | 2139×483 | `f31fdc15047861b51d25ec4e2829f2317289ad75cf349e0fa2c126780862661a` |
| 20 | 16 | 完整PDF区域300 dpi | 1521×1839 | `441be97539db96a1feb8394486896862c92bcd5858d9fca354f5b9aee6a5ea1a` |
| 21 | 17 | 完整PDF区域300 dpi | 2180×1072 | `03c863e2cdde86d45bcd764ee3bc62facf7f414a2c3976720aa2659ac1a37fb2` |
| 22 | 17 | 完整PDF区域300 dpi | 921×684 | `ba6b4826a644ef13380c308074171e1ffc25cf265267752b96a2466983d767cd` |
| 23 | 17 | 原始嵌入像素 | 2129×475 | `8ded3af3010336e35e3b5f27431501ea1f3e69d84dfc778c1321296f838ce120` |
| 24 | 18 | 原始嵌入像素 | 1829×703 | `27f751b226d40ef2e065c68e64271df54b1699dc36b2be7b644ccc40143196c8` |
| 25 | 18 | 完整PDF区域300 dpi | 2134×1138 | `d24cab6bcd6652132f87a8d957810a73e198b1c322380c7a1557d04be589096d` |
| 26 | 19 | 完整PDF区域300 dpi | 1076×772 | `b5334e329961f88cffddb5bd95cd593908ba9c116245c2f9ebf90978e91089d6` |
| 27 | 19 | 完整PDF区域300 dpi | 1084×1172 | `49ab63ca35462d950a94d4cdb11aa89c022f84e3b5bda37886b1231580965a16` |

### 本轮检查

- 通过：`python3 scripts/check-public-safe-content.py`
- 通过：`python3 tools/publications/artifacts.py --check`，产物同步问题列表为空
- 通过：本篇RST、review和素材范围的`git diff --check`
- 通过：隔离的Sphinx单篇HTML诊断构建，`-W --keep-going -E`，包括全部图、可编辑表格、公式及引用解析，最终零警告
- 未运行：本子任务不启动共享整站构建；完整`./scripts/check-docs.sh`与部署检查由整批发布阶段执行
- 未验收：独立逐句复核、整站发布验收与微信后台手机预览；不因本地诊断通过而提升相关状态


## 2026-10-06 独立源文与原图复核结论

- 逐段逐句源文对照、全部编号公式、表格数值、文内引用与参考文献、逐张最终图片均通过独立复核；没有残余正文遗漏。
- 原生图像/指定源区域渲染均与最终图逐像素对应；原文自身的科学与排版差异保留，不作为已解决的作者勘误。
- 内联数学与引用角色已检查实际生成 HTML，不以无警告构建替代显示检查；不改变公式和引用内容。
- 共 89 个正文单元、18 个公式、5 张表、27 幅图、45 条参考文献和 59 处展开引用。平均纵摇约束的上横线、单位 d 原印 Shanxi 及内联角色边界已修复并复核。Fig. 11/13 的原文件内部裁切/遮盖依然明确记录，仅补充同文可证实的单位和线型说明。
- 无原文附录。后台公众号预览、上传与发布均未执行；整站标准构建和线上结果由本批对应提交验证。
