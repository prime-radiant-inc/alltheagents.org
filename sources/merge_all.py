#!/usr/bin/env python3
"""Merge all awesome-list sources into one unified candidate pool of coding agent harnesses."""
import os, re, csv, json

SRCDIR = os.path.dirname(os.path.abspath(__file__))

def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()

# ---- Parsers per source format ----

def parse_jqueryscript(text):
    """Format: - [Name](url) - **N stars** · `Platform` · `License`. Description."""
    out = []
    for line in text.splitlines():
        m = re.match(r"^- \[([^\]]+)\]\((https?://[^)]+)\) - \*\*([^*]+)stars?\*\* · (.+)$", line)
        if not m:
            continue
        name = clean(m.group(1)); url = clean(m.group(2))
        rest = clean(m.group(4))
        # rest = "`CLI` · `MIT`. Description"  or  "`CLI` · `Web` · `Autonomous` · `MIT`. Description"
        # split license/desc at first ". "
        # platforms are backtick tokens before the period
        desc = ""
        license_ = ""
        platforms = []
        # find the ". " that separates tags from description
        # tags part is everything up to first ". " that follows a backtick token
        parts = rest.split(". ", 1)
        tags = parts[0]
        desc = parts[1] if len(parts) > 1 else ""
        # also handle trailing period in tags
        for tok in re.findall(r"`([^`]+)`", tags):
            if tok.lower() in ("mit","apache-2.0","agpl-3.0","closed source","source available","gpl","bsd","mit license","apache","proprietary","free","commercial","open source"):
                license_ = tok
            else:
                platforms.append(tok)
        # also catch plain license words not in backticks
        if not license_:
            for w in ["MIT","Apache-2.0","AGPL-3.0","Closed Source","Source Available"]:
                if w.lower() in tags.lower():
                    license_ = w
        out.append({"name":name,"url":url,"license":license_,"platforms":";".join(platforms),
                    "stars":clean(m.group(3)),"what_makes_it_special":desc,"source_list":"jqueryscript"})
    return out

def parse_flatlogic(text):
    """Table format: | Name | URL | Platform | Type | Description | Pricing |"""
    out = []
    for line in text.splitlines():
        if not line.startswith("|") or "---" in line or "Name" in line and "URL" in line:
            continue
        cells = [c.strip() for c in line.split("|")]
        cells = [c for c in cells if c != ""]
        if len(cells) < 5:
            continue
        name = clean(cells[0])
        if name in ("Name","") or name.startswith("!["):
            continue
        url = clean(cells[1]) if len(cells)>1 else ""
        platform = clean(cells[2]) if len(cells)>2 else ""
        typ = clean(cells[3]) if len(cells)>3 else ""
        desc = clean(cells[4]) if len(cells)>4 else ""
        pricing = clean(cells[5]) if len(cells)>5 else ""
        out.append({"name":name,"url":url,"license":"","platforms":platform,
                    "stars":"","what_makes_it_special":desc,"source_list":"flatlogic"})
    return out

def parse_e2b(text):
    """## [Name](URL)\nshort desc\n<details> ### Category ### Description ### Links"""
    out = []
    pat = re.compile(r"^##\s+\[([^\]]+)\]\(([^)]+)\)\s*$", re.MULTILINE)
    matches = list(pat.finditer(text))
    for i, m in enumerate(matches):
        name = clean(m.group(1)); url = clean(m.group(2))
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        block = text[start:end]
        short = ""
        for l in block.splitlines():
            if l.strip() and not l.strip().startswith("<") and not l.strip().startswith("!["):
                short = clean(l); break
        cm = re.search(r"###\s+Category\s*\n(.+?)(?=###|\Z)", block, re.S)
        cat = clean(cm.group(1)) if cm else ""
        dm = re.search(r"###\s+Description\s*\n(.+?)(?=###|\Z)", block, re.S)
        desc = clean(dm.group(1)) if dm else short
        # homepage link
        web = ""
        wm = re.search(r"\[Web\]\(([^)]+)\)", block)
        if wm: web = clean(wm.group(1))
        out.append({"name":name,"url":url,"license":"","platforms":"","stars":"",
                    "what_makes_it_special":desc or short,"category":cat,"web":web,"source_list":"e2b"})
    return out

