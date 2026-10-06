---
publication_ref: ref-yang2025-JBE
doi: 10.1016/j.jobe.2025.113635
wechat_status: awaiting_review
wechat_author: Yang Junhui
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
rtd_full_paper_self_check: passed
rtd_independent_review: awaiting_review
wechat_cover_image: wechat/assets/public-safe/ref-yang2025-JBE/cover-wechat-900x383-imagegen-v5b-pub-line-route.png
rtd_cover_image: wechat/assets/public-safe/ref-yang2025-JBE/cover-wechat-900x383-imagegen-v5b-pub-line-route.png
---

# ref-yang2025-JBE 原文核验记录

## 当前核验结果

- 2026-10-06：RTD 已由选读简介改为直接根据授权出版版制作的逐段中文全文精解；作者自检通过，独立审校尚未完成。`rtd_page_checked: false` 保留最终验收门槛，不表示本次离线检查未做
- 本次覆盖：24 页源文、全部科学正文及说明文字、46 个编号公式、21 幅科学图、4 张中文可编辑表、50 条参考文献及原文参考文献外链；原文无附录、无独立符号表
- 已保留 a–d 作者单位对应关系、通讯作者脚注、出版日期和 DOI；顶部精简版微信公众号链接行之后立即是原封面
- 公众号正文及所有封面保持原样；6 幅既有公众号科学图别名同步采用本次校准素材。公众号仍未通过本轮后台手机预览，不更新后台或发布状态
- 2026-10-05 的“RTD 全文未完成”是此前版本结论，本次已补齐其缺项；既有事实边界继续保留并扩充源文差异说明

## 正文与公开素材

- RTD：`docs/source/paper-notes/ref-yang2025-JBE.rst`
- 公众号：`wechat/articles/draft-public-safe/ref-yang2025-JBE.md`
- 全文科学图：`wechat/assets/public-safe/ref-yang2025-JBE/fig01.png` 至 `fig21.png`
- 保留的公众号别名：`fig-01-building-principal-axes-wind-direction.jpg`、`fig-03-method-error-random-signals.jpg`、`fig-05-error-correlation-map.jpg`、`fig-17-width-depth-fe-models.jpg`、`fig-18-width-depth-wind-direction-response.jpg`、`fig-20-center-corner-response-ratio.jpg`
- RTD 本次自检正文 SHA-256：`920ad55b899fd98733105af6abdb5106dc66fcd93ac23a9650dca85c52bd30ba`

## 源文件获取记录

- DOI：https://doi.org/10.1016/j.jobe.2025.113635
- 源档案条目标识：YZ2D62NB；题名、作者、期刊、年份与 WOEAI 学术成果对应条目及当前 PDF 一致
- 来源类别：用户授权的期刊出版版 PDF；当前工作区有可读源文件，未发现本任务可用的更高优先级作者终稿，因此使用已授权出版版
- 文件页数：24；文中 `PDF file page N` 均指文件物理页码
- 当前核验副本 SHA-256：`9c68cfe79bddd2b50839d9251df3e18579a0f20edbe6ad8738a1ed252e27f26c`
- 历史原始源档案 SHA-256 与当前副本一致；本次重新计算当前字节哈希，没有把传输记录本身视为字节等同证明
- 元数据来源：当前 PDF 首页和已有成果条目；附件记录沿用授权源清单，本次未连接 Zotero Desktop API，也未调用 Zotero Web API `/file`
- 私有存储类别：授权源文件及校核中间产物；原始 PDF、逐页提取文本、源页截图与诊断 HTML 不进入公开目录
- 本次无网页 PDF 下载、无凭据访问、无图片上传、无外部草稿更新
- 摘要、正文、表格、公式和图题均来自当前 PDF；图像均来自同一源文件，按已有作者身份及素材使用授权处理

## 关键事实证据定位记录

