---
name: "swift-coding-agent"
slug: "swift-coding-agent"
layout: "agent.njk"
category: "agent"
maker: "ivan-magda"
license: "MIT"
url: "https://github.com/ivan-magda/swift-coding-agent"
source_code_url: "https://github.com/ivan-magda/swift-coding-agent"
source_available: True
platforms: []
first_released: "2026-03-10"
current_release: "2026-06-26"
stars: "178"
language: "Swift"
homepage: "https://ivanmagda.dev/posts/s00-bootstrapping-the-project/"
mcp_support: False
plugin_support: False
claude_code_plugin: False
subagents: True
hooks: False
plan_mode: False
model_providers: "Anthropic"
pricing: "Free / open source (MIT); bring your own Anthropic API key"
install_method: "git clone, cp .env.example .env (set ANTHROPIC_API_KEY and MODEL_ID), swift build, swift run agent"
docs_url: "https://github.com/ivan-magda/swift-coding-agent#readme"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Swift reimplementation of a Claude Code-style coding agent CLI built stage-by-stage to explore coding-agent architecture. Philosophy: coding agents benefit more from a small set of excellent tools and a tight loop than from large orchestration layers. The agent loop is fixed and minimal (~15 lines); each roadmap stage isolates one mechanism (subagents, context compaction, task DAGs, background tasks). Built with Swift 6.2 strict concurrency. Runs on macOS and Linux with no IDE dependency."
---

Swift reimplementation of a Claude Code-style coding agent CLI built stage-by-stage to explore coding-agent architecture. Philosophy: coding agents benefit more from a small set of excellent tools and a tight loop than from large orchestration layers. The agent loop is fixed and minimal (~15 lines); each roadmap stage isolates one mechanism (subagents, context compaction, task DAGs, background tasks). Built with Swift 6.2 strict concurrency. Runs on macOS and Linux with no IDE dependency.
