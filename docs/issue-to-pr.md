# Processing an issue into a pull request

This is the procedure for turning a filled-in issue form into a pull request,
one PR per issue. It runs on a maintainer's machine inside Claude Code, and a
human reviews every PR. Read it top to bottom before starting.

Told "process issue N": do steps 1 to 5 for that issue. Told "process every
waiting issue": run step 0, then do steps 1 to 5 for each issue it lists, in
order, finishing one (PR opened or rejection posted) before starting the next.
A rejected issue does not stop the loop.

`node scripts/issue_to_pr.mts <subcommand>` does the mechanical steps: reading
the form, writing the entry file, the ledger row, and the maker record in the
repo's exact format, and opening the PR. Your own work is research: confirm
every claim against a primary source, then write down what you found. For a
new entry you never hand-edit `agents/`, `CATEGORIZATION_LEDGER.md`, or
`_data/makers.json`; the helper writes them. `_data/agents.json` and
`scripts/categorization_ledger.json` are not part of this process; the site
builds its search index from the entry files.

## Setup

Once per checkout:

```bash
npm ci            # Eleventy, for the build check
gh auth status    # must succeed; the helper pushes and opens PRs with this login
```

Every run starts from a clean, current `main` (the last command prints nothing):

```bash
git checkout main && git pull && git status --short
```

The one command that starts a run, from the repo root:

```bash
claude "Process issue 23"
```

or `claude "Process every waiting issue"`. `CLAUDE.md` points Claude Code at
this file. Node 24 or newer runs the helper as it is: no build step, no
dependencies. Everything a run produces lives in `work/issue-<N>/`, which is
gitignored.

## 0. List what is waiting

```bash
node scripts/issue_to_pr.mts list
```

One line per open issue from either form that has no `needs-info` label and no
open PR on an `issue-<N>-...` branch: the issue number, `add` or `fix`, and the
title. An issue counts as a form submission by its label (`new-entry` or
`correction`) or, because issues filed with the `gh` CLI can lack the label, by
its title prefix (`Add: ` or `Fix: `). An empty list means nothing to do.

## 1. Fetch and pre-check

```bash
node scripts/issue_to_pr.mts fetch <N>
```

Writes `work/issue-<N>/issue.json`: `kind` (`add` or `fix`) and `fields`, the
form's answers keyed by the field ids in `.github/ISSUE_TEMPLATE/`. A blank
optional field is `null`, a checkbox group is the list of checked labels, and
the category dropdown keeps only the text before the colon.

Before researching, check:

- Add: `name`, `url`, `maker`, `category`, `rationale`,
  `what_makes_it_special`, and `narrative` are not null. The slug (table
  below) has no file in `agents/`. Neither `url` nor `source_code_url` is
  already listed: `grep -il "github.com/owner/repo" agents/*.md`, grepping
  without the scheme, `www.`, trailing slash, or `.git`.
