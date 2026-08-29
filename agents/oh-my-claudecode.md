---
name: "oh-my-claudecode"
slug: "oh-my-claudecode"
layout: "agent.njk"
category: "multiplexer"
maker: "Yeachan-Heo"
license: "MIT"
url: "https://github.com/Yeachan-Heo/oh-my-claudecode"
source_code_url: "https://github.com/Yeachan-Heo/oh-my-claudecode"
source_available: "Yes"
platforms: []
first_released: "2026-01-09"
current_release: "2026-08-18"
stars: "38670"
language: "TypeScript"
homepage: "https://oh-my-claudecode.dev"
mcp_support: "partial (.mcp.json exists; v4.4.0 removed Codex/Gemini MCP servers in favor of CLI-first tmux workers)"
plugin_support: "yes"
claude_code_plugin: "yes (it is itself a Claude Code plugin)"
subagents: "yes"
hooks: "yes"
plan_mode: "yes"
model_providers: "Claude, Codex, Gemini, Antigravity, Grok, Cursor"
pricing: "freemium (free/open source; requires Claude Max/Pro or Anthropic API key; ~$60/mo for multi-AI)"
install_method: "npm"
docs_url: "https://yeachan-heo.github.io/oh-my-claudecode-website"
plugin_docs_url: "https://github.com/Yeachan-Heo/oh-my-claudecode#readme"
config_docs_url: null
download_url: "https://github.com/Yeachan-Heo/oh-my-claudecode"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Teams-first multi-agent orchestration for Claude Code with zero learning curve, offering multiple orchestration modes (Team, Autopilot, Ralph, Ultrawork, UltraQA, Pipeline), smart model routing for cost savings, and cross-provider orchestration via tmux CLI workers."
---

oh-my-claudecode extends Claude Code with a teams-first orchestration layer: a staged pipeline (plan, PRD, execute, verify, fix) using Claude Code's native agent teams, with autopilot and persistent verify-fix loops for autonomous runs. As a plugin plus companion CLI it also spawns tmux worker panes running Codex, Gemini, Antigravity, Grok, or Cursor CLIs, letting one model review another's output. Smart model routing downgrades cheap tasks to smaller models for token savings, and a skill-learning system extracts reusable procedures into project files. Natural-language shortcuts and zero-config defaults target users who do not want to study Claude Code's internals. Installation is via the Claude Code plugin marketplace or npm, with tmux required for team features.
