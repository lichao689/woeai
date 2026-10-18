---
publication_ref: ref-zhao2021-EFM
doi: 10.1007/s10652-021-09796-4
research_family: 工程结构抗风
subdirection: 数值风洞
publication_mode: first_publish
wechat_status: drafting
wechat_author: Zhao Zihan
body_images_upload_approved: true
source_checked: true
copyright_checked: true
public_safety_checked: false
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
wechat_backend_preview_checked: false
rtd_page_checked: false
cover_image: wechat/assets/public-safe/ref-zhao2021-EFM/cover.png
---

# ref-zhao2021-EFM 内容制作记录

## 当前范围

- RTD直接依据完整32页原文逐段翻译；公众号为独立导读，不以导读替代全文。
- 公开文件为本篇RST、MD、review与18张原图；PDF、逐页图、提取文本、源页定位和清单均留私有工作材料。
- 作者自查完成；2026-10-14 root 独立科学内容审核通过，准确范围见文末记录。真实封面现已独立检查并绑定，官方离线渲染通过；完整网站/浏览器与实际手机后台仍待。
- 本轮正文图上传许可为true，仅表示授权，不表示已上传、后台接收或预览通过。

## 源文件获取记录

- 来源：本轮用户授权的作者团队期刊PDF附件；题名、六作者、Environmental Fluid Mechanics、2021和DOI与首页核对。
- 完整可读32物理页，在线出版版；2020-05-31收稿、2021-05-24录用、2021-06-03在线发表。当前副本未给卷期页码，不猜填。
- 当前副本与清单来源SHA一致；源PDF、页图、哈希清单留私有存储，不公开附件或原始文本。
- 无需尝试Zotero Web API `/file` 或网页下载；采用已获准可读完整源，不降级摘要。
- 摘要取物理p1，科学正文p3–30，符号表p1–2，参考文献p30–32；没有科学附录。
- 团队论文原图按本轮授权复用。先运行pdfimages，再检查原生图是否包括向量坐标/标注；不重绘数据。

## 工程叙事证据卡

天气网格与局部山地CFD既不同尺度也不同湍流闭合 → 调整涡黏度一致性、用统计指标选择IDW搜索方式，再守恒修正边界质量流量 → 用空域、Askervein近中性事件和Feng Men日变化验证 → 平均风速改善，但背风TKE、部分时段误差和未求解热力过程仍限制适用范围。

## 关键事实证据定位记录

- 单向WRF→URANS、MYJ/YSU方案及摘要限定：p1、p3–4；不声称双向耦合、LES或强热层结验证。
- 涡黏度一致、MYJ C_mu=0.1729、YSU=0.0417及两组k-omega常数：p5–8，式1–11、表1–3。式2的压力输运既有内层相关量横线又有外层横线，按放大源式保留。
- IDW四点/竖向八点/水平八点、空间权重、第一WRF层以下外推、统计指标：p8–10，图1、式12–17。
- 10min离线数据、CFD每步线性时间插值及质量守恒调整：p9–10，式18–20。式20原符号为下标Z_cp，不擅改上标。
- YSU经验k、omega及湍强；两个山丘EC4(.2,.2,.03)：p10–11，式21–23。
- Askervein TU-03B，1983-10-03 1300–1600UTC，Ri −.0038至−.0074，RS 8.9m/s/207°：p11。Feng Men 2017-08-21 0600至次日0600，风速30mAGL/温度10mAGL：p11–12、表4。
- WRF三层9/3/1km、40竖层、6h起转；CFD两域9×9×1.2km和8.4×10.5×1.8km、选择网格方案3：p12–16、图2–5、表5–6。
- URANS步长1s、20–25迭代、残差1e-4、SIMPLEC、边界及近壁处理：p16。科里奥利式按原文保留。
- 中尺度探空验证与不确定性：p16–18、图6–7，不把站点差异写成全部吻合。
- 二维空域4km×1.2km，首层.01m、增长1.07，海面EC5(.16,.15,.002)：p17–20、图8–9。速度保持较好，TKE均衰减，MYJ更好但其入流本身偏低。
- 四点q_c=1选择仅针对本研究高长宽比WRF网格；交叉边界推荐水平八点：p20–22、图10–12。图11的部分负估计方差不掩盖。
- 山顶10m风速MYJ15.27、YSU15.76，实测16.2m/s；增速峰1.03/1.21；AA-AA局部差异仍20%/60%：p22–25、图13–15。
- 背风TKE不足，时变URANS仍难再现间歇性分离；MYJ197±4°、YSU200±6°对实测207°：p25；图16边界TKE保持差异：p25–26。
- Feng Men表7全部32指标数值：p28。公众号引用YSU P1/P2 NMSE .067→.021/.112→.028、IOA .897→.974/.802→.931，并就近说明时段限定。
- 能量方程与地表热通量未加入，部分时段Ri<−.5；两时刻风向、尾流变化：p26–30、图17–18。全文不把目标“近中性”扩大为24h严格中性。
- 六个结论段及未来高嵌套比不稳定/热层结/低空急流研究：p29–30。

