"""Render current verified papers: successful Sphinx builds can leak literal roles."""
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

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
    def test_verified_papers_render_roles_instead_of_literal_markup(self):
        rows = json.loads((ROOT / 'docs/data/publications.json').read_text())
        papers = [row['custom'] for row in rows
                  if row['custom'].get('rtd', {}).get('status') == 'verified']
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
            index = 'Verified papers\n===============\n\n.. toctree::\n\n'
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
                    if ref == 'ref-li2024-POF':
                        for target in (15, 1, 21, 23, 41, 43):
                            self.assertTrue(any(link.endswith(f'#li2024-reference-{target}')
                                                for link in parsed.links))


if __name__ == '__main__':
    unittest.main()
