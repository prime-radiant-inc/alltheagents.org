---
name: "DeepCode"
slug: "deepcode"
layout: "agent.njk"
category: "agent"
maker: "HKUDS"
license: "MIT"
url: "https://github.com/HKUDS/DeepCode"
source_code_url: "https://github.com/HKUDS/DeepCode"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
  - "Autonomous"
first_released: "2025-05-14"
current_release: "2026-08-19"
stars: null
language: "Python"
homepage: "http://arxiv.org/abs/2512.07921"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "False"
plan_mode: "True"
model_providers: "OpenRouter, OpenAI, Anthropic, DeepSeek, Gemini, Ollama, vLLM, OpenAI-compatible, Requesty, Forge, MiniMax"
pricing: "Free / open-source"
install_method: "uv tool install --python 3.12 deepcode-hku"
docs_url: "https://hkuds.github.io/DeepCode/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/HKUDS/DeepCode/releases"
maintained: "active"
sources:
  - "jqueryscript"
what_makes_it_special: "Paper2Code workflow reproduces research papers into runnable code (75.9% on PaperBench, beating commercial agents by 26 points); Loop Engineering with durable steerable Goals; parallel agents in isolated Git worktrees; same agent runtime across CLI and Desktop."
---

DeepCode came out of HKU's Data Intelligence Lab as a multi-agent system whose orchestrator coordinates specialist agents for intent understanding, document parsing, code planning, reference mining, indexing, and generation, backed by CodeRAG and iterative verification. That pipeline reproduces machine-learning research papers as executable code, and the lab reports PaperBench results ahead of commercial agents on the commercial-agent subset. The project has since broadened into a general coding agent (v2.0) with a CLI/TUI and a Tauri-based desktop app sharing one runtime, full MCP client support with lazy loading and per-tool approvals, skills, plugins, subagents, and sandboxed sessions. Researchers use it for paper reproduction while developers adopt it as a general open-source harness; it is MIT-licensed, Python-based, and actively released.
