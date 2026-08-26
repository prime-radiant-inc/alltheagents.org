# Categorization Methodology

**Version:** v1.1
**Status:** Draft for review
**Applies to:** every record under `agents/` in the harness-census repository
**Contains:** the classification rubric (§1–9) and the boundary register (§10)

This document tells a reviewer how to classify one item. It is the operative rubric: if it and
any other document disagree, this one governs, and the disagreement is a bug to file.

---

## 1. Scope and unit of analysis

You classify **one named product surface**, as it exists on the date in
`classification_last_verified`. Not the company, not the model behind it, not the family of
things sharing its brand.

Resolve the unit *before* researching it. Most bad calls in this project's history were about
what the row referred to, not about which category it belonged in.

- **A brand spanning a model and a product** — CodeGeeX is both a model line and an IDE
  assistant. Name which one the row is (see BR-003).
- **Sibling products** — MiniMax Code, MiniMax Agent and MiniMax CLI are three different rows.
  Evidence about one never decides another.
- **A peripheral artifact is not the product** — an auxiliary SDK repository is not the service
  it talks to. If the only reachable material is peripheral, the row is *blocked*, not
  low-confidence.
- **Renames and pivots** — record the former name and classify the unit the row names; the
  successor goes in the lifecycle fields (BR-004).

Record the outcome in `name`, `slug`, `url`, and the alias fields. If you cannot state in one
sentence what the unit is, stop and escalate rather than guessing.

---

## 2. The four categories

### `harness`

The product owns a complete agentic coding loop. Given a software task it accepts the task,
chooses the next action, uses tools, **modifies code directly**, observes the result, and
iterates. A harness may coordinate its own subagents; that does not make it a multiplexer.

### `multiplexer`

The product's primary role is launching, managing, supervising or coordinating other coding
agents — Claude Code, Codex, OpenCode, Cline and the like. Those agents own the coding loops.
Incidental file or configuration edits by the coordinator do not make it a harness.

### `support`

The product materially helps developers or coding agents through specifications, prompts,
context, memory, SDKs, frameworks, evaluation, infrastructure or workflow support, but does not
independently run a complete coding loop and is not primarily a manager for external coding
agents.

### `something-else`

A related discovery outside the census: a model, dataset, tutorial, course, general-purpose
application or non-coding agent. The record stays in the repository so the discovery and the
exclusion decision are not lost, but it is never published.

---

## 3. The five coding-loop signals

Establish these as facts before choosing a category. Each is a boolean:

| Field | Question |
|---|---|
| `accepts_software_task` | Can a user hand it a software task in natural language? |
| `chooses_next_action` | Does it decide what to do next, rather than following a fixed script? |
| `uses_tools` | Does it read files, run commands, or call tools? |
| `modifies_code_directly` | Does *it* change project code? |
| `iterates_on_results` | Does it observe outcomes and continue? |

Four further booleans carry the boundary tests:

| Field | Question |
|---|---|
| `software_task_domain` | Is its primary task domain software creation or modification? |
| `is_sdk_or_framework` | Is the named unit itself an SDK, library or framework? |
| `delegates_code_changes` | Is the code-changing step performed by a separately named coding agent? |
| `supports_coding_agents` | Does it materially help developers or coding agents, in the sense of step 5? |

`null` means not yet researched. `False` means researched and confirmed absent. Never leave a
decisive field `null` on a verified record.

The first three are decisive on every path, so a verified record must carry all three. The
fourth is decisive only if the record reaches step 5, so it is not demanded of a harness or a
multiplexer — but a record that reaches step 5 without it derives no category at all and cannot
be verified. **These eight fields plus `something_else_kind` are the complete input to the
procedure.** If the rule engine ever reads a ninth, that is a bug in the engine, not an
undocumented feature; `test_every_signal_field_the_engine_reads_is_documented` enforces it.

**Incidental edits do not count as `modifies_code_directly`.** Section 2 excludes "incidental
file or configuration edits by the coordinator" from what makes a harness, so a coordinator that
only writes its own config, lockfiles or scratch directory has `modifies_code_directly: False`.
Read the field as: does it change *project* code as the substance of the work? Without this
reading a wrapper that writes a settings file satisfies all five loop signals and derives
`harness` at step 4.

**Why `modifies_code_directly` and `delegates_code_changes` are separate.** A single
"modifies code" boolean cannot distinguish a product that edits files from one that dispatches
Codex to edit them — and that distinction is the entire harness/multiplexer boundary. A
delegating product can honestly satisfy every other loop signal.

