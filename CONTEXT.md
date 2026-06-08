# WOEAI Public Website

This context defines the public-facing language for the WOEAI research group website. It keeps publication and proof-page terms precise so public claims stay source-bounded.

## Language

**WOEAI Full Name**:
The canonical expanded English name is `Wind and Ocean Engineering with AI (WOEAI)`. Use it on first mention in public identity surfaces, then use `WOEAI` in short navigation, buttons, and repeated prose. In body copy, `AI-enabled wind and ocean engineering` can describe the research approach when a sentence needs a natural descriptive phrase rather than the brand name.
_Avoid_: ampersand-form expansions, empowered-by-AI phrasing as the canonical name

**Public Journal Paper**:
A journal article that belongs to the group leader's curated public research publication record and is suitable for the website's journal-paper list. It is narrower than the broader research library and broader than only first-author or corresponding-author papers. Teaching-reform and ideological-and-political-course-construction papers are not Public Journal Papers; place them under the Teaching Reform Publication section instead.
_Avoid_: reference-library item, collected paper, first-author-only paper, teaching-reform paper, course ideological-and-political construction paper

**Proof Page**:
A factual public page whose purpose is to support recruitment, engineering applications, and academic credibility with verifiable records.
_Avoid_: marketing page, archive dump

**Teaching Reform Publication**:
A teaching-reform, course-construction, or ideological-and-political-course-construction paper that belongs on `docs/source/Teaching.rst` under `教改探索 Teaching Reform Exploration`. It should not be counted, numbered, mapped, or displayed as a Public Journal Paper in Academic Outputs or the Thematic Publication View.
_Avoid_: research-family mapping, Academic Outputs listing, publication-number assignment

**Official Profile Link**:
The canonical way to reference the group leader's official external profile. Link to `https://homepage.hit.edu.cn/lichao` instead of reproducing local institution, college, address, title, or employment-history claims on the public site.
_Avoid_: local institution identity copy, college-address claims, school-official wording on the personal/group website

**Public Contact Channels**:
The public contact channels for WOEAI are the website URL, the personal email address `lichaosz@qq.com`, the Official Profile Link, and the WeChat QR code already used on the homepage. These channels may be published, but they should not be expanded into additional personal contact details without explicit confirmation.
_Avoid_: workplace address as contact, alternate private contact, unconfirmed phone or messaging IDs

**Privacy Notice**:
The public page that explains the website's personal-information handling boundary. It should say that the website itself does not provide forms, accounts, comments, analytics, or tracking scripts; platform logs are handled by GitHub or Read the Docs under their own policies; information sent through Public Contact Channels is used only for replies, application or academic communication, engineering-application or technical-collaboration communication, and academic exchange. If a page embeds a third-party video player, the Privacy Notice should disclose that the visitor's browser may request resources from that third-party platform.
_Avoid_: legal guarantee, platform-log control claim, consent-heavy wording for functions the site does not run

**Site Statement**:
The concise homepage statement for site purpose, non-official status, and content-use boundary. It should say the site is for academic output display and engineering-application exchange, and that it does not represent any organization or institution's official position.
_Avoid_: recruitment purpose in the statement, local institution name, legal guarantee, broad public-relations language

**Engineering Applications**:
The canonical public label for the second conversion path for external engineering cooperation and consulting-oriented work. Use `工程应用 Engineering Applications` for the navigation path and page title, with `docs/source/EngineeringApplications.rst` as the canonical page URL. The page should present public application scenarios by Research Family and second-level research subdirection before pointing to public project evidence. Technical collaboration remains a contact action, not the primary page title.
_Avoid_: 产业合作 Industry Collaboration as the public navigation label, sales-style cooperation page, partner-name display without source confirmation

**Embedded Video**:
A public video player embedded from a third-party platform such as Bilibili or YouTube. Use it only for self-owned, authorized, or clearly test-labeled public videos. Test embeds must not be described as WOEAI evidence or成果, and final public embeds should identify the source and provide an external link fallback.
_Avoid_: unmarked third-party video, implying team ownership of external demonstrations, embedding sensitive or unpublished project footage

**Enterprise Project Evidence**:
Public evidence for enterprise-commissioned work. It may show approved capability direction, problem type, year, and role, but should not disclose partner names, current cooperation status, or unpublished project details. Already anonymized descriptions such as `某再生能源发电厂` do not need further generalization unless they become identifiable.
_Avoid_: partner name, exact facility name, active project detail, over-generalizing already anonymized evidence

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

