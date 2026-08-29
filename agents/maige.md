---
name: "Maige"
slug: "maige"
layout: "agent.njk"
category: "agent"
maker: null
license: "AGPL-3.0"
url: "https://maige.app"
source_code_url: null
source_available: "True"
platforms: []
first_released: "2024-05-01"
current_release: "2026-08-28"
stars: null
language: "TypeScript"
homepage: "https://maige.app"
mcp_support: "no"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: null
pricing: "Standard $30/month; Enterprise coming soon"
install_method: "Self-host: bun i + bun run dev (with GitHub App + ngrok); or hosted via GitHub App install"
docs_url: "https://github.com/RubricLab/maige"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "e2b"
what_makes_it_special: "Open-source infrastructure by Rubric Labs for running natural language workflows on your codebase; auto-labels, assigns, comments on, and reviews issues/PRs via a GitHub App. Currently in alpha."
---

Maige automates the triage and review labor that consumes maintainer time on active repositories: plain-language rules replace webhooks-plus-scripts, so instructions like 'review any PR touching auth for security issues' or 'label new issues by component' become standing agent behavior. Runs execute in a sandbox against codebase embeddings, letting the agent label, assign, comment, review, and propose code changes through the GitHub API. The hosted service costs $30/month after 30 free issues, and the AGPL-licensed source supports self-hosting for teams that want their own deployment. Repositories such as Documenso, Nuxt, Highlight.io, and Cal.com have used it; the product remains in alpha under Rubric Labs.
