# Categorization

Every entry in this directory is one of four things: a harness, a multiplexer, a support tool, or
something else. This is the plan for sorting all 1,165 of them: the definitions, the order to apply
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

**This roughly halves the public directory, and that has to be a decision, not a side effect.** A
random sample of 100 records, scored against this procedure, puts 46 in `support` or
`something-else`. The 101-row audit, scored independently under the methodology this replaces, put
51 of 101 there. Call it half of 1,165.
The site's current count survives only while records still carry the legacy `agent` label; the
`.eleventy.js` change below is a no-op *today* for exactly that reason, and stops being one the
moment a batch merges. Agree the shrink before batch one, because it is expensive to reverse at
batch twelve.

## Ask in this order

The order decides the answer. The same product lands in a different bucket depending on which
question you ask first, so ask them in sequence and stop at the first yes. **Order is
load-bearing.** `harness` is the fourth test and not the first: a product has to clear the domain
gate, the SDK rule and the delegation test before its own loop matters.

1. **Is the primary task domain something other than software creation or modification — or is
   the named unit itself a model, dataset, course or tutorial?** → `something-else`
2. **Is the named unit itself an SDK, library or framework?** → `support`
3. **Is the code-changing step performed by a separately named coding agent?** → `multiplexer`
4. **Does it accept a software task, choose its next action, use tools, modify project code
   directly, and iterate on results?** → `harness`
5. **Does it materially help developers or coding agents?** → `support`
6. **Anything else** → `something-else`

**Question 1 is about the work product, not the mechanism.** "A product built exactly like a
coding agent, that drives coding agents, is still out of scope if its work product is not
software." PentestGPT produces security findings and is `something-else`; deepsec scans *your
repository* and "the only thing it adds to your repository is a `.deepsec/` folder", so its domain
is software and it falls through to question 5. Doing agent things is not the test; doing them to
a codebase is.

**For a tool, the domain test asks what it acts on.** It is in the software domain if it acts on
your code, your build or your deployment, or if it exists to serve coding agents — a scaffolder, a
delivery pipeline, a docs service for agents, a provider proxy all clear the gate, whether or not
any AI is involved. It is out if it does neither, however much developers use it: a tool whose work
is your data, your running services or your APIs is not working on software. "Useful to developers"
is not the test, and question 5 should not be read as if it were.

**Question 2 is nominal, and it beats the loop.** "The nominal test wins over the functional one
for this class, even when the package ships a runnable complete loop." The Claude Agent SDK
bundles the Claude Code CLI, so every loop signal is genuinely true — but the named unit is an
SDK, and the application a developer ships is theirs. A product that merely *ships* an SDK
alongside a different primary unit is not covered; it is decided by the delegation test instead.

**The nominal test reads what a developer installs, not what the vendor calls it.** An SDK, library
or framework is something you build *your own* agent with: you write code against it and ship the
result. A product you run, that does the work itself and hands you the output, is not one, whatever
its README title says — taglines reach for "framework" because it sounds foundational. The test is
whether the thing still needs you to write the agent. Get this backwards and a runnable product
with a grand tagline derives `support` at question 2 and never reaches the loop test at all.

**Question 3 is the only multiplexer test, and running the session counts as delegating.**
"Coordinating, launching or supervising other agents without delegating the code-changing step
does not make a multiplexer; such a product falls through to step 5" — but a terminal, workspace
or session manager built to run coding agents *is* delegating, because the agent it launches is
the one editing your repository. cmux, Claude Squad, Paseo, gastown and opcode are all
`multiplexer`, and so is Zellij. Neither "only one agent" nor "the vendor's own agent" is material.

What falls through to question 5 is narrower than it looks: a product where nothing is edited at
all — `postmortemthis` runs every major coding agent in read-only mode to cross-review a diff — or
one that carries traffic or exposes tools without ever running the session, like a provider proxy
or an MCP tool server.

**Question 4 wants all five signals, and incidental edits don't count.** "Read the field as: does
it change *project* code as the substance of the work?" A coordinator that only writes its own
config, lockfiles or scratch directory has not modified project code — without that reading, a
wrapper that writes a settings file satisfies every loop signal and derives `harness`.

Marketing copy — "agent", "autonomous", "AI developer" — tells you where to look. It never tells
you the answer.

**If the record never says what the thing does to a codebase, or who does it, fetch.**
`what_makes_it_special` collects differentiators: it is reliable about what is unusual and silent
about what is ordinary, and questions 1, 3 and 4 turn on the most ordinary facts there are. A
record that lists integrations, models and UI without once saying whether the thing edits code, or
what it edits code *for*, has answered neither 1 nor 4, however confident the rest of it reads.

