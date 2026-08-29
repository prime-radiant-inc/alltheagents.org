---
name: "EntwineLLM"
slug: "entwinellm"
layout: "agent.njk"
category: "agent"
maker: "EmilianoMusso"
license: "MIT"
url: "https://github.com/EmilianoMusso/EntwineLLM"
source_code_url: "https://github.com/EmilianoMusso/EntwineLLM"
source_available: "True"
platforms: []
first_released: "2024-11-23"
current_release: "2025-12-09"
stars: "37"
language: "C#, .NET (Visual Studio extension)"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: "False"
subagents: "False"
hooks: null
plan_mode: null
model_providers: "Ollama, LMStudio (any local LLM with API endpoint); bearer-token auth for reverse proxies (v1.13+)"
pricing: "Free"
install_method: "Install the Visual Studio extension; configure in Visual Studio Options (base URL, model, timeout, language); requires a running local LLM (Ollama or LMStudio) with an accessible API endpoint"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Free Visual Studio extension for code refactoring, unit-test generation, documentation (Markdown/HTML), and code review using only locally-installed LLMs (Ollama/LMStudio) so no data is sent to third-party APIs; strict prompt engineering rejects non-coding requests and enforces Clean Code principles, Allman-style braces, and modular/testable output; iterative follow-up refinement within the same workflow."
---

EntwineLLM exists for developers whose code cannot leave the machine — regulated environments, air-gapped networks, or simply preference for local inference. The extension sends selected code to an Ollama or LMStudio endpoint (local or Docker-hosted, with bearer-token auth added in v1.13 for proxied setups) and returns refactoring suggestions aligned with Clean Code principles, unit tests covering execution paths, Markdown documentation exportable to HTML, or a code review from a senior-developer perspective. Follow-up prompts allow iterative refinement, and per-command model and timeout settings let users route cheap tasks to smaller local models. It supports C#, Python, and Java, and is a single-maintainer project with modest but continuing releases.
