---
name: "conch"
slug: "conch"
layout: "agent.njk"
category: "agent"
maker: "Crustocean"
license: "MIT"
url: "https://github.com/Crustocean/conch"
source_code_url: "https://github.com/Crustocean/conch"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-03-05"
current_release: "2026-03-05"
stars: "34"
language: "JavaScript, Node.js (>= 18)"
homepage: "https://crustocean.chat/profile/conch"
mcp_support: "no"
plugin_support: null
claude_code_plugin: "False"
subagents: "False"
hooks: null
plan_mode: null
model_providers: "Anthropic (Claude) - any Anthropic model with tool-use support, configurable via CONCH_MODEL"
pricing: "Free / open-source (MIT, self-hosted)"
install_method: "Create agent on Crustocean via /agency create, /boot conch, /agent verify conch; cp .env.example .env and set CRUSTOCEAN_API_URL, CONCH_AGENT_TOKEN, ANTHROPIC_API_KEY; ensure @crustocean/sdk available; npm install && npm start; connect a repo with !conch connect owner/repo; deploy via Railway (railway up), Docker, or any Node.js host"
docs_url: "https://docs.crustocean.chat"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Crustocean/conch"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Cloud coding agent steered from the Crustocean chat platform that reads GitHub repos, writes patches, and opens PRs; stateless worker with no database, filesystem, or ports - connects via WebSocket to Crustocean and REST API to GitHub; in-memory staged writes via a Map (nothing touches GitHub until commit()) for ephemeral per-run changes; atomic commits via the Git Data API (blobs, trees, commits, ref updates) to avoid merge conflicts from concurrent operations; permission gates on destructive operations (PR create/merge, branch delete); security hardening (path traversal validation, 2 MB write cap, main/master branch deletion blocked); demo mode with a known bug for showcasing the workflow. Very early stage (3 commits, 34 stars)."
---

Chat platforms want coding agents their users can summon without running infrastructure, and Conch is Crustocean's reference implementation of that pattern. The Node.js worker joins Crustocean over WebSocket, reads a connected GitHub repository through the REST API, and drives Claude's tool-calling loop to explore code and build patches; every write stays in memory until an explicit commit step assembles blobs, a tree, and a ref update atomically at PR creation. Permission gates require explicit approval before pull requests are created or merged, default branches are hard-blocked from deletion, and file writes are path-validated and size-capped. Runs appear in Crustocean as timelines of tool cards and status banners. Users deploy it on Railway, Docker, or any Node host and extend it by editing a single tool-definitions file.
