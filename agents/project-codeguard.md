---
name: "project-codeguard"
slug: "project-codeguard"
layout: "agent.njk"
category: "other"
maker: "cosai-oasis"
license: "CC BY 4.0"
url: "https://github.com/cosai-oasis/project-codeguard"
source_code_url: "https://github.com/cosai-oasis/project-codeguard"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-01-22"
current_release: "2026-08-18"
stars: "313"
language: "Python, Markdown"
homepage: "https://project-codeguard.org/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "no"
plan_mode: "True"
model_providers: "Model-agnostic: Cursor, GitHub Copilot, Codex, Windsurf, Claude Code"
pricing: "Free/open-source (CC BY 4.0)"
install_method: "Download skills/rules from GitHub Releases; copy AI agent/IDE-specific skills and rules into your repository; start coding"
docs_url: "https://project-codeguard.org/getting-started/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/cosai-oasis/project-codeguard/releases"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Vendor-neutral, model-agnostic security coding agent skills framework from the Coalition for Secure AI (CoSAI, an OASIS Open Project). Ships unified security rules in markdown covering cryptography, input validation, authentication, authorization, supply chain, cloud security, and post-quantum cryptography; includes translators for popular coding agents, an MCP server for centralized organizational deployment, and validators to test compliance."
---

Project CodeGuard exists because security guidance for AI coding agents was fragmented across vendor-specific formats with no neutral governance. The Coalition for Secure AI, an OASIS-hosted industry consortium, publishes a single set of security rules in markdown spanning cryptography, injection, authentication and authorization, supply chain, cloud infrastructure, and data protection. A translation pipeline converts those unified sources into skills and rules for Cursor, Copilot, Codex, Windsurf, and Claude Code, so an organization writes its security posture once and every agent consumes the same content. Distribution works two ways: teams can copy released rules into their repositories as static context, or run the included MCP server so every developer's assistant pulls centrally managed rules over HTTP. Validators test rule compliance, and releases package everything as downloadable archives. Enterprises and open-source projects adopt it to get consistent, auditable security behavior from whatever agents their developers use.
