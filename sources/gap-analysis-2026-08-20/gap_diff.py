#!/usr/bin/env python3
"""Diff discovery candidates (pipe-delimited) against the harness-census baseline TSV.

Usage: python3 gap_diff.py baseline.tsv candidates1.txt [candidates2.txt ...]
Candidate line format: name|maker_or_publisher|url|extra|description|source
Outputs: gap_report.tsv (unmatched candidates) and match_log.tsv (matched, with reason).
"""
import csv
import re
import sys
from difflib import SequenceMatcher
from urllib.parse import urlparse

GENERIC_DOMAINS = {
    "github.com", "gitlab.com", "bitbucket.org", "marketplace.visualstudio.com",
    "open-vsx.org", "plugins.jetbrains.com", "producthunt.com", "ycombinator.com",
    "google.com", "microsoft.com", "amazon.com", "aws.amazon.com", "npmjs.com", "pypi.org",
}

STOP_SUFFIXES = (
    " ai", " agent", " code", " coder", " copilot", " assistant", " cli", " ide",
    " for vs code", " for vscode", " for jetbrains", " plugin", " extension", " beta",
)


def norm_name(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"\(.*?\)", "", s)
    # keep only the product-name part of long marketplace titles
    s = re.split(r"\s*[:,–—]\s+|\s+-\s+|\s+/\s+", s)[0]
    for suf in STOP_SUFFIXES:
        if s.endswith(suf) and len(s) > len(suf) + 2:
            s = s[: -len(suf)]
    return re.sub(r"[^a-z0-9]", "", s)


def domain_of(url: str) -> str | None:
    if not url or not url.strip():
        return None
    u = url.strip()
    if not u.startswith("http"):
        u = "https://" + u
    try:
        host = urlparse(u).netloc.lower().removeprefix("www.")
    except ValueError:
        return None
    return host or None


def repo_slug(url: str) -> str | None:
    m = re.search(r"github\.com/([\w.-]+/[\w.-]+)", url or "", re.I)
    return m.group(1).lower().rstrip("/").removesuffix(".git") if m else None


def load_baseline(path):
    names, domains, slugs, raw_names = set(), set(), set(), []
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            n = (row.get("name") or "").strip()
            if not n:
                continue
            raw_names.append(n)
            names.add(norm_name(n))
            for field in ("url", "source_code_url", "homepage"):
                d = domain_of(row.get(field) or "")
                if d and d not in GENERIC_DOMAINS:
                    domains.add(d)
                s = repo_slug(row.get(field) or "")
                if s:
                    slugs.add(s)
    return names, domains, slugs, raw_names


def main():
    baseline_path, dropped_path, cand_paths = sys.argv[1], sys.argv[2], sys.argv[3:]
    names, domains, slugs, raw_names = load_baseline(baseline_path)
    dnames, ddomains, dslugs, draw = load_baseline(dropped_path)
    norm_to_raw = {norm_name(n): n for n in raw_names}

    seen_cand = set()
    gaps, matches, prev_dropped = [], [], []
    for path in cand_paths:
        with open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line or line.count("|") < 4:
                    continue
                parts = [p.strip() for p in line.split("|")]
                name, maker, url = parts[0], parts[1], parts[2]
                nn = norm_name(name)
                if not nn or nn in seen_cand:
                    continue
                seen_cand.add(nn)

                reason = None
                if nn in names:
                    reason = f"name={norm_to_raw.get(nn, name)}"
                if not reason:
                    s = repo_slug(url)
                    if s and s in slugs:
                        reason = f"repo={s}"
                if not reason:
                    d = domain_of(url)
                    if d and d not in GENERIC_DOMAINS and d in domains:
                        reason = f"domain={d}"
                if not reason:
                    best, best_r = None, 0.0
                    for bn in names:
                        r = SequenceMatcher(None, nn, bn).ratio()
                        if r > best_r:
                            best_r, best = r, bn
                    if best_r >= 0.92:
                        reason = f"fuzzy({best_r:.2f})={norm_to_raw.get(best, best)}"

                dropped_hit = ""
                if not reason:
                    s, d = repo_slug(url), domain_of(url)
                    if nn in dnames:
                        dropped_hit = "name"
                    elif s and s in dslugs:
                        dropped_hit = f"repo={s}"
                    elif d and d not in GENERIC_DOMAINS and d in ddomains:
                        dropped_hit = f"domain={d}"

                if reason:
                    matches.append(parts + [reason])
                elif dropped_hit:
                    prev_dropped.append(parts + [dropped_hit])
                else:
                    gaps.append(parts + [""])

    with open("gap_report.tsv", "w", encoding="utf-8") as f:
        f.write("name\tmaker\turl\textra\tdescription\tsource\n")
        for g in gaps:
            f.write("\t".join(g[:6]) + "\n")
    with open("match_log.tsv", "w", encoding="utf-8") as f:
        for m in matches:
            f.write("\t".join(m[:3] + [m[-1]]) + "\n")

    with open("previously_dropped.tsv", "w", encoding="utf-8") as f:
        for m in prev_dropped:
            f.write("\t".join(m[:3] + [m[-1]]) + "\n")

    print(f"baseline entries: {len(raw_names)}")
    print(f"candidates (deduped): {len(seen_cand)}")
    print(f"matched to baseline: {len(matches)}")
    print(f"previously evaluated & dropped: {len(prev_dropped)}")
    print(f"GAPS (never seen by census): {len(gaps)}")


if __name__ == "__main__":
    main()
