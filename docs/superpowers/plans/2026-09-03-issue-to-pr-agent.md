# Issue-to-PR Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Any coding agent, told "process issue N", can turn a filled-in issue form into a verified pull request using one runbook and one script.

**Architecture:** A stdlib-only Python package `scripts/entrybot/` does every exact operation (parse the form, validate, write the entry and ledger, regenerate JSON, call `gh`). A thin CLI `scripts/entry_bot.py` exposes it as subcommands. A runbook `docs/issue-to-pr.md` holds the research protocol the agent follows between the subcommands.

**Tech Stack:** Python 3 standard library only (`re`, `json`, `subprocess`, `urllib`, `argparse`, `unittest`). `gh` CLI for GitHub. Eleventy (already installed) for the build check.

**Spec:** `docs/superpowers/specs/2026-09-03-issue-to-pr-agent-design.md`

## Global Constraints

- No dependencies beyond the Python standard library. No PyYAML.
- No credentials stored in the repo. All GitHub access goes through the already-authenticated `gh` CLI.
- The script owns `CATEGORIZATION_LEDGER.md`, `scripts/categorization_ledger.json`, `_data/makers.json`, `_data/agents.json`. The agent never hand-edits them.
- Entry files must parse with `parse_frontmatter` in `scripts/generate_json_from_md.py`: strings quoted, `null` bare, lists as `key:` then `  - "value"`, empty lists as `[]`, booleans as the strings `"True"` / `"False"`.
- Per-run scratch lives in `work/issue-<N>/` (gitignored).
- Test count stays small: five tests in one file. Do not add more without a reason.
- All `gh`, `git`, and HTTP calls go through `entrybot.gh.run` / `entrybot.gh.http_ok` so tests can patch them.
- Deviation from the spec, agreed here: the spec names one file `scripts/entry_bot.py`; this plan keeps that as the CLI and puts the logic in a package `scripts/entrybot/` so no file grows past a few hundred lines.

## File map

| Path | Responsibility |
|------|---------------|
| `scripts/entry_bot.py` | argparse CLI; each subcommand is a thin handler that loads JSON, calls the package, writes JSON |
| `scripts/entrybot/__init__.py` | empty |
| `scripts/entrybot/forms.py` | read a form template's field ids/labels/types; parse a rendered issue body; parse `field: old -> new` lines |
| `scripts/entrybot/repo.py` | `Repo` class: entries, slugs, URL normalisation, ledger read/render, makers, entry resolution; the frontmatter parser copied from `generate_json_from_md.py` |
| `scripts/entrybot/checks.py` | enums, required fields, `check_add`, `check_fix`, `check_built` |
| `scripts/entrybot/writer.py` | render frontmatter, `write_entry`, `apply_fix` |
| `scripts/entrybot/gh.py` | `run`, `http_ok`, and `gh` wrappers |
| `scripts/entrybot/publish.py` | `pr` and `reject` |
| `scripts/tests/test_entry_bot.py` | the five tests |
| `scripts/tests/fixtures/add.md`, `fix.md` | rendered issue bodies |
| `docs/issue-to-pr.md` | the runbook |
| `AGENTS.md`, `CLAUDE.md` | pointers to the runbook |
| `.gitignore` | add `work/` |
| `_data/source_urls.json`, `scripts/source_urls.json` | add `github-issue` |

Run tests with:

```bash
python3 -m unittest scripts/tests/test_entry_bot.py -v
```

---

### Task 1: Form parsing

**Files:**
- Create: `scripts/entrybot/__init__.py` (empty)
- Create: `scripts/entrybot/forms.py`
- Create: `scripts/tests/fixtures/add.md`
- Create: `scripts/tests/fixtures/fix.md`
- Create: `scripts/tests/test_entry_bot.py`

**Interfaces:**
- Produces: `forms.template_fields(path) -> list[dict(id, label, type, required)]`
- Produces: `forms.parse_add(body: str, template_path) -> dict[id, value]` (category reduced to the word before the colon; checkbox groups are lists; blanks are `None`)
- Produces: `forms.parse_fix(body: str, template_path) -> dict(fields, changes, unparsed, slug_hint)`
- Produces: `forms.parse_changes(text) -> (changes: list[dict(field, old, new)], unparsed: list[str])`
- Produces: `forms.slug_from_link(text) -> str | None`

- [ ] **Step 1: Create the fixtures**

`scripts/tests/fixtures/add.md` (this is how GitHub renders the add form; note `_No response_`, `[X]` checkboxes, and the category option text):

```markdown
### Name

Foo Agent

### Primary URL

https://foo.dev

### Source code URL

https://github.com/foo-inc/foo-agent

### Maker

Foo Inc

### License

_No response_

### Category

agent: codes itself and owns its own tool loop

### Category rationale

A terminal agent that drives its own prompt-model-tool loop and edits files directly.

### What makes it special

Runs entirely offline against local models and never phones home.

### Narrative

Foo Agent started as a weekend project to prove a coding agent could run on a laptop with no network.
It reads the repo, plans, and edits files in a loop, and its users are developers in air-gapped environments.

### Platforms

- [X] CLI
- [ ] IDE
- [X] Web
- [ ] Desktop
- [ ] Autonomous

### Implementation language

_No response_

### First released

2025-03-01

### Most recent release

_No response_

### Maintained

active

### Pricing

BYOK

### Model providers

Ollama, OpenAI

### Install method

_No response_

### Docs URL

_No response_

### Extensibility

- [X] MCP
- [ ] Plugins
- [ ] Subagents
- [X] Hooks
- [ ] Plan mode

### Anything else?

_No response_

### Before submitting

- [X] I searched the catalog and this is not already listed.
```

`scripts/tests/fixtures/fix.md`:

```markdown
### Entry

https://alltheagents.org/agents/cline/

### What changed?

license: Apache-2.0 -> MIT
maintained: active -> dormant
this line is not a change

### Source

https://github.com/cline/cline/blob/main/LICENSE

### New category

No change

### Category rationale

_No response_

### Anything else?

_No response_
```

- [ ] **Step 2: Write the two parser tests**

`scripts/tests/test_entry_bot.py`:

```python
"""Tests for scripts/entrybot. Run: python3 -m unittest scripts/tests/test_entry_bot.py -v"""
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent
ROOT = SCRIPTS.parent
FIXTURES = HERE / "fixtures"
sys.path.insert(0, str(SCRIPTS))

from entrybot import forms  # noqa: E402

ADD_TEMPLATE = ROOT / ".github" / "ISSUE_TEMPLATE" / "add-agent.yml"
FIX_TEMPLATE = ROOT / ".github" / "ISSUE_TEMPLATE" / "update-agent.yml"


class FormsTest(unittest.TestCase):
    def test_parse_add_fixture(self):
        fields = forms.parse_add((FIXTURES / "add.md").read_text(), ADD_TEMPLATE)
        self.assertEqual(fields["name"], "Foo Agent")
        self.assertEqual(fields["url"], "https://foo.dev")
        self.assertIsNone(fields["license"])
        self.assertEqual(fields["category"], "agent")
        self.assertEqual(fields["platforms"], ["CLI", "Web"])
        self.assertEqual(fields["extensibility"], ["MCP", "Hooks"])
        self.assertEqual(fields["pricing"], "BYOK")
        self.assertIn("air-gapped", fields["narrative"])
        self.assertNotIn("confirm", fields)

    def test_parse_fix_fixture(self):
        parsed = forms.parse_fix((FIXTURES / "fix.md").read_text(), FIX_TEMPLATE)
        self.assertEqual(parsed["slug_hint"], "cline")
        self.assertEqual(
            parsed["changes"],
            [
                {"field": "license", "old": "Apache-2.0", "new": "MIT"},
                {"field": "maintained", "old": "active", "new": "dormant"},
            ],
        )
        self.assertEqual(parsed["unparsed"], ["this line is not a change"])
        self.assertIsNone(parsed["fields"]["category"])
        self.assertEqual(parsed["fields"]["source"], "https://github.com/cline/cline/blob/main/LICENSE")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `python3 -m unittest scripts/tests/test_entry_bot.py -v`
Expected: ImportError, `No module named 'entrybot'`.

- [ ] **Step 4: Write forms.py**

Create empty `scripts/entrybot/__init__.py`, then `scripts/entrybot/forms.py`:

```python
"""Parse GitHub issue-form bodies back into the form's field ids.

GitHub renders a submitted form as one `### <Label>` heading per field
followed by the value. Blank optional fields render as `_No response_`.
Checkbox groups render as `- [X] Label` / `- [ ] Label` lines. The field
ids and labels are read from the template YAML so a label edit in the
form never breaks parsing.
"""
import re
from pathlib import Path

