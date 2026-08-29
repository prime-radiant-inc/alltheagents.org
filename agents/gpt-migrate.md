---
name: "GPT Migrate"
slug: "gpt-migrate"
layout: "agent.njk"
category: "agent"
maker: "joshpxyne"
license: "MIT"
url: "https://github.com/0xpayne/gpt-migrate"
source_code_url: "https://github.com/0xpayne/gpt-migrate"
source_available: "True"
platforms: []
first_released: "2023-06-24"
current_release: "2024-09-17"
stars: "6979"
language: "Python"
homepage: "https://gpt-migrate.com"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenRouter, OpenAI"
pricing: "BYOK"
install_method: "pip"
docs_url: "https://gpt-migrate.com/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/joshpxyne/gpt-migrate"
maintained: "active"
sources:
  - "e2b"
what_makes_it_special: "Automated full-codebase migration across languages/frameworks using LLMs. Spins up a Docker environment for the target language, recursively rebuilds code from a source entry file, iteratively debugs using logs/errors/context, generates and validates unit tests. Hierarchical prompt design system (p1-p4 preference levels). Currently development alpha."
---

GPT Migrate attacks the problem most coding assistants avoid: porting an entire codebase from one language or framework to another, such as Flask to Node.js. It stands up a Docker environment for the destination language, recursively rebuilds the application outward from a source entry file, generates unit tests, and iteratively debugs the rewritten code against them using error logs and context. A hierarchical prompt system (p1 through p4 preference levels) organizes instructions, and OpenAI or OpenRouter keys drive the model calls. It is MIT-licensed but explicitly a development alpha with high token costs for full-codebase rewrites; with 75 commits and no releases since 2024, it remains a well-known alpha rather than a maintained tool.
