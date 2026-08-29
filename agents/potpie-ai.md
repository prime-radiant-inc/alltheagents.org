---
name: "Potpie AI"
slug: "potpie-ai"
layout: "agent.njk"
category: "agent"
maker: "Potpie"
license: "Apache-2.0"
url: "https://potpie.ai"
source_code_url: null
source_available: "True"
platforms:
  - "Web"
first_released: "2025"
current_release: "2026"
stars: null
language: "Python"
homepage: null
mcp_support: null
plugin_support: "True"
claude_code_plugin: "True"
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "Custom quote-based pricing (per-user licensing + platform fee). No public pricing tiers. No explicit free plan mentioned."
install_method: "pip or uv via PyPI: 'uv tool install potpie' or 'python3 -m pip install --user potpie'"
docs_url: "https://docs.potpie.ai"
plugin_docs_url: null
config_docs_url: "https://docs.potpie.ai"
download_url: "https://github.com/potpie-ai/potpie"
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "Turns codebase and SDLC into a living context graph for AI agents - indexes code, structure, decisions, source history, team knowledge, and engineering workflows so agents can answer questions, plan changes, debug failures, and write code with project-specific context. Integrates with GitHub, Linear, Jira, and Confluence. Supports Claude Code, OpenAI Codex, Cursor, and OpenCode as coding harnesses via a skills system."
---

Potpie addresses the problem that coding agents answer questions about unfamiliar codebases poorly because they lack indexed, structural understanding of the code. On installation it parses a repository into a knowledge graph of functions, classes, dependencies, and their relationships, then runs purpose-built agents — debugging, test generation, codebase Q&A, implementation planning — that traverse that graph rather than guessing from raw text. Each agent is reachable through a hosted app or the open-source self-hosted runtime, and a Claude Code plugin exposes the same indexed context to agents developers already use. Teams adopt it for recurring workflows like root cause analysis, regression test generation, and impact analysis, where per-incident prompting does not scale. The open-source core plus enterprise pricing model suits organizations that want the context layer inside their own infrastructure.
