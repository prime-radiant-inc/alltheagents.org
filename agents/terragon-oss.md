---
name: "terragon-oss"
slug: "terragon-oss"
layout: "agent.njk"
category: "multiplexer"
maker: "terragon-labs"
license: "Apache-2.0"
url: "https://github.com/terragon-labs/terragon-oss"
source_code_url: "https://github.com/terragon-labs/terragon-oss"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
  - "Autonomous"
first_released: "2026-01-16"
current_release: "2026-02-10"
stars: "257"
language: "TypeScript"
homepage: "https://www.terragonlabs.com/"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Claude Code, OpenAI Codex, Amp, Gemini"
pricing: "Free / open-source (provided as-is)"
install_method: "git clone + pnpm install (prerequisites: Node.js v20+, pnpm v10.14.0+, Docker, Stripe CLI); also terragon-setup.sh script"
docs_url: "https://www.terragonlabs.com/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/terragon-labs/terragon-oss"
maintained: "dormant"
sources:
  - "github_deep"
what_makes_it_special: "Remote background agent orchestrator for coding CLIs in the cloud. Multi-agent support with sandbox isolation per agent. Seamless automatic git workflow (branches, commits, PRs). Local handoff via terry CLI. MCP server for task management. BYO subscriptions/API keys. Integrates with Slack/GitHub via @-mentions. Real-time task status streaming to browser. NOTE: This is a snapshot at time of shutdown (January 16, 2026), provided as-is with no maintenance."
---

Terragon Labs operated a hosted service that ran coding CLIs such as Claude Code, Codex, Amp, and Gemini in cloud sandboxes, letting developers fire tasks at multiple agents in parallel and receive branches, commits, and pull requests automatically. After shutting the product down, the company published this repository — a single-snapshot Apache-2.0 monorepo (two commits) containing the web app, WebSocket broadcast service, docs site, sandbox provisioning, and the terry CLI for handing tasks back to a local environment. Features included per-agent sandbox isolation, automated git workflows, an MCP server for task management, Slack and GitHub integrations, and BYO subscriptions or API keys. Because the snapshot is explicitly provided as-is with no maintenance or completeness guarantees, it functions as a reference implementation of a background-agent orchestration platform rather than a live tool. Developers studying how such orchestrators are assembled, or forking the architecture, are its remaining audience.
