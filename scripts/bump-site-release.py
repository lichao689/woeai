#!/usr/bin/env python3
"""Update the Sphinx site metadata with a Beijing-time Site Build ID."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONF_PATH = ROOT / "docs/source/conf.py"
BEIJING = ZoneInfo("Asia/Shanghai")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--conf-path", type=Path, default=DEFAULT_CONF_PATH)
    parser.add_argument(
        "--datetime",
        help="Build datetime for deterministic runs, e.g. 2026-06-07T15:30:00+08:00",
    )
    return parser.parse_args()


def build_datetime(value: str | None) -> dt.datetime:
    if value:
        parsed = dt.datetime.fromisoformat(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=BEIJING)
        return parsed.astimezone(BEIJING)
    return dt.datetime.now(BEIJING)


def replace_assignment(text: str, name: str, value: str) -> str:
    pattern = re.compile(
        rf"^{name}\s*=\s*(['\"]).*?\1(?P<line_end>\r?\n|$)",
        flags=re.M,
    )

    def replacement(match: re.Match[str]) -> str:
        line_end = "\n" if match.group("line_end") else ""
        return f"{name} = '{value}'{line_end}"

    text, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise SystemExit(f"Could not find exactly one {name!r} assignment")
    return text


def update_conf(conf_path: Path, when: dt.datetime) -> tuple[str, str]:
    release = when.strftime("%Y.%m.%d-%H%M")
    version = when.strftime("%Y.%m.%d")
    with conf_path.open("r", encoding="utf-8", newline="") as handle:
        text = handle.read()
    had_final_newline = text.endswith("\n")
    text = replace_assignment(text, "release", release)
    text = replace_assignment(text, "version", version)
    if had_final_newline and not text.endswith("\n"):
        text += "\n"
    with conf_path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return release, version


def main() -> None:
    args = parse_args()
    release, version = update_conf(args.conf_path, build_datetime(args.datetime))
    print(f"Updated {args.conf_path}: release={release} version={version}")


if __name__ == "__main__":
    main()
