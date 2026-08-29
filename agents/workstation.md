---
name: "workstation"
slug: "workstation"
layout: "agent.njk"
category: "multiplexer"
maker: "varie-ai"
license: "MIT"
url: "https://github.com/varie-ai/workstation"
source_code_url: "https://github.com/varie-ai/workstation"
source_available: "True"
platforms: []
first_released: "2026-02-06"
current_release: "2026-07-25"
stars: "10"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "no"
plan_mode: "True"
model_providers: "Gemini, Claude, GPT"
pricing: "open-source"
install_method: "Download DMG from GitHub Releases (recommended); install Claude Code plugin via /plugin marketplace add; or build from source (npm install && npm run dev)"
docs_url: "https://github.com/varie-ai/workstation"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/varie-ai/workstation/releases"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Agentic coding orchestrator that lets you control Claude Code from your phone via Telegram or WhatsApp (through OpenClaw). Voice control (WhisperKit/Apple Speech), multi-session management, smart routing by repo name, live notifications with screenshots, plan approvals from phone, and work reports/checkpoints. Ships as an Electron app plus a Claude Code plugin with skills."
---

workstation exists for the case where Claude Code runs autonomously on a Mac but the developer is away from the desk: it pairs with OpenClaw so plans can be approved, questions answered, and commands dispatched from Telegram or WhatsApp, with the bridge detecting finishes and questions and replying with screenshots and notifications. It manages multiple Claude Code sessions with smart routing by repo name, a manager session, checkpoints, and work reports generated through a bundled Claude Code plugin/skills. Voice input uses WhisperKit or Apple Speech entirely on-device, with optional LLM-based routing (Gemini/Claude/GPT) as an opt-in. It is a free, MIT-licensed macOS Electron app installed as a Claude Code plugin marketplace package plus DMG, fully local with no telemetry. Its users are Claude Code developers who want to supervise autonomous sessions from a phone.
