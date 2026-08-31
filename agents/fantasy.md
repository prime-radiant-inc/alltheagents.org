---
name: "Fantasy"
slug: "fantasy"
layout: "agent.njk"
category: "agent-sdk"
maker: "charmbracelet"
license: "Apache-2.0"
url: "https://github.com/charmbracelet/fantasy"
source_code_url: "https://github.com/charmbracelet/fantasy"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-08-15"
current_release: "2026-08-19"
stars: "954"
language: "Go"
homepage: null
mcp_support: null
plugin_support: "no"
claude_code_plugin: "no"
subagents: null
hooks: null
plan_mode: null
model_providers: "Azure, Amazon Bedrock, OpenRouter, OpenAI-compatible (via openaicompat)"
pricing: "open-source"
install_method: "go"
docs_url: "https://pkg.go.dev/charm.land/fantasy"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "author_search"
what_makes_it_special: "A unified Go library for building AI agents with a single API across many LLM providers and models, compiling to native machine code; built to power Charm's Crush coding agent."
---

Fantasy came out of Charmbracelet's work on Crush, their terminal coding agent, when the team needed a multi-provider LLM layer in Go that could compile to a single native binary. It exposes fantasy.NewAgent() with system prompts and typed tools, normalizes streaming, retries, JSON repair, and structured output generation across providers, and ships dedicated packages for OpenRouter, Azure, and Bedrock plus a generic openaicompat layer for everything else. Because it is a library, decisions about the loop, the UI, and permissions belong to the embedding program — Crush being the reference implementation. Go developers building terminal-native AI tools use it to avoid writing provider adapters themselves.
