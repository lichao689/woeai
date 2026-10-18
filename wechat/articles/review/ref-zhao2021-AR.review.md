---
body_images_upload_approved: true
publication_ref: ref-zhao2021-AR
doi: 10.1016/j.atmosres.2021.105507
research_family: 工程结构抗风
subdirection: 数值风洞
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
cover_image: wechat/assets/public-safe/ref-zhao2021-AR/cover.png
---

# ref-zhao2021-AR 内容制作记录

## 正文文件

- 独立全文：`docs/source/paper-notes/ref-zhao2021-AR.rst`
- 公众号：`wechat/articles/draft-public-safe/ref-zhao2021-AR.md`
- 原图：`wechat/assets/public-safe/ref-zhao2021-AR/`，图 1–18。
- 真实封面与科学简报已由封面审核确认并集成；正文科学审核、离线排版和实际手机验收分开记录。

## 源文件获取记录

- 元数据来源：项目注册表、学术成果条目、PDF 首页。
- 附件记录：本轮提供的作者团队原文清单，未访问 Zotero Desktop 或 Web API。
- 本地 PDF：完整可读，共 18 页。
- 选用版本：作者团队提供且授权复用的出版社排版原文；未提供另一个可优先选用的作者终稿。
- 私有存储类别：私有论文来源及本轮制作记录；PDF、原始全文、截图、源哈希和清单均不进入公开仓库。
- Zotero Web API `/file`：无需。
- 网页 PDF 下载：未使用。
- 摘要依据：PDF file page 1。
- 正文依据：PDF file pages 1–18，包括结论后的附录 A 科学符号表及参考文献。
- 图片依据：先 pdfimages 提取；18 幅完整嵌入原图以原始像素文件输出，未重采样或重绘。

## 关键事实证据定位记录

- 过指定侧边界、简单系统到真实地形的验证路径：PDF file pages 1–2，摘要与§1。
- 一维推导及波反射系数：PDF file pages 2–4，式 (1)–(19)。
- GA 配置、种群 500、相邻代停止条件 10⁻⁷、惩罚项10⁴：PDF file page 4，§2.3。
- 各层权重及前两层反射指标：PDF file page 5，表 1，a=4。
- 浅水算例网格40×40、间距10 km、步长10 s、积分3 h：PDF file pages 5–6，§3、式 (20)。
- 4/6/8 层最大残余扰动相对 L-93 差值23.5%/38.1%/50%：PDF file page 6，表 2；公众号限定为浅水试验，不推广成山地风速误差改善。
- TU-03B 时段、51层、WRF配置与初始化：PDF file pages 6–7，§4.1.1、表 3。
- 黏度一致性修正常数与模型方程：PDF file page 7，§4.1.2、式 (21)–(24)、表 4。
- 三维域11×12×1.8 km、最小水平网格17 m、第一层0.05 m：PDF file pages 7–8，§4.1.3。
- 边界源项、两类指定变量、质量守恒调整及时间插值：PDF file pages 8–9，式 (25)、表 5。
- WRF探空验证：PDF file pages 9–10，式 (26)–(28)、表 6、图 11。
- 0.6 km六层二维松弛、p_m敏感性、1.5–2 km影响范围及线性松弛副作用：PDF file pages 9–12，§4.3、图 12–14。
- 三维0.9 km松弛、p_m=0.05、s=6：PDF file page 12，§4.4。
- 不适定与质量守恒/松弛对比：PDF file pages 12、14，图 15；配置不止一个参数不同，公众号明确不做单因素因果归因。
- 背风侧DS(U)-MYJ最大k约3.04 m²/s²、实测4.87 m²/s²：PDF file page 14，图18；保留低估。
- 各工况统计表现：PDF file page 15，表 7。
- 热层结和重力波适用缺口：PDF file page 16，结论末段。
- 附录 A：PDF file pages 16–17，46项科学符号，完整可编辑转写；不因位于声明之后而删去。
- 参考文献：PDF file pages 17–18，共63条。

