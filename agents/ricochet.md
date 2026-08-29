---
name: "ricochet"
slug: "ricochet"
layout: "agent.njk"
category: "agent"
maker: "Grik-ai"
license: "Apache-2.0"
url: "https://github.com/Grik-ai/ricochet"
source_code_url: "https://github.com/Grik-ai/ricochet"
source_available: "True"
platforms:
  - "IDE"
  - "Autonomous"
first_released: "2025-06-08"
current_release: "2026-07-08"
stars: "55"
language: "Go, TypeScript"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: "True"
model_providers: "OpenRouter, OpenAI, Anthropic, Mistral, DeepSeek, Z.AI, xAI, MiniMax"
pricing: "freemium"
install_method: "VS Code Marketplace: ext install grik.ricochet; or installer script curl -fsSL https://grik.io/ricochet/install | sh"
docs_url: "https://github.com/Grik-ai/ricochet#readme"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Local-first AI coding agent with a native Go core for VS Code-compatible editors and terminal; review-before-apply edits, checkpoints (workspace snapshots), and an optional Ether/Live Mode for remote control via Telegram/Discord."
---

Ricochet exists for developers who want one agent across VS Code-compatible editors and the terminal without giving up control over what gets written to disk. The Go core runs the inspect-plan-edit-verify loop, routes to whichever provider the user configures — hosted Grik models or BYOK keys for OpenAI, Anthropic, OpenRouter, Mistral, DeepSeek, and others — while the TypeScript layer supplies the VS Code extension and webview UI. A task timeline records every read, search, command, edit, and approval, and checkpoints allow rolling the workspace back to any prior state. MCP servers and project instruction skills extend the tool surface, and remote steering over Telegram or Discord targets people who kick off long tasks and monitor from elsewhere. The project is young, with a small commit history and no GitHub releases yet.
