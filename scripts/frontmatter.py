"""Read and write YAML frontmatter in agents/*.md records.

update_record() is surgical: it rewrites only the keys you name and leaves every
other byte of the file alone, so a classification commit diffs as the handful of
lines it actually changed. A full re-emit through yaml.safe_dump would rewrite
all 1,164 records -- they quote their scalars and safe_dump does not -- and bury
the real change in formatting noise.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterator

import yaml

DELIMITER = "---\n"
TEMPLATE_NAME = "_TEMPLATE.md"


def _split(text: str, path) -> tuple[str, str]:
    """Split a record into (frontmatter_text, body).

    Splits on a line that is *exactly* `---`, not on the substring. Splitting on
    the substring truncated the frontmatter at the first comment line ending in
    `---` -- `# --- identity ---` in agents/_TEMPLATE.md does it -- and the
    truncation was silent: yaml.safe_load() saw only comments, returned None,
    and read_record() handed back an empty dict with the real frontmatter
    reclassified as body.
    """
    if not text.startswith(DELIMITER):
        raise ValueError(f"{path}: missing YAML frontmatter")
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i] == "---":
            fm = "\n".join(lines[1:i])
            if i > 1:
                fm += "\n"
            return fm, "\n".join(lines[i + 1:])
    raise ValueError(f"{path}: unterminated YAML frontmatter")


def read_record(path: Path) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Raises ValueError on malformed records."""
    text = Path(path).read_text(encoding="utf-8")
    fm_text, body = _split(text, path)
    data = yaml.safe_load(fm_text) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path}: frontmatter must be a mapping")
    return data, body.lstrip("\n")


def iter_record_paths(agents_dir: Path) -> Iterator[Path]:
    """Every canonical record, sorted, excluding the template."""
    yield from sorted(
        p for p in Path(agents_dir).glob("*.md") if p.name != TEMPLATE_NAME
    )


def _emit_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    # Quote unless it is unambiguously a plain scalar, so a value like "no" or
    # "1.0" cannot be re-parsed as a bool or a number on the next read.
    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 ._/-]*", text) and not re.fullmatch(
        r"(?i:true|false|null|yes|no|on|off|~)|[-+]?[0-9.]+", text
    ):
        return text
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _render(key: str, value: Any) -> list[str]:
    if isinstance(value, list):
        if not value:
            return [f"{key}: []"]
        return [f"{key}:"] + [f"  - {_emit_scalar(v)}" for v in value]
    return [f"{key}: {_emit_scalar(value)}"]


def update_record(path: Path, updates: dict) -> bool:
    """Set the given keys in place, preserving every other byte.

    Existing keys are replaced where they sit; new keys are appended to the end
    of the frontmatter block. Returns True if the file changed on disk.
    """
    path = Path(path)
    original = path.read_text(encoding="utf-8")
    fm_text, body = _split(original, path)
    lines = fm_text.split("\n")

    current = yaml.safe_load(fm_text) or {}
    # Skip keys whose value is already correct. Without this a "no-op" update
    # still rewrites the line and changes its quoting style, which would churn
    # every record in the corpus on the first classification run.
    pending = {
        k: v for k, v in updates.items()
        if not (k in current and current[k] == v and type(current[k]) is type(v))
    }
    if not pending:
        return False

    for key, value in pending.items():
        # A top-level key: at column 0, plus any indented continuation lines.
        start = None
        for i, line in enumerate(lines):
            if re.match(rf"^{re.escape(key)}\s*:", line):
                start = i
                break
        replacement = _render(key, value)
        if start is None:
            while lines and lines[-1].strip() == "":
                lines.pop()
            lines.extend(replacement)
            lines.append("")
            continue
        end = start + 1
        if re.match(rf"^{re.escape(key)}\s*:\s*[|>][-+0-9]*\s*$", lines[start]):
            # Block scalar: the value runs until the next line at column 0.
            # Blank lines are part of the block, so the "stop on blank" rule
            # used for plain values would orphan everything after one.
            while end < len(lines):
                line = lines[end]
                if line.strip() and not line.startswith((" ", "\t")):
                    break
                end += 1
            while end > start + 1 and not lines[end - 1].strip():
                end -= 1  # leave trailing blank lines where they were
        else:
            while end < len(lines) and (
                lines[end].startswith((" ", "\t", "-")) and lines[end].strip()
            ):
                end += 1
        lines[start:end] = replacement

    updated = DELIMITER + "\n".join(lines) + DELIMITER + body
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True