NO_RESPONSE = {"", "_No response_", "None", "No change"}
CHANGE_RE = re.compile(r"^\s*([A-Za-z_]+)\s*:\s*(.*?)\s*->\s*(.*?)\s*$")
IGNORED_IDS = {"confirm"}


def template_fields(path):
    """Return [{id, label, type, required}] in form order from a template YAML.

    A deliberately small scanner: the templates are flat enough that
    tracking `- type:`, `id:`, the first `label:`, and `required: true`
    per field is sufficient. Option labels are `- label:` lines and skip
    the label regex because of the leading dash.
    """
    fields = []
    current = None
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        m = re.match(r"^-\s+type:\s*(\S+)", line)
        if m:
            current = {"id": None, "label": None, "type": m.group(1), "required": False}
            fields.append(current)
            continue
        if current is None:
            continue
        m = re.match(r"^id:\s*(\S+)", line)
        if m and current["id"] is None:
            current["id"] = m.group(1)
            continue
        m = re.match(r"^label:\s*(.+)$", line)
        if m and current["label"] is None:
            current["label"] = m.group(1).strip().strip('"')
            continue
        if line == "required: true" and current["type"] != "checkboxes":
            current["required"] = True
    return [f for f in fields if f["id"] and f["id"] not in IGNORED_IDS]


def split_sections(body):
    """Return [(label, text)] from a rendered issue body."""
    body = body.replace("\r\n", "\n")
    parts = re.split(r"^### (.+?)\s*$", body, flags=re.M)
    return [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts) - 1, 2)]


def parse_body(body, fields):
    """Map a rendered body onto field ids. Unknown headings are ignored."""
    by_label = {f["label"]: f for f in fields}
    out = {f["id"]: None for f in fields}
    for label, text in split_sections(body):
        field = by_label.get(label)
        if field is None:
            continue
        if field["type"] == "checkboxes":
            out[field["id"]] = re.findall(r"^- \[[xX]\] (.+?)\s*$", text, flags=re.M)
        elif text in NO_RESPONSE:
            out[field["id"]] = None
        else:
            out[field["id"]] = text
    return out


def parse_add(body, template_path):
    fields = parse_body(body, template_fields(template_path))
    if fields.get("category"):
        fields["category"] = fields["category"].split(":", 1)[0].strip()
    return fields


def parse_changes(text):
    """Parse `field: old -> new` lines. Non-matching lines go to `unparsed`."""
    changes, unparsed = [], []
    for line in (text or "").splitlines():
        if not line.strip():
            continue
        m = CHANGE_RE.match(line)
        if m:
            changes.append({"field": m.group(1), "old": m.group(2) or None, "new": m.group(3) or None})
        else:
            unparsed.append(line.strip())
    return changes, unparsed


def slug_from_link(text):
    m = re.search(r"/agents/([A-Za-z0-9._-]+)/?", text or "")
    return m.group(1) if m else None


def parse_fix(body, template_path):
    fields = parse_body(body, template_fields(template_path))
    changes, unparsed = parse_changes(fields.get("changes"))
    return {
        "fields": fields,
        "changes": changes,
        "unparsed": unparsed,
        "slug_hint": slug_from_link(fields.get("entry")),
    }
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `python3 -m unittest scripts/tests/test_entry_bot.py -v`
Expected: both tests PASS.

- [ ] **Step 6: Commit**

```bash
git add scripts/entrybot/__init__.py scripts/entrybot/forms.py scripts/tests/fixtures/add.md scripts/tests/fixtures/fix.md scripts/tests/test_entry_bot.py
git commit -m "Entry bot: issue form parser"
```

---

### Task 2: Repo state and pre-flight checks

**Files:**
- Create: `scripts/entrybot/repo.py`
- Create: `scripts/entrybot/checks.py`
- Create: `scripts/entrybot/gh.py`
- Modify: `scripts/tests/test_entry_bot.py`

**Interfaces:**
- Consumes: nothing from Task 1 beyond the test file.
- Produces: `repo.FIELD_ORDER: list[str]`, `repo.parse_frontmatter(text) -> (dict, body)`, `repo.slugify(name)`, `repo.normalize_url(url)`
- Produces: `repo.Repo(root)` with `.root`, `.agents_dir`, `.ledger_md`, `.ledger_json`, `.makers_json`, `.entries() -> dict[slug, {path, fm, body}]`, `.slug_for(name)`, `.urls_in_use() -> dict[norm_url, slug]`, `.resolve_entry(text) -> list[slug]`, `.makers() -> dict`, `.ledger_rows() -> list[dict(slug, name, category, rationale)]`, `.render_ledger(rows) -> str`, `.ledger_json_rows() -> list`
- Produces: `checks.CATEGORIES`, `checks.MAINTAINED`, `checks.PRICING`, `checks.PLATFORMS`, `checks.enum_problems(values) -> list[str]`, `checks.check_add(fields, repo, url_ok=None) -> list[str]`, `checks.check_fix(issue, repo) -> (problems, warnings)`, `checks.check_built(repo, slug) -> list[str]`
- Produces: `gh.run(args, input=None) -> str`, `gh.http_ok(url) -> bool`

- [ ] **Step 1: Write the test for check_add**

Add to `scripts/tests/test_entry_bot.py` after the imports:

```python
import json  # noqa: E402
import shutil  # noqa: E402
import tempfile  # noqa: E402

from entrybot import checks, repo as repo_mod  # noqa: E402

ALPHA_MD = '''---
name: "Alpha"
slug: "alpha"
layout: "agent.njk"
category: "agent"
maker: "alpha-co"
license: "MIT"
url: "https://alpha.dev"
source_code_url: "https://github.com/alpha-co/alpha"
source_available: "True"
platforms:
  - "CLI"
maintained: "active"
stars: "12"
sources: []
what_makes_it_special: "Alpha special."
---

Alpha narrative body.
'''

ZED_MD = '''---
name: "Zed Thing"
slug: "zed-thing"
layout: "agent.njk"
category: "multiplexer"
maker: null
license: null
url: "https://zed.example"
source_code_url: null
platforms: []
what_makes_it_special: "Zed special."
---

Zed narrative body.
'''

LEDGER_MD = '''# Categorization Ledger

Intro paragraph.

## Summary

**2 entries**: 1 agent, 1 multiplexer, 0 agent-sdk, 0 other.

## Decisions

| Slug | Name | Category | Rationale |
|------|------|----------|-----------|
| `alpha` | Alpha | agent | Owns its loop. |
| `zed-thing` | Zed Thing | multiplexer | Runs other agents. |
'''


def make_repo():
    """A throwaway repo root with two entries, a ledger, and one maker."""
    root = Path(tempfile.mkdtemp(prefix="entrybot-"))
    (root / "agents").mkdir()
    (root / "_data").mkdir()
    (root / "scripts").mkdir()
    (root / "agents" / "alpha.md").write_text(ALPHA_MD)
    (root / "agents" / "zed-thing.md").write_text(ZED_MD)
    (root / "CATEGORIZATION_LEDGER.md").write_text(LEDGER_MD)
    (root / "scripts" / "categorization_ledger.json").write_text(json.dumps([
        {"slug": "alpha", "name": "Alpha", "category": "agent", "rationale": "Owns its loop."},
        {"slug": "zed-thing", "name": "Zed Thing", "category": "multiplexer", "rationale": "Runs other agents."},
    ], indent=2))
    (root / "_data" / "makers.json").write_text(json.dumps({
        "alpha-co": {"name": "Alpha Co", "maker_type": "company", "country": "US",
                     "makes_models": False, "revenue_model": [], "website": "https://alpha.dev"}
    }, indent=2) + "\n")
    (root / "scripts" / "slug_overrides.json").write_text("{}")
    return repo_mod.Repo(root)
```

And the test class:

