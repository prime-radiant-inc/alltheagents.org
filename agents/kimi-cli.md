---
name: "Kimi CLI"
slug: "kimi-cli"
layout: "agent.njk"
category: "agent"
maker: null
license: "Apache-2.0"
url: "https://kimi.ai"
source_code_url: null
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: null
current_release: null
stars: null
language: "Python"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "pip install kimi-cli (PyPI package)"
docs_url: "https://moonshotai.github.io/kimi-cli/en/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "ishandutta"
what_makes_it_special: "Terminal-based AI coding agent and shell by Moonshot AI that can read/edit code, execute shell commands, search/fetch web pages, and autonomously plan actions. Supports MCP (stdio + HTTP with OAuth), zsh and VS Code integrations. Note: evolving into Kimi Code CLI; this project will be gradually wound down."
---

Moonshot AI built Kimi CLI as a terminal agent that reads and edits code, runs commands, and fetches web pages while planning and adjusting its actions mid-task. It integrates with editors through the Agent Client Protocol (kimi acp for Zed and JetBrains IDEs), a VS Code extension, and a zsh plugin, and its kimi mcp subcommands add stdio or HTTP MCP servers with header or OAuth authentication. The project is Apache-2.0 and installable via pip or uv, but the README states it is being wound down in favor of Kimi Code CLI, the team's next-generation agent; existing configurations and sessions migrate automatically. Developers already using it can continue, while new users are pointed at the successor.