**Homepage Latest Academic Progress**:
The homepage research section should surface the latest academic progress so recurring paper-article updates remain visible. Show up to 10 newest paper notes or RTD companion articles under `最新学术进展 Latest Academic Progress`, while keeping the complete archive and longer research narrative on `docs/source/Research.rst`.
_Avoid_: hiding new paper notes only in deep pages, duplicating the full Research archive on the homepage, listing more than 10 homepage progress items

**Chronological Publication View**:
The canonical complete Academic Outputs view in `docs/source/Publications.rst`. It lists Public Journal Papers by publication year in descending order and owns the full citation text, DOI, Publication Metrics, Student First Author Marker, anchors, and current Publication Numbers.
_Avoid_: treating the direction view as the full bibliography, maintaining duplicate long citations

**Thematic Publication View**:
The alternate Academic Outputs browsing view in `docs/source/PublicationsByResearch.rst`. It groups the same Public Journal Papers by Research Family first and subdirection second. Inside each subdirection, paper entries are listed by publication year in descending order. Each paper entry must use the exact same public citation expression as the Chronological Publication View, including authors, title, venue, DOI, Publication Metrics, Student First Author Marker, and current Publication Number. It should be registered under the Chronological Publication View's toctree so it appears as part of Academic Outputs in the left navigation, not as a separate root-level site directory.
_Avoid_: JavaScript-only tabs, alternate short-index citation style, duplicate hand-maintained citation text, publication-year section headings inside subdirections, root-level navigation entry for the thematic view

**Publication Research Mapping**:
The machine-readable mapping from Zotero item keys to Research Family and subdirection, stored at `docs/data/publication-research-map.json`. Every Public Journal Paper must have exactly one canonical Research Family and one canonical subdirection before the thematic view can be generated.
_Avoid_: Publication Number as mapping key, selected WeChat paper list as full mapping source, unmapped public papers

**Student First Author**:
The first author of a Public Journal Paper who is listed publicly as the group leader's current or graduated student. This includes both master's and doctoral students when their public names are available.
_Avoid_: coauthor student, undocumented student status, degree-level-only student marker

**Student First Author Marker**:
A visual marker applied only to the Student First Author's displayed name in a Public Journal Paper entry. It marks the person, not the full author list, separator punctuation, or paper title.
_Avoid_: student paper marker, student coauthor marker, first-author separator marker

**Member Status Tag**:
A public People-page label that indicates whether a student member is current or graduated. It supplements the degree-level grouping and must not change the member's public name.
_Avoid_: status in the name, current/graduated as the primary student category

**Academic Member Listing**:
A public member listing that supports academic context only. It may show a student's public name, degree-level group, Member Status Tag, and degree thesis information when the thesis record is public, but should not add institution, college, address, personal contact, private biography, photo, student ID, demographic detail, or non-academic personal information.
_Avoid_: unit-bearing student profile, contact directory, private student record

**Degree Thesis Listing**:
A People-page line that presents a member through public graduation thesis metadata in the format `姓名(English Name)，年份日期，学位论文类型：题目。`. It is ordinary listing text, not a subsection heading or a private biography. Degree Thesis Listings are sorted by graduation date in ascending order within each degree-level group.
_Avoid_: thesis as member profile heading, unpublished private thesis note, non-public student record

**Research Family**:
The canonical public first-level research taxonomy for WOEAI. Use exactly two public research families: `建筑结构抗风` and `海上漂浮风电`. Method names such as `数值风洞` are subdirections, not first-level public families.
_Avoid_: treating `数值风洞`, `结构抗风`, or `海上风电` as peer first-level directions after this taxonomy change

**建筑结构抗风**:
The first canonical public research family. It covers building and structural wind-resistance research, including `数值风洞与湍动入流` and `高层建筑抗风与优化` as subdirections. Urban wind environment and complex terrain wind fields belong under `数值风洞与湍动入流`. Wind-induced vibration control, flow control, and historical tower-line wind-resistance proof belong under `高层建筑抗风与优化` when they are needed as supporting evidence.
_Avoid_: expanding this into a broad all-structures direction in current public navigation

**海上漂浮风电**:
The second canonical public research family. It covers floating offshore wind research, including `浮式风机系统一体化分析与优化`, `浮式混凝土平台结构设计`, and `数值风浪流水池` as subdirections.
_Avoid_: generic `海上风电` when the public page is specifically about floating offshore wind

