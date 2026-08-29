---
name: "Traycer"
slug: "traycer"
layout: "agent.njk"
category: "multiplexer"
maker: "traycerai"
license: "MIT"
url: "https://github.com/traycerai/traycer"
source_code_url: "https://github.com/traycerai/traycer"
source_available: "True"
platforms:
  - "CLI"
  - "Desktop"
first_released: "2024-05-11"
current_release: "2026-08-20"
stars: "1207"
language: "TypeScript"
homepage: "https://traycer.ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic, OpenAI, Cursor, OpenCode"
pricing: "open-source"
install_method: "binary"
docs_url: "https://docs.traycer.ai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://traycer.ai/download"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Open-source AI orchestration app for advanced agent orchestration. Bring Your Own Agent (BYOA) to use existing subscriptions without paying twice. Unified context to instantly switch models within the same agent with seamlessly shared memory. Agent-to-agent communication for tasks like debates or code reviews. Integrated team collaboration features."
---

The open-source Traycer app exists so developers can orchestrate the agents they already pay for instead of duplicating spend on a new inference subscription. It connects existing agent CLIs under one desktop workspace where the context window is shared across providers, enabling mid-task model switches, and automates agent-to-agent loops such as architecture debates and peer code review. Team collaboration features add shared boards, real-time editing, and ticket assignment, while Privacy Mode (default on for Team plans) keeps code in memory only. Developers and small teams running several agent subscriptions install the free desktop app on macOS, Linux, or Windows; the codebase is an active TypeScript/Bun monorepo with nearly a thousand commits, and optional Traycer-side inference exists for users who prefer not to BYO.