- PDF file page 1：完整摘要、a–d 单位映射、通讯作者脚注、2025-03-13 收稿、2025-07-18 修回、2025-07-29 录用、2025-07-30 在线发表
- PDF file page 2–3，§1：完整文献综述、时域/频域方法边界、非高斯与窄带问题、SRSS/ERF/CDC/RPA/CPF 来源和研究安排
- PDF file page 3–6，§2.1，Eq.(1)–(21)：精细积分法、极值穿越理论、Davenport 和带宽修正峰值因子；零均值平稳高斯过程前提、平均风响应另作静力处理均保留
- PDF file page 6–9，§2.2，Eq.(22)–(41)：角点平动/转动关系、矢量模长与投影分量区别、分量相关性、广义极值统计及五种组合方法的完整推导与假定
- PDF file page 9–10，§3.1、Fig.2–3：Python 3.12、10 Hz、600 s、6000 点、1000 次模拟；ρ=0.2 且标准差比为 1 时误差为 SRSS +25.76%、ERF −7.18%、CDC +0.61%、RPA −2.54%、CPF +4.40%
- PDF file page 10–12，Fig.4–5：完整参数扫描和误差热图；横轴标准差比、纵轴相关系数；未把不显式依赖相关系数的预测公式误写为误差不受相关性影响
- PDF file page 11–13，§3.2.1–3.2.2、Table1、Eq.(42)–(43)：模型、风洞采样、风速与时间换算；位移用 50 年风速、2% 阻尼，加速度用 10 年风速、1.5% 阻尼；初始响应分析考虑前 30 阶
- PDF file page 13–16，§3.2.3、Eq.(44)–(46)、Fig.12–13：0° 风向、以前 20 阶结果为参照；前 3 阶位移 99.8%、前 6/11 阶加速度 96.7%/99.0%；11 阶仅是该算例建议
- PDF file page 15–18，§3.2.4、Table2、Fig.14–16：10 min 分段极值均值、三种一维峰值因子和五种二维极值方法；没有将 CDC 的综合评价泛化为各个单项误差都最小
- PDF file page 17–21，§3.3.1、Table3–4、Fig.17–20：TPU 数据、宽深比模型、基本风压、风向和主轴/合成极值比较；表 4 全风向最大值与逐风向误差分别保留
- PDF file page 19、21，Fig.20：19%（2:1）/28%（3:1）指中心点主轴加速度相对角点二维加速度的低估，不是全部位移指标；分母也不同于表 4 的中心点基准增幅
- PDF file page 19、21，Table4：B31 全风向最大值的角点二维/角点主轴差别为位移 2.20%、加速度 1.58%；B31T 加速度为 5.19%，因此“3% 以内”不适用于任意扭转周期比
- PDF file page 21–23，§3.3.2、§4：保留扭转增大时部分响应下降的负面结果、五项结论及其算例边界；没有声称所有建筑均有统一误差或固定振型数保证

## 源文内部差异与译文处理

- PDF file page 2 称峰值因子乘“方差”，后文公式采用标准差；原词与译注并存
- PDF file page 4，Eq.(7)：原文余项印为 `0(Δt^(2n−1))`，指数积分时间参数与 Eq.(6) 的排式也不完全一致；不静默重写。正文称 1994 年提出 PI，文献 [19] 为 2004 年，日期分别保留
- PDF file page 5–6，Eq.(18)–(19)：`E(k)` 重用、`Pk/pk` 和密度/累积分布符号差别保留；穿越率的原始 υ/v 用字按源文转录
- PDF file page 7，Eq.(22)–(23)：Y 向角加速度项符号与直接求导的一致性疑问明确提示，未擅改符号
- PDF file page 7，Eq.(25)–(27)：概率密度未显式包含相关系数、等标准差时归一化/指数系数问题，以及 GEVD 均值符号与存在条件问题明确披露；公式按出版版保留
- PDF file page 8，Eq.(36)：极值导数与右端平方峰值因子的关系、角度相关性和反正切分支须核验；保留源式，不补做未授权模拟
- PDF file page 9：原文关于 Rayleigh“标准差为 1”及非负模长“穿越零界限”的措辞加注核验范围；Fig.2 负峰值标记与正文绝对值口径并列保留
- PDF file page 10–12：模拟端点 0.01/0.99 与轴刻度 0.0/1.0 并存；SRSS 正文最大约 42%，Fig.5 最大格值 0.41。Fig.5 的 SRSS 格值与 Fig.4 同坐标数值直接计算亦不一致，举出左下角 3.92/3.95 对照 0.41，不声称重新复算作者全部试验
- PDF file page 11–12，Table1/Eq.(43)：几何比代入方向与 268/354 min 持续时间对应关系须核验，源表数字不替换
- PDF file page 14，Eq.(45)：分母无平方，与无量纲权重表述有量纲疑问；保留源式
- PDF file page 15–17，Table2：X 向位移最小误差为 Vanmarcke 3.99%，不是 C&L 5.86%；作者的总体判断不被扩写成所有单项成立
- PDF file page 16、18，Fig.16：CPF 位移曲线与“偏于不安全”的总体文字存在张力；ERF 位移 3.2%、RPA 加速度 3.4% 分别小于 CDC 4.5%/3.5%，保留分项结果。原图子题称峰值因子、纵轴却有位移/加速度单位，图内文字译注说明
- PDF file page 19：B31 “所有比值超过 0.98”与最大位移低估 3.1% 不一致；该页两处加速度工况均标 3:1，Fig.20 第一组实际对应 B11；不静默消除差异
- PDF file page 21，Table4：显示精度下的百分数未必可直接重算，保留全部数字；B21T 位移下降而加速度上升，B31T 主轴加速度也下降
- PDF file page 18、21–22：Table3 的 B21T `TZ/TY≈0.877` 与“大于 0.9”的文字和 Fig.21 图题不一致；B31T 约为 0.907。保留周期表与图题并明确说明
- PDF file page 23，结论(5)：第二阶振型中扭转占比“超过 50%”未给独立计算定义，不与周期比阈值混同

