---
name: "2389 Claude Plugins"
slug: "claude-plugins-2389"
layout: "agent.njk"
category: "other"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/claude-plugins"
source_code_url: "https://github.com/2389-research/claude-plugins"
source_available: "True"
platforms:
  - "IDE"
first_released: null
current_release: null
stars: "93"
language: "JavaScript"
homepage: null
mcp_support: "yes (includes MCP servers)"
plugin_support: "yes (28 plugins and MCP servers)"
claude_code_plugin: "yes"
subagents: "yes (multi-agent orchestration plugin)"
hooks: "yes (TDD, iterative refinement, structured decisions)"
plan_mode: "yes (structured decision plugins)"
model_providers: "Claude (via Claude Code)"
pricing: "free"
install_method: "/plugin marketplace add 2389-research/claude-plugins"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Collection of 28 plugins and MCP servers for Claude Code covering TDD, multi-agent orchestration, iterative refinement, binary reverse engineering, structured decisions, and more. Install any skill in one command via the Claude Code plugin marketplace."
---

2389 Research's claude-plugins repo is a curated marketplace entry point for their Claude Code ecosystem: 28 plugins and MCP servers installable with a single `/plugin marketplace add` command. The collection spans TDD workflows, multi-agent orchestration, iterative refinement (Simmer), binary reverse engineering, structured decision-making, and specialized tools — each running inside Claude Code's existing agent loop rather than defining its own. Individual plugins like Thrifty, Simmer, and Binary RE have their own repos and census entries; this repo is the umbrella that makes them installable as a set. Developers browsing the marketplace pick the skills they need, and Claude Code's plugin system handles discovery, installation, and invocation.
