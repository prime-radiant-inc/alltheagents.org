---
name: "opendev"
slug: "opendev"
layout: "agent.njk"
category: "agent"
maker: "opendev-to"
license: "MIT"
url: "https://github.com/opendev-to/opendev"
source_code_url: "https://github.com/opendev-to/opendev"
source_available: True
platforms:
  - "CLI"
first_released: "2026-03-04"
current_release: "2026-08-08"
stars: "820"
language: "Rust"
homepage: null
mcp_support: "yes (dynamic tool discovery; opendev mcp add/list/enable/disable)"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Fireworks, Google, Groq, Mistral, DeepInfra, OpenRouter, Azure OpenAI; local via Ollama, LM Studio, llama-server"
pricing: "open-source"
install_method: "cargo, brew, binary"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Compound AI system: multiple models collaborate, each optimized for its role across 5 workflow slots (Normal, Thinking, Compact, Critique, VLM), each independently bindable to any model/provider. Parallel agent fleet via async Tokio tasks. Blazing fast (4.3 ms startup, 9.4 MB RAM, 18 MB single binary). Both TUI and Web UI with remote session support."
---

Compound AI system: multiple models collaborate, each optimized for its role across 5 workflow slots (Normal, Thinking, Compact, Critique, VLM), each independently bindable to any model/provider. Parallel agent fleet via async Tokio tasks. Blazing fast (4.3 ms startup, 9.4 MB RAM, 18 MB single binary). Both TUI and Web UI with remote session support.
