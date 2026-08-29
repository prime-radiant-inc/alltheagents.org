---
name: "opendev"
slug: "opendev"
layout: "agent.njk"
category: "agent"
maker: "opendev-to"
license: "MIT"
url: "https://github.com/opendev-to/opendev"
source_code_url: "https://github.com/opendev-to/opendev"
source_available: "True"
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
docs_url: "https://github.com/opendev-to/opendev/blob/main/docs/providers.md"
plugin_docs_url: null
config_docs_url: "https://github.com/opendev-to/opendev/blob/main/docs/providers.md"
download_url: "https://github.com/opendev-to/opendev/releases"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Compound AI system: multiple models collaborate, each optimized for its role across 5 workflow slots (Normal, Thinking, Compact, Critique, VLM), each independently bindable to any model/provider. Parallel agent fleet via async Tokio tasks. Blazing fast (4.3 ms startup, 9.4 MB RAM, 18 MB single binary). Both TUI and Web UI with remote session support."
---

Most coding agents lock a session to one model, which wastes frontier tokens on summarization and under-provisions hard reasoning. OpenDev, a Rust CLI, treats the agent as a compound AI system: five workflow slots — Normal for execution, Thinking for planning, Compact for context summarization, Critique for self-review, VLM for vision — each bind independently to any of nine providers (OpenAI, Anthropic, Fireworks, Google, Groq, Mistral, DeepInfra, OpenRouter, Azure) or to Ollama/LM Studio locally, with defined fallback chains when a slot's model is absent. An Agent Fleet runs parallel sub-agents, each with its own binding, and MCP integration connects external tools; a TUI and remote-accessible Web UI cover interaction. Distribution spans cargo, Homebrew, shell installers, and GitHub Release binaries for all three OSes. Its maintainers publish an arXiv technical report on the compound-AI design, and the performance pitch — 4.3 ms startup, 9.4 MB RAM — targets developers who find Node-based agents heavy.
