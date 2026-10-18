---
publication_ref: ref-li2013-RE
body_images_upload_approved: true
cover_image: wechat/assets/public-safe/ref-li2013-RE/cover.png
---

# ref-li2013-RE 内容与证据审阅记录

## 当前状态

独立科学内容审核已通过，准确范围与原冻结哈希见下文。真实封面已由根逐张审核并绑定双渠道；本次仅加入封面，不改科学正文、原图、表格或公众号。完整标准构建、浏览器实际视觉、部署及微信手机后台验收仍待，不提前标verified。

## 源文件获取记录

- 元数据依据：项目现有出版注册表、学术成果条目及论文首页。题名、作者、期刊、年份与DOI已核对；现有学术成果条目卷号后出现指标样式的括号，本稿按PDF采用卷51、页317–330，不据此改动全局注册表。
- 附件依据：现有授权团队论文清单。本轮直接使用工作区已有作者团队论文PDF，为出版社排版版；未发现本篇可用的更高优先级作者稿。
- 本地PDF状态：14页完整可读，正文、结论和参考文献均可读取；当前副本与清单原始来源的字节哈希一致，详细哈希仅留在私有记录。
- 私有存储类别：授权原论文、原始文本抽取、逐页渲染、图像抽取中间件、覆盖审计及整合清单。
- Zotero桌面附件API：本轮未访问。Zotero Web API `/file`：未尝试。网页PDF下载：未使用。
- 摘要、正文、图题、公式和参考文献均依据完整PDF；公众号导读不作为RTD译文的来源。
- 原图复用依据：已授权的团队作者论文。先执行嵌入图像抽取；图4、9、10、13、14、19、20使用原生嵌入图像，其他图因坐标、曲线和标注为矢量而采用页面局部裁切。

## 关键事实证据定位记录

- 原摘要：PDF file page 1，完整忠实翻译；2.5D不能捕捉叶尖与竖向发散的限定保留。
- 单翼型设置：PDF file page 3–5，第2.1节；NACA0018，来流22.2 m/s，雷诺数300,000，展向2c，40层。
- 单翼型网格与转捩边界：PDF file page 5–7，第2.2节，图5–8；完全湍流模式，不模拟层流分离泡。
- 失速后涡结构与壁面压力：PDF file page 6–8，图9–11。
- 旋转风机几何：PDF file page 8–9，第3.2.1节，图12–14；半径1.4 m、来流10 m/s、修正弦长420 mm、无支臂模型。
- 试验法向力均值由计算结果辅助调整：PDF file page 10，第3.3节首段。导读将其作为独立验证边界明确保留。
- 四组力系数：PDF file page 10–11，图15；图中为0.70、1.11、1.46、1.96，后文另提1.81时背风峰值，不擅自删除。
- 功率公式(5)–(6)及14.5%误差：PDF file page 11，图16；从叶尖速比1.32开始的URANS高估亦在本页。
- 动态失速机制：PDF file page 11–13，图19–20；低速相对更好，高速背风第二峰未复现的结论见PDF file page 14。
- 公众号使用原图1（PDF file page 2）、8（PDF file page 5）、16（PDF file page 11）、19（PDF file page 12）。
- RTD图号与物理页：1–2：page 2；3：page 3；4–5：page 4；6–8：page 5；9：page 6；10–11：page 7；12–13：page 8；14：page 9；15：page 10；16–18：page 11；19：page 12；20：page 13。
- RTD公式(1)–(2)：PDF file page 2；(3)–(4)：PDF file page 9；(5)–(6)：PDF file page 11。无新增编辑解释式。

## 原文疑点与保留方式

- PDF file page 8称0.82 m为两倍弦长；同页及图12又给修正弦长420 mm。两者按原文保留，不替原作者改算；公众译文就近注明两处数值不完全相符。
- PDF file page 1“Available online”后未列日期，因此不编造在线日期。
- PDF file page 14文献[2]保留原文缩写页码1087–109，不擅自补成其他页码；文献[38] DOI排版空隙仅去除断行空格。
- 图8横轴画至180°，正文模拟范围为0°–140°，导读依正文写法，未扩大计算覆盖。

## 工程叙事证据卡

二维计算的功率偏高不能只归因于叶尖损失 → 同时改变计算维度和湍流方法，以静止翼型及旋转叶片两级验证 → LES对失速后的三维涡扩散及动态失速时刻再现较好 → 低速载荷预测较好，高速背风峰值和完整有限展长系统仍不在已验证范围内。

## 研究方向与写作审校

保留海上漂浮风电 / 一体化分析，作为已批准的风机气动关联基础研究。正文与封面不得暗示浮体、系泊或海上系统试验。摘要逐句对应；导读按“研究问题与解决思路＋四个具体章节”组织，数字均保留指标与工况。首次解释必要术语；没有口号式创新声明，没有把潜在自启动用途写成已验证的自由启动过程。法向力校正、完全湍流假定、无支臂与叶尖模型等限制就近呈现。

## 本轮封面简报

