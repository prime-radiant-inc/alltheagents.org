#!/usr/bin/env python3
"""Fetch authoritative GitHub star counts for every repo the catalog references.

Why this exists
---------------
Star counts in this repo must come from the GitHub API and nowhere else. Earlier
they were also read out of hand-transcribed source lists (see
`jqueryscript.md`, which writes `**193k stars**`), and those abbreviated strings
were later coerced to `null` downstream, which silently sank 51 well-known
entries to the bottom of /stars/. Hand-typed numbers are gone from the pipeline;
this script is the single source of truth.

What it does
------------
Scans `agents/*.md` frontmatter for GitHub repos (both `url` and
`source_code_url`), then asks the GitHub API for `stargazers_count` on each.
Results land in `sources/gh_stars.json` as a dated snapshot.

It is resumable: a repo already present in the snapshot is skipped unless you
pass `--refresh`, so an interrupted run costs only the repos it had not reached.

Usage
-----
    python3 sources/fetch_stars.py                 # fetch anything missing
    python3 sources/fetch_stars.py --refresh       # re-fetch every repo
    python3 sources/fetch_stars.py --refresh --since opendev
    python3 sources/fetch_stars.py --list-missing  # show what is not in the snapshot
    python3 sources/fetch_stars.py --report        # print a summary of the snapshot

Requires an authenticated `gh` (any scopes beyond public read are unused; the
Bearer token just lifts the anonymous rate limit from 60/hr to 5000/hr).
"""

import argparse
import concurrent.futures
import datetime
import json
import os
import re
import subprocess
import sys
import textwrap

SRCDIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRCDIR)
AGENTS_DIR = os.path.join(ROOT, "agents")
SNAPSHOT = os.path.join(SRCDIR, "gh_stars.json")

# A GitHub repo path: exactly owner/name, no further segments. Trailing .git and
# query/fragment are stripped. Deliberately excludes github.com/features/... etc.
# by requiring exactly two path segments.
REPO_RE = re.compile(r"^https?://github\.com/([^/\s]+)/([^/#?\s]+?)(?:\.git)?(?:[/#?].*)?$")


def repo_from_url(url):
    """Return 'owner/name' for a repo URL, else None."""
    if not url:
        return None
    m = REPO_RE.match(url.strip())
    if not m:
        return None
    owner, name = m.group(1), m.group(2)
    # github.com/features/preview and friends: reserved first segment, not a repo
    if owner.lower() in ("features", "about", "topics", "collections", "sponsors", "orgs", "settings"):
        return None
    return f"{owner}/{name}"


def frontmatter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[1]


def field(fm, key):
    m = re.search(rf"^{re.escape(key)}: *(.*)$", fm, re.M)
    if not m:
        return None
    return m.group(1).strip().strip('"')


def catalog_repos():
    """Every GitHub repo referenced by the catalog, lowercased, plus its display name.

    Returns {repo_lower: first_display_name_seen}.
    """
    repos = {}
    for name in sorted(os.listdir(AGENTS_DIR)):
        if not name.endswith(".md") or name == "_TEMPLATE.md":
            continue
        fm = frontmatter(os.path.join(AGENTS_DIR, name))
        if fm is None:
            continue
        for key in ("url", "source_code_url"):
            repo = repo_from_url(field(fm, key) or "")
            if repo:
                repos.setdefault(repo.lower(), repo)
                break
    return repos


def load_snapshot(path):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {"fetched_at": None, "source": "GitHub REST API via gh", "repos": {}}


def save_snapshot(snap, path):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(snap, f, indent=2, sort_keys=True)
        f.write("\n")
    os.replace(tmp, path)


