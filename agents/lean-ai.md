---
name: "Lean AI"
slug: "lean-ai"
layout: "agent.njk"
category: "agent"
maker: "lean-ai"
license: null
url: "https://plugins.jetbrains.com/plugin/31110-lean-ai"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-06-06"
current_release: null
stars: null
language: null
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic, Google Gemini, Ollama"
pricing: "free"
install_method: "Install from the JetBrains Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/31110-lean-ai"
maintained: null
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Agentic coding assistant with local LLM via Ollama"
---

Lean AI's stated philosophy is to plan well, give the LLM tools, and let it work, deliberately avoiding multi-agent orchestration in favor of one model following a deterministic workflow. Inside JetBrains IDEs it runs a plan-approve-execute cycle, a bug-fix mode with a separate investigation phase, open-ended request mode, FIM-based inline completions, and internet search tools for documentation lookups, with post-execution review steps. Models come from Ollama locally or from OpenAI, Anthropic, and Google in the cloud, which keeps costs at zero for local setups. The plugin is free on the JetBrains Marketplace and published by a small independent vendor.
