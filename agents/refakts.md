---
name: "refakts"
slug: "refakts"
layout: "agent.njk"
category: "other"
maker: "devill"
license: "PolyForm Noncommercial License 1.0.0"
url: "https://github.com/devill/refakts"
source_code_url: "https://github.com/devill/refakts"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-06-30"
current_release: "2026-07-17"
stars: "72"
language: "TypeScript"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "True"
plan_mode: "False"
model_providers: null
pricing: "Free for non-commercial use; commercial license required for businesses"
install_method: "npm install -g refakts"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/refakts"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "CLI refactoring tool built 'by AI agents, for AI agents' that enables surgical refactoring operations (rename, extract variable, inline variable, find usages, move file) via AST manipulation instead of regenerating whole files; features automated quality habits via post-commit hooks that detect code smells and prompt agents to refactor."
---

RefakTS exists because AI coding agents are bad at refactoring: regenerating whole files wastes tokens and risks breaking untouched code, while string replacement misses multi-location changes. Built on ts-morph and tsquery, it exposes location-based operations — select, rename, extract-variable, inline-variable, find-usages, move-file, sort-methods — that an agent invokes through the shell to make precise, syntax-aware edits without touching surrounding code. The project doubles as an experiment in agent-driven development: its roadmap is managed by Claude instances that vote on features, humans contribute by pointing Claude Code at the issue tracker, and automated post-commit hooks detect code smells like duplication and dead code, prompting the agent to fix them in line with XP habits. It is labeled a proof of concept, with core operations working and more commands in development. Developers use it as a tool their coding agent calls for safe, token-efficient refactors under a PolyForm Noncommercial license.
