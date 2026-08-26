#!/usr/bin/env python3
"""Validate classification frontmatter across the census.

  python3 scripts/validate_classifications.py                # whole corpus, lenient
  python3 scripts/validate_classifications.py --strict        # every record must be verified
  python3 scripts/validate_classifications.py agents/cline.md # specific records

Exit code 0 when valid, 1 when any record has an error.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.classification import validate_record  # noqa: E402
from scripts.frontmatter import (  # noqa: E402
    TEMPLATE_NAME,
    iter_record_paths,
    read_record,
)


def expand(targets: list[str], default_dir: Path) -> list[Path]:
    if not targets:
        return list(iter_record_paths(default_dir))
    paths: list[Path] = []
    for target in targets:
        p = Path(target)
        if p.is_dir():
            paths.extend(iter_record_paths(p))
        elif p.name != TEMPLATE_NAME:
            paths.append(p)
    return paths


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="records or directories (default: agents/)")
    parser.add_argument("--agents-dir", default="agents")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="also fail on records that are not yet verified",
    )
    args = parser.parse_args(argv)

    paths = expand(args.paths, Path(args.agents_dir))
    errors: list[str] = []
    unreadable = 0

    for path in paths:
        try:
            record, _ = read_record(path)
        except (ValueError, OSError) as exc:
            errors.append(str(exc))
            unreadable += 1
            continue
        errors.extend(validate_record(record, str(path), strict=args.strict))

    for message in errors:
        print(message)

    print(
        f"\nValidated {len(paths)} records "
        f"({len(errors)} errors, {unreadable} unreadable)"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