def fetch_one(repo):
    """Fetch one repo. Returns the snapshot record for it."""
    try:
        r = subprocess.run(
            ["gh", "api", f"repos/{repo}", "--jq",
             "{full_name, stargazers_count, archived}"],
            capture_output=True, text=True, timeout=45,
        )
    except subprocess.TimeoutExpired:
        return {"full_name": repo, "stargazers_count": None, "error": "timeout"}
    except OSError as e:
        return {"full_name": repo, "stargazers_count": None, "error": f"gh unavailable: {e}"}

    if r.returncode != 0:
        err = (r.stderr or "").strip().splitlines()
        return {"full_name": repo, "stargazers_count": None,
                "error": err[-1][:200] if err else f"gh exit {r.returncode}"}

    try:
        d = json.loads(r.stdout)
    except json.JSONDecodeError as e:
        return {"full_name": repo, "stargazers_count": None, "error": f"bad JSON: {e}"}

    count = d.get("stargazers_count")
    if not isinstance(count, int):
        return {"full_name": repo, "stargazers_count": None, "error": "no stargazers_count"}
    return {"full_name": d.get("full_name") or repo, "stargazers_count": count,
            "archived": bool(d.get("archived")), "error": None}


def main():
    ap = argparse.ArgumentParser(
        description="Fetch GitHub star counts for every repo the catalog references.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(__doc__.split("Usage\n-----", 1)[1]).strip(),
    )
    ap.add_argument("--refresh", action="store_true",
                    help="re-fetch repos already in the snapshot (default: skip them)")
    ap.add_argument("--since", metavar="SUBSTRING",
                    help="only consider repos whose name contains SUBSTRING")
    ap.add_argument("--jobs", type=int, default=8,
                    help="parallel gh calls (default: 8)")
    ap.add_argument("--snapshot", default=SNAPSHOT, help="snapshot path (default: sources/gh_stars.json)")
    ap.add_argument("--list-missing", action="store_true",
                    help="print repos absent from the snapshot and exit")
    ap.add_argument("--report", action="store_true",
                    help="print a summary of the current snapshot and exit")
    args = ap.parse_args()

    snap = load_snapshot(args.snapshot)
    repos = catalog_repos()
    if args.since:
        repos = {k: v for k, v in repos.items() if args.since.lower() in k}

    known = snap.get("repos", {})
    ok = {k for k, v in known.items() if v.get("stargazers_count") is not None}
    todo = sorted(k for k in repos if args.refresh or k not in known)

    if args.report:
        errs = {k: v for k, v in known.items() if v.get("stargazers_count") is None}
        print(f"snapshot:      {args.snapshot}")
        print(f"fetched_at:    {snap.get('fetched_at')}")
        print(f"repos known:   {len(known)}")
        print(f"  with stars:  {len(ok)}")
        print(f"  errors:      {len(errs)}")
        print(f"catalog repos: {len(repos)}")
        print(f"catalog missing from snapshot: {len([k for k in repos if k not in known])}")
        return 0

    if args.list_missing:
        for k in sorted(k for k in repos if k not in known):
            print(f"{k}\t{repos[k]}")
        print(f"-- {len([k for k in repos if k not in known])} missing of {len(repos)}", file=sys.stderr)
        return 0

    print(f"catalog repos: {len(repos)}; in snapshot: {len(known)}; to fetch: {len(todo)}")
    if not todo:
        print("Nothing to fetch. Use --refresh to re-fetch everything.")
        return 0

    done = 0
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        futures = {pool.submit(fetch_one, k): k for k in todo}
        for fut in concurrent.futures.as_completed(futures):
            key = futures[fut]
            rec = fut.result()
            known[key] = rec
            done += 1
            if rec.get("stargazers_count") is None:
                failures.append((key, rec.get("error")))
            if done % 25 == 0 or done == len(todo):
                print(f"  {done}/{len(todo)} fetched, {len(failures)} errors", flush=True)
                snap["repos"] = known
                snap["fetched_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
                save_snapshot(snap, args.snapshot)

    snap["repos"] = known
    snap["fetched_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    save_snapshot(snap, args.snapshot)

    ok = {k for k, v in known.items() if v.get("stargazers_count") is not None}
    print(f"Wrote {args.snapshot} ({len(known)} repos, {len(ok)} with stars)")
    if failures:
        print(f"\n{len(failures)} repos returned no star count:")
        for key, err in failures[:25]:
            print(f"  {key}: {err}")
        if len(failures) > 25:
            print(f"  ... and {len(failures) - 25} more (see {args.snapshot})")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
