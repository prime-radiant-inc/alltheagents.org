---
name: "fireproof"
slug: "fireproof"
layout: "agent.njk"
category: "other"
maker: "fireproof-storage"
license: "Apache-2.0"
url: "https://github.com/fireproof-storage/fireproof"
source_code_url: "https://github.com/fireproof-storage/fireproof"
source_available: "True"
platforms:
  - "Web"
first_released: "2023-08-17"
current_release: "2026-05-07"
stars: "972"
language: "TypeScript"
homepage: "https://use-fireproof.com"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "npm"
docs_url: "https://use-fireproof.com/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Lightweight embedded document database with encrypted live sync and git-like versioning via hash history (cryptographic causal consistency). Encrypted content-addressed blob replication, CRDT-based multi-writer safe real-time collaboration. Runs anywhere (browser, Node, Deno, Bun, edge), offline-first with no loading/error states, small package with no WASM. Designed to fit in LLM context windows for AI code generation."
---

Fireproof addresses the persistence gap in AI-built applications: an LLM can generate a React app in seconds, but wiring up a real database, sync, and conflict handling traditionally breaks the flow. As an embedded library (@fireproof/core, use-fireproof), it runs in the browser, Node, Deno, and Bun with live queries through React hooks, CRDT-based multi-writer collaboration, and a hash-chain version history that gives git-like rollback without a server. Content-addressed encrypted blob replication means data syncs between devices without a trusted server, which suits local-first and collaborative apps. Its growth tracks the vibe-coding ecosystem — it is frequently the database an AI app builder reaches for — while remaining a general-purpose embedded database for any JavaScript application.
