---
name: "SKI"
slug: "ski"
layout: "agent.njk"
category: "other"
maker: "pattern-ai-labs"
license: "Proprietary"
url: "https://heyski.io/"
source_code_url: null
source_available: "False"
platforms:
  - "Desktop"
first_released: "2026-07-27"
current_release: "2026-07-27"
stars: null
language: null
homepage: "https://heyski.io/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "delegates to the connected agents (Claude Code, Codex, Cursor, Gemini CLI, Windsurf, OpenClaw)"
pricing: "freemium"
install_method: "Download the desktop app from heyski.io (macOS 14.4+ Apple Silicon, Windows 10/11 x64, Ubuntu/Debian x64)"
docs_url: "https://heyski.io/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/pattern-ai-labs/ski-releases"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A two-way voice layer for coding agents that runs fully on-device: on-device speech-to-text hands text to the agent over plain files inside the project (no daemon, no cloud), and the reply is spoken aloud with full-duplex barge-in, while the agent itself does the coding."
---

SKI is a free desktop app from Pattern AI Labs that adds voice to the coding agent you already use. You speak, on-device speech recognition transcribes it, the text goes to Claude Code, Codex, Cursor, Gemini CLI, Windsurf, or OpenClaw through a small skill file, and the agent's reply is spoken back in a natural voice — with full-duplex barge-in so you can interrupt mid-sentence, approve-before-send transcript review, per-project voices, global hotkeys, and on Mac a floating pill or notch display. Communication happens over plain files inside the project with no daemon and no cloud, and both recognition and the neural voice run locally, so no audio or transcripts are uploaded and it works offline. The voice loop is free for life; the only paid feature is AgentCall, which sends your agent into Zoom, Meet, or Teams calls as a per-minute cloud participant. It is a voice interface layer rather than a coding agent, included here as agent tooling.
