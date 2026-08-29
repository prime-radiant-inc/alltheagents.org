---
name: "arc-kit"
slug: "arc-kit"
layout: "agent.njk"
category: "agent"
maker: "tractorjuice"
license: "MIT"
url: "https://github.com/tractorjuice/arc-kit"
source_code_url: "https://github.com/tractorjuice/arc-kit"
source_available: "Yes"
platforms: []
first_released: "2025-10-14"
current_release: "2026-08-19"
stars: "2192"
language: "Python"
homepage: "https://arckit.org/"
mcp_support: "yes (bundles 6 MCP servers: AWS Knowledge, Microsoft Learn, Google Developer Knowledge, GovRepoScrape, uk-tenders, plus diagnostics)"
plugin_support: "yes"
claude_code_plugin: "yes"
subagents: "yes"
hooks: "yes"
plan_mode: "yes"
model_providers: "Claude Code, Gemini CLI, GitHub Copilot, OpenAI Codex CLI, OpenCode CLI, Mistral Vibe CLI, Kimi Code CLI"
pricing: "open-source"
install_method: "pip"
docs_url: "https://github.com/tractorjuice/arc-kit/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/tractorjuice/arc-kit"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Enterprise architecture governance harness that transforms scattered architecture documents into systematic AI-assisted workflows covering the full lifecycle: principles, stakeholders, risk, business case, requirements, data modeling, research, procurement, design review, and compliance, with specialized compliance overlays for UK Government, EU, France, Netherlands, Austria, Canada, UAE, USA, and NHS clinical safety."
---

Enterprise architecture work is usually scattered across Word documents, Confluence pages, and slide decks with no systematic workflow, and arc-kit exists to give that material the same harness treatment coding gets. It installs as a Claude Code plugin (with Gemini, Copilot, Codex, OpenCode, Mistral, and Kimi CLI support) providing slash commands such as /arckit:principles and /arckit:requirements, 29 agent descriptors, 9 hooks, and 6 bundled MCP servers (AWS Knowledge, Microsoft Learn, Google Developer Knowledge, govreposcrape, uk-tenders). Commands map to a phase-by-phase lifecycle: principles, stakeholders, risk registers, Green Book business cases, requirements, research, procurement, design review, and compliance packs for UK, EU, NHS, and other jurisdictions. Artifacts stay under Git version control and are explicitly labeled as drafts for qualified review. It targets enterprise and government architects, with the UK MOD and public-sector compliance packs as its most distinctive deployments.
