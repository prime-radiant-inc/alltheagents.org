---
name: "github"
slug: "github"
layout: "agent.njk"
category: "other"
maker: "axflow"
license: "MIT"
url: "https://github.com/axflow/axflow"
source_code_url: "https://github.com/axflow/axflow"
source_available: "True"
platforms:
  - "Web"
first_released: "2023-07-02"
current_release: "2024-03-02"
stars: "1121"
language: "TypeScript"
homepage: "https://axflow.dev"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "Any LLM (OSS or proprietary)"
pricing: "open-source"
install_method: "npm"
docs_url: "https://docs.axflow.dev"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Code-first modular framework for building natural-language-powered applications and AI development features in TypeScript. Modules can be adopted incrementally (models, chat, chains, agents) to form an end-to-end AI development framework. Includes React hooks for LLM integration. Last commit March 2024."
---

Axflow approached LLM application development the way a database toolkit approaches persistence: as a set of small, independently adoptable modules rather than one monolithic framework. The @axflow/models package provided a zero-dependency SDK with React hooks for streaming chat, axgen wired data sources into RAG pipelines, and axeval scored model outputs, with extract, serve, and finetune planned but never delivered. It targeted TypeScript teams building natural-language features into products rather than anyone running an autonomous coding loop. Development stalled after 264 commits — the roadmap modules never shipped and the last release activity was in early 2024 — leaving a 1.1k-star archive of a plausible framework that lost its window.
