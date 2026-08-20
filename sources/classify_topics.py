#!/usr/bin/env python3
"""Classify new topic repos: keep genuine coding-agent harnesses, drop ancillary tools."""
import os, csv, re

SRCDIR = os.path.dirname(os.path.abspath(__file__))

# Load topic repo descriptions
repo_desc = {}
import glob
for f in glob.glob(os.path.join(SRCDIR, "topics", "*.tsv")):
    for line in open(f, encoding="utf-8", errors="replace"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) >= 3:
            repo, stars, desc = parts[0], parts[1], parts[2]
            repo_desc.setdefault(repo.lower(), (repo, stars, desc))

new_repos = [l.strip() for l in open(os.path.join(SRCDIR, "new_topic_repos.txt")) if l.strip()]
print(f"New topic repos: {len(new_repos)}")

# Exclude keywords: ancillary tools, not harnesses themselves
EXCLUDE = ["skill","prompt","system-prompt","mcp server","mcp-server","model context protocol",
           "book","tutorial","guide","course","awesome","collection","directory","template",
           "marketing","seo","copywriting","slide","video production","design.md","design system",
           "knowledge graph","knowledge-graph","calendar","cheatsheet","cheat sheet","playlist",
           "docker","kubernetes","ansible","terraform","monitoring","observability","dashboard",
           "chatgpt clone","chat ui","chatbot framework","telegram","discord bot","slack bot",
           "raspberry pi","arduino","robot","home automation","iot","game agent","trading",
           "cybersecurity","security skill","penetration","hack","ctf","medical","healthcare",
           "legal","finance","crm","sales","hr","resume","recipe","travel","weather"]
# Include keywords: indicates a coding agent / harness
INCLUDE_STRONG = ["coding agent","code agent","coding harness","agent harness","pair programmer",
                  "pair programming","software engineer","software engineering","code editor",
                  "code generation","codegen","swe agent","swe-agent","dev agent","developer agent",
                  "autonomous agent","autonomous coding","autonomous software","terminal agent",
                  "cli agent","cli coding","ide agent","agentic ide","agent ide","code assistant",
                  "coding assistant","ai coding","ai pair","ai developer","ai engineer",
                  "autonomous dev","autonomous engineer","repo agent","codebase agent",
                  "agent framework","multi-agent","agent platform","agent os","agent runtime"]

def classify(repo, stars, desc):
    d = (desc or "").lower()
    n = repo.lower()
    # exclude ancillary
    for ex in EXCLUDE:
        if ex in d or ex in n:
            return ("exclude", ex)
    # strong include
    for inc in INCLUDE_STRONG:
        if inc in d or inc in n:
            return ("include", inc)
    # also include if name has 'code'/'coding'/'dev'/'agent' AND desc mentions code/edit/file/repo
    if any(w in n for w in ["code","coding","dev-agent","devagent","swe"]):
        if any(w in d for w in ["code","edit","file","repo","program","build","terminal","cli","test","debug","compile","prompt","llm","gpt","agent"]):
            return ("include", "name+desc")
    return ("maybe", "")

keep, exclude, maybe = [], [], []
for rp in new_repos:
    repo, stars, desc = repo_desc.get(rp.lower(), (rp, "0", ""))
    verdict, why = classify(repo, stars, desc)
    if verdict == "include":
        keep.append((repo, stars, desc, why))
    elif verdict == "exclude":
        exclude.append((repo, stars, desc, why))
    else:
        maybe.append((repo, stars, desc, why))

print(f"Include: {len(keep)}; Exclude: {len(exclude)}; Maybe: {len(maybe)}")
print("\n=== INCLUDE (top by stars) ===")
for r,s,d,w in sorted(keep, key=lambda x:-int(x[1]) if x[1].isdigit() else 0)[:50]:
    print(f"  {r:40s} {s:>7s}  [{w}]  {d[:60]}")
print("\n=== MAYBE (top by stars) ===")
for r,s,d,w in sorted(maybe, key=lambda x:-int(x[1]) if x[1].isdigit() else 0)[:30]:
    print(f"  {r:40s} {s:>7s}  {d[:60]}")
print("\n=== EXCLUDE (sample) ===")
for r,s,d,w in sorted(exclude, key=lambda x:-int(x[1]) if x[1].isdigit() else 0)[:15]:
    print(f"  {r:40s} {s:>7s}  [{w}]  {d[:50]}")

# Write keep list for second enrichment pass
with open(os.path.join(SRCDIR, "second_pass_repos.txt"), "w") as f:
    for r,s,d,w in keep:
        f.write(f"{r}\t{s}\t{d}\t{w}\n")
print(f"\nWrote second_pass_repos.txt with {len(keep)} repos")