---

## 4. Decision procedure

Apply these in order. **Order is load-bearing**: two reviewers converge only if they apply the
tests in sequence, and where a rule sits determines the answer.

1. **Domain gate.** Is the primary task domain something other than software creation or
   modification? → `something-else`, and set `something_else_kind`.

   This is *not* the same as `accepts_software_task`. A penetration-testing agent accepts a task,
   plans, uses tools and may drive Claude Code — but its domain is security. Same for video
   editing, finance, and smartphone operation. (BR-006)

2. **SDK rule.** Is the named unit itself an SDK, library or framework? → `support`.

   For this class the nominal test wins over the functional one, even when the package ships a
   runnable complete loop. A product that merely *ships* an SDK alongside a different primary
   unit is not covered. (BR-001)

3. **Delegation test.** Is the code-changing step performed by a separately named coding agent?
   → `multiplexer`.

   This precedes the loop test on purpose. Neither "only one agent" nor "the vendor's own agent"
   is material. (BR-009)

   This is the **only** multiplexer test. Coordinating, launching or supervising other agents
   without delegating the code-changing step does not make a multiplexer; such a product falls
   through to step 5. The procedure has six steps and no others.

4. **Loop ownership.** Are all five loop signals true, with `modifies_code_directly`? →
   `harness`.

5. **Material support.** Does it materially help developers or coding agents? → `support`.

   Owning an agentic loop is not sufficient for `harness`. A product that runs an unattended loop
   but never modifies project code — a scanner, a reviewer — is `support`. (BR-002)

6. **Otherwise** → `something-else` with an exclusion kind.

Marketing language — "agent", "autonomous", "AI developer", "coding assistant" — is a discovery
clue, never evidence. Vendors describe scanners as agents and wrappers as platforms.

---

## 5. Evidence

Use sources in this order:

1. Current source code or implementation documentation
2. Current official product documentation
3. Current official repository README
4. Official product pages, demos and release notes
5. Reliable secondary sources, only when primary sources are unavailable

**Every verified record needs a verbatim quote** in `classification_quote` that on its own
decides the category, with its source in `classification_quote_source`. Copy it; do not
paraphrase. The validator fetches the source and asserts the quote appears in it.

This is not a stylistic preference. Across five passes over the same hundred items, every record
carrying a verbatim primary-source quote was classified correctly by every pass, and every
record carrying a paraphrase is where the errors were. An evidence URL alone does not prevent a
confident fabrication, and at corpus scale nobody re-reads every row.

Good deciding quotes, all of which settled a contested row:

- Tembo: *"harness- and model-agnostic"* → multiplexer
- MiniMax Code: *"The coding harness built for MiniMax models"* → harness
- Codex Security, from OpenAI's own `AGENTS.md`: *"a thin wrapper around Codex and its security
  plugin"* → multiplexer

Also required: a rationale connecting observed behaviour to the definition; counterevidence
naming the strongest competing category and why it loses; source-quality and confidence labels;
a verification date; and two reviewer identifiers.

### Confidence

| Level | Meaning |
|---|---|
| `high` | Current primary evidence for every decisive signal, plus a located quote |
| `medium` | One bounded inference, or incomplete current documentation |
| `low` | Contradictory, unavailable or stale evidence. Never silently upgrade. |

Confidence is *derived*, not chosen. If the only source is vendor marketing that describes
outcomes without mechanism, the ceiling is `medium` however plausible it reads.

---

## 6. Lifecycle is not category

Category is a claim about capability and is close to timeless. Lifecycle is a claim about status
and decays weekly. Keep them apart.

**A discontinued harness is still a harness.** Archived and shut-down products keep their
capability category; the death goes in the lifecycle fields (BR-004).

Every lifecycle claim carries a date and either a measurement or a dated primary source. **You
may not assert a lifecycle fact the mechanical sweep can measure** — whether a repository is
archived, when it was last pushed, whether a URL redirects. Run the sweep and cite it. A previous
pass recorded "active repository with current commits" for a repository dormant ten months, and
an acquisition as closed while it was still pending. Both were free to state and free to check.

---

## 7. Review workflow

1. **Intake.** Normalise name, slug, canonical URL, aliases and discovery sources. New records
   start `category: null`, `classification_status: unreviewed`.
2. **Sweep.** Refresh observable facts. Categorize against swept data, never stale frontmatter.
3. **Primary research.** Establish the primary workflow and fill the capability signals *before*
   choosing a category.
