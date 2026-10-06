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

## 当前范围与状态

- 2026-10-06：RTD 已由历史选择性导读替换为独立全文中文译稿，直接依据原论文完成，不由公众号正文转换
- 本轮作者自检覆盖 24 页 PDF、77 个摘要／正文／公式解释自然段、34 幅图、6 张可编辑中文表、式（1）–（21）和 68 条参考文献；独立来源复核尚未完成，因此仍保留 `rtd_page_checked: false`
- 公众号正文及封面保持原样；已有 5 张科学选图与全文图统一为经核准的原始完整图像对象。公众号后台手机预览未执行，后台草稿没有更新
- 不将本轮自检、诊断 HTML 构建或公式离线渲染称为独立审稿、标准发布检查或微信手机验收

## 正文与公开素材

- 公众号正文：`wechat/articles/draft-public-safe/ref-zhao2025-SCS.md`
- RTD 正文：`docs/source/paper-notes/ref-zhao2025-SCS.rst`
- 封面：`wechat/assets/public-safe/ref-zhao2025-SCS/cover-wechat-900x383-v2.png`
- 完整科学图：`wechat/assets/public-safe/ref-zhao2025-SCS/fig01.png` 至 `fig34.png`
- 原公众号选图别名：`fig-01-workflow.png`、`fig-14-dense-point-cloud.png`、`fig-18-geometry-reconstruction.png`、`fig-25-velocity-magnitude.png`、`fig-34-webgis-interpolation.png`，分别与完整图 1、14、18、25、34 的像素及文件内容一致

## 源文件获取记录

- DOI：https://doi.org/10.1016/j.scs.2025.106237
- 来源：用户授权的期刊出版版 PDF；题名、五名作者、期刊卷号及文章号、DOI 均与原文首页一致
- 文件物理页数：24；全文科学正文及图表在 PDF file pages 1–22，参考文献在 PDF file pages 23–24
- 当前核验副本 SHA-256：`c1dceebf21a54b93e7595851052191a2198f508bb4d0a55e1dc8eccb36765b08`
- 当前文件校验值与已有授权来源记录的校验值一致；本次没有再次取得历史原始文件字节，不额外作独立原件字节比对声明
- 采用已存在的授权出版版副本；本次未重新查询 Zotero 附件、未调用 Zotero 下载接口、未从公开网页另行下载 PDF
- 源 PDF、全文提取、逐页渲染、逐段覆盖表、图像原始定位及像素核验材料保留于非公开工作存储；公开文件仅保留允许公开的中文译稿、核验摘要和授权科学图
- 摘要、正文证据和全部图像均来自同一核验 PDF；沿用既有作者论文图片使用授权，不改变其使用范围

## 关键事实证据定位记录

- PDF file page 1：题名、作者及单位 a／b／c、收稿／修回／录用／在线日期；通讯星号仅属于 Xiaolu Wang。完整单位、通讯邮箱及原文 ORCID 已保留
- PDF file pages 1–2，Section 1：完整研究背景与文献链；全文保留原作者—年份引文，每一条都链接至文末对应参考文献
- PDF file pages 2–6，Sections 2.1–2.2：场景划分、SfM／二维关键点映射、GaussianPro、自适应加密、损失项、120 m 建筑、1560 张图、1k 降采样、12,000 次迭代与 150 次加密间隔
- PDF file pages 6–8，Section 2.3：HISA、VDVI、地形／植被／建筑提取、RANSAC／DBSCAN、形态学及 Canny、RDP、轮廓规则化和棱柱模型生成，全部逐段保留
- PDF file pages 9–11，Section 3.1、Tables 1–2：仅比较五栋代表建筑。B4 的 Acc 本方法为 0.2168 m，COLMAP 为 0.1379 m；完整性、召回率、黑色屋顶、植被遮挡、曝光及重叠率的负面结果和条件均保留
- PDF file pages 11–12，Sections 3.2–3.4：LoD2／LoD2.5、立面细节限制、显存方案 A／B、内存需求、SfM 数小时至数天、复杂建筑及密集城中村退化情况，均完整译入
- PDF file pages 12–15，Section 4.1：加密区及计算域距离、790／1680／3790 万网格、1.44／1.2／1 m 分辨率、SST RANS、冠层动量及湍流源项、32 点 GCI；没有把植被写成未纳入研究
- PDF file page 15，Table 3：基础网格 U／p／k／ε 的 GCI 为 3.51／3.76／4.89／4.70%；粗网格相应结果为 5.20／5.57／7.24／6.96%，明确区分基础网格指标和总物理误差
- PDF file pages 16–19，Section 4.2、Tables 4–6：POT／Weibull、九个风向、1:400 模型、2 m 行人高度、10 m 参考高度、5 m/s 参考风速及 30 个测点；25／28 为 III 类、23 为 IV 类，其余 I／II 类
- PDF file pages 19–22，Sections 4.3–5：30°、10 m、约 711,000 条点云、五字段数据库、100 个半变异函数及大小 100 的子集、GeoServer／Cesium／WMS 工作流、完整结论与局限

