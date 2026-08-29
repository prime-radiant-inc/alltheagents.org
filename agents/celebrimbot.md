---
name: "Celebrimbot"
slug: "celebrimbot"
layout: "agent.njk"
category: "agent"
maker: "GiacomoSaccaggi"
license: null
url: "https://plugins.jetbrains.com/plugin/32055-celebrimbot"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-07-09"
current_release: null
stars: null
language: "Kotlin"
homepage: "https://plugins.jetbrains.com/plugin/32055-celebrimbot"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Local model with cloud escalation (LazyModelManager loads on demand, unloads after 60s idle)"
pricing: "free"
install_method: "Install from the JetBrains Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/32055-celebrimbot"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Full multi-agent AI system that reads, writes, executes"
---

Celebrimbot is an IntelliJ plugin that embeds a multi-agent AI coding system directly in JetBrains IDEs. From a single chat panel the system reads project files, writes and modifies code, executes terminal commands, searches the web, and inspects git history, with an agentic loop that routes requests, executes tasks locally where possible, and escalates to cloud planning only when the task requires it, retrying failures automatically. Its architecture splits into three modules — a pure-Kotlin core, the IntelliJ plugin layer, and a standalone CLI/HTTP server — with a lazy model manager that loads the model on first use and unloads it after 60 seconds of inactivity to avoid taxing IDE memory. This targets JetBrains developers who want an agentic, tool-using assistant inside their IDE without the per-token subscription model of cloud-bound competitors. It is distributed free on the JetBrains Marketplace (created July 2026) under an Apache-2.0 license, with source available on GitHub.
