# Issue-to-PR agent: design

Date: 2026-09-03
Status: draft for review

## Goal

Turn a filled-in issue form into a reviewed pull request. Any coding agent
(Claude Code, Codex, Gemini CLI, Aider) or a human follows one runbook and
calls one script. The repo stores no credentials.

Two forms exist in `.github/ISSUE_TEMPLATE/`:

- `add-agent.yml` ("Add an entry", label `new-entry`, title prefix `Add: `)
- `update-agent.yml` ("Fix an entry", label `correction`, title prefix `Fix: `)

For each issue the agent reads the form, verifies every claim against primary
sources, writes the entry files, and opens a PR. When it cannot, it posts one
comment on the issue saying what would unblock it.

## Decisions already made

| Question | Decision |
|----------|----------|
| Where does it run? | Anywhere with an authenticated `gh` CLI and a coding agent. No trigger wrapper in v1. |
| Credentials | None stored in the repo. No PAT, no GitHub App, no API key secret. |
| Submitted value disagrees with research | The verified value goes in the PR. The PR body lists every disagreement with its evidence URL. |
| Issue cannot be processed | One comment on the issue, a `needs-info` label, no PR. |
| Harness | Agnostic. Mechanical work lives in a script; judgment lives in a runbook. |

## Non-goals for v1

- Metrics history files (`metrics/<slug>.yaml`)
- A GitHub Actions, cloud, or local scheduler trigger
- Processing more than one issue per run
- Reacting to comments or edits after the first pass
- Any change to the issue forms

## Architecture

Three parts, each with one job:

1. **Runbook** (`docs/issue-to-pr.md`). The procedure an agent follows when
   told "process issue N". It contains the research protocol: which source
   confirms each field and what counts as confirmed.
2. **Script** (`scripts/entry_bot.py`). A stdlib-only Python CLI that does
   everything that must be exact: parsing, validation, file writing, ledger
   maintenance, JSON regeneration, and the `gh` calls that post the PR or the
   rejection comment.
3. **Pointer files** (`AGENTS.md`, `CLAUDE.md`). Three lines each. Most
   harnesses auto-load `AGENTS.md`; Claude Code loads `CLAUDE.md`, which
   imports it. Both say: to process an issue, follow the runbook.

The agent never edits `CATEGORIZATION_LEDGER.md`, `_data/agents.json`,
`_data/makers.json`, or `scripts/categorization_ledger.json` by hand. The
script owns those files.

## Working directory

Every run writes its intermediate files to `work/issue-<N>/`. The directory
is gitignored. Files:

| File | Written by | Contents |
|------|-----------|----------|
| `issue.json` | `fetch` | Parsed form fields plus issue metadata |
| `verified.json` | the agent | Per-field submitted value, verified value, evidence URL, and note |
| `reject.md` | the agent | Reason for rejection, when applicable |

## Script: `scripts/entry_bot.py`

Python 3, no dependencies beyond the standard library. All network access
goes through one function that shells out to `gh`; tests replace it.

### `fetch <N>`

Runs `gh issue view N --json number,title,body,labels,author,url`.
Decides the form type from the label (`new-entry` or `correction`); with
neither label it exits non-zero.

Parses the body. GitHub renders a form as a `### <Label>` heading per field
followed by the value. The parser reads the matching template YAML to map each
label back to its field id, so a label change in the form never breaks the
parser. Rules:

- `_No response_` becomes `null`.
- Checkbox groups become a list of the checked labels.
- The category dropdown keeps the text before the first colon.
- Whitespace is stripped; internal newlines in textareas are kept.

For a fix issue the `changes` textarea is parsed line by line as
`field: old -> new`. Lines that do not match the pattern are kept in a
`unparsed` list for the agent to read. The `entry` field is resolved to a
slug: a page link yields its last path segment; a name is matched
case-insensitively against `name` in `agents/*.md`.

Writes `work/issue-N/issue.json`.

### `check work/issue-N/issue.json`

Deterministic pre-flight. Exits non-zero with one line per problem.

For add issues:

- A required form field is blank.
- `category` is not one of `agent`, `multiplexer`, `agent-sdk`, `other`.
- `maintained`, `pricing`, or a platform value is outside its enum.
- The primary URL does not answer an HTTP request (any 2xx or 3xx passes).
- The derived slug already exists in `agents/`, or `slug_overrides.json` maps
  the name elsewhere.
- The primary URL or source code URL, normalised (scheme, `www.`, trailing
  slash, `.git` removed, lowercased), already appears in any entry.

For fix issues:

- The entry cannot be resolved to exactly one slug.
- A change names a field that is not in the entry template.
- No parseable change lines.
- Warning only: `old` does not match the entry's current value.

`check --built` is a separate mode used after writing: it runs
`npx @11ty/eleventy` and confirms `_site/agents/<slug>/index.html` exists
and `_data/agents.json` contains the slug. On success it writes
`work/issue-N/built.ok`, the marker `pr` requires.

