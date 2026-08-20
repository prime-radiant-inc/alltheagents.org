---
name: "cersei"
slug: "cersei"
layout: "agent.njk"
category: "agent"
maker: "pacifio"
license: "MIT"
url: "https://github.com/pacifio/cersei"
source_code_url: "https://github.com/pacifio/cersei"
source_available: True
platforms: []
first_released: "2026-04-02"
current_release: "2026-08-06"
stars: "443"
language: "Rust"
homepage: "https://cersei.tryatlas.cc/docs/"
mcp_support: True
plugin_support: True
claude_code_plugin: null
subagents: True
hooks: True
plan_mode: True
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
what_makes_it_special: "Reverse-engineered Rust port of Claude Code architecture as an embeddable SDK; graph memory (Grafeo) with 98us recall vs Claude Code's 7.5s LM call; 6MB binary, 4.9MB RSS; 30+ built-in tools; #[derive(Tool)] macro; three-tier memory system (flat files + CLAUDE.md + graph)"
---

Reverse-engineered Rust port of Claude Code architecture as an embeddable SDK; graph memory (Grafeo) with 98us recall vs Claude Code's 7.5s LM call; 6MB binary, 4.9MB RSS; 30+ built-in tools; #[derive(Tool)] macro; three-tier memory system (flat files + CLAUDE.md + graph)