### 原图与表格定位

- 图1：PDF file page3；图2–3：page4；图4–5：page5；图6–7：page6；图8–10：page8；图11：page10；图12：page11；图13：page12；图14：page13；图15–16：page14；图17–18：page15。
- 表1–2：PDF file pages5–6；表3–4：page7；表5–6：page9；表7：page15。表6改为按工况逐行排列，全部数值和有效数字保留。
- 公式1–5：PDF file page2；6–18：page3；19：page4；20：page5；21–24：page7；25：page8；26–28：page9。

### 原文内部不一致与译文处理

- PDF file page3正文 B* 区间为[1/10,10]；page4图2–3图题写[1/10,1]。分别保留并加译注。
- PDF file page3式(15)第二个指数中，求和号外仍有 Δx_fn 的 n 下标；原文未说明，按原式保留，未改成猜测的 j。
- PDF file page7式(23)使用 Pφ、FφW，随后说明写 Pω、FωW；分别保留，并有译注。
- PDF file page9正文用ERR-J，表3/6为ERJ-J；正文称IOA大于0.85，表6最低为0.85。全文标出差异。
- PDF file page9 §4.3.1指六层方案“表2”，具体权重在表1，page11图12也引用表1；全文注明。
- PDF file page13写最大ΔS=2.2，但page15图17(c)近地曲线和横轴不支持该幅值；全文保留原句并指出图文差异，公众号不使用此数值。
- PDF file page15表7将无量纲ΔS的RMSE标为m/s；保留原表单位并明确说明，不擅自换算。
- PDF file page7科里奥利力表达式及附录符号按原文转写，不以教科书形式代替作者表达。

## 工程叙事证据卡

- 论证线：粗、细模型在地形和动力学上不一致，过指定边界可能反射与失稳；优化边缘松弛并配合质量守恒，再验证应指定哪些湍流量；平均风速合理仍不代表湍动能完全准确。
- 验证层次：一维解析优化、二维浅水反射、二维URANS敏感性、三维历史山地观测，不混淆各层的指标。
- 证据限定：浅水23.5%–50%不是真实风场通用改善；真实山地背风湍动能仍低估；仅近中性条件，热层结留作后续。
- 迁移要求：联合检查指定变量、松弛厚度与强度、模型常数、质量守恒及目标区域距边界的距离。

## 写作及图文审校

- 完整译文以源论文逐段写作，未从公众号导读生成；保留方法推导、全部28个编号公式、7张表、18图、附录46项及63参考文献。
- 公众号采用原图8、10、15、18；摘要之后设置“研究问题与解决思路”与四节具体论证。
- 18个最终原图文件均与源页和最终联系图核对，坐标、图例、分图、标尺、原图文字完整；非手机后台验收。
- 作者字段保持论文第一作者，完整作者名单与学生/通讯标记保持不变；末尾仅一次本轮明确要求的AI辅助说明。
- 未设未发布的延伸阅读；公众号不增加独立公式，只对变量和量纲使用LaTeX。

## 状态

- 完成作者侧源文核对、逐段译文和图文自查；没有声称独立科学审核通过。
- 独立科学复核和封面生成、固定排版及像素检查已完成；尚需标准全站构建、实际浏览器排版及微信浅色/深色手机预览。
- 未读取凭据、调用远程API、上传、建草稿、发布、提交或推送。

## 2026-10-14 方向字段格式修正

方向行改为注册表要求的半角冒号及精确一级/二级值；关联基础研究边界如有则移到独立段落，不改变其含义。未改论文作者、摘要、科学正文或原图。既有科学审查的内容范围不扩张；当前公众号文件 SHA-256 为 `0e52c48c893906ed50b1a73950897b0a5f4f2cb7cf66b0b64e4c3654b380b445`。