def parse_generic_links(text, source_list):
    """Pull [Name](url) markdown links with line context as description."""
    out = []
    for line in text.splitlines():
        for m in re.finditer(r"\[([^\]]+)\]\((https?://[^)]+)\)", line):
            name = clean(m.group(1)); url = clean(m.group(2))
            if url.endswith((".png",".jpg",".svg",".gif",".webp")):
                continue
            out.append({"name":name,"url":url,"license":"","platforms":"","stars":"",
                        "what_makes_it_special":clean(line),"source_list":source_list})
    return out

def main():
    files = {
        "jqueryscript.md": ("jqueryscript", "special"),
        "flatlogic-dev-agents.md": ("flatlogic", "special"),
        "e2b-awesome-ai-agents.md": ("e2b", "special"),
        "brad-cli-coding-agents.md": ("brad", "generic"),
        "jim-ai-agents.md": ("jim", "generic"),
        "slava-ai-agents.md": ("slava", "generic"),
        "caramaschi-2026.md": ("caramaschi", "generic"),
        "vinkius.md": ("vinkius", "generic"),
        "brandonhimpfen.md": ("brandonhimpfen", "generic"),
        "kzhou.md": ("kzhou", "generic"),
        "zhouhao.md": ("zhouhao", "generic"),
        "namphuong.md": ("namphuong", "generic"),
        "quome.md": ("quome", "generic"),
        "ishandutta.md": ("ishandutta", "generic"),
        "tiennm.md": ("tiennm", "generic"),
    }
    all_entries = []
    for fn, (src, kind) in files.items():
        path = os.path.join(SRCDIR, fn)
        if not os.path.exists(path) or os.path.getsize(path)==0:
            continue
        text = open(path, encoding="utf-8", errors="replace").read()
        if kind == "special":
            if src == "jqueryscript":
                ents = parse_jqueryscript(text)
            elif src == "flatlogic":
                ents = parse_flatlogic(text)
            elif src == "e2b":
                ents = parse_e2b(text)
            else:
                ents = parse_generic_links(text, src)
        else:
            ents = parse_generic_links(text, src)
        all_entries.extend(ents)
        print(f"{src:14s}: {len(ents):5d} entries")

    # Dedupe by GitHub repo full_name or URL root
    def repo_key(url):
        m = re.match(r"https?://github\.com/([^/]+/[^/#?]+)", url)
        if m:
            return ("gh", m.group(1).lower())
        return ("url", url.lower().rstrip("/").split("?")[0])

    seen = {}
    merged = []
    for e in all_entries:
        k = repo_key(e["url"])
        if k in seen:
            # merge: fill missing fields from existing
            ex = seen[k]
            for f in ["license","platforms","what_makes_it_special","stars","category","web"]:
                if not ex.get(f) and e.get(f):
                    ex[f] = e[f]
            ex["source_list"] = ex.get("source_list","") + "," + e.get("source_list","")
            continue
        seen[k] = e
        merged.append(e)
    print(f"\nMerged unique: {len(merged)}")

    # Extract GitHub owner/repo for enrichment
    for e in merged:
        m = re.match(r"https?://github\.com/([^/]+/[^/#?]+)", e["url"])
        e["github_repo"] = m.group(1) if m else ""

    # Write merged TSV
    cols = ["name","url","github_repo","license","platforms","stars","what_makes_it_special","category","web","source_list"]
    out = os.path.join(SRCDIR, "merged.tsv")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\t".join(cols)+"\n")
        for e in merged:
            f.write("\t".join(str(e.get(c,"")).replace("\t"," ").replace("\n"," ") for c in cols)+"\n")
    print(f"Wrote {out}")

    # Stats
    gh = [e for e in merged if e["github_repo"]]
    print(f"With GitHub repo: {len(gh)}; without: {len(merged)-len(gh)}")
    # how many already have a license
    withlic = [e for e in merged if e.get("license")]
    print(f"With license already: {len(withlic)}")

if __name__ == "__main__":
    main()
