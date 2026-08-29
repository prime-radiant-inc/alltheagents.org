---
name: "Dexto"
slug: "dexto"
layout: "agent.njk"
category: "agent"
maker: "truffle-ai"
license: "Elastic License 2.0"
url: "https://github.com/truffle-ai/dexto"
source_code_url: "https://github.com/truffle-ai/dexto"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2025-03-24"
current_release: "2026-08-18"
stars: "645"
language: "TypeScript"
homepage: "https://dexto.ai"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: null
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Google, Groq, xAI, Cohere, Ollama, AWS Bedrock, Vertex AI, OpenRouter, LiteLLM, Glama, node-llama-cpp"
pricing: "open-source"
install_method: "binary"
docs_url: "https://cli.dexto.ai/docs/getting-started/intro/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://dexto.ai/install"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
what_makes_it_special: "Configuration-driven (YAML) agent harness ('OS for AI agents'); batteries-included (sessions, memory, tools, observability); instant mid-conversation model switching; multi-agent sub-agent spawning; runs as CLI, Web UI, REST API, Discord/Telegram, or MCP server; ships with production-ready coding agent"
---

Dexto treats the agent runtime as infrastructure: a YAML file defines the model, tools, and MCP servers, and the same harness exposes the agent through CLI, Web UI, REST API, or chat platforms. The bundled coding agent edits code, runs tests, spawns ephemeral explore subagents with unified approval forwarding, and swaps models mid-conversation — but the same YAML pattern builds non-coding agents, which is the point. An SDK embeds the runtime in Node applications with session management and observability included. It targets developers building their own agents who want the orchestration layer handled: state, tool orchestration, memory, and recovery instead of raw model calls.
