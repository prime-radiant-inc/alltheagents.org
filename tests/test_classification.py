"""Rule-engine and validation tests.

The regression cases below are the four that broke the first rule engine. Each
one failed for a different structural reason, so they are worth keeping
individually rather than collapsing into a table.
"""

import csv
import json
import os
import re
import unittest
from collections import Counter
from pathlib import Path

from scripts.classification import (
    KNOWN_RULINGS, derive_category, is_public, validate_record,
)

REPO = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures"

# A record with every loop signal true and a software domain.
LOOP = {
    "software_task_domain": True,
    "accepts_software_task": True,
    "chooses_next_action": True,
    "uses_tools": True,
    "modifies_code_directly": True,
    "iterates_on_results": True,
}

VERIFIED = {
    **LOOP,
    "is_sdk_or_framework": False,
    "delegates_code_changes": False,
    "category": "harness",
    "classification_status": "verified",
    "classification_confidence": "high",
    "classification_source_quality": "primary-current",
    "classification_rationale": "Owns the complete coding loop.",
    "classification_counterevidence": "Can launch helpers, but remains the controlling loop.",
    "classification_evidence": ["https://example.com/docs"],
    "classification_quote": "an agentic coding tool that lives in your terminal",
    "classification_quote_source": "https://example.com/docs",
    "classification_reviewers": ["model:opus-5", "eden"],
    "classification_last_verified": "2026-08-25",
}


class DeriveCategoryTest(unittest.TestCase):
    def test_complete_loop_is_harness_even_with_subagent_coordination(self):
        self.assertEqual(
            derive_category({**LOOP, "coordinates_external_coding_agents": True}),
            "harness",
        )

    def test_external_agent_coordinator_is_multiplexer(self):
        self.assertEqual(
            derive_category({
                **LOOP,
                "modifies_code_directly": False,
                "delegates_code_changes": True,
            }),
            "multiplexer",
        )

    def test_non_loop_framework_is_support(self):
        self.assertEqual(
            derive_category({
                **LOOP, "iterates_on_results": False, "supports_coding_agents": True,
            }),
            "support",
        )

    def test_model_is_something_else(self):
        self.assertEqual(
            derive_category({
                **{k: False for k in LOOP}, "something_else_kind": "model",
            }),
            "something-else",
        )

    def test_undecidable_record_returns_none(self):
        self.assertIsNone(derive_category({"software_task_domain": True}))

    # --- regression: the four cases the original engine got wrong -----------

    def test_sdk_is_support_even_though_it_ships_a_complete_loop(self):
        """Claude Agent SDK bundles the Claude Code CLI, so every loop signal is
        genuinely true. BR-001 puts the nominal test ahead of the functional one."""
        self.assertEqual(
            derive_category({
                **LOOP, "is_sdk_or_framework": True, "supports_coding_agents": True,
            }),
            "support",
        )

    def test_non_software_domain_wins_over_agent_coordination(self):
        """PentestGPT accepts a task and can drive Claude Code or Codex, but its
        domain is security. Without the domain gate it derived as multiplexer."""
        self.assertEqual(
            derive_category({
                **LOOP,
                "software_task_domain": False,
                "coordinates_external_coding_agents": True,
                "something_else_kind": "non-coding-agent",
            }),
            "something-else",
        )

    def test_delegated_code_changes_beat_loop_ownership(self):
        """Codex Security scans, plans, patches and opens PRs -- but Codex tasks
        perform the edits. A single modifies_code boolean derived harness."""
        self.assertEqual(
            derive_category({
                **LOOP,
                "modifies_code_directly": False,
                "delegates_code_changes": True,
            }),
            "multiplexer",
        )

    def test_non_software_domain_wins_over_support(self):
        """video-use is a skill installed into coding agents, which reads as
        support by the letter of the definition, but it produces video."""
        self.assertEqual(
            derive_category({
                **LOOP,
                "software_task_domain": False,
                "supports_coding_agents": True,
                "something_else_kind": "other",
            }),
            "something-else",
        )

    def test_coordination_without_delegation_is_not_a_multiplexer(self):
        """Section 4 has exactly six steps and step 3 is the only multiplexer
        test. An engine that also treated bare coordination as multiplexing
        returned 'multiplexer' here, contradicting section 4 and BR-009, which
        make delegation of the code-changing step the discriminator."""
        record = {
            **LOOP,
            "modifies_code_directly": False,
            "delegates_code_changes": False,
            "coordinates_external_coding_agents": True,
            "supports_coding_agents": True,
        }
        self.assertEqual(derive_category(record), "support")

    def test_coordination_flag_never_changes_any_outcome(self):
        """The field is not part of the procedure, so setting it must be inert
        on every path. If a future step reads it, this fails and the document
        has to be amended first."""
        cases = [
            {**LOOP},
            {**LOOP, "modifies_code_directly": False, "delegates_code_changes": True},
            {**LOOP, "iterates_on_results": False, "supports_coding_agents": True},
            {**LOOP, "software_task_domain": False, "something_else_kind": "model"},
            {**LOOP, "is_sdk_or_framework": True},
        ]
        for record in cases:
            with self.subTest(record=record):
                self.assertEqual(
                    derive_category(record),
                    derive_category({**record, "coordinates_external_coding_agents": True}),
                )

    def test_additive_delegation_does_not_demote_a_harness(self):
        """DeerFlow edits directly and can also delegate over ACP. Delegation is
        additive, so it stays a harness."""
        self.assertEqual(
            derive_category({
                **LOOP,
                "modifies_code_directly": True,
                "delegates_code_changes": True,
            }),
            "harness",
        )