- 本轮用户明确授权：由助手依据原文拟定并复核主副标题，不再逐篇五选一；工程插图使用imagegen，文字和方向标签采用固定排版。仅适用于本轮，不视为永久规则。
- 选定文字：一体化分析 | 功率为何算高了 / 高攻角流动的涡结构检验。
- 期刊年份：Renewable Energy · 2013。
- 场景：一段直叶片翼型与迎风分离涡，突出二维平滑涡与三维破碎涡的示意对照；依据PDF file page 6–7图9–10。对照仅为机制示意，不画虚构数值曲线。
- 可用辅助对象：图1的三叶片垂直轴转子俯视轮廓。不是水平轴三叶片风机。
- 禁止误画：海浪、漂浮平台、系泊、发电量提升比例、真实叶尖涡、完整海上机组部署；不得把2.5D描述为完整三维模型。
- 画布与标签：最终900×383；一体化分析深蓝/黄色系列；固定标签160×40；固定排版后仍需实测、视觉复核与手机预览。
- 当前状态：文字已在本轮批量授权内选定；工程插图未生成；最终封面未验收；后台预览未执行。

## 覆盖与检查

全文覆盖包含原文摘要、关键词、第1–4节、全部原图1–20、公式(1)–(6)、参考文献[1]–[39]。无表格、无附录、无符号表。原文致谢按项目规范不进入公开译文。段落级覆盖与源副本哈希记录在私有审计中。最终顶部封面、独立复审、Sphinx集成检查、微信浅色/深色实际手机预览仍须分别完成，不把文件存在视为核验完成。

## 2026-10-14 方向字段格式修正

方向行改为注册表要求的半角冒号及精确一级/二级值；关联基础研究边界如有则移到独立段落，不改变其含义。未改论文作者、摘要、科学正文或原图。既有科学审查的内容范围不扩张；当前公众号文件 SHA-256 为 `37a71b9b0d70151d1890658acd30326def5b7a52077f24fbd397bb571bbd6361`。

## 2026-10-14 独立科学内容审核通过

独立复核覆盖14页全部原文、6公式、20幅原图、39参考文献和公众号全文。高叶尖速比符合程度、未模拟叶尖/支撑臂及法向力均值重调整等限定保留。 科学内容审核通过不等于原模型独立重算，也不代表封面、HTML/公式排版、全站构建、部署、后台和手机浅/深色验收。以下哈希锁定本次内容与图像范围，后续变化须按范围重审。

- `docs/source/paper-notes/ref-li2013-RE.rst`：SHA-256 `1d642dae79d858ddc11d4194f00b681b25c366d09748c85f26dfbb188bcc231c`。
- `wechat/articles/draft-public-safe/ref-li2013-RE.md`：SHA-256 `37a71b9b0d70151d1890658acd30326def5b7a52077f24fbd397bb571bbd6361`。
- `wechat/assets/public-safe/ref-li2013-RE/fig01.png`：SHA-256 `4b8e700514d522aea562c9badce5492cb9f10b38de484d6b526af367e53c5526`。
- `wechat/assets/public-safe/ref-li2013-RE/fig02.png`：SHA-256 `9c049aec05624cd136956091e9c74503e7d9064ac61d40ea5640533bda1e177c`。
- `wechat/assets/public-safe/ref-li2013-RE/fig03.png`：SHA-256 `7db79c6eb50c16a3863b5689f2ae5eb2855d38eae2ed750cc6978ae2bde06a46`。
- `wechat/assets/public-safe/ref-li2013-RE/fig04.jpg`：SHA-256 `205ccc0cf8589e7b2ee3cf07501c0c3d5e5e2215f028dd5b98af93e933d449b6`。
- `wechat/assets/public-safe/ref-li2013-RE/fig05.png`：SHA-256 `45a20796f50e61a8a7e68c4cd8ec3dddb5501690997a28ceec14825542e6ab44`。
- `wechat/assets/public-safe/ref-li2013-RE/fig06.png`：SHA-256 `00c9d9e25b27e0c86de97117f24ce6d8837348d819fec06c5f1c1e059d5a5208`。
- `wechat/assets/public-safe/ref-li2013-RE/fig07.png`：SHA-256 `8fd190db471f56a3520bec013d4d30a72d5fe3ce791d14d0515c47df770f6cfd`。
- `wechat/assets/public-safe/ref-li2013-RE/fig08.png`：SHA-256 `de105f9f9dc9f24080d184157d5b0e2c477d8fb67f7ad117c7e531b89a2ff447`。
- `wechat/assets/public-safe/ref-li2013-RE/fig09.jpg`：SHA-256 `e83f73d2298f7d00b8ddf713aad29e96e3eb8920072adcc0d5ea53e515dbb525`。
- `wechat/assets/public-safe/ref-li2013-RE/fig10.jpg`：SHA-256 `975fa11b29d792d09d5208bce179e0f9d69b416dff8abe018e946c849d698f3a`。
- `wechat/assets/public-safe/ref-li2013-RE/fig11.png`：SHA-256 `7db896ce8d8ff215a0d9d933eeed448e52a6a70ccbfdfe65ad1d2853f965d2a7`。
- `wechat/assets/public-safe/ref-li2013-RE/fig12.png`：SHA-256 `cfb41059d46bebee0e51d712f3403a43e87583b2a1721abcda8e613aa9544405`。
- `wechat/assets/public-safe/ref-li2013-RE/fig13.jpg`：SHA-256 `f9d16743bde375bc2530f38da5a4b6218d1dbce6e535ee2ee1c9b5eade27dbd0`。
- `wechat/assets/public-safe/ref-li2013-RE/fig14.jpg`：SHA-256 `6fb69c7edfd89b4dc93ec04fb86fb9a289b9d459183f65c2237d0ee0e75fa7a1`。
- `wechat/assets/public-safe/ref-li2013-RE/fig15.png`：SHA-256 `7df85e4db7bee08e6508091c85058b9c3700f79dbc793781700fa1b9ff07c199`。
- `wechat/assets/public-safe/ref-li2013-RE/fig16.png`：SHA-256 `5a924a15082e66e147f8aa775afa8d95fac2b9935ab2daec0c1b346b08d58d16`。
- `wechat/assets/public-safe/ref-li2013-RE/fig17.png`：SHA-256 `a5b3dd8628b41e68de298918340ba5066ecd71d041b362af672bbe45accaca82`。
- `wechat/assets/public-safe/ref-li2013-RE/fig18.png`：SHA-256 `bf29e8b58c3096e33eadfce8ce13b2ebc42d01c4e5387b8c0dff7e9480031918`。
- `wechat/assets/public-safe/ref-li2013-RE/fig19.jpg`：SHA-256 `ea1a3a9c70647b4d300c56b5ed5680b3538ca429dd7ba210dfa6141c6b311e40`。
- `wechat/assets/public-safe/ref-li2013-RE/fig20.jpg`：SHA-256 `4d874eee07d7c40974e9ff7a51bd6408afa4e6ab3435af669ee611dd0e7449d7`。

