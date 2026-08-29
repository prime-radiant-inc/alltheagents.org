---
name: "honeycomb"
slug: "honeycomb"
layout: "agent.njk"
category: "other"
maker: "legioncodeinc"
license: "AGPL-3.0-or-later"
url: "https://github.com/legioncodeinc/honeycomb"
source_code_url: "https://github.com/legioncodeinc/honeycomb"
source_available: "True"
platforms: []
first_released: "2026-06-17"
current_release: "2026-07-23"
stars: "109"
language: "TypeScript"
homepage: "https://www.theapiary.sh"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: "nomic-embed-text-v1.5 (opt-in)"
pricing: "Free/open-source"
install_method: "curl -fsSL https://get.theapiary.sh | sh (macOS/Linux) or irm https://get.theapiary.sh/install.ps1 | iex (Windows); or npm install -g @legioncodeinc/honeycomb; or build from source"
docs_url: "https://theapiary.sh"
plugin_docs_url: null
config_docs_url: null
download_url: "https://get.theapiary.sh"
maintained: "active"
sources:
  - "github_topic5"
what_makes_it_special: "Shared, persistent memory for AI coding agents; local daemon captures every agent turn and distills into three-tier memory (key -> summary -> raw) with deterministic SQL joins; session priming injects bounded ~300-800 token index at session start; Skillify & propagation mines reusable skills and auto-pulls team skills; pollinating loop merges duplicates/prunes junk/supersedes stale facts; knowledge graph + multi-language AST codebase graph (TS, JS, Python, Go, Rust, Java, Ruby, C/C++); hybrid recall (BM25 + 768-dim semantic vectors via Reciprocal Rank Fusion, recall@5 ~0.72-0.78); cross-tool shared brain (one local daemon, any harness reads/writes same memory); per-harness capture hooks for Claude Code, Cursor, Codex; built on Activeloop Deeplake."
---

honeycomb gives coding agents a shared, durable memory across sessions, tools, and machines. A local daemon captures each agent turn through harness hooks, distills it into a three-tier structure — a one-line keyword key, a distilled summary, and the raw dialogue — and serves recall to any connected client, so a decision made in Claude Code is available to Cursor or a teammate's session later. Session priming injects a bounded keyword index at the start of each session rather than re-reading raw transcripts, keeping context overhead low, while a pollinating maintenance loop merges duplicates and retires stale facts. Beyond raw memory it mines recurring patterns into skills that propagate across a team, and it maintains both an entity knowledge graph and a multi-language AST graph of the codebase. Retrieval combines BM25 with optional local embeddings through reciprocal rank fusion, with deterministic SQL joins guaranteeing exact recall of stored records.
