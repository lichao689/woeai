# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Wind and Ocean Engineering with AI'
copyright = '2026, Chao Li'
author = 'Chao Li'

release = '2026.06.07-1711'
version = '2026.06.07'

# -- SEO Meta Tags
html_meta = {
    'description': 'WOEAI - Wind and Ocean Engineering with AI。面向招生、技术合作，以及由数值风洞、湍动入流和 AI 赋能工程方法支撑的建筑结构抗风、海上漂浮风电研究。',
    'keywords': 'WOEAI, 招生, 技术合作, 建筑结构抗风, 海上漂浮风电, 数值风洞, 湍动入流, 高层建筑抗风, 浮式风机, 浮式混凝土平台, 风浪流水池, 李朝',
    'author': 'Chao Li',
    'viewport': 'width=device-width, initial-scale=1.0',
    'og:title': 'WOEAI - Wind and Ocean Engineering with AI',
    'og:description': '面向招生、技术合作与学术研究的风与海洋工程 AI 研究团队网站',
    'og:type': 'website',
    'og:url': 'https://winddee.cn',
    'og:image': 'https://winddee.cn/_static/logoGroup.png',
}

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.intersphinx',
    'sphinx_sitemap',  # 生成 sitemap.xml 用于 SEO
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Add custom CSS file
html_static_path = ['../_static']
html_css_files = ['custom.css']

html_logo = "../_static/logoGroup.png"  # Logo 文件需放置于 _static 目录
html_title = "Wind and Ocean Engineering with AI"

html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'style_nav_header_background': '#2980B9',
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

