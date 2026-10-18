---
body_images_upload_approved: true
publication_ref: ref-li2012-JWEIA
doi: 10.1016/j.jweia.2011.12.004
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
cover_image: wechat/assets/public-safe/ref-li2012-JWEIA/cover.png
---

# ref-li2012-JWEIA 内容制作记录

## 正文文件

- 公众号正文：`wechat/articles/draft-public-safe/ref-li2012-JWEIA.md`
- 独立全文译文：`docs/source/paper-notes/ref-li2012-JWEIA.rst`
- 原图：`wechat/assets/public-safe/ref-li2012-JWEIA/`，图 1–18。
- 真实封面已加入 RTD 顶部并绑定公众号；本地工程插画与排版审核通过，后台及实际手机预览仍待。

## 源文件获取记录

- 元数据来源：项目出版物注册表、学术成果条目及论文首页交叉核对。
- 附件记录：使用本轮已提供的作者团队论文清单；未连接 Zotero Desktop 或 Web API。
- 本地 PDF：完整可读，共 13 页。
- 已选 PDF 类型：作者团队提供并授权使用的出版社排版原文；当前提供的来源中未另有可优先选用的作者终稿。
- 私有存储类别：私有论文源文件存储与本轮私有制作记录；哈希与清单保持私有。
- Zotero Web API `/file`：无需尝试。
- 网页 PDF 下载：未使用。
- 摘要依据：PDF file page 1 的原摘要。
- 正文证据依据：PDF file pages 1–13 的完整正文与参考文献，不以公众号导读生成全文译文。
- 图片依据：团队作者获准复用的 PDF 原图；先完成 pdfimages 提取，再针对矢量图使用页面局部裁切。

## 关键事实证据定位记录

- 摘要：PDF file page 1。
- 变特征尺度、独立峰值包络线：PDF file page 6，§2.3，式 (30)–(36)。
- 单参数竖向形状函数：PDF file page 3，式 (5)；公众号仅采用此原式。
- 三种雷诺数 6.9×10⁴、3.5×10⁵、6.9×10⁵，入口湍流强度 0.04，光滑地面：PDF file pages 6–7，§3.2。
- 1,089,822 个六面体网格、近壁 y⁺<5、长宽比<50、网格增长因子<1.2、二阶离散和残差条件：PDF file page 7，§3.2；仅在全文页完整保留。
- 径向速度改善的范围 0.75<r/D<3、0.02<z/D<0.2：PDF file pages 8、12，§4.1 及结论第 4 项。
- r/D=1 近地径向速度低估：PDF file page 11，§4.4，图 15。
- 竖向速度局限、变量耦合后无法直接使用原推导：PDF file pages 6、12，§2.3、§4.4 与结论第 3 项。
- 稳态射流和真实下击暴流的衰减差别：PDF file pages 8–9，§4.1。
- 形状函数继续校准的要求：PDF file page 12，结论第 7 项。
- 原图定位：图 1 在 PDF file page 2；图 2 在 page 3；图 3 在 page 4；图 4–5 在 page 5；图 6 在 page 6；图 7 在 page 7；图 8–9 在 page 8；图 10–11 在 page 9；图 12–14 在 page 10；图 15–17 在 page 11；图 18 在 page 12。
- 公式定位：式 (1) 在 PDF file page 2；式 (2)–(5) 及 (3.a)–(3.c)、(4.a)–(4.c) 在 page 3；式 (6)–(17) 在 page 4；式 (18)–(29) 在 page 5；式 (30)–(36) 在 page 6；式 (37)–(41) 在 page 9；式 (42)–(45) 在 page 10。

### 原文内部疑点

