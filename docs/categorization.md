# Categorization

Every entry in this directory is one of four things: a harness, a multiplexer, a support tool, or
something else. This is the plan for sorting all 1,164 of them: the definitions, the order to apply
them in, how big the job is, and the small amount of tooling it needs.

Nothing is classified yet and nothing is built yet. **No record should take a new label until two
fixes land** — see [Before you classify anything](#before-you-classify-anything).

## The four

**`harness`** — Does the work itself. Give it a software task and it picks the next move, runs
tools, **edits the code**, and iterates. Running its own subagents doesn't make it a multiplexer.

**`multiplexer`** — Drives the ones that do. Its job is launching, managing or coordinating
coding agents, and they are the ones touching the code.

**`support`** — Helps with the work; doesn't do it. SDKs, frameworks, prompt packs, context and
memory tools, evaluation, infrastructure. No complete loop of its own.

**`something-else`** — Not in scope. Models, datasets, courses, tutorials, general-purpose agents,
anything whose output isn't software.

## Where each one goes

**`harness` and `multiplexer` are the public directory.** That's what the site shows.

**`support` and `something-else` are tracked but never published.** They stay in `agents/` like
everything else and keep their own categories, so the four groups stay separable — they just don't
reach the site.

They are never deleted. The point is that nothing gets researched twice: an item ruled out today is
still on file, with the reason, if the directory's scope ever widens.

## Ask in this order

The order decides the answer. The same product lands in a different bucket depending on which
question you ask first, so ask them in sequence and stop at the first yes.

1. **Does it take a software task, run the loop, and edit the code itself?** → `harness`
2. **Is the work something other than software?** → `something-else`
3. **Is the thing itself an SDK, library or framework?** → `support`
4. **Does a separately named coding agent make the edits?** → `multiplexer`
5. **Does it materially help developers or coding agents?** → `support`
6. **Anything else** → `something-else`

Question 1 goes first because a thing can be an SDK *and* a real coding agent. The Claude Agent SDK
ships the Claude Code CLI and runs a genuine loop; when something is both, what it does beats what
it's called.

Note the word *software* in question 1. An agent that runs a full loop and edits video, or one that
investigates and reports on security, fails question 1 and falls through to question 2. Doing agent
things is not the test; doing them to a codebase is.

Marketing copy — "agent", "autonomous", "AI developer" — tells you where to look. It never tells
you the answer.

## How that plays out

| Entry | Lands on | The question that settled it |
|---|---|---|
| Claude Agent SDK | `harness` | 1 — an SDK, but it ships Claude Code and runs a real loop |
| MiniMax Code | `harness` | 1 — "the coding harness built for MiniMax models" |
| PentestGPT | `something-else` | 2 — drives coding agents, but the work is security |
| LangChain | `support` | 3 — a framework for building agents; the agent you build owns the loop |
| Codex Security | `multiplexer` | 4 — scans on its own; Codex writes the patches |
| deepsec | `support` | 5 — unattended agentic scanner that never edits code |
| MiniMax Agent | `something-else` | 6 — general-purpose; builds artifacts, not codebases |

## Standing rulings

Nine edge cases, settled once so nobody re-argues them record by record. Change one in a PR, not
inline.

| The case | The call |
|---|---|
| The named thing is an SDK, library or framework | `support` — unless it runs the loop and edits code itself, which question 1 catches first |
| It owns a loop but never edits project code | `support` |
| The brand covers both a model and a product | Classify the product |
| Discontinued, archived or acquired | Category doesn't move; the lifecycle fields carry that news |
| It's a template, prompt pack or method | `support` |
| The work isn't software | `something-else`, however agentic it looks |
| General-purpose agent that can also code | `something-else` — unless it documents a workflow acting on an existing repository |
| No-code platform for building agents | `support` |
| Wrapper around a single coding agent, first-party included | `multiplexer`, if it hands off the edits |

## Writing it down

Two fields. That's the whole schema.

```yaml
category: "support"
category_note: "README: 'an SDK for building agents' — no loop of its own."
```

Quote the source in `category_note`. Don't summarise it. In the audit behind this page, every row
carrying a direct quote came through every pass intact; every row carrying a paraphrase is where
the errors turned up.

## Adding the gap list

`gap_report_clean.tsv` holds 410 discovered items — most of the commercial tier the census missed.
Merging them is three steps, and the middle one is far smaller than it sounds.

**Write records, not JSON.** Each row becomes one `agents/<slug>.md` file. Don't add rows to
`_data/agents.json`; it's generated. Don't add them to `coding_agent_harnesses.tsv` either —
`scripts/generate_pages.py` rebuilds every record from that file and flattens hand edits. The TSV
is already ten records behind `agents/`, and nothing in CI runs it. Slug collisions go in
`scripts/slug_overrides.json`, never into an improvised filename.

**Dedupe is about seven rows, not four hundred.** Measured against the corpus on 2026-08-26: one
gap row already exists by URL; five match an existing record by name with a different URL — Omnara,
KaneAI, Zoo Code, Pi Coding Agent, Code Assistant; and one URL appears twice inside the gap report.
Every row has a URL, and no two rows share a name. The corpus has no duplicate primary URLs today.
Keep it that way.

**Name variants are the real risk, not URLs.** Xcode is in the list as "Xcode Coding Intelligence".
Rovo Dev is there twice — once on its own, once inside "Atlassian: Jira, Rovo Dev, Bitbucket", a row
naming three products that has to be split before any of it can be classified, because a category
describes one product surface and not a vendor. Ten rows carry a colon or a comma in the name; most
are only taglines, but read them before trusting the name.

**The list isn't the whole gap.** MiniMax Code is in neither the corpus nor the 410 rows. Merging
the file closes most of the hole, not all of it.

## What the work looks like

1,164 records today, plus the gap list once it's merged. Most of it is a reading pass rather than a
research project, because the records already describe themselves:

| | |
|---|---:|
| Records | 1,164 |
| Decidable from text already in the record | 1,150 |
| Needing a look at the source | 14 |
| Already answered by the verified audit | 70 |

So about 1,094 need a judgment, 14 need a fetch, and 70 can be written straight in from work that
is already done. Batches of 25 to 50 records per pull request.

What none of that measures is how often the existing `agent` label is wrong. The 101-row audit was
enriched for hard cases, so its split is a regression suite and not a base rate. The first two or
three batches will tell us.

## What we'd need to build

Four small pieces, none of them written here.

**A frontmatter writer**, roughly 150 lines. Sets named keys in an `agents/*.md` file and leaves
every other byte alone. Needed because the corpus quotes its scalars and `yaml.safe_dump` doesn't:
re-emitting frontmatter the obvious way rewrites all 1,164 records at once and buries the real
change in formatting noise. A 50-record batch has to diff as 50 records.

**A no-op churn test.** Copies every record to a sandbox, writes each one's existing category
straight back, and asserts that nothing changed on disk. This is what keeps a batch reviewable, and
it's the first thing to run if the corpus ever shifts underneath us.

**A completeness check**, roughly ten lines. Every record carries one of the four categories, no
`agent` survives, and every record with a category has a note. Run before each batch merges.

**A gap-list importer.** Reads `gap_report_clean.tsv`, writes one `agents/<slug>.md` per row, and
reports the handful of dedupe cases instead of guessing at them.

Plus the two repo fixes under [Before you classify anything](#before-you-classify-anything), which
are edits to existing files rather than new scripts.

## Don't add anything else

The version this replaces carried 21 fields per record. Two are enough. If a call needs more room
than `category_note` gives it, write a shorter note — don't add a field.

No confidence scores. No reviewer fields. No capability booleans. No evidence objects. No workflow
status. No second data model.

## Before you classify anything

No record carries `harness`, `support` or `something-else` today. The corpus still runs on the old
labels — `agent` on 1,053 records, `multiplexer` on 111 — where `agent` means "not a multiplexer"
and is not a verdict about anything.

**The records are `agents/*.md`.** `_data/agents.json` is a build artifact — `scripts/generate_json_from_md.py`
writes it and Eleventy copies it to the site as the search index. Edit it by hand and the next build
discards the edit.

Two things used to stand in the way of a record taking a new value. Both are fixed in this change.

**The site published everything that wasn't a multiplexer.** `.eleventy.js` built its main
collection as `category !== "multiplexer"`, so the moment a record was labelled `support` it would
have appeared in the public list. It now excludes both unpublished categories, and
`scripts/generate_json_from_md.py` applies the same rule so hidden records don't linger in site
search. It still accepts the legacy `agent` label alongside `harness`, because filtering on
`harness` alone would empty the site today. Verified a no-op against the current corpus: 1,053 in
the main collection and 111 multiplexers, before and after.

**The generator overwrote the field.** `scripts/generate_pages.py` rebuilt every record from the
TSV on every run, taking `category` from a hardcoded `scripts/multiplexer_slugs.json`. It now
creates only missing records and never touches an existing one. The category was the least of it —
1,129 of 1,164 records have a hand-written body that a run would have flattened. To rebuild a
record from the TSV, delete the file first.
