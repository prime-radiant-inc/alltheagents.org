---
name: "context-hub"
slug: "context-hub"
layout: "agent.njk"
category: "other"
maker: "andrewyng"
license: "MIT"
url: "https://github.com/andrewyng/context-hub"
source_code_url: "https://github.com/andrewyng/context-hub"
source_available: "Yes"
platforms: []
first_released: "2025-10-30"
current_release: "2026-05-31"
stars: "13929"
language: "JavaScript"
homepage: null
mcp_support: "no"
plugin_support: "yes (agent skills via SKILL.md files)"
claude_code_plugin: "yes (drop SKILL.md into ~/.claude/skills/)"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "None (a CLI serving markdown documentation; no model inference)"
pricing: "open-source (MIT)"
install_method: "npm"
docs_url: "https://github.com/andrewyng/context-hub/blob/main/docs/cli-reference.md"
plugin_docs_url: "https://github.com/andrewyng/context-hub/blob/main/cli/skills/get-api-docs/SKILL.md"
config_docs_url: null
download_url: "https://www.npmjs.com/package/@aisuite/chub"
maintained: "active"
sources:
  - "namphuong"
what_makes_it_special: "Provides curated, versioned API documentation as open markdown that coding agents can fetch via CLI, reducing API hallucinations. Enables self-improving agents through local annotations that persist across sessions and community feedback (up/down ratings) that flows back to doc authors."
---

Coding agents hallucinate APIs because their training data lags current library versions, and pasting entire documentation sites into context wastes tokens. Context Hub maintains curated, versioned API documentation as plain markdown in a git repository: an agent searches the catalog, fetches exactly the pages needed for its language and version, and writes correct calls against current APIs. Two feedback mechanisms make the corpus self-improving - agents leave local annotations that persist across sessions and are re-injected into later fetches, and users vote pages up or down so authors see which content needs fixing. Installation is a global npm package, and a SKILL.md lets Claude Code load it as a skill. Developers wiring agents to third-party APIs are the users, and the corpus grows through community pull requests.