```python
class ChecksTest(unittest.TestCase):
    def setUp(self):
        self.repo = make_repo()
        self.addCleanup(shutil.rmtree, self.repo.root)

    def test_check_add_rejects_blank_required_and_duplicate_url(self):
        fields = forms.parse_add((FIXTURES / "add.md").read_text(), ADD_TEMPLATE)
        fields["maker"] = None
        fields["source_code_url"] = "https://github.com/Alpha-Co/alpha.git"
        problems = checks.check_add(fields, self.repo, url_ok=lambda url: True)
        self.assertIn("required field blank: maker", problems)
        self.assertIn("source_code_url already listed under entry: alpha", problems)
        self.assertEqual(len(problems), 2)

        problems = checks.check_add(fields, self.repo, url_ok=lambda url: False)
        self.assertIn("primary URL not reachable: https://foo.dev", problems)
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest scripts/tests/test_entry_bot.py -v`
Expected: ImportError for `entrybot.checks`.

- [ ] **Step 3: Write gh.py**

`scripts/entrybot/gh.py`:

```python
"""Every external call: subprocess (git, gh, npx, python) and HTTP.

Tests patch `run` and `http_ok`; nothing else in the package touches the
network or a subprocess directly.
"""
import json
import subprocess
import urllib.error
import urllib.request

USER_AGENT = "alltheagents-entry-bot"


def run(args, input=None, cwd=None):
    """Run a command, return stdout. Raise RuntimeError with stderr on failure."""
    proc = subprocess.run(args, input=input, capture_output=True, text=True, cwd=cwd)
    if proc.returncode != 0:
        raise RuntimeError(f"{' '.join(str(a) for a in args)} failed:\n{proc.stderr.strip()}")
    return proc.stdout


def http_ok(url, timeout=10):
    """True when the URL answers 2xx or 3xx (redirects are followed)."""
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return 200 <= resp.status < 400
        except urllib.error.HTTPError as err:
            if method == "GET":
                return 200 <= err.code < 400
        except Exception:
            if method == "GET":
                return False
    return False


def gh_json(args):
    return json.loads(run(["gh", *args]))


def issue_view(number):
    return gh_json(["issue", "view", str(number), "--json",
                    "number,title,body,labels,author,url,comments"])


def issue_comment(number, body_file):
    run(["gh", "issue", "comment", str(number), "--body-file", str(body_file)])


def ensure_label(name, color="d4c5f9", description=""):
    names = {l["name"] for l in gh_json(["label", "list", "--limit", "200", "--json", "name"])}
    if name not in names:
        run(["gh", "label", "create", name, "--color", color, "--description", description])


def add_label(number, name):
    run(["gh", "issue", "edit", str(number), "--add-label", name])


def remote_branch_exists(remote, branch):
    return bool(run(["git", "ls-remote", "--heads", remote, branch]).strip())


def pr_create(title, body_file, base, head):
    return run(["gh", "pr", "create", "--base", base, "--head", head,
                "--title", title, "--body-file", str(body_file)]).strip()
```

- [ ] **Step 4: Write repo.py**

`scripts/entrybot/repo.py`:

```python
"""Read and update repo state: entries, ledger, makers.

`parse_frontmatter` and `slugify` are copied from
scripts/generate_json_from_md.py and scripts/generate_pages.py. Those
scripts run their generators at import time, so they cannot be imported.
Keep the copies byte-for-byte in sync with the originals.
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
SUMMARY_RE = re.compile(r"^\*\*\d+ entries\*\*: .*$", re.M)
TABLE_HEADER = "| Slug | Name | Category | Rationale |"
CATEGORY_ORDER = ("agent", "multiplexer", "agent-sdk", "other")


def parse_frontmatter(content):
    """Copied from scripts/generate_json_from_md.py."""
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
        self.ledger_json = self.root / "scripts" / "categorization_ledger.json"
        self.makers_json = self.root / "_data" / "makers.json"
        self.slug_overrides = self.root / "scripts" / "slug_overrides.json"
        self.agents_json = self.root / "_data" / "agents.json"

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

    def ledger_json_rows(self):
        return json.loads(self.ledger_json.read_text(encoding="utf-8"))

    def render_ledger(self, rows):
        """The ledger file with `rows` as its table and a recomputed summary.

        Row order is preserved as given so a single insert makes a
        one-line diff.
        """
        text = self.ledger_md.read_text(encoding="utf-8")
        head = text[: text.index(TABLE_HEADER)]
        counts = {c: 0 for c in CATEGORY_ORDER}
        for row in rows:
            counts[row["category"]] = counts.get(row["category"], 0) + 1
        summary = (f"**{len(rows)} entries**: {counts['agent']} agent, "
                   f"{counts['multiplexer']} multiplexer, {counts['agent-sdk']} agent-sdk, "
                   f"{counts['other']} other.")
        head = SUMMARY_RE.sub(summary, head, count=1)
        table = [TABLE_HEADER, "|------|------|----------|-----------|"]
        for row in rows:
            table.append(f"| `{row['slug']}` | {row['name']} | {row['category']} | {row['rationale']} |")
        return head + "\n".join(table) + "\n"
```

- [ ] **Step 5: Write checks.py**

`scripts/entrybot/checks.py`:

```python
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
```

- [ ] **Step 6: Run the tests to verify they pass**

Run: `python3 -m unittest scripts/tests/test_entry_bot.py -v`
Expected: three tests PASS.

- [ ] **Step 7: Commit**

```bash
git add scripts/entrybot/repo.py scripts/entrybot/checks.py scripts/entrybot/gh.py scripts/tests/test_entry_bot.py
git commit -m "Entry bot: repo state, pre-flight checks, gh wrappers"
```

---

### Task 3: Write a new entry

**Files:**
- Create: `scripts/entrybot/writer.py`
- Modify: `scripts/tests/test_entry_bot.py`

**Interfaces:**
- Consumes: `repo.Repo`, `repo.FIELD_ORDER`, `repo.LIST_FIELDS`, `checks.enum_problems`, `checks.ENTRY_REQUIRED`
- Produces: `writer.render_field(key, value) -> list[str]`, `writer.render_entry(entry, body) -> str`, `writer.write_entry(repo, verified, today=None) -> list[Path]` (touched files)

`verified.json` for an add issue (the agent writes this; `write_entry` reads it):

```json
{
  "number": 12,
  "kind": "add",
  "slug": "foo-agent",
  "entry": {"name": "Foo Agent", "category": "agent", "maker": "foo-inc", "url": "https://foo.dev", "...": "any other FIELD_ORDER key"},
  "body": "narrative paragraph",
  "rationale": "one sentence for the ledger",
  "maker_record": {"name": "Foo Inc", "maker_type": "company", "country": null, "makes_models": false, "revenue_model": [], "website": "https://foo.dev"},
  "evidence": {"license": {"submitted": null, "verified": "Apache-2.0", "source": "https://github.com/foo-inc/foo-agent/blob/main/LICENSE", "note": ""}}
}
```

- [ ] **Step 1: Write the round-trip test**

Add to the imports in the test file:

```python
from entrybot import writer  # noqa: E402


def real_parse_frontmatter():
    """The parser the site build uses, pulled out of the generator script
    without running its module-level code."""
    src = (SCRIPTS / "generate_json_from_md.py").read_text()
    block = src[src.index("def parse_frontmatter"):src.index("# Load source URLs")]
    ns = {}
    exec(block, ns)
    return ns["parse_frontmatter"]


VERIFIED_ADD = {
    "number": 12,
    "kind": "add",
    "slug": "foo-agent",
    "entry": {
        "name": "Foo Agent",
        "category": "agent",
        "maker": "foo-inc",
        "license": None,
        "url": "https://foo.dev",
        "source_code_url": "https://github.com/foo-inc/foo-agent",
        "source_available": True,
        "platforms": ["CLI", "Web"],
        "maintained": "active",
        "pricing": "BYOK",
        "stars": 42,
        "what_makes_it_special": "Runs entirely offline against local models.",
    },
    "body": "Foo Agent started as a weekend project.",
    "rationale": "Drives its own prompt-model-tool loop.",
    "maker_record": {"name": "Foo Inc", "maker_type": "company", "country": None,
                     "makes_models": False, "revenue_model": [], "website": "https://foo.dev"},
    "evidence": {},
}
```

And the test class:

```python
class WriterTest(unittest.TestCase):
    def setUp(self):
        self.repo = make_repo()
        self.addCleanup(shutil.rmtree, self.repo.root)

    def test_write_entry_round_trip_and_ledger(self):
        touched = writer.write_entry(self.repo, VERIFIED_ADD, today="2026-09-03")
        text = (self.repo.agents_dir / "foo-agent.md").read_text()
        fm, body = real_parse_frontmatter()(text)
        self.assertEqual(fm["name"], "Foo Agent")
        self.assertEqual(fm["slug"], "foo-agent")
        self.assertEqual(fm["layout"], "agent.njk")
        self.assertIsNone(fm["license"])
        self.assertEqual(fm["source_available"], "True")
        self.assertEqual(fm["platforms"], ["CLI", "Web"])
        self.assertEqual(fm["autonomy_level"], [])
        self.assertEqual(fm["stars"], "42")
        self.assertEqual(fm["sources"], ["github-issue"])
        self.assertEqual(fm["last_verified"], "2026-09-03")
        self.assertEqual(body.strip(), VERIFIED_ADD["body"])

        ledger = self.repo.ledger_md.read_text()
        self.assertIn("**3 entries**: 2 agent, 1 multiplexer, 0 agent-sdk, 0 other.", ledger)
        self.assertLess(ledger.index("| `foo-agent` |"), ledger.index("| `zed-thing` |"))
        self.assertEqual(self.repo.ledger_json_rows()[-1]["slug"], "foo-agent")
        self.assertEqual(self.repo.makers()["foo-inc"]["name"], "Foo Inc")
        self.assertEqual(
            sorted(p.name for p in touched),
            ["CATEGORIZATION_LEDGER.md", "categorization_ledger.json", "foo-agent.md", "makers.json"],
        )
        with self.assertRaises(FileExistsError):
            writer.write_entry(self.repo, VERIFIED_ADD, today="2026-09-03")
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest scripts/tests/test_entry_bot.py -v`
Expected: ImportError for `entrybot.writer`.

- [ ] **Step 3: Write writer.py (write_entry only)**

`scripts/entrybot/writer.py`:

```python
"""Write entry files, ledger rows, and maker records in the repo's exact format."""
import json
from datetime import date

from .checks import ENTRY_REQUIRED, enum_problems
from .repo import FIELD_ORDER, LIST_FIELDS

DEFAULTS = {"layout": "agent.njk", "specialization": "general",
            "platforms": [], "autonomy_level": [], "sources": ["github-issue"]}


def yaml_str(value):
    return '"' + str(value).replace('"', '\\"') + '"'


def render_field(key, value):
    """Lines for one frontmatter field, matching the site's parser."""
    if key in LIST_FIELDS or isinstance(value, list):
        items = value or []
        if not items:
            return [f"{key}: []"]
        return [f"{key}:"] + [f"  - {yaml_str(v)}" for v in items]
    if value is None:
        return [f"{key}: null"]
    if isinstance(value, bool):
        return [f"{key}: " + ('"True"' if value else '"False"')]
    return [f"{key}: {yaml_str(value)}"]


def render_entry(entry, body):
    lines = ["---"]
    for key in FIELD_ORDER:
        lines += render_field(key, entry.get(key))
    lines.append("---")
    return "\n".join(lines) + "\n\n" + body.strip() + "\n"


def validate_entry(entry):
    problems = [f"required entry field blank: {k}" for k in ENTRY_REQUIRED if not entry.get(k)]
    problems += enum_problems(entry)
    unknown = sorted(set(entry) - set(FIELD_ORDER))
    if unknown:
        problems.append(f"unknown entry fields: {unknown}")
    return problems


def ledger_cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def insert_ledger_row(rows, new):
    """Insert at the first position where the existing slug sorts after ours."""
    for i, row in enumerate(rows):
        if row["slug"] > new["slug"]:
            rows.insert(i, new)
            return rows
    rows.append(new)
    return rows


def dump_ledger_json(rows):
    return json.dumps(rows, ensure_ascii=False, indent=2)


def dump_makers(makers):
    return json.dumps(makers, ensure_ascii=False, indent=2) + "\n"


def write_entry(repo, verified, today=None):
    """Create agents/<slug>.md plus ledger and maker updates. Returns touched paths.

    Every file's new contents are built first and written last, so a
    validation failure leaves the repo untouched.
    """
    today = today or date.today().isoformat()
    slug = verified["slug"]
    entry = {**DEFAULTS, **verified["entry"]}
    entry["slug"] = slug
    entry["last_verified"] = today
    problems = validate_entry(entry)
    if not verified.get("body", "").strip():
        problems.append("body (narrative) is empty")
    if not verified.get("rationale", "").strip():
        problems.append("rationale is empty")
    if problems:
        raise ValueError("\n".join(problems))

    path = repo.agents_dir / f"{slug}.md"
    if path.exists():
        raise FileExistsError(f"entry already exists: {path}")

    writes = {path: render_entry(entry, verified["body"])}

    row = {"slug": slug, "name": entry["name"], "category": entry["category"],
           "rationale": ledger_cell(verified["rationale"])}
    writes[repo.ledger_md] = repo.render_ledger(insert_ledger_row(repo.ledger_rows(), row))
    writes[repo.ledger_json] = dump_ledger_json(repo.ledger_json_rows() + [row])

    makers = repo.makers()
    if entry["maker"] not in makers:
        record = verified.get("maker_record")
        if not record:
            raise ValueError(f"maker {entry['maker']!r} is not in _data/makers.json and no maker_record was supplied")
        makers[entry["maker"]] = record
        writes[repo.makers_json] = dump_makers(makers)

    for target, text in writes.items():
        target.write_text(text, encoding="utf-8")
    return list(writes)
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m unittest scripts/tests/test_entry_bot.py -v`
Expected: four tests PASS.

- [ ] **Step 5: Commit**

```bash
git add scripts/entrybot/writer.py scripts/tests/test_entry_bot.py
git commit -m "Entry bot: entry, ledger, and maker writer"
```

---

### Task 4: Apply a fix to an existing entry

**Files:**
- Modify: `scripts/entrybot/writer.py`
- Modify: `scripts/tests/test_entry_bot.py`

**Interfaces:**
- Consumes: `writer.render_field`, `repo.Repo`, `checks.enum_problems`
- Produces: `writer.set_frontmatter_field(text, key, value) -> str`, `writer.replace_body(text, body) -> str`, `writer.apply_fix(repo, verified, today=None) -> list[Path]`

`verified.json` for a fix issue:

```json
{
  "number": 13,
  "kind": "fix",
  "slug": "cline",
  "entry": {"license": "MIT", "maintained": "dormant"},
  "body": null,
  "rationale": null,
  "not_applied": [{"field": "pricing", "new": "free", "reason": "pricing page still shows paid tiers"}],
  "evidence": {"license": {"submitted": "MIT", "verified": "MIT", "source": "https://github.com/cline/cline/blob/main/LICENSE", "note": ""}}
}
```

`rationale` is required when `entry` contains `category`. `body` replaces the narrative when present.

- [ ] **Step 1: Write the apply-fix test**

Add to `WriterTest`:

```python
    def test_apply_fix_touches_only_target_lines(self):
        path = self.repo.agents_dir / "alpha.md"
        before = path.read_text().splitlines()
        verified = {"number": 13, "kind": "fix", "slug": "alpha",
                    "entry": {"license": "Apache-2.0", "platforms": ["CLI", "IDE"]},
                    "body": None, "rationale": None, "not_applied": [], "evidence": {}}
        touched = writer.apply_fix(self.repo, verified, today="2026-09-03")
        after = path.read_text().splitlines()
        self.assertIn('license: "Apache-2.0"', after)
        self.assertIn('last_verified: "2026-09-03"', after)
        self.assertEqual(after[after.index("platforms:") + 1:after.index("platforms:") + 3], ['  - "CLI"', '  - "IDE"'])
        changed_prefixes = ("license:", "platforms:", "  - ", "last_verified:")
        keep = lambda lines: [l for l in lines if not l.startswith(changed_prefixes)]
        self.assertEqual(keep(after), keep(before))
        self.assertEqual([p.name for p in touched], ["alpha.md"])

        verified = {"number": 14, "kind": "fix", "slug": "alpha",
                    "entry": {"category": "multiplexer"}, "body": "New body.",
                    "rationale": "Now orchestrates agents.", "not_applied": [], "evidence": {}}
        touched = writer.apply_fix(self.repo, verified, today="2026-09-03")
        self.assertIn("**2 entries**: 0 agent, 2 multiplexer, 0 agent-sdk, 0 other.", self.repo.ledger_md.read_text())
        self.assertIn("| `alpha` | Alpha | multiplexer | Now orchestrates agents. |", self.repo.ledger_md.read_text())
        self.assertEqual(self.repo.ledger_json_rows()[0]["category"], "multiplexer")
        self.assertTrue(path.read_text().endswith("---\n\nNew body.\n"))
        self.assertEqual(sorted(p.name for p in touched), ["CATEGORIZATION_LEDGER.md", "alpha.md", "categorization_ledger.json"])
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest scripts/tests/test_entry_bot.py -v`
Expected: AttributeError, `module 'entrybot.writer' has no attribute 'apply_fix'`.