- 独立科学审核修订：式 (4)–(6)、对应解释与附录 A 恢复原版的误差横线及精确解估计横线；附录均匀流符号恢复大写 U 的横线。待审核方复验。

## 2026-10-14 独立科学内容审核通过

已独立逐页核对18页原PDF、28公式、7张表、18幅最终原图、46符号附录、63参考文献和公众号全文。式4–6及附录横线已恢复并复验；公众号4图链接后缀已更正且全部存在。 科学内容审核通过不等于原模型独立重算，也不代表封面、HTML/公式排版、全站构建、部署、后台和手机浅/深色验收。以下哈希锁定本次内容与图像范围，后续变化须按范围重审。

- `docs/source/paper-notes/ref-zhao2021-AR.rst`：SHA-256 `39bdb4b4a9556b2bf711a5ea4e05ec5185a5cb4ef43a3b977b5c4280185a0724`。
- `wechat/articles/draft-public-safe/ref-zhao2021-AR.md`：SHA-256 `56a30c3c0e16d2c9ac5168360131e52719271450e863c4151247596caaee5db9`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig01-original.jpeg`：SHA-256 `5c8b70ffbc9824a683fa9ca80298140dc0077cc69c0cabdf0434ee257bcedce2`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig02-original.jpeg`：SHA-256 `af57bca8f94f5e1b17cdbe2bcf82a4e3fed3d47e20a313233aacdb4a7cc9d7c8`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig03-original.jpeg`：SHA-256 `fc25bf1e30fbaed59c4953ef9a158d7d9ed7da9ccecd6b50933a208c1f453cc7`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig04-original.jpeg`：SHA-256 `3a4677cad684bc4c1a5839be90cb4fc7f681617e130f5061c27ad5fb1799cafb`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig05-original.jpeg`：SHA-256 `872479db20a7db1831f9406f007355db8a5c60979d741abdcc2b481c80d30715`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig06-original.jpeg`：SHA-256 `085bb2f0a3075f60448ccaad73c361b1989a5e24bd77acd3cf6e96df8654e5aa`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig07-original.jpeg`：SHA-256 `b83bec9ab8fee48502128fb996a9fa8db8231b4b9a8bcec57d1e760ae6cdccf3`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig08-original.jpeg`：SHA-256 `e5f3b46e7d54dc7cd59b78574cbb45d1665106ebbb2521072e5346efdc2d9878`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig09-original.jpeg`：SHA-256 `522ad0b659f595fdde34a2b184a092561d5a4cbcbc047949506a8975e28c4ac2`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig10-original.jpeg`：SHA-256 `9f0e025075e07eaebfa780ece8468a7bc27e7d7b7bf17feb9721728b779c56b3`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig11-original.jpeg`：SHA-256 `9b4663da7d11e75d568349e9327a8d39583ede270cecb4afe54d7748d1072a8c`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig12-original.jpeg`：SHA-256 `5dc8382f1e03cd6052d85be331ba089f25d2351d5afd9fd2d3bf34203022fb4a`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig13-original.jpeg`：SHA-256 `3aa118ec59439b5d61ad6aac2620ba4ae7d0fecc11a6bc731089469e231f198a`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig14-original.jpeg`：SHA-256 `32abebf4235e1b650b2ec4c667a963234b08dbe4c02563fc2cc078fd7f356597`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig15-original.jpeg`：SHA-256 `d2d419de5d8373a31f562a572794311699cc42f5ac1be618be8f14a44d584439`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig16-original.jpeg`：SHA-256 `0464bad388a63eae1a57d5cf71c2dc0e88b406885670090d8c1ed9ae3064aea5`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig17-original.jpeg`：SHA-256 `8f9dd8b1870607ba8647b53d4986b02e3d1f20398cd7d90e694dc748112cdd65`。
- `wechat/assets/public-safe/ref-zhao2021-AR/fig18-original.jpeg`：SHA-256 `d6283db3feeb8ff2261ff82d903d1b759a845ce2c42fb6d6c52e0734ed974b22`。

## 本轮正文图上传许可

2026-10-14本轮明确要求完成所选27篇双渠道内容并制作公众号草稿，许可范围包含这些论文原图用于对应草稿的必要上传。`body_images_upload_approved: true` 仅记录这一许可，不表示图片已经上传、草稿已经建立、科学审核通过或后台预览通过；正式发表仍不在自动执行范围。实际后台操作由统一交付流程执行。

## 2026-10-14 真实封面集成与非内容等价检查

真实封面 `wechat/assets/public-safe/ref-zhao2021-AR/cover-wechat-900x383-20261014-v5.png` 的 SHA-256 为 `17507665d9e2db2f917a43a9e6007139039d4eb009908afc80c2267ce6ea246e`，与根审核冻结清单一致；公开封面简报 `wechat/assets/public-safe/ref-zhao2021-AR/cover-brief.md` 的 SHA-256 为 `12e0da49641ae34ce1c63f3401052a97f38bee5d926e1346d5c39de8d8e148c6`，同样匹配。封面置于“精简版微信公众号文章：待发布”之后、目录之前，双渠道使用同一真实资产。

加封面前 RST SHA-256 为 `39bdb4b4a9556b2bf711a5ea4e05ec5185a5cb4ef43a3b977b5c4280185a0724`；仅加封面后为 `3628a2ff03337b36f1b7f560c1dd421ad9cff7a05917403b9d2012ae5fc01751`。删除新增封面指令块可精确恢复加图前字节。随后只为 RST 解析补数学角色后的分隔空格、延长过短标题下划线，未改科学文字、LaTeX、表格、原图或公众号；去空白及标题下划线的逐字符比较一致。当前 RST SHA-256 为 `fa72fc4da5444a8e71457d799154358979fb9ac238ba61a664982eb65b0d946d`。既有独立科学内容审核保留原范围，不把封面集成说成新全文审核。

本轮文案由明确授权的编辑选择，工程插画与固定文字分层制作；本地独立封面审核通过不等于后台手机预览。

## 2026-10-14 本批官方离线预检与冻结

- 官方 `preflight`、`dry-run` 与 `render-copy-ready.py`（academic-clean / mathjax-svg）均通过。本次未读取凭据、未联系微信、未上传或改后台草稿。
- 公众号 HTML 含 12 个行内公式、0 个独立公式块、4 张正文图。逐个 SVG 静态核对 LaTeX 元数据、viewBox 和路径几何，以及首层 g 的 fill/stroke 属性和内联样式均继承 currentColor，全部通过，未见 MathJax 错误；正文图全部嵌入 HTML。
- RST 诊断 HTML 含 19 张图（包括真实封面）及 28 个显示数学块；9 个 HTML 表格对应原文 7 表及拉丁/希腊符号附录两表。本篇无 system-message 或 problematic 解析节点，真实封面在目录之前。当前仅留待注册表整合后生成目录的 toctree 接入警告。
- 根已独立审定封面，本文作者另再次打开最终 900 × 383 图核对文案与场景；封面与公开简报 SHA 均和冻结清单匹配。
- 工作区全局公共安全检查仍因其他待制论文缺真实封面而失败，不据本篇通过称全站通过。局部 Sphinx 禁用 sitemap 只作为解析诊断，绝不是标准构建验收；完整标准脚本交指定环境执行。
- 已生成 390 px 浅/深色容器诊断 HTML，供指定浏览器 QA 打开核对。当前环境不能取得真实浏览器渲染截图，本批未重复尝试先前受阻操作；浅深色、公式细节、长表和原图实际显示均待指定环境复验，不将静态 SVG 检查或容器模拟称作手机验收。
- 实际微信后台、手机浅/深色预览与发布未执行。科学审核保留原有范围，不扩称公式渲染或 backend 验收。