class PublicationTest(unittest.TestCase):
    def test_shared_fixture_cases_all_agree(self):
        """The same fixture must drive lib/publication.js once Task 7 lands, so
        the Python and Node predicates cannot drift."""
        cases = json.loads((FIXTURES / "publication_cases.json").read_text())["cases"]
        self.assertTrue(cases)
        for case in cases:
            with self.subTest(case=case["name"]):
                self.assertEqual(is_public(case["record"]), case["expected_public"])

    def test_only_verified_in_scope_records_are_public(self):
        self.assertTrue(is_public({"category": "support", "classification_status": "verified"}))
        self.assertFalse(is_public({"category": "something-else", "classification_status": "verified"}))
        self.assertFalse(is_public({"category": "harness", "classification_status": "researched"}))
        self.assertFalse(is_public({"category": None, "classification_status": "unreviewed"}))


class ValidateRecordTest(unittest.TestCase):
    def test_a_complete_verified_record_passes(self):
        self.assertEqual(validate_record(VERIFIED, "agents/example.md"), [])

    def test_requires_two_distinct_reviewers(self):
        record = {**VERIFIED, "classification_reviewers": ["eden"]}
        self.assertIn(
            "agents/example.md: verified records require two distinct reviewers",
            validate_record(record, "agents/example.md"),
        )

    def test_same_reviewer_twice_is_not_two_reviewers(self):
        record = {**VERIFIED, "classification_reviewers": ["eden", "eden"]}
        self.assertIn(
            "agents/example.md: verified records require two distinct reviewers",
            validate_record(record, "agents/example.md"),
        )

    def test_stored_category_must_match_derived(self):
        record = {**VERIFIED, "category": "support"}
        self.assertIn(
            "agents/example.md: stored category support does not match derived category harness",
            validate_record(record, "agents/example.md"),
        )

    def test_verified_record_requires_a_quote(self):
        record = {**VERIFIED, "classification_quote": None}
        self.assertIn(
            "agents/example.md: verified records require a verbatim classification_quote",
            validate_record(record, "agents/example.md"),
        )

    def test_null_decisive_boolean_blocks_verification(self):
        record = {**VERIFIED, "delegates_code_changes": None}
        self.assertIn(
            "agents/example.md: verified records require delegates_code_changes "
            "to be true or false, not null",
            validate_record(record, "agents/example.md"),
        )

    def test_unknown_boundary_ruling_is_rejected(self):
        record = {**VERIFIED, "classification_boundary_ruling": "BR-042"}
        self.assertIn(
            "agents/example.md: classification_boundary_ruling 'BR-042' is not in the register",
            validate_record(record, "agents/example.md"),
        )

    def test_something_else_kind_only_on_something_else(self):
        record = {**VERIFIED, "something_else_kind": "model"}
        self.assertIn(
            "agents/example.md: something_else_kind is set but category is 'harness'",
            validate_record(record, "agents/example.md"),
        )

    def test_unreviewed_passes_lenient_and_fails_strict(self):
        record = {"category": None, "classification_status": "unreviewed"}
        self.assertEqual(validate_record(record, "agents/new.md"), [])
        self.assertIn(
            "agents/new.md: strict mode: record is not yet classified",
            validate_record(record, "agents/new.md", strict=True),
        )

    def test_missing_supports_flag_blocks_verification(self):
        """supports_coding_agents is decisive only on the step-5 path, so it is
        not in DECISIVE_FIELDS. It needs no separate check: without it the
        record derives nothing and cannot be verified."""
        record = {
            **VERIFIED,
            "category": "support",
            "modifies_code_directly": False,
        }
        record.pop("supports_coding_agents", None)
        self.assertIsNone(derive_category(record))
        self.assertIn(
            "agents/example.md: verified record's signals do not derive any category",
            validate_record(record, "agents/example.md"),
        )
        ok = {**record, "supports_coding_agents": True}
        self.assertEqual(derive_category(ok), "support")
        self.assertEqual(validate_record(ok, "agents/example.md"), [])

    def test_bad_date_is_rejected(self):
        record = {**VERIFIED, "classification_last_verified": "25-08-2026"}
        self.assertIn(
            "agents/example.md: classification_last_verified '25-08-2026' is not an ISO date",
            validate_record(record, "agents/example.md"),
        )


