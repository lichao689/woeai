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
The canonical complete Academic Outputs view in `docs/source/Publications.rst`. It lists Public Journal Papers by publication year in descending order, groups Public Journal Papers before 2019 under `更早 Earlier`, and owns the full citation text, DOI, Publication Metrics, Student First Author Marker, anchors, and current Publication Numbers. It also contains Degree Thesis Listings after the Journal Papers section.
_Avoid_: treating the direction view as the full bibliography, maintaining duplicate long citations

**Thematic Publication View**:
The alternate Academic Outputs browsing view in `docs/source/PublicationsByResearch.rst`. It groups the same Public Journal Papers by Research Family first and subdirection second. Inside each subdirection, paper entries are listed by publication year in descending order. Each paper entry must use the exact same public citation expression as the Chronological Publication View, including authors, title, venue, DOI, Publication Metrics, Student First Author Marker, and current Publication Number. It should be registered under the Chronological Publication View's toctree so it appears as part of Academic Outputs in the left navigation, not as a separate root-level site directory.
_Avoid_: JavaScript-only tabs, alternate short-index citation style, duplicate hand-maintained citation text, publication-year section headings inside subdirections, root-level navigation entry for the thematic view

**Publication Research Mapping**:
The machine-readable mapping from Zotero item keys to Research Family and subdirection, stored at `docs/data/publication-research-map.json`. Every Public Journal Paper must have exactly one canonical Research Family and one canonical subdirection before the thematic view can be generated.
_Avoid_: Publication Number as mapping key, selected WeChat paper list as full mapping source, unmapped public papers

**Student First Author**:
The first author of a Public Journal Paper who is listed publicly as the group leader's current or graduated student. This includes both master's and doctoral students when their names are present in Degree Thesis Data or confirmed public student-author aliases.
_Avoid_: coauthor student, undocumented student status, degree-level-only student marker

**Student First Author Marker**:
A visual marker applied only to the Student First Author's displayed name in a Public Journal Paper entry. It marks the person, not the full author list, separator punctuation, or paper title.
_Avoid_: student paper marker, student coauthor marker, first-author separator marker

**Degree Thesis Data**:
The machine-readable source for public student thesis metadata and student-first-author aliases, stored at `docs/data/degree-theses.json`. It replaces People-page parsing for publication generation and should include only public academic metadata needed by Academic Outputs.
_Avoid_: private student record, contact directory, personal biography, unit-bearing student profile

**Degree Thesis Listing**:
An Academic Outputs line that presents public graduation thesis metadata in the format `姓名(English Name)，年份日期，学位论文类型：题目。`. It is ordinary listing text under `学位论文 Degree Theses`, grouped into doctoral and master's theses after the Journal Papers section. Degree Thesis Listings are sorted by graduation date in ascending order within each degree-level group.
_Avoid_: thesis as member profile heading, People-page dependency, unpublished private thesis note, non-public student record

**Early Publication Group**:
The Chronological Publication View section titled `更早 Earlier`, grouping Public Journal Papers before 2019 instead of keeping many sparse historical year headings.
_Avoid_: standalone pre-2019 year sections, `Early` without the Chinese label

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
A WeChat Official Account article whose core unit is one selected paper. It should explain the paper's problem, method, findings, boundaries, engineering significance, DOI, and selected related direction links. It should avoid repeating a WOEAI publication-page anchor when that linked page does not add reader value beyond the article itself.
_Avoid_: forcing every article into a multi-paper theme essay

**WeChat Article Source**:
The canonical public-safe Markdown source for a One-Paper WeChat Article before publication. WeChat HTML, rendered previews, API payloads, draft-box records, and RTD Paper Companion Pages are derived outputs and should not become the source of truth for article wording or facts.
_Avoid_: treating rendered HTML, WeChat draft content, doocs/md previews, API payloads, or RTD pages as the canonical article source

