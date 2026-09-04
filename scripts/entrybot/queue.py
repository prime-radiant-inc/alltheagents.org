"""Which open issues are waiting for the bot."""
import re

KIND_LABELS = {"new-entry": "add", "correction": "fix"}
KIND_PREFIXES = {"Add:": "add", "Fix:": "fix"}
SKIP_LABEL = "needs-info"
BRANCH_RE = re.compile(r"^issue-(\d+)-")


def issue_kind(labels, title):
    for label in labels:
        if label in KIND_LABELS:
            return KIND_LABELS[label]
    for prefix, kind in KIND_PREFIXES.items():
        if (title or "").startswith(prefix):
            return kind
    return None


def waiting(issues, open_prs):
    """Issues from the two forms that have no needs-info label and no open
    PR on an `issue-<N>-...` branch. Returns [(number, kind, title)] by number."""
    claimed = set()
    for pr in open_prs:
        m = BRANCH_RE.match(pr.get("headRefName") or "")
        if m:
            claimed.add(int(m.group(1)))
    out = []
    for issue in issues:
        labels = [l["name"] for l in issue.get("labels", [])]
        kind = issue_kind(labels, issue.get("title"))
        if kind is None or SKIP_LABEL in labels or issue["number"] in claimed:
            continue
        out.append((issue["number"], kind, issue.get("title") or ""))
    return sorted(out)
