---
body_images_upload_approved: true
publication_ref: ref-li2017-BS
doi: 10.1007/s12273-017-0348-1
research_family: 工程结构抗风
subdirection: 数值风洞
publication_mode: first_publish
wechat_status: drafting
wechat_author: Li Chao
source_checked: true
copyright_checked: true
public_safety_checked: false
formula_preview_checked: false
figure_preview_checked: false
cover_image_checked: false
wechat_backend_preview_checked: false
rtd_page_checked: false
cover_image: wechat/assets/public-safe/ref-li2017-BS/cover.png
---

# ref-li2017-BS 内容制作记录

## 正文文件

- 独立全文：`docs/source/paper-notes/ref-li2017-BS.rst`
- 公众号：`wechat/articles/draft-public-safe/ref-li2017-BS.md`
- 原图：`wechat/assets/public-safe/ref-li2017-BS/fig01-original.png` 至 `fig17-original.png`。
- 真实封面工程插画与固定排版已完成并集成；后台和实际手机预览仍待，不是发布就绪。

## 源文件获取记录

- 元数据来源：项目注册表、学术成果页和 PDF 首页。
- 附件记录：已提供的作者团队原文清单；未访问 Zotero Desktop 或 Web API。
- 本地 PDF：存在且完整，共 16 页。
- 选用版本：作者团队提供、获准复用的出版社排版原文；当前可用附件未另有优先作者终稿。
- 私有存储类别：私有论文来源与制作记录；原文、原始抽取、截图、哈希和清单不进入公开文件。
- Zotero Web API `/file`：无需。
- 网页 PDF 下载：未使用。
- 摘要与全文依据：PDF file page 1 摘要，PDF file pages 1–16 正文及参考文献。
- 图片依据：团队作者获准复用的原图；先用 pdfimages 提取，再按页面位置无重采样拼回原始条带。

## 关键事实证据定位记录

- 摘要：PDF file page 1。
- 本文为稳态 CFD–CFD，不是一次台风的 NWP–CFD 重演：PDF file pages 4、8，§3.1、§4.3.1。
- SE、SE1、WGL 测量高度及用途：PDF file page 4，§2.2、表 1。
- 三风向 70°、90°、110°：PDF file page 4，§2.1。
- realizable k–ε、SIMPLE、离散、残差、壁面处理与边界：PDF file pages 4–5，§3.1。
- 三套网格及边界层层数敏感性：PDF file pages 6–7，§3.3、表 2、图 7。
- 上游模型 2425 万网格、海面粗糙度 0.0002 m、U(10)=10 m/s：PDF file page 8，§4.3.1。
- FEP 的三个拟合粗糙度长度 2.176、1.180、1.250 m：PDF file page 9，§4.3.2。
- IMP 截面低风速区影响达平均海平面以上 600 m：PDF file page 9，§4.3.3，图 13 在 page 10。
- 15 m 高度云图 70° 工况两方法约 40% 与 80% 背景风：PDF file pages 10–11，§6.1、图 15；不写成台风实测差值。
- 一年资料、10 分钟平均、风向 ±5° 筛选及传播时滞：PDF file pages 11–12，§6.2。
- 阈值 5 m/s 时 FEP 约 12%、IMP 近 20%；20 m/s 时 FEP 37%；IMP 在 15、20 m/s 时低于 10%：PDF file page 12，§6.2、图 16。
- 样本总数 3531、1133、57、33；20 m/s 阈值、70° 风向仅 4 条：PDF file page 12，表 3。
- 代表范围和风向：PDF file page 13，§6.3、表 4、图 17。
- 中性假设、插值后动力学与质量守恒、热耦合和高频湍流缺口：PDF file page 14，§7。
- 原图定位：图 1–2 在 PDF file page 3；图 3 在 page 4；图 4–5 在 page 5；图 6 在 page 6；图 7–9 在 page 7；图 10–11 在 page 8；图 12 在 page 9；图 13–14 在 page 10；图 15 在 page 11；图 16 在 page 12；图 17 在 page 13。
- 公式：式 (1) 在 PDF file pages 6–7；式 (2) 在 page 8；式 (3)–(6) 在 page 9；式 (7) 在 page 10。全部转写为可编辑数学表达。
- 表格：表 1、2、3、4 分别位于 PDF file pages 4、6、12、13，全文均为可编辑表格。

