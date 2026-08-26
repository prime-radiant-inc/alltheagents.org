"""Category derivation, publication eligibility, and record validation.

This module is the executable form of docs/methodology/categorization.md. If the
two ever disagree, that is a bug: the document governs and this file is wrong.
The regression fixtures in tests/test_classification.py exist to catch drift.
"""

from __future__ import annotations

import re
from datetime import date
from urllib.parse import urlparse

CATEGORIES = {"harness", "multiplexer", "support", "something-else"}
PUBLIC_CATEGORIES = {"harness", "multiplexer", "support"}
STATUSES = {"unreviewed", "researched", "verified", "disputed"}
CONFIDENCE = {"high", "medium", "low"}
SOURCE_QUALITY = {"primary-current", "primary-stale", "mixed", "secondary-only"}
SOMETHING_ELSE_KINDS = {
    "model", "dataset", "tutorial", "course",
    "general-application", "non-coding-agent", "other",
}

LOOP_FIELDS = (
    "accepts_software_task",
    "chooses_next_action",
    "uses_tools",
    "modifies_code_directly",
    "iterates_on_results",
)
# Booleans required on EVERY verified record, whichever path it takes through
# the procedure. Leaving one null means the derivation rests on a guess.
DECISIVE_FIELDS = LOOP_FIELDS + (
    "software_task_domain",
    "is_sdk_or_framework",
    "delegates_code_changes",
)
# Decisive only on the step-5 path, so it is not required of a harness or a
# multiplexer. It needs no separate check: a record that reaches step 5 without
# it derives None, and validate_record() rejects that. See the regression test
# test_missing_supports_flag_blocks_verification.
PATH_SPECIFIC_FIELDS = ("supports_coding_agents",)

BOUNDARY_RULING_RE = re.compile(r"^BR-\d{3}$")
# Mirrors the "Rulings in force" table in docs/methodology/categorization.md
# section 10. Listed explicitly rather than generated from a range so that
# adding a ruling is a visible edit here as well as in the document;
# test_boundary_register_matches_the_methodology fails if the two drift.
KNOWN_RULINGS = frozenset({
    "BR-001",  # named unit is an SDK, library or framework -> support
    "BR-002",  # owns a loop but never modifies project code -> support
    "BR-003",  # brand spans a model and a product -> classify the product
    "BR-004",  # discontinued/archived/acquired -> keep the capability category
    "BR-005",  # template, prompt pack or method -> support
    "BR-006",  # task domain is not software -> something-else
    "BR-007",  # general-purpose agent that can also code -> something-else
    "BR-008",  # no-code platform for building agents -> support
    "BR-009",  # wrapper delegating the code-changing step -> multiplexer
})


def derive_category(record: dict) -> str | None:
    """Apply the ordered decision procedure. Returns None if undecidable.

    Order is load-bearing; see categorization.md section 4.
    """
    # 1. Domain gate (BR-006). Distinct from accepts_software_task: a pentest
    #    agent accepts a task and may drive coding agents, but its domain is
    #    security, not software construction.
    if record.get("software_task_domain") is False:
        return "something-else"

    # 2. SDK rule (BR-001). Nominal test beats the functional one for this
    #    class, even when the package ships a runnable complete loop.
    if record.get("is_sdk_or_framework") is True:
        return "support"

    # 3. Delegation test (BR-009). Precedes loop ownership because a delegating
    #    product can satisfy every other loop signal while never editing code.
    if (
        record.get("delegates_code_changes") is True
        and record.get("modifies_code_directly") is not True
    ):
        return "multiplexer"

    # 4. Loop ownership.
    if all(record.get(f) is True for f in LOOP_FIELDS):
        return "harness"

    # 5. Material support (BR-002): owns a loop but never modifies code.
    #    There is deliberately no "coordinates other agents" step here. Step 3
    #    is the only multiplexer test, because BR-009 makes delegation of the
    #    code-changing step -- not coordination as such -- the discriminator.
    if record.get("supports_coding_agents") is True:
        return "support"

    # 6. Otherwise.
    if record.get("something_else_kind") in SOMETHING_ELSE_KINDS:
        return "something-else"
    return None


