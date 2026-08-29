---
name: "real-world-rails"
slug: "real-world-rails"
layout: "agent.njk"
category: "other"
maker: "steveclarke"
license: "MIT"
url: "https://github.com/steveclarke/real-world-rails"
source_code_url: "https://github.com/steveclarke/real-world-rails"
source_available: "True"
platforms: []
first_released: "2026-02-23"
current_release: "2026-08-17"
stars: "537"
language: "Ruby"
homepage: null
mcp_support: "no"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "git clone ... && cd real-world-rails && bin/setup (requires git-lfs); agent skill: npx skills add steveclarke/real-world-rails"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/steveclarke/real-world-rails"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Aggregates 200+ production open source Rails apps and engines as git submodules in one repo, enabling AI coding agents to search and cross-reference real-world codebases to research architectural patterns (multi-tenancy, auth, background jobs, soft deletes, etc.)."
---

Real World Rails aggregates more than two hundred open-source, production-grade Rails applications and engines as git submodules in a single repository, giving an AI coding agent — or a human — a corpus of real architectural decisions to search across. A companion agent skill, installable through the skills CLI, teaches an agent how to navigate the corpus and answer cross-cutting questions: how different apps handle multi-tenancy, background job retries, soft deletes, or authorization. The collection descends from a pre-AI-era resource for learning Rails by reading production code, reframed here for agentic research with a weekly GitHub Action keeping submodules current. Inclusion criteria require open-source licensing, real-world provenance rather than tutorials, and active maintenance. Rails developers and anyone building AI coding tools use it as reference material that grounds agent answers in real codebase patterns rather than generic advice.
