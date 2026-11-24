#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun bounty entry.

Writes the entry text (exactly two lines, each one sentence) to
/output/entry.txt. The entry text is the only output.
"""

import os

ENTRY = (
    "Do not hit reply-all at 2 a.m. the night before the wedding "
    "to complain that the seating chart is wrong.\n"
    "It reached all 180 guests before dawn, and you spent your wedding "
    "morning apologizing instead of getting married."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