### 原文差异及处理

- PDF file page 7，§3.3 称参考点为离地 82.7 m；PDF file page 11，§6.2 使用平均海平面以上 82.7 m，表 1 明确 WGL 离地 26.9 m、海拔 82.7 m。全文按原文保留并加译注，不擅自统一高度基准。
- PDF file page 11，§6.2 引用不存在的 §2.3；实际测站说明为 PDF file page 4 的 §2.2，全文注明。
- 原摘要说 400 m 内代表性良好，正文表 4 按风向给出不同、更大范围；公众号直接解释，不误写成所有风向上限均为 400 m。
- 原文“increasing wind speed removes thermal effects”是基于阈值的近似判断。公众号明确缺少稳定度资料，避免将筛选写成严格中性判定。
- 图 9(b) 图内称 blue line，正文称 dashed line；全文图注保留这项差异。

## 工程叙事证据卡

- 论证线：局部高分辨率模型仍可能因经验入口丢失上游遮挡信息；先模拟上游再传递入流，用不同筛选阈值下的实测风速比验证，随后评估测站空间代表性。
- 比较基线：FEP 采用相同位置 IMP 剖面展向平均后的对数拟合，不是任意选一个粗糙度作弱基线。
- 验证限定：三个固定风向、稳态中性 RANS、九龙湾具体地形；较低风速阈值下 FEP 反而更接近观测，正文未删除该结果。
- 原始样本数量随阈值锐减，不能只挑选最小误差；公众号同时列出总数和最少单组样本。
- 代表性无统一半方差阈值，作者承认主观性；不推广为通用城市测站标准。
- 潜在用途：长期全风向数据库是原文展望，不称本研究已经部署。

## 写作与原图检查

- 公众号忠实摘要后设置“研究问题与解决思路”，后续四节分别讨论入流信息、验证工况、阈值敏感性、代表性与局限。
- 公众号采用原图 9、15、16、17；全文使用全部 17 图。
- 17 图均由嵌入原始条带按页面顺序拼接，未重采样、未重绘；最终素材已逐图通过本地联系图与 PDF 页面范围核对，保留分图、坐标轴、图例、比例尺及原图内说明。
- 全文保留 7 个编号公式、4 张可编辑表格、49 条完整参考文献；没有附录与科学符号表。
- 公众号不增加独立公式，量纲及变量按 LaTeX 排版；没有延伸阅读链接。
- 审稿中的作者列表与投稿通讯标记依据论文和学术成果记录；未改成公众号编辑署名。

## 检查与待办

- 作者侧来源核对、逐段译稿、原图核图和写作自查已完成；随后独立科学内容审核也已通过，准确范围见日期记录。
- 独立科学审核与真实封面已完成；等待集成后的全站标准检查、实际浏览器排版与微信真实手机浅色/深色预览。
- 没有访问凭据、调用远程 API、上传、创建草稿、发布、提交或推送。

## 2026-10-14 方向字段格式修正

方向行改为注册表要求的半角冒号及精确一级/二级值；关联基础研究边界如有则移到独立段落，不改变其含义。未改论文作者、摘要、科学正文或原图。既有科学审查的内容范围不扩张；当前公众号文件 SHA-256 为 `f095cbd76ab76f423e8b937402be5c3e4db59bce7f47f22aeec81da3d1635222`。

## 2026-10-14 独立科学内容审核通过

独立复核覆盖16页全部原文、7公式、17幅原图、4表、49参考文献和公众号。1125m上游平坦段的误译已修复后复验。 科学内容审核通过不等于原模型独立重算，也不代表封面、HTML/公式排版、全站构建、部署、后台和手机浅/深色验收。以下哈希锁定本次内容与图像范围，后续变化须按范围重审。

