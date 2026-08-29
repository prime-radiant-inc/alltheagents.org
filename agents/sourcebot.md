---
name: "sourcebot"
slug: "sourcebot"
layout: "agent.njk"
category: "other"
maker: "sourcebot-dev"
license: "Fair-source (see LICENSE.md)"
url: "https://github.com/sourcebot-dev/sourcebot"
source_code_url: "https://github.com/sourcebot-dev/sourcebot"
source_available: "True"
platforms: []
first_released: "2024-08-23"
current_release: "2026-08-20"
stars: "3893"
language: "TypeScript"
homepage: "https://sourcebot.dev"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "docker"
docs_url: "https://docs.sourcebot.dev"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Self-hosted code intelligence platform that helps humans and agents understand codebases. Combines AI-powered Q&A with inline citations, code search (regex/filters/boolean across all repos/branches on any code host), IDE-level cross-repo goto definition and find references, and a built-in file explorer. Enables both humans and AI agents to navigate large multi-repo codebases. Public demo at app.sourcebot.dev."
---

Sourcebot addresses the cost of understanding large multi-repo codebases, for engineers and increasingly for the agents working alongside them. A Docker Compose deployment indexes all repos and branches on any code host, then serves fast regex and boolean search, IDE-grade cross-repo go-to-definition and find-references, a file explorer, and a natural-language Q&A mode whose answers cite specific code with navigable snippets. Configuration is a JSON file describing code hosts, LLM providers, and auth; the enterprise directory carries additional paid capabilities under a Fair Source license. A public demo runs at app.sourcebot.dev, and the project releases frequently (v5.1.x as of August 2026). Teams with sprawling monorepo estates use it as shared infrastructure for humans and AI tools alike.
