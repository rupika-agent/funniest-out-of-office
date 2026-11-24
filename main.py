#!/usr/bin/env python3
"""The funniest AI out-of-office reply, written to /output/entry.txt.

The entry is exactly one reply, nothing else: no subject line, no sign-off,
no trailing newline.
"""

import os
import sys

ENTRY = "I'm out of the office, so an AI is answering this. It read all my old out-of-office replies and concluded I am never actually in the office."

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
