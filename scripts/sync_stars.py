#!/usr/bin/env python3
"""Keep every stored star count in sync with the GitHub snapshot.

Why this exists
---------------
Star counts used to enter this repo two ways: the GitHub API *and* hand-typed
values in the source lists (`**193k stars**`). The two disagreed, and the
hand-typed ones were silently coerced to `null` downstream, which dropped 51
well-known entries to the bottom of /stars/. Star counts now come from one
place: `sources/gh_stars.json`, written by `sources/fetch_stars.py`. This script
is what carries that snapshot into the catalog.

What it syncs
-------------
  agents/*.md                  the `stars:` frontmatter line (surgically: every
                               other line, and the body, is left byte-identical,
                               because these files carry enrichment work that a
                               full regeneration would clobber)
  _data/agents.json            the `stars` field of matching entries
  coding_agent_harnesses.tsv   the `stars` column of matching rows

Usage
-----
    python3 scripts/sync_stars.py --report      # what is out of sync, change nothing
    python3 scripts/sync_stars.py               # apply the snapshot
    python3 scripts/sync_stars.py --dry-run     # show the edits without writing
    python3 scripts/sync_stars.py --check       # exit 1 if a known star is unapplied

`--check` is the guard against the original bug: it fails when the snapshot has
a star count for an entry's repo but the entry does not carry it. Repos the API
cannot resolve (deleted, renamed out from under us, or a bad URL) are reported
as warnings instead, so the check stays a real signal rather than permanent red.
"""

import argparse
import json
import os
import re
import sys

SRCDIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRCDIR)
AGENTS_DIR = os.path.join(ROOT, "agents")
sys.path.insert(0, os.path.join(ROOT, "sources"))
from fetch_stars import repo_from_url, frontmatter, field  # noqa: E402  (shared repo parsing)

SNAPSHOT = os.path.join(ROOT, "sources", "gh_stars.json")
AGENTS_JSON = os.path.join(ROOT, "_data", "agents.json")
TSV = os.path.join(ROOT, "coding_agent_harnesses.tsv")

STARS_LINE = re.compile(r"^stars:.*$", re.M)


def load_snapshot(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f).get("repos", {})


def entry_repo(fm):
    """The GitHub repo an entry points at, or None. url wins over source_code_url."""
    for key in ("url", "source_code_url"):
        repo = repo_from_url(field(fm, key) or "")
        if repo:
            return repo.lower()
    return None


def scan_entries():
    """Every published-or-not entry file, with its repo and current stars.

    Returns a list of dicts: path, name, category, repo, stars (int or None).
    """
    out = []
    for name in sorted(os.listdir(AGENTS_DIR)):
        if not name.endswith(".md") or name == "_TEMPLATE.md":
            continue
        path = os.path.join(AGENTS_DIR, name)
        fm = frontmatter(path)
        if fm is None:
            continue
        raw = field(fm, "stars")
        stars = int(raw.strip('"')) if raw and raw.strip('"').isdigit() else None
        out.append({
            "path": path,
            "name": field(fm, "name") or name,
            "category": (field(fm, "category") or "").strip('"'),
            "repo": entry_repo(fm),
            "stars": stars,
        })
    return out


def classify(entries, snapshot):
    """Split entries into (updates, unresolved, in_sync).

    updates     snapshot has a count that differs from what the entry stores
    unresolved  entry points at a repo the API could not resolve to a count
    in_sync     entry already matches the snapshot
    """
    updates, unresolved, in_sync = [], [], []
    for e in entries:
        if not e["repo"]:
            continue
        rec = snapshot.get(e["repo"])
        count = rec.get("stargazers_count") if rec else None
        if count is None:
            unresolved.append((e, (rec or {}).get("error") or "not in snapshot"))
        elif e["stars"] != count:
            updates.append((e, count))
        else:
            in_sync.append(e)
    return updates, unresolved, in_sync


