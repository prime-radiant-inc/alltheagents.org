---
name: "Agent-harness-kit"
slug: "agent-harness-kit"
layout: "agent.njk"
category: "multiplexer"
maker: "cardor"
license: "MIT"
url: "https://ahk.cardor.dev"
source_code_url: null
source_available: "Source available"
platforms:
  - "CLI"
first_released: null
current_release: null
stars: null
language: null
homepage: "https://ahk.cardor.dev"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, OpenCode, Codex CLI, Grok Build (works with any MCP-compatible agent)"
pricing: "open-source"
install_method: "npm (npx/npm install @cardor/agent-harness-kit)"
docs_url: "https://stack.cardor.dev/ahk"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@cardor/agent-harness-kit"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "Imposes a five-role agent workflow (Lead, Explorer, Consultant, Builder, Reviewer) where only the Builder may write files, backed by a persistent SQLite log of every action, a health.sh gate that must pass before work starts, and an MCP server exposing task-claim tools to any compatible client."
---

Multi-agent coding setups tend to degrade into several agents freestyling over the same files with no shared memory, so agent-harness-kit scaffolds structure first: ahk init creates a task backlog, a defined workflow with five role-separated agents, and an SQLite-backed log of every action taken. A health gate (health.sh) must pass before any work starts, and the ahk serve command runs a local MCP server exposing tasks.get, tasks.claim, and action tools to MCP-compatible clients like Claude Code, OpenCode, Codex CLI, and Grok Build. Storage works over SQLite, PostgreSQL, or MySQL, and a real-time web dashboard shows live progress. Maintainers who want AI agents to follow an auditable, health-gated process instead of improvising are the audience.
