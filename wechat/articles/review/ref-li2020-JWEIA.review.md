---
publication_ref: ref-li2020-JWEIA
doi: 10.1016/j.jweia.2020.104281
research_family: 工程结构抗风
subdirection: 数值风洞
publication_mode: first_publish
wechat_status: drafting
wechat_author: Li Chao
body_images_upload_approved: true
wechat_cover_image: wechat/assets/public-safe/ref-li2020-JWEIA/cover-wechat-900x383-20261014-v5.png
rtd_cover_image: wechat/assets/public-safe/ref-li2020-JWEIA/cover-wechat-900x383-20261014-v5.png
source_checked: true
copyright_checked: true
public_safety_checked: false
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
wechat_backend_preview_checked: false
rtd_page_checked: false
---

# ref-li2020-JWEIA 内容制作记录

## 正文文件

- 独立全文：`docs/source/paper-notes/ref-li2020-JWEIA.rst`
- 公众号：`wechat/articles/draft-public-safe/ref-li2020-JWEIA.md`
- 原图：`wechat/assets/public-safe/ref-li2020-JWEIA/` 中 fig01–fig33；fig03 为 PNG，其余为 JPEG，按实际文件引用。
- 真实封面已独立检查并绑定双渠道，官方离线渲染已通过；完整网站/浏览器与实际手机后台验收仍待，不提前声称完成。
- 正文图上传许可为本轮任务授权，仅表示可以由集成人员按授权流程上传，不表示已上传或已完成后台检查。

## 源文件获取记录

- 元数据来源：项目注册表、学术成果页及原文首页。
- 附件记录：已提供的作者团队原文；本地完整 PDF 共 22 页。
- 已选版本：作者团队提供、获准复用的出版社排版原文；当前未有另行提供的优先作者终稿。
- 私有存储类别：论文来源、原始文字、逐页截图、抽图记录、覆盖审计及集成清单均私有保存，不进入公开文件。
- Zotero Web API 与网页下载：无需，未使用。
- 摘要依据：PDF file page 1；正文及参考文献依据：PDF file pages 1–22。
- 图片依据：先运行 pdfimages 提取嵌入图，再按 PDF 图像位置取得相同原生图像字节，无缩放、无重绘；33 幅最终原图均已作者侧目视检查；根独立复核已查看全部概览，并核对全部原生字节与来源页码，未将概览扩称逐张放大检查。

## 关键事实证据定位记录

- 摘要、作者及 DOI：PDF file page 1。
- 传统冠层三项源项与新 ECD 仅动量源项：PDF file pages 3–4，式 (1)–(7)、§2.1。
- 12 m × 1.8 m 二维域、约 1.2 m 边界层、x=4 m 监测位置、六个决策变量：PDF file page 4，图 1、§2.2。
- NSGA-II、参数边界及两目标：PDF file pages 4–6，式 (8)、图 2。
- 两类入流、三种地表、网格、参考风速：PDF file pages 5–8，表 1–3、式 (9)–(14)。
- 36 线程、最快29小时、平均37小时、91% CFD 时间：PDF file page 9，§4.1；不推广为普遍耗时。
- 对数律目标速度误差无/有 ECD：15.7%/5.6%、25.8%/4.8%、43%/7.0%；TKE 37.2%/26.1%、39.3%/27.0%、42.6%/26.8%：PDF file page 11，§4.2、图 9–10。
- 幂律目标速度误差 15.5%/5.1%、25.6%/10.9%、71.4%/9.8%；TKE 56.2%/50.5%、56.3%/44.0%、56.6%/39.8%：PDF file pages 14–15，§4.3、图 14–15。
- 120 个均匀点、参考风速归一化的平均绝对差：PDF file pages 15–16，式 (15)、表 4（page 14）。该指标不同于式 (8) 的逐点入口归一化相对误差。
- 标准 k–ε、EWT/SWF 及近壁单元高度：PDF file pages 16–18，§5.1、图 19–20。
- 分别重优化5/20 m/s 与直接迁移10 m/s系数的两组试验：PDF file pages 18–19，§5.2、图21–28；迁移后近地TKE分别不足、过量。
- 三维展向1.8m、67格，与二维比较：PDF file pages 19–21，§5.3、图29–33。
- 参数仍需优化、TKE敏感、五个系数个数与实尺度尚待研究：PDF file page21，§6。
- 全部编号公式：式1–7在page3，式8在page4，式9在page6，式10–12在page7，式13–14在page8，式15在page15。另有未编号矩阵、优化表达式及正文内公式，全部保留。
- 5张编号表：表1–3在page5，表4在page14，表5在page17；表4将原分组宽表展开为六行，不遗漏数值。
- 原图：图1在page4；图2在page5；图3–4在page6；图5–6在page7；图7在page8；图8–9在page9；图10–11在page10；图12在page11；图13–14在page12；图15–16在page13；图17–18在page14；图19–20在page15；图21–22在page16；图23–24在page17；图25–26在page18；图27–28在page19；图29–31在page20；图32–33在page21。
- 科学符号表：PDF file page2，共48项；为不打断引言跨页段落，全文在摘要后完整列出并说明位置调整。
- 参考文献：PDF file page22，共46条；无科学附录。

