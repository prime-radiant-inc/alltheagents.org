---
name: "m1nd"
slug: "m1nd"
layout: "agent.njk"
category: "other"
maker: "maxkle1nz"
license: "MIT"
url: "https://github.com/maxkle1nz/m1nd"
source_code_url: "https://github.com/maxkle1nz/m1nd"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-03-12"
current_release: "2026-08-15"
stars: "22"
language: "Rust"
homepage: "https://m1nd.world"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: null
pricing: "Free / open-source"
install_method: "npx -y @maxkle1nz/m1nd update apply --yes (npm installer fetches signed Rust binary), or cargo install m1nd-mcp from source"
docs_url: "https://m1nd.world/wiki/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@maxkle1nz/m1nd"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Local-first context runtime that builds a local code graph per repository served over MCP, with memory anchored to cited code, trust verdicts on answers, and code transplantation across files. Treats refusals and 'insufficient evidence' as first-class answers; multi-agent coordination with presence and mailbox; signed binary updates with rollback; everything stays local with no cloud dependency."
---

Coding agents repeatedly rebuild the same structural picture of a repository and hallucinate cross-file relationships, so m1nd maintains a persistent code graph per repository - built from extractors for 20-plus languages plus document formats - and serves it over MCP to hosts like Claude Code, Cursor, and Codex. Memory persists as plain greppable markdown under agent-memory/, with claims carrying evidence paths, authorship, and supersession, and cross_verify re-hashing cited files to flag stale answers. Multi-agent coordination adds presence detection, collision warnings, and a defect mailbox so parallel agents can share findings. Everything runs locally from a single signed Rust binary with no cloud dependency, and the project is developed agent-first, with coding agents building it under spec-oracle review and worktree-isolated reviewers.