4. **Preliminary decision.** Apply §4 in order. Record the quote, evidence, rationale,
   confidence, source quality, date, and the `BR-nnn` ruling if one applies.
5. **Adversarial check.** Try to *disprove* your category using the strongest neighbouring one.
   For a harness: what if the coding is delegated? For a multiplexer: does it edit code itself?
   For support: does it run a complete loop? For something-else: is the domain really not
   software?
6. **Independent review.** A second reviewer reads the sources and the record without relying on
   the first reviewer's conclusion.
7. **Adjudication.** Disagreement sets `disputed` until resolved. **Route the resolution to the
   boundary register**, not to a one-off decision — a disagreement that produces no written rule
   will recur.
8. **Verification.** Set `verified` only when the schema is satisfied, both reviews agree, and
   the stored category equals `derive_category()`.

### Who reviews

The corpus is too large for two human reviews of every record. The two required reviewers are the
model classification pass and a human, recorded as distinct identifiers with the model version as
the model's identifier so the decision is auditable. Two *human* reviews are required only for
records that reach dispute, sit on an unruled boundary, or rank in the top 200 by stars — label
errors on widely used projects are disproportionately costly.

### Peer-group consistency

After classifying, cluster records by kind — agent frameworks, harness-agnostic runners, IDE
assistants, prompt-to-app builders, scanners and reviewers, context and memory tools, enterprise
platform agents — and re-read each cluster as a set. Any record sitting apart from its cluster
needs a written reason or gets corrected.

This is a distinct pass, not a side effect of per-record review. Skipping it is what left
PraisonAI classified as a harness while its five nearest peers had already moved to support.

---

## 8. Publication

- `harness`, `multiplexer` and `support` records with `classification_status: verified` are
  public.
- `something-else` and every non-verified status stay in Git and in the complete
  `_data/agents.json`, but generate no public page and appear in no public collection, count,
  export or search index.
- Eligibility is derived from category and status. There is no hand-maintained `published` flag.
- Category labels appear on aggregate public listings, so support tools are never presented as
  harnesses.

---

## 9. Maintenance

- Re-run the mechanical sweep monthly.
- Re-review only what the sweep flags: newly archived, no push in six months, a changed redirect
  target, a non-200 status, or a changed repository description.
- A genuinely novel edge case becomes a new boundary-register entry, by PR, before it is applied.
- Track the rate of reviewer disagreement over time. It should fall as the register fills. If it
  stays flat, the definitions are the problem, not the reviewers.

---

## 10. Boundary register

Recurring edge classes are ruled **once**, here, and cited by identifier from a record's
`classification_boundary_ruling` field. Changing a ruling requires a pull request.

### Why the register exists

Across five passes over the same hundred items, roughly three quarters of the churn came from
unresolved definitional policy rather than research failure. On the same evidence a careful
reviewer could reach either answer, defensibly, every time — so every pass re-litigated the same
boundaries and reached a different conclusion.

Adding research passes does not fix that. Writing the precedent down does.

**These are policy decisions, not findings.** They are made by the census owner and recorded
here. A reviewer who encounters a genuinely novel edge case opens a PR adding an entry; they do
not decide it inline.

### Rulings in force

| Id | Edge class | Ruling | Decided |
|---|---|---|---|
| BR-001 | Named unit is an SDK, library or framework | `support` | 2026-08-24 |
| BR-002 | Owns an agentic loop but never modifies project code | `support` | 2026-08-25 |
| BR-003 | Brand spans a model and a product | Classify the product surface | 2026-08-25 |
| BR-004 | Discontinued, archived or acquired | Keep the capability category; lifecycle carries status | 2026-08-25 |
| BR-005 | Template, prompt pack or method | `support` | 2026-08-25 |
| BR-006 | Task domain is not software | `something-else` | 2026-08-25 |
| BR-007 | General-purpose agent that can also code | `something-else`, unless it ships a documented software-engineering surface operating on an existing project or repository | 2026-08-25 |
| BR-008 | No-code platform for building agents | `support` | 2026-08-25 |
| BR-009 | Wrapper around a coding agent, single-agent and first-party included | `multiplexer` when the code-changing step is delegated | 2026-08-25 |

### Rationale

#### BR-001 — SDKs are support

The nominal test wins over the functional one for this class, even when the package ships a
runnable complete loop. The Claude Agent SDK bundles the Claude Code CLI, so every loop signal is
genuinely true — but the named unit is an SDK, and the application a developer ships is theirs.
This keeps the row consistent with Strands, LangChain and TypeChat.

