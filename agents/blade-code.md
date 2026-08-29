---
name: "blade-code"
slug: "blade-code"
layout: "agent.njk"
category: "agent"
maker: "echoVic"
license: "MIT"
url: "https://github.com/echoVic/blade-code"
source_code_url: "https://github.com/echoVic/blade-code"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2025-05-30"
current_release: "2026-08-19"
stars: "175"
language: "TypeScript"
homepage: "https://echovic.github.io/blade-code/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "38+ providers via pi-ai including OpenAI, Anthropic, DeepSeek, Google, AWS Bedrock, and more"
pricing: "Free / open source (MIT); BYOK with built-in cost tracking (/cost)"
install_method: "npm install -g blade-code, or npx blade-code"
docs_url: "https://github.com/echoVic/blade-code#readme"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Next-generation AI coding assistant with three run modes (CLI terminal, Web UI, Headless JSONL for CI/sandbox). Features 20+ built-in tools, automatic cross-session memory that learns build commands and code patterns, precise multi-turn token cost tracking with cached pricing, four-tier permission system (default/autoEdit/plan/yolo), unified multi-model runtime with 38+ providers via pi-ai with auto-fetched model metadata, and Thinking mode support. Built with React + Ink (terminal) / React + Vite (web)."
---

blade-code is a TypeScript coding agent built on the pi-ai runtime, which unifies more than 38 model providers behind one interface with auto-fetched model metadata such as context windows and pricing. It runs in three modes: a React+Ink terminal UI, a browser-based web UI served by a Hono server, and a headless JSONL mode for CI pipelines and sandboxed automation. Twenty-plus built-in tools cover file editing, search, shell execution, git, and browser automation through a session-isolated Chromium. A four-tier permission system (default, autoEdit, plan, yolo) plus tool allowlists governs autonomy, while a persistent memory layer learns each project's build commands and code patterns across sessions. Cost visibility is built in, with per-turn token and cost tracking that accounts for cached tokens. Individual developers and small teams use it as an open-source, multi-provider alternative to single-vendor agents.
