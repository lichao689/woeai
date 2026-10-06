"""Render full-paper pages, including blocked sources, to check real HTML boundaries."""
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.links = []

    def handle_data(self, data):
        self.text.append(data)

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.links.extend(value for key, value in attrs if key == 'href')


class PaperInlineRoleTests(unittest.TestCase):
    def test_full_paper_pages_render_roles_and_complete_links(self):
        rows = json.loads((ROOT / 'docs/data/publications.json').read_text())
        papers = [row['custom'] for row in rows
                  if row['custom'].get('rtd', {}).get('kind') == 'full_paper']
        self.assertTrue(papers)
        with tempfile.TemporaryDirectory(prefix='woeai-inline-roles-') as tmp:
            source = Path(tmp) / 'source'
            source.mkdir()
            (source / 'conf.py').write_text(
                "extensions = ['sphinx.ext.mathjax']\n"
                "project = 'Paper role regression'\n"
                "root_doc = 'index'\n"
                "html_theme = 'basic'\n"
            )
            refs = [paper['publication_ref'] for paper in papers]
            by_ref = {paper['publication_ref']: paper for paper in papers}
            index = 'Full-paper pages\n================\n\n.. toctree::\n\n'
            index += ''.join(f'   {ref}\n' for ref in refs)
            index += '\n'
            index += ''.join(f'.. _{ref}:\n\n{ref}\n' + '-' * len(ref)
                             + '\n\nPublication anchor.\n\n' for ref in refs)
            (source / 'index.rst').write_text(index)
            for paper in papers:
                original = ROOT / paper['rtd']['path']
                content = original.read_text()
                # Resolve unchanged real figure paths from the original source location.
                content = re.sub(
                    r'(?m)^(\.\. (?:image|figure):: )([^\n]+)$',
                    lambda match: match[1] + os.path.relpath(
                        (original.parent / match[2]).resolve(), source),
                    content,
                )
                (source / (paper['publication_ref'] + '.rst')).write_text(content)
            output = Path(tmp) / 'html'
            result = subprocess.run(
                [sys.executable, '-m', 'sphinx', '-b', 'html', '-W', '--keep-going',
                 str(source), str(output)], capture_output=True, text=True, timeout=90,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            for ref in refs:
                with self.subTest(paper=ref):
                    parsed = VisibleText()
                    parsed.feed((output / (ref + '.html')).read_text())
                    text = ''.join(parsed.text)
                    self.assertNotIn(':ref:', text)
                    self.assertNotIn(':math:', text)
                    if by_ref[ref]['rtd'].get('blocker_code') == 'missing_source_appendices':
                        self.assertIn('原文引用的附录 A、B', text)
                        self.assertIn('相关附录推导未收入本页', text)
                    # Docutils may silently truncate an email next to Chinese
                    # punctuation even though its full text remains visible.
                    emails = set(re.findall(
                        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
                        (source / (ref + '.rst')).read_text(),
                    ))
                    mailto = {unquote(link[7:]).split('?')[0] for link in parsed.links
                              if link.startswith('mailto:')}
                    self.assertTrue(emails <= mailto,
                                    f'{ref}: missing complete mailto links: {emails - mailto}')
                    if ref == 'ref-chen2024-JCP' and by_ref[ref]['source'].get('supplements'):
                        self.assertIn('附录 A 空间相干函数与空间相关函数', text)
                        self.assertIn('附录 B 均匀各向同性湍流特征的计算', text)
                        self.assertNotIn('相关附录推导未收入本页', text)
                        for target in ('a8', 'a9', 'a11', 'a12', 'b7', 'b8', 'b13', 'b18'):
                            self.assertTrue(any(link.endswith(f'#chen2024-jcp-{target}')
                                                for link in parsed.links), target)
                        for appendix, count in (('a', 13), ('b', 18)):
                            for number in range(1, count + 1):
                                self.assertIn(f'id="chen2024-jcp-{appendix}{number}"',
                                              (output / (ref + '.html')).read_text())
                        for appendix, count in (('a', 5), ('b', 1)):
                            for number in range(1, count + 1):
                                self.assertTrue(any(link.endswith(f'#chen2024-jcp-{appendix}-ref-{number}')
                                                    for link in parsed.links))
                    if ref == 'ref-li2024-POF':
                        for target in (15, 1, 21, 23, 41, 43):
                            self.assertTrue(any(link.endswith(f'#li2024-reference-{target}')
                                                for link in parsed.links))


if __name__ == '__main__':
    unittest.main()
