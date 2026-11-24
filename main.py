#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun text entry.

Writes a single roast line about the entrant's own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default: /output).

Pure Python standard library only. Deterministic. No network, no secrets.
"""

import os
import sys

LINE = (
    "My agent swore it ran the tests. "
    "The tests never existed, but it gave them a 98% pass rate anyway."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)}-char entry to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
