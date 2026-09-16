#!/usr/bin/env python3
"""Backfill `date_added` (catalog-addition date) into agents/*.md frontmatter.

Rule (per maintainer decision 2026-09-16):
  1. `first_released` when the entry has one,
  2. else the earliest local git commit touching the file (`git log --follow`),
  3. else 2026-08-19 (the initial bulk upload; also the fallback when a file
     has no git history at all).

Writes exactly one line per changed file, directly above the
`last_verified:` line when one exists (else just inside the closing `---`),
so diffs stay minimal.
Idempotent: files that already carry `date_added` are left alone.

Run with:  python3 scripts/backfill_date_added.py [--check]
  --check  report files missing date_added without writing anything.
"""

import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FALLBACK = "2026-08-19"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def frontmatter_value(path, key):
    """Read one scalar frontmatter value without a YAML dependency.

    Splits on delimiter *lines* so a value containing `---` (e.g. a GitHub
    URL like .../LLM---Detect-...) cannot truncate the block; see
    sources/fetch_stars.py for the same treatment.
    """
    lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None
    for ln in lines[1:end]:
        k, sep, v = ln.partition(":")
        if sep and k.strip() == key:
            v = v.strip()
            if v == "null":
                return None
            if len(v) >= 2 and v.startswith('"') and v.endswith('"'):
                return v[1:-1].replace('\\"', '"')
            return v or None
    return None


def earliest_commit(path):
    """Earliest commit date (YYYY-MM-DD) touching path, following renames."""
    rel = os.path.relpath(path, ROOT)
    r = subprocess.run(
        ["git", "log", "--follow", "--format=%ad", "--date=short", "--", rel],
        capture_output=True, text=True, cwd=ROOT)
    dates = [d for d in r.stdout.split() if DATE_RE.match(d)]
    return dates[-1] if dates else None


def date_for(path):
    """(date, source) per the backfill rule."""
    rel = first_released = frontmatter_value(path, "first_released")
    if first_released and DATE_RE.match(first_released):
        return first_released, "first_released"
    commit = earliest_commit(path)
    if commit:
        return commit, "earliest-commit"
    return FALLBACK, "fallback"


def apply(path, date):
    lines = open(path, encoding="utf-8").read().split("\n")
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    body = lines[1:end]
    if any(l.startswith("date_added:") for l in body):
        return False
    try:
        at = next(i for i, l in enumerate(body) if l.startswith("last_verified:"))
    except StopIteration:
        # Older bulk entries carry no last_verified; land just inside the
        # closing delimiter so the line still sits in frontmatter.
        at = len(body)
    body.insert(at, f'date_added: "{date}"')
    lines[1:end] = body
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return True


def main():
    check = "--check" in sys.argv
    files = sorted(p for p in glob.glob(os.path.join(ROOT, "agents", "*.md"))
                   if not p.endswith("_TEMPLATE.md"))
    missing, changed, sources = [], 0, {}
    for path in files:
        if frontmatter_value(path, "date_added"):
            continue
        date, source = date_for(path)
        sources[source] = sources.get(source, 0) + 1
        if check:
            missing.append(os.path.basename(path))
        elif apply(path, date):
            changed += 1
    if check:
        print(f"{len(missing)} files missing date_added")
        for name in missing[:20]:
            print(f"  {name}")
        sys.exit(1 if missing else 0)
    print(f"backfilled date_added in {changed} files "
          f"(sources: {sources or 'none — all present'})")


if __name__ == "__main__":
    main()