## 原文内部疑点及处理

1. p2符号表K/Z与正文k/z大小写不同；q印m²/s，Q_m、q_m,res均印kg/(m·s)，与名称或式18量纲有疑点。原值保留并译注。
2. p6表1雷诺应力闭合的正负号、导数和bar按源表转写，不按教科书默改。
3. p14表6多行表头错位；按正文物理定义展开水平、竖向最小网格尺寸列，数值全部保持。
4. p15图5题说(a)Askervein/(b)Feng Men，但两幅均含两地点，实际坐标为方案1/2与方案2/3比较。保留原图题并相邻解释。
5. p16科里奥利项印F_c1=fu、F_c2=−fv，未自行换成交叉分量。
6. p17称Kings Park与ZGOW相距76km，按原文明确归属，不将其当作已外部核实地理距离。
7. 图8(c)称dissipation rate但单位1/s；全文按原图题保留并说明对应omega比耗散率，不混写epsilon。
8. p20–22称MSE但阈值和图12单位是m/s；不改名RMSE、不改数值，不据该单位另作百分比推算。图10–12将q_c引至式12，实际含参数的权重为式13。
9. 图11“估计方差”有负值，保持曲线和说明，不解释为严格非负统计方差已证实。
10. p25把经验k与omega共同指向式22，而实际分别为21/22；相邻译注说明。
11. p27几何平均偏差先写MB、后为MG，公式和表7均MG；翻译保留差异说明。
12. p28把Ri<−.5称为略不稳定。原文条件与措辞保留，导读不称整段24h严格中性。
13. 参考文献的作者大小写、期刊格式及Pope条目异常按印刷表保留，不编造修订书目。

## RTD覆盖与原图自查

- 75个源页标定的叙述/公式引导段，含摘要与6个结论段；另保留引言3项和IDW讨论2项列点。正文所有章节次序完整。
- 25个编号公式完整可编辑；7个编号表，数据行分别3/2/2/2/8/6/4。原表合并项展开为明确列，数值未合并压缩。
- 50个符号条目：36拉丁、14希腊；45条参考文献完整保留。无科学附录。只省略致谢、基金、出版者声明及重复页眉页脚。
- 18张原图完整：图2/10/16/18使用PDF原生字节；其余因向量曲线、坐标或覆盖标注需保留而采用4倍页裁切。全部最终图已作者侧打开核对，无补色、伪曲线或相邻正文。
- 公众号用图1/12/15/17，alt与图题首行一致，另有独立读图句。

## 写作与交付边界

