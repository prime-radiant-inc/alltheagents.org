---
# Canonical per-agent template (schema v1.1, 2026-08-20).
# Copy this file to agents/<slug>.md for a new entry. Delete these header comments.
# Null convention: null = not yet researched. False = researched and confirmed absent.

# --- identity ---
name: null                    # canonical product name
slug: null                    # url slug, must match the filename; on collision, register an
                              # override in scripts/slug_overrides.json rather than improvising
layout: "agent.njk"
category: "agent"             # agent = codes itself (owns its own agentic loop)
                              # multiplexer = orchestrates/runs OTHER agents rather than coding
                              # agent-sdk = general agent-building framework/SDK/toolkit that
                              # ships no coding agent itself (autogen, crewai, langgraph, ...)
                              # other = neither (gateways, prompt libs, eval tooling, datasets,
                              # tutorials, link-only artifacts). Every decision + rationale lives
                              # in CATEGORIZATION_LEDGER.md (see also scripts/categorization_ledger.json)
maker: null                   # key of a record in _data/makers.json (maker = creator, one concept).
                              # Maker records carry: maker_type (individual | company | community),
                              # country (ISO 3166-1 alpha-2 or null), makes_models (bool),
                              # revenue_model (subset of [tokens, subscriptions]; empty = neither).
                              # Corrections to generated/enriched fields belong in
                              # scripts/field_overrides.json, not hand-edits that regeneration wipes.
license: null                 # MIT, Apache-2.0, Proprietary, ...
url: null                     # primary URL
source_code_url: null
source_available: null        # True | False
homepage: null
docs_url: null
download_url: null
install_method: null

# --- classification ---
platforms: []                 # CLI, IDE, Web, Desktop, Autonomous (multi-select)
autonomy_level: []            # multi-select: list every mode the product supports
                              # autocomplete | pair-programmer | agentic | autonomous-background |
                              # one-shot-generative (generates a codebase/app from a single prompt
                              # with no interactive loop, e.g. GPT-Engineer, many app builders)
specialization: "general"     # CLOSED enum — use a canonical value, extend the list via PR:
                              # general | ui-generation | sql-data | evals | code-review |
                              # testing | security | migration | documentation | devops | mobile
language: null                # primary implementation language (open-source only)

# --- lifecycle ---
first_released: null          # YYYY-MM-DD
current_release: null         # YYYY-MM-DD
maintained: null              # active | dormant | dead | acquired | renamed

# --- extensibility ---
mcp_support: null
plugin_support: null
claude_code_plugin: null      # compatible with the Claude Code plugin format?
subagents: null
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null

# --- commercial ---
model_providers: null         # e.g. "Anthropic, OpenAI, Ollama" — or "locked" if single-provider
pricing: null                 # free | freemium | subscription | usage | BYOK

# --- traction (latest snapshot only; append-only histories live in metrics/<slug>.yaml,
#     see metrics/_TEMPLATE.yaml — kept out of agent files to avoid constant churn here) ---
github_stars: null            # latest snapshot (existing files use `stars`; rename is a follow-up
                              # migration). Downloads live only in metrics/<slug>.yaml for now —
                              # no frontmatter field until collection automation exists.

# --- provenance ---
sources: []                   # which discovery channel(s) surfaced this entry
last_verified: null           # YYYY-MM-DD a human or agent last confirmed the facts above

what_makes_it_special: null   # 1-2 sentences, frontmatter only — never repeated in the body
---

Body = a short narrative about the harness: why it exists, what it's meant for, and
who uses it. Required for every entry. Only as long as it needs to be — usually about
a paragraph. Do NOT duplicate frontmatter content here — repeating
what_makes_it_special (or any frontmatter field) in the body is forbidden.

Example (for a hypothetical entry): "Aider grew out of its author's frustration with
copy-pasting between ChatGPT and an editor, and became the reference open-source pair
programmer for git-native workflows: it maps the repo, edits files directly, and commits
each change. Its users skew toward experienced developers who want tight control over
every diff rather than autonomous runs, and its benchmark suite became a de facto
standard other harnesses report against."
