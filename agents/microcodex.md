---
name: "MicroCodex"
slug: "microcodex"
layout: "agent.njk"
category: "agent"
maker: "paoloanzn"
license: "Apache-2.0"
url: "https://github.com/paoloanzn/microcodex"
source_code_url: "https://github.com/paoloanzn/microcodex"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-07-30"
current_release: "2026-08-06"
stars: 37
language: "C++"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "locked"
pricing: "free"
install_method: "curl -fsSL https://github.com/paoloanzn/microcodex/releases/latest/download/install.sh | sh"
docs_url: "https://github.com/paoloanzn/microcodex/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/paoloanzn/microcodex/releases/latest"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "An ultra-lightweight Codex-compatible terminal coding agent written in C++23 with no runtime dependencies beyond libcurl and OpenSSL on Linux — it authenticates with your ChatGPT plan via OAuth and reuses Codex skills from the filesystem, without being a Codex distribution."
---

MicroCodex is an independently written C++ client for the OpenAI Codex service: a terminal coding agent offering one-shot prompts and an interactive TUI, local coding tools for file read/write/edit, bash execution, and glob, durable conversations, and automatic context compaction. It logs in with your ChatGPT plan through OAuth (including device-auth for headless machines), stores credentials alongside Codex's own under ~/.codex, and discovers Codex skills installed under $CODEX_HOME/skills, so an existing Codex user's setup carries over. The bash tool runs behind a lexical safety gate that blocks destructive commands like rm -f and git reset --hard — explicitly not a sandbox — and MCP support is not yet implemented. It builds for macOS (Apple Silicon and Intel) and Linux, and targets developers who want a tiny, dependency-light alternative frontend to the Codex service.
