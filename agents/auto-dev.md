---
name: "auto-dev"
slug: "auto-dev"
layout: "agent.njk"
category: "agent"
maker: "phodal"
license: "MPL-2.0"
url: "https://github.com/phodal/auto-dev"
source_code_url: "https://github.com/phodal/auto-dev"
source_available: "True"
platforms: []
first_released: "2023-04-14"
current_release: "2026-08-04"
stars: "4534"
language: "Kotlin"
homepage: "https://ide.unitmesh.cc/"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Google, DeepSeek, Ollama"
pricing: "open-source"
install_method: "vscode"
docs_url: "https://ide.unitmesh.cc/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/phodal/auto-dev/releases"
maintained: "active"
sources:
  - "github_final"
what_makes_it_special: "Same project as unit-mesh/auto-dev (GitHub redirect). AI-native multi-agent development platform built on Kotlin Multiplatform (JVM, Android, iOS, JS, WASM). Core agents (Document, Coding, CodeReview, ChatDB, Artifact) + 9 specialized SubAgents, MCP integration, AGENTS.md awareness, Tree-sitter code intelligence. Ships as IntelliJ plugin, VS Code extension, CLI, desktop, and web."
---

AutoDev, created by Phodal (Huang Yi), is an AI-native multi-agent development platform now in its third generation, 'Xiuper', built on Kotlin Multiplatform so a single codebase targets JVM, Android, iOS, JS, and WASM. Core agents cover coding, document research, code review, ChatDB (natural-language SQL), and artifact generation, with a 'agent as tool' layer of specialized micro-agents such as NanoDSL for UI code, PlotDSL for charts, Error Recovery, and E2E testing. The shared runtime provides file, grep/glob, shell, web, and MCP tools, automatic AGENTS.md discovery and injection, tree-sitter code intelligence across seven languages, and multi-LLM support spanning OpenAI, Anthropic, Google, DeepSeek, and Ollama. It reaches users through IntelliJ and VS Code plugins, an npm CLI (@xiuper/cli), web.xiuper.com, and GitHub releases under MPL-2.0, with docs at ide.unitmesh.cc. The phodal and unit-mesh repositories mirror the same project; version 3.0 is alpha while 2.0 remains the stable branch.
