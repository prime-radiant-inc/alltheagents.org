---
name: "PATAPIM"
slug: "patapim"
layout: "agent.njk"
category: "multiplexer"
maker: null
license: "Proprietary (main app); open-source TypeScript SDK (@patapim/sdk)"
url: "https://patapim.ai"
source_code_url: null
source_available: "Partial (SDK is open-source; main app is commercial)"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
first_released: null
current_release: null
stars: null
language: "TypeScript (SDK)"
homepage: "https://patapim.ai"
mcp_support: "yes (plugins can register MCP tools that automatically show up in Claude Code sessions)"
plugin_support: "yes (extensible plugin system with marketplace, local API, TypeScript SDK — @patapim/sdk is open-source)"
claude_code_plugin: "yes (enhancement layer for Claude Code)"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude, Codex, Antigravity, Gemini, or any custom CLI"
pricing: "Free: $0 (3 terminals, 30 min dictation); Pro: $6.99/mo (unlimited); Lifetime: $59.99 one-time"
install_method: "patapim install; macOS: curl install-mac.sh | bash; Windows: PowerShell irm install.ps1 | iex"
docs_url: "https://patapim.ai/docs/releases"
plugin_docs_url: null
config_docs_url: "https://patapim.ai/docs/extensibility/local-api"
download_url: null
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Terminal IDE enhancement for Claude Code with 9-terminal grid for running multiple CLI coding agents simultaneously; full computer control (drives mouse/keyboard) and embedded per-terminal Chrome browsers using existing AI subscription (zero extra API costs); 100% local Whisper voice dictation; zero-setup LAN remote control; organizes projects by folders rather than chats."
---

PATAPIM grew from a solo developer's setup into a terminal manager for people running multiple CLI coding agents, wrapping Claude Code, Codex, Antigravity, Gemini, or any custom CLI in a nine-terminal grid organized by project folder rather than chat history. Beyond window management it adds capabilities the underlying CLIs lack: a local Whisper dictation layer for voice input, an embedded Chrome instance per terminal that agents can see and drive, full mouse/keyboard computer control, and zero-configuration LAN remote access from a phone or second desktop. An isolated plugin system registers MCP tools that automatically appear in every Claude Code session, adds UI panels and scheduled tasks, and is extensible through a TypeScript SDK with a marketplace. Because it wraps the user's own subscriptions, there are no per-token charges beyond the app's own tiers. Its users are solo developers and small teams running several agent sessions at once.
