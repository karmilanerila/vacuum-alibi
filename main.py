#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters.

A robot vacuum files its excuse for missing a spot. The program writes
exactly one line of text to /output/entry.txt, deterministically.
"""

import os

LINE = (
    "I left that crumb as a control sample. If it moves, we have a pest "
    "problem. If it doesn't, we have a cleaning problem."
)


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1 to 200 characters, got %d" % len(text))
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if "  " in text:
        raise SystemExit("entry must not contain double spaces")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
