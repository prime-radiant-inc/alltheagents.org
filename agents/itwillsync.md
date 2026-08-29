---
name: "itwillsync"
slug: "itwillsync"
layout: "agent.njk"
category: "multiplexer"
maker: "shrijayan"
license: "MIT"
url: "https://github.com/shrijayan/itwillsync"
source_code_url: "https://github.com/shrijayan/itwillsync"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
first_released: "2026-02-26"
current_release: "2026-08-07"
stars: "97"
language: "TypeScript"
homepage: "https://shrijayan.github.io/itwillsync/"
mcp_support: "no"
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "Free / open-source (MIT)"
install_method: "npx itwillsync <command> (Node.js 20+)"
docs_url: "https://shrijayan.github.io/itwillsync/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Syncs any terminal-based AI coding agent to your phone over a local network (WiFi/Tailscale/localhost); privacy-first E2E encrypted with per-session NaCl secretbox tokens, zero cloud/accounts/telemetry; multi-session dashboard with attention detection and sleep prevention; agent-agnostic (works with Claude Code, Aider, Codex, Goose, Cline, Copilot CLI, or any terminal tool)."
---

itwillsync answers a small but constant pain: your agent is working, but you are not at the desk. It wraps the agent command in a PTY, streams the terminal over an encrypted WebSocket, and renders it in a mobile browser after a QR scan — approve prompts, type commands, and watch output from a phone. A hub daemon tracks all running sessions with attention detection and can keep the machine awake during long runs. Everything stays on the local network or Tailscale, encrypted end-to-end with per-session NaCl keys and no accounts. It is deliberately agent-agnostic plumbing rather than an agent itself.
