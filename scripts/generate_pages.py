#!/usr/bin/env python3
"""Convert coding_agent_harnesses.tsv into individual YAML-frontmatter Markdown files for Eleventy."""
import os, csv, re, json

SRCDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV = os.path.join(SRCDIR, "coding_agent_harnesses.tsv")
AGENTS_DIR = os.path.join(SRCDIR, "agents")
DATA_DIR = os.path.join(SRCDIR, "_data")

def slugify(name):
    slug = name.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_-]+', '-', slug)
    slug = slug.strip('-')
    return slug or "unnamed"

def yaml_escape(s):
    if s is None:
        return "null"
    s = str(s).replace('"', '\\"')
    return f'"{s}"'

def main():
    os.makedirs(AGENTS_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)
    
    rows = list(csv.DictReader(open(TSV, encoding="utf-8"), delimiter="\t"))
    print(f"Read {len(rows)} entries from TSV")
    
    used_slugs = {}
    agents_data = []
    
    for r in rows:
        name = r.get("name", "").strip()
        slug = slugify(name)
        
        if slug in used_slugs:
            used_slugs[slug] += 1
            slug = f"{slug}-{used_slugs[slug]}"
        else:
            used_slugs[slug] = 1
        
        platforms = [p.strip() for p in (r.get("platforms", "") or "").split(";") if p.strip()]
        sources = [s.strip() for s in (r.get("source_list", "") or "").split(",") if s.strip()]
        
        # Build frontmatter manually (no PyYAML dependency)
        fm_lines = ["---"]
        fm_lines.append(f"name: {yaml_escape(name)}")
        fm_lines.append(f"slug: {yaml_escape(slug)}")
        fm_lines.append(f"maker: {yaml_escape(r.get('maker','').strip() or None)}")
        fm_lines.append(f"license: {yaml_escape(r.get('license','').strip() or None)}")
        fm_lines.append(f"url: {yaml_escape(r.get('url','').strip() or None)}")
        fm_lines.append(f"source_code_url: {yaml_escape(r.get('source_code_url','').strip() or None)}")
        fm_lines.append(f"source_available: {yaml_escape(r.get('source_available','').strip() or None)}")
        if platforms:
            fm_lines.append("platforms:")
            for p in platforms:
                fm_lines.append(f"  - {yaml_escape(p)}")
        else:
            fm_lines.append("platforms: []")
        fm_lines.append(f"first_released: {yaml_escape(r.get('first_released','').strip() or None)}")
        fm_lines.append(f"current_release: {yaml_escape(r.get('current_release','').strip() or None)}")
        stars = r.get("stars","").strip()
        fm_lines.append(f"stars: {int(stars) if stars.isdigit() else 'null'}")
        fm_lines.append(f"language: {yaml_escape(r.get('language','').strip() or None)}")
        fm_lines.append(f"homepage: {yaml_escape(r.get('homepage','').strip() or None)}")
        if sources:
            fm_lines.append("sources:")
            for s in sources:
                fm_lines.append(f"  - {yaml_escape(s)}")
        else:
            fm_lines.append("sources: []")
        fm_lines.append("---")
        
        description = r.get("what_makes_it_special", "").strip() or "No description available."
        
        md_path = os.path.join(AGENTS_DIR, f"{slug}.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("\n".join(fm_lines) + "\n\n" + description + "\n")
        
        agents_data.append({
            "name": name,
            "slug": slug,
            "maker": r.get("maker","").strip() or None,
            "license": r.get("license","").strip() or None,
            "url": r.get("url","").strip() or None,
            "source_code_url": r.get("source_code_url","").strip() or None,
            "platforms": platforms,
            "stars": int(stars) if stars.isdigit() else None,
            "first_released": r.get("first_released","").strip() or None,
            "language": r.get("language","").strip() or None,
            "description": description[:200],
        })
    
    with open(os.path.join(DATA_DIR, "agents.json"), "w", encoding="utf-8") as f:
        json.dump(agents_data, f, ensure_ascii=False, indent=2)
    
    print(f"Generated {len(agents_data)} agent pages in {AGENTS_DIR}/")
    print(f"Generated search index: {os.path.join(DATA_DIR, 'agents.json')}")

if __name__ == "__main__":
    main()
