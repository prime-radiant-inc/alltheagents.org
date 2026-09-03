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

import json  # noqa: E402
import shutil  # noqa: E402
import tempfile  # noqa: E402

from entrybot import checks, repo as repo_mod  # noqa: E402
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

ADD_TEMPLATE = ROOT / ".github" / "ISSUE_TEMPLATE" / "add-agent.yml"
FIX_TEMPLATE = ROOT / ".github" / "ISSUE_TEMPLATE" / "update-agent.yml"

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


if __name__ == "__main__":
    unittest.main()