def is_public(record: dict) -> bool:
    """Publication eligibility. Mirrored in lib/publication.js -- keep in sync
    via tests/fixtures/publication_cases.json."""
    return (
        record.get("classification_status") == "verified"
        and record.get("category") in PUBLIC_CATEGORIES
    )


def _valid_url(value) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _nonempty(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_record(record: dict, path: str, strict: bool = False) -> list[str]:
    """Return every problem with this record. Empty list means valid."""
    errors: list[str] = []

    def err(message: str) -> None:
        errors.append(f"{path}: {message}")

    category = record.get("category")
    status = record.get("classification_status")

    # --- closed enums -------------------------------------------------------
    if category is not None and category not in CATEGORIES:
        err(f"category {category!r} is not one of {sorted(CATEGORIES)}")
    if status not in STATUSES:
        err(f"classification_status {status!r} is not one of {sorted(STATUSES)}")
    for field, allowed in (
        ("classification_confidence", CONFIDENCE),
        ("classification_source_quality", SOURCE_QUALITY),
        ("something_else_kind", SOMETHING_ELSE_KINDS),
    ):
        value = record.get(field)
        if value is not None and value not in allowed:
            err(f"{field} {value!r} is not one of {sorted(allowed)}")

    ruling = record.get("classification_boundary_ruling")
    if ruling is not None:
        if not BOUNDARY_RULING_RE.match(str(ruling)):
            err(f"classification_boundary_ruling {ruling!r} is not a BR-nnn identifier")
        elif ruling not in KNOWN_RULINGS:
            err(f"classification_boundary_ruling {ruling!r} is not in the register")

    # --- exclusion kind belongs only to something-else ----------------------
    kind = record.get("something_else_kind")
    if category == "something-else":
        if status == "verified" and kind not in SOMETHING_ELSE_KINDS:
            err("verified something-else records require a something_else_kind")
    elif kind is not None:
        err(f"something_else_kind is set but category is {category!r}")

    # --- unreviewed ---------------------------------------------------------
    if category is None:
        if status not in {"unreviewed", "researched", "disputed"}:
            err(f"category is null but classification_status is {status!r}")
        if strict:
            err("strict mode: record is not yet classified")
        return errors

    if status != "verified":
        if strict:
            err(f"strict mode: classification_status is {status!r}, not verified")
        return errors

    # --- everything below applies to verified records only ------------------
    for field in DECISIVE_FIELDS:
        if record.get(field) is None:
            err(f"verified records require {field} to be true or false, not null")

    derived = derive_category(record)
    if derived is None:
        err("verified record's signals do not derive any category")
    elif derived != category:
        err(f"stored category {category} does not match derived category {derived}")

    evidence = record.get("classification_evidence") or []
    if not isinstance(evidence, list) or not any(_valid_url(u) for u in evidence):
        err("verified records require at least one http(s) evidence URL")

    if not _nonempty(record.get("classification_quote")):
        err("verified records require a verbatim classification_quote")
    if not _valid_url(record.get("classification_quote_source")):
        err("verified records require a valid classification_quote_source URL")

    if not _nonempty(record.get("classification_rationale")):
        err("verified records require a classification_rationale")
    if not _nonempty(record.get("classification_counterevidence")):
        err("verified records require classification_counterevidence")

    if record.get("classification_confidence") is None:
        err("verified records require a classification_confidence")
    if record.get("classification_source_quality") is None:
        err("verified records require a classification_source_quality")

    reviewers = record.get("classification_reviewers") or []
    if not isinstance(reviewers, list) or len({r for r in reviewers if _nonempty(r)}) < 2:
        err("verified records require two distinct reviewers")

    verified_on = record.get("classification_last_verified")
    if verified_on is None:
        err("verified records require a classification_last_verified date")
    else:
        try:
            date.fromisoformat(str(verified_on))
        except ValueError:
            err(f"classification_last_verified {verified_on!r} is not an ISO date")

    return errors