- [ ] **Step 3: Add the fix functions to writer.py**

Append to `scripts/entrybot/writer.py`:

```python
def _frontmatter_bounds(lines):
    """Indices of the opening and closing `---` lines."""
    if not lines or lines[0].strip() != "---":
        raise ValueError("file does not start with frontmatter")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return 0, i
    raise ValueError("frontmatter never closes")


def set_frontmatter_field(text, key, value):
    """Rewrite one field's line(s) in place; add it before the closing --- if absent."""
    lines = text.split("\n")
    start, end = _frontmatter_bounds(lines)
    new_lines = render_field(key, value)
    for i in range(start + 1, end):
        if lines[i].startswith(f"{key}:"):
            j = i + 1
            while j < end and lines[j].startswith("  - "):
                j += 1
            return "\n".join(lines[:i] + new_lines + lines[j:])
    return "\n".join(lines[:end] + new_lines + lines[end:])


def replace_body(text, body):
    lines = text.split("\n")
    _, end = _frontmatter_bounds(lines)
    return "\n".join(lines[: end + 1]) + "\n\n" + body.strip() + "\n"


def apply_fix(repo, verified, today=None):
    """Edit only the changed fields of an existing entry. Returns touched paths."""
    today = today or date.today().isoformat()
    slug = verified["slug"]
    path = repo.agents_dir / f"{slug}.md"
    if not path.exists():
        raise FileNotFoundError(f"no entry: {path}")
    changes = dict(verified.get("entry") or {})
    problems = enum_problems(changes)
    unknown = sorted(set(changes) - set(FIELD_ORDER))
    if unknown:
        problems.append(f"unknown entry fields: {unknown}")
    if "category" in changes and not (verified.get("rationale") or "").strip():
        problems.append("category change needs a rationale")
    if problems:
        raise ValueError("\n".join(problems))

    text = path.read_text(encoding="utf-8")
    for key, value in changes.items():
        text = set_frontmatter_field(text, key, value)
    text = set_frontmatter_field(text, "last_verified", today)
    if verified.get("body"):
        text = replace_body(text, verified["body"])
    writes = {path: text}

    if "category" in changes:
        rationale = ledger_cell(verified["rationale"])
        rows = repo.ledger_rows()
        json_rows = repo.ledger_json_rows()
        for row in rows + json_rows:
            if row["slug"] == slug:
                row["category"] = changes["category"]
                row["rationale"] = rationale
        writes[repo.ledger_md] = repo.render_ledger(rows)
        writes[repo.ledger_json] = dump_ledger_json(json_rows)

    for target, content in writes.items():
        target.write_text(content, encoding="utf-8")
    return list(writes)
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m unittest scripts/tests/test_entry_bot.py -v`
Expected: five tests PASS.

- [ ] **Step 5: Commit**

```bash
git add scripts/entrybot/writer.py scripts/tests/test_entry_bot.py
git commit -m "Entry bot: apply-fix writer"
```

---

### Task 5: CLI for fetch, check, write, apply-fix, regen

**Files:**
- Create: `scripts/entry_bot.py`
- Modify: `.gitignore`

**Interfaces:**
- Consumes: everything from Tasks 1 to 4.
- Produces: `python3 scripts/entry_bot.py fetch N [--body-file F --kind add|fix --title T]`, `check work/issue-N/issue.json [--offline]`, `check --built work/issue-N/verified.json`, `write work/issue-N/verified.json`, `apply-fix work/issue-N/verified.json`, `regen`. Writes `work/issue-N/issue.json`, `work/issue-N/touched.json`, `work/issue-N/built.ok`.

No unit test for the CLI; Task 8 exercises it end to end.

- [ ] **Step 1: Add `work/` to .gitignore**

Append the line `work/` to `.gitignore`.

- [ ] **Step 2: Write the CLI**

`scripts/entry_bot.py`:

```python
#!/usr/bin/env python3
"""Turn an issue form into an entry PR. See docs/issue-to-pr.md for the procedure.

Subcommands, in the order a run uses them:
  fetch N        gh issue -> work/issue-N/issue.json
  check FILE     pre-flight on issue.json (exit 1 on any problem)
  write FILE     verified.json -> new entry + ledger + makers + regen
  apply-fix FILE verified.json -> edited entry (+ ledger) + regen
  check --built FILE   eleventy build + page rendered -> work/issue-N/built.ok
  pr N           branch, commit, push, open PR
  reject N --reason-file F   comment + needs-info label, no PR
  regen          rebuild _data/agents.json
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from entrybot import checks, forms, gh, publish, writer  # noqa: E402
from entrybot.repo import Repo  # noqa: E402

TEMPLATES = {"add": ROOT / ".github/ISSUE_TEMPLATE/add-agent.yml",
             "fix": ROOT / ".github/ISSUE_TEMPLATE/update-agent.yml"}
KIND_LABELS = {"new-entry": "add", "correction": "fix"}
KIND_PREFIXES = {"Add:": "add", "Fix:": "fix"}


def work_dir(number):
    d = ROOT / "work" / f"issue-{number}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def fail(lines):
    for line in lines:
        print(line, file=sys.stderr)
    sys.exit(1)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save(path, data):
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {Path(path).relative_to(ROOT)}")


def detect_kind(labels, title, explicit):
    if explicit:
        return explicit
    for label in labels:
        if label in KIND_LABELS:
            return KIND_LABELS[label]
    for prefix, kind in KIND_PREFIXES.items():
        if (title or "").startswith(prefix):
            return kind
    return None


def cmd_fetch(args):
    repo = Repo(ROOT)
    if args.body_file:
        raw = {"number": args.number, "title": args.title or "", "body": Path(args.body_file).read_text(encoding="utf-8"),
               "labels": [], "author": {"login": "local"}, "url": ""}
    else:
        raw = gh.issue_view(args.number)
    labels = [l["name"] for l in raw.get("labels", [])]
    kind = detect_kind(labels, raw.get("title"), args.kind)
    if kind is None:
        fail([f"cannot tell add from fix: labels={labels} title={raw.get('title')!r}; pass --kind"])
    issue = {"number": raw["number"], "kind": kind, "title": raw.get("title"),
             "author": (raw.get("author") or {}).get("login"), "url": raw.get("url")}
    if kind == "add":
        issue["fields"] = forms.parse_add(raw["body"], TEMPLATES["add"])
    else:
        parsed = forms.parse_fix(raw["body"], TEMPLATES["fix"])
        issue.update(parsed)
        candidates = repo.resolve_entry(parsed["fields"].get("entry"))
        issue["slug"] = candidates[0] if len(candidates) == 1 else None
        issue["slug_candidates"] = candidates
    save(work_dir(args.number) / "issue.json", issue)


def cmd_check(args):
    repo = Repo(ROOT)
    data = load(args.file)
    if args.built:
        problems = checks.check_built(repo, data["slug"])
        if problems:
            fail(problems)
        (work_dir(data["number"]) / "built.ok").write_text("ok\n")
        print("build ok; page rendered; slug in agents.json")
        return
    if data["kind"] == "add":
        url_ok = (lambda url: True) if args.offline else None
        problems, warnings = checks.check_add(data["fields"], repo, url_ok=url_ok), []
    else:
        problems, warnings = checks.check_fix(data, repo)
    for w in warnings:
        print(f"warning: {w}")
    if problems:
        fail(problems)
    print("check ok")


def cmd_write(args):
    repo = Repo(ROOT)
    verified = load(args.file)
    try:
        touched = writer.write_entry(repo, verified)
    except (ValueError, FileExistsError) as err:
        fail(str(err).splitlines())
    finish_write(verified, touched)


def cmd_apply_fix(args):
    repo = Repo(ROOT)
    verified = load(args.file)
    try:
        touched = writer.apply_fix(repo, verified)
    except (ValueError, FileNotFoundError) as err:
        fail(str(err).splitlines())
    finish_write(verified, touched)


def finish_write(verified, touched):
    cmd_regen(None)
    rel = [str(p.relative_to(ROOT)) for p in touched] + ["_data/agents.json"]
    save(work_dir(verified["number"]) / "touched.json", rel)


def cmd_regen(args):
    print(gh.run([sys.executable, str(ROOT / "scripts/generate_json_from_md.py")]).strip())


def cmd_pr(args):
    d = work_dir(args.number)
    url = publish.pr(Repo(ROOT), load(d / "issue.json"), load(d / "verified.json"),
                     load(d / "touched.json"), d, base=args.base)
    print(url)


def cmd_reject(args):
    publish.reject(args.number, Path(args.reason_file))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("fetch"); s.add_argument("number", type=int)
    s.add_argument("--body-file"); s.add_argument("--kind", choices=["add", "fix"]); s.add_argument("--title")
    s.set_defaults(fn=cmd_fetch)

    s = sub.add_parser("check"); s.add_argument("file")
    s.add_argument("--offline", action="store_true", help="skip the URL reachability check")
    s.add_argument("--built", action="store_true", help="run eleventy and confirm the page rendered")
    s.set_defaults(fn=cmd_check)

    s = sub.add_parser("write"); s.add_argument("file"); s.set_defaults(fn=cmd_write)
    s = sub.add_parser("apply-fix"); s.add_argument("file"); s.set_defaults(fn=cmd_apply_fix)
    s = sub.add_parser("regen"); s.set_defaults(fn=cmd_regen)

    s = sub.add_parser("pr"); s.add_argument("number", type=int)
    s.add_argument("--base", default="main"); s.set_defaults(fn=cmd_pr)

    s = sub.add_parser("reject"); s.add_argument("number", type=int)
    s.add_argument("--reason-file", required=True); s.set_defaults(fn=cmd_reject)

    args = p.parse_args(argv)
    args.fn(args)


if __name__ == "__main__":
    main()
```

