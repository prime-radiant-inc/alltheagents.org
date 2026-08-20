#!/usr/bin/env python3
"""Append findings to alternatives_findings.tsv, dedup by url (case-insensitive)."""
import sys
import csv

FINDINGS = "/Users/jesse/agent-survey/sources/alternatives_findings.tsv"

def load_existing():
    seen = set()
    rows = []
    try:
        with open(FINDINGS, encoding="utf-8") as f:
            r = csv.DictReader(f, delimiter="\t")
            for row in r:
                key = (row["name"].strip().lower(), row["url"].strip().lower().rstrip("/"))
                seen.add(key)
                rows.append(row)
    except FileNotFoundError:
        pass
    return seen, rows

def main():
    seen, rows = load_existing()
    added = 0
    for line in sys.stdin:
        line = line.rstrip("\n")
        if not line:
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        name, url, desc = parts[0], parts[1], "\t".join(parts[2:])
        key = (name.strip().lower(), url.strip().lower().rstrip("/"))
        if key in seen:
            continue
        seen.add(key)
        rows.append({"name": name.strip(), "url": url.strip(), "description": desc.strip()})
        added += 1
    with open(FINDINGS, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name", "url", "description"], delimiter="\t")
        w.writeheader()
        for row in rows:
            w.writerow(row)
    print(f"Added {added} new rows; total now {len(rows)}")

if __name__ == "__main__":
    main()
