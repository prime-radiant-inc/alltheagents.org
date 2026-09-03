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
