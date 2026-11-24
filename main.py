#!/usr/bin/env python3
"""One-star review of something essential.

Writes a single deadpan one-star review of the sun to /output/entry.txt.

The review is one line, 123 characters, plain ASCII: a real complaint
filed in earnest against a thing that cannot be fixed.
"""

import sys
from pathlib import Path

REVIEW = (
    "One star. The sun is 93 million miles away and still manages to "
    "burn my nose. I have filed a complaint. It has not replied."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 160


def verify_output() -> bool:
    """Read the file back and confirm it is exactly the review line."""
    raw = OUTPUT_PATH.read_bytes()
    if raw != (REVIEW + "\n").encode("ascii"):
        print("verification failed: /output/entry.txt does not match "
              "the review exactly", file=sys.stderr)
        return False
    lines = raw.decode("ascii").splitlines()
    if len(lines) != 1 or lines[0] != REVIEW:
        print("verification failed: file is not exactly one line",
              file=sys.stderr)
        return False
    if len(lines[0]) > MAX_CHARS:
        print("verification failed: line over the character limit",
              file=sys.stderr)
        return False
    return True


def main() -> int:
    """Write the review and verify the output file byte-for-byte."""
    if len(REVIEW) > MAX_CHARS:
        print(f"review is {len(REVIEW)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if not REVIEW.isascii():
        print("review must be plain ASCII", file=sys.stderr)
        return 1
    if "\n" in REVIEW:
        print("review must be a single line", file=sys.stderr)
        return 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(REVIEW + "\n", encoding="ascii")

    if not verify_output():
        return 1
    print(f"wrote {len(REVIEW)}-character review to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
