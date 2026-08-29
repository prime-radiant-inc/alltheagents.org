---
name: "cliclaw"
slug: "cliclaw"
layout: "agent.njk"
category: "multiplexer"
maker: "choiyounggi"
license: "MIT"
url: "https://github.com/choiyounggi/cliclaw"
source_code_url: "https://github.com/choiyounggi/cliclaw"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
  - "Desktop"
  - "Autonomous"
first_released: "2026-05-13"
current_release: "2026-08-19"
stars: "7"
language: "TypeScript"
homepage: "https://www.npmjs.com/package/@younggichoi/cliclaw"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "True"
plan_mode: "True"
model_providers: "Claude Code (Anthropic), Codex (OpenAI), Pi (Earendil), Gemini (Google)"
pricing: "free"
install_method: "bun add -g @younggichoi/cliclaw (or npm install -g @younggichoi/cliclaw); then cliclaw init"
docs_url: "https://github.com/choiyounggi/cliclaw#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@younggichoi/cliclaw"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "macOS daemon that turns a Telegram chat into a remote control for local coding agent CLIs (Claude Code, Codex, Pi, Gemini). Kick off tasks, stream progress, approve/deny dangerous commands, and send follow-ups from your phone. Per-chat per-agent sessions, confirm gate, launchd auto-start, corporate TLS auto-detection. Spawns Claude Code with --permission-mode plan/bypassPermissions and injects a dangerous-command hook."
---

The tool answers a specific gap: coding agents run unattended on a development machine, but the developer is away from the keyboard. A single Bun daemon bridges Telegram to up to four local agent CLIs, streaming responses into the chat, accepting images, and requiring explicit inline-keyboard taps before dangerous commands execute, with silence meaning denial and every decision appended to an audit log. Sensitive-path reads are denied, corporate TLS interception is auto-detected, and a launchd agent keeps it running across reboots. Developers who kick off long agent tasks and leave the desk are the users; it is MIT-licensed, on npm, and actively maintained.
