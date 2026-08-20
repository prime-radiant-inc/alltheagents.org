---
name: "Bernstein"
slug: "bernstein"
layout: "agent.njk"
category: "agent"
maker: "sipyourdrink-ltd"
license: "Apache-2.0"
url: "https://github.com/chernistry/bernstein"
source_code_url: "https://github.com/chernistry/bernstein"
source_available: True
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-03-22"
current_release: "2026-08-19"
stars: "936"
language: "Python"
homepage: "https://bernstein.run"
mcp_support: "yes — MCP server mode, .mcp.json present"
plugin_support: "yes — .plugin directory, plugin.json, agent catalogs"
claude_code_plugin: "no"
subagents: "yes — manager decomposes goals into tasks with roles; 49 selectable agent adapters"
hooks: "yes — hooks/ directory in repo"
plan_mode: "yes — bernstein run plan.yaml for multi-stage plans"
model_providers: "Claude Code, Codex, Gemini CLI, GitHub Copilot, Cursor, Aider, Goose, Ollama, OpenCode, OpenHands, and 39+ more CLI agent adapters"
pricing: "open-source"
install_method: "pip"
docs_url: "https://bernstein.readthedocs.io/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
  - "jim"
  - "caramaschi"
what_makes_it_special: "Deterministic orchestrator for CLI coding agents with no LLM in the coordination loop — replay yesterday's plan and get yesterday's task graph byte-identical; cryptographic checkability with Ed25519-signed receipts; each task gets its own git worktree; air-gap deployable."
---

Deterministic orchestrator for CLI coding agents with no LLM in the coordination loop — replay yesterday's plan and get yesterday's task graph byte-identical; cryptographic checkability with Ed25519-signed receipts; each task gets its own git worktree; air-gap deployable.
