"""Read and update repo state: entries, ledger, makers.

`parse_frontmatter` is the line-based parser the repo's original
generator (scripts/generate_json_from_md.py, removed 2026-09-03) used to
read entry files; `slugify` is copied from scripts/generate_pages.py so this package does
not depend on that legacy importer being on sys.path. The site
itself parses frontmatter with gray-matter inside Eleventy; the unit test
round-trips written entries through that parser.
"""
import json
import re
from pathlib import Path

# Template order (agents/_TEMPLATE.md), with `stars` where the template
# says `github_stars` because every existing file uses `stars`.
FIELD_ORDER = [
    "name", "slug", "layout", "category", "maker", "license", "url",
    "source_code_url", "source_available", "homepage", "docs_url",
    "download_url", "install_method", "platforms", "autonomy_level",
    "specialization", "language", "first_released", "current_release",
    "maintained", "mcp_support", "plugin_support", "claude_code_plugin",
    "subagents", "hooks", "plan_mode", "plugin_docs_url", "config_docs_url",
    "model_providers", "pricing", "stars", "sources", "last_verified",
    "what_makes_it_special",
]
LIST_FIELDS = {"platforms", "autonomy_level", "sources"}

LEDGER_ROW = re.compile(r"^\| `([^`]+)` \| (.*?) \| (\S+) \| (.*) \|$")
TABLE_HEADER = "| Slug | Name | Category | Rationale |"


def parse_frontmatter(content):
    """Line-based frontmatter parser (see module docstring)."""
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


def slugify(name):
    """Copied from scripts/generate_pages.py."""
    slug = name.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_-]+", "-", slug)
    slug = slug.strip("-")
    return slug or "unnamed"


def normalize_url(url):
    """Lowercase, drop scheme, www., query, fragment, trailing slash, .git."""
    if not url:
        return None
    u = str(url).strip().lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    u = u.split("#", 1)[0].split("?", 1)[0].rstrip("/")
    if u.endswith(".git"):
        u = u[:-4]
    return u or None


class Repo:
    def __init__(self, root):
        self.root = Path(root)
        self.agents_dir = self.root / "agents"
        self.ledger_md = self.root / "CATEGORIZATION_LEDGER.md"
        self.makers_json = self.root / "_data" / "makers.json"
        self.slug_overrides = self.root / "scripts" / "slug_overrides.json"

    def entries(self):
        out = {}
        for path in sorted(self.agents_dir.glob("*.md")):
            if path.name == "_TEMPLATE.md":
                continue
            fm, body = parse_frontmatter(path.read_text(encoding="utf-8"))
            out[path.stem] = {"path": path, "fm": fm, "body": body}
        return out

    def slug_for(self, name):
        overrides = {}
        if self.slug_overrides.exists():
            overrides = json.loads(self.slug_overrides.read_text(encoding="utf-8"))
        return overrides.get(name) or slugify(name)

    def urls_in_use(self):
        seen = {}
        for slug, entry in self.entries().items():
            for key in ("url", "source_code_url", "homepage"):
                norm = normalize_url(entry["fm"].get(key))
                if norm:
                    seen.setdefault(norm, slug)
        return seen

    def resolve_entry(self, text):
        """Slugs matching a page link, a slug, or a name (case-insensitive)."""
        entries = self.entries()
        m = re.search(r"/agents/([A-Za-z0-9._-]+)/?", text or "")
        if m:
            return [m.group(1)] if m.group(1) in entries else []
        needle = (text or "").strip().lower()
        if needle in entries:
            return [needle]
        return [s for s, e in entries.items() if str(e["fm"].get("name") or "").lower() == needle]

    def makers(self):
        return json.loads(self.makers_json.read_text(encoding="utf-8"))

    def ledger_rows(self):
        rows = []
        for line in self.ledger_md.read_text(encoding="utf-8").splitlines():
            m = LEDGER_ROW.match(line)
            if m:
                rows.append({"slug": m.group(1), "name": m.group(2),
                             "category": m.group(3), "rationale": m.group(4)})
        return rows

    def render_ledger(self, rows):
        """The ledger file with `rows` as its table; everything above the
        table is kept verbatim.

        Row order is preserved as given so a single insert makes a
        one-line diff.
        """
        text = self.ledger_md.read_text(encoding="utf-8")
        head = text[: text.index(TABLE_HEADER)]
        table = [TABLE_HEADER, "|------|------|----------|-----------|"]
        for row in rows:
            table.append(f"| `{row['slug']}` | {row['name']} | {row['category']} | {row['rationale']} |")
        return head + "\n".join(table) + "\n"
