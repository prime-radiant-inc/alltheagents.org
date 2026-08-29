---
name: "stacklit"
slug: "stacklit"
layout: "agent.njk"
category: "other"
maker: "glincker"
license: "MIT"
url: "https://github.com/glincker/stacklit"
source_code_url: "https://github.com/glincker/stacklit"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-04-09"
current_release: "2026-05-07"
stars: "102"
language: "Go"
homepage: "https://www.npmjs.com/package/stacklit"
mcp_support: "True"
plugin_support: null
claude_code_plugin: "True"
subagents: null
hooks: "True"
plan_mode: null
model_providers: "Claude (optional --summary flag); otherwise runs locally with no LLM needed"
pricing: "Free / open source"
install_method: "npx stacklit init (recommended), npm install -g stacklit, go install ...@latest, or binary from GitHub Releases"
docs_url: "https://github.com/glincker/stacklit/blob/master/USAGE.md"
plugin_docs_url: null
config_docs_url: "https://github.com/glincker/stacklit/blob/master/USAGE.md"
download_url: "https://github.com/glincker/stacklit/releases"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "~250-token structured index vs 50k-500k full-dump approaches (Repomix, code2prompt); committable JSON + Merkle diagram; interactive HTML visual map (4 views); works with any AI tool that reads files; no server/setup required"
---

stacklit attacks the token cost of codebase orientation: where full-dump tools paste 50,000-500,000 tokens, it parses eleven languages with tree-sitter and writes a committable ~250-4,000 token index of modules, exports with signatures, dependencies, and hints such as where a feature belongs and what the test command is. A post-commit git hook regenerates the index using Merkle hashes to skip unchanged subtrees, taking roughly 50 ms on a 10k-line repo. stacklit serve exposes seven MCP tools that Claude Desktop and Cursor can call, and stacklit setup writes the navigation map into CLAUDE.md, .cursorrules, or aider config automatically. An optional --summary flag is the only network call; everything else runs locally. It targets teams whose agents waste context exploring rather than editing.
