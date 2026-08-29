---
name: "Calyx"
slug: "calyx"
layout: "agent.njk"
category: "multiplexer"
maker: "yuuichieguchi"
license: "MIT"
url: "https://github.com/yuuichieguchi/Calyx"
source_code_url: "https://github.com/yuuichieguchi/Calyx"
source_available: "True"
platforms:
  - "CLI"
  - "Desktop"
first_released: "2026-03-08"
current_release: "2026-08-17"
stars: "292"
language: "Swift"
homepage: "https://help.getcalyx.app/"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, Codex, OpenCode, Hermes, Grok, pi"
pricing: "open-source"
install_method: "brew tap yuuichieguchi/calyx && brew install --cask calyx; or manual download from latest release"
docs_url: "https://help.getcalyx.app"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/yuuichieguchi/Calyx/releases/latest"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Native macOS terminal (built on Ghostty) for running and supervising multiple coding agents (Claude Code, Codex, OpenCode, Hermes, Grok, pi) in parallel. Provides one approval inbox, live agent status sidebar, persistent sessions, agent-readable command history, inline diff review, IPC between agents, LSP proxy, and browser scripting."
---

Calyx exists because running several coding agents in parallel in ordinary terminals means juggling tabs, missing permission prompts, and losing track of which agent is blocked. Built on Ghostty as a native macOS app, it hosts Claude Code, Codex, OpenCode, Hermes, Grok, and pi in panes with a sidebar showing live status, unread badges, and subagent state, while a single approval inbox queues permission requests from every pane for one-by-one review. An agent-readable command history (with secrets redacted) and an MCP server for inter-agent messaging let agents discover and talk to each other; git integration supports inline diff review with comments routed back into the originating agent's pane. Persistent daemon-backed sessions survive restarts, and an LSP proxy plus scriptable browser commands round out the toolkit. It targets developers running agent fleets on macOS who want supervision without leaving the terminal, is distributed via Homebrew cask, and accepts issues but not external pull requests.
