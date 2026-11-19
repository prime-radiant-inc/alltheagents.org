---
name: "Pizza"
slug: "pizza"
layout: "agent.njk"
category: "agent"
maker: "pizza-agent"
license: "Apache-2.0"
url: "https://github.com/pizza-agent/pizza"
source_code_url: "https://github.com/pizza-agent/pizza"
source_available: "True"
homepage: "https://pizza.hertzbeat.com/"
docs_url: "https://github.com/pizza-agent/pizza#readme"
download_url: "https://github.com/pizza-agent/pizza/releases"
install_method: "Desktop installer from GitHub Releases (macOS/Linux/Windows); or npm install -g @tomsun28/pizza then run pizza"
platforms:
  - "Desktop"
  - "CLI"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "TypeScript"
first_released: "2026-06-25"
current_release: "2026-11-15"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
plugin_docs_url: null
config_docs_url: null
model_providers: "40+ providers via API key or OAuth subscription login — Anthropic, OpenAI, Google, DeepSeek, GLM, Kimi, and more"
pricing: "free"
stars: "51"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "An event-driven agent with no while-true loop: every conversation, tool call, and file edit is an event in an immutable SQLite log, and the UI, LLM context, and branchable session tree are all projections of that log. The model gets a single execution tool — a CLI with first-class _read/_write/_edit commands — and any SSH host can be deployed as a remote workspace."
---

Pizza rejects the conventional while-true agent loop as brittle: each turn is a state machine driven by an event-handler table, so interrupts, retries, parallel tool calls, and mid-turn failures have explicit handlers, and every message, model call, tool result, and file change lands in an immutable SQLite EventStore that the desktop GUI, interactive TUI, JSON-RPC server, and one-shot print mode all consume as projections of one runtime. The shell descends from Pi (the project credits it), but Pizza gives the model a single CLI tool through which it calls _read, _write, _edit, and the other built-in commands — one small schema per call, automatic context compaction, and a git-log-like session tree that forks from any earlier message. Workspaces are location-flexible: point Pizza at a remote machine over SSH and it deploys itself there, a gateway daemon pools long-lived agent processes so one agent can _tell another workspace's agent and get its reply relayed back, and built-in cron plus an always-on main agent keep work running unattended. Its users are developers who want an inspectable, replayable agent log and chat-in-place access: the gateway also connects Slack, Discord, Telegram, Lark, voice, and webhooks to the same agent, with 40+ model providers via API key or OAuth login.
