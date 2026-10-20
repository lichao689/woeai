#!/usr/bin/env python3
"""Check explicitly selected WeChat articles; do not force legacy bulk migration."""
import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from woeai.publications.registry import load_registry
from woeai.wechat.editorial import article_structure_findings, article_title_findings
from woeai.wechat.figures import parse_figure_groups


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('articles', type=Path, nargs='+')
    args = parser.parse_args()
    research_families = {
        (ROOT / row['custom']['wechat']['path']).resolve(): row['custom']['research_family']
        for row in load_registry(ROOT)
    }
    failed = False
    for article in args.articles:
        try:
            text = article.read_text(encoding='utf-8')
            findings = article_structure_findings(text)
            _, figure_findings = parse_figure_groups(text)
            findings += figure_findings
            if article.resolve() in research_families:
                findings += article_title_findings(text, research_families[article.resolve()])
        except OSError as error:
            findings = [error.strerror or 'Cannot read article']
        for finding in findings:
            print(f'{article}: {finding}', file=sys.stderr)
        failed |= bool(findings)
    if not failed:
        print(f'WeChat editorial structure passed ({len(args.articles)} articles); semantic review still required')
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
