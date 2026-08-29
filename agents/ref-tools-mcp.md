---
name: "ref-tools-mcp"
slug: "ref-tools-mcp"
layout: "agent.njk"
category: "other"
maker: "ref-tools"
license: "MIT"
url: "https://github.com/ref-tools/ref-tools-mcp"
source_code_url: "https://github.com/ref-tools/ref-tools-mcp"
source_available: "True"
platforms: []
first_released: "2025-04-22"
current_release: "2026-06-26"
stars: "1154"
language: "TypeScript"
homepage: "http://ref.tools"
mcp_support: "yes (Streamable-HTTP recommended, stdio legacy)"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "freemium"
install_method: "npm"
docs_url: "https://ref.tools"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/ref-tools-mcp"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Token-efficient agentic documentation search MCP server. Reduces 'context rot' by filtering repeated results within sessions and returning only the ~5k most relevant tokens per page based on search history. Supports both public web/GitHub docs and private repos/PDFs. Includes OpenAI deep research compatibility. Works with Claude Code, Cursor, and OpenAI deep research."
---

Documentation lookups are one of the fastest ways a coding agent burns its context window: a naive page fetch returns 20k+ tokens of boilerplate, and repeated searches echo the same results. Ref's MCP server attacks this with session-aware search that filters duplicates across a session's history and returns only about five thousand of the most relevant tokens per page, calibrated to what the agent's search trajectory suggests it needs. It exposes just two tools — search documentation and read a URL — with a hosted HTTP endpoint as the recommended deployment and a legacy stdio server in this repository. Public web and GitHub documentation can be blended with private sources like internal repos and PDFs, and the tools map onto OpenAI deep research's search/fetch contract. Developers wiring Claude Code, Cursor, or other MCP clients use it to keep doc research cheap and precise.
