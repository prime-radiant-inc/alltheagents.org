---
name: "MiniAgent"
slug: "miniagent"
layout: "agent.njk"
category: "agent"
maker: "ZhuLinsen"
license: "Apache-2.0"
url: "https://github.com/ZhuLinsen/MiniAgent"
source_code_url: "https://github.com/ZhuLinsen/MiniAgent"
source_available: True
platforms:
  - "CLI"
first_released: "2025-04-27"
current_release: "2026-07-12"
stars: "194"
language: "Python"
homepage: null
mcp_support: True
plugin_support: True
claude_code_plugin: False
subagents: True
hooks: null
plan_mode: null
model_providers: "DeepSeek, OpenAI, Gemini, Claude, any OpenAI-compatible endpoint"
pricing: "Free / open-source"
install_method: "git clone; uv sync (or pip install -r requirements.txt; pip install -e .)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Minimal, transparent CLI agent framework combining Claude Code-style coding with Manus-style OS control; single-file core engine (agent.py, ~1,000 lines) with no hidden abstractions. Achieves extensibility using just 6 code tools + bash; Skill system with built-in roles (coder/researcher/reviewer/tester); MCP client built-in; dual tool-calling modes (text parsing + native Function Calling); minimal dependencies (only 7)."
---

Minimal, transparent CLI agent framework combining Claude Code-style coding with Manus-style OS control; single-file core engine (agent.py, ~1,000 lines) with no hidden abstractions. Achieves extensibility using just 6 code tools + bash; Skill system with built-in roles (coder/researcher/reviewer/tester); MCP client built-in; dual tool-calling modes (text parsing + native Function Calling); minimal dependencies (only 7).
