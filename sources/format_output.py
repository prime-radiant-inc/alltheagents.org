#!/usr/bin/env python3
"""Generate the final formatted deliverable: markdown table and CSV."""
import os, csv, re

SRCDIR = os.path.dirname(os.path.abspath(__file__))
FINAL = os.path.join(SRCDIR, "..", "coding_agent_harnesses.tsv")

def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()

def main():
    rows = list(csv.DictReader(open(FINAL), delimiter="\t"))
    print(f"Total entries: {len(rows)}")
    
    # Write CSV (same as TSV but comma-separated, with proper quoting)
    csv_path = os.path.join(SRCDIR, "..", "coding_agent_harnesses.csv")
    with open(csv_path, "w", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow({k: v for k, v in r.items()})
    print(f"Wrote {csv_path}")
    
    # Write markdown table (first 100 entries for readability)
    md_path = os.path.join(SRCDIR, "..", "coding_agent_harnesses.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# Coding Agent Harnesses — Comprehensive List\n\n")
        f.write(f"**Total entries: {len(rows)}**\n\n")
        f.write(f"This table catalogs coding agent harnesses — systems that let an LLM autonomously write, modify, debug, or run code. Sources: e2b-dev/awesome-ai-agents, jqueryscript/awesome-coding-agent, bradAGI/awesome-cli-coding-agents, flatlogic/awesome-ai-software-development-agents, and GitHub topic searches (coding-agent, ai-coding-agent, code-agent, etc.). GitHub metadata enriched via GitHub API.\n\n")
        
        # Write summary stats
        has_maker = sum(1 for r in rows if r.get('maker'))
        has_lic = sum(1 for r in rows if r.get('license') and r['license'] not in ('','NOASSERTION','None'))
        has_date = sum(1 for r in rows if r.get('first_released'))
        has_stars = sum(1 for r in rows if r.get('stars') and r['stars'] != '0')
        has_src = sum(1 for r in rows if r.get('source_code_url'))
        f.write(f"## Data Completeness\n\n")
        f.write(f"| Field | Filled | Coverage |\n|-------|--------|----------|\n")
        f.write(f"| Name | {len(rows)} | 100% |\n")
        f.write(f"| Maker | {has_maker} | {100*has_maker//len(rows)}% |\n")
        f.write(f"| License | {has_lic} | {100*has_lic//len(rows)}% |\n")
        f.write(f"| URL | {len(rows)} | 100% |\n")
        f.write(f"| Source code URL | {has_src} | {100*has_src//len(rows)}% |\n")
        f.write(f"| First released | {has_date} | {100*has_date//len(rows)}% |\n")
        f.write(f"| Stars | {has_stars} | {100*has_stars//len(rows)}% |\n\n")
        
        # Full table (all entries)
        f.write(f"## Full Table\n\n")
        f.write("| # | Name | Maker | License | URL | Source Code | What Makes It Special | Platforms | First Released | Current Release | Stars |\n")
        f.write("|---|------|-------|---------|-----|-------------|----------------------|-----------|----------------|-----------------|-------|\n")
        for i, r in enumerate(rows, 1):
            name = clean(r.get('name',''))
            maker = clean(r.get('maker',''))
            license_ = clean(r.get('license','')) or '—'
            url = clean(r.get('url',''))
            src = clean(r.get('source_code_url','')) or '—'
            special = clean(r.get('what_makes_it_special',''))[:120]
            platforms = clean(r.get('platforms','')) or '—'
            first = clean(r.get('first_released','')) or '—'
            current = clean(r.get('current_release','')) or '—'
            stars = clean(r.get('stars','')) or '—'
            f.write(f"| {i} | {name} | {maker} | {license_} | {url} | {src} | {special} | {platforms} | {first} | {current} | {stars} |\n")
    print(f"Wrote {md_path}")

if __name__ == "__main__":
    main()
