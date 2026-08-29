---
name: "Linear-Coding-Agent-Harness"
slug: "linear-coding-agent-harness"
layout: "agent.njk"
category: "agent"
maker: "coleam00"
license: "MIT"
url: "https://github.com/coleam00/Linear-Coding-Agent-Harness"
source_code_url: "https://github.com/coleam00/Linear-Coding-Agent-Harness"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2025-12-07"
current_release: "2026-01-28"
stars: "227"
language: "Python"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: null
model_providers: "Anthropic"
pricing: "Free"
install_method: "npm install -g @anthropic-ai/claude-code; pip install -r requirements.txt"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/coleam00/Linear-Coding-Agent-Harness"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Minimal harness demonstrating long-running autonomous coding with the Claude Agent SDK; two-agent pattern (initializer + coding agent) with Linear as the core project management system for tracking all work. Uses Linear MCP (HTTP) and Puppeteer MCP (stdio)."
---

The harness demonstrates a specific architectural idea: put the agent's entire task state in Linear rather than local files, so any session — or a new machine — can resume work by querying the tracker. An initializer agent reads an app spec, creates the Linear project, issues, and a META issue; coding agents then pull Todo issues, implement with Claude, test through Puppeteer MCP, comment results, and close issues. Session handoff happens through Linear comments, making runs resumable and inspectable from anywhere Linear is. Colem00 published it as a minimal MIT-licensed reference (2 commits) that others fork to build Linear-integrated autonomous loops.
