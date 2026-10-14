---
publication_ref: ref-li2018-AE
body_images_upload_approved: true
wechat_cover_image: wechat/assets/public-safe/ref-li2018-AE/cover-wechat-900x383-20261014-v5.png
rtd_cover_image: wechat/assets/public-safe/ref-li2018-AE/cover-wechat-900x383-20261014-v5.png
---

# ref-li2018-AE 内容与证据审阅记录

## 当前状态

独立科学内容审核已通过，准确范围与原冻结哈希见下文。真实封面已由根逐张审核并绑定双渠道；本次仅加入封面，不改科学正文、原图、表格或公众号。完整标准构建、浏览器实际视觉、部署及微信手机后台验收仍待，不提前标verified。Li2018-AE本轮范围为19页主文，不含用户已明确不需增加的外部代码/视频。

## 源文件获取记录

- 元数据依据现有论文条目、出版注册表与PDF首页。题名、作者、期刊、年份、DOI相符。
- 使用授权团队原论文清单中19页出版社排版PDF；当前副本与来源清单SHA相同。未另行下载、未访问Zotero Desktop Local API或Zotero Web API `/file`。
- 原PDF、逐页渲染、原始文本、pdfimages原生图、覆盖审计及整合清单均存私有区，不发布主PDF或原始抽取文本。
- 图像先用pdfimages抽取，图3、15、20、25采用完整原生位图；其余为矢量或混合图，采用页面局部裁切保留全部标签。图21、22虽有嵌入位图，但外部Zero/Optimized标签为页面矢量内容，最终改用完整局部裁切，未用缺标签的原生位图冒充完整原图。
- 27张最终图逐幅查看；图2上方图例、图10上沿、图21–22外部标签修正后重新查看。未重绘科学图、未以生成图替代原图。
- 外部补充材料范围：PDF file page 4第2.2节明确写MATLAB候选曲线生成代码见Appendix A；PDF file page 17仅给出“Appendix. Supplementary materials”及[DOI补充材料入口](http://dx.doi.org/10.1016/j.apenergy.2017.12.035)，没有代码正文。第4.3节（PDF file page 13）另提及流场动画补充数据。当前未取得代码或动画，按本轮用户明确决定不再获取，不作为主论文范围完成的阻塞项。

## 关键事实证据定位记录

- 作者、摘要、关键词、4项研究要点及日期：PDF file page 1。完整符号表在PDF file page 2，共26组条目。
- 流入角、攻角与桨距角定义：PDF file page 2–3，图1、式(1)–(4)。叶片后缘向中心转动时桨距为正。
- 五参数等效表达、控制点保留比例及三次样条：PDF file page 3–4，式(5)–(7)、图2；不是五个离散桨距角。
- GA-CFD联接、目标与约束：PDF file page 4–5，图3、式(8)、表1；20个体、50代、代沟0.8、5变量、12位精度。
- 模型几何：PDF file page 5–6，第3.1节、表2；NACA0018、3叶片、半径1000 mm、弦长100/200 mm，表中实度0.15/0.3。二维模型不含支撑臂的三维气动效应。
- 计算域、边界、滑移/重叠网格、动态变桨实现：PDF file page 6–7，第3.2–3.4节，图4–5。
- 网格、时间步、迭代数、阻塞比及周期检验：PDF file page 7–8，第3.5节、式(9)–(11)、图6–10。
- 零桨距风洞验证：PDF file page 8–9，第3.6节、图11–13。不同力分组测量，左右列TSR略不同；二维CFD低估零桨距总功率系数，低TSR失速段存在非规则波纹。不能称最优变桨方案已获试验验证。
- 最终CFD设置：PDF file page 9表3；108886单元、DDES-SST、T/720、每步10次、6周初始化、3周性能评价。
- 八个叶尖速比及两种弦长：PDF file page 9–12，图14–18、表4。0.177和0.317是平均功率系数的绝对增量，而非相对百分比。
- 最大CP为0.638和0.718及超过Betz极限的谨慎解释：PDF file page 11；原文同时指出数值误差可能高估，尚无变桨试验支持，不得当成实机效率证明。
- 正弦变桨比较：PDF file page 11–13，第4.2节、式(12)、图19–20。200 mm模型，正弦方案优化幅值；10代、164个个体。高四档TSR下非零幅值正弦变桨不及零桨距。
- 低TSR失速与高TSR背风能量机制：PDF file page 13–16，第4.3节、图21–24；两代表工况为100 mm/0.82与200 mm/3.43。
- 优化性能与计算成本：PDF file page 16–17，第4.4节、图25–27；每工况约145小时，普通工作站，50代；不是在线实时控制速度。
- 第5节完整结论及未来变桨试验需求：PDF file page 17。参考文献1–77在PDF file page 17–19。
- 图页对应：图1 page 2；图2 page 3；图3 page 4；图4 page 6；图5–6 page 7；图7–10 page 8；图11–13 page 9；图14–15 page 10；图16 page 11；图17–19 page 12；图20 page 13；图21 page 14；图22 page 15；图23–25 page 16；图26–27 page 17。

## 原文疑点与编辑处理

- 第3.1节文字的第二个实度写0.03，表2为0.3。RTD忠实保留并注明冲突；导读采用可由几何参数核查的表2值0.3。
- 第3.2节将包含网格细节的子图称为Fig.4(c)(d)，实际为图5相应子图。正文保留原指称并注明。
- 第4.1节200 mm模型最大功率系数增量位置写TSR4.47，而表4和结论为4.94，对应0.487。RTD保留两处并注明；导读不混用这组数值。
- 式(8)约束范围说明中原文写αu和αd，与诱导因子a的前文符号疑似不一致；不静默重写原文。
- 第4.3节Amet与Sagharichi均标文献[77]，但[77]作者为Amet等。保留原引用并指出重复编号。
- 图3首代判断节点的Yes/No与后续“由上一代建立新一代”文字存在逻辑疑点；原图和全部节点翻译原样保留，不能仅据此保证实现正确。
- 两个数值最大功率系数高于传统Betz值；完整保留原文解释和反向限制，不替作者删去不确定性，也不作物理突破结论。

## 工程叙事证据卡

旋转过程中攻角变化及迎风尾流使背风气动复杂 → 用五参数表达并光滑整周桨距 → GA结合经过零桨距试验对照的二维CFD寻优 → 低TSR推迟失速，高TSR改善背风来流与转矩 → 改善属于数值模型的受限结果，最优变桨试验、三维效应、机构执行和科学代码附录不在本轮范围内。

## 写作与方向审校

保留注册表主归属海上漂浮风电 / 一体化分析，并明确这是一篇风机气动与控制关联基础研究，不误称海上浮式系统验证。独立导语、忠实摘要、研究问题与解决思路及四个具体正文节，不以导读扩写RTD。导读使用图2、17、23，alt与紧随图题逐字一致。作者字段及原论文作者不改，文末仅一次“本文由 AI 辅助整理与撰写”；RTD不新增该声明。

## 本轮封面简报

- 本轮已获文案据原文自行拟定复核、工程插图imagegen、文字标签固定排版授权，不延伸为永久规则。
- 采用文案：一体化分析 | 变桨曲线怎样选 / 用五个参数连接气动与寻优。
- 期刊年份：Applied Energy · 2018。
- 工程场景：三片直叶片H型VAWT的转子平面及叶片局部转角，背景可有简洁尾流；依据PDF file page 2图1、page 6图4、page 10图14和page 16图23。可用少量俯视翼型表现迎风/背风桨距差别，不伪造原论文曲线或定量云图。
- 机制锚点：整周桨距不是一条简单正弦；迎风侧抑制分离，为背风侧保留更高来流速度；示意图只解释关系，不宣称测得效率。
- 禁止误画：水平轴三叶大风机、漂浮平台、系泊线、海浪、桨叶扭转成水平轴、额外叶片、0.718实测效率标牌、突破Betz证明、实时控制器已部署、捏造设备照片。
- 最终900×383，160×40固定方向标签，深蓝/黄系列；文字由固定排版覆盖。当前未生成，后续仍需尺寸测量、科学场景复核与手机实际预览。

## 覆盖与检查

主PDF全文科学内容包括4条要点、摘要、关键词、26组符号、第1–5节全部自然段与两组编号结论、式(1)–(12)、图1–27、表1–4及参考文献1–77。按项目规范省略致谢与声明性补充材料尾注，但仍说明其所指科学代码附录A未纳入：主PDF覆盖完成不等于全部外部科学材料已取得。按用户明确缩小后的本轮范围，主论文内容制作完成；full_paper_coverage不用于宣称附件已覆盖，authorized_main_pdf_scope_complete为true。最终封面、独立科学复审、Sphinx集成以及微信手机浅/深色预览均尚待分别完成。

## 2026-10-14 方向字段格式修正

方向行改为注册表要求的半角冒号及精确一级/二级值；关联基础研究边界如有则移到独立段落，不改变其含义。未改论文作者、摘要、科学正文或原图。既有科学审查的内容范围不扩张；当前公众号文件 SHA-256 为 `a46ccbf24e72f3ffe93859f6e850a1db563f08ea2042963f22953730db237683`。

## 本轮正文图上传许可

2026-10-14本轮明确要求完成所选27篇双渠道内容并制作公众号草稿，许可范围包含这些论文原图用于对应草稿的必要上传。`body_images_upload_approved: true` 仅记录这一许可，不表示图片已经上传、草稿已经建立、科学审核通过或后台预览通过；正式发表仍不在自动执行范围。实际后台操作由统一交付流程执行。

尾部范围复审：已核对PDF file page 17。依项目全文精解规范排除致谢及声明性补充材料尾注，不计为科学正文遗漏；原科学正文中的附录提及及本轮不含外部代码/视频范围说明仍保留。

## 2026-10-14 独立科学内容审核通过（主论文范围）

由非本篇撰稿者逐页核对19页主论文、91个科学段落、12公式、4表全部数值、26符号、27幅最终原图、77参考文献及公众号全文。图3分支说明已按原图恢复并复验，原文疑点明确保留。致谢及补充材料入口等声明性尾注按项目规范排除，不属于科学遗漏。本轮范围不包含外部MATLAB代码或视频，不宣称已取得或译完这些附件。

科学内容通过不代表原模型已独立重算，也不代表封面、HTML/公式排版、全站构建、部署、后台及手机浅/深色验收。以下哈希锁定本次审核范围；后续变化按范围重审。

- `docs/source/paper-notes/ref-li2018-AE.rst`：SHA-256 `3da1de7d6e68513ca58d43bf293a61f0dacf0c67c84d016a50a8cbdc0364efc4`。
- `wechat/articles/draft-public-safe/ref-li2018-AE.md`：SHA-256 `b8a4e3827ab1a5f3b96e226a80bf3bde0367ba57055486bc04cc343e0b600b1b`。
- `wechat/assets/public-safe/ref-li2018-AE/fig01.png`：SHA-256 `3466880b108033d7e2b886ad187ff2597a15736724c700efb58ca40c6e15d23a`。
- `wechat/assets/public-safe/ref-li2018-AE/fig02.png`：SHA-256 `e715fbd2a1e1c896914494a345c9626a8b481870b1e4cd1c2324f4093a338add`。
- `wechat/assets/public-safe/ref-li2018-AE/fig03.jpg`：SHA-256 `b0f76acefe4091a8695042eae2150bc8337deab1b560cae70b76036c460c68bd`。
- `wechat/assets/public-safe/ref-li2018-AE/fig04.png`：SHA-256 `ef5628a0a918c9f635145224c6681de771a43c6024bf8bcda832751e0badf9a1`。
- `wechat/assets/public-safe/ref-li2018-AE/fig05.png`：SHA-256 `00502784c3ca3bd622fdd35ddd8623ed3352bf46e6cb4134d71847e65f4b51e6`。
- `wechat/assets/public-safe/ref-li2018-AE/fig06.png`：SHA-256 `b8a0ba746918941f9e666ff89600350d34350f10cad4f61bad8ca3470a6ab920`。
- `wechat/assets/public-safe/ref-li2018-AE/fig07.png`：SHA-256 `1b446a022431f0a123aad282d6587dcfe7b2ec8a46954f093db81d65445f13db`。
- `wechat/assets/public-safe/ref-li2018-AE/fig08.png`：SHA-256 `89dfb2efd5b1e11f9a0fa4f439cf75fb70f9032f06409cdf58d6112a373b8c95`。
- `wechat/assets/public-safe/ref-li2018-AE/fig09.png`：SHA-256 `2f145e0d48e3cf99c37078baca97d543da006404c5445e1c815703d369cc6deb`。
- `wechat/assets/public-safe/ref-li2018-AE/fig10.png`：SHA-256 `1772bdf47d7c514fb4fbe2e7cec56e83449bc95e1e0bfe6ae552176bc68b6c54`。
- `wechat/assets/public-safe/ref-li2018-AE/fig11.png`：SHA-256 `7c10f380f321792b7cb8e0b4c58b1d2dace4358b82ff3733dd98129c147faa36`。
- `wechat/assets/public-safe/ref-li2018-AE/fig12.png`：SHA-256 `065d49aab27fba431bef82cab930cf8be06ff833a76247910518526062c68c46`。
- `wechat/assets/public-safe/ref-li2018-AE/fig13.png`：SHA-256 `23468ca9e6df26dcf441276728613097e5f06cc058f021e7c4e47c1490b4debe`。
- `wechat/assets/public-safe/ref-li2018-AE/fig14.png`：SHA-256 `e196ed140f91b34028e22c61a426cb1eea1cfc4debfa8a2a18737e33b9a382cc`。
- `wechat/assets/public-safe/ref-li2018-AE/fig15.jpg`：SHA-256 `97588030b90f9bc89f72bffacef77665b041bb77fc0cf0fd22c21e6ed907feae`。
- `wechat/assets/public-safe/ref-li2018-AE/fig16.png`：SHA-256 `aa2e36b1572897e2f6d43d54da69a9d8b7dfee5a8bf8a23978b0e07e4bb022c7`。
- `wechat/assets/public-safe/ref-li2018-AE/fig17.png`：SHA-256 `a0cf4e7d0dc197f7b2589d96c2fd15879594625e65913f6c21a515b65be92b6a`。
- `wechat/assets/public-safe/ref-li2018-AE/fig18.png`：SHA-256 `1586b8d8c47b157ba5d0776b003444a683f2e70fc3b4c49bbdf103a18c2e28e9`。
- `wechat/assets/public-safe/ref-li2018-AE/fig19.png`：SHA-256 `513005ed1ba992484edc4056e9bac1f77fb51471435a2f14b7e9ec0308c45f1e`。
- `wechat/assets/public-safe/ref-li2018-AE/fig20.jpg`：SHA-256 `d144debc7ab9d74a361d5e647c3bde47d3253d2eb2895e1bf46d9b0d8da86a5b`。
- `wechat/assets/public-safe/ref-li2018-AE/fig21.png`：SHA-256 `c60e8b8da78ca892b13cc38244db0798f45552eeef9c27ef95b80e2d5eb232d2`。
- `wechat/assets/public-safe/ref-li2018-AE/fig22.png`：SHA-256 `fb571ad208c20370b8db0d253d392f2dfce5ca802adb06fb98ebadfef86690f9`。
- `wechat/assets/public-safe/ref-li2018-AE/fig23.png`：SHA-256 `95f6750d9ad4ab73eaed0d65fcc67f6b0acfc3228a93807f7c1d1203a8071f5e`。
- `wechat/assets/public-safe/ref-li2018-AE/fig24.png`：SHA-256 `4404cccd97b158ca26af67a2c8f6dd95f560fa216cbeb74ed99099c5a571ec02`。
- `wechat/assets/public-safe/ref-li2018-AE/fig25.jpg`：SHA-256 `3a62bc62f4d15aa3258028fb52f04bd8e362834ddf64f98b4d535ca52a48f5be`。
- `wechat/assets/public-safe/ref-li2018-AE/fig26.png`：SHA-256 `cdd60b9c8cefa79163ea1cc46f31b32a3c4bf3ef4718f8903f62c41d7f3d2918`。
- `wechat/assets/public-safe/ref-li2018-AE/fig27.png`：SHA-256 `2334ff363b6d963473c24ed5fda6b2b83490c997d201ac3ae24eb60ca943f892`。

## 2026-10-14 真实封面绑定与精确等价

封面 `wechat/assets/public-safe/ref-li2018-AE/cover-wechat-900x383-20261014-v5.png` SHA-256 `c878f7f00a651fd9cf1ea86e3e5182ff46ce38858ca7167cab84906b227cc565`，brief SHA-256 `1970894c118f8737f790271b8e5ace8cb29242b93bcff41e475495fdb6f70564`，均匹配根逐图批准冻结清单。加图前RST `3da1de7d6e68513ca58d43bf293a61f0dacf0c67c84d016a50a8cbdc0364efc4`，加图后RST `243e86bc88fce26b75db8eb4aebc172f10997ea6827941455ce678199b221689`；去掉新增image指令块可精确恢复原字节，原科学审核范围不扩大。原图、科学公式、表值及公众号未变；不将本地封面审阅等同于手机验收。

## 2026-10-14 离线渲染、纯标记修正与冻结

官方 preflight、dry-run、academic-clean / MathJax SVG 渲染均通过；没有读取凭据、联系微信、上传或建草稿。公众号有3张正文图、0个行内SVG公式和0个独立公式块，图像嵌入、SVG几何及currentColor继承静态检查通过。已有可独立打开的390px浅深色容器对照，但不等于真实手机验收。

参照项目paper-inline-roles回归方法建立的四页最小Sphinx语法测试，以正常mathjax扩展和warnings-as-errors运行通过：无可见 :math: / :ref: 泄漏、无problematic或system-message。该最小测试不是全站构建，也没有通过禁用全站扩展声称标准门禁完成。页面包含28张图（含真实封面）、12个显示数学块、5个HTML表（4张原表及1张符号表），封面在目录前。

修正仅为行内math角色前后的分隔空白；Li2012-GCLX另延长标题下划线。去空白和标题下划线后的全文逐字符相同，公式LaTeX、原图、表值及公众号完全不变。修正前RST SHA-256 `243e86bc88fce26b75db8eb4aebc172f10997ea6827941455ce678199b221689`，修正后 `8759d17f4a6487471b26de4135551f9e49de531995bfb4c51f8e2c4931a426a4`；原科学审核范围保留，未将纯标记修正冒充新科学结论。

根已独立逐张看过最终封面，本次整合负责人也重新打开4张900×383实际PNG核对，哈希与源构型限制吻合。封面、静态SVG和语法测试均不能替代完整标准检查、真实浏览器、网站部署或微信后台手机浅/深色验收，相关flags保持未通过。
