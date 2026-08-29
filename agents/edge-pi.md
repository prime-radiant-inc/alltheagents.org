---
name: "edge-pi"
slug: "edge-pi"
layout: "agent.njk"
category: "agent"
maker: "marcusschiesser"
license: "MIT"
url: "https://github.com/marcusschiesser/edge-pi"
source_code_url: "https://github.com/marcusschiesser/edge-pi"
source_available: "True"
platforms: []
first_released: "2026-02-01"
current_release: "2026-02-23"
stars: "62"
language: "TypeScript"
homepage: "https://edge-pi-beta.vercel.app/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Multi-provider via Vercel AI SDK"
pricing: "open-source"
install_method: "npm install -g edge-pi-cli"
docs_url: "https://edge-pi-beta.vercel.app/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/edge-pi-cli"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Lightweight Vercel AI SDK-based coding agent library providing core primitives for building AI-powered coding assistants with tool support, session management, and context compaction; includes epi CLI as a full-featured coding agent with multi-provider support and skills"
---

Building a coding assistant on the Claude Agent SDK locks the loop to Anthropic's runtime, and the Vercel AI SDK alone leaves you to write session handling, tool plumbing, and context compaction yourself. edge-pi supplies exactly those missing primitives on top of the Vercel AI SDK: tool execution, session management, and compaction, usable with any LLM provider. Its epi CLI is a compact, working agent — multi-provider, skills-aware — included to show the library end to end; the code descends from Mario Zechner's pi coding agent. It is aimed at developers who want an embeddable, provider-neutral agent kernel rather than a finished product.
