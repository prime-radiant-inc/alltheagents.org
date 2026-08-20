---
name: "handoff"
slug: "handoff"
layout: "agent.njk"
category: "multiplexer"
maker: "dazuiba"
license: null
url: "https://github.com/dazuiba/handoff"
source_code_url: "https://github.com/dazuiba/handoff"
source_available: True
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-06-05"
current_release: "2026-08-02"
stars: "85"
language: "Python"
homepage: null
mcp_support: null
plugin_support: True
claude_code_plugin: null
subagents: True
hooks: null
plan_mode: null
model_providers: "DeepSeek, Claude (Anthropic), Codex (OpenAI), Gemini (Google), Kimi (Moonshot)"
pricing: null
install_method: "uv tool install handoff-cli"
docs_url: "https://github.com/dazuiba/handoff/blob/main/docs/configuration.zh-CN.md"
plugin_docs_url: null
config_docs_url: "https://github.com/dazuiba/handoff/blob/main/docs/cli-reference.zh-CN.md"
download_url: null
maintained: null
sources:
  - "brad"
what_makes_it_special: "CLI tool that lets coding agents (Claude Code, Codex) delegate tasks to other models (DeepSeek, Gemini, Opus, etc.) in the background without blocking the main session or losing context. Supports parallel tasks, session resume, TUI task browser (handoff list/tail), and Claude skills + Codex custom agents. Custom backends configurable via config."
---

CLI tool that lets coding agents (Claude Code, Codex) delegate tasks to other models (DeepSeek, Gemini, Opus, etc.) in the background without blocking the main session or losing context. Supports parallel tasks, session resume, TUI task browser (handoff list/tail), and Claude skills + Codex custom agents. Custom backends configurable via config.
