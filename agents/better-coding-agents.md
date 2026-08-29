---
name: ".better-coding-agents"
slug: "better-coding-agents"
layout: "agent.njk"
category: "other"
maker: "bmdavis419"
license: null
url: "https://github.com/bmdavis419/.better-coding-agents"
source_code_url: "https://github.com/bmdavis419/.better-coding-agents"
source_available: "True"
platforms: []
first_released: "2025-11-13"
current_release: "2025-11-13"
stars: "168"
language: "TypeScript"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: "Clone into ~/.better-coding-agents and run the init command (copies slash commands for OpenCode & Cursor, plus an OpenCode theme)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/bmdavis419/.better-coding-agents"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Utility that clones full source repos of libraries (Svelte/SvelteKit, Effect.ts, neverthrow, opencode) as git subtrees so coding agents can search the actual library codebase rather than relying on training data."
---

Coding agents answer library questions from training data, which goes stale and produces hallucinated APIs. This project's remedy is deliberately simple: clone the full source repositories of Svelte/SvelteKit, Effect, neverthrow, and opencode as git subtrees into a home-directory repo, then provide OpenCode and Cursor slash commands plus a dedicated OpenCode agent that instructs the coding agent to search those real codebases before answering. A single init command upserts agent definitions, commands, and themes into the OpenCode and Cursor config directories, so setup takes seconds and works alongside existing tooling. A custom OpenCode theme rounds out the package. It is a small community utility (168 stars) for developers who want grounded, current library answers from their existing agents.
