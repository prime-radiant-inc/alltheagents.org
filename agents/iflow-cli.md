---
name: "iFlow CLI"
slug: "iflow-cli"
layout: "agent.njk"
category: "agent"
maker: "Alibaba (Xinliu)"
license: null
url: "https://platform.iflow.cn"
source_code_url: null
source_available: null
platforms:
  - "CLI"
first_released: null
current_release: null
stars: null
language: null
homepage: "https://platform.iflow.cn/cli"
mcp_support: "yes"
plugin_support: null
claude_code_plugin: null
subagents: "yes"
hooks: null
plan_mode: "yes"
model_providers: null
pricing: "free"
install_method: "curl install script (cloud.iflow.cn), Homebrew, or npm i -g @iflow-ai/iflow-cli (Node.js 22+)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dead"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Free Chinese terminal coding agent"
---

iFlow CLI put Alibaba-affiliated open platform models — Kimi K2, Qwen3 Coder, DeepSeek V3, GLM 4.5 — behind a free terminal agent built on the Gemini CLI codebase. It ran four permission modes including plan mode, dispatched preconfigured SubAgents with automatic context compression at 70%, and installed MCP tools and workflows from a curated marketplace. Configuration stayed OpenAI-compatible via ~/.iflow/settings.json, and plugins reached VS Code and JetBrains IDEs. The economics relied on the iFlow open platform absorbing model costs, which is the part that ended: the team announced service shutdown for April 17, 2026 and pointed users to Qoder CLI for migration.
