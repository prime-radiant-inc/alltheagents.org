---
name: "harness-engineering-from-cc-to-ai-coding"
slug: "harness-engineering-from-cc-to-ai-coding"
layout: "agent.njk"
category: "other"
maker: "ZhangHanDong"
license: "MIT"
url: "https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding"
source_code_url: "https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding"
source_available: "True"
platforms: []
first_released: "2026-04-01"
current_release: "2026-04-10"
stars: "1488"
language: "Chinese (Markdown book)"
homepage: "https://zhanghandong.github.io/harness-engineering-from-cc-to-ai-coding/"
mcp_support: "n/a - covered as a book topic, not a feature"
plugin_support: "n/a"
claude_code_plugin: "n/a - has .claude/skills/skillify directory"
subagents: "n/a - book covers multi-agent orchestration"
hooks: "n/a - covered as a book topic"
plan_mode: "n/a"
model_providers: "none"
pricing: "free"
install_method: "Read online (mdBook on GitHub Pages); MIT-licensed source in the repo"
docs_url: "https://zhanghandong.github.io/harness-engineering-from-cc-to-ai-coding/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic5"
what_makes_it_special: "Chinese technical book ('Harness Engineering: From Claude Code Source Code to AI Coding Best Practices', nicknamed 'the horse book') that reverse-engineers Claude Code v2.1.88 via source maps to extract architecture patterns, context strategies, permission systems, and production practices for AI coding agents. Covers agent loop architecture, tool execution orchestration, auto/micro-compression, token budgets, prompt cache, permission modes, YOLO classifier, hooks, skill systems, feature flags, and unpublished capability pipelines - translating them into reusable patterns. English translation in progress."
---

This project is an open-source technical book, written in Chinese, that dissects Claude Code's architecture from its shipped artifacts. Using the public npm package and embedded source maps, the author reconstructed Claude Code v2.1.88's source and organized the findings into seven parts covering the agent loop and tool orchestration, system and tool prompts, context management with auto- and micro-compaction, prompt caching, the permission and security rule system including the YOLO classifier and hooks, and advanced subsystems such as multi-agent orchestration and the skills system, closing with lessons for agent builders. The book is built with mdBook and published on GitHub Pages, with an English translation in progress. It serves engineers studying production agent design rather than anyone running a coding tool, and the author notes it reflects reverse-engineering rather than Anthropic's official position.
