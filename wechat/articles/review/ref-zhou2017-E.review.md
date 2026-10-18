---
publication_ref: ref-zhou2017-E
body_images_upload_approved: true
cover_image: wechat/assets/public-safe/ref-zhou2017-E/cover.png
---

# ref-zhou2017-E 内容与证据审阅记录

## 当前状态

27页主论文科学正文完整中文译文、独立公众号导读、29幅原图、6张可编辑表、5个编号公式及53条参考文献已制作。作者自查与非撰稿者的独立科学复审均完成；科学范围通过；真实封面现已独立检查并绑定、官方离线渲染通过，完整网站/浏览器、部署和实际手机后台仍待。

## 源文件获取记录

- 元数据依据授权论文条目、注册表与PDF首页，题名、8位作者、期刊、年份与DOI一致。
- 源为授权团队原论文清单中27页出版社排版PDF。当前副本哈希与早期来源清单哈希不同，不能声称字节身份一致；以本次实际阅读的副本及其私有哈希锁定证据。首页、连续页码、题名、DOI与内容已核对。
- 原PDF、原始文本、逐页渲染、提图清单及覆盖审计只保留在私有区。不发布原PDF、全文原文转录、私人联系信息或逐页截图。
- 先执行pdfimages原生提取。29幅图均包含矢量曲线、文字或跨原生对象的子图标识，因此采用保留全部面板与标注的局部页面裁剪，没有重绘原图、伪造数据或裁入整页正文。最终29图均已逐幅目视检查。
- 未访问Zotero Desktop Local API或Web API `/file`，没有另行联网下载来源。

## 关键事实证据定位记录

- 摘要及研究范围：PDF file page 1；引言 page 1–3。研究多个同向风浪来向，不是风浪夹角变化。
- ConFloat构型、5 MW直驱风机、90 m轮毂、切入/额定/切出风速3/11.5/25 m/s：page 3–5，第2节、图1、表1–2。轻质混凝土密度1900 kg/m³、壁厚350 mm、吃水23 m；中央和3外立柱由Y形矩形浮箱相连，无斜撑。
- 1:60弗劳德模型、0.95 mm不锈钢外壳、110 cm阻力盘、平均推力匹配：page 5–7，第3.1–3.2节、图2–4。原型混凝土与缩尺模型钢板不得混称。
- 悬链线替换为三向水平弹簧及恢复曲线校核：page 7–8，图5–6。仅模拟规定恢复特性，非原型悬链线全动力测量。
- 平均风速11.5 m/s、低于5%的湍流强度、风剖面指数0.1：page 9。Hs=2.23 m、Tp=6.74 s，JONSWAP及水槽反射限制：page 9，图8。
- 立体视觉六自由度测量、双相机5靶点和激光校验：page 8–9，图7。48工况、五类试验、三个来向和记录时长：page 9–10，表4。
- 六自由度运动方程、平均/差频二阶水动力和忽略和频：page 10–11，式(1)、图9。60频率0.05–3 rad/s，步长0.05；二次阻尼根据自由衰减试验调整。
- 非旋转钝体气动力模型：page 11–12，式(2)。线性系泊矩阵与方向差别：page 12–13，式(3)、图10。塔筒一二阶弯曲频率0.444/2.949 Hz：page 13，图11。
- 固有周期与二次阻尼：page 14，表5–6。规则波比较、5 s时部分风机RAO三至四倍以及长周期高估：page 14–16，图12–14。塔底荷载及机舱加速度并未在试验中测量，仅数值估计。
- 仅风时各方向平均纵摇一致：page 16，图15。仅不规则波时90°纵荡大、60°纵摇大：page 16–19，图16–19、式(4)–(5)；300组波浪种子为数值统计，不是300次试验。
- 不规则波塔底弯矩和机舱加速度：page 19–20，图20–21。一阶纵荡与二阶纵摇作用频带不同。
- 联合风浪简化模型及风致低频响应限制：page 20–22，图22–25。真实旋转转子和湍流风比较：page 22–24，图26–29；TurbSim Kaimal、11.4 m/s、14.48%、剖面指数0.14；3P约0.5–0.65 Hz；最大塔底弯矩高近20%，不是减载20%。
- 结论：page 24–25。53条参考文献：page 25–27。无科学附录。按项目风格排除作者贡献、致谢、利益声明及出版许可等声明性尾注。
- 图页对应：1 p4；2 p5；3 p6；4 p7；5–6 p8；7–8 p9；9 p11；10 p12；11 p13；12 p15；13–15 p16；16 p17；17–18 p18；19–20 p19；21–22 p20；23–24 p21；25 p22；26–28 p23；29 p24。