- 忠实摘要后设置“研究问题与解决思路”，再以闭合一致、插值点数、背风TKE及日变化验证四节独立展开，不重复摘要。
- 数字保留站点、时间、指标和基线；没有把平均风速改进写成湍流完全准确、把四点IDW写成普遍最优或把本篇写成台风研究。
- 末尾唯一追加“本文由 AI 辅助整理与撰写”；原论文作者与公众号author字段不改为AI署名，RTD不另加声明。
- 封面私有简报已给五个具体选项，本轮授权采用“大尺度来风怎样落地 / 近中性山地风场嵌套”；真实图未生成，不以占位文件过门禁。
- 独立科学内容审核已通过；真实封面、实际浏览器浅深色/长表/公式检查、后台和手机预览尚待，科学通过不扩展至这些范围。

## 本地可执行检查

241 个 LaTeX 表达式（含25个编号公式及行内/表格符号）经仓库 MathJax SVG 渲染器编译成功；公众号官方 academic-clean / mathjax-svg HTML 生成成功。22处本地图链接全部存在。Sphinx 仅用禁用 sitemap 的受限诊断发现本篇没有语法警告，仅未接入 toctree；这不是标准全站通过。公共安全门禁针对本篇仍报缺真实顶部封面，保持待集成，不用占位绕过。未做实际浏览器或微信手机显示检查。

## 独立科学内容审核记录（2026-10-14）

审核者 root，依据其由制作负责人转达的准确报告登记：完整阅读 32 页原文文本（1680 行）、完整 RST（937 行）及公众号稿；25 个编号公式均对照原页，其中式 2、24、25 额外放大；核对 7 表，包括表 6 错位表头。18 图在六幅整板中全部查看，独立重新提取 4 张原生嵌图与 14 张页裁图，18/18 字节一致。结果为独立科学内容通过，没有新增科学阻塞。该范围不等于每张图逐像素视觉检查，也不涵盖封面、排版、后台、手机或部署。

冻结科学稿哈希：

- docs/source/paper-notes/ref-zhao2021-EFM.rst: 170019fec1a81d6995b2213f93785f85ea55962eb201c89c7b4b5710b2399e74
- wechat/articles/draft-public-safe/ref-zhao2021-EFM.md: 86859226c680689f6558f69ca7fa6d8e47d29e0d8cbc25b026b43f72f833a577
- wechat/assets/public-safe/ref-zhao2021-EFM/fig01-original.png: 5bb6bc6b1fb926f623c57fe0e5ed766d344b822322a37e8d27ef0596fad8ff31
- wechat/assets/public-safe/ref-zhao2021-EFM/fig02-original.jpeg: ca1ef9e29f04211b341b29a2615eea322095b5a46d8c95d986af7728e094cf93
- wechat/assets/public-safe/ref-zhao2021-EFM/fig03-original.png: ccef553d593999844a4db3c80ef704aed6d0116932b32ecd25061aeabcea24cc
- wechat/assets/public-safe/ref-zhao2021-EFM/fig04-original.png: f5aa464cb5c58198438856f30f16a9896ffb0b21857c766f8484bf6065361e87
- wechat/assets/public-safe/ref-zhao2021-EFM/fig05-original.png: 5c3db75474b9373e7fcb6b083ca8a4fcfc75cd87b506efc5fc38739050af20f9
- wechat/assets/public-safe/ref-zhao2021-EFM/fig06-original.png: e6874e53b053b8014a30765e2f540bddb2f81e542a75d1b18dd52bafb4ea045c
- wechat/assets/public-safe/ref-zhao2021-EFM/fig07-original.png: 471f630864795b0a21caae8f92996f30be7d0650528939a25dcd99ba49b6f981
- wechat/assets/public-safe/ref-zhao2021-EFM/fig08-original.png: 70c7e16395ff54d365871691665a45b2b8917c6c2096fc29a0ca3f5c53071b8f
- wechat/assets/public-safe/ref-zhao2021-EFM/fig09-original.png: 03d4af9e4f2baba833e60977d9492822f25c7e8591dbf78e1d8ae81ff81b6953
- wechat/assets/public-safe/ref-zhao2021-EFM/fig10-original.png: 840b58d8ae9a1d8662882f71b164548b88689ab3478a21fc220cfa0203c30bc8
- wechat/assets/public-safe/ref-zhao2021-EFM/fig11-original.png: 212f96c4f04abdd8e137af9577e5e7fcdab17dfd115965eca75fa82263b28d07
- wechat/assets/public-safe/ref-zhao2021-EFM/fig12-original.png: f8837c6e3abba734a1e1c50329f84d9073ed934a3bd1290611c823d9e6043217
- wechat/assets/public-safe/ref-zhao2021-EFM/fig13-original.png: 3c757d721a8cf7da5a8f4fd8cf8ea03443dfce597da0ddd48e3aae2e89bcffa9
- wechat/assets/public-safe/ref-zhao2021-EFM/fig14-original.png: 2a1475de5e38b6dd5a82989a6c5a1ed3b0996ccfcdd7268d91ab8b8563b5590f
- wechat/assets/public-safe/ref-zhao2021-EFM/fig15-original.png: a23a8b934f6e8ed52488af3c3bf7d2eab250a6e912f0b2497c9333bf8b295344
- wechat/assets/public-safe/ref-zhao2021-EFM/fig16-original.png: 89ceae6f659d8caa0287eaba7ab4d68d07c135d253c89e9e4f8df17e796cbf50
- wechat/assets/public-safe/ref-zhao2021-EFM/fig17-original.png: 41bba4ca7611ac6ef7d32cbf3007e28c5da8a18f67c3ac587506dd4dec7fdb3a
- wechat/assets/public-safe/ref-zhao2021-EFM/fig18-original.png: 0646b6fde44f7bcc4dd2ff0525b9ebb1f160f7bdfff037a4ac6b4b2f250cc283

