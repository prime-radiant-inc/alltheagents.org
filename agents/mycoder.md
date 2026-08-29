---
name: "MyCoder"
slug: "mycoder"
layout: "agent.njk"
category: "agent"
maker: "bhouston"
license: "MIT"
url: "https://github.com/bhouston/mycoder"
source_code_url: "https://github.com/bhouston/mycoder"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2025-02-07"
current_release: "2026-01-07"
stars: "566"
language: "TypeScript"
homepage: "https://mycoder.ai"
mcp_support: "yes"
plugin_support: null
claude_code_plugin: null
subagents: "yes"
hooks: null
plan_mode: null
model_providers: "Anthropic Claude, OpenAI, Ollama (local)"
pricing: "open-source"
install_method: "npm install -g mycoder"
docs_url: "https://docs.mycoder.ai"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "An open-source Claude Code alternative with distinctive GitHub-native automation: agents trigger from issue comments via /mycoder, run with githubMode for issue-and-PR workflows, spawn parallel subagents with color-coded hierarchical logging, and accept mid-run human corrections interactively; MIT-licensed, npm-installable, and developed in a monorepo with Playwright browser automation built in."
---

MyCoder packages a Claude Code-style terminal agent behind a one-command npm install, with defaults tuned to get developers productive immediately. Its distinguishing surface is GitHub integration: with githubMode enabled, the agent works directly against issues and pull requests, and a /mycoder comment on an issue triggers a headless run that implements and opens a PR, turning issue triage into delegated automation. Subagents run in parallel for concurrent task processing, message compaction keeps long sessions inside the context window, and an interactive correction channel lets a developer redirect a running agent mid-task — a pattern borrowed from how parent agents message subagents. Model configuration spans Anthropic, OpenAI, and local Ollama endpoints, with MCP supplying external tools and context sources. The project maintains conventional-commit release automation through a pnpm monorepo, publishes continuously to npm, and targets developers who want GitHub workflow integration — comment-triggered PRs, issue-driven automation — rather than a purely local REPL.
