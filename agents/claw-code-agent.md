---
name: "claw-code-agent"
slug: "claw-code-agent"
layout: "agent.njk"
category: "agent"
maker: "HarnessLab"
license: null
url: "https://github.com/HarnessLab/claw-code-agent"
source_code_url: "https://github.com/HarnessLab/claw-code-agent"
source_available: "True"
platforms: []
first_released: "2026-04-01"
current_release: "2026-06-22"
stars: "543"
language: "Python"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "vLLM, Ollama, LiteLLM Proxy, OpenRouter"
pricing: "free"
install_method: "git clone; pip install -e .; set OPENAI_BASE_URL/OPENAI_API_KEY/OPENAI_MODEL env vars; run python3 -m src.main"
docs_url: "https://github.com/HarnessLab/claw-code-agent#readme"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Full Python reimplementation of Claude Code's npm agent architecture with zero external dependencies (pure stdlib), designed for local open-source models (especially Qwen3-Coder via vLLM). Includes local web GUI and comprehensive runtime subsystems (tasks, plans, MCP, plugins, hooks, LSP, worktrees, workflows, teams, background sessions)."
---

The project exists for developers who want Claude Code's workflow on local models and under their own control: the entire agent runtime is standard-library Python, so the loop is auditable without node_modules, and the documented deployment is vLLM serving Qwen3-Coder with tool-call parsing configured server-side. It reimplements CLAUDE.md discovery, slash commands, session persistence, and context compaction, then extends them with MCP support, agent delegation, and cost budgets. Permission tiers default to read-only and escalate explicitly, which suits shared machines and enterprise settings. Researchers studying agent architecture and teams with data-sovereignty constraints are the primary users; the project is in alpha with active monthly feature work.
