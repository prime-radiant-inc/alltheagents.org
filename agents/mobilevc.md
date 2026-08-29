---
name: "MobileVC"
slug: "mobilevc"
layout: "agent.njk"
category: "multiplexer"
maker: "JayCRL"
license: "MIT"
url: "https://github.com/JayCRL/MobileVC"
source_code_url: "https://github.com/JayCRL/MobileVC"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-03-19"
current_release: "2026-06-30"
stars: "209"
language: "Go, Dart (Flutter)"
homepage: "https://www.mobilevc.top"
mcp_support: null
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: "True"
model_providers: "Claude Code, OpenAI Codex (manages local CLI sessions)"
pricing: "Free / open-source"
install_method: "npm install -g @justprove/mobilevc; mobilevc start (mobile app via TestFlight/APK)"
docs_url: "https://www.mobilevc.top"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@justprove/mobilevc"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Turns a phone into a control center for AI coding assistant CLI sessions (Claude/Codex) on a computer, structuring high-frequency waiting states into actionable mobile workflows (buttons/cards) rather than mirroring a terminal. Supports LAN or encrypted Relay, diff approvals, Plan Mode advancement, and voice pre-communication."
---

Agentic CLI sessions spend most of their wall-clock time waiting for a human — to approve a permission, advance a plan, accept a diff — and that waiting usually pins the developer to their desk. MobileVC turns the phone into the approval surface: a Go server wraps local Claude Code or Codex CLI sessions in a PTY with a WebSocket event stream, and a Flutter app renders pending decisions as buttons and diff cards rather than a tiny terminal. Sessions can be started, continued, and restored from history; files, logs, and run state are browsable; and plan-mode advancement plus voice pre-communication let a user brief the agent verbally before handing off. Connectivity runs over LAN with QR-scan token auth or through an encrypted relay whose server never sees plaintext, and an ADB/WebRTC bridge adds Android emulator debugging from the phone. Developers running long unattended agent sessions use it to keep work moving from anywhere.
