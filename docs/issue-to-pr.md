# Processing an issue into a pull request

This is the procedure for turning one filled-in issue form into one pull
request. It is written for a coding agent that has never seen this repo. A
human can follow it too. Read it top to bottom before starting.

You run `python3 scripts/entry_bot.py <subcommand>` for every mechanical
step. Your own work is research: confirm every claim against a primary
source, then write down what you found. You never hand-edit
`CATEGORIZATION_LEDGER.md`, `scripts/categorization_ledger.json`,
`_data/makers.json`, or `_data/agents.json`. The script owns them.

## Preconditions

```bash
gh auth status          # must succeed; the script pushes and opens PRs with this login
git status --short      # must be empty
git checkout main && git pull
npm ci                  # once per checkout; the build check needs eleventy
python3 -m unittest scripts/tests/test_entry_bot.py   # must pass
```

Everything the run produces lives in `work/issue-<N>/` (gitignored).

## 1. Fetch and check

```bash
python3 scripts/entry_bot.py fetch <N>
python3 scripts/entry_bot.py check work/issue-<N>/issue.json
```

`fetch` writes `issue.json`: the form fields keyed by id, plus `kind`
(`add` or `fix`). `check` exits non-zero with one line per problem. If it
fails, skip to step 5 and use its output as the reason. Warnings
(`warning:` lines) do not stop you, but mention them in the PR body's
notes.

Read `agents/_TEMPLATE.md` now. It defines every frontmatter key and the
meaning of `null` versus `"False"`.

## 2. Research an add issue

Open `work/issue-<N>/issue.json`. For every field below, find the value
in the named source. Write what you found to
`work/issue-<N>/verified.json` in the shape shown at the end of this
section.

| Field | Confirm from | Rule |
|-------|-------------|------|
| `url`, `homepage`, `docs_url` | Load each page | It must load and be about this product. Any other outcome is a reject. |
| `source_code_url`, `source_available` | The repo exists and is public | Blank in the form means closed source: `source_available: false`. |
| `license` | `gh api repos/{owner}/{repo} --jq .license.spdx_id`, else the LICENSE file, else the pricing page | `Proprietary` when nothing is published. `NOASSERTION` from the API means read the LICENSE file. |
| `stars`, `language` | Same API call (`.stargazers_count`, `.language`) | Non-GitHub: `null`. |
| `first_released` | Earliest of: first release, first tag, repo `created_at`, an announced launch date | `gh api repos/{o}/{r}/releases --jq 'last.published_at'`; `gh api repos/{o}/{r} --jq .created_at`. |
| `current_release` | Latest release `published_at`, else latest tag, else `pushed_at` | `gh api repos/{o}/{r}/releases/latest --jq .published_at`. |
| `maintained` | Dates above, plus `.archived` | `active` if pushed within 6 months; `dormant` within 18; `dead` beyond that or archived. `acquired` / `renamed` only with a source that says so. |
| `maker` | Repo owner, or the company on the site's footer or about page | First look for an existing key in `_data/makers.json` (keys are lowercase slugs; match on `name` too). If none, choose a lowercase slug and supply `maker_record`. `maker_type` is `individual`, `company`, or `community`; `gh api users/{owner} --jq .type` says `User` or `Organization`. |
| `category` | The README or product page | Apply the test in `README.md`: with the host tool removed, does this still run a coding task end to end? Yes: `agent`. Runs or coordinates other agents: `multiplexer`. Ships primitives but no agent: `agent-sdk`. Otherwise `other`. Disagreeing with the submitter is a discrepancy, not a reject. Write a one-sentence rationale of your own if you change the category. |
| `platforms`, `mcp_support`, `plugin_support`, `subagents`, `hooks`, `plan_mode`, `model_providers`, `pricing`, `install_method` | The docs or README | Confirmed present: `true`. Confirmed absent: `false`. Not confirmed: `null`. Never guess. `pricing` is one of `free`, `freemium`, `subscription`, `usage`, `BYOK`. |
| `what_makes_it_special`, narrative | The submission, edited | Light edits for house style only: one or two sentences for the first, about a paragraph for the narrative, no sentence repeated between them, and nothing the sources do not support. Remove claims you could not confirm rather than softening them. |

Fill `evidence` for every field you looked at, including the ones that
matched. `submitted` is the form's value, `verified` is yours, `source` is
the URL that settles it, and `note` says why they differ when they do.

Reject at this step only when you cannot confirm that the product exists
and does what the issue says it does.

