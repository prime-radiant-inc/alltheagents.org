"""Deterministic pre-flight checks. Each returns a list of problem strings."""
from pathlib import Path

from . import gh
from .repo import FIELD_ORDER, normalize_url

CATEGORIES = {"agent", "multiplexer", "agent-sdk", "other"}
MAINTAINED = {"active", "dormant", "dead", "acquired", "renamed"}
PRICING = {"free", "freemium", "subscription", "usage", "BYOK"}
PLATFORMS = {"CLI", "IDE", "Web", "Desktop", "Autonomous"}
ADD_REQUIRED = ("name", "url", "maker", "category", "rationale",
                "what_makes_it_special", "narrative")
ENTRY_REQUIRED = ("name", "url", "maker", "category")
FIX_FIELDS = set(FIELD_ORDER) | {"narrative"}


def enum_problems(values):
    problems = []
    checks = (("category", CATEGORIES), ("maintained", MAINTAINED), ("pricing", PRICING))
    for key, allowed in checks:
        val = values.get(key)
        if val is not None and val not in allowed:
            problems.append(f"{key} not one of {sorted(allowed)}: {val}")
    for plat in values.get("platforms") or []:
        if plat not in PLATFORMS:
            problems.append(f"platform not one of {sorted(PLATFORMS)}: {plat}")
    return problems


def check_add(fields, repo, url_ok=None):
    url_ok = url_ok or gh.http_ok
    problems = [f"required field blank: {k}" for k in ADD_REQUIRED if not fields.get(k)]
    problems += enum_problems(fields)
    if fields.get("url") and not url_ok(fields["url"]):
        problems.append(f"primary URL not reachable: {fields['url']}")
    if fields.get("name"):
        slug = repo.slug_for(fields["name"])
        if slug in repo.entries():
            problems.append(f"slug already exists: {slug}")
    used = repo.urls_in_use()
    for key in ("url", "source_code_url"):
        norm = normalize_url(fields.get(key))
        if norm and norm in used:
            problems.append(f"{key} already listed under entry: {used[norm]}")
    return problems


def check_fix(issue, repo):
    """Returns (problems, warnings). Warnings do not block."""
    problems, warnings = [], []
    slug = issue.get("slug")
    if not slug:
        cands = issue.get("slug_candidates") or []
        problems.append("entry not resolved to exactly one slug" + (f" (candidates: {cands})" if cands else ""))
        return problems, warnings
    entry = repo.entries().get(slug)
    if entry is None:
        return [f"no entry file for slug: {slug}"], warnings
    changes = issue.get("changes") or []
    if not changes:
        problems.append("no parseable change lines (expected `field: old -> new`)")
    for ch in changes:
        if ch["field"] not in FIX_FIELDS:
            problems.append(f"unknown field: {ch['field']}")
            continue
        if ch["field"] == "narrative":
            continue
        current = entry["fm"].get(ch["field"])
        current_str = "null" if current is None else str(current)
        if (ch["old"] or "null") != current_str:
            warnings.append(f"{ch['field']}: submitted old value {ch['old']!r} but entry has {current_str!r}")
        if ch["new"] is None:
            problems.append(f"{ch['field']}: new value is empty")
    problems += enum_problems({ch["field"]: ch["new"] for ch in changes if ch["field"] != "platforms"})
    if issue["fields"].get("category") and not issue["fields"].get("rationale"):
        problems.append("category change needs a rationale")
    return problems, warnings


def check_built(repo, slug):
    """Run the Eleventy build and confirm the entry rendered."""
    problems = []
    try:
        gh.run(["npx", "@11ty/eleventy"], cwd=repo.root)
    except RuntimeError as err:
        return [f"eleventy build failed:\n{err}"]
    page = repo.root / "_site" / "agents" / slug / "index.html"
    if not page.exists():
        problems.append(f"page not rendered: {page.relative_to(repo.root)}")
    if f'"slug": "{slug}"' not in repo.agents_json.read_text(encoding="utf-8"):
        problems.append(f"slug missing from _data/agents.json: {slug}")
    return problems
