# Categorization

Every entry in this directory is one of four things: a harness, a multiplexer, a support tool, or
something else. This is how we decide which, and what to do when it isn't clear.

Round one is a first pass over all 1,316 records. It is deliberately conservative about what counts
as a harness — see [Harness needs positive evidence](#harness-needs-positive-evidence).

## The four

**`harness`** — Owns its own agentic loop and edits code itself using an LLM. Give it a software
task and it picks its next move, uses tools, and changes the code.

**`multiplexer`** — Primarily launches, manages, or coordinates other coding agents such as Claude
Code or Codex. The underlying agents do the coding loops.

**`support`** — Helps developers or coding agents through specifications, prompts, context, memory,
SDKs, frameworks, or workflow support, but does not independently run a complete coding loop.

**`something-else`** — Related discovery that does not fit the census: a model, dataset, tutorial,
course, general-purpose application, or non-coding agent.

## The tiebreak: who touches the code?

Almost every hard record is hard for the same reason. It is unclear whether the thing edits code
itself or hands that job to something else.

When `harness` and `multiplexer` are both plausible, ask one question: **does the record name a
separate coding agent that performs the code-changing step?**

Yes, and that agent does the editing → `multiplexer`. No, the unit does it itself → `harness`.

Running its own subagents does not make something a multiplexer. Delegating to Claude Code does.

## Harness needs positive evidence

Label a record `harness` only if its own text says it edits, writes, or applies code changes.
"AI-powered development platform" is not that. "Intelligent coding assistant" is not that.

No positive evidence, no harness this round. Give the record its next best category, or put it on
the edge list.

This is on purpose, and it buys trust in one direction at the cost of accuracy in the other. A
harness wrongly demoted is one row we fix later. A support tool sitting in the harness list is what
makes the whole directory untrustworthy.

## When you are not sure, name the pattern

Do not invent a rule to break a tie. Do not guess.

Write down what made the record ambiguous, phrased as the **class** it belongs to rather than the
row it happens to be — "general-purpose agent that also codes", "reviewer that suggests changes but
never applies them", "IDE plugin that only completes". Then move on.

Classes go to a human for a single ruling that settles every row in them. That is the whole reason
the edge list exists. The 2026-08-24 audit found roughly three-quarters of the churn between passes
came from unresolved definitional policy, not from bad research: one ruling is cheaper than a
hundred re-reads.

## Worked examples

| Record | Category | Why |
|---|---|---|
| `oh-my-pi` | `harness` | "LSP-integrated edits… AST-based edits." The record says it edits code. |
| `agent-deck` | `multiplexer` | "Manage multiple AI agent sessions (Claude Code, Gemini CLI, OpenCode, Codex)." The named agents do the editing. |
| `Agentic Engineering Framework` | `support` | Calls itself a "harness around AI coding agents" and supplies governance, gates and audit trails. It wraps the agents; it does not edit. What a record calls itself is not the answer. |
| `Agentic-Coding-with-Claude-Code` | `something-else` | The code repository for a book. |
| `obra/superpowers` | `support` | A skills library that a coding agent loads. The agent owns the loop. |

## What gets written

Two fields in the record's frontmatter, and no status field.

- **`category`** — one of `harness`, `multiplexer`, `support`, `something-else`. The field already
  exists on all 1,316 records; this changes the values it can hold.
- **`category_note`** — one sentence, quoted from the record where possible, that the call rests on.
  This is the one field round one adds. It is defined in `agents/_TEMPLATE.md` on branch
  `eden/categorization-plumbing` and does not yet appear on any record.

**A record still reading `category: agent` has not been done yet.** That is the progress marker,
and it costs nothing.

`agent` cannot simply be renamed to `harness`, tempting as it looks. The template on `main`
documents it as "agent = codes itself (owns its own agentic loop)", which is the harness test — but
1,172 of 1,316 records carry the label, and they got it by not being multiplexers rather than by
passing any test. The label means "unsorted", whatever the template says.

## What this does to the site

Nothing, except where a record's multiplexer status changes.

`category` is read in exactly two places, both in `.eleventy.js`: one collection takes every record
that is not `multiplexer`, the other takes every record that is. Nothing renders it, and nothing
outside that file reads it. So `agent` → `harness` and `agent` → `support` are invisible to the
site. Only `agent` ↔ `multiplexer` moves anything, and correcting that split is the point.

Whether `support` and `something-else` should eventually leave the public directory is a real
decision, and it is not this document's to make. Make it once the counts are real.

## Round one

1. **Pilot.** 100 seeded-random records, plus the rows of the 2026-08-24 verified audit that match a
   live record, shuffled together and classified blind. Nothing is written to any record. The output
   is a scored table and the edge-class list.
2. **Rule.** The census owner rules once per edge class. Rulings are appended to this document.
3. **Sweep.** The rest of the corpus in batches, written to frontmatter, delivered as PRs.

When handing this method to a classifier, give it everything above "Round one" and nothing below.
A classifier that knows which rows are scored, or that a verified audit exists to look up, stops
measuring the method.

### Tools it needs

- `scripts/frontmatter.py` — already written and tested on branch `eden/categorization-plumbing`.
  Surgical: it rewrites only the keys you name and leaves every other byte alone.
- A seeded sampler, and a scorer that joins predictions to the audit table. Both throwaway.

Nothing else. This document does not change `.eleventy.js`, `scripts/generate_pages.py`, the TSV, or
`_data/agents.json`. That last one keeps a stale `category` for any record we relabel; nothing reads
it, so it is flagged here rather than fixed.
