#!/usr/bin/env python3
"""Add third_pass_repos.txt entries into merged.tsv as new candidates."""
import os, csv

SRCDIR = os.path.dirname(os.path.abspath(__file__))
merged = os.path.join(SRCDIR, "merged.tsv")
existing_repos = set()
rows = list(csv.DictReader(open(merged), delimiter="\t"))
for r in rows:
    rp = r.get("github_repo","").strip().lower()
    if rp: existing_repos.add(rp)

added = 0
with open(merged, "a") as f:
    for line in open(os.path.join(SRCDIR,"third_pass_repos.txt")):
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 3: continue
        repo, stars, desc = parts[0], parts[1], parts[2]
        if repo.lower() in existing_repos: continue
        existing_repos.add(repo.lower())
        name = repo.split("/")[-1]
        url = f"https://github.com/{repo}"
        f.write("\t".join([name,url,repo,"","",stars,desc,"","","github_topic2"])+"\n")
        added += 1
print(f"Added {added} new entries to merged.tsv")