## 原文疑点与编辑处理

- 式(3)原图每个非零矩阵单元堆叠三个方向的数值；译文展开为三个6×6矩阵方便读取，仍共用原编号(3)，保留不完全对称的交叉项及原式正号，不自行改成理论上预期的形式。
- 式(5)在差频求和条件下仍写相位和φmn+φm+φn。核对原页后保留，并加译注提醒不能据译文静默修正科学公式。
- 图13纵荡力RAO的纵轴单位原图为kN/m²；图20、24、28加速度PSD轴标签使用(m/s)²/Hz。原图保留，正文以响应名称解读，不擅改数据单位。
- 原参考文献的年份、卷号、页码与拼写均按源保留，未将看似不一致条目静默替换为其他文献。
- 关于“60°最不利”的表述限定为文中相关塔底荷载/机舱加速度和纵摇；纵荡在90°较大，不能扩成所有响应均60°最大。

## 工程叙事证据卡

Y形浮体各来向受波不同 → 三方向同向风浪缩尺试验与FAST比较 → 用QTF分离低频二阶运动，用波频响应解释一阶荷载差别 → 加入旋转与湍流检验简化气动力的影响 → 分指标选择方向工况，不把额定单海况推广到全寿命安全。

## 写作与方向审校

保留海上漂浮风电 / 一体化分析，导语与忠实摘要独立，研究问题与解决思路单列，正文四节使用具体标题。原图1、17、28用于公众号，alt与紧随图题一致；作者不改，文末仅一次“本文由 AI 辅助整理与撰写”。RTD没有该声明，也未由公众号扩写代替完整翻译。

## 本轮封面简报

- 选定：一体化分析 | 同向风浪也看朝向 / Y形平台响应的方向效应。
- 期刊年份：Energies · 2017。
- 工程场景：五兆瓦风机立于中央立柱，三外立柱通过水面下矩形浮箱连接成Y形；整体为预应力混凝土，三根悬链线。用平行同向的风箭头与波列、平台周围三条方向参考线表现0°/60°/90°比较，勿画成同时三面风浪围攻。依据PDF file page 4图1。
- 机制锚点：同向风浪相对浮体的朝向变化；低频运动与波频荷载分别检查。不用一个“危险60°”标签概括所有自由度。
- 禁止误画：钢桁架斜撑、三外柱无中央柱、单柱Spar、底固定导管架、风浪相互垂直、三个方向同时施加载荷、把1:60阻力盘试验画成真实叶片实验、全尺度海试实拍、发电增益或疲劳寿命百分比。
- 文案选择是本轮批量授权，不延伸为通用许可。工程图imagegen，文字与160×40方向标签固定排版，最终900×383；等待统一生成及独立视觉验收，不使用占位封面。

## 正文图上传许可与未完成事项

body_images_upload_approved: true 只表示本轮27篇对应草稿正文原图的必要上传已获授权，不代表图片已上传、草稿已建立、独立科学审核或后台预览通过。最终封面、独立科学复审、Sphinx集成及手机浅/深色排版仍需分别完成。

覆盖计数：73个原文科学自然段，对应74个译文显示段（原文内联阻力公式单独排版而将其所在段拆为前后两段），按源段归并为73个对应单元；5编号式加1未编号阻力式、29图、6表、53参考文献。原有CrossRef链接已保留。

独立复审反馈修订：式(5)初稿漏转求和整体的模及运动QTF的模，现已按PDF file page18放大原式补回；式(4)–(5)及定义中的QTF上标M/F按原文恢复。此项是转写修正，不是原论文错误；待独立复验。

