---
name: "claw-code-agent"
slug: "claw-code-agent"
layout: "agent.njk"
category: "agent"
maker: "HarnessLab"
license: null
url: "https://github.com/HarnessLab/claw-code-agent"
source_code_url: "https://github.com/HarnessLab/claw-code-agent"
source_available: True
platforms: []
first_released: "2026-04-01"
current_release: "2026-06-22"
stars: "543"
language: "Python"
homepage: null
mcp_support: True
plugin_support: True
claude_code_plugin: null
subagents: True
hooks: True
plan_mode: True
model_providers: "vLLM, Ollama, LiteLLM Proxy, OpenRouter"
pricing: null
install_method: "git clone; pip install -e .; set OPENAI_BASE_URL/OPENAI_API_KEY/OPENAI_MODEL env vars; run python3 -m src.main"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Full Python reimplementation of Claude Code's npm agent architecture with zero external dependencies (pure stdlib), designed for local open-source models (especially Qwen3-Coder via vLLM). Includes local web GUI and comprehensive runtime subsystems (tasks, plans, MCP, plugins, hooks, LSP, worktrees, workflows, teams, background sessions)."
---

Full Python reimplementation of Claude Code's npm agent architecture with zero external dependencies (pure stdlib), designed for local open-source models (especially Qwen3-Coder via vLLM). Includes local web GUI and comprehensive runtime subsystems (tasks, plans, MCP, plugins, hooks, LSP, worktrees, workflows, teams, background sessions).
