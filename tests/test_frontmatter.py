import os
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.frontmatter import (
    iter_record_paths, read_record, update_record, write_record,
)

def _agents_dir() -> Path:
    """The census records.

    These live in the harness-census checkout, not in this drop, so the corpus
    tests would silently skip for anyone reviewing the code on its own. Point
    HARNESS_CENSUS_AGENTS at a checkout to run them; see README.md.
    """
    override = os.environ.get("HARNESS_CENSUS_AGENTS")
    if override:
        return Path(override).expanduser()
    here = Path(__file__).resolve().parent.parent
    for candidate in (here / "agents", here.parent / "agents",
                      Path.home() / "code" / "harness-census" / "agents"):
        if candidate.is_dir():
            return candidate
    return here / "agents"


AGENTS = _agents_dir()


class ReadTest(unittest.TestCase):
    def test_round_trip_preserves_types_and_body(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "cline.md"
            path.write_text(
                '---\nname: "Cline"\ncategory: "harness"\n'
                'uses_tools: true\nclassification_evidence:\n'
                '  - "https://github.com/cline/cline"\n---\n\nNarrative.\n',
                encoding="utf-8",
            )
            data, body = read_record(path)
            self.assertEqual(data["category"], "harness")
            self.assertIs(data["uses_tools"], True)
            self.assertEqual(data["classification_evidence"], ["https://github.com/cline/cline"])
            self.assertEqual(body, "Narrative.\n")

    def test_comment_line_ending_in_dashes_does_not_truncate(self):
        """agents/_TEMPLATE.md uses `# --- identity ---` section comments.
        Splitting on the substring `---\\n` cut the frontmatter there, and did
        it silently: safe_load saw only comments and returned None, so the
        record came back with an empty dict and 34 real fields demoted to body."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "t.md"
            path.write_text(
                '---\n# header comment\n\n# --- identity ---\nname: "X"\n'
                'category: "harness"\n\n# --- classification ---\n'
                'uses_tools: true\n---\n\nNarrative.\n',
                encoding="utf-8",
            )
            data, body = read_record(path)
            self.assertEqual(data["name"], "X")
            self.assertEqual(data["category"], "harness")
            self.assertIs(data["uses_tools"], True)
            self.assertEqual(body, "Narrative.\n")

    def test_unterminated_frontmatter_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "t.md"
            path.write_text('---\nname: "X"\n', encoding="utf-8")
            with self.assertRaises(ValueError):
                read_record(path)

    def test_update_preserves_section_comments(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "t.md"
            path.write_text(
                '---\n# --- identity ---\nname: "X"\n'
                '# --- classification ---\ncategory: "agent"\n---\n\nBody.\n',
                encoding="utf-8",
            )
            update_record(path, {"category": "harness"})
            text = path.read_text(encoding="utf-8")
            self.assertIn("# --- identity ---", text)
            self.assertIn("# --- classification ---", text)
            self.assertIn("category: harness", text)
            data, _ = read_record(path)
            self.assertEqual(data["name"], "X")

    def test_iteration_excludes_template(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "_TEMPLATE.md").write_text("---\n---\n", encoding="utf-8")
            (root / "cline.md").write_text("---\nname: Cline\n---\n", encoding="utf-8")
            self.assertEqual([p.name for p in iter_record_paths(root)], ["cline.md"])


class UpdateRecordTest(unittest.TestCase):
    """update_record must be surgical: only the named keys may change."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp)

    def _write(self, text):
        path = Path(self.tmp) / "item.md"
        path.write_text(text, encoding="utf-8")
        return path

    def test_no_op_update_leaves_the_file_byte_identical(self):
        path = self._write('---\nname: "X"\ncategory: "harness"\n---\n\nBody.\n')
        before = path.read_bytes()
        self.assertFalse(update_record(path, {"category": "harness"}))
        self.assertEqual(path.read_bytes(), before)

    def test_only_the_named_key_changes(self):
        path = self._write(
            '---\nname: "X"\nmaker: "Someone"\ncategory: "agent"\n'
            'stars: "854"\nsource_available: True\n---\n\nBody text.\n'
        )
        update_record(path, {"category": "harness"})
        text = path.read_text(encoding="utf-8")
        self.assertIn('category: harness', text)
        # Untouched lines keep their original formatting exactly.
        self.assertIn('name: "X"', text)
        self.assertIn('stars: "854"', text)
        self.assertIn('source_available: True', text)
        self.assertTrue(text.endswith("Body text.\n"))

    def test_new_keys_are_appended(self):
        path = self._write('---\nname: "X"\n---\n\nBody.\n')
        update_record(path, {"classification_status": "verified"})
        data, body = read_record(path)
        self.assertEqual(data["classification_status"], "verified")
        self.assertEqual(data["name"], "X")
        self.assertEqual(body, "Body.\n")

    def test_lists_replace_cleanly(self):
        path = self._write(
            '---\nname: "X"\nclassification_evidence:\n  - "https://a.example"\n'
            '  - "https://b.example"\nmaker: "Someone"\n---\n\nBody.\n'
        )
        update_record(path, {"classification_evidence": ["https://c.example"]})
        data, _ = read_record(path)
        self.assertEqual(data["classification_evidence"], ["https://c.example"])
        self.assertEqual(data["maker"], "Someone")

    def test_empty_list_and_null_round_trip(self):
        path = self._write('---\nname: "X"\n---\n\nBody.\n')
        update_record(path, {"classification_reviewers": [], "category": None})
        data, _ = read_record(path)
        self.assertEqual(data["classification_reviewers"], [])
        self.assertIsNone(data["category"])

    def test_ambiguous_scalars_are_quoted_so_they_survive_reparse(self):
        path = self._write('---\nname: "X"\n---\n\nBody.\n')
        update_record(path, {"quote": "no", "version": "1.0", "flag": "true"})
        data, _ = read_record(path)
        self.assertEqual(data["quote"], "no")
        self.assertEqual(data["version"], "1.0")
        self.assertEqual(data["flag"], "true")

    def test_block_scalar_with_a_blank_line_is_replaced_whole(self):
        """A blank line is part of a block scalar. Stopping the continuation
        scan at the first blank line left the tail orphaned at top level and
        silently changed the value of the next key."""
        path = self._write(
            '---\nname: "X"\ndescription: >\n  first paragraph\n\n'
            '  second paragraph\nmaker: "Someone"\n---\n\nBody.\n'
        )
        update_record(path, {"description": "new text"})
        data, body = read_record(path)
        self.assertEqual(data["description"], "new text")
        self.assertEqual(data["maker"], "Someone")
        self.assertEqual(list(data), ["name", "description", "maker"])
        self.assertNotIn("second paragraph", path.read_text(encoding="utf-8"))
        self.assertEqual(body, "Body.\n")

    def test_literal_block_scalar_is_replaced_whole(self):
        path = self._write(
            '---\nname: "X"\nnotes: |\n  line one\n\n  line two\n'
            'category: "agent"\n---\n\nBody.\n'
        )
        update_record(path, {"notes": "replaced"})
        data, _ = read_record(path)
        self.assertEqual(data["notes"], "replaced")
        self.assertEqual(data["category"], "agent")

    def test_body_with_yaml_delimiter_is_preserved(self):
        path = self._write('---\nname: "X"\n---\n\nBody.\n\n---\n\nMore body.\n')
        update_record(path, {"category": "support"})
        _, body = read_record(path)
        self.assertIn("More body.", body)


@unittest.skipUnless(
    AGENTS.is_dir(),
    f"census records not found at {AGENTS}; set HARNESS_CENSUS_AGENTS to a checkout",
)
class RealCorpusTest(unittest.TestCase):
    """The test the original plan was missing."""

    def test_the_corpus_is_the_expected_size(self):
        """Guards against pointing at the wrong directory and getting a
        vacuously green run."""
        self.assertGreater(len(list(iter_record_paths(AGENTS))), 1000)

    def test_no_op_update_churns_no_real_record(self):
        """Runs against a throwaway copy. AGENTS may be the developer's actual
        checkout, and a test must never write into it -- update_record() is
        exercised here precisely because it might not be a no-op."""
        with tempfile.TemporaryDirectory() as tmp:
            sandbox = Path(tmp) / "agents"
            shutil.copytree(AGENTS, sandbox)
            churned = []
            for path in iter_record_paths(sandbox):
                before = path.read_bytes()
                record, _ = read_record(path)
                update_record(path, {"category": record.get("category")})
                if path.read_bytes() != before:
                    churned.append(path.name)
            self.assertEqual(
                churned, [], f"{len(churned)} records churned by a no-op update"
            )

    def test_every_record_parses(self):
        bad = []
        for path in iter_record_paths(AGENTS):
            try:
                read_record(path)
            except ValueError as exc:
                bad.append(f"{path.name}: {exc}")
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