复审读者文案修订：公众号摘要恢复原文三项平台实例；图28读图句改按(a)(b)(c)标识，不误称纵向三层。RTD图13及20/24/28附近新增公开量纲校核注，保留源轴单位而不宣称物理正确。

## 2026-10-14 独立科学内容审核通过

非本篇作者逐页查看27页原文并完整对照RTD及公众号，覆盖73个科学段落对应单元、5编号式和1未编号阻力式、式3三组6×6矩阵全部单元、6表所有值、29幅最终原图、53引用。式5两层模的转写遗漏及QTF上标已修正并对放大原式复验；公众号摘要例子和图28分图读法已修，图轴量纲疑点已公开说明。

科学通过不等于独立重算原模型，也不代表封面、HTML/公式/图片排版、标准构建、部署、后台及手机浅深色验收。以下哈希锁定本次审核范围，后续变化按范围重审。

- `docs/source/paper-notes/ref-zhou2017-E.rst`：SHA-256 `49ceaa5221eb6b1b67f2ad26c054da09a47276e506c48f6c0a6695f72e5a07c0`。
- `wechat/articles/draft-public-safe/ref-zhou2017-E.md`：SHA-256 `64394152fa7c7f2d3a9f8567753429cb36dc0979fbe7bca3f928ae16d36591a0`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig01.png`：SHA-256 `50087c351cd3fc1a6afde3805ac3d71b4f227073f1d1589b4df339038e7b0a11`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig02.png`：SHA-256 `44ea8942308e088cc583f77cf7127fe8a243ed2745ec4886d8cdbfce4e658a44`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig03.png`：SHA-256 `b44896780663f9b5f6f68fb67303d15594eb37a42a3bcec4200f43e27544f582`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig04.png`：SHA-256 `cd1ef447d67c71351ee62823a8010d0bfe2b65061e79d396df6add2b3162e712`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig05.png`：SHA-256 `3cb534bb17ea9bf1512db9289b709378232f017679e2d52506c346b4c942644c`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig06.png`：SHA-256 `0be30366f993f5feeedc9db4ea19ff3408ebcbc3df0a91030c9c6ba9c2c0b16e`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig07.png`：SHA-256 `0a19a3403bb4b8557a4e1ef3c09540db6b89c530a489d468abb2484de20d95dd`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig08.png`：SHA-256 `7cbc8fdf822cc285b4a102bbbf49298f4696a5688760c99f986215c890c59f9d`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig09.png`：SHA-256 `f4e6f5e9c8bfccb0929cb0abf4173f05d2ee47c2e5cfb6e12a07ad95f671bf4c`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig10.png`：SHA-256 `6f702af7821a7d3dc371c2f3f263f93e840236306af851e6dd466e36bb2be9f4`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig11.png`：SHA-256 `29192689ce6fda7b2353597f06c3bd22e64fa1ee6b195fbc43dd7eddb3464610`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig12.png`：SHA-256 `3771771f775ccae07e2d332a97286db910fd20de80a122ceba855557aa02b9a8`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig13.png`：SHA-256 `e2d0d097a43cc7c53b36ada3ea69a4ad93c2a7c976e032a0825d672e5a87f522`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig14.png`：SHA-256 `da8bd4eb95f02748651a578d7a51822678521a7c6eb9848eccf0522bd9f9dce1`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig15.png`：SHA-256 `ec1cdce5c0176582e9ba4357aaabda63060ac77125239e8919d34746abe5d22e`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig16.png`：SHA-256 `272738ee1b2f12dfb439b81113b6c8e230ff9e23455d03afdd6ddcad8a7a8840`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig17.png`：SHA-256 `b928f035d3315de8178bb044c3b8cc7d6a5b576fb4b71cf7868d5f29af8bdfd5`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig18.png`：SHA-256 `d347e239005b140545e2f0817188b3e4fac49db4984cf6333f94d65cbd014c12`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig19.png`：SHA-256 `58a1d939b9d5ddfb5b8d8ba3bec9f68063fac009214b3f2cd6e80b348cea8de7`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig20.png`：SHA-256 `79dcfdd06ea1bb0d20d508439e90e1f9fa076fc19cf718979e8e69379f88fe56`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig21.png`：SHA-256 `37e614f76464d7301a03d452f429f1af0bc7b768f76ebb5c84bbe3f9332ebb9e`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig22.png`：SHA-256 `ea69f38070c7c255f147a34ce64390c41c8ed5968a7bb630e35d287fa1243b69`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig23.png`：SHA-256 `5d76aabc7677d0685e20c3bb3bc2de2ad971c92403a524ea9ba93c5f06e3d580`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig24.png`：SHA-256 `5921541cde40ebd178003661267254b09206b3c531e32e30fb4854d6912f67ec`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig25.png`：SHA-256 `0729986394b63e5beb9b3058f4ed265aaba96f97ce787c78504217d1ef1b58fd`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig26.png`：SHA-256 `322e24bc4401863349ae1a777c9d07c1a6d6b036661b0a0f39d1c4c106cc15a9`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig27.png`：SHA-256 `71389c89ecfeb2e1862dcda12c187181e3b18b3eff046f07701259dabf57d548`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig28.png`：SHA-256 `83f72ed5a91080a38ca8fec5b280050cbe06917614bc6cc1c22a0b684f1e7902`。
- `wechat/assets/public-safe/ref-zhou2017-E/fig29.png`：SHA-256 `60b6d77ffd864d903309122bde286067bdcb13c8bcfae2fe2c2f58e34fcca6cd`。

