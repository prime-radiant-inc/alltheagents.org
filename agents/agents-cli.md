---
name: "agents-cli"
slug: "agents-cli"
layout: "agent.njk"
category: "multiplexer"
maker: "phnx-labs"
license: "Apache-2.0"
url: "https://github.com/phnx-labs/agents-cli"
source_code_url: "https://github.com/phnx-labs/agents-cli"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-04-20"
current_release: "2026-08-19"
stars: "14"
language: "TypeScript"
homepage: "https://agi-cli.sh"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Claude Code, Codex CLI, Antigravity, Grok Build, OpenClaw, Cursor, OpenCode, Copilot, Amp, Kiro, Kimi, MiniMax, GLM, Qwen, DeepSeek (via OpenRouter), Factory AI Droid, Meta Muse Code, Warp Agent CLI, Hermes Agent, Ollama, vLLM"
pricing: "free"
install_method: "npm install -g @phnx-labs/agents-cli (or curl -fsSL agi-cli.sh | sh)"
docs_url: "https://agi-cli.sh/learn/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@phnx-labs/agents-cli"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Distributed agent factory — dispatches multiple AI coding agents (Claude, Codex, Antigravity, Grok, etc.) across your own machines in parallel on existing subscriptions. Fleet management, cross-agent session search, performance insights, routines/monitors scheduling, browser automation via your real Chrome, menu-bar fleet control, and one-config-syncs-to-all-agents resource management. Note: repo redirects to phnx-labs/agi-cli."
---

Individual developers accumulate subscriptions to several coding agents but can only run one or two at a time on a laptop. agents-cli turns the collection of machines a user already has into a dispatchable fleet: agents.yaml profiles are reconciled onto each device over SSH, OAuth logins stay native per machine rather than being copied, and runs fan out to one device or all of them through the same CLI. Routines (cron-style schedules) and event-driven monitors turn recurring work into scheduled jobs, while the feed, insights, and a macOS menu bar surface every open question across the fleet. Teams run parallel agents in dependency order, each in an isolated worktree, and cloud dispatch can hand tasks to managed providers that open PRs. It is free with no account requirement, licensed under FSL-1.1-Apache-2.0.
