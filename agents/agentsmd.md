---
name: "agents.md"
slug: "agentsmd"
layout: "agent.njk"
category: "other"
maker: "agentsmd"
license: "MIT"
url: "https://github.com/agentsmd/agents.md"
source_code_url: "https://github.com/agentsmd/agents.md"
source_available: "Yes"
platforms: []
first_released: "2025-08-19"
current_release: "2026-03-12"
stars: "23732"
language: "TypeScript"
homepage: "https://agents.md"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Provider-agnostic (open format for any coding agents)"
pricing: "open-source"
install_method: "npm (for local Next.js website)"
docs_url: "https://agents.md/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/agentsmd/agents.md"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Acts as a 'README for agents' -- a dedicated, predictable file format designed to provide context, environment tips, testing instructions, and PR rules to help guide AI coding agents working within a project."
---

As coding agents spread, every tool proposed its own instruction file, leaving repositories with fragmented per-tool configuration. AGENTS.md defines a predictable, plain-Markdown convention: a single file where a project documents environment setup, testing commands, and pull-request rules, with no schema or tooling required. The repository hosts both the specification and the agents.md website, and dogfoods the format with its own AGENTS.md. Adoption spread across major tools and thousands of repositories, making it the reference point against which alternatives like AGENT.md position themselves. Its audience is any team whose repositories are worked on by AI coding agents.
