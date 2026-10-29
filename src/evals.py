"""Offline eval runner stub."""

from __future__ import annotations
import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", required=True)
    args = parser.parse_args()
    suite = json.loads(Path(args.suite).read_text(encoding="utf-8"))
    cases = suite.get("cases", [])
    print(f"Loaded {len(cases)} eval cases from {args.suite}")
    for case in cases:
        print(f"- {case.get('id', 'case')}: pending")
    print("Wire scorers.py to compute pass/fail.")


if __name__ == "__main__":
    main()
