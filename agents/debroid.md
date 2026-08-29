---
name: "debroid"
slug: "debroid"
layout: "agent.njk"
category: "other"
maker: "PatilShreyas"
license: "Apache-2.0"
url: "https://github.com/PatilShreyas/debroid"
source_code_url: "https://github.com/PatilShreyas/debroid"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2026-08-02"
current_release: "2026-08-09"
stars: "184"
language: "Kotlin"
homepage: "https://github.com/PatilShreyas/debroid"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: null
pricing: "Free / open source (Apache-2.0)"
install_method: "curl -fsSL https://raw.githubusercontent.com/PatilShreyas/debroid/main/install.sh | bash; or build from source"
docs_url: "https://github.com/PatilShreyas/debroid#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/PatilShreyas/debroid/releases"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Headless CLI tool that speaks the Java Debug Wire Protocol (JDWP), allowing AI coding agents (Claude Code, Grok Build, Codex, OpenCode, Cursor, Antigravity) to debug live Android apps from the terminal. Features strict JSON output for agent consumption, persistent background daemon architecture, full debugging capabilities (breakpoints, watchpoints, exception traps, deep object inspection, live variable mutation, expression evaluation), Kotlin coroutine support, and ships with SKILL.md for agent integration."
---

Debroid addresses a gap in AI-assisted Android development: coding agents can edit code and run builds, but until now they had no way to debug a running app. The headless CLI speaks JDWP to the app's Dalvik/ART VM over an ADB port-forward, keeping the connection alive in a background daemon so agent commands (breakpoints, exception catches, stepping, variable inspection and mutation, expression evaluation) return immediately as parseable JSON. Integration is through skills rather than MCP: a SKILL.md is symlinked into each agent's skills directory so Claude Code, Cursor, Codex, OpenCode, and similar CLIs learn the command vocabulary. The daemon exposes live JVM manipulation on localhost without authentication, so it is meant for trusted developer machines; it is Apache-2.0, built in Kotlin/Java, and targets Android engineers who run agentic workflows.
