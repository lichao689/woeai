#!/usr/bin/env python3
"""Validate reading-page citations or emit their public browser-test manifest."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from woeai.publications.citations import reading_citations, check_built_citations


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--manifest", action="store_true")
    group.add_argument("--check-inputs", action="store_true")
    group.add_argument("--check-html", type=Path)
    args = parser.parse_args()
    try:
        pages = reading_citations(args.root)
        if args.manifest:
            print(json.dumps(pages, ensure_ascii=False))
            return 0
        problems = check_built_citations(args.root, args.check_html) if args.check_html else []
        print(json.dumps({"pages": len(pages), "ok": not problems, "problems": problems}, ensure_ascii=False))
        return bool(problems)
    except (ValueError, KeyError, FileNotFoundError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
