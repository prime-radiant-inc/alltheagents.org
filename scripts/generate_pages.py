#!/usr/bin/env python3
"""Convert coding_agent_harnesses.tsv into individual YAML-frontmatter Markdown files for Eleventy."""
import os, csv, re, json, sys

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
    
    overrides_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "slug_overrides.json")
    slug_overrides = {}
    if os.path.exists(overrides_path):
        with open(overrides_path, encoding="utf-8") as f:
            slug_overrides = json.load(f)
        print(f"Loaded {len(slug_overrides)} slug overrides")
    
    field_overrides_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "field_overrides.json")
    field_overrides = {}
    if os.path.exists(field_overrides_path):
        with open(field_overrides_path, encoding="utf-8") as f:
            field_overrides = json.load(f)
        print(f"Loaded {len(field_overrides)} field overrides")
    
    source_urls_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source_urls.json")
    source_urls = {}
    if os.path.exists(source_urls_path):
        with open(source_urls_path, encoding="utf-8") as f:
            source_urls = json.load(f)
        print(f"Loaded {len(source_urls)} source URLs")
    
    multiplexer_slugs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "multiplexer_slugs.json")
    multiplexer_slugs = set()
    if os.path.exists(multiplexer_slugs_path):
        with open(multiplexer_slugs_path, encoding="utf-8") as f:
            multiplexer_slugs = set(json.load(f))
        print(f"Loaded {len(multiplexer_slugs)} multiplexer slugs")
    
    rows = list(csv.DictReader(open(TSV, encoding="utf-8"), delimiter="\t"))
    print(f"Read {len(rows)} entries from TSV")
    
    used_slugs = {}
    agents_data = []
    
    for row_num, r in enumerate(rows, start=2):
        name = r.get("name", "").strip()
        url = r.get("url", "").strip()
        slug = slug_overrides.get(name) or slug_overrides.get(url) or slugify(name)
        
        if slug in used_slugs:
            prev = used_slugs[slug]
            print(f"\nFATAL: Slug collision on '{slug}'")
            print(f"  First  (line {prev[3]}): {prev[0]} by {prev[1]} — {prev[2]}")
            print(f"  Second (line {row_num}): {name} by {r.get('maker','').strip()} — {r.get('url','').strip()}")
            print(f"\nAdd manual slug overrides in scripts/slug_overrides.json to resolve.")
            sys.exit(1)
        else:
            used_slugs[slug] = (name, r.get("maker", "").strip(), r.get("url", "").strip(), row_num)
        
        platforms = [p.strip() for p in (r.get("platforms", "") or "").split(";") if p.strip()]
        sources = list(dict.fromkeys(s.strip() for s in (r.get("source_list", "") or "").split(",") if s.strip()))
        
        if url in field_overrides:
            for field, value in field_overrides[url].items():
                if value is None:
                    r[field] = ""
                    print(f"  Override: cleared '{field}' for {name} ({url})")
                else:
                    r[field] = str(value)
                    print(f"  Override: set '{field}' to '{value}' for {name} ({url})")
        
        category = "multiplexer" if slug in multiplexer_slugs else "agent"
        
        # Build frontmatter
        fm_lines = ["---"]
        fm_lines.append(f"name: {yaml_escape(name)}")
        fm_lines.append(f"slug: {yaml_escape(slug)}")
        fm_lines.append("layout: agent.njk")
        fm_lines.append(f"category: {category}")
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
        # New enrichment fields (empty until enriched)
        fm_lines.append(f"mcp_support: null")
        fm_lines.append(f"plugin_support: null")
        fm_lines.append(f"claude_code_plugin: null")
        fm_lines.append(f"subagents: null")
        fm_lines.append(f"hooks: null")
        fm_lines.append(f"plan_mode: null")
        fm_lines.append(f"model_providers: null")
        fm_lines.append(f"pricing: null")
        fm_lines.append(f"install_method: null")
        fm_lines.append(f"docs_url: null")
        fm_lines.append(f"plugin_docs_url: null")
        fm_lines.append(f"config_docs_url: null")
        fm_lines.append(f"download_url: null")
        fm_lines.append(f"maintained: null")
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
            "category": category,
            "maker": r.get("maker","").strip() or None,
            "license": r.get("license","").strip() or None,
            "url": r.get("url","").strip() or None,
            "source_code_url": r.get("source_code_url","").strip() or None,
            "platforms": platforms,
            "stars": int(stars) if stars.isdigit() else None,
            "first_released": r.get("first_released","").strip() or None,
            "language": r.get("language","").strip() or None,
            "description": description[:200],
            "sources": sources,
            "source_urls": {s: source_urls.get(s) for s in sources if s in source_urls},
        })
    
    # The search index is built by Eleventy from agents/*.md (agents-index.json.njk);
    # nothing is written to _data/agents.json any more.

if __name__ == "__main__":
    main()
