#!/usr/bin/env python3
"""Generate agents.json from enriched .md frontmatter files (not from TSV)."""
import os, json, re, glob

SRCDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTS_DIR = os.path.join(SRCDIR, "agents")
DATA_DIR = os.path.join(SRCDIR, "_data")

def parse_frontmatter(content):
    if not content.startswith("---\n"):
        return {}, content
    end = content.find("\n---", 4)
    if end == -1:
        return {}, content
    fm_text = content[4:end]
    body = content[end + 4:].lstrip("\n")
    fm = {}
    current_key = None
    current_list = None
    for line in fm_text.strip().split("\n"):
        if line.startswith("  - "):
            val = line[4:].strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            if current_list is not None:
                current_list.append(val)
        elif ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val == "[]":
                fm[key] = []
                current_list = None
            elif val == "null":
                fm[key] = None
                current_list = None
            elif val.startswith('"') and val.endswith('"'):
                fm[key] = val[1:-1]
                current_list = None
            else:
                try:
                    fm[key] = int(val)
                except ValueError:
                    fm[key] = val
                current_list = None
            if val == "" or val == "[]":
                if val == "[]":
                    fm[key] = []
                else:
                    fm[key] = []
                    current_list = fm[key]
    return fm, body

# Load source URLs
source_urls_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source_urls.json")
source_urls = {}
if os.path.exists(source_urls_path):
    with open(source_urls_path) as f:
        source_urls = json.load(f)

agents_data = []
for md_path in sorted(glob.glob(os.path.join(AGENTS_DIR, "*.md"))):
    if os.path.basename(md_path) == "_TEMPLATE.md":
        continue

    with open(md_path, encoding="utf-8") as f:
        content = f.read()
    fm, body = parse_frontmatter(content)
    if not fm.get("name") or not fm.get("slug"):
        raise ValueError(f"Missing required search fields in {md_path}")

    sources = fm.get("sources", []) or []
    agents_data.append({
        "name": fm.get("name"),
        "slug": fm.get("slug"),
        "category": fm.get("category", "agent"),
        "maker": fm.get("maker"),
        "license": fm.get("license"),
        "url": fm.get("url"),
        "source_code_url": fm.get("source_code_url"),
        "source_available": fm.get("source_available"),
        "platforms": fm.get("platforms", []),
        "first_released": fm.get("first_released"),
        "current_release": fm.get("current_release"),
        "stars": fm.get("stars"),
        "language": fm.get("language"),
        "homepage": fm.get("homepage"),
        "description": body.strip()[:200],
        "mcp_support": fm.get("mcp_support"),
        "plugin_support": fm.get("plugin_support"),
        "claude_code_plugin": fm.get("claude_code_plugin"),
        "subagents": fm.get("subagents"),
        "hooks": fm.get("hooks"),
        "plan_mode": fm.get("plan_mode"),
        "model_providers": fm.get("model_providers"),
        "pricing": fm.get("pricing"),
        "install_method": fm.get("install_method"),
        "docs_url": fm.get("docs_url"),
        "plugin_docs_url": fm.get("plugin_docs_url"),
        "config_docs_url": fm.get("config_docs_url"),
        "download_url": fm.get("download_url"),
        "maintained": fm.get("maintained"),
        "sources": sources,
        "source_urls": {s: source_urls.get(s) for s in sources if s in source_urls},
    })

with open(os.path.join(DATA_DIR, "agents.json"), "w", encoding="utf-8") as f:
    json.dump(agents_data, f, ensure_ascii=False, indent=2)

print(f"Generated {len(agents_data)} entries in agents.json from .md files")
