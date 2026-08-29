---
name: "deepclaude"
slug: "deepclaude"
layout: "agent.njk"
category: "agent"
maker: "aattaran"
license: "MIT"
url: "https://github.com/aattaran/deepclaude"
source_code_url: "https://github.com/aattaran/deepclaude"
source_available: "Yes"
platforms:
  - "Autonomous"
first_released: "2026-05-03"
current_release: "2026-07-23"
stars: "2250"
language: "Shell"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "yes"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "DeepSeek, OpenRouter, Fireworks AI, Anthropic"
pricing: "BYOK"
install_method: "binary"
docs_url: "https://github.com/aattaran/deepclaude#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/aattaran/deepclaude"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Swaps Claude Code's model backend while keeping its full autonomous agent loop (file editing, bash, git, subagents), achieving the same UX at ~17x lower cost with DeepSeek. Features live mid-session model switching via slash commands and automatic DeepSeek context caching."
---

deepclaude addresses the cost problem of running Claude Code for heavy daily use: it leaves the agent's loop, tools, and subagent machinery untouched and routes the model calls to DeepSeek V4 Pro through a local proxy, cutting output-token cost from $15/M to about $0.87/M. A localhost proxy (port 3200) intercepts requests, supports switching between DeepSeek, OpenRouter, Fireworks, and Anthropic mid-session via slash commands or keybindings, and exposes cost and benchmark endpoints. Users keep Claude Code's file editing, bash, git, and subagent behavior while trading away vision input, MCP server tools, and some complex-reasoning quality. It appeals to individual developers and teams running large volumes of agentic sessions who want the Claude Code UX without Anthropic pricing.