**WeChat Paper Author Line**:
The author list shown in the `论文信息` section of a One-Paper WeChat Article. It uses the same author-marker semantics as the Chronological Publication View: the Student First Author Marker applies only to Student First Authors, and an author-name `*` marks a corresponding author.
_Avoid_: marking every first author as a Student First Author, spelling out `corresponding author` in the reader-facing author line, or moving the full paper author list into the WeChat draft author field

**WeChat Paper Original Abstract**:
The original English abstract shown in a One-Paper WeChat Article for an English Public Journal Paper. It comes from Zotero metadata, the paper PDF, an author manuscript, or another approved source and is not an editorial English paraphrase.
_Avoid_: public-safe English paraphrase as the original abstract, summary-as-abstract, invented abstract

**WeChat Draft Record**:
A non-sensitive repository record showing that a WeChat Article Source has been submitted to the WeChat Official Account draft box for human preview and publication review. It may record workflow status, the remote draft `media_id`, draft creation/update time, and the eventual published URL, but it must not store access tokens, AppSecret, cookies, preview credentials, full API responses, or other secrets.
_Avoid_: treating WeChat credentials, cookies, preview tokens, raw API payloads, or human preview material as publishable state

**WeChat Draft Author Field**:
The short author value submitted to the Official WeChat draft metadata for a One-Paper WeChat Article. For journal-paper articles, it defaults to the paper's first author rather than the WOEAI account name; the full author list remains in the WeChat Paper Author Line.
_Avoid_: using the account name as the paper author by default, placing the full paper author list in the draft metadata author field

**Manual Publication Gate**:
The required human checkpoint around WeChat draft delivery and public release. Agents and automation may prepare content, upload approved images, render WeChat-compatible HTML, and create or update Official Account drafts only after the agent explains the real draft-creation action and the user explicitly confirms creating the WeChat draft. They must not automatically publish, mass-send, or otherwise release the article publicly.
_Avoid_: allowing an agent, scheduled job, API script, or browser automation flow to create or publish WeChat content from vague approval such as "continue", or without human preview and manual confirmation in the WeChat backend

**Official WeChat Draft API Path**:
The primary automation path for WOEAI WeChat article delivery. It converts the WeChat Article Source and approved public-safe assets into WeChat-compatible HTML, uploads approved cover and body images through official WeChat API endpoints, creates or updates the Official Account draft, records only a WeChat Draft Record, and then stops at the Manual Publication Gate. Its default mode is a no-submit check; a real draft creation/update requires explicit live confirmation. doocs/md is an auxiliary route for theme design, formula/style preview, and manual copy-paste fallback, not the primary automated submission path.
_Avoid_: treating doocs/md, Wechatsync, browser extensions, copied editor content, or WeChat backend HTML as the primary system of record or default automation path

**WeChat Remote Runner**:
A small trusted machine used only to run the Official WeChat Draft API Path from a stable public egress IP. It should pull the public-safe repository content, keep WeChat credentials outside the repository, run `ip-check` or `preflight` before live draft creation/update, and stop after the draft reaches the WeChat backend for human preview.
_Avoid_: using changing home/campus network IPs for unattended API calls, storing AppSecret in GitHub Actions secrets without a fixed runner IP, or letting the runner publish/mass-send content

**WeChat Egress IP Diagnostic**:
An optional diagnostic check that reports the current public egress IP and compares it with a configured fixed runner IP list. The expected IP list belongs in `~/.config/woeai/wechat_runner.env` as `WOEAI_WECHAT_EXPECTED_EGRESS_IPS`, separate from the AppID/AppSecret credential file. This local IP probe is not a live-run gate because it can disagree with the actual WeChat API path; live draft creation/update should call the official API directly after explicit user confirmation and treat WeChat's own response as the source of truth.
_Avoid_: reading private credentials just to learn the current public IP, or treating local IP-probe mismatch as stronger evidence than the WeChat API response

