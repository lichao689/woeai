# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Wind & Ocean Engineering empowered by AI'
copyright = '2025, Wind & Ocean Engineering empowered by AI Group'
author = 'Chao Li <lichaosz@qq.com>'

release = '0.1'
version = '0.1.0'

# -- SEO Meta Tags
html_meta = {
    'description': 'WOEAI - 风与海洋工程人工智能赋能团队，哈尔滨工业大学（深圳）。研究方向：数值风洞、结构抗风、海上风电。',
    'keywords': 'WOEAI, 风工程, 海洋工程, 海上风电, 数值风洞, 结构抗风, 哈尔滨工业大学, HIT, 李朝',
    'author': 'Chao Li',
    'viewport': 'width=device-width, initial-scale=1.0',
    'og:title': 'WOEAI - 风与海洋工程人工智能赋能团队',
    'og:description': '将人工智能技术赋能建筑和海洋工程结构防灾减灾',
    'og:type': 'website',
    'og:url': 'https://winddee.cn',
    'og:image': 'https://winddee.cn/_static/logoGroup.png',
}

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
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
html_title = "Wind & Ocean Engineering empowered by AI"

# -- Google Analytics 配置
# 请将下方的 GA_MEASUREMENT_ID 替换为你的 Google Analytics 4 衡量 ID
# 格式: G-XXXXXXXXXX
html_theme_options = {
    'analytics_id': 'G-387579615',  # Google Analytics 4
    'analytics_anonymize_ip': True,
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

# -- Favicon 配置
# html_favicon = "../_static/favicon.ico"  # 如有 favicon 可取消注释