## 全文覆盖自检

- 首页元数据、作者单位与通讯脚注、摘要和五个关键词：已翻译
- 1 引言：7 段全部保留
- 2 方法：方法总述，2.1.1／2.1.2、2.2.1／2.2.2、2.3.1／2.3.2／2.3.3 全部保留；公式前后解释独立保留
- 3 结果与讨论：3.1／3.2／3.3／3.4 全部保留
- 4 应用：4.1.1／4.1.2／4.1.3、4.2 总述及 4.2.1–4.2.4、4.3 全部保留
- 5 结论与未来工作：原文两段全部保留；结论之后直接进入参考文献
- 表格：Tables 1–6 均以 RST list-table 重建，逐项核对表头、单位、全部行列与数值；没有使用表格截图替代可编辑表格
- 公式：式（1）–（21）全部保留为可编辑数学文本，另保留行内相对误差、观测精度阶及全部符号解释，编号统一为 `\qquad (N)`
- 参考文献：68 条完整保留原顺序及书目信息；原 PDF 的 65 条 RefHub 链接和 3 条 arXiv 链接均保留，100 处正文／表格／译注引文链接覆盖全部 68 条文献
- 附录、科学符号表、独立缩写表：原文均无，未新增；CRediT、利益冲突、致谢、数据可用性等声明性尾部按项目规则不进入公开译文
- 顶部精简版微信链接行之后紧接原封面；末尾保留“完整引用”和 Publications 对应条目回链
- 未发现遗漏占位符、私有路径、原稿下载链接、凭据或 `\tag{}`；未新增营销式导读替代段落

## 全部科学图校准记录

本轮逐页查看原 PDF，并逐幅核对最终图像的完整分图、坐标轴、图例、色标、标记和边界。34 幅图均可直接使用 PDF 内嵌的完整原始图像对象；逐个验证最终 PNG 与对应内嵌对象的 RGB 像素完全一致，且对象边界内没有遗漏的 PDF 外置文字或矢量覆盖。不以自动图号匹配替代视觉检查，不保留邻接正文或原英文图题污染，不重绘科学内容，也不以放大插值冒充更高源清晰度。

- PDF file page 3：Fig. 1
- PDF file page 4：Figs. 2–3
- PDF file page 5：Fig. 4
- PDF file page 6：Figs. 5–6
- PDF file page 7：Figs. 7–8
- PDF file page 8：Fig. 9
- PDF file page 9：Figs. 10–11
- PDF file page 10：Figs. 12–13
- PDF file page 11：Fig. 14
- PDF file page 12：Fig. 15
- PDF file page 13：Figs. 16–17
- PDF file page 14：Figs. 18–19
- PDF file page 15：Figs. 20–21，分别核实复杂屋顶四面板及城中村两面板，未按内嵌对象的排列顺序误配
- PDF file page 16：Fig. 22
- PDF file page 17：Fig. 23，保留全部 (a)–(d) 分图，包括两张近壁网格放大图
- PDF file page 18：Figs. 24–26，分别核实植被棱柱、速度图、湍动能图，没有互换；后两幅完整保留坐标及色标
- PDF file page 19：Figs. 27–28
- PDF file page 20：Figs. 29–30
- PDF file page 21：Figs. 31–32
- PDF file page 22：Figs. 33–34

图 14 的 5×4 排列、图 18 的 (a)–(i)、图 29 和图 31 的各九个分图、图 34 的整体地图／局部三维视图／连线／图例均已逐项核对。图题与必要图内文字提供中文，保留原图科学内容和原图号。封面没有重新生成或改动。

