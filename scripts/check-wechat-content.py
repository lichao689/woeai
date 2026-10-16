#!/usr/bin/env python3
"""Check explicitly selected WeChat articles; do not force legacy bulk migration."""
import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from woeai.wechat.editorial import article_structure_findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('articles', type=Path, nargs='+')
    args = parser.parse_args()
    failed = False
    for article in args.articles:
        try:
            findings = article_structure_findings(article.read_text(encoding='utf-8'))
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
