#!/usr/bin/env python3
"""Merge enrichment results from subagent JSON files into agent .md files."""
import os, json, re, sys, glob

SRCDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTS_DIR = os.path.join(SRCDIR, "agents")

ENRICHMENT_FIELDS = [
    "mcp_support", "plugin_support", "claude_code_plugin",
    "subagents", "hooks", "plan_mode", "model_providers",
    "pricing", "install_method", "docs_url",
    "plugin_docs_url", "config_docs_url", "download_url", "maintained",
    # Also allow corrections to existing fields
    "license", "source_available", "language", "what_makes_it_special",
]

def yaml_escape(s):
    if s is None:
        return "null"
    s = str(s).replace('"', '\\"')
    return f'"{s}"'

def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    fm_text = parts[1]
    body = parts[2].lstrip("\n")
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
                fm[key] = val
                current_list = None
            # Check if next lines are list items
            if val == "":
                fm[key] = []
                current_list = fm[key]
    return fm, body

def write_frontmatter(fm, body):
    """Write YAML frontmatter + body to markdown."""
    lines = ["---"]
    for key, val in fm.items():
        if isinstance(val, list):
            if not val:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                for item in val:
                    lines.append(f"  - {yaml_escape(item)}")
        elif val is None:
            lines.append(f"{key}: null")
        elif isinstance(val, (int, float)):
            lines.append(f"{key}: {val}")
        else:
            lines.append(f"{key}: {yaml_escape(val)}")
    lines.append("---")
    return "\n".join(lines) + "\n\n" + body + "\n"

def merge_file(enrichment_file):
    """Merge a single enrichment JSON file into .md files."""
    with open(enrichment_file) as f:
        entries = json.load(f)
    
    updated = 0
    for entry in entries:
        slug = entry.get("slug")
        if not slug:
            continue
        
        md_path = os.path.join(AGENTS_DIR, f"{slug}.md")
        if not os.path.exists(md_path):
            print(f"  WARNING: {slug}.md not found, skipping")
            continue
        
        with open(md_path, encoding="utf-8") as f:
            content = f.read()
        
        fm, body = parse_frontmatter(content)
        
        changed = False
        for field in ENRICHMENT_FIELDS:
            if field in entry and entry[field] is not None:
                old_val = fm.get(field)
                new_val = entry[field]
                if old_val != new_val:
                    fm[field] = new_val
                    changed = True
        
        if "what_makes_it_special" in entry and entry["what_makes_it_special"]:
            new_desc = entry["what_makes_it_special"]
            if body.strip() != new_desc.strip():
                body = new_desc
                changed = True
        
        if changed:
            new_content = write_frontmatter(fm, body)
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated += 1
    
    print(f"  Merged {updated}/{len(entries)} entries from {enrichment_file}")
    return updated

if __name__ == "__main__":
    enrichment_dir = os.path.join(SRCDIR, "sources", "enrichment_results")
    if len(sys.argv) > 1:
        # Merge specific files
        files = sys.argv[1:]
    else:
        # Merge all JSON files in enrichment_results
        files = sorted(glob.glob(os.path.join(enrichment_dir, "*.json")))
    
    total = 0
    for f in files:
        total += merge_file(f)
    print(f"\nTotal entries updated: {total}")