- 独立科学复核后修订：PDF file page 5，式 (28) 第二项分母为 R²（无 c 下标），已还原原式并补译注，不擅自统一为 R_c²。
- PDF file page 5，式 (29) 第二项分母为 2R_c²，与 page 4 式 (9)、page 4 式 (17) 的一般指数推导有代数一致性疑点；全文保留原式并加明确译注，不擅自修正。
- PDF file page 6 指向不存在的 §4.2.2，实际相关段落为 page 10 的 §4.3；全文说明原文指向与实际章节。
- PDF file page 8 以同一句话描述图 8、9 的归一化坐标，但两图轴向定义不同；全文保留原叙述并提醒以各图轴标为准。
- PDF file page 9 关于 δ 与雷诺数的末句引用图 12，相关 δ 曲线实为同页图 11；全文明确指出。
- PDF file page 10 式 (42) 使用 r_mm 及 0.0078D，原文也提示极近地面时会给出负值；均保留，未用常识替换符号或抹去负值限制。
- PDF file page 3 式 (3.a) 的区间按原始端点顺序转写；page 9 式 (38) 原排印函数名 LamberW 与前文 LambertW 写法不同，保留原式写法。
- 学术成果条目未给 Q.S. Li 添加通讯标记；PDF file page 1 明确标注其为通讯作者，本文依据原文标记并记录这一元数据差异。

## 工程叙事证据卡

- 论证线：固定特征尺度不能充分表示边界层非线性增长，改用位置相关尺度和独立峰值包络线，以三维 RSM 冲击射流及既有实测/风洞资料检验；改善主要针对限定区域的径向稳态平均速度，竖向速度和近地面仍有偏差。
- 已验证：轴对称稳态平均流场与光滑地面冲击射流，不是完整移动雷暴、建筑荷载或粗糙城市地表验证。
- 潜在用途：校准尺度、强度和形状参数后生成速度剖面；生成移动多点时程是原文提出的用途，不能误称本文已完成瞬态工程验证。
- 迁移前要求：更多实测及风洞校准，检查近地面低估、地表条件和竖向速度。

## 写作审校记录

- 导语直入近地风速剖面问题，首段可独立作为微信摘要。
- 摘要忠实翻译，后设“研究问题与解决思路”，再以四节分别展开尺度机制、形状函数与数值验证、结果偏差、适用边界。
- 已自查空泛拔高、重复导语、缩写堆叠和固定招生结尾；未新增工程案例、性能百分比或部署承诺。
- 数字均与工况就近对应；不以局部改进推广为任意真实下击暴流预测。
- 此为作者侧自查，不替代独立逐句复核和实际手机预览。

## 图片使用记录

- 图 6、7：pdfimages 原生 JPEG，未重采样。
- 图 1：图形包含矢量线条和文字，嵌入位图仅为局部纹理，故使用完整图范围的页面裁切。
- 图 2–5、8–18：原始矢量曲线及文字，使用局部页面渲染裁切，保留坐标轴、图例和分图，未重绘。
- 18 张最终素材均在本地与原 PDF 图范围对照，检查了分图、轴标、图例完整及未夹带相邻正文。此检查不等于实际手机后台验收。
- 公众号选图：1、8、15、18；其余原图在全文译文中使用。

## 公式与链接

- 公众号使用原式 (5)，采用 Markdown LaTeX；浅色/深色手机预览均未进行。
- 全文页保留编号式 (1)–(45) 与六个分式编号，共 51 个编号公式；原文未编号条件和文中公式也保留。
- 完整参考文献 42 条；无编号表格，科学符号表完整转写为可编辑表格；无附录。
- 未设置延伸阅读：无本篇可用的已发布关联公众号链接。
- 阅读原文目标为本篇 RTD 全文精解页，待集成与部署核验。

## 检查记录

- 已完成：源文通读、全文译稿、原图提取、本地原图范围检查、公众号独立写作与作者侧事实自查。
- 独立科学审核与本地真实封面审核已完成；未完成标准全站构建、实际浏览器排版验收、微信后台和真实手机浅色/深色预览。
- 未执行：凭据访问、远程 API、上传、创建草稿、发布、提交或推送。

## 2026-10-14 方向字段格式修正

方向行改为注册表要求的半角冒号及精确一级/二级值；关联基础研究边界如有则移到独立段落，不改变其含义。未改论文作者、摘要、科学正文或原图。既有科学审查的内容范围不扩张；当前公众号文件 SHA-256 为 `ef5c935b7f2d9d8fc5e9a4c2b322aebe51fb6831f3ba51ccad70045f5a75c2c5`。

