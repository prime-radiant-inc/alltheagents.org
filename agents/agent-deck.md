---
name: "agent-deck"
slug: "agent-deck"
layout: "agent.njk"
category: "multiplexer"
maker: "asheshgoplani"
license: "MIT"
url: "https://github.com/asheshgoplani/agent-deck"
source_code_url: "https://github.com/asheshgoplani/agent-deck"
source_available: True
platforms:
  - "CLI"
first_released: "2025-12-03"
current_release: "2026-08-17"
stars: "754"
language: "Go"
homepage: "https://discord.gg/e4xSs6NBN8"
mcp_support: "yes (built-in MCP Manager with socket pooling; stdio; 85-90% memory reduction)"
plugin_support: "yes (Skills Manager; managed pool workflow; materializes into .claude/skills)"
claude_code_plugin: "yes (/plugin marketplace add asheshgoplani/agent-deck; /plugin install agent-deck@agent-deck)"
subagents: "partial (Conductor: persistent supervisor agents orchestrate/monitor sessions, launch child sessions with parent linkage, auto-respond, escalate via Telegram/Slack)"
hooks: "yes (Claude Code hook integration for cost tracking; Codex notify hooks; transition notifier daemon)"
plan_mode: "no"
model_providers: "Claude, Gemini, OpenCode, Codex, Copilot, Crush, Cursor, DeepSeek Harness; custom endpoints via env vars (e.g., GLM via ANTHROPIC_BASE_URL)"
pricing: "open-source"
install_method: "curl install script, brew, go"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Terminal session manager / mission control for AI coding agents — manage multiple AI agent sessions (Claude Code, Gemini CLI, OpenCode, Codex, Copilot, Cursor, Crush, Hermes Agent) from a single TUI. AI-aware status detection, session forking with inherited context, Conductor orchestration (auto-respond, escalate to phone via Telegram/Slack), MCP socket pooling (85-90% memory reduction), git worktree integration, Docker sandboxing, cost tracking with budget limits, watchers (GitHub webhooks, ntfy, Slack), remote instances, web UI mode."
---

Terminal session manager / mission control for AI coding agents — manage multiple AI agent sessions (Claude Code, Gemini CLI, OpenCode, Codex, Copilot, Cursor, Crush, Hermes Agent) from a single TUI. AI-aware status detection, session forking with inherited context, Conductor orchestration (auto-respond, escalate to phone via Telegram/Slack), MCP socket pooling (85-90% memory reduction), git worktree integration, Docker sandboxing, cost tracking with budget limits, watchers (GitHub webhooks, ntfy, Slack), remote instances, web UI mode.