`work/issue-<N>/verified.json`:

```json
{
  "number": 12,
  "kind": "add",
  "slug": "foo-agent",
  "entry": {
    "name": "Foo Agent",
    "category": "agent",
    "maker": "foo-inc",
    "license": "Apache-2.0",
    "url": "https://foo.dev",
    "source_code_url": "https://github.com/foo-inc/foo-agent",
    "source_available": true,
    "homepage": null,
    "docs_url": null,
    "install_method": null,
    "platforms": ["CLI"],
    "autonomy_level": ["agentic"],
    "language": "Rust",
    "first_released": "2025-03-01",
    "current_release": "2026-08-20",
    "maintained": "active",
    "mcp_support": true,
    "plugin_support": false,
    "subagents": null,
    "hooks": true,
    "plan_mode": null,
    "model_providers": "Ollama, OpenAI",
    "pricing": "BYOK",
    "stars": 1234,
    "what_makes_it_special": "Runs entirely offline against local models."
  },
  "body": "Foo Agent started as ... (the narrative paragraph)",
  "rationale": "A terminal agent that drives its own prompt-model-tool loop and edits files directly.",
  "maker_record": {
    "name": "Foo Inc",
    "maker_type": "company",
    "country": null,
    "makes_models": false,
    "revenue_model": [],
    "website": "https://foo.dev"
  },
  "evidence": {
    "license": {"submitted": null, "verified": "Apache-2.0", "source": "https://github.com/foo-inc/foo-agent/blob/main/LICENSE", "note": "not given in the form; LICENSE file is Apache-2.0"},
    "category": {"submitted": "agent", "verified": "agent", "source": "https://github.com/foo-inc/foo-agent#readme", "note": ""}
  }
}
```

`slug` comes from the name: lowercase, non-alphanumerics dropped, spaces
to hyphens (`check` already confirmed it is free). `maker_record` is
`null` when the maker key already exists. Keys you leave out of `entry`
are written as `null`.

## 3. Research a fix issue

`issue.json` has `slug`, `changes` (one object per `field: old -> new`
line), `unparsed` (lines that did not fit that pattern; read them, they
may be a change written loosely), and `fields.source`.

For each change open the cited source and confirm the new value using the
rules in the table above. A change the source does not support goes in
`not_applied` with a one-line reason, not in `entry`. If no change
survives, go to step 5.

`work/issue-<N>/verified.json`:

```json
{
  "number": 13,
  "kind": "fix",
  "slug": "cline",
  "entry": {"license": "MIT", "maintained": "dormant"},
  "body": null,
  "rationale": null,
  "not_applied": [{"field": "pricing", "new": "free", "reason": "pricing page still lists paid tiers"}],
  "evidence": {
    "license": {"submitted": "MIT", "verified": "MIT", "source": "https://github.com/cline/cline/blob/main/LICENSE", "note": ""}
  }
}
```

`entry` holds only the keys that change. `body` is the full new
narrative only when the narrative changes. `rationale` is required when
`category` is in `entry`.

## 4. Write, build, open the PR

```bash
python3 scripts/entry_bot.py write work/issue-<N>/verified.json        # add
python3 scripts/entry_bot.py apply-fix work/issue-<N>/verified.json    # fix
python3 scripts/entry_bot.py check --built work/issue-<N>/verified.json
git diff --stat                                                        # look at it
python3 scripts/entry_bot.py pr <N>
```

`write` refuses to overwrite an existing entry and rejects values outside
the enums. `check --built` runs the site build and confirms the page
rendered. `pr` creates branch `issue-<N>-<slug>` (or
`issue-<N>-fix-<slug>`), commits only the touched files, pushes, opens
the PR with the verification table and `Closes #<N>`, and returns you to
the branch you started on. It refuses to run without a passing build or
when the branch already exists.

Report the PR URL. You are done.

## 5. Reject

Write `work/issue-<N>/reject.md` in three short parts: what you checked,
what failed, what would unblock it. The first line is the summary; a
re-run that produces the same first line will not post twice.

```bash
python3 scripts/entry_bot.py reject <N> --reason-file work/issue-<N>/reject.md
```

This posts one comment and adds the `needs-info` label. No PR. Report
what you posted. You are done.

## Never

- Edit the ledger, the JSON data files, or `makers.json` by hand.
- Invent a value for a field the sources do not confirm. `null` is correct.
- Open a PR for an issue that failed `check`.
- Process a second issue in the same run.
- Push to `main`.
