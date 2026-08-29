---
name: "postmortemthis"
slug: "postmortemthis"
layout: "agent.njk"
category: "multiplexer"
maker: "Softeria"
license: "MIT"
url: "https://github.com/Softeria/postmortemthis"
source_code_url: "https://github.com/Softeria/postmortemthis"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-06-15"
current_release: "2026-07-27"
stars: "1"
language: "Rust, Shell"
homepage: "https://postmortemthis.com"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "False"
hooks: "no"
plan_mode: "no"
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

Postmortemthis starts from the observation that the agent which wrote your code is the worst judge of it, so a diff deserves review by models that had no hand in producing it. Piping one prompt into its small Rust launcher fans the review out to Claude Code, Codex, Antigravity, Qwen, Vibe, and Grok in parallel, each forced read-only through its own CLI flags so the working tree cannot change mid-run. There is deliberately no server, no MCP, and no resold access: agents you are logged into review directly, and OpenRouter covers the rest through a setup subcommand. Results aggregate into a single ship or no-ship call before a real postmortem happens. It is aimed at developers who already run several agent CLIs and want cross-model second opinions with zero setup.
