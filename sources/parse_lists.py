#!/usr/bin/env python3
"""Parse awesome-list markdown files into a unified TSV of candidate coding agent harnesses."""
import os, re, sys, json, html

SOURCES = {
    "e2b": "e2b-awesome-ai-agents.md",
    "brad": "brad-cli-coding-agents.md",
    "jim": "jim-ai-agents.md",
    "slava": "slava-ai-agents.md",
    "caramaschi": "caramaschi-2026.md",
}

def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()

def parse_e2b(text):
    """e2b format: ## [Name](URL)\nOne-line desc\n<details> ... ### Category ... ### Description ... ### Links ..."""
    entries = []
    # Split on top-level ## headers that contain a link
    pat = re.compile(r"^##\s+\[([^\]]+)\]\(([^)]+)\)\s*$", re.MULTILINE)
    matches = list(pat.finditer(text))
    for i, m in enumerate(matches):
        name = clean(m.group(1))
        url = clean(m.group(2))
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        block = text[start:end]
        # first non-empty line after header = short desc
        lines = [l for l in block.splitlines()]
        short = ""
        for l in lines:
            if l.strip() and not l.strip().startswith("<") and not l.strip().startswith("!["):
                short = clean(l)
                break
        # category
        cat = ""
        cm = re.search(r"###\s+Category\s*\n(.+?)(?=###|\Z)", block, re.S)
        if cm:
            cat = clean(cm.group(1))
        # description bullets
        desc = ""
        dm = re.search(r"###\s+Description\s*\n(.+?)(?=###|\Z)", block, re.S)
        if dm:
            desc = clean(dm.group(1))
        entries.append({
            "name": name, "url": url, "short": short,
            "category": cat, "desc": desc or short,
        })
    return entries

def parse_markdown_links(text):
    """Generic: pull all [Name](url) markdown links with surrounding context line."""
    entries = []
    seen = set()
    for line in text.splitlines():
        for m in re.finditer(r"\[([^\]]+)\]\((https?://[^)]+)\)", line):
            name = clean(m.group(1))
            url = clean(m.group(2))
            if url in seen:
                continue
            seen.add(url)
            entries.append({"name": name, "url": url, "short": clean(line), "category": "", "desc": ""})
    return entries

def main():
    alldir = os.path.dirname(os.path.abspath(__file__))
    all_entries = []
    for key, fn in SOURCES.items():
        path = os.path.join(alldir, fn)
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            continue
        text = open(path, encoding="utf-8", errors="replace").read()
        if key == "e2b":
            ents = parse_e2b(text)
        else:
            ents = parse_markdown_links(text)
        for e in ents:
            e["source_list"] = key
            all_entries.append(e)
    # Dedupe by URL (case-insensitive); entries without URL dedupe by name
    by_url = {}
    name_only = {}
    for e in all_entries:
        u = e["url"].lower().rstrip("/")
        if u:
            if u not in by_url:
                by_url[u] = e
        else:
            n = e["name"].lower()
            if n not in name_only:
                name_only[n] = e
    merged = list(by_url.values()) + list(name_only.values())
    # write TSV
    out = os.path.join(alldir, "all_candidates.tsv")
    cols = ["name","url","short","category","desc","source_list"]
    with open(out, "w", encoding="utf-8") as f:
        f.write("\t".join(cols)+"\n")
        for e in merged:
            f.write("\t".join(e.get(c,"").replace("\t"," ").replace("\n"," ") for c in cols)+"\n")
    print(f"Total raw entries: {len(all_entries)}; unique: {len(merged)}")
    print(f"Wrote {out}")
    # also print category breakdown for e2b
    cats = {}
    for e in merged:
        c = e.get("category","")
        cats[c] = cats.get(c,0)+1
    print("Top categories:")
    for c,n in sorted(cats.items(), key=lambda x:-x[1])[:20]:
        print(f"  {n:4d}  {c[:70]}")

if __name__ == "__main__":
    main()
