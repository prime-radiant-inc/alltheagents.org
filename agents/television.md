---
name: "Television"
slug: "television"
layout: "agent.njk"
category: "multiplexer"
maker: "telepath-computer"
license: "MIT"
url: "https://television.run/"
source_code_url: "https://github.com/telepath-computer/television"
source_available: "True"
homepage: null
docs_url: "https://github.com/telepath-computer/television/blob/main/README.md"
download_url: "https://dl.todesktop.com/260923p52umxx/mac/dmg/arm64"
install_method: "Download and install the macOS app from television.run (Apple Silicon, macOS 12+), or paste the install prompt from the site into your agent to set up the browser-based interface; build from source with npm install, npm run build, npm run link, tv serve"
platforms:
  - "Desktop"
  - "Web"
autonomy_level: []
specialization: "general"
language: "TypeScript"
first_released: "2026-10-01"
current_release: "2026-11-19"
maintained: "active"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: null
subagents: "False"
hooks: "False"
plan_mode: "False"
plugin_docs_url: null
config_docs_url: null
model_providers: "works with any agent harness; agents bring their own providers (recommended: Hermes, OpenClaw, Pi, Claude Code, Codex)"
pricing: "free"
stars: "252"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A visual space where your agent pins interactive artifacts — documents, data, visualizations, live web pages and vibe-coded apps — into persistent channels instead of losing them in chat, working alongside whatever harness you already use."
---

Television is built by Telepath (Unternet PBC), a software company working on interfaces for personal agents, on the premise that agents produce work worth seeing rather than scrolling past in a terminal. It consists of three parts: a lightweight server installed on the machine where your agent runs, a skills bundle that teaches the agent how Television works and how to create and modify artifacts, and a client app used as a sidecar next to your existing chat interface. You keep talking to your agent as usual — Claude Code, Pi, Hermes, Codex or OpenClaw, anything that can run commands and write files — and the agent puts artifacts on your Television: cards, interactive views or external web pages, organized into persistent channels you can both return to. The Mac app is the primary distribution, with an experimental browser-based interface for other platforms set up by your own agent following the site's admin guide, and the project is open source under MIT. The README recommends harnesses that support skills and file access, and the repo also contains an experimental, unsupported ACP bridge for hosting an OpenClaw or Hermes chat session that is explicitly not part of the public surface. It suits people who want their agent's output to be inspectable and arranged rather than buried in scrollback.