## 2026-10-14 第四批真实封面绑定与科学等价

沿用上文独立科学内容审查范围，不重作或扩大原PDF审核。最终封面 `wechat/assets/public-safe/ref-zhao2021-EFM/cover-wechat-900x383-20261014-v5.png` SHA-256 `66698a86e81131ada4ff887708225219596e0c930bc8e898256577cbea7be617` 已逐张独立核对，当前整合亦重新打开实际900×383PNG核对。工程图仅作概念示意；边界与不表达的几何/效果见同篇cover-brief，不将本地封面审阅当成微信手机验收。

本次仅在RTD顶部加入封面image指令，并绑定主review的双渠道封面路径。加图前RST SHA-256 `170019fec1a81d6995b2213f93785f85ea55962eb201c89c7b4b5710b2399e74`；新增指令块逆向移除后逐字节恢复原稿。公众号正文、作者、摘要、科学原图和数据完全未改，AI声明仍只在文末一次。正式排版、标准整站构建、实际浏览器、后台草稿与手机浅/深色验收另行记录；不提前标记verified或发布。

## 2026-10-14 第四批离线渲染与冻结边界

官方 preflight、dry-run 与 academic-clean / MathJax SVG 渲染通过。本篇公众号正文含4张原图、4个行内SVG公式和0个显示公式；图像嵌入和SVG几何/currentColor静态检查通过。390px浅/深色容器对照仅为离线诊断，不证明真实微信手机行为。

六页最小RST语法测试以正常mathjax扩展、warnings-as-errors运行通过，无可见math/ref角色泄漏或problematic/system-message节点；该测试不替代标准全站构建。RTD含19张图（首张为真实封面）、25个显示数学块和9个HTML表；表格数量包括论文符号表等编辑呈现，不改原论文覆盖数。

本篇仅有顶部封面块及0处行内math括号边界ASCII空格、0个标题下划线字符的版式增量。逆向删除这些精确插入即恢复已科学审查RST原字节；公式LaTeX内容、表值、作者、摘要、全部原图及公众号MD逐字节不变。当前RST SHA-256为 `6c628eb8cc29a9502400ed33a5957c4fe9ae323cf172333feac541e6725c77c1`。实际浏览器、标准全站构建、部署及微信后台手机验收另行记录，仍待最终接入验收，不标verified、ready_to_publish或published。
