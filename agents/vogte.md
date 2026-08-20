---
name: "vogte"
slug: "vogte"
layout: "agent.njk"
category: "agent"
maker: "piqoni"
license: "MIT"
url: "https://github.com/piqoni/vogte"
source_code_url: "https://github.com/piqoni/vogte"
source_available: True
platforms: []
first_released: "2025-07-30"
current_release: "2026-05-12"
stars: "180"
language: "Go"
homepage: null
mcp_support: False
plugin_support: False
claude_code_plugin: False
subagents: False
hooks: False
plan_mode: False
model_providers: "OpenAI, Anthropic, AWS Bedrock"
pricing: "Free / open source (MIT); uses your own API keys"
install_method: "go install github.com/piqoni/vogte@latest"
docs_url: "https://github.com/piqoni/vogte#readme"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Agentic TUI for existing Go codebases that uses AST parsing to extract compressed, relevant context for the LLM. Two-step context approach: first extracts structs/interfaces/methods/signatures, asks LLM which files it needs in full, then provides full content. Runs go vet as a sanity check after patching. Stateless design (each message is a new chat) for cost-effectiveness. Features local PR review and context generation for web-based LLMs."
---

Agentic TUI for existing Go codebases that uses AST parsing to extract compressed, relevant context for the LLM. Two-step context approach: first extracts structs/interfaces/methods/signatures, asks LLM which files it needs in full, then provides full content. Runs go vet as a sanity check after patching. Stateless design (each message is a new chat) for cost-effectiveness. Features local PR review and context generation for web-based LLMs.
