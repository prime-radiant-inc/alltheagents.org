---
name: "Browserbase"
slug: "browserbase"
layout: "agent.njk"
category: "other"
maker: null
license: "Proprietary (Stagehand SDK and CLI are open source)"
url: "https://twitter.com/browserbasehq"
source_code_url: null
source_available: "No (proprietary)"
platforms:
  - "Web"
  - "Autonomous"
first_released: null
current_release: null
stars: null
language: null
homepage: "https://www.browserbase.com"
mcp_support: "yes (Browserbase MCP server for Claude and other agents)"
plugin_support: "no"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "usage"
install_method: null
docs_url: "https://docs.browserbase.com"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Associated link: the Twitter/X account for Browserbase (twitter.com/browserbasehq), a cloud browser infrastructure provider; not a standalone coding agent harness"
---

Browserbase sells browser infrastructure: on-demand, isolated browser sessions in the cloud that agents and automations can drive, alongside SDKs (the open-source Stagehand framework), a Fetch API for URL-to-markdown extraction, session replays for observability, and identity management for authenticated flows. Coding agents consume it as a tool — a Browserbase MCP server lets Claude Code or similar harnesses call live web browsing as a tool, and templates exist specifically for wiring Claude Code to the service — but Browserbase itself performs no coding and has no agent loop of its own. Its customers are AI product teams and agent developers (Anthropic, Vercel, and thousands of others) who need reliable web access at scale without managing browser fleets. The entry sits in the census as ecosystem infrastructure rather than a harness, which is why the category is 'other'.
