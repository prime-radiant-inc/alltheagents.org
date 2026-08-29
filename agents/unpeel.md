---
name: "Unpeel"
slug: "unpeel"
layout: "agent.njk"
category: "multiplexer"
maker: null
license: null
url: "https://unpeel.com"
source_code_url: null
source_available: "False"
platforms:
  - "CLI"
  - "Desktop"
first_released: null
current_release: null
stars: null
language: "Swift, Rust"
homepage: "https://unpeel.com"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (Claude Code), OpenAI (Codex), Google (Gemini CLI), Moonshot (Kimi), Cline, Cursor, Kiro"
pricing: "Free app download; Unpeel Link remote relay service is a paid subscription"
install_method: "Download macOS app from website; also ships a CLI/TUI (e.g. unpeel --host ssh://your-box)"
docs_url: "https://unpeel.com/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://unpeel.com"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Terminal-first workspace that runs AI agent sessions as persistent hosted processes on your own machine; iPhone remote control via QR pairing; multi-agent orchestration via local Unpeel Sessions MCP; browser automation via your existing Chrome; session forking and markdown export"
---

Unpeel exists because long agent runs are fragile: close the terminal or laptop lid and the session dies, and there is no way to check on or approve an agent's work from away from the desk. It hosts agent sessions (Claude Code, Codex, Gemini CLI, Cursor Agent, Kimi, Cline, Kiro) as processes independent of the UI, so quitting the app leaves them running, while a sidebar dashboard shows busy/done/needs-you status and a menu-bar item pulses on activity. A paired iPhone provides live terminals, input, approvals, and push notifications, with screenshots annotatable and returned into the agent's context; workspaces can also run on any SSH-reachable machine. Developers who step away from their desk — or manage several agents across machines — use it to supervise runs remotely; the app and TUI are free, with the Unpeel Link encrypted relay sold separately, and all state lives in plain files under ~/.unpeel.