`publish` does not exist until Task 6. To keep this task runnable, create `scripts/entrybot/publish.py` now with two stubs that Task 6 replaces:

```python
"""Open the PR or post the rejection comment. Filled in by Task 6."""


def pr(repo, issue, verified, touched, work, base="main"):
    raise NotImplementedError


def reject(number, reason_file):
    raise NotImplementedError
```

- [ ] **Step 3: Smoke-test offline against the fixture**

Run:

```bash
python3 scripts/entry_bot.py fetch 9001 --body-file scripts/tests/fixtures/add.md --kind add --title "Add: Foo Agent"
python3 scripts/entry_bot.py check work/issue-9001/issue.json --offline
cat work/issue-9001/issue.json
```

Expected: `wrote work/issue-9001/issue.json`, then `check ok`, and the JSON shows `"category": "agent"` and `"platforms": ["CLI", "Web"]`.

Then the fix fixture:

```bash
python3 scripts/entry_bot.py fetch 9002 --body-file scripts/tests/fixtures/fix.md --kind fix
python3 scripts/entry_bot.py check work/issue-9002/issue.json
```

Expected: `"slug": "cline"` in the JSON, then `check ok` with no `warning:` lines (cline's entry has `license: "Apache-2.0"` and `maintained: "active"`, both matching the fixture's old values). If a warning appears, the comparison in `check_fix` is wrong.

- [ ] **Step 4: Confirm `work/` is ignored**

Run: `git status --short`
Expected: no `work/` entry.

- [ ] **Step 5: Commit**

```bash
git add scripts/entry_bot.py scripts/entrybot/publish.py .gitignore
git commit -m "Entry bot: CLI for fetch, check, write, apply-fix, regen"
```

---

### Task 6: Publish (pr and reject)

**Files:**
- Modify: `scripts/entrybot/publish.py`

**Interfaces:**
- Consumes: `gh.run`, `gh.remote_branch_exists`, `gh.pr_create`, `gh.issue_view`, `gh.issue_comment`, `gh.ensure_label`, `gh.add_label`
- Produces: `publish.build_pr_body(issue, verified) -> str`, `publish.pr(repo, issue, verified, touched, work, base="main") -> str` (PR URL), `publish.reject(number, reason_file) -> None`

No unit test; Task 8 dry-runs `build_pr_body` and the guards.

- [ ] **Step 1: Replace the stubs**

`scripts/entrybot/publish.py`:

```python
"""Open the PR or post the rejection comment. All GitHub access via gh."""
from . import gh

FOOTER = "Opened by the issue-to-PR runbook (`docs/issue-to-pr.md`)."


def _display(value):
    if value is None:
        return "—"
    if isinstance(value, list):
        return ", ".join(str(v) for v in value) or "—"
    return str(value).replace("|", "\\|").replace("\n", " ")


def build_pr_body(issue, verified):
    number = issue["number"]
    kind = issue["kind"]
    slug = verified["slug"]
    name = (verified.get("entry") or {}).get("name") or (issue.get("fields") or {}).get("name") or slug
    form = "Add an entry" if kind == "add" else "Fix an entry"
    verb = "Adds" if kind == "add" else "Updates"
    author = issue.get("author") or "unknown"

    lines = [
        "## What does this change?", "",
        f"{verb} the entry for **{name}** (`agents/{slug}.md`) from issue #{number}.", "",
        "## Why?", "",
        f"Submitted through the \"{form}\" form by @{author}. Every field below was checked against the linked source.", "",
        "## How did you test it?", "",
        "`python3 scripts/entry_bot.py check --built` passed: the Eleventy build succeeded, the page rendered, and the slug is in `_data/agents.json`.", "",
        "## Verification", "",
        "| Field | Submitted | Verified | Evidence |", "|---|---|---|---|",
    ]
    evidence = verified.get("evidence") or {}
    for field, ev in evidence.items():
        src = ev.get("source") or "—"
        lines.append(f"| {field} | {_display(ev.get('submitted'))} | {_display(ev.get('verified'))} | {src} |")
    if not evidence:
        lines.append("| — | — | — | — |")

    discrepancies = [(f, ev) for f, ev in evidence.items() if ev.get("submitted") != ev.get("verified")]
    if discrepancies:
        lines += ["", "## Discrepancies", ""]
        for field, ev in discrepancies:
            note = f" {ev['note']}" if ev.get("note") else ""
            lines.append(f"- **{field}**: submitted {_display(ev.get('submitted'))}, verified {_display(ev.get('verified'))}.{note}")

    not_applied = verified.get("not_applied") or []
    if not_applied:
        lines += ["", "## Not applied", ""]
        for item in not_applied:
            lines.append(f"- **{item['field']}** -> {_display(item.get('new'))}: {item.get('reason', 'source did not support it')}")

    lines += ["", f"Closes #{number}", "", FOOTER, ""]
    return "\n".join(lines)


def _remote():
    names = gh.run(["git", "remote"]).split()
    if not names:
        raise RuntimeError("no git remote configured")
    return "origin" if "origin" in names else names[0]


def pr(repo, issue, verified, touched, work, base="main"):
    number = issue["number"]
    slug = verified["slug"]
    kind = issue["kind"]
    if not (work / "built.ok").exists():
        raise RuntimeError("refusing to open a PR: run `check --built` first")
    branch = f"issue-{number}-{slug}" if kind == "add" else f"issue-{number}-fix-{slug}"
    remote = _remote()
    if gh.remote_branch_exists(remote, branch):
        raise RuntimeError(f"branch already exists on {remote}: {branch}")

    name = (verified.get("entry") or {}).get("name") or slug
    title = f"{'Add' if kind == 'add' else 'Fix'} entry: {name} (#{number})"
    body_file = work / "pr-body.md"
    body_file.write_text(build_pr_body(issue, verified), encoding="utf-8")

    start = gh.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo.root).strip()
    gh.run(["git", "checkout", "-b", branch], cwd=repo.root)
    try:
        gh.run(["git", "add", "--", *touched], cwd=repo.root)
        gh.run(["git", "commit", "-m", title], cwd=repo.root)
        gh.run(["git", "push", "-u", remote, branch], cwd=repo.root)
        url = gh.pr_create(title, body_file, base, branch)
    finally:
        gh.run(["git", "checkout", start], cwd=repo.root)
    return url


def reject(number, reason_file):
    reason = reason_file.read_text(encoding="utf-8")
    first_line = reason.strip().splitlines()[0] if reason.strip() else ""
    if not first_line:
        raise RuntimeError("reason file is empty")
    existing = gh.issue_view(number).get("comments") or []
    for c in existing:
        body = (c.get("body") or "").strip()
        if body.splitlines() and body.splitlines()[0] == first_line:
            print(f"a comment starting with the same line already exists on #{number}; not posting again")
            return
    gh.issue_comment(number, reason_file)
    gh.ensure_label("needs-info", description="Issue form needs more information before a PR can be opened")
    gh.add_label(number, "needs-info")
    print(f"commented on #{number} and added needs-info")
```

