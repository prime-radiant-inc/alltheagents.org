---
name: "postmortemthis"
slug: "postmortemthis"
layout: "agent.njk"
category: "multiplexer"
maker: "Softeria"
license: "MIT"
url: "https://github.com/Softeria/postmortemthis"
source_code_url: "https://github.com/Softeria/postmortemthis"
source_available: True
platforms:
  - "CLI"
first_released: "2026-06-15"
current_release: "2026-07-27"
stars: "1"
language: "Rust, Shell"
homepage: "https://postmortemthis.com"
mcp_support: False
plugin_support: True
claude_code_plugin: True
subagents: False
hooks: null
plan_mode: null
model_providers: "Claude Code, Codex, Antigravity, Qwen, Vibe, Grok, Gemini, OpenRouter"
pricing: "Free; usage bills to your own provider accounts"
install_method: "Paste a prompt into your coding agent (Claude Code, Codex, etc.) to create a /postmortemthis skill that downloads postmortemthis.cmd from GitHub Releases; run via echo '...' | sh postmortemthis.cmd. Supports Windows, macOS, Linux."
docs_url: "https://postmortemthis.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Softeria/postmortemthis"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "One tiny script with zero setup runs every major coding agent simultaneously in read-only mode to cross-review your diff and deliver a unified ship/no-ship verdict; no server, no MCP, uses your own provider logins. Antigravity (which lacks a read-only switch) enforces read-only via plan mode."
---

One tiny script with zero setup runs every major coding agent simultaneously in read-only mode to cross-review your diff and deliver a unified ship/no-ship verdict; no server, no MCP, uses your own provider logins. Antigravity (which lacks a read-only switch) enforces read-only via plan mode.
