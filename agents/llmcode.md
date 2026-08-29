---
name: "LLMCode"
slug: "llmcode"
layout: "agent.njk"
category: "agent"
maker: "syscalldev"
license: "Apache-2.0"
url: "https://github.com/syscalldev/LLMCode"
source_code_url: "https://github.com/syscalldev/LLMCode"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-02-25"
current_release: "2025-02-25"
stars: "64"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI-compatible API (configurable baseUrl and model)"
pricing: "Free / open source (Apache-2.0)"
install_method: "git clone + pip install -r requirements.txt"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/syscalldev/LLMCode"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Agentic terminal-based coding assistant that understands your codebase and helps you code faster via natural language commands (file ops, context gathering, AI assistance)"
---

LLMCode demonstrates how much of the Claude Code workflow a compact terminal REPL can reproduce: gather context with /context or /#, request changes in natural language, and write the result with /write or /append, with workspace navigation and configuration handled by further commands. Because any OpenAI-compatible endpoint works, it ran against DeepSeek-R1 and local Llama 3 servers as readily as OpenAI itself, with settings stored in ~/.llm_code_config.json. The repository describes itself as under active development and partially built with its own assistance, but work stalled at 11 commits, leaving a prototype rather than a maintained tool.
