"""Chinese homepage headings use Chinese; the English homepage stays English."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

from jinja2 import Environment, FileSystemLoader
from woeai.publications.homepage import render_home_progress

ROOT = Path(__file__).resolve().parents[1]


class HeadingLabels(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.labels = []
        self.current = None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get('class', '').split()
        if tag in {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'} or (
                tag == 'p' and {'eyebrow', 'card-index'} & set(classes)):
            self.current = [tag, classes, '']
        elif tag == 'br' and self.current:
            self.current[2] += ' '

    def handle_data(self, text):
        if self.current:
            self.current[2] += text

    def handle_endtag(self, tag):
        if self.current and self.current[0] == tag:
            self.labels.append(self.current)
            self.current = None


def render_home(english=False):
    source = (ROOT / 'docs/source/index.rst').read_text()
    # Exercise fresh generated cards as well as the hand-maintained heading source.
    before, generated = source.split('.. BEGIN GENERATED LATEST PAPER NOTES', 1)
    _, after = generated.split('.. END GENERATED LATEST PAPER NOTES', 1)
    cards = '\n'.join('   ' + line for line in render_home_progress(ROOT).splitlines())
    source = before + '\n.. raw:: html\n\n' + cards + '\n' + after
    body = '\n'.join(line[3:] for line in source.splitlines() if line.startswith('   '))
    env = Environment(loader=FileSystemLoader(ROOT / 'docs/source/_templates'))
    return env.get_template('en-home.html' if english else 'home.html').render(
        language='en' if english else 'zh-CN', is_english=english,
        body=body, recent_progress=render_home_progress(ROOT, english=english),
        title='WOEAI', metatags='', pageurl='', css_files=[], script_files=[],
        pathto=lambda page, *args: page, site_home='en/index' if english else 'index',
        language_target='index' if english else 'en/index', language_label='中文' if english else 'EN',
        pagename='en/index' if english else 'index', copyright='2026, Chao Li')


class HomepageHeadingLanguageTests(unittest.TestCase):
    def test_chinese_home_titles_and_attached_labels_do_not_repeat_english(self):
        html = render_home()
        labels = HeadingLabels(html).labels
        self.assertGreater(len(labels), 15)
        for tag, classes, text in labels:
            with self.subTest(tag=tag, text=text):
                self.assertTrue(text.strip(), 'no empty heading or retained empty label')
                if tag in {'h1', 'h2', 'h3'} or 'eyebrow' in classes:
                    self.assertIsNone(re.search('[A-Za-z]', re.sub(r'\b(?:AI|WOEAI)\b', '', text)))
                if 'card-index' in classes:
                    self.assertRegex(text, r'^0[12]$')
        self.assertNotIn('Wind and Ocean Engineering with AI Laboratory', html)
        for text in ('AI 赋能', 'WOEAI', 'Kriging 代理模型',
                     'A novel framework for urban geometry rapid reconstruction',
                     'Numerical research on the impact of built-in rectangular poles'):
            self.assertIn(text, html)

    def test_english_home_retains_its_original_heading_labels_and_brand(self):
        html = render_home(english=True)
        labels = [text for _, _, text in HeadingLabels(html).labels]
        for text in ('WIND AND OCEAN ENGINEERING WITH AI LABORATORY',
                     'WOEAI Lab', 'RESEARCH DIRECTIONS', 'LATEST ACADEMIC PROGRESS',
                     'CONNECT & COLLABORATE'):
            self.assertIn(text, labels)
        self.assertIn('Wind and Ocean Engineering with AI Laboratory', html)
        self.assertIn('01 / WIND', labels)
        self.assertIn('02 / OCEAN', labels)