### 原文疑点与保留

- page7 将 β* 写为1.0，page8交叉扩散项采用原印表达；全文忠实保留并加注，不以外部SST公式默改，也不声称实现代码已验证。
- page9以每代两目标平均值小于10⁻⁴描述收敛，但最终剖面目标误差仍是百分数量级；全文保留说明，不改造成全场误差阈值承诺。
- page12幂律作用高度文字写0.03–0.05δ且均大于对数律；page14表4列0.022、0.023、0.051，与文字不完全一致。正文并列保留并加译注。表5基准高度与表4也有细小差别，未擅自统一。
- 原文表1幂律速度用u、u₀，而TKE及耗散公式用U；按源保留。原文符号表采用Dirac称谓，未以译者改写替代。
- 原版在线发表日期显示xxxx；未虚构日期。

## 工程叙事证据卡

- 论证线：入口剖面会沿程变形 → 近地有限高等效阻力和双目标优化 → 两种入流、三类粗糙地表及迁移试验 → 平均风改善较明显 → TKE、跨风速和实尺度仍须单独检验。
- 工程问题与决策者：给建筑/结构风效应模型准备来流的计算人员，需要判断到达目标位置时的平均风和湍流是否仍与预期一致；未虚构工程项目。
- 基线及局限：无ECD基线，不等于与所有已有方法逐一性能对比；全文并未验证实尺度复杂地形。
- 具体改动：仅x动量方程近地源项，五个高度系数加作用高度；不额外改湍流模型常数、不把源项涂满全高度。
- 机制与验证：速度剪切和雷诺应力改变可间接影响TKE；二维/三维和RANS模型迁移为数值验证，不是风洞装置试验。
- 已验证结果：正文明确列目标误差及其基线/地表/入流，不与表4另一指标混用。
- 潜在用途：空域来流自保持检查；具体建筑、污染物或高雷诺数问题须先复核目标选择、边界与参数。
- 适用边界：近地改善不等于全高度完全均匀；重新优化不等于直接迁移；LES与实尺度均为未来工作。
- 标题与导语依据：page1–4对入口/顶面/壁面相容性及近地阻力机理的讨论。
- 封面钩子依据：采用“入流正确还不够 / 冠层阻力维持风场均匀”；本轮获批按原文拟定后采用，尚未出图。

## 写作与去 AI 味审校

- 摘要依原文完整翻译，与正文解释分开。
- 研究问题与解决思路后保留四节，围绕源项、六参数、误差口径和迁移边界展开，无泛化价值口号。
- 两类误差、两类跨风速试验分别描述，保留TKE不足及过量。
- 作者名单保持原论文；文末且仅一次附“本文由 AI 辅助整理与撰写”。
- 公众号使用图1、8、9、28，图注第一行与图片替代文字一致，第二行解释读图位置。

## 全文覆盖与验收边界

- 作者侧逐句对照完成：79个正文/公式解释段落（含摘要，跨页段落合并计一次），另3个编号结论；15个编号公式、2个未编号显示公式块及行内表达；33幅原图；5张可编辑编号表；48项符号；46条参考文献。
- 原文CRediT、利益冲突与致谢按项目规则不纳入公共科学正文；无附录。
- 独立科学内容复核：已由根审核通过，精确范围见下方记录；作者自查本身仍不等于独立验证。
- 本地37个正文图链接存在；不使用封面占位。
- 公共内容检查目前报缺顶部真实封面，属于待集成门槛，不能标通过；未发现本篇其他公开安全条目。
- 数学渲染、HTML长表布局、手机预览和微信后台检查尚未完成；实际API和部署由集成人员另行执行。

