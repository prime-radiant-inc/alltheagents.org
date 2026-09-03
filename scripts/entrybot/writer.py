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
    for key in LIST_FIELDS:
        val = entry.get(key)
        if val is not None and not isinstance(val, list):
            problems.append(f"{key} must be a list: {val!r}")
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
