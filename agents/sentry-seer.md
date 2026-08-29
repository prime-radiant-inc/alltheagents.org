---
name: "Sentry Seer"
slug: "sentry-seer"
layout: "agent.njk"
category: "agent"
maker: "Sentry"
license: null
url: "https://sentry.io"
source_code_url: null
source_available: null
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: "https://sentry.io/product/seer/"
mcp_support: "yes"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: null
docs_url: "https://docs.sentry.io"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "AI debugging agent: RCA from telemetry + fix PRs + PR review"
---

Seer exists because Sentry already holds the strongest debugging signal available — production telemetry correlated with deploys — and an agent grounded in that data can explain why code failed rather than where. The product ships as four surfaces: automatic root-cause analysis on every issue, Autofix patches proposed as merge-ready diffs, AI code review on pull requests informed by the project's error history, and a conversational Seer Agent inside Sentry. Because it consumes first-party telemetry, adoption is natural for existing Sentry customers, with fixes reviewed through the normal PR flow. Sentry operates it as a commercial SaaS product with its own pricing page, alongside the MCP server that lets Claude Code and similar tools pull Sentry context. It targets production engineering teams debugging at scale.
