---
publication_ref: ref-zhao2023-GYJZ
body_images_upload_approved: true
wechat_cover_image: wechat/assets/public-safe/ref-zhao2023-GYJZ/cover-wechat-900x383-20261014-v5.png
rtd_cover_image: wechat/assets/public-safe/ref-zhao2023-GYJZ/cover-wechat-900x383-20261014-v5.png
research_family: 工程结构抗风
subdirection: 结构抗风
publication_mode: first_publish
wechat_status: drafting
wechat_author: Zhao Zihan
source_checked: true
copyright_checked: true
public_safety_checked: false
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
wechat_backend_preview_checked: false
rtd_page_checked: false
---

# 输电塔首次超越易损性：双渠道制作记录

## 当前范围与状态

独立RTD完整正文整理、独立公众号导读、8幅原图和8张可编辑表已制作。来源为11页网络首发PDF，其中首发说明1页、论文正文及引用10页。作者自查及非撰稿者的独立科学审查均已完成；科学范围通过，不是封面、HTML排版、部署或公众号后台验收。真实封面现已独立检查并绑定，官方离线渲染通过；最终完整网站/浏览器及手机后台仍待。

## 源文件获取记录

- 使用本轮已授权的团队论文附件；当前可读PDF与既有清单记录的源SHA相同。精确哈希、附件标识、原始文本和页面图保存在私有来源与审计存储。
- 版本：期刊网络首发稿；首页给出题名、五位作者及2023-02-27首发日期；第二页给出10:39:45首发时间与知网首发地址。其余10页连续为本篇论文。
- 没有优先可用的另一版作者终稿，未降级到摘要写全文。未访问Zotero Desktop、未请求Web API `/file`，未下载网页PDF。
- 原稿未列DOI，也没有作者通讯星号或通讯说明。现有书目字段中的DOI样式字符串无本稿支持，正文不用它；无独立来源时不补通讯标记。
- 团队作者原图依本轮授权复用；先执行pdfimages提取，向量/混合图再裁切原页。没有用生成图代替论文图，没有编辑水印或科学内容。
- 外部只读元数据交叉检查：作者[哈尔滨工业大学主页](https://homepage.hit.edu.cn/lichao)列有该篇、五作者及2023网络首发页码，但未给DOI；该结果不替代完整PDF。

## 工程叙事证据卡

塔身抗风能力随限值、不确定性和导线耦合改变 → 推覆确定三档塔顶位移角，比较单塔LHS与线塔动力可靠性 → 用置信度易损性曲线和HCLPF作同口径对照 → 本算例支持方法比较，但原稿保守性措辞与表值有差异，不作普遍安全保证。

## 关键事实证据定位记录

- PDF file pages 1–2：题名、作者、单位、首发版本/日期，中英文摘要及关键词。中文摘要保持原意与原句，英文摘要在原位置后独立译为中文。
- PDF file pages 2–3，Section 0：风灾背景、定性/定量方法及首次超越研究目的；完整保留引用[1]–[10]。
- PDF file page 3，Section 1，Eqs.1–2：功能函数与联合概率积分；page4 Fig.1流程及连接部分不失效的研究限定。
- PDF file page 4，Section2.1，Fig.2：大亚湾500kV，塔高57m，档距250m，设计风速38m/s，BEAM188/LINK8/LINK10及三塔两线简化。
- PDF file page 5，Table1：两种导地线8列参数；Eqs.3–4：Kaimal谱、Davenport相干、C=8、十个竖向点和16m水平间距、忽略风压脉动平方项。
- PDF file pages5–6，Section2.3，Table2、Figs.3–5：45°/90°推覆、90°不利方向、Y0/Y1/Y2=1/200、1/150、1/100；构件黑点与4组风速、剪力均保留。
- PDF file pages6–7，Section3.1，Tables3–5，Eq.5：LHS均值趋稳停止；材料/几何/荷载分布，K–S显著性0.05，12个风速下对数均值/标准差；page8 Fig.6。
- PDF file page8，Section3.2，Eqs.6–8：修正正态法、误差函数与超越次数、修正Vanmarcke法；包括sigma的一阶/二阶导数下标及根号范围，依据放大原页转写。
- PDF file pages8–9，Section3.3，Eqs.9–10：两种不确定性、置信度Q、betaU=0.12、HCLPF为95%置信曲线上的5%失效概率对应风速。
- PDF file page9，Tables6–7：8个单塔风速×3限值、5个线塔风速×2方法×3限值全部转为窄表，数值未变；方法1为修正正态，方法2为修正Vanmarcke。
- PDF file page10，Figs.7–8与Table8：两组各3子图，5/50/95%置信曲线；9个HCLPF数值均完整保留。
- PDF file page10，Section4：三条结论和灾后调查不足/其他塔型待讨论的末段；pages10–11全部20条引用，中英文并列保留。

## 源内差异及复现边界

1. Table1中文题为“各测点的统计参数汇总设置”，实际为导地线参数；Table3中英文题为M0–M3平均风荷载对比，实际为8个不确定参数分布。公开RTD均保留原题并说明，未编造测点。
2. Table2中Y1为2%及3–4主材，Y2为20%及8–10主材，两组不能反推统一主材总数。照录并公开说明，不擅改比例。
3. Eq.3的n与Eq.7的n语境不同，原段未展开Monin坐标、风剖面指数、全部时程参数；Eq.8未文字定义二阶导数标准差。未补写完整可复现设置。
4. Section3.3写图7–12，但本版仅图1–8，图7/8各三子图。未虚构图9–12。
5. Table7在48m/s、Y1、方法2处是8.88E-02，不是8.88E-03。保留原指数并标明邻值比例差异。
6. Table8的单塔HCLPF低于线塔；Section3.3却称单塔“偏于不安全”，结论(2)称线塔“趋于保守”。Tables6–7共同50m/s处单塔3限值概率都更大。RTD和公众号并列披露，禁止摘单句推出普遍保守性结论。
7. “不超过2%”“12%以内”是原文对本算例HCLPF风速的对比，不是全风速/全塔型失效概率误差界。没有全套原始样本，不把内容校核冒充独立重算。
8. 参考文献[19]题为地震易损性方法，正文称风灾分析模型；[1]中英文页码不同；[20]中文期刊名写“中国机电工程学报”。均保留并标注。
9. 原稿未量化耗时或加速比；没有把塔顶位移角超限写成全部倒塔/断线事件联合概率，也没有将38m/s设计风速与HCLPF风速混为同一设计量。

## 全文覆盖与原图自查

- 原节0、1、2.1–2.3、3.1–3.3、4全部按原顺序逐段保留，10个编号公式均可编辑，20引用齐全，无科学附录或独立符号表。
- 英文摘要在中文摘要后原位置译出；基金、页眉页脚及网络出版流程说明不是科学正文，不公开复制。
- 表1–8完整；表5–7只变换行列布局便于窄屏，全部条件和值对应。
- 图1/3/5/6为向量图；图2为多图加向量尺寸/坐标；图4为位图加向量荷载/风速。采用原页裁切保留全部部件、坐标、图例、黑点与标签；源中已有淡色标记保留。
- 图7/8直接采用pdfimages原生像素，不重采样；不把覆盖在PDF页面上的文字当成需要人为修图的对象。
- 8幅最终资产逐张打开与源页核对，留白和关键内容完整。公众号选图3/6/7，各有独立图题与读图句。
- 公众号含忠实摘要、研究问题与解决思路、四个具体小节与限制；AI声明在末尾仅一次。

## 本轮正文图上传许可

2026-10-14本轮明确要求完成所选27篇双渠道内容并制作公众号草稿，许可范围包括这些论文原图用于对应草稿的必要上传。body_images_upload_approved仅表示许可，不代表实际已上传、已建草稿、已审科学内容或后台验收。正式发表不在本轮自动执行范围，实际API由统一交付流程执行。

## 封面简报

详见同篇公开素材目录的cover-brief.md。文字已按本轮批量授权拟定，尚待独立科学复核和实际生成；真实封面形成后才执行完整渲染门槛。

## 2026-10-14 独立科学内容审核通过

非本篇撰稿者独立核对全部11页来源（首发说明1页、科学正文及引用10页）、41个科学段落对应单元、10编号公式、8表全部数值、8幅最终原图、20参考文献及公众号全文。公式根号/上下标、合并表格分布栏、源内数值与保守性措辞矛盾均逐项复验。规范顶部锚点、论文精解题名和待发布引导已纳入此哈希。科学通过不代表原模型独立重算，也不代表封面、HTML公式图像排版、全站构建、部署、微信后台或手机浅深色验收。

- `docs/source/paper-notes/ref-zhao2023-GYJZ.rst`：SHA-256 `c50a99c484ea08081bfd0ae5d56209a80cfe9cbd4224df81616f4e262da03258`。
- `wechat/articles/draft-public-safe/ref-zhao2023-GYJZ.md`：SHA-256 `f1edde722c6662609180d0c4c7e87c3ad5ddea0c2dd281e5338e8f3a1bd1ce60`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig01.png`：SHA-256 `98b2fe159f6daa984a58745be1633698d0c96cd62d04778d1b535ce52905bd59`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig02.png`：SHA-256 `b47d23f21c20f5cd2128714e1d105283765878e12c44c90165dee0acc0230027`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig03.png`：SHA-256 `97078c428f9bc66cfb0f2a04e0ae702e3413a1ee15c49a907e8681e603f3d795`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig04.png`：SHA-256 `541f0df5591ac076cc3db781d2304164acecac032bd53a49756d5c11bafe624b`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig05.png`：SHA-256 `b18d4e519f93209c5822d793e83f45f50dced8d0e93e7c779ee857d364b504e0`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig06.png`：SHA-256 `04c596b8505195ae9d3b687b66a2bcee3229a2d91e98597f62f5e3ae073d7ebd`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig07.png`：SHA-256 `26d54b7f3c70b7f3751689356e8689a3cc8bbc59d4e6f4d35bc9ad4c5350b94d`。
- `wechat/assets/public-safe/ref-zhao2023-GYJZ/fig08.png`：SHA-256 `830d7d56c0e7af8293f85666a222f7225e9a50463968128536fc5c5d63dcc534`。

## 2026-10-14 第四批真实封面绑定与科学等价

沿用上文独立科学内容审查范围，不重作或扩大原PDF审核。最终封面 `wechat/assets/public-safe/ref-zhao2023-GYJZ/cover-wechat-900x383-20261014-v5.png` SHA-256 `a527c5659b870596ceea8defab5b54a7482b8ac6de9c3763940837ee581cfcab` 已逐张独立核对，当前整合亦重新打开实际900×383PNG核对。工程图仅作概念示意；边界与不表达的几何/效果见同篇cover-brief，不将本地封面审阅当成微信手机验收。

本次仅在RTD顶部加入封面image指令，并绑定主review的双渠道封面路径。加图前RST SHA-256 `c50a99c484ea08081bfd0ae5d56209a80cfe9cbd4224df81616f4e262da03258`；新增指令块逆向移除后逐字节恢复原稿。公众号正文、作者、摘要、科学原图和数据完全未改，AI声明仍只在文末一次。正式排版、标准整站构建、实际浏览器、后台草稿与手机浅/深色验收另行记录；不提前标记verified或发布。

## 2026-10-14 第四批离线渲染与冻结边界

官方 preflight、dry-run 与 academic-clean / MathJax SVG 渲染通过。本篇公众号正文含3张原图、0个行内SVG公式和0个显示公式；图像嵌入和SVG几何/currentColor静态检查通过。390px浅/深色容器对照仅为离线诊断，不证明真实微信手机行为。

六页最小RST语法测试以正常mathjax扩展、warnings-as-errors运行通过，无可见math/ref角色泄漏或problematic/system-message节点；该测试不替代标准全站构建。RTD含9张图（首张为真实封面）、10个显示数学块和8个HTML表；表格数量包括论文符号表等编辑呈现，不改原论文覆盖数。

本篇仅有顶部封面块及1处行内math括号边界ASCII空格、0个标题下划线字符的版式增量。逆向删除这些精确插入即恢复已科学审查RST原字节；公式LaTeX内容、表值、作者、摘要、全部原图及公众号MD逐字节不变。当前RST SHA-256为 `803f48486e591367b9702d79741d9d7a13904d5c64ba4ba7499400ec137fb11c`。实际浏览器、标准全站构建、部署及微信后台手机验收另行记录，仍待最终接入验收，不标verified、ready_to_publish或published。
