---
name: "maestro"
slug: "maestro"
layout: "agent.njk"
category: "multiplexer"
maker: "its-maestro-baby"
license: "MIT"
url: "https://github.com/its-maestro-baby/maestro"
source_code_url: "https://github.com/its-maestro-baby/maestro"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-01-07"
current_release: "2026-04-19"
stars: "1167"
language: "Rust, TypeScript"
homepage: null
mcp_support: "yes (stdio)"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (Claude Code), Google (Gemini CLI), OpenAI (Codex)"
pricing: "open-source"
install_method: "binary"
docs_url: "https://its-maestro-baby.github.io/maestro/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Cross-platform desktop application that orchestrates 1-6 AI coding assistants (Claude Code, Gemini CLI, OpenAI Codex) in parallel, running each session simultaneously in its own isolated git worktree to enable true parallel development without merge conflicts. Plugin Marketplace supports Skills, Commands, and MCP servers."
---

Parallel agent work usually means juggling terminal tabs and manual branch hygiene, so Maestro provides a Tauri-based desktop grid where each cell is a CLI session bound to its own git worktree, eliminating merge conflicts between concurrent agents on one repository. A visual git graph with diffs shows what each agent changed, quick actions cover running the app, committing, or firing custom prompts at a session, and a plugin marketplace adds skills, commands, and MCP servers. Developers running multiple Claude Code, Gemini CLI, or Codex sessions against the same repository - the 'Bloomberg terminal for CLI agents' workflow - are the target user.
