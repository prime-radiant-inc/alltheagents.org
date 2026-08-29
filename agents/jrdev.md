---
name: "jrdev"
slug: "jrdev"
layout: "agent.njk"
category: "agent"
maker: "presstab"
license: "MIT"
url: "https://github.com/presstab/jrdev"
source_code_url: "https://github.com/presstab/jrdev"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2025-03-13"
current_release: "2026-06-28"
stars: "67"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: null
hooks: "False"
plan_mode: null
model_providers: "Anthropic, Google, DeepSeek, OpenAI, Mistral"
pricing: "Free and open-source (BYO API keys)"
install_method: "pip install jrdev (PyPI), or install from GitHub source"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Terminal AI developer assistant with smart project indexing (/init) that scans codebase and infers conventions; uses multiple AI models for different task tiers to balance cost and performance; smart controls for reviewing/editing code diffs; real-time token/cost monitoring with cancel capability; Git integration (PR summaries, code reviews, commit messages)."
---

jrdev targets developers who want a terminal agent that spends expensive models only where they pay off. The /init pass builds a project overview and convention profile that grounds later generations. Tasks flow through an intent router that parses natural-language commands and a code agent that picks models per tier — frontier models for planning and review, cheap ones for searches and fixes — with real-time token and cost readouts and a cancel switch. Diffs land in reviewable, editable form before application, and Git helpers cover PR summaries, reviews, and commit messages. It is early-access software, explicitly warning about breaking changes, distributed via pip under MIT.
