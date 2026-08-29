---
name: "handoff"
slug: "handoff"
layout: "agent.njk"
category: "multiplexer"
maker: "dazuiba"
license: "MIT"
url: "https://github.com/dazuiba/handoff"
source_code_url: "https://github.com/dazuiba/handoff"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-06-05"
current_release: "2026-08-02"
stars: "85"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "yes"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "DeepSeek, Claude (Anthropic), Codex (OpenAI), Gemini (Google), Kimi (Moonshot)"
pricing: "open-source"
install_method: "uv tool install handoff-cli"
docs_url: "https://github.com/dazuiba/handoff/blob/main/docs/configuration.zh-CN.md"
plugin_docs_url: null
config_docs_url: "https://github.com/dazuiba/handoff/blob/main/docs/cli-reference.zh-CN.md"
download_url: "https://pypi.org/project/handoff-cli/"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "CLI tool that lets coding agents (Claude Code, Codex) delegate tasks to other models (DeepSeek, Gemini, Opus, etc.) in the background without blocking the main session or losing context. Supports parallel tasks, session resume, TUI task browser (handoff list/tail), and Claude skills + Codex custom agents. Custom backends configurable via config."
---

handoff solves the cost and context problems of doing everything inside one expensive agent session. From inside Claude Code or Codex, the user dispatches a task to a named backend — DeepSeek by default, with Gemini, Codex, Claude Opus, and custom Anthropic-compatible endpoints configurable — and handoff runs the target agent's CLI in an isolated background process, streaming output to disk instead of into the parent conversation. The parent session receives only a RESULT file path it can read when convenient, and follow-up commands reattach to the same run, preserving the worker's accumulated context. Tasks can run in parallel, be followed live with handoff tail, and be reviewed in an interactive task-history TUI. The intended pattern pairs a premium planning model with inexpensive execution models, and the project documents itself primarily in Chinese with English README support.
