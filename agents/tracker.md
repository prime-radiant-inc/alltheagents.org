---
name: "Tracker"
slug: "tracker"
layout: "agent.njk"
category: "multiplexer"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/tracker"
source_code_url: "https://github.com/2389-research/tracker"
source_available: "True"
platforms:
  - "CLI"
first_released: null
current_release: null
stars: "19"
language: "Go"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes (parallel agent fan-out/fan-in, subgraphs)"
hooks: "yes (human-in-the-loop gates)"
plan_mode: "yes (pipeline definitions in .dip files)"
model_providers: "Anthropic, OpenAI, Gemini, OpenAI-compatible APIs"
pricing: "free"
install_method: "brew install 2389-research/tap/tracker or go install"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Pipeline orchestration engine for multi-agent LLM workflows that executes pipelines defined in the Dippin DSL (.dip files) with parallel LLM agents, human-in-the-loop gates, Slack bot and terminal REPL front-ends, cost governance/budget limits, decision audit trails, and git checkpointing. Embedded workflows include ask_and_execute (competitive implementation across Claude/Codex/Gemini) and build_product (milestone-based spec-driven building)."
---

Tracker is a pipeline orchestration engine for multi-agent LLM workflows rather than a coding agent itself. Pipelines are authored in the Dippin DSL as .dip files — node graphs of agent, tool, human, parallel, and subgraph steps — and Tracker executes them with parallel LLM agent fan-out and fan-in, human-in-the-loop gates that pause for approval, and budget limits that enforce cost governance. A human-facing TUI dashboard surfaces live status, and Slack bot and terminal REPL front-ends let operators drive runs from where they already work. Every decision is recorded to an audit trail and each step is git-checkpointed, so a failed run can be inspected and resumed. Embedded workflows ship out of the box: ask_and_execute runs competitive implementations across Claude, Codex, and Gemini, and build_product drives milestone-based spec-driven building. The audience is teams orchestrating coding agents through defined, reviewable pipelines.
