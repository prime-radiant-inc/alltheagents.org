---
name: "aft"
slug: "aft"
layout: "agent.njk"
category: "other"
maker: "cortexkit"
license: "MIT"
url: "https://github.com/cortexkit/aft"
source_code_url: "https://github.com/cortexkit/aft"
source_available: "True"
platforms:
  - "IDE"
  - "Autonomous"
first_released: "2026-03-15"
current_release: "2026-08-19"
stars: "254"
language: "Rust"
homepage: "https://discord.gg/DSa65w8wuf"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI-compatible, Ollama (for semantic search embeddings)"
pricing: "Free / open-source"
install_method: "npx @cortexkit/aft@latest setup"
docs_url: "https://github.com/cortexkit/aft/blob/main/docs/tools.md"
plugin_docs_url: null
config_docs_url: "https://github.com/cortexkit/aft/blob/main/docs/config.md"
download_url: "https://www.npmjs.com/package/@cortexkit/aft"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Gives coding agents a sensorimotor cortex — IDE-like code perception (tree-sitter parsing, symbol-aware edits, semantic search, call graphs) and OS-like environment management (background bash, output compression, PTY sessions, undo stack). Hoists host tools so agents keep calling familiar read/edit/bash but get structured, token-efficient operations. Ships as plugins for OpenCode and Pi harnesses."
---

Coding agents treat code as raw text, so they re-read whole files, miss symbol boundaries, and burn context on noise — aft exists to fix that perception layer. Installed via npx @cortexkit/aft@latest setup as a plugin for OpenCode and Pi, it hoists the host's familiar read, edit, bash, and grep tools into tree-sitter-backed, symbol-aware versions and adds aft_ tools for outlines, semantic search, call graphs, and refactors, plus OS-level capabilities like background bash, output compression, PTY sessions, and an undo stack. Agents keep calling the same tool names, so no prompt or workflow changes are needed. It is MIT-licensed Rust, and its users are OpenCode and Pi harness owners optimizing for token efficiency.
