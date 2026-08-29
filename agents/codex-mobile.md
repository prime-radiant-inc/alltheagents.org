---
name: "codex-mobile"
slug: "codex-mobile"
layout: "agent.njk"
category: "multiplexer"
maker: "friuns2"
license: "MIT"
url: "https://github.com/friuns2/codex-mobile"
source_code_url: "https://github.com/friuns2/codex-mobile"
source_available: "True"
platforms:
  - "Desktop"
first_released: "2026-02-21"
current_release: "2026-05-26"
stars: "871"
language: "TypeScript"
homepage: "https://friuns2.github.io/codex-mobile/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Claude, DeepSeek, Gemini, GLM, GPT, Grok, Kimi, MiniMax, Qwen"
pricing: "open-source"
install_method: "npm"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Lightweight bridge exposing the Codex app-server as a browser-accessible web UI; runs on Android via Termux; one-command launch (npx codexapp); Telegram bot bridge; voice dictation; project ZIP export/import with chat rewriting."
---

Codex-mobile addresses a practical constraint: Codex's desktop experience runs on one machine, but operators often want to check on or steer sessions from a phone or another computer. The tool runs a local Express and Vue server that bridges HTTP and WebSocket traffic to the Codex app-server over RPC, making the Codex interface available in any browser on the network or, through an optional built-in Cloudflare tunnel, from anywhere with a QR-code pairing flow and password protection. Beyond remote access it adds voice dictation, a Telegram bot bridge for allowlisted users to interact with a mapped Codex thread, and project portability through ZIP export and import that rewrites chat history for a destination CODEX_HOME, project path, and provider. It runs on Linux, Windows, and Android via Termux, launched with npx codexapp, and is developed openly on GitHub.