### `write work/issue-N/verified.json`

Creates a new entry from the agent's verified data. It first validates
`entry` with the same enum and required-field rules `check` applies to the
form, so an agent cannot write a value the form could not have submitted.
Steps, in order:

1. Write `agents/<slug>.md` in the canonical format: quoted strings, `null`
   unquoted, lists as `  - "value"`, booleans as `"True"` / `"False"`,
   field order as in `agents/_TEMPLATE.md`. Existing files use `stars`;
   new files do too. `sources` is `["github-issue"]`. `last_verified` is
   today's date. The body is the verified narrative.
2. If the maker key is not in `_data/makers.json`, add the record the agent
   supplied (`name`, `maker_type`, `country`, `makes_models`,
   `revenue_model`, `website`).
3. Insert the ledger row into `CATEGORIZATION_LEDGER.md` at its sorted
   position by slug, and append the same record to
   `scripts/categorization_ledger.json`. Recompute the summary line
   (`**N entries**: a agent, b multiplexer, c agent-sdk, d other`) from the
   table.
4. Run `regen`.

The command refuses to overwrite an existing entry file.

### `apply-fix work/issue-N/verified.json`

Edits an existing entry. For each verified change it rewrites only that
frontmatter line, preserving every other byte of the file. If the change is
to the narrative body it replaces the body. If `category` changed it updates
the ledger row's category and rationale in both copies and recomputes the
summary. Sets `last_verified` to today, adding the line if absent. Runs
`regen`.

### `regen`

Runs the existing `scripts/generate_json_from_md.py`.

### `pr <N>`

Creates the branch (`issue-N-<slug>` or `issue-N-fix-<slug>`), stages
exactly the files the run touched, commits, pushes with the existing `gh`
login, and opens the PR with `gh pr create`. The body follows
`.github/pull_request_template.md` and adds:

- a verification table with one row per field: submitted, verified, evidence
- a "Discrepancies" list when any verified value differs from the submission
- `Closes #N`

It refuses to run if `check --built` has not passed in this run (it looks
for the marker file `work/issue-N/built.ok`).

### `reject <N> --reason-file work/issue-N/reject.md`

Posts the file as one comment, adds the `needs-info` label (creating it if
the repo lacks it), and leaves the issue open. Never opens a PR.

## Runbook: `docs/issue-to-pr.md`

Written for an agent that has never seen the repo. Sections:

1. **Preconditions.** `gh auth status` succeeds; `git status` is clean;
   `npm ci` has run.
2. **Fetch and check.** Run `fetch`, then `check`. Any `check` failure goes
   straight to step 6 with the script's output as the reason.
3. **Research (add issues).** Per-field protocol:

   | Field | Confirm from | Notes |
   |-------|-------------|-------|
   | url, homepage, docs_url | Fetch each; must load and be about this product | |
   | source_code_url, source_available | Repo exists and is public | Blank means closed source: `source_available: "False"` |
   | license | `gh api repos/{o}/{r}` `license.spdx_id`, else the LICENSE file, else the pricing page | Proprietary when no license is published |
   | stars, language | Same API call | Non-GitHub: `null` |
   | first_released | Earliest of: first release, first tag, repo `created_at`, announced launch date | |
   | current_release | Latest release `published_at`, else latest tag, else `pushed_at` | |
   | maintained | `active` if pushed within 6 months; `dormant` within 18; `dead` beyond, or repo archived; `acquired` / `renamed` only with a source | |
   | maker | Repo owner, or the company on the site's footer or about page | Check `_data/makers.json` for an existing key first; the key is a lowercase slug |
   | category | Read the README or product page and apply the test from `README.md`: with the host removed, does it still run a coding task end to end? | Disagreement with the submitter is a discrepancy, not a failure |
   | platforms, extensibility, model_providers, pricing, install_method | The docs or README | Unconfirmed optional fields stay `null`, never guessed |
   | what_makes_it_special, narrative | Light edit for house style only: no repetition between the two, about a paragraph, no facts the sources do not support | |

   The agent writes `verified.json` with, for every field, the submitted
   value, the verified value, the evidence URL, and a note when they differ.
4. **Research (fix issues).** For each change line, open the cited source
   and confirm the new value. A change the source does not support is dropped
   and listed in the PR body under "Not applied". If no change survives, go to
   step 6.
5. **Write, build, PR.** `write` or `apply-fix`, then `check --built`, then
   `pr`.
6. **Reject.** Write `reject.md` in three parts: what was checked, what
   failed, what would unblock it. Run `reject`. Stop.
7. **What the agent never does.** Edit the ledger, JSON, or makers file by
   hand. Invent a value for a field the sources do not confirm. Open a PR
   for an issue that failed `check`. Process a second issue in the same run.

The run fails at research only when the agent cannot confirm that the
product exists and does what the issue claims.

## Data formats

### `issue.json`