- `docs/source/paper-notes/ref-li2017-BS.rst`：SHA-256 `6e20ab1709fed32fc2ea40352c45b87f4929814ff95b9626f4f5eee8f3590592`。
- `wechat/articles/draft-public-safe/ref-li2017-BS.md`：SHA-256 `f095cbd76ab76f423e8b937402be5c3e4db59bce7f47f22aeec81da3d1635222`。
- `wechat/assets/public-safe/ref-li2017-BS/fig01-original.png`：SHA-256 `47b467b4fe167c22e3ffd04f7fa3cf6d65b1a212365a163d999c66c2796750fd`。
- `wechat/assets/public-safe/ref-li2017-BS/fig02-original.png`：SHA-256 `7cf083748c4f1a541b844279c1281d6de8594400166cf9b1950958da6a0dc16f`。
- `wechat/assets/public-safe/ref-li2017-BS/fig03-original.png`：SHA-256 `ec82f62a6ec7f3b06192f7fb4caba9abbc63eba0ea35a05a7bf9b6f3961a553e`。
- `wechat/assets/public-safe/ref-li2017-BS/fig04-original.png`：SHA-256 `ffd04c312d7e8262b3729548454c8a2415f7cfbb246ddf842526b7af279f5002`。
- `wechat/assets/public-safe/ref-li2017-BS/fig05-original.png`：SHA-256 `e34d47c4bec6d29fcc1e587a7b4d05789c29c2f7db73d6c0753ed29313b4ca67`。
- `wechat/assets/public-safe/ref-li2017-BS/fig06-original.png`：SHA-256 `74aaf5698934c436f07da66e1e19aab7a21c9fe4d290e67d816506488da792c4`。
- `wechat/assets/public-safe/ref-li2017-BS/fig07-original.png`：SHA-256 `49a2c9a9ddf6e9f851bbeea476c9c61478400d30c1b6dbe86e084ab0b0b61501`。
- `wechat/assets/public-safe/ref-li2017-BS/fig08-original.png`：SHA-256 `90e22a4be0f4826986a3a58a04dd0144b524cd2aa6c2a3c6724ddd31568fe44b`。
- `wechat/assets/public-safe/ref-li2017-BS/fig09-original.png`：SHA-256 `ebb57df7550653babffe4c6edcc04cc8817ed85935a4695a304d9ccd02dd5c8c`。
- `wechat/assets/public-safe/ref-li2017-BS/fig10-original.png`：SHA-256 `befef55607510ed7dca2630a0fbb871fb99b4834520c2c4ac2a73712b72fb446`。
- `wechat/assets/public-safe/ref-li2017-BS/fig11-original.png`：SHA-256 `bd8592984cce5977c0cf7760b4e849783e64cf8e8d24dc1026c7ad5133ac8a7b`。
- `wechat/assets/public-safe/ref-li2017-BS/fig12-original.png`：SHA-256 `4245f240b924a81fb8078d88f89a78292e04084b2d7dcdae3ce34bf74975c268`。
- `wechat/assets/public-safe/ref-li2017-BS/fig13-original.png`：SHA-256 `186bd3c83ba40963f7a5dd882bcf62e6aaabd4745f9a56915457b07ae687c3d4`。
- `wechat/assets/public-safe/ref-li2017-BS/fig14-original.png`：SHA-256 `f3d99ed3d1d248f8e569bb499a40481d03dfc4fce337d252a5068662f04c4d12`。
- `wechat/assets/public-safe/ref-li2017-BS/fig15-original.png`：SHA-256 `029fe683d2efb3df08d84b3f881cae550405465520b585e415353549da7d7ba1`。
- `wechat/assets/public-safe/ref-li2017-BS/fig16-original.png`：SHA-256 `66841fff9c2444d333f6e8e4dcabf62e80ab17d1d21abfc886888903e414ff0c`。
- `wechat/assets/public-safe/ref-li2017-BS/fig17-original.png`：SHA-256 `fe4009e11d5843db2fa81309b4fd44f37a29dc4c3dac5386f43959ed967932b9`。

