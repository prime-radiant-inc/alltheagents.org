---
name: "eca"
slug: "eca"
layout: "agent.njk"
category: "agent"
maker: "editor-code-assistant"
license: "Apache-2.0"
url: "https://github.com/editor-code-assistant/eca"
source_code_url: "https://github.com/editor-code-assistant/eca"
source_available: "True"
platforms:
  - "IDE"
first_released: "2025-06-16"
current_release: "2026-08-19"
stars: "968"
language: "Clojure"
homepage: "http://eca.dev"
mcp_support: "yes (stdio) — supports MCP resources and prompts for additional code context"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes — configure multiple agents with different models, tools, and behaviors"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, GitHub Copilot, Ollama"
pricing: "open-source"
install_method: "binary"
docs_url: "https://eca.dev"
plugin_docs_url: null
config_docs_url: "https://eca.dev/config/introduction"
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Editor-agnostic AI pair programming tool using an LSP-like protocol; a central server handles tool call management, multi-LLM interaction, telemetry, and unified configuration so any editor gets the same UX."
---

Every editor was growing its own AI plugin, each with different features and configuration; ECA borrows the LSP idea to end that: one Clojure server speaks a well-defined protocol, and editor integrations — Emacs, VS Code, IntelliJ, a desktop app — stay thin. The server owns chat, rewrite, and completion flows, multi-agent configuration with different models and tools per agent, MCP resources/prompts for context, and OpenTelemetry export of tool and prompt metrics. One global or local config makes behavior identical across editors. It appeals to developers who move between editors or use non-mainstream ones and want their AI setup to follow them.
