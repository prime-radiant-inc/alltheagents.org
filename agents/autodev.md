---
name: "AutoDev"
slug: "autodev"
layout: "agent.njk"
category: "agent"
maker: "phodal"
license: "MPL-2.0"
url: "https://github.com/unit-mesh/auto-dev"
source_code_url: "https://github.com/unit-mesh/auto-dev"
source_available: "True"
platforms:
  - "IDE"
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
download_url: "https://github.com/unit-mesh/auto-dev/releases"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "AI-native multi-agent development platform built on Kotlin Multiplatform (JVM, Android, iOS, JS, WASM from a single codebase). Core agents (Document, Coding, CodeReview, ChatDB, Artifact) + 9 specialized SubAgents following 'agent-as-tool' pattern. MCP integration, A2A agent commands, Claude Skill loading, SpecKit integration, AGENTS.md awareness, Tree-sitter code intelligence, artifact generation. Ships as IntelliJ plugin, VS Code extension, CLI, desktop, and web."
---

AutoDev, by Phodal (Huang Yi) under the UnitMesh umbrella, is an AI-native multi-agent development platform rebuilt on Kotlin Multiplatform so the same agent core runs on JVM, Android, iOS, JS, and WASM. Top-level agents cover coding, document research, code review, ChatDB (natural-language SQL), and artifact generation, each backed by a shared runtime of filesystem, grep/glob, shell, web, and MCP tools, plus a subagent layer ('agent as tool') with specialists like NanoDSL, PlotDSL, Error Recovery, and Codebase Investigator. Tree-sitter parsing covers Java, Kotlin, Python, JS/TS, Go, Rust, and C#, and multi-LLM support spans OpenAI, Anthropic, Google, DeepSeek, and Ollama. Distribution spans a JetBrains plugin, VS Code extension, web.xiuper.com, npm CLI (@xiuper/cli), and desktop/mobile builds under MPL-2.0. The phodal/auto-dev repository mirrors the same project; version 3.0 'Xiuper' is in alpha.
