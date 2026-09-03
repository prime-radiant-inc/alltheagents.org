#!/usr/bin/env python3
"""Turn an issue form into an entry PR. See docs/issue-to-pr.md for the procedure.

Subcommands, in the order a run uses them:
  fetch N        gh issue -> work/issue-N/issue.json
  check FILE     pre-flight on issue.json (exit 1 on any problem)
  write FILE     verified.json -> new entry + ledger + makers + regen
  apply-fix FILE verified.json -> edited entry (+ ledger) + regen
  check --built FILE   eleventy build + page rendered -> work/issue-N/built.ok
  pr N           branch, commit, push, open PR
  reject N --reason-file F   comment + needs-info label, no PR
  regen          rebuild _data/agents.json
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from entrybot import checks, forms, gh, publish, writer  # noqa: E402
from entrybot.repo import Repo  # noqa: E402

TEMPLATES = {"add": ROOT / ".github/ISSUE_TEMPLATE/add-agent.yml",
             "fix": ROOT / ".github/ISSUE_TEMPLATE/update-agent.yml"}
KIND_LABELS = {"new-entry": "add", "correction": "fix"}
KIND_PREFIXES = {"Add:": "add", "Fix:": "fix"}


def work_dir(number):
    d = ROOT / "work" / f"issue-{number}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def fail(lines):
    for line in lines:
        print(line, file=sys.stderr)
    sys.exit(1)


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save(path, data):
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {Path(path).relative_to(ROOT)}")


def detect_kind(labels, title, explicit):
    if explicit:
        return explicit
    for label in labels:
        if label in KIND_LABELS:
            return KIND_LABELS[label]
    for prefix, kind in KIND_PREFIXES.items():
        if (title or "").startswith(prefix):
            return kind
    return None


def cmd_fetch(args):
    repo = Repo(ROOT)
    if args.body_file:
        raw = {"number": args.number, "title": args.title or "", "body": Path(args.body_file).read_text(encoding="utf-8"),
               "labels": [], "author": {"login": "local"}, "url": ""}
    else:
        raw = gh.issue_view(args.number)
    labels = [l["name"] for l in raw.get("labels", [])]
    kind = detect_kind(labels, raw.get("title"), args.kind)
    if kind is None:
        fail([f"cannot tell add from fix: labels={labels} title={raw.get('title')!r}; pass --kind"])
    issue = {"number": raw["number"], "kind": kind, "title": raw.get("title"),
             "author": (raw.get("author") or {}).get("login"), "url": raw.get("url")}
    if kind == "add":
        issue["fields"] = forms.parse_add(raw["body"], TEMPLATES["add"])
    else:
        parsed = forms.parse_fix(raw["body"], TEMPLATES["fix"])
        issue.update(parsed)
        candidates = repo.resolve_entry(parsed["fields"].get("entry"))
        issue["slug"] = candidates[0] if len(candidates) == 1 else None
        issue["slug_candidates"] = candidates
    save(work_dir(args.number) / "issue.json", issue)


def cmd_check(args):
    repo = Repo(ROOT)
    data = load(args.file)
    if args.built:
        problems = checks.check_built(repo, data["slug"])
        if problems:
            fail(problems)
        (work_dir(data["number"]) / "built.ok").write_text("ok\n")
        print("build ok; page rendered; slug in agents.json")
        return
    if data["kind"] == "add":
        url_ok = (lambda url: True) if args.offline else None
        problems, warnings = checks.check_add(data["fields"], repo, url_ok=url_ok), []
    else:
        problems, warnings = checks.check_fix(data, repo)
    for w in warnings:
        print(f"warning: {w}")
    if problems:
        fail(problems)
    print("check ok")


def cmd_write(args):
    repo = Repo(ROOT)
    verified = load(args.file)
    try:
        touched = writer.write_entry(repo, verified)
    except (ValueError, FileExistsError) as err:
        fail(str(err).splitlines())
    finish_write(verified, touched)


def cmd_apply_fix(args):
    repo = Repo(ROOT)
    verified = load(args.file)
    try:
        touched = writer.apply_fix(repo, verified)
    except (ValueError, FileNotFoundError) as err:
        fail(str(err).splitlines())
    finish_write(verified, touched)


def finish_write(verified, touched):
    try:
        cmd_regen(None)
    except RuntimeError as err:
        fail(str(err).splitlines())
    rel = [str(p.relative_to(ROOT)) for p in touched] + ["_data/agents.json"]
    save(work_dir(verified["number"]) / "touched.json", rel)


def cmd_regen(args):
    print(gh.run([sys.executable, str(ROOT / "scripts/generate_json_from_md.py")]).strip())


def cmd_pr(args):
    d = work_dir(args.number)
    url = publish.pr(Repo(ROOT), load(d / "issue.json"), load(d / "verified.json"),
                     load(d / "touched.json"), d, base=args.base)
    print(url)


def cmd_reject(args):
    publish.reject(args.number, Path(args.reason_file))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("fetch"); s.add_argument("number", type=int)
    s.add_argument("--body-file"); s.add_argument("--kind", choices=["add", "fix"]); s.add_argument("--title")
    s.set_defaults(fn=cmd_fetch)

    s = sub.add_parser("check"); s.add_argument("file")
    s.add_argument("--offline", action="store_true", help="skip the URL reachability check")
    s.add_argument("--built", action="store_true", help="run eleventy and confirm the page rendered")
    s.set_defaults(fn=cmd_check)

    s = sub.add_parser("write"); s.add_argument("file"); s.set_defaults(fn=cmd_write)
    s = sub.add_parser("apply-fix"); s.add_argument("file"); s.set_defaults(fn=cmd_apply_fix)
    s = sub.add_parser("regen"); s.set_defaults(fn=cmd_regen)

    s = sub.add_parser("pr"); s.add_argument("number", type=int)
    s.add_argument("--base", default="main"); s.set_defaults(fn=cmd_pr)

    s = sub.add_parser("reject"); s.add_argument("number", type=int)
    s.add_argument("--reason-file", required=True); s.set_defaults(fn=cmd_reject)

    args = p.parse_args(argv)
    args.fn(args)


if __name__ == "__main__":
    main()
