---
name: "GitHub Copilot CLI"
slug: "github-copilot-cli"
layout: "agent.njk"
category: "agent"
maker: "github"
license: "Source Available"
url: "https://github.com/github/copilot-cli"
source_code_url: "https://github.com/github/copilot-cli"
source_available: "True"
platforms:
  - "CLI"
first_released: "2023-01-06"
current_release: "2026-08-19"
stars: null
language: "Shell"
homepage: "https://github.com/features/copilot/cli"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Sonnet 4.5, Claude Sonnet 4, GPT-5"
pricing: "Requires active Copilot subscription; each prompt consumes one premium request from monthly quota"
install_method: "curl -fsSL https://gh.io/copilot-install | bash"
docs_url: "https://docs.github.com/copilot/concepts/agents/about-copilot-cli"
plugin_docs_url: null
config_docs_url: null
download_url: "https://gh.io/copilot-install"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "tiennm"
what_makes_it_special: "Terminal-native synchronous AI agent powered by the same agentic harness as GitHub's Copilot coding agent; deep GitHub workflow integration (repos, issues, PRs via natural language); MCP extensibility; LSP support for code intelligence; full user control with action preview before execution; cross-platform."
---

Copilot CLI moves GitHub's coding agent from github.com and IDEs into the terminal, where developers already work. It plans and executes tasks locally with explicit approval before each action, talks to repositories, issues, and pull requests in natural language, and ships the GitHub MCP server by default with custom MCP servers supported for extension. Language Server Protocol integration supplies go-to-definition, hover, and diagnostics beyond plain text, and model selection covers Claude Sonnet 4.5 (default), Sonnet 4, and GPT-5, with an experimental Autopilot mode that keeps working until a task completes. It requires an active Copilot subscription, with each prompt consuming a premium request from the monthly quota.
