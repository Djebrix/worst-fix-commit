#!/usr/bin/env python3
"""Worst Fix Ever entry: writes the single commit-message line to /output/entry.txt.

Stdlib only, no network, deterministic: every run writes byte-identical output.
"""

import os

ENTRY = "fix: crash on save fixed, crash on load added"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
