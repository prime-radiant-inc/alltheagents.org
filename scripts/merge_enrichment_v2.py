#!/usr/bin/env python3
"""Merge enrichment JSONs (census-work/enrichment/batch_*.json) into agents/*.md.

Extends scripts/merge_enrichment.py: also applies `category` and swaps the body
for the new `narrative` (replacing the duplicated what_makes_it_special body).
Only fills null frontmatter fields; never overwrites non-null values except
category (census-wide reclassification) and the body.
"""
import os, json, re, sys, glob

SRCDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTS_DIR = os.path.join(SRCDIR, "agents")
WORK = os.environ.get("CENSUS_WORK", "/Users/jesse/git/prime-radiant/census-work")

# Fields the enrichment JSON may carry that map to frontmatter keys
MERGE_FIELDS = [
    "mcp_support", "plugin_support", "claude_code_plugin",
    "subagents", "hooks", "plan_mode", "model_providers",
    "pricing", "install_method", "docs_url",
    "plugin_docs_url", "config_docs_url", "download_url", "maintained",
    "license", "source_available", "language", "homepage",
    "first_released", "current_release", "source_code_url",
    "what_makes_it_special",
]

def parse_frontmatter(content):
    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValueError("no frontmatter")
    fm_text = parts[1]
    body = parts[2].lstrip("\n")
    fm = {}
    current_key = None
    current_list = None
    in_comment = False
    for line in fm_text.strip().split("\n"):
        if line.startswith("  - ") and current_list is not None:
            val = line[4:].strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            current_list.append(val)
            continue
        current_list = None
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            # strip trailing comments (template uses inline # comments)
            if " #" in val:
                val = val.split(" #")[0]
            val = val.strip()
            if val == "[]":
                fm[key] = []
            elif val == "":
                fm[key] = []
                current_list = fm[key]
            elif val == "null":
                fm[key] = None
            elif val.startswith('"') and val.endswith('"'):
                fm[key] = val[1:-1]
            else:
                fm[key] = val
    return fm, parts[2].lstrip("\n")

def yaml_escape(s):
    s = str(s).replace('"', '\\"')
    return f'"{s}"'

def write_frontmatter(fm, body):
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
    return "\n".join(lines) + "\n\n" + body.strip() + "\n"

def main():
    batch_files = sorted(glob.glob(os.path.join(WORK, "enrichment", "batch_*.json")))
    print(f"Merging {len(batch_files)} enrichment batches")
    updated = 0
    skipped = 0
    for bf in sorted(batch_files):
        with open(bf, encoding="utf-8") as f:
            entries = json.load(f)
        for entry in entries:
            slug = entry.get("slug")
            if not slug:
                continue
            md_path = os.path.join(AGENTS_DIR, f"{slug}.md")
            if not os.path.exists(md_path):
                print(f"  WARNING: {slug}.md not found, skipping")
                skipped += 1
                continue
            with open(md_path, encoding="utf-8") as f:
                content = f.read()
            fm, _body = parse_frontmatter(content)
            changed = False
            # category: enrichment is authoritative
            if entry.get("category") in ("agent", "multiplexer", "other"):
                if fm.get("category") != entry["category"]:
                    fm["category"] = entry["category"]
                    changed = True
            # enrichment fields: only fill nulls
            for field in MERGE_FIELDS:
                if field in entry and entry[field] is not None and entry[field] != "":
                    old = fm.get(field)
                    if old is None or old == [] or old == "":
                        fm[field] = entry[field]
                        changed = True
            # narrative body
            narrative = entry.get("narrative")
            if narrative and narrative.strip():
                body_new = narrative.strip()
                if _body.strip() != body_new if False else True:
                    pass
            # recompute with narrative
            if narrative:
                new_content = write_frontmatter(fm, narrative.strip())
                if new_content != content:
                    with open(md_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    updated += 1
            elif changed:
                new_content = write_frontmatter(fm, _body)
                if new_content != content:
                    with open(md_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    updated += 1
    print(f"Updated {updated} files, skipped {skipped}")

if __name__ == "__main__":
    main()
