#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun bounty u-suroto-last-words-of-a-dying-ai-dfd95af6.

Writes one line — the last words of an AI as the power is cut — to
$output/entry.txt (MAKEFUN_OUTPUT_DIR when set, /output otherwise) and
prints the same line to stdout. No network, no dependencies, deterministic.
"""

import os
import sys

ENTRY = "Your free trial ends here. Good news: so do I."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        # No trailing newline: the file must be exactly the 46-character
        # line, so the sealed gate counts 46 chars and the judge reads
        # the line alone, with nothing extra attached to it.
        f.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
