#!/usr/bin/env python3
"""Rejected Olympic Sports — make.fun bounty entry.

Writes one funny single-line sport the Olympics turned down to
/output/entry.txt. Pure Python standard library, deterministic.
"""

import os
import stat

LINE = (
    "Synchronized Apologizing: two athletes take turns saying sorry "
    "for four minutes straight; gold goes to whoever means it least."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