## 2026-10-14 第四批真实封面绑定与科学等价

沿用上文独立科学内容审查范围，不重作或扩大原PDF审核。最终封面 `wechat/assets/public-safe/ref-zhou2017-E/cover-wechat-900x383-20261014-v5.png` SHA-256 `00c38c7c15f621c28a99b6f6ca7147b24464e461239c10e7e6972ba99a4d9be0` 已逐张独立核对，当前整合亦重新打开实际900×383PNG核对。工程图仅作概念示意；边界与不表达的几何/效果见同篇cover-brief，不将本地封面审阅当成微信手机验收。

本次仅在RTD顶部加入封面image指令，并绑定主review的双渠道封面路径。加图前RST SHA-256 `49ceaa5221eb6b1b67f2ad26c054da09a47276e506c48f6c0a6695f72e5a07c0`；新增指令块逆向移除后逐字节恢复原稿。公众号正文、作者、摘要、科学原图和数据完全未改，AI声明仍只在文末一次。正式排版、标准整站构建、实际浏览器、后台草稿与手机浅/深色验收另行记录；不提前标记verified或发布。

## 2026-10-14 第四批离线渲染与冻结边界

官方 preflight、dry-run 与 academic-clean / MathJax SVG 渲染通过。本篇公众号正文含3张原图、0个行内SVG公式和0个显示公式；图像嵌入和SVG几何/currentColor静态检查通过。390px浅/深色容器对照仅为离线诊断，不证明真实微信手机行为。

六页最小RST语法测试以正常mathjax扩展、warnings-as-errors运行通过，无可见math/ref角色泄漏或problematic/system-message节点；该测试不替代标准全站构建。RTD含30张图（首张为真实封面）、6个显示数学块和6个HTML表；表格数量包括论文符号表等编辑呈现，不改原论文覆盖数。

本篇仅有顶部封面块及3处行内math括号边界ASCII空格、0个标题下划线字符的版式增量。逆向删除这些精确插入即恢复已科学审查RST原字节；公式LaTeX内容、表值、作者、摘要、全部原图及公众号MD逐字节不变。当前RST SHA-256为 `01b3a90727f938d60b93dd27e36e0fb7ed2ece6b6ddf9010b7ab2e3cca392183`。实际浏览器、标准全站构建、部署及微信后台手机验收另行记录，仍待最终接入验收，不标verified、ready_to_publish或published。

## 2026-10-14 文末空白门禁修正

为通过git差异空白检查，仅移除RTD文末一个多余空白行，即1个换行字节；未删任何科学内容。对版式修正逆变换补回该换行后，仍可逐字节恢复先前已审RST。其他文字、公式LaTeX、图表及公众号MD均保持不变。
