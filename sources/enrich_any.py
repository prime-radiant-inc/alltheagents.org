#!/usr/bin/env python3
"""Enrich an arbitrary list of GitHub repos using the shared cache. Resumable."""
import os, csv, json, subprocess, sys

SRCDIR = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(SRCDIR, "gh_cache.json")

def load_cache():
    if os.path.exists(CACHE):
        return json.load(open(CACHE))
    return {}

def save_cache(c):
    with open(CACHE, "w") as f:
        json.dump(c, f)

def gh_api(repo):
    try:
        r = subprocess.run(
            ["gh", "api", f"repos/{repo}", "--jq",
             "{full_name,description,license:.license.spdx_id,owner:.owner.login,owner_type:.owner.type,created_at,pushed_at,language,stargazers_count,homepage,archived,topics}"],
            capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            return {"error": r.stderr.strip()[:200]}
        return json.loads(r.stdout)
    except Exception as e:
        return {"error": str(e)[:200]}

def enrich_list(repos):
    """repos: list of repo strings (owner/name). Enriches those not in cache."""
    cache = load_cache()
    todo = [r for r in repos if r.lower() not in cache]
    print(f"Cache: {len(cache)}; to fetch: {len(todo)}")
    for i, repo in enumerate(todo):
        if i % 50 == 0:
            print(f"  {i}/{len(todo)} ... {repo}", flush=True)
        cache[repo.lower()] = gh_api(repo)
        if i % 25 == 0:
            save_cache(cache)
    save_cache(cache)
    print(f"Cache now: {len(cache)}")

if __name__ == "__main__":
    # repos from a file (one per line, or tab-sep with repo in col 1)
    repos = []
    for line in open(os.path.join(SRCDIR, sys.argv[1] if len(sys.argv)>1 else "second_pass_repos.txt")):
        rp = line.split("\t")[0].strip()
        if rp and "/" in rp:
            repos.append(rp)
    repos = list(dict.fromkeys(repos))  # dedupe preserve order
    enrich_list(repos)