## 2026-10-14 独立科学内容复核通过

根审核完整阅读 RTD、公众号与 22 页原文文本，并核对原页 3、4、5、7、8、14、17 的关键版面。15 个编号公式及另 2 个显示块、5 表、48 个符号、46 条参考文献均在核验覆盖内。33 图全部概览已查看，33/33 原图与源 PDF 嵌入字节、页码及哈希一致；这不等于逐张全尺寸放大视觉检查。重点核验两种误差口径、六参数、37 h 的硬件限定、重新优化与直接迁移之别、TKE 尚未充分改善、SST 原文印刷疑点和 h_s 范围矛盾，无新增科学阻塞。

仅科学内容通过；封面、最终 HTML、浅深色手机预览、微信后台与部署不在通过范围。下列为本次科学审核冻结文件 SHA-256；审核后只改本 review 的状态和图格式说明，未改科学正文或图像。

- `docs/source/paper-notes/ref-li2020-JWEIA.rst`：`bfc72920db604748304df1ac91b9b78abe4bb3542d7bec35f836551c4ce0b85a`。
- `wechat/articles/draft-public-safe/ref-li2020-JWEIA.md`：`14c255f68ca1ad6479cafa3b831993c7508600fafb1cefd065499eb5baedc98f`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig01-original.jpeg`：`8a59ba765fd907d1295c79bd8d6f5578cfc6234eafe82ac877a3c3524f4d940e`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig02-original.jpeg`：`1a1dee334accec21fc274f0237b3aff149354560fd911a75ee99a1dcd8f24ce9`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig03-original.png`：`24c02f33d158fb34d68e3ae4cdcded5cb989f0318af768619e860ef76eabace6`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig04-original.jpeg`：`3da47fed907b162a4283a6ff34bb99c853511dde701bda7652bcde09af3ab6a4`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig05-original.jpeg`：`4452ff2f572e2f7631922b532d73a3d8deda2ef11780cd80113c016ebe4cc044`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig06-original.jpeg`：`fb28eac9b4789d689a20c9a6e0d2b90ae20f494d72dc33c5d12c4b339f245d5e`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig07-original.jpeg`：`7182356875acdc8e240244aa6b982dd068599d3a9bbba1ff02ede056b5d84a90`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig08-original.jpeg`：`4cd9b1d78496798f1d9b1e80c42c0822627e3b119e17bb8542539c3b92058673`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig09-original.jpeg`：`5011a893684025fbd16e7d5c23e66368eeef49b7743de645c05ea6fb262d0fb3`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig10-original.jpeg`：`08a253daaf9cb5e33699513c1574de4c1cd87c1a5922713e6215dc1c193b97ed`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig11-original.jpeg`：`39764a73f8e070d8aabdf0e2655772f72c9400c51550e6fec77048a617a65f7e`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig12-original.jpeg`：`1267a7cc75f1d7fd908d60259da2a83b633fc65403dd83f1d9f1788293b21773`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig13-original.jpeg`：`63197520481562b20cbee91733a31cf17daa922fb25448cc63b6dff65e187748`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig14-original.jpeg`：`b104fa803a7908f90be8924fdf375eafa959ca2f1f4fbfb2e33ee4f6acab6c6d`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig15-original.jpeg`：`451913688921a91a828406681b3e74e93ee301e4caa736cf62e2f9d044d2f499`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig16-original.jpeg`：`6aac54dfd18518910cd11d64b4c447d0700530e134c68c4ba8b3a36964230010`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig17-original.jpeg`：`886d4faf4277e818876fc2825dd9926179681baf664957b0320025e18b47be1a`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig18-original.jpeg`：`98fa5ec5e60edb4eecccf21b67a72f7dec875bb0b07b4f46b0efacb7bbf068fd`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig19-original.jpeg`：`1fbb385d8c0cf368733f084a78572df59af1fca790cd3bf0a3f418ab634dfeff`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig20-original.jpeg`：`2b6d7d3ab1754a23496867f2e1f95bd067866fc1820fe08b47462f3b1b78e8d0`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig21-original.jpeg`：`7de698bff5f626e224c3e4d40347e2cf07abf367aefc2f3c553685782a521591`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig22-original.jpeg`：`46c2fc13119d8524ba7579d47c71cc1e264cf260699ac4b33a3c37163039b20b`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig23-original.jpeg`：`ff48b5a5a8c3ab9a5a2c33379609e23422c09a3e0092065c80c270e31a0cc14d`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig24-original.jpeg`：`f1f74df1b209ff5b52fe5dbc65fa84752aaf26ea2e0caa68e232639a6adb67cc`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig25-original.jpeg`：`539eff7584f51170d92719c2f25d8184640cffbf0bd2e0ea0c6f900b0776cf38`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig26-original.jpeg`：`1f1d99f2b5c11e94d1a4f2a7a0c754a51e019925ce02f06f9812abd6f3e119cc`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig27-original.jpeg`：`12ad80f2c5540f10c25fed6d29f8efcdb4e5cbb0db0756baf7b1d6716a03305b`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig28-original.jpeg`：`42367db2a73e51946b652175be828667631419c8b1534cc5b4f734f34aa2a640`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig29-original.jpeg`：`28fc7b3bd42621dd4e40ae5844fb8f1c154376902e457a729572925cdb566111`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig30-original.jpeg`：`9f87ebf73f9901041dde3f374527b0c9528f331c593ff1514e5b8fcab619bdc7`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig31-original.jpeg`：`ec09df3b489196e981f6caf37658bda4ee63e759fea04c22efcd6fd1386911c5`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig32-original.jpeg`：`4f263a6dd0edc5270bb416b6728f5d77554c9cce21fd8b0ff286de1062f7aa53`。
- `wechat/assets/public-safe/ref-li2020-JWEIA/fig33-original.jpeg`：`018fb6be729a7dbf4f7e1c3408c56ced0ef8cdb6843398af96853caf04776e3d`。

