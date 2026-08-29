---
name: "PRarena"
slug: "prarena"
layout: "agent.njk"
category: "other"
maker: "aavetis"
license: null
url: "https://github.com/aavetis/PRarena"
source_code_url: "https://github.com/aavetis/PRarena"
source_available: "True"
platforms: []
first_released: "2025-05-22"
current_release: "2026-08-19"
stars: "299"
language: "Python"
homepage: "https://prarena.ai"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: null
docs_url: "https://prarena.ai"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Tracks opened and merged pull requests created by top SWE coding agents (Copilot, Codex, Cursor, Devin, Codegen, Jules) to provide analytics on PR volume versus success (merge) rates."
---

PRarena answers a question benchmarks avoid: when real coding agents open pull requests against real GitHub repositories, how often do those PRs get merged? It runs GitHub search queries keyed on agent-specific identifiers — branch prefixes like head:codex/ or bot accounts such as devin-ai-integration[bot] — and tracks opened versus merged PRs per agent, updating a public dashboard and chart automatically. Comparisons use ready PRs only, since agents like Codex iterate privately before opening while Copilot and Codegen open drafts first, which would otherwise skew merge rates. The distinction between draft, ready, and merged states makes the comparison more honest than raw PR counts. Researchers and buyers of coding agents use it as one of the few population-scale measures of whether agent-authored work actually survives review.
