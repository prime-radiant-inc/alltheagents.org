---
# Canonical per-agent template (schema v1.1, 2026-08-20).
# Copy this file to agents/<slug>.md for a new entry. Delete these header comments.
# Null convention: null = not yet researched. False = researched and confirmed absent.

# --- identity ---
name: null                    # canonical product name
slug: null                    # url slug, matches filename
layout: "agent.njk"
category: "agent"             # agent | multiplexer
maker: null                   # slug of a record in _data/makers.json (maker = creator, one concept)
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
autonomy_level: []            # PROPOSED SCALE, open for discussion in this PR:
                              # autocomplete | pair-programmer | agentic | autonomous-background
                              # multi-select: list every mode the product supports
specialization: "general"     # general = any language/any task
                              # or name the narrow focus: ui-generation, sql-data, evals,
                              # code-review, testing, security-fixing, migration, docs, ...
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

# --- traction (latest snapshots only; append-only histories live in metrics/<slug>.yaml,
#     see metrics/_TEMPLATE.yaml — kept out of agent files to avoid constant churn here) ---
github_stars: null            # latest snapshot (existing files use `stars`; rename is a follow-up migration)
downloads: null               # latest snapshot across sources

# --- provenance ---
sources: []                   # which discovery channel(s) surfaced this entry
last_verified: null           # YYYY-MM-DD a human or agent last confirmed the facts above

what_makes_it_special: null   # 1-2 sentences, frontmatter only — never repeated in the body
---

Body = a short narrative about the harness: why it exists, what it's meant for, and
who uses it. Required for every entry. Only as long as it needs to be — usually about
a paragraph. Do NOT duplicate frontmatter content here — repeating
what_makes_it_special (or any frontmatter field) in the body is forbidden.
