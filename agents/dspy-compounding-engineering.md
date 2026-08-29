---
name: "dspy-compounding-engineering"
slug: "dspy-compounding-engineering"
layout: "agent.njk"
category: "agent"
maker: "Strategic-Automation"
license: "MIT"
url: "https://github.com/Strategic-Automation/dspy-compounding-engineering"
source_code_url: "https://github.com/Strategic-Automation/dspy-compounding-engineering"
source_available: "True"
platforms: []
first_released: "2025-11-29"
current_release: "2026-06-13"
stars: "70"
language: "Python"
homepage: "https://strategic-automation.github.io/dspy-compounding-engineering/"
mcp_support: "True"
plugin_support: null
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "True"
model_providers: "OpenAI, Anthropic, Ollama, OpenRouter"
pricing: "Free/open-source (BYO API keys)"
install_method: "curl -LsSf https://raw.githubusercontent.com/Strategic-Automation/dspy-compounding-engineering/main/scripts/install.sh | sh; or pip install dspyce-install + dspyce-install; or uv sync from source"
docs_url: "https://strategic-automation.github.io/dspy-compounding-engineering/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Local-first AI engineering CLI implementing a 'compounding engineering' philosophy: every todo resolution automatically codifies learnings into a knowledge base that informs all future AI operations. Features 10+ parallel specialized review agents (security, performance, architecture), ReAct-based file editing with zero hallucination, isolated git worktrees, built on the DSPy framework."
---

Most agent tools forget everything between tasks; this CLI's premise is that each unit of engineering work should make the next one easier. Every todo resolution codifies what was learned into a local knowledge base, and that knowledge base is injected into subsequent planning, review, and editing operations, so recurring issues stop recurring. Under that loop, DSPy programs run ten-plus specialized reviewers in parallel (security, performance, architecture, data integrity), a ReAct file editor gathers context before touching files, and plans can pull live documentation from the web. Work executes in isolated git worktrees with parallel workers, and a local knowledge base keeps code on the machine. It fits solo engineers or small teams who want review-and-implementation automation that accumulates institutional memory.
