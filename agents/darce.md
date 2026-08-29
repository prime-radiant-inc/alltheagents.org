---
name: "Darce"
slug: "darce"
layout: "agent.njk"
category: "agent"
maker: "AmerSarhan"
license: "MIT"
url: "https://github.com/AmerSarhan/darce-cli"
source_code_url: "https://github.com/AmerSarhan/darce-cli"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-03-31"
current_release: "2026-04-01"
stars: "9"
language: "TypeScript"
homepage: "https://cli.darce.dev"
mcp_support: "no"
plugin_support: null
claude_code_plugin: null
subagents: "no"
hooks: null
plan_mode: "no"
model_providers: "qwen, x-ai (Grok), anthropic (Claude), google (Gemini), deepseek, meta-llama"
pricing: "Free (25 req/mo); Builder $15/mo (500 req); Power $65/mo (2,500 req)"
install_method: "npm install -g darce-cli"
docs_url: "https://cli.darce.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/darce-cli"
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Terminal-based AI coding agent — 14 kB package, 3-second install, smart model routing/switching, works in any terminal, supports any model. Reads, writes, edits code, runs shell commands, and searches codebases. Free tier available."
---

Darce exists to strip a terminal coding agent down to the smallest practical footprint: a 14 kB TypeScript package that installs in seconds and ships seven tools (Read, Write, Edit, Bash, Glob, Grep, WebFetch) rather than the sprawling feature sets of Claude Code-class harnesses. Requests route through a hosted API to models including Qwen3 Coder, Grok, Claude Sonnet, Gemini, DeepSeek, and Llama 4, with free and paid request quotas, and the CLI adds session resume, context compaction, and cost tracking on top. The target user is someone on constrained hardware or bandwidth who wants basic agentic editing without a large install. Development has stalled — 15 commits, no releases, and a comparison table whose 'open source' claim the repo does not clearly support — so it functions best as a minimalist reference.
