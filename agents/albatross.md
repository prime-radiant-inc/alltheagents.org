---
name: "Albatross"
slug: "albatross"
layout: "agent.njk"
category: "agent"
maker: "morganlinton"
license: "MIT"
url: "https://github.com/morganlinton/Albatross"
source_code_url: "https://github.com/morganlinton/Albatross"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-04-25"
current_release: "2026-08-03"
stars: "222"
language: "Rust"
homepage: "https://albatross.sh"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Ollama,LM Studio,MLX,llama.cpp,OpenRouter,OpenAI,Anthropic,OpenAI Codex,Grok"
pricing: "Free"
install_method: "brew install morganlinton/tap/albatross"
docs_url: "https://albatross.sh"
plugin_docs_url: null
config_docs_url: null
download_url: "https://crates.io/crates/albatross-cli"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Terminal-first AI coding agent/harness with multi-model routing; supports local (Ollama, LM Studio, MLX, llama.cpp) or cloud providers with one TUI. MCP-native; hooks via agent.config.json; /plan commands for plan mode."
---

Albatross is a Rust TUI whose pitch is 'no black box': every routing decision, token spend, and provider switch is itemized. Work is planned through /plan, which expands an intent into a spec file (.albatross/spec.md) and can build routed task graphs across configured model tiers; /iterate adds a critic-scored generate-evaluate loop and /auto runs batches overnight. MCP servers plug in through mcpServers in agent.config.json with trust gating, and lifecycle hooks can allow, deny, or block tool calls. It is MIT-licensed, installed via Homebrew or cargo, embeds an SDK for building other tools, and stays on a fast release cadence (v2.4.x, 224 stars) as a solo project.