- [ ] **Step 2: Dry-run the body builder and the guard**

Run:

```bash
python3 - <<'EOF'
import sys, json, pathlib
sys.path.insert(0, "scripts")
from entrybot import publish
issue = json.load(open("work/issue-9001/issue.json"))
verified = {"slug": "foo-agent", "entry": {"name": "Foo Agent"},
            "evidence": {"license": {"submitted": None, "verified": "Apache-2.0", "source": "https://example/LICENSE", "note": "LICENSE file"}}}
print(publish.build_pr_body(issue, verified))
try:
    publish.pr(None, issue, verified, [], pathlib.Path("work/issue-9001"))
except RuntimeError as e:
    print("guard ok:", e)
EOF
```

Expected: a body with the three template headings, one verification row, a Discrepancies bullet for license, `Closes #9001`, then `guard ok: refusing to open a PR: run `check --built` first`.

- [ ] **Step 3: Run the tests**

Run: `python3 -m unittest scripts/tests/test_entry_bot.py -v`
Expected: five tests PASS.

- [ ] **Step 4: Commit**

```bash
git add scripts/entrybot/publish.py
git commit -m "Entry bot: pr and reject"
```

---

### Task 7: Runbook and pointer files

**Files:**
- Create: `docs/issue-to-pr.md`
- Create: `AGENTS.md`
- Create: `CLAUDE.md`
- Modify: `_data/source_urls.json`, `scripts/source_urls.json`
- Modify: `README.md` (one line under Contents)

- [ ] **Step 1: Add the `github-issue` source**

In both `_data/source_urls.json` and `scripts/source_urls.json`, add after the `"hackernews"` line:

```json
  "hackernews": "https://news.ycombinator.com",
  "github-issue": "https://github.com/prime-radiant-inc/alltheagents.org/issues"
```

Confirm both files still parse: `python3 -c "import json;json.load(open('_data/source_urls.json'));json.load(open('scripts/source_urls.json'))"`.

- [ ] **Step 2: Write the runbook**

`docs/issue-to-pr.md`:

````markdown
# Processing an issue into a pull request

This is the procedure for turning one filled-in issue form into one pull
request. It is written for a coding agent that has never seen this repo. A
human can follow it too. Read it top to bottom before starting.

You run `python3 scripts/entry_bot.py <subcommand>` for every mechanical
step. Your own work is research: confirm every claim against a primary
source, then write down what you found. You never hand-edit
`CATEGORIZATION_LEDGER.md`, `scripts/categorization_ledger.json`,
`_data/makers.json`, or `_data/agents.json`. The script owns them.

## Preconditions

```bash
gh auth status          # must succeed; the script pushes and opens PRs with this login
git status --short      # must be empty
git checkout main && git pull
npm ci                  # once per checkout; the build check needs eleventy
python3 -m unittest scripts/tests/test_entry_bot.py   # must pass
```

Everything the run produces lives in `work/issue-<N>/` (gitignored).

## 1. Fetch and check

```bash
python3 scripts/entry_bot.py fetch <N>
python3 scripts/entry_bot.py check work/issue-<N>/issue.json
```

`fetch` writes `issue.json`: the form fields keyed by id, plus `kind`
(`add` or `fix`). `check` exits non-zero with one line per problem. If it
fails, skip to step 5 and use its output as the reason. Warnings
(`warning:` lines) do not stop you, but mention them in the PR body's
notes.

Read `agents/_TEMPLATE.md` now. It defines every frontmatter key and the
meaning of `null` versus `"False"`.

## 2. Research an add issue

Open `work/issue-<N>/issue.json`. For every field below, find the value
in the named source. Write what you found to
`work/issue-<N>/verified.json` in the shape shown at the end of this
section.

| Field | Confirm from | Rule |
|-------|-------------|------|
| `url`, `homepage`, `docs_url` | Load each page | It must load and be about this product. Any other outcome is a reject. |
| `source_code_url`, `source_available` | The repo exists and is public | Blank in the form means closed source: `source_available: false`. |
| `license` | `gh api repos/{owner}/{repo} --jq .license.spdx_id`, else the LICENSE file, else the pricing page | `Proprietary` when nothing is published. `NOASSERTION` from the API means read the LICENSE file. |
| `stars`, `language` | Same API call (`.stargazers_count`, `.language`) | Non-GitHub: `null`. |
| `first_released` | Earliest of: first release, first tag, repo `created_at`, an announced launch date | `gh api repos/{o}/{r}/releases --jq 'last.published_at'`; `gh api repos/{o}/{r} --jq .created_at`. |
| `current_release` | Latest release `published_at`, else latest tag, else `pushed_at` | `gh api repos/{o}/{r}/releases/latest --jq .published_at`. |
| `maintained` | Dates above, plus `.archived` | `active` if pushed within 6 months; `dormant` within 18; `dead` beyond that or archived. `acquired` / `renamed` only with a source that says so. |
| `maker` | Repo owner, or the company on the site's footer or about page | First look for an existing key in `_data/makers.json` (keys are lowercase slugs; match on `name` too). If none, choose a lowercase slug and supply `maker_record`. `maker_type` is `individual`, `company`, or `community`; `gh api users/{owner} --jq .type` says `User` or `Organization`. |
| `category` | The README or product page | Apply the test in `README.md`: with the host tool removed, does this still run a coding task end to end? Yes: `agent`. Runs or coordinates other agents: `multiplexer`. Ships primitives but no agent: `agent-sdk`. Otherwise `other`. Disagreeing with the submitter is a discrepancy, not a reject. Write a one-sentence rationale of your own if you change the category. |
| `platforms`, `mcp_support`, `plugin_support`, `subagents`, `hooks`, `plan_mode`, `model_providers`, `pricing`, `install_method` | The docs or README | Confirmed present: `true`. Confirmed absent: `false`. Not confirmed: `null`. Never guess. `pricing` is one of `free`, `freemium`, `subscription`, `usage`, `BYOK`. |
| `what_makes_it_special`, narrative | The submission, edited | Light edits for house style only: one or two sentences for the first, about a paragraph for the second, no sentence repeated between them, and nothing the sources do not support. Remove claims you could not confirm rather than softening them. |

Fill `evidence` for every field you looked at, including the ones that
matched. `submitted` is the form's value, `verified` is yours, `source` is
the URL that settles it, and `note` says why they differ when they do.

Reject at this step only when you cannot confirm that the product exists
and does what the issue says it does.

`work/issue-<N>/verified.json`:

```json
{
  "number": 12,
  "kind": "add",
  "slug": "foo-agent",
  "entry": {
    "name": "Foo Agent",
    "category": "agent",
    "maker": "foo-inc",
    "license": "Apache-2.0",
    "url": "https://foo.dev",
    "source_code_url": "https://github.com/foo-inc/foo-agent",
    "source_available": true,
    "homepage": null,
    "docs_url": null,
    "install_method": null,
    "platforms": ["CLI"],
    "autonomy_level": ["agentic"],
    "language": "Rust",
    "first_released": "2025-03-01",
    "current_release": "2026-08-20",
    "maintained": "active",
    "mcp_support": true,
    "plugin_support": false,
    "subagents": null,
    "hooks": true,
    "plan_mode": null,
    "model_providers": "Ollama, OpenAI",
    "pricing": "BYOK",
    "stars": 1234,
    "what_makes_it_special": "Runs entirely offline against local models."
  },
  "body": "Foo Agent started as ... (the narrative paragraph)",
  "rationale": "A terminal agent that drives its own prompt-model-tool loop and edits files directly.",
  "maker_record": {
    "name": "Foo Inc",
    "maker_type": "company",
    "country": null,
    "makes_models": false,
    "revenue_model": [],
    "website": "https://foo.dev"
  },
  "evidence": {
    "license": {"submitted": null, "verified": "Apache-2.0", "source": "https://github.com/foo-inc/foo-agent/blob/main/LICENSE", "note": "not given in the form; LICENSE file is Apache-2.0"},
    "category": {"submitted": "agent", "verified": "agent", "source": "https://github.com/foo-inc/foo-agent#readme", "note": ""}
  }
}
```

