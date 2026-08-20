---
name: "Amplifier"
slug: "amplifier-agent"
layout: "agent.njk"
category: "agent"
maker: "microsoft"
license: "MIT"
url: "https://github.com/microsoft/amplifier"
source_code_url: "https://github.com/microsoft/amplifier"
source_available: True
platforms:
  - "CLI"
first_released: "2025-09-09"
current_release: "2026-08-19"
stars: "3117"
language: "Shell"
homepage: null
mcp_support: True
plugin_support: True
claude_code_plugin: null
subagents: True
hooks: null
plan_mode: null
model_providers: "Anthropic, OpenAI, Azure OpenAI, Ollama, GitHub Copilot, ChatGPT (OAuth), Chat Completions (OpenAI-compatible), Gemini, vLLM"
pricing: null
install_method: "uv tool install git+https://github.com/microsoft/amplifier"
docs_url: "https://github.com/microsoft/amplifier#readme"
plugin_docs_url: null
config_docs_url: "https://github.com/microsoft/amplifier-bundle-recipes"
download_url: "https://github.com/microsoft/amplifier"
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Microsoft's modular AI development assistant. The CLI is one interface on top of a modular platform — bundles ship focused agents you invoke by name, and the amplifier-agent engine underneath provides the full agent loop with tools, sub-agents, skills, and MCP. Anything that can spawn a subprocess can use the engine. Nine model providers behind one interface with role-based routing for sub-agents."
---

Microsoft's modular AI development assistant. The CLI is one interface on top of a modular platform — bundles ship focused agents you invoke by name, and the [amplifier-agent](https://github.com/microsoft/amplifier-agent) engine underneath provides the full agent loop with tools, sub-agents, skills, and MCP. Anything that can spawn a subprocess can use the engine. Nine model providers behind one interface with role-based routing for sub-agents.