AUDIT_DIR = "outputs/category-audit-first-100-pass5-2026-08-24"


def _find(name: str, env: str) -> Path | None:
    """Locate a companion file that may sit outside the checkout.

    The gold set is committed under tests/fixtures/ so these pins always run,
    including on a fresh clone. The remaining candidates find the working copy
    in the parent workspace, which is where the import plan reads it from as
    `../outputs/...`. Set the env var to point somewhere else explicitly.

    A repo-only search that silently skipped was exactly the failure these
    tests exist to prevent.
    """
    override = os.environ.get(env)
    if override:
        return Path(override) if Path(override).exists() else None
    candidates = (
        FIXTURES / name,
        REPO / "docs" / "methodology" / name,
        REPO / name,
        REPO.parent / name,
        REPO.parent / AUDIT_DIR / name,
        Path.home() / "code" / AUDIT_DIR / name,
    )
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


class MethodologySyncTest(unittest.TestCase):
    """The document governs. These fail when the code drifts away from it."""

    def setUp(self):
        self.doc = _find("categorization.md", "CATEGORIZATION_MD")
        if self.doc is None:
            self.skipTest("categorization.md not found; set CATEGORIZATION_MD")

    def test_boundary_register_matches_the_methodology(self):
        text = self.doc.read_text(encoding="utf-8")
        in_doc = set(re.findall(r"^\| (BR-\d{3}) \|", text, re.MULTILINE))
        self.assertTrue(in_doc, "no rulings table found in the methodology")
        self.assertEqual(
            in_doc, set(KNOWN_RULINGS),
            "boundary register and KNOWN_RULINGS disagree; update both together",
        )

    def test_every_signal_field_the_engine_reads_is_documented(self):
        """A reviewer fills in a record from section 3. Any boolean the engine
        reads but section 3 omits is a field they cannot know to supply."""
        source = (REPO / "scripts" / "classification.py").read_text(encoding="utf-8")
        body = source.split("def derive_category", 1)[1].split("def is_public", 1)[0]
        read_by_engine = set(re.findall(r'record\.get\("([a-z_]+)"\)', body))
        read_by_engine.discard("something_else_kind")
        documented = set(re.findall(r"^\| `([a-z_]+)` \|", self.doc.read_text(encoding="utf-8"), re.MULTILINE))
        self.assertEqual(
            read_by_engine - documented, set(),
            "engine reads signal fields that categorization.md section 3 never defines",
        )


class GoldSetTest(unittest.TestCase):
    """Pins the verified audit artifact so an accidental edit is caught."""

    def setUp(self):
        self.tsv = _find("category_audit_first_100_pass5_verified.tsv", "GOLD_SET_TSV")
        if self.tsv is None:
            self.skipTest(f"gold set not found; set GOLD_SET_TSV (looked under {REPO} and {REPO.parent})")
        with open(self.tsv, newline="", encoding="utf-8") as fh:
            self.rows = list(csv.DictReader(fh, delimiter="\t"))

    def test_row_ids_are_unique_and_contiguous(self):
        ids = [r["row"] for r in self.rows]
        self.assertEqual(len(set(ids)), len(ids), "duplicate row ids; row is not a key")
        self.assertEqual(
            sorted(int(i) for i in ids), list(range(1, len(ids) + 1)),
            "row ids are not 1..N",
        )

    def test_tallies_match_the_implementation_plan(self):
        self.assertEqual(len(self.rows), 101)
        self.assertEqual(
            Counter(r["pass5_category"] for r in self.rows),
            Counter({"harness": 28, "multiplexer": 22, "support": 39, "something-else": 12}),
        )
        hundred = [r for r in self.rows if r["pass4_category"].strip() != "(not in list)"]
        self.assertEqual(len(hundred), 100)
        self.assertEqual(
            Counter(r["pass5_category"] for r in hundred),
            Counter({"harness": 27, "multiplexer": 22, "support": 39, "something-else": 12}),
        )

    def test_every_category_is_in_the_taxonomy(self):
        from scripts.classification import CATEGORIES
        bad = sorted({r["pass5_category"] for r in self.rows} - CATEGORIES)
        self.assertEqual(bad, [])

    def test_names_are_distinct(self):
        names = [r["name"].strip() for r in self.rows]
        self.assertEqual(len(set(names)), len(names))


if __name__ == "__main__":
    unittest.main()
