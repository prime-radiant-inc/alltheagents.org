---
name: "Pi Coding Agent"
slug: "pi-coding-agent-vscode"
layout: "agent.njk"
category: "other"
maker: "pi0"
license: null
url: "https://marketplace.visualstudio.com/items?itemName=pi0.pi-vscode"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-02-26"
current_release: "2026-04-24"
stars: null
language: null
homepage: "https://pi.dev"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "whatever the pi CLI supports (multi-provider; requires the @mariozechner/pi-coding-agent CLI)"
pricing: "free"
install_method: "Install from the VS Code Marketplace"
docs_url: "https://pi.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=pi0.pi-vscode"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "VS Code extension for the pi coding agent"
---

This extension is the pi project's own bridge into VS Code: it runs the pi CLI (a prerequisite, installed globally) in an integrated terminal with full PTY support, then bundles a pi extension that feeds the agent around 25 tools reflecting live editor state. The agent can query active editors, selections, diagnostics, symbols, and definitions, and apply workspace edits synchronized with open buffers, while a footer shows the active file, cursor position, and diagnostic counts inside the TUI. A @pi chat participant brings streamed RPC-backed replies into VS Code Chat, and a package-manager sidebar installs pi extensions, skills, prompts, and themes without leaving the editor. With about 7,800 installs, it serves pi users who want the CLI's autonomy without leaving VS Code, keeping the agent loop itself entirely in pi.
