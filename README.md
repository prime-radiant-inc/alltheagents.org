# All the Agents

Comprehensive census of coding agent harnesses — systems that let an LLM autonomously write, modify, debug, or run code — plus the multiplexers that manage them and the SDKs used to build them.

The catalog is large and continually updated. Every entry is sorted into exactly one of four categories — **agent**, **multiplexer**, **agent-sdk**, or **other** (gateways, frameworks, tooling, and adjacent artifacts). Browse it, with current counts, at [alltheagents.org](https://alltheagents.org).

## Categorization

Every entry carries exactly one category, decided against these definitions:

- **agent** — a coding agent or harness: something that uses tools in a loop to create or modify software. The agent **owns its own loop** — it drives the iterate-decide-invoke cycle (prompt -> model -> tool -> result -> repeat) and invokes at least one tool itself. "Expansive and inclusive" refers to what counts as software and as a tool, not to who owns the loop. A framework that installs personas or workflows into a host agent's loop (Claude Code, Cursor, etc.) does not own the loop and is not an agent. Test: if you remove the host, does the product still run a coding task end-to-end? If yes, it is an agent.
- **multiplexer** — not an agent: a tool that helps manage a set of agents with a human-facing UI (orchestrates/runs other agents rather than coding itself). A multiplexer launches, schedules, or coordinates other agents' loops but does not code itself.
- **agent-sdk** — a general agent-building framework, SDK, or toolkit that ships no coding agent of its own (e.g. AutoGen, CrewAI, LangGraph). Developers use its primitives to build something that would own a loop; the SDK itself does not own one.
- **other** — neither of the above: model gateways, prompt libraries, workflow packs installed into a host agent, eval tooling, MCP tool servers, memory layers, datasets, tutorials, link-only artifacts. These may use tools or appear in loops, but they do not own the loop or invoke tools themselves. Entries in this category are recorded here but are not published on the website.

Every decision, with a one-line rationale, is recorded in [`CATEGORIZATION_LEDGER.md`](CATEGORIZATION_LEDGER.md). The 2026-08-28 review pass reclassified entries against the tightened definitions, was independently verified by three reviewer passes over the full list, and folded in a 30-day Hacker News sweep.

## Contents

- `agents/` — individual agent pages (Markdown with YAML frontmatter; see `agents/_TEMPLATE.md` for the schema)
- `CATEGORIZATION_LEDGER.md` — per-entry category decisions with rationale
- `_layouts/`, `*.njk` — Eleventy templates
- `css/style.css` — dark theme stylesheet
- `scripts/` — the issue-to-PR bot (`entry_bot.py`) and its tests
- `docs/issue-to-pr.md` — runbook for turning an issue form into a PR (`scripts/entry_bot.py` does the mechanical parts)
- `metrics/` — per-entry traction history (stars/downloads over time)

## Website

The site is built with [Eleventy](https://www.11ty.dev/) and deployed to GitHub Pages via GitHub Actions.

### Local development

```bash
npm install
npx @11ty/eleventy --serve
```

This starts a local dev server at `http://localhost:8080`.

### Build

```bash
npm install
npx @11ty/eleventy
```

Output goes to `_site/`.

## Entry schema

Each `agents/<slug>.md` file is YAML frontmatter plus a narrative body. Key fields:

| Field | Description |
|-------|-------------|
| name | Canonical product name |
| category | agent \| multiplexer \| agent-sdk \| other |
| maker | Key into `_data/makers.json` |
| license | License (MIT, Apache-2.0, Proprietary, etc.) |
| url | Primary URL |
| source_available | Whether source code is available |
| platforms | CLI, IDE, Web, Desktop, Autonomous |
| autonomy_level | autocomplete, pair-programmer, agentic, autonomous-background, one-shot-generative |
| maintained | active, dormant, dead, acquired, renamed |
| mcp_support, plugin_support, hooks, plan_mode, subagents | Extensibility booleans |
| model_providers, pricing | Model access and cost model |
| what_makes_it_special | 1-2 sentence description (frontmatter only) |

The body is a short narrative — why the harness exists, how it works, and who uses it — kept distinct from the frontmatter fields.

## Methodology

Initially built from 15 "awesome" aggregation lists, 5 rounds of GitHub topic/keyword searches, GitHub API enrichment of 1,516 repos, and manual research of commercial products. The 2026-08-28 pass re-researched every entry's primary URL, filled null fields, rewrote all 1,316 narrative bodies, and categorized every entry per the definitions above; ambiguous calls were adjudicated after three independent full-list review passes. The discovery pipeline's working files (source lists, candidate tables, enrichment batches, and the scripts that turned them into entry files) were removed on 2026-09-04 once the entry files became the only source; they remain in git history.
