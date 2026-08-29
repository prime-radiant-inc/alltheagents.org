---
name: "SpecBuddy"
slug: "specbuddy"
layout: "agent.njk"
category: "multiplexer"
maker: "SpecBuddy"
license: "Proprietary (SpecBuddy EULA)"
url: "https://plugins.jetbrains.com/plugin/32645-specbuddy"
source_code_url: null
source_available: "no"
platforms:
  - "IDE"
first_released: "2026-08-24"
current_release: null
stars: null
language: null
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "free"
install_method: "Install from the JetBrains Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/32645-specbuddy"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Structured plan-to-step control layer over AI coding agents"
---

SpecBuddy exists because chat-driven coding only reveals an agent's misunderstanding after the diff exists. Its workflow starts with a Markdown spec in the editor — the agent can expand a short draft into a full specification — which becomes a step-by-step plan the developer edits and approves before any code is generated. Execution happens step by step in a dedicated git worktree via Claude Code or Codex running in the IDE terminal, with pre/post snapshots making rollback safe at every step, and inline comments can send a step back with feedback. Developers who prefer plain chat get the same diff-review-rollback wrapper without a spec. It is free, closed source under a vendor EULA, and entered the JetBrains Marketplace in August 2026.
