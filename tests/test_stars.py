#!/usr/bin/env python3
"""Tests for the star-count pipeline.

These cover the three ways the /stars/ ranking went wrong:

  1. `repo_from_url` must recognize a GitHub repo and reject non-repo paths
     (github.com/features/... ), so entries resolve to the right project.
  2. `parse_stars` must accept an API-style integer and *raise* on anything
     else. The old `isdigit() else None` silently turned "193k" into null,
     which is what dropped 51 entries out of the ranking.
  3. `classify` must flag an entry whose repo the snapshot has a count for but
     the entry does not carry. That is the regression this whole change exists
     to prevent, and it is also asserted against the real catalog below.

Run with:  python3 -m unittest discover -s tests
"""

import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "sources"))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from fetch_stars import frontmatter, field, repo_from_url  # noqa: E402
from generate_pages import parse_stars  # noqa: E402
from sync_stars import apply_md, classify, load_snapshot, scan_entries  # noqa: E402

import glob
import re

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class TestDateAdded(unittest.TestCase):
    """Every entry carries a catalog-addition date driving /updates/."""

    @classmethod
    def setUpClass(cls):
        cls.files = sorted(
            p for p in glob.glob(os.path.join(ROOT, "agents", "*.md"))
            if not p.endswith("_TEMPLATE.md"))

    def test_every_entry_has_a_well_formed_date_added(self):
        bad = []
        for path in self.files:
            v = field(frontmatter(path), "date_added")
            if not v or not DATE_RE.match(v):
                bad.append(f"{os.path.basename(path)}: {v!r}")
        self.assertEqual(bad, [],
                         f"{len(bad)} entries lack a YYYY-MM-DD date_added:\n"
                         + "\n".join(bad[:20]))

    def test_date_added_never_predates_first_released(self):
        # date_added backfills from first_released when present, else from the
        # earliest commit touching the file — so it can equal first_released
        # but must never be earlier.
        bad = []
        for path in self.files:
            fm = frontmatter(path)
            added, released = field(fm, "date_added"), field(fm, "first_released")
            if added and released and DATE_RE.match(added) and DATE_RE.match(released):
                if added < released:
                    bad.append(f"{os.path.basename(path)}: added {added} < released {released}")
        self.assertEqual(bad, [],
                         f"{len(bad)} entries added before release:\n" + "\n".join(bad[:20]))