**Question 3 is the one this rule is most often needed for, and the easiest to think you've
answered.** Which agent performs the edit is exactly the kind of ordinary fact the field leaves
out, so a record can describe orchestration in detail and still not say who touches the repository.
Read "harness builder", "agent platform", "meta-harness" and "AI coding agent platform" as
positioning, not as answers: every one of them is used by products that delegate and by products
that don't. Archon's record calls it "the first open-source harness builder for AI coding"; its
README says *"don't bundle Claude Code. Install it separately, then point Archon at it."* If the
record does not name the thing that edits, question 3 is unanswered and the record gets fetched.

This is the rule that catches the records which don't look like they need a fetch — the ones that
get decided wrongly.

**Before you write the category down, try to disprove it** using the strongest neighbouring one.
For a `harness`: what if the coding is delegated? For a `multiplexer`: does it edit code itself?
For `support`: does it run a complete loop after all? For `something-else`: is the domain really
not software? If the answer takes more than a sentence, the note should say so.

## How that plays out

| Entry | Lands on | The question that settled it |
|---|---|---|
| PentestGPT | `something-else` | 1 — drives coding agents, but the work product is security findings |
| Runway-style video agent | `something-else` | 1 — full agentic loop, but the output isn't software |
| CodeLlama | `something-else` | 1 — a model, not a product built on one |
| Claude Agent SDK | `support` | 2 — ships Claude Code and runs a real loop; the named unit is still an SDK |
| LangChain | `support` | 2 — a framework for building agents; the agent you build owns the loop |
| Codex Security | `multiplexer` | 3 — scans on its own, then hands the patch to Codex |
| cmux | `multiplexer` | 3 — a terminal built for running coding agents; they make the edits |
| Zellij | `multiplexer` | 3 — general-purpose, but it is where the agents run |
| MiniMax Code | `harness` | 4 — "the coding harness built for MiniMax models" |
| DeerFlow | `harness` | 4 — ships sandbox, bash access and file-write tools, and documents repository tasks |
| postmortemthis | `support` | 5 — launches every major agent, but read-only, so nothing is delegated |
| deepsec | `support` | 5 — unattended agentic scanner that never edits code |
| MiniMax Agent | `something-else` | 6 — general-purpose; builds artifacts, not codebases |

## Standing rulings

Ten edge cases, settled once so nobody re-argues them record by record. Change one in a PR, not
inline.

| The case | The call |
|---|---|
| The named thing is an SDK, library or framework | `support` — the nominal test wins even when the package ships a runnable complete loop |
| It owns a loop but never edits project code | `support` |
| The brand covers both a model and a product | Classify the product |
| Discontinued, archived or acquired | Category doesn't move; the lifecycle fields carry that news |
| It's a template, prompt pack or method | `support` |
| The work isn't software | `something-else`, however agentic it looks |
| General-purpose agent that can also code | `something-else` — unless it acts on a codebase: file editing in a project context, repository or workspace awareness, *and* a documented software-task workflow. Never settle this one from the record alone; read the source. |
| No-code platform for building agents | `support` |
| It builds a new codebase from a prompt | `harness` if it runs or tests what it wrote; `support` if it emits the code and stops. Question 1 says "software creation *or* modification", so writing the project clears the domain gate either way — but question 4 still wants the loop |
| Wrapper around a single coding agent, first-party included | `multiplexer`, if it hands off the edits |

## Writing it down

Two fields. That's the whole schema.

```yaml
category: "support"
category_note: "README: 'an SDK for building agents' — no loop of its own."
```

Quote the source in `category_note`. Don't summarise it. In the audit behind this page, every row
carrying a direct quote came through every pass intact; every row carrying a paraphrase is where
the errors turned up. That warning applies to this page too: two of the rulings below were
paraphrased out of the methodology this replaces, and both paraphrases changed the call.

## Checking a batch

Two passes over each batch before it merges. Neither adds a field — the first is a read over
records that already exist, the second decides where a disagreement gets written down.

**Read each batch by cluster, not by row.** Sort the batch by kind — agent frameworks and SDKs,
terminals and session managers, IDE assistants, prompt-to-app builders, scanners and reviewers,
context and memory tools, prompt packs — and read each cluster as a set. Any record sitting apart
from its cluster gets corrected or gets a written reason. This is a distinct pass, not something
that happens by itself while classifying row by row.

It is also the only check here that catches a *confident* error, because it never asks how sure you
were — only whether you treated like things alike. Measured against the 100-record sample: the
cluster read flags six records, and four of them were real errors, including two the classifier had
marked high confidence. Skipping this pass is what left PraisonAI classified as a harness in the
audit while its five nearest peers had already moved to `support`.