- 独立科学复核后修订：公众号模型段标题改为“一个参数，也要满足峰值条件”，明确三种竖向模型实质均为单参数，避免把新表达式误称为减少独立自由参数。

## 2026-10-14 独立科学内容审核通过

独立复核覆盖13页原文、全部51个编号公式、18幅原图、42参考文献和公众号。式28的R²转写、导读单参数误导标题已修复后复验。 科学内容审核通过不等于原模型独立重算，也不代表封面、HTML/公式排版、全站构建、部署、后台和手机浅/深色验收。以下哈希锁定本次内容与图像范围，后续变化须按范围重审。

- `docs/source/paper-notes/ref-li2012-JWEIA.rst`：SHA-256 `40e76a272119257deda5a05de6bc3087f28dffeda24f0ef7f8a31a1af3600a7e`。
- `wechat/articles/draft-public-safe/ref-li2012-JWEIA.md`：SHA-256 `eb7b74d3be440a15c42e05d8400361b2c0565f267ec5b51a3afdfd7a63dc45ae`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig01-original.png`：SHA-256 `882d38e0644f39e147ced6aa6c40d3d9a82c31f8ed2f0b9c3a16822334c6eff2`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig02-original.png`：SHA-256 `b929a0ce190c0a9b11a9eb2c3c6a8bd84b8f9b9ba01a91554b4a86b84f0f5bf5`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig03-original.png`：SHA-256 `349980bf95d67ec408d3ac8dac6770bd7d831a747060857eb9b2a9d2ee70b870`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig04-original.png`：SHA-256 `57ad9ec17e4b4c5ddde13cd7e10f50d3acacf3551fd5072604e7cfc617b4e3af`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig05-original.png`：SHA-256 `a44571a6abadeefc04d9d446ea5e682f722973cd08627fdd13288cb515faec02`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig06-original.jpg`：SHA-256 `caba76335c9420d799b1ffa6a26e45359ef0838fa4016e2861b836777e320204`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig07-original.jpg`：SHA-256 `69c337d1ab3114d595b35c1df47e1beb91ee0d579b8688ddac765ab0ea34cbc7`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig08-original.png`：SHA-256 `a8c94d6e266fb5bfc9c54248aa43ecdcafe8ed27da4abb76e133cf6fb8e013bd`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig09-original.png`：SHA-256 `32170e17443ed3377b06121753d9274f56496c8245fcdbee2c5697183c056a10`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig10-original.png`：SHA-256 `1529ac399def63e8ab7c9777a96350153e44b80bd5b6c184d0442fcd61a3adb0`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig11-original.png`：SHA-256 `c2985d7a4448c7aafb344e1bc88493154fb1cd164516f121635b3f185eebbfe0`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig12-original.png`：SHA-256 `b10acd4afb38e3caff14705ba7349f5fb042e277525e9bdfc4448205c178b70c`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig13-original.png`：SHA-256 `314607b456000272d94cbba0134ae7e7bab7666bed91e1d12caae5f0b31d9d04`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig14-original.png`：SHA-256 `23aa121e67ff015620f3daddcdf8689e04e44ed4bfd5bcbd465e9796bd8b83b3`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig15-original.png`：SHA-256 `0f422387c5c33a8fc52ea3460b6d47de996e6936ca16e545864d7c54fc37cab3`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig16-original.png`：SHA-256 `ca90d3b61df8e5daf84a91afc6a8eca8b68cfffca14c1187f150a0856c814dd8`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig17-original.png`：SHA-256 `c19cbe7b8965bfb433fdb885b4681c1ee0c841edaf4a9aa4eddf8fda004e46dc`。
- `wechat/assets/public-safe/ref-li2012-JWEIA/fig18-original.png`：SHA-256 `733e56508c2b25a74ff7c0d4fa4c013a36356ff475c1147b478d9bdf3c777f4f`。

## 本轮正文图上传许可

2026-10-14本轮明确要求完成所选27篇双渠道内容并制作公众号草稿，许可范围包含这些论文原图用于对应草稿的必要上传。`body_images_upload_approved: true` 仅记录这一许可，不表示图片已经上传、草稿已经建立、科学审核通过或后台预览通过；正式发表仍不在自动执行范围。实际后台操作由统一交付流程执行。

## 2026-10-14 真实封面集成与非内容等价检查

真实封面 `wechat/assets/public-safe/ref-li2012-JWEIA/cover-wechat-900x383-20261014-v5.png` 的 SHA-256 为 `cd43df957edca242836f34c9af70247100896c5296d8a6f1e2266eeb24c688e3`，与根审核冻结清单一致；公开封面简报 `wechat/assets/public-safe/ref-li2012-JWEIA/cover-brief.md` 的 SHA-256 为 `7aac9c0ba46017d9e58bd8523b060dee3722d5ab2ff44fbcfd88c32890f1c026`，同样匹配。封面置于“精简版微信公众号文章：待发布”之后、目录之前，双渠道使用同一真实资产。

加封面前 RST SHA-256 为 `40e76a272119257deda5a05de6bc3087f28dffeda24f0ef7f8a31a1af3600a7e`；仅加封面后为 `898c8fee5b7ccf131b8b58ddf80e9dc46f62c1927e429cdc386c6b2a73fd6ef2`。删除新增封面指令块可精确恢复加图前字节。随后只为 RST 解析补数学角色后的分隔空格、延长过短标题下划线，未改科学文字、LaTeX、表格、原图或公众号；去空白及标题下划线的逐字符比较一致。当前 RST SHA-256 为 `21bc8ac8fbf6406bcca2c1a53882fde6f6bacbca5f1e4d9100901a506afe373b`。既有独立科学内容审核保留原范围，不把封面集成说成新全文审核。

本轮文案由明确授权的编辑选择，工程插画与固定文字分层制作；本地独立封面审核通过不等于后台手机预览。

封面副标题采用根审核确定的“用变尺度修正风速模型”，限定修正对象为模型；未据封面文案改写已审科学正文。

## 2026-10-14 本批官方离线预检与冻结

- 官方 `preflight`、`dry-run` 与 `render-copy-ready.py`（academic-clean / mathjax-svg）均通过。本次未读取凭据、未联系微信、未上传或改后台草稿。
- 公众号 HTML 含 12 个行内公式、1 个独立公式块、4 张正文图。逐个 SVG 静态核对 LaTeX 元数据、viewBox 和路径几何，以及首层 g 的 fill/stroke 属性和内联样式均继承 currentColor，全部通过，未见 MathJax 错误；正文图全部嵌入 HTML。
- RST 诊断 HTML 含 19 张图（包括真实封面）及 52 个显示数学块；1 个 HTML 表格为原文符号表；52 个显示数学块含51个编号表达式及另一个未编号关系式。本篇无 system-message 或 problematic 解析节点，真实封面在目录之前。当前仅留待注册表整合后生成目录的 toctree 接入警告。
- 根已独立审定封面，本文作者另再次打开最终 900 × 383 图核对文案与场景；封面与公开简报 SHA 均和冻结清单匹配。
- 工作区全局公共安全检查仍因其他待制论文缺真实封面而失败，不据本篇通过称全站通过。局部 Sphinx 禁用 sitemap 只作为解析诊断，绝不是标准构建验收；完整标准脚本交指定环境执行。
- 已生成 390 px 浅/深色容器诊断 HTML，供指定浏览器 QA 打开核对。当前环境不能取得真实浏览器渲染截图，本批未重复尝试先前受阻操作；浅深色、公式细节、长表和原图实际显示均待指定环境复验，不将静态 SVG 检查或容器模拟称作手机验收。
- 实际微信后台、手机浅/深色预览与发布未执行。科学审核保留原有范围，不扩称公式渲染或 backend 验收。