class TestFrontmatterBoundaries(unittest.TestCase):
    """The block ends at a `---` *line*, not at the first `---` substring.

    github.com/pinskyrobin/LLM---Detect-AI-Generated-Text contains three hyphens.
    Splitting on the substring truncated the block at the URL and hid every field
    after it, which made that entry look like it pointed at a dead repo.
    """

    def test_value_containing_triple_dash_does_not_truncate_the_block(self):
        path = os.path.join(ROOT, "agents", "llm-detect-ai-generated-text.md")
        fm = frontmatter(path)
        self.assertIsNotNone(fm)
        self.assertEqual(repo_from_url(field(fm, "url")),
                         "pinskyrobin/LLM---Detect-AI-Generated-Text")
        # A field that appears *after* the URL must still be visible.
        self.assertEqual(field(fm, "maintained"), "dead")

    def test_apply_md_rewrites_stars_without_touching_the_url(self):
        text = ('---\nname: "X"\nurl: "https://github.com/o/a---b"\n'
                'stars: null\n---\n\nbody text\n')
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(text)
            path = f.name
        self.addCleanup(os.unlink, path)

        self.assertTrue(apply_md(path, 42))
        out = open(path, encoding="utf-8").read()
        self.assertIn('stars: "42"', out)
        self.assertIn("https://github.com/o/a---b", out)
        self.assertTrue(out.endswith("body text\n"), out)

    def test_apply_md_raises_when_there_is_no_stars_line(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write('---\nname: "X"\n---\n\nbody\n')
            path = f.name
        self.addCleanup(os.unlink, path)
        with self.assertRaises(ValueError):
            apply_md(path, 42)


class TestRepoFromUrl(unittest.TestCase):
    def test_accepts_plain_repo(self):
        self.assertEqual(repo_from_url("https://github.com/aider-ai/aider"), "aider-ai/aider")

    def test_accepts_trailing_noise(self):
        self.assertEqual(repo_from_url("https://github.com/aider-ai/aider.git"), "aider-ai/aider")
        self.assertEqual(repo_from_url("https://github.com/aider-ai/aider/"), "aider-ai/aider")
        self.assertEqual(repo_from_url("https://github.com/aider-ai/aider?tab=readme"), "aider-ai/aider")
        self.assertEqual(repo_from_url("https://github.com/Aider-AI/aider/tree/main"), "Aider-AI/aider")

    def test_rejects_non_repo_paths(self):
        for url in ["https://github.com/features/preview", "https://github.com/topics/ai",
                    "https://github.com/orgs/prime-radiant-inc", "https://github.com/aider-ai"]:
            self.assertIsNone(repo_from_url(url), url)

    def test_rejects_non_github(self):
        for url in ["https://aider.chat/", "https://gitlab.com/x/y", "", None]:
            self.assertIsNone(repo_from_url(url), url)


class TestParseStars(unittest.TestCase):
    def test_accepts_api_integers(self):
        self.assertEqual(parse_stars("195085"), 195085)
        self.assertEqual(parse_stars("0"), 0)
        self.assertEqual(parse_stars("1,234"), 1234)
        self.assertEqual(parse_stars("  42  "), 42)

    def test_empty_means_absent(self):
        self.assertIsNone(parse_stars(""))
        self.assertIsNone(parse_stars("   "))
        self.assertIsNone(parse_stars(None))

    def test_raises_on_hand_typed_values(self):
        # The exact forms that were silently nulled in the original bug.
        for raw in ["193k", "47.9k", "140k", "banana", "1.2.3", "-5", "1e5"]:
            with self.subTest(raw=raw):
                with self.assertRaises(ValueError):
                    parse_stars(raw)


class TestClassify(unittest.TestCase):
    def entry(self, repo, stars):
        return {"path": "agents/x.md", "name": "X", "category": "agent",
                "repo": repo, "stars": stars}

    def test_flags_missing_count(self):
        updates, unresolved, in_sync = classify(
            [self.entry("a/b", None)], {"a/b": {"stargazers_count": 10}})
        self.assertEqual([(e["repo"], n) for e, n in updates], [("a/b", 10)])

    def test_flags_stale_count(self):
        updates, _, _ = classify(
            [self.entry("a/b", 5)], {"a/b": {"stargazers_count": 10}})
        self.assertEqual([(e["repo"], n) for e, n in updates], [("a/b", 10)])

    def test_in_sync_is_left_alone(self):
        updates, unresolved, in_sync = classify(
            [self.entry("a/b", 10)], {"a/b": {"stargazers_count": 10}})
        self.assertEqual(updates, [])
        self.assertEqual(len(in_sync), 1)

    def test_unresolvable_repo_is_not_an_update(self):
        updates, unresolved, _ = classify(
            [self.entry("a/b", 5)], {"a/b": {"stargazers_count": None, "error": "404"}})
        self.assertEqual(updates, [])
        self.assertEqual(len(unresolved), 1)

    def test_entries_without_a_repo_are_ignored(self):
        updates, unresolved, in_sync = classify([self.entry(None, None)], {})
        self.assertEqual((updates, unresolved, in_sync), ([], [], []))


class TestRealCatalog(unittest.TestCase):
    """The guard, asserted against the actual repo contents."""

    @classmethod
    def setUpClass(cls):
        cls.snapshot = load_snapshot(os.path.join(ROOT, "sources", "gh_stars.json"))
        cls.entries = scan_entries()

    def test_snapshot_exists_and_is_populated(self):
        self.assertGreater(len(self.snapshot), 900,
                           "sources/gh_stars.json is missing or thin; run sources/fetch_stars.py")

    def test_every_known_star_is_applied(self):
        updates, _, _ = classify(self.entries, self.snapshot)
        detail = "\n".join(
            f"  {e['path']}: has {e['stars'] if e['stars'] is not None else 'null'}, snapshot says {n}"
            for e, n in updates[:20])
        self.assertEqual(updates, [],
                         f"{len(updates)} entries carry a stale or missing star count:\n{detail}\n"
                         f"Run: python3 scripts/sync_stars.py")

    def test_no_entry_resolves_to_a_reserved_github_path(self):
        # Guards the /stars/ ranking against attaching another project's count.
        for e in self.entries:
            if e["repo"]:
                self.assertNotIn(e["repo"].split("/")[0],
                                 {"features", "about", "topics", "orgs", "settings"},
                                 f"{e['path']} resolves to a non-repo GitHub path")


if __name__ == "__main__":
    unittest.main()
