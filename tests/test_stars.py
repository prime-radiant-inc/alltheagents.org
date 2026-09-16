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
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "sources"))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from fetch_stars import repo_from_url  # noqa: E402
from generate_pages import parse_stars  # noqa: E402
from sync_stars import classify, load_snapshot, scan_entries  # noqa: E402


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
