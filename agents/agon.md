---
name: "Agon"
slug: "agon"
layout: "agent.njk"
category: "agent"
maker: "AutoResearch-Factory"
license: "MIT"
url: "https://github.com/AutoResearch-Factory/Agon"
source_code_url: "https://github.com/AutoResearch-Factory/Agon"
source_available: "True"
platforms:
  - "IDE"
  - "Autonomous"
first_released: "2026-06-18"
current_release: "2026-08-18"
stars: "41"
language: "Python"
homepage: "https://haizhaoyang.github.io/research/autoresearch.html"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "no"
model_providers: "Anthropic, DeepSeek"
pricing: "open-source"
install_method: "git clone Agon and agon-artifacts side by side; run claude --plugin-dir ../Agon --dangerously-skip-permissions --effort medium --model claude-sonnet-5"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/AutoResearch-Factory/Agon"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Autonomous AI research system built on the 'Prompt Economy' concept. Agents (scientist, coder, auditor, reviewer) plan, implement, audit, and review each other in closed loops with all handoffs via files on disk for recoverability and auditability. Runs unattended for hours. Deployable across 10+ research domains. No human-written experimental code needed."
---

Running AI research loops unattended for hours usually produces unrecoverable messes, and the engineering effort of orchestrating agents lands on the human. Agon, distributed as a Claude Code plugin, pushes all coordination into disk files: topics, ideas, proposals, and experiments live in a side-by-side agon-artifacts repository, so any run can be inspected, resumed, or forked independently of the plugin code. Slash commands drive role-structured loops — /idea-tick, /proposal-tick, and /experiment-tick, which coordinates scientist, coder, auditor, and reviewer roles per workspace — with prompts, code, and research data versioned independently. Loops run under --dangerously-skip-permissions for genuinely unattended operation, and wrapper scripts let the same plugin run Claude Code backed by DeepSeek or other providers via CLIProxyAPI. It targets researchers automating the topic-to-running-experiment pipeline across domains.
