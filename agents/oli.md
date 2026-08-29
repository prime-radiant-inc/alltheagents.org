---
name: "oli"
slug: "oli"
layout: "agent.njk"
category: "agent"
maker: "amrit110"
license: "Apache-2.0"
url: "https://github.com/amrit110/oli"
source_code_url: "https://github.com/amrit110/oli"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-02-11"
current_release: "2026-06-29"
stars: "245"
language: "Rust"
homepage: "https://amrit110.github.io/oli/"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Anthropic, OpenAI, Google, Ollama"
pricing: "Free / open-source"
install_method: "git clone + ./build.sh (build from source)"
docs_url: "https://docs.rs/oli-server"
plugin_docs_url: null
config_docs_url: null
download_url: "https://crates.io/crates/oli-server"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Open-source Claude Code alternative with hybrid architecture (Rust backend + React/Ink terminal UI), supporting both cloud and local LLMs with agentic capabilities (file search, edit, command execution). Early stage."
---

oli is an open-source terminal coding assistant positioned as a Claude Code alternative, built around a Rust agent core and a React/Ink interface communicating over JSON RPC. The agentic loop covers file search, code editing, and shell execution, with function-calling support implemented across all four supported providers rather than only cloud APIs. Local operation through Ollama keeps the workflow private, matching the Open-Local-Intelligent name. The README is explicit that the project is early stage and bug-prone, and installation is from source rather than packaged binaries. A single maintainer drives development with a docs site and moderate community activity.
