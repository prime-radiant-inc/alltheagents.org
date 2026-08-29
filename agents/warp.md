---
name: "Warp"
slug: "warp"
layout: "agent.njk"
category: "agent"
maker: "warpdotdev"
license: "MIT (UI framework), AGPL-3.0 (rest)"
url: "https://github.com/warpdotdev/warp"
source_code_url: "https://github.com/warpdotdev/warp"
source_available: "True"
platforms:
  - "CLI"
  - "Desktop"
first_released: "2021-07-08"
current_release: "2026-08-20"
stars: null
language: "Rust"
homepage: "https://warp.dev"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "yes"
plan_mode: "no"
model_providers: "OpenAI, supports external agents (Claude Code, Codex, Gemini CLI)"
pricing: "freemium"
install_method: "Download from https://www.warp.dev/download, or build from source (./script/bootstrap && ./script/run)"
docs_url: "https://docs.warp.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.warp.dev/download"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
  - "tiennm"
what_makes_it_special: "Agentic development environment born from the terminal. Combines a modern terminal with AI-powered coding agent capabilities and support for external CLI agents (Claude Code, Codex, Gemini CLI). Client codebase is open source."
---

Warp began as a modern terminal and grew into an agentic development environment for running fleets of coding agents across the software lifecycle. Work is defined as factories-as-code — factory.yaml plus agent files specifying triggers, agent types, models, permissions, and approval gates — and work flows in from Slack, Teams, Linear, Jira, and GitHub, with runs steerable from web, mobile, terminal, or IDE. A quality loop runs evals on a team's own work, cross-model benchmarks, and self-improvement in which observer agents open PRs against the factory config itself. Warp supports MCP servers in both local and cloud agents, exposes its own MCP server, and works with any MCP-capable harness including Claude Code and Codex. Pricing is credit-based per agent run across Free, Build ($20), Max, Business, and Enterprise tiers, with self-hosted-VPC options.
