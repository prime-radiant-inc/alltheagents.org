"""Every external call: subprocess (git, gh, npx, python) and HTTP.

Tests patch `run` and `http_ok`; nothing else in the package touches the
network or a subprocess directly.
"""
import json
import subprocess
import urllib.error
import urllib.request

USER_AGENT = "alltheagents-entry-bot"


def run(args, input=None, cwd=None):
    """Run a command, return stdout. Raise RuntimeError with stderr on failure."""
    proc = subprocess.run(args, input=input, capture_output=True, text=True, cwd=cwd)
    if proc.returncode != 0:
        raise RuntimeError(f"{' '.join(str(a) for a in args)} failed:\n{proc.stderr.strip()}")
    return proc.stdout


def http_ok(url, timeout=10):
    """True when the URL answers 2xx or 3xx (redirects are followed)."""
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return 200 <= resp.status < 400
        except urllib.error.HTTPError as err:
            if method == "GET":
                return 200 <= err.code < 400
        except Exception:
            if method == "GET":
                return False
    return False


def gh_json(args):
    return json.loads(run(["gh", *args]))


def issue_view(number):
    return gh_json(["issue", "view", str(number), "--json",
                    "number,title,body,labels,author,url,comments"])


# gh caps list output; 500 is far above this repo's open-issue and open-PR
# counts. Raise it if `list` ever seems to miss issues.
LIST_LIMIT = "500"


def issue_list():
    """Open issues: number, title, label names."""
    return gh_json(["issue", "list", "--state", "open", "--limit", LIST_LIMIT,
                    "--json", "number,title,labels"])


def pr_list():
    """Open pull requests: number, head branch name."""
    return gh_json(["pr", "list", "--state", "open", "--limit", LIST_LIMIT,
                    "--json", "number,headRefName"])


def issue_comment(number, body_file):
    run(["gh", "issue", "comment", str(number), "--body-file", str(body_file)])


def ensure_label(name, color="d4c5f9", description=""):
    names = {l["name"] for l in gh_json(["label", "list", "--limit", "200", "--json", "name"])}
    if name not in names:
        run(["gh", "label", "create", name, "--color", color, "--description", description])


def add_label(number, name):
    run(["gh", "issue", "edit", str(number), "--add-label", name])


def remote_branch_exists(remote, branch):
    return bool(run(["git", "ls-remote", "--heads", remote, branch]).strip())


def pr_create(title, body_file, base, head):
    return run(["gh", "pr", "create", "--base", base, "--head", head,
                "--title", title, "--body-file", str(body_file)]).strip()
