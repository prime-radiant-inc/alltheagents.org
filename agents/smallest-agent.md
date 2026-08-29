---
name: "Smallest Agent"
slug: "smallest-agent"
layout: "agent.njk"
category: "agent"
maker: "obra"
license: null
url: "https://github.com/obra/smallest-agent"
source_code_url: "https://github.com/obra/smallest-agent"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-06-14"
current_release: "2026-03-02"
stars: "121"
language: "JavaScript"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: null
model_providers: null
pricing: "Free (no license specified)"
install_method: "git clone and npm install; run npm test for the API smoke test (no published package)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/obra/smallest-agent"
maintained: "active"
sources:
  - "author_search"
what_makes_it_special: "Minimalism challenge coding agent golfed down to just 493 bytes (src/smallest-agent.js); functional coding agent with unrestricted bash access; commented readable version at src/smallest-agent.commented.js; created as a demonstration of how small a Claude Code-like agent can be"
---

The project is a demonstration built to answer how little code a functional agent needs. Jesse Vincent wrote a first draft comparable in behavior to Claude Code, then used the agent itself to golf its own source down to a few hundred bytes, documenting the process in HACKING-TRANSCRIPT.md. The minified loop calls a hosted LLM API and gives the model unrestricted bash, which the README flags in capital letters as capable of destructive actions; a commented companion file and an npm smoke test make the mechanics studyable. There is no MCP, plugin, hook, or subagent machinery by design. Its audience is developers studying the minimal anatomy of an agent loop, not teams shipping software.
