---
name: "ai-doc-gen"
slug: "ai-doc-gen"
layout: "agent.njk"
category: "agent"
maker: "divar-ir"
license: "MIT"
url: "https://github.com/divar-ir/ai-doc-gen"
source_code_url: "https://github.com/divar-ir/ai-doc-gen"
source_available: True
platforms: []
first_released: "2025-07-19"
current_release: "2026-07-21"
stars: "748"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "yes (Claude Code plugin)"
claude_code_plugin: "yes (/plugin marketplace add divar-ir/ai-doc-gen; /plugin install ai-doc-gen@divar)"
subagents: "yes (5 specialized analysis agents: code structure, data flow, dependencies, request flow, APIs; coordinated by AnalyzerAgent via worker pool)"
hooks: "no"
plan_mode: "no"
model_providers: "any OpenAI-compatible (OpenAI, Anthropic-compatible gateways, OpenRouter, local models)"
pricing: "open-source"
install_method: "Claude Code plugin install, pip (uv sync), docker"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "AI-powered multi-agent system that analyzes codebases and generates documentation (README.md) plus AI assistant configuration files (CLAUDE.md, AGENTS.md, .cursor/rules/). 5 specialized AI agents run in parallel for deep analysis. Dual-purpose as Claude Code plugin (no API keys needed). GitLab cronjob automation discovers active projects and opens MRs with fresh docs. Production-ready with Docker, Helm, OpenTelemetry/Langfuse observability."
---

AI-powered multi-agent system that analyzes codebases and generates documentation (README.md) plus AI assistant configuration files (CLAUDE.md, AGENTS.md, .cursor/rules/). 5 specialized AI agents run in parallel for deep analysis. Dual-purpose as Claude Code plugin (no API keys needed). GitLab cronjob automation discovers active projects and opens MRs with fresh docs. Production-ready with Docker, Helm, OpenTelemetry/Langfuse observability.
