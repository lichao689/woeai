# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Wind and Ocean Engineering with AI'
copyright = '2026, Chao Li'
author = 'Chao Li'

release = '2026.10.21-1129'
version = '2026.10.21'

# -- SEO Meta Tags
html_meta = {
    'description': 'WOEAI - Wind and Ocean Engineering with AI。面向招生、工程应用，以及由数值风洞、湍动入流和 AI 赋能工程方法支撑的结构风工程、海洋能源结构研究。',
    'keywords': 'WOEAI, 招生, 工程应用, 技术合作, 结构风工程, 海洋能源结构, 数值风洞, 湍动入流, 高层建筑抗风, 浮式风机, 浮式混凝土平台, 风浪流水池, 李朝',
    'author': 'Chao Li',
    'viewport': 'width=device-width, initial-scale=1.0',
    'og:title': 'WOEAI - Wind and Ocean Engineering with AI',
    'og:description': '面向招生、工程应用与学术研究的风与海洋工程 AI 研究团队网站',
    'og:type': 'website',
    'og:url': 'https://winddee.cn',
    'og:image': 'https://winddee.cn/_static/logoGroup.png',
}

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.mathjax',
    'sphinx_sitemap',  # 生成 sitemap.xml 用于 SEO
]

templates_path = ['_templates']
exclude_patterns = ['_paper-notes-fragment.rst']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Add custom CSS file
html_static_path = ['../_static']
html_css_files = ['custom.css']
html_js_files = ['doi-new-tab.js', 'site-navigation.js']

# -- MathJax: vendored instead of an overseas CDN -------------------------
# 42 of 44 paper-note pages render LaTeX with MathJax. The Sphinx default
# (cdn.jsdelivr.net) added a second overseas dependency on top of the Cloudflare
# edge and was measured from Guangzhou at 1.2 s best case and 7.3 s worst case,
# with formulas invisible until it finished. The bundle is now served from our
# own _static, so every request shares one origin.
mathjax_path = 'mathjax/tex-mml-chtml.js'
# ``chtml.fontURL`` is not set here: MathJax writes it verbatim into the page's
# @font-face rules, and a static value would be page-relative and 404 on every
# nested paper-note page. The mathjax_vendored extension injects the correct
# root-relative path per page (see its module docstring).

html_logo = "../_static/logoGroup.png"  # Logo 文件需放置于 _static 目录
html_title = "Wind and Ocean Engineering with AI"

html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'style_nav_header_background': '#f6f7f4',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# -- 搜索功能优化
html_search_language = 'zh'  # 支持中文搜索
html_use_indexer = True

# -- SEO: Canonical URL
html_baseurl = 'https://winddee.cn/'

# -- Sitemap 配置 (用于 SEO)
sitemap_url_scheme = "{link}"

# -- Options for EPUB output
# epub_show_urls = 'footnote'

# 关闭"查看页面源代码"链接
html_show_sourcelink = False

html_favicon = "../_static/favicon.png"


# Keep operational-board assets page-local and content-versioned. Raw HTML
# script/link tags bypass Sphinx's asset hashes and may remain cached after RTD
# publishes a new build. The JSON URL likewise changes whenever its bytes do.
def _add_publication_board_assets(app, pagename, templatename, context, doctree):
    if pagename != 'PublicationProgress':
        return
    import hashlib
    from pathlib import Path

    app.add_css_file('publication-board.css')
    app.add_js_file('publication-board.js', loading_method='defer')
    data = Path(app.confdir).parent / '_static/publication-board-data.json'
    version = hashlib.sha256(data.read_bytes()).hexdigest()[:16]
    source = 'data-source="_static/publication-board-data.json"'
    if context['body'].count(source) != 1:
        raise ValueError('Publication board must contain exactly one data source')
    context['body'] = context['body'].replace(
        source, f'data-source="_static/publication-board-data.json?v={version}"')


def _select_home_template(app, pagename, templatename, context, doctree):
    if pagename == 'index':
        return 'home.html'


def setup(app):
    # Sphinx 9.0.4's Chinese search uses english-stemmer.js but emits the
    # nonexistent ChineseStemmer constructor. Register a matching constructor
    # name while retaining Chinese tokenization and the existing zh index.
    from sphinx.search.zh import SearchChinese

    class ChineseSearchWithEnglishStemmer(SearchChinese):
        language_name = 'English'

    app.add_search_language(ChineseSearchWithEnglishStemmer)
    app.connect('html-page-context', _add_publication_board_assets)
    app.connect('html-page-context', _select_home_template)

# Local bilingual presentation, sharing the publication registry and site shell.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
extensions.append('english_site')
# Reader-page headings follow the homepage: English eyebrow, Chinese h1.
extensions.append('page_eyebrow')
# Vendored MathJax needs its fontURL rewritten per page depth (see module docstring).
extensions.append('mathjax_vendored')

# Every Chinese note and English highlight receives checked registry citation text.
extensions.append("paper_citations")

# Translate after parsing so existing numeric and named anchors remain stable.
extensions.append("chinese_navigation")
