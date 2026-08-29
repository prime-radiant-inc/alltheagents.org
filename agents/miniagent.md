---
name: "MiniAgent"
slug: "miniagent"
layout: "agent.njk"
category: "agent"
maker: "ZhuLinsen"
license: "Apache-2.0"
url: "https://github.com/ZhuLinsen/MiniAgent"
source_code_url: "https://github.com/ZhuLinsen/MiniAgent"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-04-27"
current_release: "2026-07-12"
stars: "194"
language: "Python"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
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

MiniAgent is built as an agent textbook: the entire engine — LLM interaction, tool dispatch, context compression — sits in one readable agent.py of about a thousand lines, positioned as an alternative to opaque frameworks like LangChain or pydantic-ai. Its design argument is that a small tool surface composes further than a large one: six code tools plus bash cover coding, while OS tools (browser, apps, clipboard, document creation) extend it toward Manus-style desktop control, and new tools register with a three-line decorator. Tool calling runs in two modes — transparent text parsing for learners and native function calling for reliability — with dangerous commands intercepted for confirmation. Skill objects bundle a prompt with a tool whitelist into reusable roles (coder, researcher, reviewer, tester), and an optional MCP client loads external servers' tools into the same namespace. Learners and tinkerers use it to read and modify a complete agent in one sitting rather than navigate a framework.