**WeChat RTD Link Domain**:
The preferred domain for WOEAI website links embedded in WeChat articles and WeChat draft API payloads. Use `https://woeai.readthedocs.io/zh-cn/latest/` for RTD companion pages, useful direction pages, and homepage-style links, because this Read the Docs project domain is less tied to the replaceable custom domain `winddee.cn`. Reader-facing links should normally appear under `延伸阅读` as direct hyperlinks, not as repeated label-plus-URL text or a separate `阅读原文` section. This rule applies to WeChat article links and draft payloads, not necessarily to the public website's own SEO canonical URL or contact-page display.
_Avoid_: hard-coding `winddee.cn` into WeChat article sources or generated WeChat HTML when an equivalent `woeai.readthedocs.io` URL exists

**Private WeChat Credential Store**:
The local-only credential location for the Official WeChat Draft API Path. The WeChat Official Account AppID and AppSecret live in `~/.config/woeai/wechat_official_account.env`, expected fixed runner IPs live separately in `~/.config/woeai/wechat_runner.env`, and fetched `access_token` data lives in `~/.cache/woeai/wechat_access_token.json`. These files are outside the public repository; the credential file may be read only when the user explicitly asks to test the API path or create/update a WeChat draft.
_Avoid_: committing, printing, logging, copying, or summarizing WeChat AppSecret, access tokens, cookies, preview credentials, or private config contents in public-safe files

**RTD Paper Companion Page**:
A Read the Docs page generated from a One-Paper WeChat Article. It is the default website companion for paper-based WeChat articles, but not required for temporary notices, activity posts, or non-paper WeChat content. It should preserve the same title, body text, images, DOI link, and useful related links as the WeChat article, while converting the markup and rendering format to Sphinx-compatible reStructuredText.
_Avoid_: creating a separate Markdown route for Sphinx, changing the article meaning for RTD, making the RTD page a shorter unrelated summary, or forcing every non-paper WeChat post to have an RTD companion page

**WeChat Figure Caption**:
The reader-facing caption attached to a figure in a One-Paper WeChat Article. It uses a Chinese figure-title line translated faithfully from the paper's original figure title, followed by a separate Chinese explanatory line that tells the reader why the figure matters in this article.
_Avoid_: leaving pure English figure titles in Chinese WeChat articles, merging the figure title and explanation into one paragraph, or using the caption to store extraction/copyright notes

**Public Formula**:
A mathematical expression included in a One-Paper WeChat Article or RTD Paper Companion Page. It should preserve one LaTeX formula meaning across publication channels, with channel-specific rendering. Public formulas include display equations, inline mathematical variables, symbolic parameters, evaluation metrics, dimensional quantities, and unit-bearing values such as `X_L`, `H_{\max}`, `R`, `1\,\mathrm{km} \times 1\,\mathrm{km}`, and `11\,\mathrm{m/s}`. They should remain text-based and explain key variables in prose.
_Avoid_: code-block formula, inline-code variable, unstructured plain-text formula, default formula screenshot, unexplained symbol list

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

Domain Expert: No. Student First Author marking applies to both master's and doctoral students when Degree Thesis Data or confirmed public aliases provide the names.

Dev: Should a private student relationship be marked if Degree Thesis Data and confirmed public aliases do not name the student?

Domain Expert: No. Student First Author marking should be source-bounded to Degree Thesis Data and confirmed public aliases.

Dev: Should Publication Metric labels be visually emphasized?

Domain Expert: No. Emphasize Publication Metric Values while keeping labels readable as labels.

Dev: Should WOEAI keep a standalone Team Members page?

Domain Expert: No. Let readers use the Official Profile Link for people information and publish public doctoral and master's thesis metadata under Academic Outputs.

Dev: Should public degree thesis metadata be removed for privacy?

Domain Expert: No. Keep Degree Thesis Listings when they support academic context, but do not add units, contact details, photos, IDs, or private biographical information.

Dev: Should graduated students be shown as one subsection per person?

Domain Expert: No. Use Degree Thesis Listings as ordinary text lines under the relevant degree-level group in Academic Outputs.

Dev: Should WOEAI use semantic versioning for public site updates?

Domain Expert: No. Use a Site Build ID for the public website; Git commits remain the authoritative change history.
