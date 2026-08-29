---
name: "Untether"
slug: "untether"
layout: "agent.njk"
category: "multiplexer"
maker: "littlebearapps"
license: "MIT"
url: "https://github.com/littlebearapps/untether"
source_code_url: "https://github.com/littlebearapps/untether"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-02-07"
current_release: "2026-08-17"
stars: "64"
language: "Python"
homepage: "https://untether.cc"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "True"
plan_mode: "True"
model_providers: "Claude Code (Anthropic), Codex (OpenAI), OpenCode, Pi, Gemini CLI (Google), Amp (Sourcegraph)"
pricing: "Free / open source; uses existing Claude or ChatGPT subscription"
install_method: "uv tool install untether (recommended) or pipx install untether"
docs_url: "https://github.com/littlebearapps/untether/tree/master/docs"
plugin_docs_url: null
config_docs_url: "https://github.com/littlebearapps/untether/blob/master/docs/reference/config.md"
download_url: "https://pypi.org/project/untether/"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Telegram bridge for AI coding agents — send tasks by voice/text from your phone, stream progress live, approve changes remotely; supports custom engines, transports, and commands"
---

Untether solves the away-from-desk problem in agent-driven development: tasks finish or stall while the developer is away, and there is no mobile surface for progress or approvals. A local Python process bridges agent CLIs — Claude Code, Codex, OpenCode, Pi, Gemini CLI, Amp — to a Telegram bot, streaming tool calls and file changes in real time, converting permission requests into inline buttons, and transcribing voice notes through a configurable Whisper-compatible endpoint. It adds scheduled tasks (cron, webhooks, one-shot /at delays), cost tracking against per-run and daily budgets, projects and worktrees organized as forum topics, file transfer, session export, and cross-environment resume so work started in a terminal can continue in Telegram. Developers managing agents from their phone use it; it installs via uv/pipx, drives agents through their existing subscriptions, and ships with no telemetry and token redaction in logs.
