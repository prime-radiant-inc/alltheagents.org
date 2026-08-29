---
name: "Neovate Code"
slug: "neovate-code"
layout: "agent.njk"
category: "agent"
maker: "neovateai"
license: "MIT"
url: "https://github.com/neovateai/neovate-code"
source_code_url: "https://github.com/neovateai/neovate-code"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-03-11"
current_release: "2026-03-24"
stars: null
language: "TypeScript"
homepage: "https://neovateai.dev/"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "False"
subagents: "yes"
hooks: "yes"
plan_mode: "yes"
model_providers: null
pricing: "BYOK"
install_method: "npm install -g @neovate/code"
docs_url: "https://neovateai.dev"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
what_makes_it_special: "Coding agent for generating code, fixing bugs, reviewing code, and adding tests, with both interactive and headless modes and a VSCode extension."
---

Neovate Code is a terminal coding agent that proposes edits and tool calls for approval before applying them. Developers pick a provider and model through slash commands, and API keys are read from standard environment variables for every supported provider, avoiding lock-in to one vendor. Work spans code generation, bug fixing, code review, test writing, refactoring, and query optimization. The same npm package covers macOS, Linux, and Windows, and the pnpm monorepo includes an e-commerce-grade test suite with end-to-end tests and a bundled ripgrep. A VS Code extension in the repository brings the agent into the editor alongside the CLI.
