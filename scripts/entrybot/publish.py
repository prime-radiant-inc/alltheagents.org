"""Open the PR or post the rejection comment. All GitHub access via gh."""
from . import gh

FOOTER = "Opened by the issue-to-PR runbook (`docs/issue-to-pr.md`)."


def _display(value):
    if value is None:
        return "—"
    if isinstance(value, list):
        return ", ".join(str(v) for v in value) or "—"
    return str(value).replace("|", "\\|").replace("\n", " ")


def build_pr_body(issue, verified):
    number = issue["number"]
    kind = issue["kind"]
    slug = verified["slug"]
    name = (verified.get("entry") or {}).get("name") or (issue.get("fields") or {}).get("name") or slug
    form = "Add an entry" if kind == "add" else "Fix an entry"
    verb = "Adds" if kind == "add" else "Updates"
    author = issue.get("author") or "unknown"

    lines = [
        "## What does this change?", "",
        f"{verb} the entry for **{name}** (`agents/{slug}.md`) from issue #{number}.", "",
        "## Why?", "",
        f"Submitted through the \"{form}\" form by @{author}. Every field below was checked against the linked source.", "",
        "## How did you test it?", "",
        "`python3 scripts/entry_bot.py check --built` passed: the Eleventy build succeeded, the page rendered, and the slug is in the built search index.", "",
        "## Verification", "",
        "| Field | Submitted | Verified | Evidence |", "|---|---|---|---|",
    ]
    evidence = verified.get("evidence") or {}
    for field, ev in evidence.items():
        lines.append(f"| {field} | {_display(ev.get('submitted'))} | {_display(ev.get('verified'))} | {_display(ev.get('source'))} |")
    if not evidence:
        lines.append("| — | — | — | — |")

    discrepancies = [(f, ev) for f, ev in evidence.items() if ev.get("submitted") != ev.get("verified")]
    if discrepancies:
        lines += ["", "## Discrepancies", ""]
        for field, ev in discrepancies:
            note = f" {ev['note']}" if ev.get("note") else ""
            lines.append(f"- **{field}**: submitted {_display(ev.get('submitted'))}, verified {_display(ev.get('verified'))}.{note}")

    not_applied = verified.get("not_applied") or []
    if not_applied:
        lines += ["", "## Not applied", ""]
        for item in not_applied:
            lines.append(f"- **{item['field']}** -> {_display(item.get('new'))}: {item.get('reason', 'source did not support it')}")

    lines += ["", f"Closes #{number}", "", FOOTER, ""]
    return "\n".join(lines)


def _remote(root):
    names = gh.run(["git", "remote"], cwd=root).split()
    if not names:
        raise RuntimeError("no git remote configured")
    return "origin" if "origin" in names else names[0]


def _local_branch_exists(root, branch):
    try:
        gh.run(["git", "rev-parse", "--verify", "--quiet", f"refs/heads/{branch}"], cwd=root)
        return True
    except RuntimeError:
        return False


def pr(repo, issue, verified, touched, work, base="main"):
    number = issue["number"]
    slug = verified["slug"]
    kind = issue["kind"]
    if not (work / "built.ok").exists():
        raise RuntimeError("refusing to open a PR: run `check --built` first")
    branch = f"issue-{number}-{slug}" if kind == "add" else f"issue-{number}-fix-{slug}"
    remote = _remote(repo.root)
    if gh.remote_branch_exists(remote, branch):
        raise RuntimeError(f"branch already exists on {remote}: {branch}")
    if _local_branch_exists(repo.root, branch):
        raise RuntimeError(
            f"local branch already exists from a previous run: {branch}; "
            f"push it or delete it with `git branch -D {branch}`"
        )

    name = (verified.get("entry") or {}).get("name") or slug
    title = f"{'Add' if kind == 'add' else 'Fix'} entry: {name} (#{number})"
    body_file = work / "pr-body.md"
    body_file.write_text(build_pr_body(issue, verified), encoding="utf-8")
    recover_cmd = (f"gh pr create --base {base} --head {branch} "
                   f'--title "{title}" --body-file {body_file}')

    start = gh.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo.root).strip()
    committed = False
    pushed = False
    try:
        gh.run(["git", "checkout", "-b", branch], cwd=repo.root)
        gh.run(["git", "add", "--", *touched], cwd=repo.root)
        gh.run(["git", "commit", "-m", title], cwd=repo.root)
        committed = True
        gh.run(["git", "push", "-u", remote, branch], cwd=repo.root)
        pushed = True
        url = gh.pr_create(title, body_file, base, branch)
    except Exception:
        gh.run(["git", "checkout", start], cwd=repo.root)
        if not committed:
            try:
                gh.run(["git", "branch", "-D", branch], cwd=repo.root)
            except Exception:
                pass
            raise
        if not pushed:
            raise RuntimeError(
                f"commit is on local branch {branch} but was not pushed; the "
                f"working tree is back on {start}. Recover manually with: "
                f"git push -u {remote} {branch} && {recover_cmd}"
            )
        raise RuntimeError(
            f"pushed branch {branch} to {remote} but failed to open the PR; "
            f"the branch and commit are on the remote with no PR. "
            f"Recover manually with: {recover_cmd}"
        )
    gh.run(["git", "checkout", start], cwd=repo.root)
    return url


def reject(number, reason_file):
    reason = reason_file.read_text(encoding="utf-8")
    first_line = reason.strip().splitlines()[0] if reason.strip() else ""
    if not first_line:
        raise RuntimeError("reason file is empty")
    existing = gh.issue_view(number).get("comments") or []
    for c in existing:
        body = (c.get("body") or "").strip()
        if body.splitlines() and body.splitlines()[0] == first_line:
            print(f"a comment starting with the same line already exists on #{number}; not posting again")
            return
    gh.issue_comment(number, reason_file)
    gh.ensure_label("needs-info", description="Issue form needs more information before a PR can be opened")
    gh.add_label(number, "needs-info")
    print(f"commented on #{number} and added needs-info")
