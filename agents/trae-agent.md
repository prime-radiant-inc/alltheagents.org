---
name: "Trae Agent"
slug: "trae-agent"
layout: "agent.njk"
category: "agent"
maker: "bytedance"
license: "MIT"
url: "https://github.com/bytedance/trae-agent"
source_code_url: "https://github.com/bytedance/trae-agent"
source_available: "True"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2025-06-13"
current_release: "2026-02-05"
stars: null
language: "Python"
homepage: "https://www.trae.ai/"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Doubao, Azure, OpenRouter, Ollama, Google Gemini"
pricing: "Free / open-source (BYO API keys)"
install_method: "git clone, uv sync --all-extras, uv run trae-cli"
docs_url: "https://github.com/bytedance/trae-agent/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
  - "tiennm"
what_makes_it_special: "Transparent, modular, research-friendly architecture designed for studying AI agent architectures and ablation studies; includes trajectory recording, Lakeview summarization, and Docker sandbox execution mode."
---

Trae Agent exists to make agent research practical: production harnesses obscure their internals, which prevents controlled comparison of prompts, tools, and orchestration strategies. It provides a modular Python CLI in which a natural-language engineering task is executed through a small tool set — bash, str_replace-based file editing, sequential thinking — with interactive mode for iterative work and Docker mode for reproducible, isolated execution from an image, existing container, Dockerfile, or archive. Every run emits a trajectory log capturing LLM calls, tool usage, and step-by-step state, and Lakeview summarizes those steps for analysis; YAML configuration with environment-variable overrides keeps experiments scriptable. Agent researchers and engineers studying harness design are its primary users, and an accompanying arXiv technical report documents the architecture.
