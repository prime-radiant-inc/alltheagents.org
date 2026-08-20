#!/usr/bin/env python3
"""Enrich GitHub-hosted coding agent candidates via gh api. Resumable via cache."""
import os, re, csv, json, subprocess, time, sys

SRCDIR = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(SRCDIR, "gh_cache.json")
OUT = os.path.join(SRCDIR, "enriched_github.tsv")

def load_cache():
    if os.path.exists(CACHE):
        return json.load(open(CACHE))
    return {}

def save_cache(cache):
    with open(CACHE, "w") as f:
        json.dump(cache, f)

def gh_api(repo):
    """Fetch repo metadata via gh api. Returns dict or None."""
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

def main():
    cache = load_cache()
    # Read candidates
    rows = list(csv.DictReader(open(os.path.join(SRCDIR,"coding_candidates.tsv")), delimiter="\t"))
    repos = []
    seen = set()
    for r in rows:
        rp = r.get("github_repo","").strip()
        if rp and rp.lower() not in seen:
            seen.add(rp.lower())
            repos.append((rp, r.get("name",""), r.get("url","")))
    print(f"Unique GitHub repos to enrich: {len(repos)}; cached: {len(cache)}")
    todo = [(rp,n,u) for (rp,n,u) in repos if rp.lower() not in cache]
    print(f"To fetch: {len(todo)}")
    for i, (repo, name, url) in enumerate(todo):
        if i % 50 == 0:
            print(f"  {i}/{len(todo)} ... {repo}", flush=True)
        data = gh_api(repo)
        cache[repo.lower()] = data
        if i % 25 == 0:
            save_cache(cache)
    save_cache(cache)
    print(f"Cache now: {len(cache)} entries")
    # Write enriched TSV
    cols = ["github_repo","name","url","license","maker","owner_type","description","language",
            "stars","homepage","created_at","pushed_at","archived","topics","error"]
    with open(OUT, "w") as f:
        f.write("\t".join(cols)+"\n")
        for repo, name, url in repos:
            d = cache.get(repo.lower(), {})
            row = [repo, name, url,
                   d.get("license",""), d.get("owner",""), d.get("owner_type",""),
                   (d.get("description") or "").replace("\t"," ").replace("\n"," "),
                   d.get("language",""), str(d.get("stargazers_count","")),
                   d.get("homepage","") or "", d.get("created_at",""), d.get("pushed_at",""),
                   str(d.get("archived","")), ";".join(d.get("topics",[])),
                   d.get("error","")]
            f.write("\t".join(str(x) for x in row)+"\n")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
