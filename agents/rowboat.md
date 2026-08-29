---
name: "Rowboat"
slug: "rowboat"
layout: "agent.njk"
category: "agent"
maker: "rowboatlabs"
license: "Apache-2.0"
url: "https://github.com/rowboatlabs/rowboat"
source_code_url: "https://github.com/rowboatlabs/rowboat"
source_available: "Yes"
platforms:
  - "IDE"
  - "Web"
first_released: "2025-01-13"
current_release: "2026-08-20"
stars: "17331"
language: "TypeScript"
homepage: "https://www.rowboatlabs.com"
mcp_support: "yes"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: "Desktop installers for macOS/Windows/Linux from rowboatlabs.com/downloads or GitHub releases; optional API keys (Deepgram, ElevenLabs, Exa, Composio) configured in ~/.rowboat/config"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.rowboatlabs.com/downloads"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "Long-lived memory is the organizing primitive: email, meetings, Slack, and assistant conversations are indexed into an Obsidian-style backlinked graph, and event- or schedule-triggered agents act from that context — including a code mode that drives parallel Claude Code or Codex sessions."
---

Rowboat started as an AI app-builder project and repositioned as a local-first "AI coworker": a desktop app that indexes the user's work into a persistent, backlinked knowledge graph rather than retrieving cold from a vector store on each question. Around that Brain sit working surfaces — an email client that triages and drafts with work context, a meeting note-taker with live transcription, an isolated browser for web tasks, and composable apps — all stored locally as plain Markdown. Background agents fire on events or schedules and can browse, search, and write code, with code mode dispatching parallel sessions to Claude Code or Codex. It is Apache-2.0, runs models locally via Ollama or LM Studio or via hosted API keys, and stores everything as local Markdown. YC S24-backed, it is used by people who want an always-on assistant with memory without shipping their data to a SaaS.