`slug` comes from the name: lowercase, non-alphanumerics dropped, spaces
to hyphens (`check` already confirmed it is free). `maker_record` is
`null` when the maker key already exists. Keys you leave out of `entry`
are written as `null`.

## 3. Research a fix issue

`issue.json` has `slug`, `changes` (one object per `field: old -> new`
line), `unparsed` (lines that did not fit that pattern; read them, they
may be a change written loosely), and `fields.source`.

For each change open the cited source and confirm the new value using the
rules in the table above. A change the source does not support goes in
`not_applied` with a one-line reason, not in `entry`. If no change
survives, go to step 5.

`work/issue-<N>/verified.json`:

```json
{
  "number": 13,
  "kind": "fix",
  "slug": "cline",
  "entry": {"license": "MIT", "maintained": "dormant"},
  "body": null,
  "rationale": null,
  "not_applied": [{"field": "pricing", "new": "free", "reason": "pricing page still lists paid tiers"}],
  "evidence": {
    "license": {"submitted": "MIT", "verified": "MIT", "source": "https://github.com/cline/cline/blob/main/LICENSE", "note": ""}
  }
}
```

`entry` holds only the keys that change. `body` is the full new
narrative only when the narrative changes. `rationale` is required when
`category` is in `entry`.

## 4. Write, build, open the PR

```bash
python3 scripts/entry_bot.py write work/issue-<N>/verified.json        # add
python3 scripts/entry_bot.py apply-fix work/issue-<N>/verified.json    # fix
python3 scripts/entry_bot.py check --built work/issue-<N>/verified.json
git diff --stat                                                        # look at it
python3 scripts/entry_bot.py pr <N>
```

`write` refuses to overwrite an existing entry and rejects values outside
the enums. `check --built` runs the site build and confirms the page
rendered. `pr` creates branch `issue-<N>-<slug>` (or
`issue-<N>-fix-<slug>`), commits only the touched files, pushes, opens
the PR with the verification table and `Closes #<N>`, and returns you to
the branch you started on. It refuses to run without a passing build or
when the branch already exists.

Report the PR URL. You are done.

## 5. Reject

Write `work/issue-<N>/reject.md` in three short parts: what you checked,
what failed, what would unblock it. The first line is the summary; a
re-run that produces the same first line will not post twice.

```bash
python3 scripts/entry_bot.py reject <N> --reason-file work/issue-<N>/reject.md
```

This posts one comment and adds the `needs-info` label. No PR. Report
what you posted. You are done.

## Never

- Edit the ledger, the JSON data files, or `makers.json` by hand.
- Invent a value for a field the sources do not confirm. `null` is correct.
- Open a PR for an issue that failed `check`.
- Process a second issue in the same run.
- Push to `main`.
````

- [ ] **Step 3: Write the pointer files**

`AGENTS.md`:

```markdown
# Agent instructions

To process an issue into a pull request, follow `docs/issue-to-pr.md` exactly.
The entry schema is `agents/_TEMPLATE.md`; the category definitions are in `README.md`.
```

`CLAUDE.md`:

```markdown
@AGENTS.md
```

- [ ] **Step 4: Add one README line**

In `README.md`, under `## Contents`, after the `scripts/` bullet, add:

```markdown
- `docs/issue-to-pr.md` — runbook for turning an issue form into a PR (`scripts/entry_bot.py` does the mechanical parts)
```

- [ ] **Step 5: Commit**

```bash
git add docs/issue-to-pr.md AGENTS.md CLAUDE.md _data/source_urls.json scripts/source_urls.json README.md
git commit -m "Entry bot: runbook, agent pointers, github-issue source"
```

---

### Task 8: End-to-end dry run

**Files:** none committed. This task proves the pieces fit and leaves the tree clean.

- [ ] **Step 1: Run the add path offline through write and build**

```bash
python3 scripts/entry_bot.py fetch 9001 --body-file scripts/tests/fixtures/add.md --kind add --title "Add: Foo Agent"
python3 scripts/entry_bot.py check work/issue-9001/issue.json --offline
cat > work/issue-9001/verified.json <<'EOF'
{
  "number": 9001, "kind": "add", "slug": "foo-agent",
  "entry": {"name": "Foo Agent", "category": "agent", "maker": "foo-inc", "license": "Apache-2.0",
            "url": "https://foo.dev", "source_code_url": "https://github.com/foo-inc/foo-agent",
            "source_available": true, "platforms": ["CLI", "Web"], "maintained": "active",
            "pricing": "BYOK", "model_providers": "Ollama, OpenAI", "stars": 42,
            "what_makes_it_special": "Runs entirely offline against local models and never phones home."},
  "body": "Foo Agent started as a weekend project to prove a coding agent could run on a laptop with no network.",
  "rationale": "A terminal agent that drives its own prompt-model-tool loop and edits files directly.",
  "maker_record": {"name": "Foo Inc", "maker_type": "company", "country": null, "makes_models": false, "revenue_model": [], "website": "https://foo.dev"},
  "evidence": {"license": {"submitted": null, "verified": "Apache-2.0", "source": "https://github.com/foo-inc/foo-agent/blob/main/LICENSE", "note": "LICENSE file"}}
}
EOF
python3 scripts/entry_bot.py write work/issue-9001/verified.json
python3 scripts/entry_bot.py check --built work/issue-9001/verified.json
git status --short
git diff --stat
```

Expected: `write` prints the regen line (`Generated 1348 entries in agents.json from .md files`) and `wrote work/issue-9001/touched.json`; `check --built` prints `build ok; page rendered; slug in agents.json`; `git status` shows `agents/foo-agent.md` new and `CATEGORIZATION_LEDGER.md`, `scripts/categorization_ledger.json`, `_data/makers.json`, `_data/agents.json` modified; the ledger diff is one inserted row plus the summary line.

- [ ] **Step 2: Inspect the ledger diff**

Run: `git diff CATEGORIZATION_LEDGER.md`
Expected: exactly two hunks: the summary line (`1347` to `1348`, `634 agent` to `635 agent`) and one added row for `foo-agent` at its sorted position (after the last slug that sorts before `foo-agent`). If any other line changed, `render_ledger` is not preserving the table.

- [ ] **Step 3: Run the fix path offline**

```bash
python3 scripts/entry_bot.py fetch 9002 --body-file scripts/tests/fixtures/fix.md --kind fix
python3 scripts/entry_bot.py check work/issue-9002/issue.json
cat > work/issue-9002/verified.json <<'EOF'
{"number": 9002, "kind": "fix", "slug": "cline", "entry": {"license": "MIT"}, "body": null, "rationale": null,
 "not_applied": [{"field": "maintained", "new": "dormant", "reason": "pushed this month"}],
 "evidence": {"license": {"submitted": "MIT", "verified": "MIT", "source": "https://github.com/cline/cline/blob/main/LICENSE", "note": ""}}}
EOF
python3 scripts/entry_bot.py apply-fix work/issue-9002/verified.json
git diff agents/cline.md
```

Expected: the diff shows only `license:` changed and a `last_verified:` line added before the closing `---`.

- [ ] **Step 4: Revert everything the dry run touched**

```bash
git checkout -- agents/cline.md CATEGORIZATION_LEDGER.md scripts/categorization_ledger.json _data/makers.json _data/agents.json
rm -f agents/foo-agent.md
rm -rf work/issue-9001 work/issue-9002 _site/agents/foo-agent
git status --short
```

Expected: clean tree.

- [ ] **Step 5: Run the full test file one last time**

Run: `python3 -m unittest scripts/tests/test_entry_bot.py -v`
Expected: five tests PASS.

---

## Self-review notes

- Spec coverage: fetch (T5), check incl. `--built` (T2, T5), write (T3), apply-fix (T4), regen (T5), pr and reject with both guards (T6), runbook with the per-field table and the three-part reject note (T7), pointer files (T7), `github-issue` source (T7), `work/` ignore (T5), five tests (T1 to T4), atomic writes (T3, T4 build-then-write), duplicate-comment guard (T6), remote branch guard (T6).
- Not in the spec but needed: `fetch --body-file/--kind/--title` for offline runs, title-prefix fallback for kind detection because the repo has no `new-entry` / `correction` labels yet, `check --offline`.
- Spec deviation: package `scripts/entrybot/` instead of one file, recorded in Global Constraints.
- Known limit: `check_fix` skips enum validation for `platforms` changes because a change line carries one string, not a list; `apply_fix` validates the list the agent supplies.
