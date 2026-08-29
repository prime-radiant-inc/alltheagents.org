---
name: "MiMo Code"
slug: "mimo-code"
layout: "agent.njk"
category: "agent"
maker: "XiaomiMiMo"
license: "MIT"
url: "https://github.com/XiaomiMiMo/MiMo-Code"
source_code_url: "https://github.com/XiaomiMiMo/MiMo-Code"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-06-10"
current_release: "2026-08-19"
stars: null
language: "TypeScript"
homepage: "https://mimo.xiaomi.com/mimocode"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "yes"
model_providers: "OpenAI-compatible, Xiaomi MiMo Platform, OpenAI/Codex, Claude Code, xAI/Grok, OpenRouter, custom providers"
pricing: "open-source"
install_method: "curl -fsSL https://mimo.xiaomi.com/install | bash"
docs_url: "https://mimo.xiaomi.com/mimocode"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
what_makes_it_special: "Persistent cross-session memory via SQLite FTS5, subagent orchestration with parallel execution, goal-driven autonomous loops with independent judge models, compose workflows (specs-driven development), self-improvement via /dream and /distill, voice input via MiMo ASR, Max Mode (parallel best-of-N reasoning). Forked from OpenCode."
---

MiMo Code extends OpenCode's terminal harness with the persistence and autonomy layer Xiaomi wanted for long-running work. Memory lives in SQLite with FTS5: project knowledge in MEMORY.md, session checkpoints written by a dedicated checkpoint-writer subagent, scratch notes, and per-task progress logs, all re-injected automatically when a session resumes. The agent operates in build mode (full write permissions), plan mode (read-only exploration and design), or compose mode — a specs-driven workflow isolated from interactive editing — and a /goal condition is judged by an independent model so the loop does not stop prematurely. Deterministic JavaScript workflows orchestrate multi-agent pipelines (deep-research, fact-check, research-experiment built-ins) with bounded retries and parallelization, while subagents spawn on demand and run in parallel with lifecycle tracking. Voice input routes through MiMo ASR, and Max Mode runs best-of-N reasoning in parallel. The project is very active with roughly 12.9k stars, works with any OpenAI-compatible provider plus OAuth against Xiaomi MiMo, OpenAI, and xAI, and explicitly does not run in macOS Terminal.app.
