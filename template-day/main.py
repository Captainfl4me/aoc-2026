#!/usr/bin/env python3
"""Advent of Code 2026 — daily solution scaffold.

Usage:
    python3 main.py            # runs on the real input
    python3 main.py --test     # runs on test.txt
    python3 main.py <path>     # runs on a custom file
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAY = Path(__file__).resolve().parent.name  # e.g. day-01


def read_input(path: Path) -> str:
    return path.read_text().strip()


def parse(data: str):
    return data.splitlines()


def part1(data) -> int:
    raise NotImplementedError


def part2(data) -> int:
    raise NotImplementedError


def main() -> None:
    args = sys.argv[1:]
    if args and not args[0].startswith("-"):
        path = Path(args[0])
    else:
        filename = "test.txt" if "--test" in args else "input.txt"
        path = ROOT / "aoc-2026-inputs" / DAY / filename
    data = parse(read_input(path))
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
