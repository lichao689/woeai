#!/usr/bin/env python3
"""Validate the publication registry and generate its read-only views."""
import argparse
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from woeai.publications.registry import load_registry, validate_registry, write_views, check_views


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT)
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check',action='store_true')
    mode.add_argument('--write',action='store_true')
    args=parser.parse_args(); root=args.root.resolve()
    try:
        records=load_registry(root); problems=validate_registry(records,root)
        from jsonschema import Draft7Validator
        schema=json.loads((ROOT/'docs/data/schemas/csl-data.json').read_text())
        problems.extend(f'CSL {list(error.path)}: {error.message}' for error in Draft7Validator(schema).iter_errors(records))
        if args.write and not problems: write_views(root,records)
        problems+=check_views(root,records)
    except (ValueError,OSError,KeyError,TypeError) as exc:
        problems=[str(exc)]
    print(json.dumps({'ok':not problems,'problems':problems},ensure_ascii=False,indent=2))
    return bool(problems)

if __name__=='__main__':
    raise SystemExit(main())