## 全文覆盖与裁图校准

- 已翻译：论文信息、关键词、摘要；§1；§2；§2.1.1–2.1.4；§2.2.1–2.2.5；§3.1；§3.2.1–3.2.4.2；§3.3.1–3.3.2；§4 五项结论；全部图题、必要图内文字、表注、公式解释及参考文献
- 自检逐段证据覆盖 106 个科学段落/表注定位单元，均能在原文和译文中找到；不是以图数或总字数替代逐段核对
- Eq.(1)–(46) 全部为可编辑数学公式；另外保留 3 个原文无编号数学块；未使用公式截图或 `\tag`
- Fig.1–21 全部保留；Table1–4 全部为中文可编辑 `list-table`，Table4 含全部 10 行数据与原始百分数
- 参考文献 [1]–[50] 完整保留；正文引文可跳转到本页对应条目；50 个原始参考文献外链逐一按 PDF 链接注释定位，保留 RefHub 标识与条目编号不相同的原始链接，没有猜测 DOI
- 无附录、无独立科学符号表。结论之后进入参考文献，再以“完整引用”链接回成果条目；按项目规则不纳入出版声明性尾注
- 10 幅原生栅格图：Fig.1–5、8、10、12、13、17；在完整源页核对，确认没有额外叠加的文字或矢量对象被漏掉
- 11 幅矢量/混合页图：Fig.6、7、9、11、14–16、18–21；以包含矢量文字和全部绘图对象的页面裁框输出，逐张核对完整源页和最终图，不包含相邻正文或英文图题
- 图源页定位：Fig.1→PDF file page 6；Fig.2→9；Fig.3→10；Fig.4→11；Fig.5→12；Fig.6–7→13；Fig.8–10→14；Fig.11–12→15；Fig.13–14→16；Fig.15→17；Fig.16–17→18；Fig.18–19→20；Fig.20→21；Fig.21→22
- 特别检查：Fig.5 的五面板、两轴方向及完整色标；Fig.7 的 story N−1 和底部 X/Y 坐标；Fig.18 的六面板、B31 底部子题、各 0°/30°/60°/90° 刻度；全部保留
- 6 个公众号 JPG 别名由同一通过目视检查的完整科学图生成，保持真实 JPEG 编码；既有封面不裁切、不替换

## 本轮离线验证

- 通过：`python3 tools/publications/artifacts.py --check`；本篇无缺失产物，结果不代表后台预览或全站发布完成
- 通过：`python3 scripts/check-public-safe-content.py` 与本篇作用域的 `git diff --check`
- 通过：新建诊断 Sphinx HTML，`-W --keep-going -E`；诊断配置仅加载 duration/mathjax，不将其冒充含 sitemap 的标准全门禁
- 通过：实际生成 HTML 含 21 个 figure、4 个 table、50 个文献锚点、46 个公式锚点，所有目标图片、内部片段和原文参考文献外链有效，无裸露 `:math:`/`:ref:`/作者角色语法
- 通过：实际 HTML 的 381 个数学节点逐一经 MathJax SVG 渲染，49 个显示块（含 46 编号式）、332 个行内式，无 merror/data-mjx-error
- 标准门禁未通过：已实际执行 `./scripts/check-docs.sh`；临时空间问题解除后重试成功安装依赖并通过安全扫描，随后停在共享登记表的 missing/stale 验证和生成视图不同步；本任务未修改共享登记表，也未声称标准门禁通过
- 未运行：原文数值模型/风洞试验复算；浏览器或微信后台手机预览；外部上传、提交、推送及部署
- 最终独立源文审校与全站登记、标准门禁、部署验证由后续批次验收处理


## 2026-10-06 独立全文与逐图复核通过

- 全部 24 页正文、作者单位与通讯脚注、21 幅完整图、4 张可编辑表、46 个编号公式与 3 个无编号展示公式、50 条参考文献及其原始链接通过独立复核。
- 逐图对照完整原页，全部坐标、图例、分图及关键文字完整；相关性坐标、模态截断和中心/角点的适用范围均忠实保留。
- 修正式（20）平方根命令缺失的反斜杠，其余公式、正文与图像保持原译稿。最终诊断 Sphinx、HTML 66 处引文/309 个链接及 381 项 MathJax 检查通过。
- 本结论取代上文待独立审核状态，标准发布门禁由最终集成批次验证；公众号后台状态不变。