**Route every disagreement to a ruling, not to a row.** When two passes disagree, the output is a
line in the standing rulings table, not a quiet edit to one record. A disagreement that produces no
written rule will recur — five passes over one batch of 100 once produced four different answers,
and about three quarters of that churn was re-litigated policy rather than research failure. The
rulings table is what makes repeated passes converge instead of oscillate; without it, more
verification makes the corpus less stable, not more.

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

1,165 records today, plus the gap list once it's merged. The earlier estimate here — 1,150
decidable from the record, 14 needing a fetch — was not measured, and the only prior pass that
was contradicts it: every one of the 101 rows in `category_audit_first_100_pass5_verified.tsv`
carries a source URL. That audit fetched everything. Tested against 100 records drawn at random,
the estimate was wrong by an order of magnitude:

| | |
|---|---:|
| Records | 1,165 |
| Sampled and classified | 100 |
| Needed a look at the source | 15 |
| — of those, records with an empty `what_makes_it_special` | 3 |
| Genuine judgment calls, two answers defensible | 16 |
| Disagreed with the existing `agent`/`multiplexer` label | 57 |

Extrapolated, that is roughly 175 fetches, not 14. Batches of 25 to 50 records per pull request
still holds, but budget one to two fetches per batch rather than one per corpus.

**The rate is not the problem; the distribution is.** Two of the fifteen fetches *reversed* the
answer, and neither record looked short of anything: `grok-cli` and `goose` both read as
general-purpose in the record and as coding agents at the source. Both would have been written
down with an accurate verbatim quote and a correct ruling citation, and both would have survived
review — a verbatim quote from an incomplete record only proves the record was read correctly.
Hence the fetch rule under [Ask in this order](#ask-in-this-order), and the note on ruling 7.

The 101-row audit was enriched for hard cases, so its split is a regression suite and not a base
rate. The random sample above is the base rate. On the eight records the two samples share, this
procedure agrees with the audit on all eight, against six for the draft it replaced — but the two
that moved were fixed by ruling 7's restored wording and by a judgment call on Claw Code that no
version of the ladder forces. The reordering is justified by BR-001, not by that comparison: no
SDK-that-ships-a-loop appears in both samples, and that is the class the order actually decides.

Re-scoring the same 100 records against this procedure moved seven of them, and the ladder is now
internally consistent: every record's deciding question implies its category, with no exceptions.
The result is `harness` 35, `support` 34, `multiplexer` 19, `something-else` 12.

## What we'd need to build

Four small pieces, none of them written here.

**A frontmatter writer**, roughly 150 lines. Sets named keys in an `agents/*.md` file and leaves
every other byte alone. Needed because the corpus quotes its scalars and `yaml.safe_dump` doesn't:
re-emitting frontmatter the obvious way rewrites all 1,165 records at once and buries the real
change in formatting noise. A 50-record batch has to diff as 50 records.

**A no-op churn test.** Copies every record to a sandbox, writes each one's existing category
straight back, and asserts that nothing changed on disk. This is what keeps a batch reviewable, and
it's the first thing to run if the corpus ever shifts underneath us.

**A completeness check**, roughly ten lines. Every record carries one of the four categories, no
`agent` survives, and every record with a category has a note. Run before each batch merges.

**A verbatim-quote check**, three lines. `grep -F` every `category_note` quote against the record
or the fetched source it cites, and fail the batch on a miss. This is cheap and it earns its place:
the first run of it over a 100-row batch caught five quotes whose em-dashes had been silently
normalised to hyphens.

**A gap-list importer.** Reads `gap_report_clean.tsv`, writes one `agents/<slug>.md` per row, and
reports the handful of dedupe cases instead of guessing at them.

Plus the two repo fixes under [Before you classify anything](#before-you-classify-anything), which
are edits to existing files rather than new scripts.

## Don't add anything else

The version this replaces carried 21 fields per record. Two are enough. If a call needs more room
than `category_note` gives it, write a shorter note — don't add a field.

No confidence scores. No reviewer fields. No capability booleans. No evidence objects. No workflow
status. No second data model. The checks under [Checking a batch](#checking-a-batch) are process,
not schema: they read the two fields that already exist and write nothing new.

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
the main collection and 111 multiplexers, before and after — a no-op only because no record carries
a real category yet. See [Where each one goes](#where-each-one-goes) for what happens when they do.

**The generator overwrote the field.** `scripts/generate_pages.py` rebuilt every record from the
TSV on every run, taking `category` from a hardcoded `scripts/multiplexer_slugs.json`. It now
creates only missing records and never touches an existing one. The category was the least of it —
1,129 of 1,164 records have a hand-written body that a run would have flattened. To rebuild a
record from the TSV, delete the file first.