A product that merely *ships* an SDK alongside a different primary unit is not covered. Codex
Security self-describes as a "CLI and TypeScript SDK", but its named unit is a scanning product;
it is decided by BR-009 instead.

*Applies to:* Claude Agent SDK, Strands, LangChain, TypeChat, CrewAI, AutoGen, AgentScope,
Swarms, Qwen-Agent, Flue.

#### BR-002 — A loop without code changes is support

Owning an agentic loop is not sufficient for `harness`; changing code is required. deepsec runs
an unattended, resumable, parallelised investigation and adds only a `.deepsec/` folder. PR-Agent
and OpenCodeReview produce findings and comments.

#### BR-003 — The product surface wins over the model

Where a brand covers both a model and a product, classify the product. CodeGeeX is a stale model
repository and a live IDE assistant; the assistant is the census-relevant unit.

#### BR-004 — Lifecycle never changes the category

A discontinued harness is still a harness. Roo Code and iFlow keep their categories; the archive
and shutdown go in the lifecycle fields. Conflating the two caused errors in both directions:
reading dead products as alive, and letting a shutdown tempt a recategorisation.

#### BR-005 — Templates and methods are support

ai-dev-tasks, BMAD-METHOD, context-engineering-intro and the like supply prompts, workflows and
scaffolding that a host agent executes. The host owns the loop.

#### BR-006 — Task domain governs, regardless of mechanism

A product built exactly like a coding agent, that drives coding agents, is still out of scope if
its work product is not software. PentestGPT produces security findings; video-use produces
edited video. Both are `something-else` however agentic they are.

#### BR-007 — General-purpose agents must act on a codebase

The discriminator is deliberately narrow. Every capable assistant can emit code; if producing
code were sufficient the census would have to admit every general-purpose agent and would stop
being a census of coding harnesses.

The test is whether the product acts **on a codebase** — file editing in a project context,
repository or workspace awareness, and a documented software-task workflow. Generating a
standalone artifact does not qualify.

- **DeerFlow → `harness`.** Ships sandbox, bash access and file-write tools, documents repository
  tasks, and self-describes as a harness.
- **MiniMax Agent → `something-else`.** "A general intelligent agent designed to tackle
  long-horizon, complex tasks", whose own material shows it generating product pages rather than
  editing repositories.
- **Google Opal → `something-else`.** Builds hosted visual mini-apps; no repository.

#### BR-008 — No-code agent platforms are support

A consistency ruling rather than fresh reasoning. CrewAI, AutoGen, AgentScope, Swarms,
Qwen-Agent, LangChain and Flue are all platforms for assembling agents, none of them
coding-specific, and all are `support`. No-code versus code is an interface distinction, and the
census must not sort by interface modality.

On such a platform the assembled agent, not the platform, is the thing that could own a loop.

*Applies to:* Coze Studio and ChatDev 2.0, which must always share a bucket.

#### BR-009 — Wrapping one agent is still multiplexing

Neither "single agent" nor "first-party" is material; the test is whether the code-changing step
is delegated to a separately named coding agent.

The corpus already rules this way. opcode wraps only Claude Code and Aperant requires only the
Claude Code CLI, and both are multiplexers at high confidence. A first-party carve-out would mean
OpenAI wrapping Codex is treated differently from a third party wrapping Codex — a
vendor-identity distinction with no behavioural content.

*Applies to:* Codex Security, opcode, Aperant, ralph.

### Adding a ruling

1. Open a PR adding a row to the table and a rationale section.
2. Name the records it decides and whether any change category.
3. Re-run validation; records citing a changed ruling must be re-derived.
4. Bump the version in `categorization.md` if the decision procedure itself changes.

---

## Appendix: worked examples

| Item | Category | Step that decided it |
|---|---|---|
| PentestGPT | `something-else` | 1 — drives coding agents, but the domain is security |
| Claude Agent SDK | `support` | 2 — bundles Claude Code and runs a real loop, but the named unit is an SDK |
| Codex Security | `multiplexer` | 3 — scans on its own, but Codex tasks perform the patches |
| MiniMax Code | `harness` | 4 — "the coding harness built for MiniMax models" |
| DeerFlow | `harness` | 4 — owns its loop and edits directly; ACP delegation is additive |
| deepsec | `support` | 5 — unattended agentic scanner that never modifies code |
| Coze Studio | `support` | 5 — a platform for assembling agents; the agent would own the loop |
| MiniMax Agent | `something-else` | 6 — general-purpose; builds artifacts, not codebases |
