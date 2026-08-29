---
name: "Droid"
slug: "droid"
layout: "agent.njk"
category: "agent"
maker: "Factory-AI"
license: null
url: "https://github.com/Factory-AI/factory"
source_code_url: "https://github.com/Factory-AI/factory"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Autonomous"
first_released: "2026-07-29"
current_release: "2026-08-17"
stars: "5"
language: "TypeScript"
homepage: "https://factory.ai"
mcp_support: "yes"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "yes"
hooks: "yes"
plan_mode: "yes"
model_providers: null
pricing: "subscription"
install_method: "macOS/Linux: curl -fsSL https://app.factory.ai/cli | sh; Windows: irm https://app.factory.ai/cli/windows | iex; npm: npm -g install droid"
docs_url: "https://docs.factory.ai"
plugin_docs_url: "https://github.com/Factory-AI/factory-plugins"
config_docs_url: null
download_url: "https://app.factory.ai/cli"
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Agent-native development platform spanning CLI, Web, Slack/Teams, Linear/Jira, and Mobile. Top-performing 'Droid' agent in terminal benchmarks. IDE integrations (VS Code, JetBrains, Zed) and GitHub Actions for automated code reviews/PR descriptions. Plugins marketplace available. Proprietary (not open source)."
---

Droid is Factory's bet that development work should be distributed across surfaces: the same agent runs in a terminal CLI, in Slack or Teams, against Linear/Jira tickets, in GitHub Actions for automated PR review and security scans, and from mobile. Inside the CLI, MCP servers extend tools, custom Droids act as specialized subagents, Missions orchestrate multi-agent runs, and hooks automate tool lifecycle; Specification Mode writes a plan before implementation. Model selection is per-session (/model), and TypeScript/Python SDKs expose the same agent to application code. Factory's repo is a thin front door — the product is closed-source with commercial subscription pricing.
