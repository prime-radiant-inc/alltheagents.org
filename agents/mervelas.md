---
name: "Mervelas"
slug: "mervelas"
layout: "agent.njk"
category: "agent"
maker: "swadhinbiswas"
license: "MIT"
url: "https://github.com/swadhinbiswas/Mervelas"
source_code_url: "https://github.com/swadhinbiswas/Mervelas"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-04-02"
current_release: "2026-04-03"
stars: "52"
language: "TypeScript"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: "False"
subagents: "True"
hooks: null
plan_mode: null
model_providers: "OpenAI, OpenRouter, NVIDIA NIM, Qwen, DeepSeek, local models"
pricing: "Free / open-source"
install_method: "git clone + bun install + bun run scripts/build.ts + node dist/cli.mjs (requires Bun)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "github_deep"
what_makes_it_special: "Independent open-source AI coding CLI built for freedom and zero telemetry, local-first, built with Bun and rendered via a custom React Ink abstraction; supports custom local coding agents and MCP integration."
---

Mervelas exists for developers who reject the telemetry and lock-in of mainstream assistants: it stores session history only in ~/.mervelas/projects/ as JSONL, ships with no analytics, and lets the user point it at OpenAI, OpenRouter, NVIDIA NIM, Qwen, DeepSeek, or locally hosted endpoints. The interface is a terminal UI rendered through a custom React Ink abstraction built on Bun, with commands for configuration, context inspection, agent switching, and MCP server attachment. Custom agents are defined and switched through /agents, letting one binary wrap different local coding agents under a single interface. Distribution is deliberately absent from npm: the README requires cloning, building with Bun, and running the bundle directly, and the repository holds exactly five commits with no releases. Its audience is developers who want provider sovereignty and zero telemetry and are comfortable building a CLI from source; the project is experimental and its trajectory depends on a single maintainer.
