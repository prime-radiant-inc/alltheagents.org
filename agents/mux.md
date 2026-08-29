---
name: "mux"
slug: "mux"
layout: "agent.njk"
category: "agent"
maker: "coder"
license: "AGPL-3.0"
url: "https://github.com/coder/mux"
source_code_url: "https://github.com/coder/mux"
source_available: "Yes"
platforms:
  - "Desktop"
first_released: "2025-09-17"
current_release: "2026-08-20"
stars: "1977"
language: "TypeScript"
homepage: "https://mux.coder.com"
mcp_support: "yes (.mcp.json config present)"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "yes"
model_providers: "Anthropic, OpenAI, xAI, Ollama (local), OpenRouter"
pricing: "open-source"
install_method: "binary"
docs_url: "https://mux.coder.com"
plugin_docs_url: null
config_docs_url: "https://mux.coder.com/config/models"
download_url: "https://github.com/coder/mux/releases"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Desktop and browser application for isolated, parallel agentic development with a custom agent loop inspired by Claude Code. Features a central view on git divergence, opportunistic compaction, mode prompts, and execution across local, worktree, or remote SSH environments."
---

Mux, built by Coder, addresses the chaos of running multiple AI coding agents in parallel: each agent gets an isolated workspace — local directory, git worktree, or remote SSH host — while a central git-divergence view shows exactly how each agent's branch diverged from the shared base. The custom agent loop borrows Claude Code's interaction model (plan and execution modes, opportunistic context compaction, mode prompts) and runs against Anthropic, OpenAI, xAI, OpenRouter, or local Ollama models. Workspaces support local directories, git worktrees, and remote SSH environments, with a VS Code extension for jumping between them, integrated code review, and cost/token tracking per agent. A trademark conflict with the media-infrastructure company Mux.com forced a rename to Xum, though documentation remains at mux.coder.com during the transition. Developers running several agents concurrently — often with different models on the same task — use it to keep each agent's changes reviewable in isolation; the project is AGPL-3.0, actively developed, and self-hosted by design rather than a cloud service.
