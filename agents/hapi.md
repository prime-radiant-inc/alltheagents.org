---
name: "hapi"
slug: "hapi"
layout: "agent.njk"
category: "multiplexer"
maker: "tiann"
license: "AGPL-3.0"
url: "https://github.com/tiann/hapi"
source_code_url: "https://github.com/tiann/hapi"
source_available: "True"
platforms: []
first_released: "2025-12-24"
current_release: "2026-08-20"
stars: "4834"
language: "TypeScript"
homepage: "https://hapi.run"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, Codex, Cursor Agent, Grok Build, OpenCode, Kimi, Copilot, Antigravity, Pi"
pricing: "open-source"
install_method: "npm"
docs_url: "https://hapi.run"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Local-first tool to run official AI coding agent sessions locally and control them remotely via Web/PWA/Telegram Mini App. Wraps existing AI agents (not replacing them), seamless local↔remote handoff with no context loss, AFK one-tap phone approval, E2E encryption via WireGuard + TLS relay, voice control, native mobile apps (Swift/Kotlin) in development."
---

hapi solves the problem of walking away from a running coding agent: the work happens on your machine, but you may not be at your desk when it needs approval or finishes. It wraps official agent CLIs — Claude Code, Codex, Cursor Agent, Grok Build, OpenCode, and others — in a local hub that relays session state to a web app, PWA, or Telegram Mini App, with QR-code pairing and end-to-end encryption through a self-hostable relay. Because it wraps the real agent process rather than replacing it, a session started in the terminal continues identically when control switches to a phone and back, and pending permission requests can be approved remotely with one tap. A terminal view, workspace-scoped file browsing, and voice input extend what the phone can do, while native iOS and Android apps are in development. It is AGPL-licensed, actively developed, and positioned as a self-hosted alternative to the Happy project.
