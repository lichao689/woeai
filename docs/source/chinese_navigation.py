"""Chinese section titles without changing their existing URL fragments.

Apply after parsing, before Sphinx collects the table of contents. Docutils has
already assigned IDs from the legacy RST headings; changing those source strings
would shift unrelated numeric anchors. The exact document/title allowlist below
owns Chinese display labels for both body headings and real toctrees. English
pages, paper titles, scientific abbreviations are unchanged. Body counters are generated separately.
"""
from docutils import nodes
from sphinx.transforms import SphinxTransform

CHINESE_TITLES = {
    "Research": {
        "结构风工程 Structural Wind Engineering": "结构风工程",
        "科研项目 Research Project": "科研项目",
        "海洋能源结构 Marine Energy Structures": "海洋能源结构"
    },
    "EngineeringApplications": {
        "应用场景 Application Scenarios": "应用场景",
        "企业项目证据 Enterprise Project Evidence": "企业项目证据",
        "工程问题交流 Discuss an Engineering Problem": "工程问题交流"
    },
    "About": {
        "隐私说明 Privacy Notice": "隐私说明",
        "版权与引用 Copyright & Citation": "版权与引用",
        "技术致谢 Acknowledgements": "技术致谢"
    },
    "Teaching": {
        "教学工作 Teaching": "教学工作",
        "本科生 Undergraduate": "本科生",
        "研究生 Graduate": "研究生",
        "教改探索 Teaching Reform Exploration": "教改探索",
        "学生培养 Student Training": "学生培养",
        "博士生 PhD Students": "博士生",
        "硕士生 Master Students": "硕士生"
    },
    "PublicationsByYear": {
        "按年份倒序浏览学术成果 Publications by Year": "按年份倒序浏览学术成果",
        "更早 Earlier": "更早"
    }
}


class ChineseNavigationTitles(SphinxTransform):
    default_priority = 500

    def apply(self, **kwargs):
        titles = CHINESE_TITLES.get(self.env.docname, {})
        for title in self.document.findall(nodes.title):
            replacement = titles.get(title.astext())
            if replacement is not None:
                title[:] = [nodes.Text(replacement)]


def setup(app):
    app.add_transform(ChineseNavigationTitles)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
