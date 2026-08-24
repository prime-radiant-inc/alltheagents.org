#!/usr/bin/env python3
"""Apply audited category values from a TSV to existing agent pages."""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "sources" / "category_audit_first_100.tsv"
AGENTS_DIR = ROOT / "agents"
VALID_CATEGORIES = {"harness", "multiplexer", "tool", "something-else"}


def update_category(content, category):
    if not content.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")

    end = content.find("\n---", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")

    frontmatter = content[:end]
    rest = content[end:]
    replacement = f"category: {category}"

    if re.search(r"^category:\s*.*$", frontmatter, flags=re.MULTILINE):
        frontmatter = re.sub(
            r"^category:\s*.*$",
            replacement,
            frontmatter,
            count=1,
            flags=re.MULTILINE,
        )
    else:
        frontmatter, count = re.subn(
            r'^layout:\s*"?agent\.njk"?\s*$',
            lambda match: f"{match.group(0)}\n{replacement}",
            frontmatter,
            count=1,
            flags=re.MULTILINE,
        )
        if count == 0:
            raise ValueError("missing layout line for category insertion")

    return frontmatter + rest


def main():
    changed = 0
    with AUDIT_PATH.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["source"] != "agents":
                continue
            category = row["category"]
            if category not in VALID_CATEGORIES:
                raise ValueError(f"invalid category {category!r} for {row['slug']}")

            path = AGENTS_DIR / f"{row['slug']}.md"
            if not path.exists():
                raise FileNotFoundError(path)

            content = path.read_text(encoding="utf-8")
            updated = update_category(content, category)
            if updated != content:
                path.write_text(updated, encoding="utf-8")
                changed += 1

    print(f"Updated {changed} agent pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