**One-Paper WeChat Article**:
A WeChat Official Account article whose core unit is one selected paper. It should explain the paper's problem, method, findings, boundaries, engineering significance, DOI, WOEAI publication anchor, and related direction pages.
_Avoid_: forcing every article into a multi-paper theme essay

**RTD Paper Companion Page**:
A Read the Docs page generated from a One-Paper WeChat Article. It should preserve the same title, body text, images, DOI link, WOEAI publication anchor, and contact/link intent as the WeChat article, while converting the markup and rendering format to Sphinx-compatible reStructuredText.
_Avoid_: creating a separate Markdown route for Sphinx, changing the article meaning for RTD, or making the RTD page a shorter unrelated summary

**Public Formula**:
A mathematical expression included in a One-Paper WeChat Article or RTD Paper Companion Page. It should preserve one LaTeX formula meaning across publication channels, with channel-specific rendering. Public formulas should remain text-based and explain their key variables in prose.
_Avoid_: code-block formula, unstructured plain-text formula, default formula screenshot, unexplained symbol list

**Academic Progress Section**:
The research-direction page section that groups RTD Paper Companion Pages by second-level research subdirection. It replaces `近期证据` as the public label for recent paper-explanation progress and should initially sort entries by publication date in descending order.
_Avoid_: treating Academic Progress as a raw publication list, a duplicate chronological publication view, or a collection grouped only by first-level Research Family

**Site Build ID**:
The public date-time identifier for a WOEAI website update. It replaces semantic software versioning for this docs-only public website and should use Beijing time in `YYYY.MM.DD-HHMM` form.
_Avoid_: package version, API compatibility version, ReadTheDocs config version

## Example Dialogue

Dev: Should every Zotero journal article appear on the website?

Domain Expert: No. Only Public Journal Papers should appear; general library references are not group output.

Dev: Should the site describe the group leader's current institution and college locally?

Domain Expert: No. Use the Official Profile Link for official external profile information and keep this site focused on WOEAI research, recruitment, collaboration, and academic outputs.

Dev: Should the homepage keep the WeChat QR code?

Domain Expert: Yes. Keep it as a Public Contact Channel alongside `lichaosz@qq.com`, but do not add further personal contact details unless explicitly confirmed.

Dev: Should the site include a privacy policy?

Domain Expert: Yes. Add a concise Privacy Notice that covers static-site boundaries, platform logs, email and WeChat messages, no tracking scripts, and requests through the public email address.

Dev: What purpose should the homepage statement give for the website?

Domain Expert: Say it is used for academic output display and engineering-application exchange. Do not include recruitment in the statement.

Dev: Should enterprise project entries be generalized further?

Domain Expert: Keep already anonymized Enterprise Project Evidence as-is. Do not disclose partner names or unpublished project details, but do not further generalize entries such as `某再生能源发电厂`.

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

Dev: Should the Academic Outputs page maintain two complete citation lists?

Domain Expert: No. Keep the Chronological Publication View as the full bibliography and use the Thematic Publication View as a short index that links back to stable publication anchors.

Dev: Can the thematic publication page use subdirections as first-level headings?

Domain Expert: No. The first level must be Research Family: `建筑结构抗风` and `海上漂浮风电`. Subdirections are second-level headings inside those sections, and papers under each subdirection are listed directly in descending publication-year order.

Dev: Should student authorship marking include only doctoral students?

Domain Expert: No. Student First Author marking applies to both master's and doctoral students when the public People page provides the names.

Dev: Should a private student relationship be marked if the public People page does not name the student?

Domain Expert: No. Student First Author marking should be source-bounded to public People-page names and confirmed aliases.

Dev: Should Publication Metric labels be visually emphasized?

Domain Expert: No. Emphasize Publication Metric Values while keeping labels readable as labels.

Dev: Should the People page split students into current and graduated categories?

Domain Expert: No. Use degree-level groups such as PhD Students and Master Students, then add Member Status Tags for current or graduated status.

Dev: Should student names and current/graduated status be removed for privacy?

Domain Expert: No. Keep Academic Member Listings when they support academic context, but do not add units, contact details, photos, IDs, or private biographical information.

Dev: Should graduated students on the People page be shown as one subsection per person?

Domain Expert: No. Use Degree Thesis Listings as ordinary text lines under the relevant degree-level group.

Dev: Should WOEAI use semantic versioning for public site updates?

Domain Expert: No. Use a Site Build ID for the public website; Git commits remain the authoritative change history.
