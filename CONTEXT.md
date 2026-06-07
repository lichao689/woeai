# WOEAI Public Website

This context defines the public-facing language for the WOEAI research group website. It keeps publication and proof-page terms precise so public claims stay source-bounded.

## Language

**WOEAI Full Name**:
The canonical expanded English name is `Wind and Ocean Engineering with AI (WOEAI)`. Use it on first mention in public identity surfaces, then use `WOEAI` in short navigation, buttons, and repeated prose. In body copy, `AI-enabled wind and ocean engineering` can describe the research approach when a sentence needs a natural descriptive phrase rather than the brand name.
_Avoid_: ampersand-form expansions, empowered-by-AI phrasing as the canonical name

**Public Journal Paper**:
A journal article that belongs to the group leader's curated public publication record and is suitable for the website's journal-paper list. It is narrower than the broader research library and broader than only first-author or corresponding-author papers.
_Avoid_: reference-library item, collected paper, first-author-only paper

**Proof Page**:
A factual public page whose purpose is to support recruitment, technical collaboration, and academic credibility with verifiable records.
_Avoid_: marketing page, archive dump

**Technical Collaboration**:
The canonical public label for external engineering cooperation and consulting-oriented work. Use `技术合作 Technical Collaboration` for the navigation path and page title.
_Avoid_: 产业合作 Industry Collaboration as the public navigation label

**Academic Outputs**:
The canonical public label for the proof page that contains journal papers and selected highlights. Use `学术成果 Academic Outputs` for the page title while preserving the existing `Publications.rst` filename and URL unless a redirect plan exists.
_Avoid_: 研究成果 Publications as a mixed-language page title

**Publication Metrics**:
Per-paper credibility indicators shown with a Public Journal Paper, including impact factor, journal quartile, Chinese Academy of Sciences division, and citation count. They must come from a confirmed source because they can change over time.
_Avoid_: inferred metrics, stale metrics

**Publication Metric Value**:
The value shown after a Publication Metric label, such as the impact-factor value with journal quartile, Chinese Academy of Sciences division number, or citation count. It is the public evidence value, not the metric label itself.
_Avoid_: metric label, inferred value

**Unavailable Publication Metric**:
A Publication Metric that does not exist for a specific Public Journal Paper or is not supplied by the confirmed source used for the update. It should be omitted rather than fabricated or marked as a public placeholder.
_Avoid_: missing proof, made-up metric

**Publication Number**:
The visible list number assigned to a Public Journal Paper according to the current complete ordering of the publications page. It is not a stable identifier; cross-page references should rely on explicit RST anchors.
_Avoid_: publication id, permanent reference key

**Representative Publication**:
A Public Journal Paper selected for highlights or direction pages because it strongly supports recruitment, technical collaboration, or academic credibility for a research theme. It is a curated subset, not a complete list of outputs.
_Avoid_: every recent paper, exhaustive topic list

**Student First Author**:
The first author of a Public Journal Paper who is listed publicly as the group leader's current or graduated student. This includes both master's and doctoral students when their public names are available.
_Avoid_: coauthor student, undocumented student status, degree-level-only student marker

**Student First Author Marker**:
A visual marker applied only to the Student First Author's displayed name in a Public Journal Paper entry. It marks the person, not the full author list, separator punctuation, or paper title.
_Avoid_: student paper marker, student coauthor marker, first-author separator marker

**Member Status Tag**:
A public People-page label that indicates whether a student member is current or graduated. It supplements the degree-level grouping and must not change the member's public name.
_Avoid_: status in the name, current/graduated as the primary student category

**Research Family**:
The canonical public first-level research taxonomy for WOEAI. Use exactly two public research families: `建筑结构抗风` and `海上漂浮风电`. Method names such as `数值风洞` are subdirections, not first-level public families.
_Avoid_: treating `数值风洞`, `结构抗风`, or `海上风电` as peer first-level directions after this taxonomy change

**建筑结构抗风**:
The first canonical public research family. It covers building and structural wind-resistance research, including `数值风洞与湍流入流` and `高层建筑抗风与优化` as subdirections. Urban wind environment and complex terrain wind fields belong under `数值风洞与湍流入流`. Wind-induced vibration control, flow control, and historical tower-line wind-resistance proof belong under `高层建筑抗风与优化` when they are needed as supporting evidence.
_Avoid_: expanding this into a broad all-structures direction in current public navigation

**海上漂浮风电**:
The second canonical public research family. It covers floating offshore wind research, including `浮式风机系统一体化分析与优化`, `浮式混凝土平台结构设计`, and `数值风浪流水池` as subdirections.
_Avoid_: generic `海上风电` when the public page is specifically about floating offshore wind

**One-Paper WeChat Article**:
A WeChat Official Account article whose core unit is one selected paper. It should explain the paper's problem, method, findings, boundaries, engineering significance, DOI, WOEAI publication anchor, and related direction pages.
_Avoid_: forcing every article into a multi-paper theme essay

**Site Build ID**:
The public date-time identifier for a WOEAI website update. It replaces semantic software versioning for this docs-only public website and should use Beijing time in `YYYY.MM.DD-HHMM` form.
_Avoid_: package version, API compatibility version, ReadTheDocs config version

## Example Dialogue

Dev: Should every Zotero journal article appear on the website?

Domain Expert: No. Only Public Journal Papers should appear; general library references are not group output.

Dev: Should we restrict the list to first-author or corresponding-author work?

Domain Expert: No. First-author or corresponding-author papers can be highlighted separately, but the public journal-paper list should use the broader curated public publication record.

Dev: Can we fill missing impact factors and citation counts from memory?

Domain Expert: No. Publication Metrics need a confirmed source before they are shown on a Proof Page.

Dev: If a paper has no available impact factor, should we still publish the paper?

Domain Expert: Yes. A complete citation can be published without every Publication Metric when the metric is genuinely unavailable.

Dev: Can another page link to publication number 61 as a permanent identifier?

Domain Expert: No. Publication Numbers can change when the page is regenerated; use the paper's RST anchor for stable links.

Dev: Should every new paper appear in the highlights?

Domain Expert: No. Highlights should use Representative Publications; the full list belongs in the journal-paper section.

Dev: Should student authorship marking include only doctoral students?

Domain Expert: No. Student First Author marking applies to both master's and doctoral students when the public People page provides the names.

Dev: Should a private student relationship be marked if the public People page does not name the student?

Domain Expert: No. Student First Author marking should be source-bounded to public People-page names and confirmed aliases.

Dev: Should Publication Metric labels be visually emphasized?

Domain Expert: No. Emphasize Publication Metric Values while keeping labels readable as labels.

Dev: Should the People page split students into current and graduated categories?

Domain Expert: No. Use degree-level groups such as PhD Students and Master Students, then add Member Status Tags for current or graduated status.

Dev: Should WOEAI use semantic versioning for public site updates?

Domain Expert: No. Use a Site Build ID for the public website; Git commits remain the authoritative change history.