- Fix: the entry resolves to exactly one slug. `slug_hint` is set when the
  form linked the entry's page; otherwise `grep -il '^name: "<entry>"'
  agents/*.md`. `changes` holds one object per `field: old -> new` line and
  `unparsed` the lines that did not fit that pattern; read those, they may be
  a change written loosely. Every `field` must be a key in
  `agents/_TEMPLATE.md`, or `narrative` for the body.

Anything failing here is a rejection (step 5) with the problem as the reason.
A duplicate is rejected naming the entry that already covers it.

Read `agents/_TEMPLATE.md` now. It defines every key and the meaning of `null`
versus `"False"`.

## 2. Research an add issue

For every key below, find the value in the named source. The form-field column
says where the submitter's claim sits in `issue.json` (the field id in
parentheses); a claim is something to verify, not something to copy. Write
what you found to `work/issue-<N>/verified.json` in the shape at the end of
this section. `{o}/{r}` is the GitHub owner and repo from `source_code_url`.

| Key | Form field | Settled by | Rule |
|-----|------------|------------|------|
| `name` | Name (`name`) | The product's own README or site heading | Use the product's own spelling and casing. |
| `slug` | derived from `name` | `scripts/slug_overrides.json`, else the name | Lowercase, drop characters that are not letters, digits, spaces, or hyphens, spaces and underscores to single hyphens. Use the override when the name is mapped there. |
| `layout` | none | fixed | Always `agent.njk`; the helper writes it. |
| `category` | Category (`category`) | The README or product page, judged by the test in `README.md` | With the host tool removed, does it still run a coding task end to end? Yes: `agent`. Runs or coordinates other agents: `multiplexer`. Ships primitives but no agent: `agent-sdk`. Otherwise `other`. Disagreeing with the submitter is a discrepancy, not a reject. |
| ledger rationale | Category rationale (`rationale`) | Your own reading of the sources | One sentence in the style of the existing ledger rows, saying what the product does and who owns the loop. Rewrite it when you change the category or when it does not say that. |
| `maker` | Maker (`maker`) | The repo owner login, else the company named in the site footer or about page | Existing entries use the GitHub owner login as the key; keep that. If the key is not in `_data/makers.json`, supply `maker_record`: `gh api users/{owner} --jq .type` gives `User` (`individual`) or `Organization` (`company` or `community`, by what the site says). `revenue_model` is a subset of `tokens`, `subscriptions`; `country` is ISO 3166-1 alpha-2 or `null`. |
| `license` | License (`license`) | `gh api repos/{o}/{r} --jq .license.spdx_id`; when that is `NOASSERTION`, the LICENSE file; closed source: the pricing or terms page | The SPDX id (`Apache-2.0`, not "Apache 2.0"). `Proprietary` when nothing is published. More than one license: the id covering the app, with the rest in the evidence note. |
| `url` | Primary URL (`url`) | Load it | It must load and be about this product. Anything else is a reject. |
| `source_code_url` | Source code URL (`source_code_url`) | Load it; the repo must be public | Blank on the form means closed source. |
| `source_available` | derived from `source_code_url` | Same | `true` when a public repo exists, `false` when the form left it blank and the docs show no source. |
| `homepage` | none | The product's own site | Set only when the product has a site distinct from `url` (the page hides it when equal). Otherwise `null`. |
| `docs_url` | Docs URL (`docs_url`) | Load it | It must load and be documentation for this product. A landing page is not docs; the README is when nothing else exists. |
| `download_url` | none | The docs' install or download page | Only when there is a dedicated download page. Otherwise `null`. |
| `install_method` | Install method (`install_method`) | The README's install section | The actual command or method (`pip install x`, `brew install --cask ...`, a download). |
| `platforms` | Platforms (`platforms`) | The README or docs | Keep the checked boxes you confirm and add the ones the docs show. Values: `CLI`, `IDE`, `Web`, `Desktop`, `Autonomous`. |
| `autonomy_level` | none | The README or docs | Every mode shown: `autocomplete`, `pair-programmer`, `agentic`, `autonomous-background`, `one-shot-generative`. `[]` when unclear. |
| `specialization` | none | The README | `general` unless it is plainly one of `ui-generation`, `sql-data`, `evals`, `code-review`, `testing`, `security`, `migration`, `documentation`, `devops`, `mobile`. |
| `language` | Implementation language (`language`) | `gh api repos/{o}/{r} --jq .language` | Not on GitHub or closed source: `null`. |
| `first_released` | First released (`first_released`) | Earliest of: repo `created_at`, first release or tag date, an announced launch date | `gh api repos/{o}/{r} --jq .created_at`; `gh api --paginate "repos/{o}/{r}/releases?per_page=100"`. For a GitHub project this is almost always `created_at`, which is what existing entries use. `YYYY-MM-DD`. |
| `current_release` | Most recent release (`current_release`) | Latest release `published_at`, else latest tag, else `pushed_at` | `gh api repos/{o}/{r}/releases/latest --jq .published_at`; when every release is a prerelease that is a 404, so use `releases?per_page=1`. A release newer than the form's date wins. |
| `maintained` | Maintained (`maintained`) | `pushed_at` and `archived` from the repo call | `active` if pushed within 6 months; `dormant` within 18; `dead` beyond that or archived. `acquired` and `renamed` only with a source that says so. |
| `mcp_support` | Extensibility, MCP box (`extensibility`) | The docs or README | `true` confirmed present, `false` confirmed absent, `null` not confirmed. A checked box is a claim to verify; an unchecked box is unknown, not `false`. |
| `plugin_support` | Extensibility, Plugins box | The docs or README | Same rule. |
| `claude_code_plugin` | none | The docs or README | `true` only when it ships in the Claude Code plugin format. Otherwise `null`. |
| `subagents` | Extensibility, Subagents box | The docs or README | Same rule. For a multiplexer, spawning child agent sessions from a running one counts. |
| `hooks` | Extensibility, Hooks box | The docs, README, or source | Same rule. Lifecycle hooks it offers, or host-agent hooks it installs and reacts to. |
| `plan_mode` | Extensibility, Plan mode box | The docs or README | Same rule. |
| `plugin_docs_url` | none | The docs | Only when there is a dedicated plugin or extension page. Otherwise `null`. |
| `config_docs_url` | none | The docs | Only when there is a dedicated configuration page. Otherwise `null`. |
| `model_providers` | Model providers (`model_providers`) | The docs or README | Comma-separated as the docs list them, or `locked` for a single provider. A multiplexer names the agent CLIs it runs and says they bring their own providers. |
| `pricing` | Pricing (`pricing`) | The pricing page, else the README | One of `free`, `freemium`, `subscription`, `usage`, `BYOK`. Open source with no paid tier is `free`. |
| `stars` | none | `gh api repos/{o}/{r} --jq .stargazers_count` | A snapshot at research time. Not on GitHub: `null`. The template calls it `github_stars`; every file uses `stars`. |
| `sources` | none | fixed | `["github-issue"]`; the helper writes it. |
| `last_verified` | none | today | The helper writes it. |
| `what_makes_it_special` | What makes it special (`what_makes_it_special`) | The submission, checked against the sources | One or two sentences of plain text, no markdown links. Remove anything the sources do not support rather than softening it. |
| the body | Narrative (`narrative`) | The submission, checked against the sources | About a paragraph: why it exists, how it works, who uses it. No sentence shared with `what_makes_it_special`. Remove unsupported claims. |
| ignored | Anything else? (`notes`), Before submitting (`confirm`) | | Context for you, and often the submitter's own evidence. Never copied into the entry. |

Write booleans as JSON `true` / `false` and unknowns as `null`; the helper
renders them as `"True"`, `"False"`, and `null`, and quotes every other value,
matching the existing files. Keys you leave out of `entry` are written as
`null`.

Fill `evidence` for every field you looked at, including the ones that
matched. `submitted` is the form's value, `verified` is yours, `source` is the
URL that settles it, and `note` says why they differ when they do. It becomes
the PR's verification table.

Reject at this step only when you cannot confirm that the product exists and
does what the issue says it does.

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
    "docs_url": "https://foo.dev/docs",
    "install_method": "cargo install foo-agent",
    "platforms": ["CLI"],
    "autonomy_level": ["agentic"],
    "specialization": "general",
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

`maker_record` is `null` when the maker key already exists in
`_data/makers.json`.

## 3. Research a fix issue

`issue.json` has `fields.entry`, `slug_hint`, `changes`, `unparsed`,
`fields.source`, `fields.category` (the "New category" dropdown, `null` when
unchanged), `fields.rationale`, and `fields.notes`.

For each change open the cited source and confirm the new value using the
rules in the table above. A change the source does not support goes in
`not_applied` with a one-line reason, not in `entry`. If no change survives,
go to step 5. A non-null `fields.category` is a category change to verify like
any other; it needs a rationale.

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

`entry` holds only the keys that change. `body` is the full new narrative only
when the narrative changes. `rationale` is required when `category` is in
`entry`.

## 4. Write, build, open the PR

For an add issue, the helper writes the entry file, the ledger row (sorted by
slug), and the maker record if new:

```bash
node scripts/issue_to_pr.mts write work/issue-<N>/verified.json
```

It refuses to overwrite an existing entry and refuses keys that are not in the
template.

For a fix issue, edit `agents/<slug>.md` yourself, one line per key, in the
file's own format: a string is `key: "value"` (a `"` inside becomes `\"`),
unknown is `key: null`, a boolean is `"True"` or `"False"`, and a list is
`key:` followed by one `  - "value"` line per item (`key: []` when empty).
Replace the key's existing line or lines; add a missing key just above the
closing `---`. Set `last_verified` to today. A new narrative replaces
everything after the closing `---`, as one blank line and the paragraph. When
`category` changes, also edit that slug's row in `CATEGORIZATION_LEDGER.md`
(`grep -n '^| `<slug>`' CATEGORIZATION_LEDGER.md`), new category and
rationale. Touch nothing else.

Then build and confirm the page rendered:

```bash
npx @11ty/eleventy --quiet
test -f _site/agents/<slug>/index.html && grep -c "\"slug\":\"<slug>\"" _site/agents.json
git diff --stat   # look at it: only the entry file, the ledger, and possibly makers.json
```

For an `other` entry the inverse holds: no page and no search-index row, by
design. A failed build is a problem in your `verified.json`; fix it and write
again.

Write the PR body to `work/issue-<N>/pr-body.md`, following
`.github/pull_request_template.md`:

```markdown
## What does this change?

Adds the entry for **<Name>** (`agents/<slug>.md`) from issue #<N>.

## Why?

Submitted through the "Add an entry" form by @<author>. Every field below was checked against the linked source.

## How did you test it?

`npx @11ty/eleventy` built the site and `_site/agents/<slug>/index.html` rendered.

## Verification

| Field | Submitted | Verified | Evidence |
|---|---|---|---|
| license | Apache 2.0 | Apache-2.0 | https://github.com/o/r/blob/main/LICENSE |

## Discrepancies

- **first_released**: submitted 2026-05-21, verified 2025-11-09. The repo was created 2025-11-09; the announcement came later.

## Filled in from sources

Left blank on the form: `stars`, `language`.

## Not applied

- **pricing** -> free: the pricing page still lists paid tiers.

Closes #<N>

Opened by the issue-to-PR runbook (`docs/issue-to-pr.md`).
```

"Updates the entry" and "Fix an entry" for a fix. A discrepancy is a submitted
value the sources contradicted; "Filled in from sources" lists fields the form
left blank; "Not applied" is for fix issues. Leave out a section that would be
empty. Then:

```bash
node scripts/issue_to_pr.mts pr <N>
```

It creates `issue-<N>-<slug>` (or `issue-<N>-fix-<slug>`) from `main`,
commits only the entry file, the ledger, and `makers.json`, pushes, opens the
PR against `main` with your body file, and returns you to the branch you
started on, so the next issue starts from a clean tree. It refuses to run when
the branch already exists on the remote or the working tree has changes
outside those files. If an earlier attempt left a local branch behind, delete
it with `git branch -D issue-<N>-<slug>` and run it again.

Report the PR URL. You are done.

## 5. Reject

Write `work/issue-<N>/reject.md` in three short parts: what you checked, what
failed, what would unblock it. The first line is the summary. Then:

```bash
gh issue view <N> --comments      # if a comment with the same first line is already there, stop
gh issue comment <N> --body-file work/issue-<N>/reject.md
gh issue edit <N> --add-label needs-info
```

One comment, no PR. Report what you posted. You are done.

## Never

- Edit the ledger or `makers.json` by hand for a new entry.
- Invent a value for a field the sources do not confirm. `null` is correct.
- Open a PR for an issue that failed the pre-check.
- Start the next issue before the current one has a PR or a rejection.
- Push to `main`.

## Reviewing a bot PR

For the human reviewing what a run opened. The PR body carries the evidence;
these are the four things to read before merging.

- **The category.** Apply the test in `README.md` yourself, and check that
  the ledger rationale is one sentence in the style of the rows around it.
- **Every item under Discrepancies.** Each is a place the run disagreed with
  the submitter and says why. Dates follow the table's rules (for a GitHub
  project `first_released` is usually the repo creation date), so a later
  announcement date from the submitter is a discrepancy, not an error; edit
  the PR if you prefer the other value.
- **One or two evidence links**, especially any value confirmed from source
  code rather than documentation.
- **The diff.** An add is exactly one new entry file, one ledger row, and at
  most one maker record. A fix touches only
  the entry file, and the ledger only when the category changed. Anything
  else means the run touched what it should not have.
