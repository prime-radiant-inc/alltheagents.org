---
name: "Superset"
slug: "superset"
layout: "agent.njk"
category: multiplexer
maker: "superset-sh"
license: "Elastic License 2.0 (ELv2)"
url: "https://github.com/superset-sh/superset"
source_code_url: "https://github.com/superset-sh/superset"
source_available: "Source-visible (no OSS license)"
platforms:
  - "CLI"
  - "IDE"
first_released: "2025-10-21"
current_release: "2026-08-20"
stars: "13105"
language: "TypeScript (Bun, React, Electron)"
homepage: "https://superset.sh"
mcp_support: "yes (MCP server; transport not specified)"
plugin_support: "yes (custom agents, skills, terminal presets, themes)"
claude_code_plugin: "yes (fully supported agent; .claude-plugin and .claude directories present)"
subagents: "yes (.agents directory; built-in orchestration skills for parallel agents)"
hooks: "yes (setup/teardown/run scripts)"
plan_mode: "yes (inline tool approvals and plan review)"
model_providers: "OpenRouter, Bedrock, Vertex, Vercel AI Gateway (BYO providers); Claude, OpenAI/Codex, Gemini, Grok, Mistral, Kimi"
pricing: "free (desktop app free forever; optional paid services)"
install_method: "brew"
docs_url: "https://docs.superset.sh"
plugin_docs_url: "https://docs.superset.sh/agent-integration"
config_docs_url: "https://docs.superset.sh/setup-teardown-scripts"
download_url: "https://github.com/superset-sh/superset/releases/latest"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Agentic IDE that orchestrates 100+ CLI coding agents (Claude Code, Codex, Cursor, etc.) in parallel across isolated git worktrees, with built-in terminal, diff viewer, in-app browser, MCP server, CLI, and SDK — all free forever for local use."
---

Agentic IDE that orchestrates 100+ CLI coding agents (Claude Code, Codex, Cursor, etc.) in parallel across isolated git worktrees, with built-in terminal, diff viewer, in-app browser, MCP server, CLI, and SDK — all free forever for local use.