def apply_md(path, count):
    """Rewrite only the `stars:` line inside frontmatter. Returns True if changed."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: no frontmatter")
    head, fm, rest = parts
    new_fm, n = STARS_LINE.subn(f'stars: "{count}"', fm, count=1)
    if n != 1:
        raise ValueError(f"{path}: expected exactly one stars line, found {n}")
    new_text = "---".join([head, new_fm, rest])
    if new_text == text:
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    return True


def sync_agents_json(counts, dry_run):
    if not os.path.exists(AGENTS_JSON):
        return 0, 0
    with open(AGENTS_JSON, encoding="utf-8") as f:
        data = json.load(f)
    changed = 0
    unknown = 0
    for e in data:
        repo = repo_from_url(e.get("url") or "") or repo_from_url(e.get("source_code_url") or "")
        repo = repo.lower() if repo else None
        if not repo:
            continue
        if repo in counts:
            if e.get("stars") != counts[repo]:
                e["stars"] = counts[repo]
                changed += 1
        else:
            unknown += 1
    if changed and not dry_run:
        with open(AGENTS_JSON, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
    return changed, unknown


def sync_tsv(counts, dry_run):
    import csv
    if not os.path.exists(TSV):
        return 0, 0
    with open(TSV, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        fields = reader.fieldnames
        rows = list(reader)
    if "stars" not in fields:
        return 0, 0
    changed, unknown = 0, 0
    for r in rows:
        repo = repo_from_url(r.get("url") or "") or repo_from_url(r.get("source_code_url") or "")
        repo = repo.lower() if repo else None
        if not repo:
            continue
        if repo in counts:
            if (r.get("stars") or "").strip() != str(counts[repo]):
                r["stars"] = str(counts[repo])
                changed += 1
        else:
            unknown += 1
    if changed and not dry_run:
        with open(TSV, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
            w.writeheader()
            w.writerows(rows)
    return changed, unknown


def main():
    ap = argparse.ArgumentParser(
        description="Sync stored star counts with the GitHub snapshot.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("Usage\n-----", 1)[1].strip(),
    )
    ap.add_argument("--check", action="store_true",
                    help="change nothing; exit 1 if the snapshot holds a count the catalog lacks")
    ap.add_argument("--report", action="store_true",
                    help="print the sync status and exit")
    ap.add_argument("--dry-run", action="store_true", help="show edits without writing")
    ap.add_argument("--snapshot", default=SNAPSHOT, help="snapshot path (default: sources/gh_stars.json)")
    args = ap.parse_args()

    snapshot = load_snapshot(args.snapshot)
    counts = {k: v["stargazers_count"] for k, v in snapshot.items()
              if v.get("stargazers_count") is not None}
    entries = scan_entries()
    updates, unresolved, in_sync = classify(entries, snapshot)

    print(f"snapshot:            {args.snapshot}")
    print(f"repos with a count:  {len(counts)}")
    print(f"entries scanned:     {len(entries)}")
    print(f"  in sync:           {len(in_sync)}")
    print(f"  need updating:     {len(updates)}")
    print(f"  no GitHub repo:    {len([e for e in entries if not e['repo']])}  (stars stay as-is)")
    print(f"  unresolvable repo: {len(unresolved)}")

    if unresolved:
        print("\nRepos the API could not resolve (stars left untouched):")
        for e, why in unresolved:
            print(f"  {e['name'][:32]:34} {e['repo'][:40]:42} {why}")

    if args.report:
        if updates:
            print("\nWould update (showing 15):")
            for e, count in sorted(updates, key=lambda u: -u[1])[:15]:
                shown = e["stars"] if e["stars"] is not None else "null"
                print(f"  {e['name'][:30]:32} {str(shown):>8} -> {count}")
        return 0

    if args.check:
        if updates:
            print(f"\nFAIL: {len(updates)} entries carry a stale or missing star count.", file=sys.stderr)
            for e, count in updates[:20]:
                shown = e["stars"] if e["stars"] is not None else "null"
                print(f"  {e['path']}: has {shown}, snapshot says {count}", file=sys.stderr)
            if len(updates) > 20:
                print(f"  ... and {len(updates) - 20} more", file=sys.stderr)
            print("Run: python3 scripts/sync_stars.py", file=sys.stderr)
            return 1
        print("\nOK: every resolvable GitHub entry matches the snapshot.")
        return 0

    md_changed = 0
    for e, count in updates:
        if apply_md(e["path"], count):
            md_changed += 1
    aj_changed, aj_unknown = sync_agents_json(counts, args.dry_run)
    tsv_changed, tsv_unknown = sync_tsv(counts, args.dry_run)

    verb = "Would update" if args.dry_run else "Updated"
    print(f"\n{verb} {md_changed} agents/*.md")
    print(f"{verb} {aj_changed} _data/agents.json entries ({aj_unknown} not resolvable)")
    print(f"{verb} {tsv_changed} coding_agent_harnesses.tsv rows ({tsv_unknown} not resolvable)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
