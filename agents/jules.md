---
name: "Jules"
slug: "jules"
layout: "agent.njk"
category: "agent"
maker: "Google"
license: "Proprietary"
url: "https://jules.google"
source_code_url: null
source_available: "False"
platforms:
  - "Web"
  - "CLI"
first_released: "2025"
current_release: "2026"
stars: null
language: null
homepage: "https://jules.google"
mcp_support: "no"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: "True"
model_providers: "Gemini (Gemini 2.5 Pro / Gemini 3 Pro)"
pricing: "Free (15 tasks/day, 3 concurrent); Pro (100 tasks/day, 15 concurrent); Ultra (300 tasks/day, 60 concurrent)"
install_method: "Web app — no local install. Visit jules.google.com, sign in with Google, connect GitHub."
docs_url: "https://jules.google/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "Async coding agent by Google that clones your repo to a Cloud VM, builds a plan using Gemini models, makes code edits, and opens pull requests for approval. GitHub-native workflow (assign via 'jules' label), plan-before-code, scales to massively parallel multi-agent development (up to 60 concurrent tasks on Ultra)."
---

Jules moves coding work off the developer's machine entirely: tasks are assigned through GitHub (a 'jules' label or a repo/branch prompt), and the agent works asynchronously on a cloud VM. The workflow is plan-first — Gemini drafts the approach, the user approves or edits it, then diffs are reviewed before Jules opens a pull request. Concurrency is the product's lever: up to 60 parallel tasks on the Ultra tier, making it suited to batch chores like dependency bumps, test backfill, and small features across many repos. Pricing ties to Google One AI tiers: free at 15 tasks/day, Pro at 100/day, Ultra at 300/day with priority model access.
