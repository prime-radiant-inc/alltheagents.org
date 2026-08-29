---
name: "Kata"
slug: "kata"
layout: "agent.njk"
category: "other"
maker: "kenn-io"
license: "MIT"
url: "https://github.com/kenn-io/kata"
source_code_url: "https://github.com/kenn-io/kata"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-04-30"
current_release: "2026-08-20"
stars: "389"
language: "Go"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: "True"
plan_mode: null
model_providers: null
pricing: "Free / open-source (MIT)"
install_method: "brew install kata, or curl -fsSL https://katatracker.com/install.sh | bash, or go install go.kenn.io/kata/cmd/kata@latest"
docs_url: "https://katatracker.com/"
plugin_docs_url: null
config_docs_url: "docs/reference/configuration.md (in-repo)"
download_url: "https://katatracker.com/install.sh"
maintained: "active"
sources:
  - "author_search"
what_makes_it_special: "Issue tracker built for coding agents and humans; native stdio MCP server with 13 section loaders; stable short refs; --json/--agent output; idempotent creates; semantic-aware search; claim flow; evidence-based closes; local-first single Go binary with SQLite; human TUI + browser UI over same data; optional remote daemon/federation/Postgres."
---

Coding agents lose track of work when state lives in chat transcripts or ad-hoc TODO files, so kata provides a durable task ledger the agent can query and update through the same CLI humans use. It runs as a local SQLite-backed binary with an MCP server (stdio or Streamable HTTP) exposing fourteen progressive section loaders, plus --json/--agent output modes, idempotent creates, and a claim flow that prevents two agents from taking the same issue. Optional remote daemons, federation, and Postgres back it for shared deployments. It is used by developers running Claude Code, Codex, and similar agents who want auditable, agent-writable project tracking without a SaaS tracker.
