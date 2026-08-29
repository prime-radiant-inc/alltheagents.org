---
name: "CodeMachine-CLI"
slug: "codemachine-cli"
layout: "agent.njk"
category: "multiplexer"
maker: "moazbuilds"
license: "Apache-2.0"
url: "https://github.com/moazbuilds/CodeMachine-CLI"
source_code_url: "https://github.com/moazbuilds/CodeMachine-CLI"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2025-09-28"
current_release: "2026-02-25"
stars: "2512"
language: "TypeScript"
homepage: "https://codemachine.co/"
mcp_support: null
plugin_support: null
claude_code_plugin: "n/a"
subagents: "yes"
hooks: null
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: "npm"
docs_url: "https://docs.codemachine.co"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Orchestration layer that runs AI coding CLIs (Claude Code, Codex, Cursor) through structured, long-running, repeatable workflows with parallel execution, context engineering, and multi-agent coordination."
---

CodeMachine-CLI starts from the observation that a coding workflow — the sequence of steps an operator runs an agent through to fix a bug or build a feature — normally exists only in the operator's head and gets rebuilt each session. The tool captures such workflows as definitions and re-executes them, spawning headless coding-agent CLIs (Claude Code, Codex, Cursor, and others), passing context between agents, running steps in parallel, and persisting state across runs that can span hours or days. It positions itself as an orchestration layer rather than an agent: the underlying coding engines do the work while CodeMachine handles coordination, agent-to-agent communication, and reproducibility. It is installed via npm, documented at docs.codemachine.co, and developed openly on GitHub with an active community.
