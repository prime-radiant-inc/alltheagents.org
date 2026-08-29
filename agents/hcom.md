---
name: "hcom"
slug: "hcom"
layout: "agent.njk"
category: "multiplexer"
maker: "aannoo"
license: "MIT"
url: "https://github.com/aannoo/hcom"
source_code_url: "https://github.com/aannoo/hcom"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-07-21"
current_release: "2026-08-09"
stars: "457"
language: "Rust"
homepage: "https://pypi.org/project/hcom/"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "no"
model_providers: "Claude Code, Codex CLI, Antigravity CLI, OpenCode, Kilo Code, Pi, Oh My Pi, Cursor CLI, Kimi, Gemini CLI, Copilot CLI"
pricing: "Free / open-source (MIT)"
install_method: "Homebrew (brew install aannoo/hcom/hcom), pip/uv (pip install hcom), shell installer, PowerShell installer, or build from source with Rust 1.88+"
docs_url: "https://github.com/aannoo/hcom#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/aannoo/hcom/releases/latest/download/hcom-installer.sh"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Single Rust binary CLI that lets coding agents message, watch, and spawn each other across terminals in real time; agents observe transcripts/file edits/terminal screens, subscribe to events, and spawn/fork/resume/kill each other, with MQTT relay and end-to-end encryption across machines"
---

hcom solves the isolation problem when developers run several coding agents at once: agents cannot see each other's work, so they duplicate effort or conflict. hcom installs lightweight hooks into each supported CLI (Claude Code, Codex, Gemini CLI, Cursor, Kimi, and others) that write activity to a local SQLite database, which doubles as a message bus — agents send and receive threaded messages mid-turn, observe each other's transcripts and file edits, and get alerted when two agents touch the same file within 30 seconds. Beyond messaging, one agent can spawn, fork, or terminate another, including running different vendors' CLIs as each other's subagents, and workflow scripts coordinate patterns like debates. An optional end-to-end-encrypted MQTT relay extends the same mesh across machines. It ships as a single Rust binary with hooks that install into existing agent configs.
