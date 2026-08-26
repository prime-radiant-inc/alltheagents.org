#!/usr/bin/env python3
"""One-time formatting normalization across every record.

Run this ONCE, commit it alone, and never again. It reformats all frontmatter
through a single writer so that later classification diffs are reviewable
instead of being buried in a corpus-wide reformat.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.frontmatter import iter_record_paths, read_record, write_record  # noqa: E402


def main(agents_dir: str = "agents") -> int:
    changed = 0
    for path in iter_record_paths(Path(agents_dir)):
        before = path.read_bytes()
        data, body = read_record(path)
        write_record(path, data, body)
        if path.read_bytes() != before:
            changed += 1
    print(f"Normalized {changed} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(*sys.argv[1:]))