## 本轮正文图上传许可

2026-10-14本轮明确要求完成所选27篇双渠道内容并制作公众号草稿，许可范围包含这些论文原图用于对应草稿的必要上传。`body_images_upload_approved: true` 仅记录这一许可，不表示图片已经上传、草稿已经建立、科学审核通过或后台预览通过；正式发表仍不在自动执行范围。实际后台操作由统一交付流程执行。

## 2026-10-14 真实封面绑定与精确等价

封面 `wechat/assets/public-safe/ref-li2013-RE/cover-wechat-900x383-20261014-v5.png` SHA-256 `adc5f996e53d6363fef8b3c80953c4cd466711fac20aa9b69c762f1729d13958`，brief SHA-256 `8e9a2f9f4c983a3fd660b43bd888322a1e3b65222deb4cc11a8472dc46c0d1ac`，均匹配根逐图批准冻结清单。加图前RST `1d642dae79d858ddc11d4194f00b681b25c366d09748c85f26dfbb188bcc231c`，加图后RST `fdfb2b1bbd034ab4a8a9ef111ae70bd905c64f226efc97a06647eb40f1c0c2b8`；去掉新增image指令块可精确恢复原字节，原科学审核范围不扩大。原图、科学公式、表值及公众号未变；不将本地封面审阅等同于手机验收。

## 2026-10-14 离线渲染、纯标记修正与冻结

官方 preflight、dry-run、academic-clean / MathJax SVG 渲染均通过；没有读取凭据、联系微信、上传或建草稿。公众号有4张正文图、12个行内SVG公式和0个独立公式块，图像嵌入、SVG几何及currentColor继承静态检查通过。已有可独立打开的390px浅深色容器对照，但不等于真实手机验收。

参照项目paper-inline-roles回归方法建立的四页最小Sphinx语法测试，以正常mathjax扩展和warnings-as-errors运行通过：无可见 :math: / :ref: 泄漏、无problematic或system-message。该最小测试不是全站构建，也没有通过禁用全站扩展声称标准门禁完成。页面包含21张图（含真实封面）、6个显示数学块、0个HTML表（原文无表），封面在目录前。

修正仅为行内math角色前后的分隔空白；Li2012-GCLX另延长标题下划线。去空白和标题下划线后的全文逐字符相同，公式LaTeX、原图、表值及公众号完全不变。修正前RST SHA-256 `fdfb2b1bbd034ab4a8a9ef111ae70bd905c64f226efc97a06647eb40f1c0c2b8`，修正后 `59b69327c57238e894d93eb80d6f326fe69f1ca94e8dabad035993964fba961d`；原科学审核范围保留，未将纯标记修正冒充新科学结论。

根已独立逐张看过最终封面，本次整合负责人也重新打开4张900×383实际PNG核对，哈希与源构型限制吻合。封面、静态SVG和语法测试均不能替代完整标准检查、真实浏览器、网站部署或微信后台手机浅/深色验收，相关flags保持未通过。
