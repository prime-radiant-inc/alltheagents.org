---
name: "cursor-agent"
slug: "cursor-agent"
layout: "agent.njk"
category: "agent"
maker: "civai-technologies"
license: "MIT"
url: "https://github.com/civai-technologies/cursor-agent"
source_code_url: "https://github.com/civai-technologies/cursor-agent"
source_available: "True"
platforms: []
first_released: "2025-03-22"
current_release: "2025-07-13"
stars: "133"
language: "Python"
homepage: "https://civai.co"
mcp_support: "no"
plugin_support: null
claude_code_plugin: "False"
subagents: "no"
hooks: null
plan_mode: "no"
model_providers: "Anthropic, OpenAI, Ollama"
pricing: "Free (MIT); API costs apply based on token usage"
install_method: "pip install cursor-agent-tools; or git clone + pip install -e ."
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/cursor-agent-tools/"
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Python-based AI agent replicating Cursor's coding assistant capabilities; function calling with registered tools; codebase semantic search, grep, fuzzy file search, web search; image analysis via LLM vision; terminal command execution with permission system (YOLO mode, allowlists/denylists)"
---

cursor-agent packages the mechanics of Cursor's coding assistant into a pip-installable Python library: a function-calling loop with registered tools for reading and editing files, semantic and regex codebase search, web search, image analysis, and terminal commands gated by a permission system. It supports Anthropic, OpenAI, and locally hosted Ollama models, and developers can extend it by registering custom tools in code. The project, authored by the founder of CIVAI Technologies, reached about 130 stars but shows no recent commits or releases and one stale pull request, so it now serves mainly as a reference implementation of an agentic coding loop in Python.
