---
name: "Claudraband"
slug: "claudraband"
layout: "agent.njk"
category: "multiplexer"
maker: "halfwhey"
license: "MIT"
url: "https://github.com/halfwhey/claudraband"
source_code_url: "https://github.com/halfwhey/claudraband"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2026-04-11"
current_release: "2026-04-18"
stars: "283"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (via bundled Claude Code)"
pricing: "free"
install_method: "npm (@halfwhey/claudraband)"
docs_url: "https://github.com/halfwhey/claudraband#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@halfwhey/claudraband"
maintained: "dormant"
sources:
  - "hackernews"
what_makes_it_special: "Power-user wrapper around the Claude Code TUI (CLI: cband): sessions run in a first-class tmux backend so they persist and can be resumed, pending permission prompts can be answered programmatically (cband prompt --select N), non-interactive runs support sessions like claude -p, an HTTP daemon (cband serve) enables headless remote control, and an ACP server lets editors such as Zed drive Claude Code through it; ships a TypeScript library and bundles Claude Code, with auth handled entirely by Claude Code itself."
---

The project exists because Claude Code's TUI is interactive-first: sessions die with the terminal, and automation means re-prompting by hand. claudraband keeps real Claude Code sessions alive in tmux, records their state under ~/.claudraband, and exposes operations - answer this pending prompt, resume this session, run this prompt non-interactively - as CLI commands, an HTTP API, an ACP server, and a TypeScript library. Nothing about the agent is re-implemented or patched; the bundled Claude Code handles authentication and behavior, which keeps the wrapper robust across upstream changes at the cost of depending on its release cadence. It is experimental, MIT-licensed, and aimed at individual power users rather than SDK users.
