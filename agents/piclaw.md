---
name: "piclaw"
slug: "piclaw"
layout: "agent.njk"
category: "agent"
maker: "rcarmo"
license: "MIT"
url: "https://github.com/rcarmo/piclaw"
source_code_url: "https://github.com/rcarmo/piclaw"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-02-17"
current_release: "2026-08-19"
stars: "823"
language: "TypeScript"
homepage: "https://rcarmo.github.io/projects/piclaw/"
mcp_support: "yes (built-in via pi-mcp-adapter)"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes (workspace env hook via /workspace/.env.sh)"
plan_mode: "no"
model_providers: "multi-provider, OpenAI-compatible, Azure OpenAI, llama.cpp"
pricing: "open-source"
install_method: "docker"
docs_url: "https://github.com/rcarmo/piclaw/blob/main/docs/configuration.md"
plugin_docs_url: null
config_docs_url: "https://github.com/rcarmo/piclaw/blob/main/docs/configuration.md"
download_url: "https://github.com/rcarmo/piclaw"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Self-hosted, single-user, mobile-friendly AI workspace packaging the Pi coding agent with a trilingual (English/Chinese/Japanese) streaming web UI, SQLite-backed persistent state, built-in tools (code editing, viewers, VNC, browser automation), optional auth (passkeys/TOTP), WhatsApp integration, and an extensible add-on system."
---

piclaw packages the pi coding agent into a self-contained workspace for people who want it reachable from a phone: one Docker container serves a streaming web UI with an editor, terminal, and file viewers, with state in SQLite and sessions persistent across reconnects. The workspace is deliberately single-user and local-first, with optional passkey or TOTP authentication, staged tool loading to keep prompts lean, and an add-on system that layers on Ghostty terminal, Draw.io, Office document rendering, Windows desktop automation, Proxmox, and a WhatsApp bridge. MCP support arrives via the pi-mcp-adapter, and an experimental Electrobun desktop shell wraps the same stack natively. With over four thousand commits and an active issue triage board, development is continuous, and the author runs it as a personal infrastructure project documented in depth. Its audience is self-hosters who want their coding agent reachable, authenticated, and persistent from any device.
