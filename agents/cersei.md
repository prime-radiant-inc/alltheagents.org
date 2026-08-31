---
name: "cersei"
slug: "cersei"
layout: "agent.njk"
category: "agent-sdk"
maker: "pacifio"
license: "MIT"
url: "https://github.com/pacifio/cersei"
source_code_url: "https://github.com/pacifio/cersei"
source_available: "True"
platforms: []
first_released: "2026-04-02"
current_release: "2026-08-06"
stars: "443"
language: "Rust"
homepage: "https://cersei.tryatlas.cc/docs/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Anthropic, OpenAI, Ollama, Azure, vLLM"
pricing: "Free / open-source (MIT)"
install_method: "cargo install --path crates/abstract-cli, or add as Cargo dependency"
docs_url: "https://cersei.pacifio.dev/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/pacifio/cersei"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "\"Reverse-engineered Rust port of Claude Code architecture as an embeddable SDK; graph memory (Grafeo) with 98us recall vs Claude Code's 7.5s LM call; 6MB binary, 4.9MB RSS; 30+ built-in tools;"
---

cersei came from reverse-engineering Claude Code's architecture and rebuilding it in Rust as a library: tool execution, LLM streaming, subagent orchestration, persistent memory, skills, and MCP integration all exposed as composable crates for embedding agents in applications. Its pitch is efficiency at the systems level — the companion Abstract CLI binary measures roughly 6MB with 4.9MB RSS and 32ms startup — alongside a three-tier memory design that combines flat files, CLAUDE.md-style context, and an optional graph memory backed by Grafeo, which answers recall queries in microseconds without an LLM call. Developers use it to build custom agents with Claude Code-like capability without Node.js, or to embed agent behavior in products where binary size and memory matter. It is MIT-licensed, Rust-based, installable via Cargo, and actively maintained with published docs and benchmark suites against Claude Code and competing agent frameworks.
