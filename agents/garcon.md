---
name: "Garcon"
slug: "garcon"
layout: "agent.njk"
category: "multiplexer"
maker: "cfal"
license: "GPL-3.0"
url: "https://github.com/cfal/garcon"
source_code_url: "https://github.com/cfal/garcon"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-02-23"
current_release: "2026-08-19"
stars: "58"
language: "TypeScript"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "True"
model_providers: "Anthropic, OpenAI; presets: Ollama, OpenRouter, Gemini, Fireworks, Together, Alibaba Cloud, Z.AI, + custom OpenAI/Anthropic-compatible endpoints"
pricing: "Free/self-hosted/open source"
install_method: "git clone https://github.com/cfal/garcon.git && cd garcon && bun run setup && bun run start (requires Bun + git)"
docs_url: "https://github.com/cfal/garcon/blob/main/docs/cli.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/cfal/garcon"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Self-hosted browser workspace for running multiple coding agents in parallel (up to 4 split panes), steering work mid-turn, reviewing real diffs with line-level staging, managing Git/PRs, forking sessions across agents/models, mobile access, Telegram alerts, CLI delegation, and scheduled prompts."
---

Garcon gives a developer running several CLI coding agents a single self-hosted web UI instead of a pile of terminal windows. It runs Claude Code, Codex, Cursor Agent, OpenCode, Amp, Factory Droid, and Pi side by side in up to four resizable panes, lets the operator queue prompts, redirect active turns, and answer agent questions, and records transcripts that can be exported or handed to another agent as a token-budgeted artifact. A Git workbench shows real diffs with line-, hunk-, and file-level staging, and companion tooling covers session forking across agents or models, mobile access, Telegram alerts, and scheduled prompts. It is GPL-3.0 and installed from source with Bun, targeting solo developers who keep their code and their agents on one machine.