## 本轮正文图上传许可

2026-10-14本轮明确要求完成所选27篇双渠道内容并制作公众号草稿，许可范围包含这些论文原图用于对应草稿的必要上传。`body_images_upload_approved: true` 仅记录这一许可，不表示图片已经上传、草稿已经建立、科学审核通过或后台预览通过；正式发表仍不在自动执行范围。实际后台操作由统一交付流程执行。

## 2026-10-14 真实封面集成与非内容等价检查

真实封面 `wechat/assets/public-safe/ref-li2017-BS/cover-wechat-900x383-20261014-v5.png` 的 SHA-256 为 `d959d91b0a2c9961ae7898233e617d283a32e555b54ba5c6f0a95bf23052ffbd`，与根审核冻结清单一致；公开封面简报 `wechat/assets/public-safe/ref-li2017-BS/cover-brief.md` 的 SHA-256 为 `7f8238ed49f41220c09de340e495eaeaedb899ef5d00a2861c55ded7eb49742d`，同样匹配。封面置于“精简版微信公众号文章：待发布”之后、目录之前，双渠道使用同一真实资产。

加封面前 RST SHA-256 为 `6e20ab1709fed32fc2ea40352c45b87f4929814ff95b9626f4f5eee8f3590592`；仅加封面后为 `5bfa3490a82ed2addecd9fa1a576b90bcf7ab104e0e73a0d0e7547f16a636ec0`。删除新增封面指令块可精确恢复加图前字节。随后只为 RST 解析补数学角色后的分隔空格、延长过短标题下划线，未改科学文字、LaTeX、表格、原图或公众号；去空白及标题下划线的逐字符比较一致。当前 RST SHA-256 为 `554b1d239531614bb07c8aed3d1debd330e1e619af0ccd1b1aea4ac2bfed3933`。既有独立科学内容审核保留原范围，不把封面集成说成新全文审核。

本轮文案由明确授权的编辑选择，工程插画与固定文字分层制作；本地独立封面审核通过不等于后台手机预览。

## 2026-10-14 本批官方离线预检与冻结

- 官方 `preflight`、`dry-run` 与 `render-copy-ready.py`（academic-clean / mathjax-svg）均通过。本次未读取凭据、未联系微信、未上传或改后台草稿。
- 公众号 HTML 含 30 个行内公式、0 个独立公式块、4 张正文图。逐个 SVG 静态核对 LaTeX 元数据、viewBox 和路径几何，以及首层 g 的 fill/stroke 属性和内联样式均继承 currentColor，全部通过，未见 MathJax 错误；正文图全部嵌入 HTML。
- RST 诊断 HTML 含 18 张图（包括真实封面）及 7 个显示数学块；4 个 HTML 表格对应原文4表。本篇无 system-message 或 problematic 解析节点，真实封面在目录之前。当前仅留待注册表整合后生成目录的 toctree 接入警告。
- 根已独立审定封面，本文作者另再次打开最终 900 × 383 图核对文案与场景；封面与公开简报 SHA 均和冻结清单匹配。
- 工作区全局公共安全检查仍因其他待制论文缺真实封面而失败，不据本篇通过称全站通过。局部 Sphinx 禁用 sitemap 只作为解析诊断，绝不是标准构建验收；完整标准脚本交指定环境执行。
- 已生成 390 px 浅/深色容器诊断 HTML，供指定浏览器 QA 打开核对。当前环境不能取得真实浏览器渲染截图，本批未重复尝试先前受阻操作；浅深色、公式细节、长表和原图实际显示均待指定环境复验，不将静态 SVG 检查或容器模拟称作手机验收。
- 实际微信后台、手机浅/深色预览与发布未执行。科学审核保留原有范围，不扩称公式渲染或 backend 验收。
