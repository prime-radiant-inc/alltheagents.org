---
name: "kota"
slug: "kota"
layout: "agent.njk"
category: "agent"
maker: "StepfenShawn"
license: "MIT"
url: "https://github.com/StepfenShawn/kota"
source_code_url: "https://github.com/StepfenShawn/kota"
source_available: "True"
platforms: []
first_released: "2026-01-11"
current_release: "2026-04-08"
stars: "100"
language: "Rust"
homepage: "https://crates.io/crates/kota"
mcp_support: "no"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: "True"
plan_mode: "True"
model_providers: "OpenAI-compatible (gpt-4o, gpt-4-turbo, gpt-3.5-turbo), DeepSeek, Anthropic Claude, Ollama"
pricing: "Free / open-source (BYO API key)"
install_method: "cargo install kota (CLI) or add as dependency in Cargo.toml (library)"
docs_url: "https://docs.rs/kota"
plugin_docs_url: null
config_docs_url: null
download_url: "https://crates.io/crates/kota"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Vim-inspired philosophy-lightweight Rust build, Lua-based configuration (Neovim-style), built-in Skills system, usable as both CLI and embeddable Rust library, plan mode similar to Claude Code, multi-model support"
---

kota applies the Neovim philosophy — small, fast, configured in Lua — to terminal coding agents. Users configure models and custom commands in .kota/config.lua, extend behavior with SKILL.md-defined skills, and drive execution through an update_plan tool that tracks task dependencies and status the way Claude Code does. Because it builds as both a CLI (cargo install kota) and a Rust crate with AgentBuilder and ContextManager APIs, the same agent core can be embedded into larger tools. Model access covers OpenAI-compatible endpoints, DeepSeek, Anthropic, and Ollama. It suits Rust users and embedding scenarios; MCP support remains on the roadmap rather than in the binary.
