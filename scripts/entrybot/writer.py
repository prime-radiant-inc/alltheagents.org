"""Write entry files, ledger rows, and maker records in the repo's exact format."""
import json
import re
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


def scalar_problems(values):
    """Problems for string values that would break frontmatter: newlines,
    carriage returns, or backslashes."""
    problems = []
    for key, val in values.items():
        if isinstance(val, str) and any(c in val for c in ("\n", "\r", "\\")):
            problems.append(f"{key} contains a newline or backslash")
    return problems


def validate_slug(slug):
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", slug):
        raise ValueError(f"invalid slug: {slug!r}")


def validate_entry(entry):
    problems = [f"required entry field blank: {k}" for k in ENTRY_REQUIRED if not entry.get(k)]
    problems += enum_problems(entry)
    problems += scalar_problems(entry)
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
    return json.dumps(rows, ensure_ascii=True, indent=2)


def dump_makers(makers):
    return json.dumps(makers, ensure_ascii=True, indent=2) + "\n"


def write_entry(repo, verified, today=None):
    """Create agents/<slug>.md plus ledger and maker updates. Returns touched paths.

    Every file's new contents are built first and written last, so a
    validation failure leaves the repo untouched.
    """
    today = today or date.today().isoformat()
    slug = verified["slug"]
    validate_slug(slug)
    entry = {**DEFAULTS, **verified["entry"]}
    entry["slug"] = slug
    entry["last_verified"] = today
    problems = validate_entry(entry)
    if not (verified.get("body") or "").strip():
        problems.append("body (narrative) is empty")
    if not (verified.get("rationale") or "").strip():
        problems.append("rationale is empty")
    if problems:
        raise ValueError("\n".join(problems))

    path = repo.agents_dir / f"{slug}.md"
    if path.exists():
        raise FileExistsError(f"entry already exists: {path}")

    writes = {path: render_entry(entry, verified["body"])}

    row = {"slug": slug, "name": ledger_cell(entry["name"]), "category": entry["category"],
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
    validate_slug(slug)
    path = repo.agents_dir / f"{slug}.md"
    if not path.exists():
        raise FileNotFoundError(f"no entry: {path}")
    changes = dict(verified.get("entry") or {})
    problems = enum_problems(changes, new_entry=False)
    problems += scalar_problems(changes)
    unknown = sorted(set(changes) - set(FIELD_ORDER))
    if unknown:
        problems.append(f"unknown entry fields: {unknown}")
    for key in LIST_FIELDS:
        if key in changes:
            value = changes[key]
            if value is not None and not isinstance(value, list):
                problems.append(f"{key} must be a list: {value!r}")
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
