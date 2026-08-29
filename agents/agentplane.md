---
name: "AgentPlane"
slug: "agentplane"
layout: "agent.njk"
category: "multiplexer"
maker: "basilisk-labs"
license: "MIT"
url: "https://github.com/basilisk-labs/agentplane"
source_code_url: "https://github.com/basilisk-labs/agentplane"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-01-27"
current_release: "2026-08-19"
stars: "73"
language: "TypeScript"
homepage: "https://agentplane.org"
mcp_support: null
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: null
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: "npm i -g agentplane"
docs_url: "https://agentplane.org"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Git-native control plane for coding agents that wraps agents like Claude Code, Codex, Cursor, and Aider in an approved, verifiable repository workflow with bounded authority, approval gates, supervisor-observed proof, verification, and closure. Features Task lifecycle management, Agent Change Records (ACR), local context management, recipes (TDD, security review, docs update), two workflow modes (direct and branch_pr), DCO-compliant multi-author commits, SLSA provenance, and Ed25519-signed recipes. Has an integrations/hermes-agentplane-plugin directory."
---

Teams adopting coding agents need an enforceable record of who did what, not chat transcripts. AgentPlane divides responsibility three ways: humans set outcomes and approve material risk, coding agents do semantic work inside bounded episodes, and the CLI (semantically blind, mechanically authoritative) owns task state, Git/PR routing, and evidence. Each task advance emits a packet with an objective, writable scope, context, and a typed result schema; agents cannot perform lifecycle transitions or claim formal approvals. Workflows run in direct mode for solo reversible work or branch_pr mode with worktrees, branches, and hosted checks. The tool is aimed at engineering teams that want Git itself to be the durable review surface for agent-driven changes.