## 2026-10-14 第四批真实封面绑定与科学等价

沿用上文独立科学内容审查范围，不重作或扩大原PDF审核。最终封面 `wechat/assets/public-safe/ref-li2020-JWEIA/cover-wechat-900x383-20261014-v5.png` SHA-256 `a5868685847f8dddef221a93061c738956649a2ed39910173b034984b86c0da9` 已逐张独立核对，当前整合亦重新打开实际900×383PNG核对。工程图仅作概念示意；边界与不表达的几何/效果见同篇cover-brief，不将本地封面审阅当成微信手机验收。

本次仅在RTD顶部加入封面image指令，并绑定主review的双渠道封面路径。加图前RST SHA-256 `bfc72920db604748304df1ac91b9b78abe4bb3542d7bec35f836551c4ce0b85a`；新增指令块逆向移除后逐字节恢复原稿。公众号正文、作者、摘要、科学原图和数据完全未改，AI声明仍只在文末一次。正式排版、标准整站构建、实际浏览器、后台草稿与手机浅/深色验收另行记录；不提前标记verified或发布。

## 2026-10-14 第四批离线渲染与冻结边界

官方 preflight、dry-run 与 academic-clean / MathJax SVG 渲染通过。本篇公众号正文含4张原图、11个行内SVG公式和1个显示公式；图像嵌入和SVG几何/currentColor静态检查通过。390px浅/深色容器对照仅为离线诊断，不证明真实微信手机行为。

六页最小RST语法测试以正常mathjax扩展、warnings-as-errors运行通过，无可见math/ref角色泄漏或problematic/system-message节点；该测试不替代标准全站构建。RTD含34张图（首张为真实封面）、17个显示数学块和6个HTML表；表格数量包括论文符号表等编辑呈现，不改原论文覆盖数。

本篇仅有顶部封面块及13处行内math括号边界ASCII空格、8个标题下划线字符的版式增量。逆向删除这些精确插入即恢复已科学审查RST原字节；公式LaTeX内容、表值、作者、摘要、全部原图及公众号MD逐字节不变。当前RST SHA-256为 `b9a8a65c652165333d72a5f00ebff4f63e88bb3288f7246d6578c0e113e74248`。实际浏览器、标准全站构建、部署及微信后台手机验收另行记录，仍待最终接入验收，不标verified、ready_to_publish或published。
