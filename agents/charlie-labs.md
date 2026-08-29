---
name: "Charlie Labs"
slug: "charlie-labs"
layout: "agent.njk"
category: "agent"
maker: "Charlie Labs"
license: "Proprietary"
url: "https://charlielabs.ai"
source_code_url: null
source_available: null
platforms:
  - "Autonomous"
first_released: null
current_release: null
stars: null
language: null
homepage: "https://charlielabs.ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes (multiple daemons per repo, each with its own watch triggers and routines)"
hooks: "yes (watch triggers on events: PR merged, Linear issue created, cron schedules)"
plan_mode: "no"
model_providers: "Proprietary (provider not disclosed)"
pricing: "usage"
install_method: "SaaS (install the Charlie GitHub app; define daemons as .md files in-repo)"
docs_url: "https://docs.charlielabs.ai"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Charlie: GitHub-native AI engineer for issues-to-PRs"
---

Charlie Labs builds Charlie, an AI engineer platform organized around 'daemons': persistent agents that watch repositories and proactively perform recurring engineering work without being prompted each time. A daemon is declared in a markdown file in the repository with frontmatter specifying its watch triggers (events like a merged PR or a new Linear issue), scheduled routines, and deny rules that bound what it may do — never merging PRs, never overriding human decisions — alongside markdown policy sections defining its role. This addresses a gap between one-shot AI coding tools and human maintainer attention: dependency upgrades, PR hygiene, issue triage, and changelog upkeep happen continuously without a developer initiating each task. Daemons wake on events (new issues, merges, security advisories) and run scheduled sweeps, opening reviewable PRs and building compounding organizational memory. Engineering teams adopt Charlie by installing its GitHub integration and committing daemon definitions to their repos, with pricing based on shared team token usage.