## 原文疑点及处理

1. PDF file page 1 摘要速度为 3–5 倍，PDF file page 22 结论为 2–3 倍。两处均忠实译出，译注说明不能统一成相同基准的端到端加速保证
2. PDF file page 7 的式（11）–（13）均缺少分段条件；保留原排版和两行表达式，未自行补出判断条件
3. PDF file page 7 Fig. 7 的屋顶高度分段标为 2 m，但同页 Section 2.3.2 文字写 1.5 m；保留差异并在图注指出
4. PDF file page 11 Table 2 的 COLMAP／NeuDA 引文与文末书目题名存在对应疑点；保留原引文，并在表后标注
5. PDF file page 12 Section 3.3 写 1800 万网格，同页 Section 4.1.1 及 PDF file page 15 Table 3 写基础网格 1680 万；两处均保留。设备清单与结果对 RTX 2080ti 的提及也按原文保留
6. PDF file page 12 同时报告连续尺度比 1.3 与 1.44／1.2／1 m 分辨率，不能静默改算；译注指出相邻分辨率之比是 1.2
7. PDF file page 15 把较小误差表述为细／粗网格比较，PDF file page 19 Fig. 27(b) 实为细／基础网格；正文忠实保留原句并紧接差异说明
8. PDF file page 13 文字用“湍流强度”，PDF file page 15 Table 3 列 k；保留文字和表头差别
9. PDF file page 16 式（20）解释将 θ 称位置参数，同时用作风向角，未解释 μθ；Table 5 的两行 kθ 为 0。原式及数据保留，注明复现需核实
10. PDF file page 21 并列使用经验贝叶斯克里金和 RBF-M，引用题名为径向基函数方法；保留两种名称，不擅自认定等价
11. 植被点、简化棱柱和冠层源项已经纳入原研究；几何细节仍集中在建筑，不能把结论中的局限解释为从未考虑植被

## 本轮检查结果

- 通过：公开内容安全检查、目标文件 `git diff --check`、publication artifacts 检查
- 通过：实际项目 Sphinx HTML 的 `-W --keep-going` 诊断构建，仅关闭已知受环境影响的 sitemap 扩展；不是标准发布门禁
- 通过：实际生成 HTML 中 34 个科学 figure、35 张图片（含封面）和 6 张表；所有本地图片存在、全部页内链接有目标、68 条参考文献均有引文链接、Publications 回链正确，无裸露 RST role 标记
- 通过：从实际 HTML 提取的 131 个数学表达式，包括 21 个独立编号公式，全部经 MathJax SVG 渲染，未出现 MathJax 错误节点
- 未通过标准整站门禁：初次运行受临时目录空间不足影响；迁移验证输出后，标准 `check-docs.sh` 成功安装依赖并通过安全检查，但在共享 registry 的既有过期 verification 与生成视图不同步处停止，未进入其后 unittest／标准 Sphinx 阶段。本任务未改共享 registry
- 单独运行 unittest：166 项中 163 项通过、3 项失败，失败均为共享 registry 过期验证／生成视图的现有一致性问题；未通过完整单元测试门禁
- 单独运行保留 sitemap 的标准 Sphinx：在 sitemap 的 builder-inited 处理程序中因当前执行环境限制而失败；诊断构建只为隔离这一阻塞，不替代标准检查
- 未执行：独立来源审稿、微信后台手机预览、远端部署验证、提交、推送或发布


## 2026-10-06 独立全文与逐图复核通过

- 全部 24 页、77 个原文自然段、34 幅完整源图、6 张可编辑表、21 个编号公式、68 条参考文献及原链接经过独立复核。
- 逐幅对照源 PDF 完整原页和原生图像像素，确认全部坐标、图例、色标、分图及多图页映射完整，封面未改。
- 最终 HTML 共 100 处引文链接，对应 97 处原文引用及 3 处明确标注的译注引用；未删减原引用链。
- 仅修复原文通讯邮箱后紧接中文括号造成的自动链接截断，地址字面值保持不变；诊断 Sphinx、链接/图像/角色检查及 131 项 MathJax 渲染通过。
- 本结论取代上文待独立全文复核状态；标准发布门禁由最终批次验证，公众号后台状态未变。
