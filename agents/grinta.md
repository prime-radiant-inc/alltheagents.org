---
name: "Grinta"
slug: "grinta"
layout: "agent.njk"
category: "agent"
maker: "josephsenior"
license: "MIT"
url: "https://github.com/josephsenior/Grinta-Coding-Agent"
source_code_url: "https://github.com/josephsenior/Grinta-Coding-Agent"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Autonomous"
first_released: "2026-01-27"
current_release: "2026-08-19"
stars: "29"
language: "Python"
homepage: "https://josephsenior.github.io/Grinta-Coding-Agent/"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "True"
model_providers: "OpenAI, Anthropic, Google, OpenRouter, Ollama, LM Studio"
pricing: "Free/open source"
install_method: "pipx install grinta (optional extras: grinta[rag], grinta[all])"
docs_url: "https://github.com/josephsenior/Grinta-Coding-Agent/blob/main/docs/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/grinta/"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Local-first autonomous coding agent (v1.0.0) that plans, edits, runs commands, debugs failures, validates results, and continues until software tasks are finished end-to-end. Local-first: control plane, execution, session history, and checkpoints all stay local. Failure recovery via durable event ledger, checkpoints, and reverts. Demonstrated a 4h 33m autonomous run (16,393 events, 373 tool outcomes) reaching FINISHED with no additional user messages. Real LSP and DAP integrations."
---

Grinta is a local-first coding agent that plans, edits files, runs commands, debugs failures, and validates its work until a task completes. Its control plane, session history, and checkpoints stay on the local machine while inference can point at hosted models (OpenAI, Anthropic, Google, OpenRouter) or local ones (Ollama, LM Studio). The architecture emphasizes surviving long runs: a durable event ledger records every step, checkpoints allow reverts, and completion quality gates reduce premature declarations of success, with recovery paths for provider outages, malformed tool calls, and context-window pressure. It integrates real LSP servers and DAP debuggers rather than inferring program state from text, and offers Chat, Plan, and Agent workflows in a terminal UI. The audience is developers who want autonomous execution without a cloud account, with optional policy gates and secret masking for safety.
