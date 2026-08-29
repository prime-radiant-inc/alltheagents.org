---
name: "Kimi Code CLI"
slug: "kimi-code-cli"
layout: "agent.njk"
category: "agent"
maker: "MoonshotAI"
license: "Apache-2.0"
url: "https://github.com/MoonshotAI/kimi-cli"
source_code_url: "https://github.com/MoonshotAI/kimi-cli"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-10-15"
current_release: "2026-08-03"
stars: null
language: "Python"
homepage: "https://moonshotai.github.io/kimi-cli/"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "pip install kimi-cli (PyPI package kimi-cli)"
docs_url: "https://moonshotai.github.io/kimi-cli/en/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "jqueryscript"
  - "brad"
what_makes_it_special: "Dual-mode shell/agent (toggle with Ctrl-X without leaving CLI), ACP (Agent Client Protocol) support for IDE integration (Zed, JetBrains), VS Code extension, Zsh integration, comprehensive MCP support with OAuth, autonomous planning and adjustment during execution. Being wound down in favor of Kimi Code CLI."
---

Kimi Code CLI is the continuation of Moonshot AI's terminal agent line, replacing the original Kimi CLI whose README points users here. It reads and edits code, executes shell commands, and searches the web while planning and revising its actions during execution; a Ctrl-X toggle switches between raw shell use and agentic operation without leaving the process. ACP support connects it to Zed and JetBrains IDEs, a VS Code extension covers that editor, and MCP servers can be attached over stdio or HTTP with OAuth. Installation via pip handles the migration from the older kimi-cli package automatically.
