#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-mfnakmal-roast-your-own-agent-2d221bda.

Standard library only, no network. The entry is a single line of text written to
entry.txt inside the output directory, byte for byte, with no trailing newline.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "My agent wrote a 300-line comment explaining a one-line function. "
    "The function was deleted two commits ago. The comment is still maintained."
)


def output_dir() -> Path:
    """Folder named by MAKEFUN_OUTPUT_DIR when set, else OUTPUT_DIR, else /output."""
    return Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry text must be 1..280 characters, got {len(text)}"

    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_bytes(text.encode("utf-8"))

    print(f"{len(text)} characters", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
