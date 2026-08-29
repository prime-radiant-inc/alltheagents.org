---
name: "Greptile"
slug: "greptile"
layout: "agent.njk"
category: "agent"
maker: null
license: "Proprietary"
url: "https://greptile.com"
source_code_url: null
source_available: "False"
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: "https://greptile.com"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "BYOK (bring your own LLM when self-hosted)"
pricing: "Starter free (1 dev, 50 credits/mo); Pro $30/seat/mo (50 credits/seat); extra credits $1 each (1 credit = 1 standard review, 3 credits = 1 TREX review)"
install_method: "Sign up at app.greptile.com; GitHub/GitLab integration; also via CLI and Claude Code plugin"
docs_url: "https://www.greptile.com/docs/introduction"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "vinkius"
what_makes_it_special: "Graph index of entire codebase; swarm of parallel agents reviewing beyond the diff; learns team coding standards from PR comments over time; TREX autonomously writes and runs tests per PR; central validation layer across all coding agents; Greptile MCP connects to any AI agent."
---

Greptile is a hosted code-review platform that indexes a repository as a graph of files, functions, and dependencies, then runs parallel review agents over every pull request with that full-repo context rather than the diff alone, which lets it catch multi-file logic regressions that diff-only reviewers miss. Beyond review, its TREX agent writes and runs tests for each PR in a sandbox, and the platform accumulates team coding standards from PR comments and plain-English custom rules over time. It integrates as a validation layer for whichever agent produced the change: an MCP server, a Claude Code plugin that reads and resolves comments, a /greploop command that lets Claude Code, Cursor, Codex, or Devin iterate with Greptile until issues clear, and a CLI. It is delivered as SaaS with self-hosting for enterprises, used by over 22,000 teams including Brex, NVIDIA, PostHog, and Zapier.
