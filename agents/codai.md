---
name: "codai"
slug: "codai"
layout: "agent.njk"
category: "agent"
maker: "meysamhadeli"
license: "Apache-2.0"
url: "https://github.com/meysamhadeli/codai"
source_code_url: "https://github.com/meysamhadeli/codai"
source_available: "True"
platforms:
  - "CLI"
first_released: "2024-10-15"
current_release: "2025-08-29"
stars: "376"
language: "Go"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Ollama, Azure OpenAI, Anthropic, Gemini, Mistral, Grok, Qwen, DeepSeek, OpenRouter"
pricing: "Free / open-source"
install_method: "go install github.com/meysamhadeli/codai@latest"
docs_url: "https://pkg.go.dev/github.com/meysamhadeli/codai"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Terminal AI coding agent with context-aware code completions; summarizes full project context using Tree-sitter; maintains conversational/code context per session; supports multi-file modifications simultaneously; tracks token consumption per request."
---

Codai targets developers who want a terminal-native assistant that understands whole-project structure rather than single files: Tree-sitter parsing produces a summarized context of the codebase in six languages, which the assistant uses for multi-file edits, refactoring, test generation, and review, with per-session conversational and code context and per-request token accounting. Configuration is a single YAML file plus environment variables, with provider, model, and temperature switchable per invocation. It is a solo Go project, self-described work in progress, whose development has been intermittent, with the most recent commits in August 2025.
