#!/usr/bin/env python3
"""Merge manual additions and commercial research into the final table."""
import os, csv, re

SRCDIR = os.path.dirname(os.path.abspath(__file__))
FINAL = os.path.join(SRCDIR, "..", "coding_agent_harnesses.tsv")

def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()

def main():
    rows = list(csv.DictReader(open(FINAL), delimiter="\t"))
    cols = list(rows[0].keys()) if rows else []
    print(f"Current table: {len(rows)} entries")
    
    # Load manual additions
    manual_path = os.path.join(SRCDIR, "manual_additions.tsv")
    if os.path.exists(manual_path):
        manual = list(csv.DictReader(open(manual_path), delimiter="\t"))
        existing_names = {r["name"].lower() for r in rows}
        added = 0
        for m in manual:
            # normalize to match existing columns
            row = {c: "" for c in cols}
            row.update({
                "name": m.get("name",""),
                "maker": m.get("maker",""),
                "license": m.get("license",""),
                "url": m.get("url",""),
                "source_code_url": m.get("source_code_url",""),
                "what_makes_it_special": m.get("what_makes_it_special",""),
                "platforms": m.get("platforms",""),
                "first_released": m.get("first_released",""),
                "current_release": m.get("current_release",""),
                "stars": "",
                "language": "",
                "homepage": "",
                "source_list": "manual_research",
            })
            # set source_available
            if m.get("source_code_url"):
                row["source_available"] = "Yes"
            else:
                row["source_available"] = "No (proprietary)"
            if m["name"].lower() not in existing_names:
                rows.append(row)
                existing_names.add(m["name"].lower())
                added += 1
        print(f"Added {added} manual additions")
    
    # Load commercial research (if exists)
    comm_path = os.path.join(SRCDIR, "commercial_research.tsv")
    if os.path.exists(comm_path) and os.path.getsize(comm_path) > 0:
        comm = list(csv.DictReader(open(comm_path), delimiter="\t"))
        existing_names = {r["name"].lower() for r in rows}
        added = 0
        updated = 0
        for c in comm:
            # Try to match to existing entry by name
            name_lower = c.get("name","").lower()
            # Handle name variants
            name_variants = {
                "cody": "cody (sourcegraph)",
                "cody by sourcegraph": "cody (sourcegraph)",
                "cursor": "cursor",
                "windsurf (devin desktop)": "windsurf",
                "v0": "v0 (vercel)",
                "v0 by vercel": "v0 (vercel)",
                "amp": "amp",
                "amp (sourcegraph)": "amp",
                "junie": "junie cli",
                "replit agent": "replit agent",
                "lovable": "lovable",
                "antigravity cli": "antigravity cli",
            }
            target_name = name_variants.get(name_lower, name_lower)
            
            # Find matching existing entry
            found = False
            for r in rows:
                if r["name"].lower() == target_name or r["name"].lower() == name_lower:
                    # Update metadata
                    if c.get("maker") and not r.get("maker"):
                        r["maker"] = c["maker"]
                    elif c.get("maker"):
                        r["maker"] = c["maker"]  # prefer commercial research (more accurate)
                    if c.get("license") and c.get("license") != "Proprietary":
                        r["license"] = c["license"]
                    elif c.get("license"):
                        r["license"] = c["license"]
                    if c.get("source_code_url"):
                        r["source_code_url"] = c["source_code_url"]
                        r["source_available"] = "Yes"
                    elif c.get("license") == "Proprietary":
                        r["source_available"] = "No (proprietary)"
                    if c.get("what_makes_it_special") and len(c["what_makes_it_special"]) > len(r.get("what_makes_it_special","")):
                        r["what_makes_it_special"] = c["what_makes_it_special"]
                    if c.get("platforms"):
                        r["platforms"] = c["platforms"]
                    if c.get("first_released"):
                        r["first_released"] = c["first_released"]
                    if c.get("current_release"):
                        r["current_release"] = c["current_release"]
                    found = True
                    updated += 1
                    break
            
            if not found:
                # Add as new entry
                row = {col: "" for col in cols}
                row.update({
                    "name": c.get("name",""),
                    "maker": c.get("maker",""),
                    "license": c.get("license",""),
                    "url": c.get("url",""),
                    "source_code_url": c.get("source_code_url",""),
                    "what_makes_it_special": c.get("what_makes_it_special",""),
                    "platforms": c.get("platforms",""),
                    "first_released": c.get("first_released",""),
                    "current_release": c.get("current_release",""),
                    "stars": "",
                    "language": "",
                    "homepage": "",
                    "source_list": "commercial_research",
                })
                if c.get("source_code_url"):
                    row["source_available"] = "Yes"
                else:
                    row["source_available"] = "No (proprietary)"
                if row["name"].lower() not in existing_names:
                    rows.append(row)
                    existing_names.add(row["name"].lower())
                    added += 1
        print(f"Commercial research: added {added}, updated {updated}")
    else:
        print("No commercial_research.tsv found (delegate still running)")
    
    # Sort by stars desc
    def star_val(r):
        try: return int(r.get("stars","0") or 0)
        except: return 0
    rows.sort(key=star_val, reverse=True)
    
    with open(FINAL, "w") as f:
        f.write("\t".join(cols)+"\n")
        for r in rows:
            f.write("\t".join(str(r.get(c,"")).replace("\t"," ").replace("\n"," ") for c in cols)+"\n")
    print(f"Wrote {FINAL} with {len(rows)} entries")

if __name__ == "__main__":
    main()
