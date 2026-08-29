---
name: "Agentic Engineering Framework"
slug: "agentic-engineering-framework"
layout: "agent.njk"
category: "multiplexer"
maker: "DimitriGeelen"
license: "Apache-2.0"
url: "https://github.com/DimitriGeelen/agentic-engineering-framework"
source_code_url: "https://github.com/DimitriGeelen/agentic-engineering-framework"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-03-03"
current_release: "2026-08-16"
stars: "13"
language: "Bash, YAML"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Claude Code, Cursor, Aider, Devin, Copilot"
pricing: "open-source"
install_method: "curl install script; brew install DimitriGeelen/agentic-fw/agentic-fw; local clone; GitHub Action; fw init per-project"
docs_url: "https://github.com/DimitriGeelen/agentic-engineering-framework/blob/master/FRAMEWORK.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://raw.githubusercontent.com/DimitriGeelen/agentic-engineering-framework/master/install.sh"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Governance and continuity harness around AI coding agents. Provides task traceability, structural gates, session continuity, audit trails, blast-radius foresight, value scoring, and cross-agent coordination. It coordinates agents but does not execute them. Enforces 'nothing gets done without a task' as a hard gate (PreToolUse hooks), three-layer persistent memory, Component Fabric for blast-radius impact analysis, Business Value Points (BVP) scoring, a tiered authority model (human sovereignty / framework authority / agent initiative), and 260+ audit checks. Develops itself under its own governance."
---

AI coding agents fail in predictable ways: they edit without a task, destroy files with force flags, and run out of context mid-change. The framework interposes itself between the agent and the repository using a PreToolUse hook, tiered authority rules (human sovereignty, framework authority, agent initiative), and Markdown task files with YAML frontmatter carrying acceptance criteria and verification commands. A budget gate watches the live transcript and blocks source edits when the context window nears its limit, forcing a commit and handover instead of a truncated change. Memory, component maps, and audit checks (over 260 checks run on every push and on a 30-minute cron) provide continuity and traceability across sessions. It is used by developers running Claude Code who want audit-grade accountability; the framework itself is developed under its own governance, with thousands of self-governed commits.