```json
{
  "number": 12,
  "kind": "add",
  "title": "Add: Foo",
  "author": "someone",
  "url": "https://github.com/prime-radiant-inc/alltheagents.org/issues/12",
  "fields": {
    "name": "Foo",
    "url": "https://foo.dev",
    "source_code_url": "https://github.com/foo/foo",
    "maker": "Foo Inc",
    "license": "MIT",
    "category": "agent",
    "rationale": "...",
    "what_makes_it_special": "...",
    "narrative": "...",
    "platforms": ["CLI", "IDE"],
    "language": null,
    "first_released": null,
    "current_release": null,
    "maintained": "active",
    "pricing": "BYOK",
    "model_providers": null,
    "install_method": null,
    "docs_url": null,
    "extensibility": ["MCP", "Hooks"],
    "notes": null
  }
}
```

A fix issue has `"kind": "fix"`, `"slug"`, and
`"changes": [{"field": "license", "old": "MIT", "new": "Apache-2.0"}]`
plus `"unparsed": []`, `"source"`, `"category"`, `"rationale"`, `"notes"`.

### `verified.json`

```json
{
  "number": 12,
  "kind": "add",
  "slug": "foo",
  "entry": { "...every frontmatter key...": "..." },
  "body": "narrative paragraph",
  "rationale": "one sentence for the ledger",
  "maker_record": null,
  "evidence": {
    "license": {"submitted": "MIT", "verified": "Apache-2.0", "source": "https://github.com/foo/foo/blob/main/LICENSE", "note": "LICENSE file is Apache-2.0"}
  }
}
```

`maker_record` is an object only when the maker key is new. For a fix,
`entry` holds only the changed keys, `body` is present only when the
narrative changed, and `not_applied` lists changes the source did not
support.

## Error handling

- `fetch`, `check`, `write`, `apply-fix`, and `pr` exit non-zero with a
  one-line-per-problem message on stderr. They never partially write: `write`
  builds every file's new contents in memory and writes them all at the end.
- `pr` refuses to run twice for the same issue number if a branch of that
  name already exists remotely.
- `reject` refuses to post if a comment by the same author with the same
  first line already exists on the issue, so a re-run does not spam.
- A `gh` failure (not logged in, rate limited) is reported verbatim and
  stops the run.

## Testing

One file, `scripts/tests/test_entry_bot.py`, using `unittest`. Fixtures are
two issue bodies saved as markdown: one complete add, one fix. Tests, kept
few and tight:

1. Parse the add fixture: field ids, null for `_No response_`, checkbox
   list, category before the colon.
2. Parse the fix fixture: slug from a page link, change lines, unparsed
   lines preserved.
3. `check` rejects a blank required field and a duplicate URL.
4. `write` round-trip: the produced file, read back through the repo's own
   `parse_frontmatter`, matches the input; the ledger summary counts
   increase by one in the right category.
5. `apply-fix` changes only the targeted lines; every other line is
   byte-identical.

All `gh` and HTTP calls go through one function, patched in tests.

## Files touched by a run

| Add | Fix |
|-----|-----|
| `agents/<slug>.md` (new) | `agents/<slug>.md` |
| `CATEGORIZATION_LEDGER.md` | `CATEGORIZATION_LEDGER.md` (category changes only) |
| `scripts/categorization_ledger.json` | `scripts/categorization_ledger.json` (category changes only) |
| `_data/makers.json` (new maker only) | |
| `_data/agents.json` | `_data/agents.json` |

## Files added by this work

- `docs/issue-to-pr.md`
- `AGENTS.md`, `CLAUDE.md`
- `scripts/entry_bot.py`
- `scripts/tests/test_entry_bot.py`, `scripts/tests/fixtures/add.md`,
  `scripts/tests/fixtures/fix.md`
- `github-issue` entry in `_data/source_urls.json` and
  `scripts/source_urls.json`
- `work/` added to `.gitignore`

## Amendment 2026-09-03: no generated data files

Decided after the first implementation, to let many entry PRs merge without
conflicts and to drop the one-issue-per-run limit later.

- `_data/agents.json` is deleted along with `scripts/generate_json_from_md.py`.
  Nothing read it: the search index the site serves at `/agents.json` is built
  by Eleventy from the entry files (`agents-index.json.njk`). The `regen`
  subcommand is gone; `write` and `apply-fix` no longer regenerate anything;
  `check --built` confirms the slug in the built `_site/agents.json`.
- `scripts/categorization_ledger.json` is deleted. Its 19 rows missing from the
  markdown table were migrated in with the note that no rationale was recorded.
  The table in `CATEGORIZATION_LEDGER.md` is the single source of category
  decisions.
- The `**N entries**: ...` summary line in the ledger is replaced by a pointer
  to the About page, which computes counts at build time. The script no longer
  recomputes counts.
- `_data/makers.json` is written with sorted keys so a new maker is inserted at
  its alphabetical position rather than appended.

A bot PR now touches the entry file, one ledger row, and at most one maker
record. Statements above about `regen`, `_data/agents.json`, the ledger JSON
copy, and the summary line are superseded.
