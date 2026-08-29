---
name: "TeamHero"
slug: "teamhero"
layout: "agent.njk"
category: "multiplexer"
maker: "sagiyaacoby"
license: "MIT"
url: "https://github.com/sagiyaacoby/TeamHero"
source_code_url: "https://github.com/sagiyaacoby/TeamHero"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-03-15"
current_release: "2026-04-03"
stars: "35"
language: "JavaScript, Node.js"
homepage: null
mcp_support: "yes"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "yes"
hooks: "no"
plan_mode: "True"
model_providers: "Claude CLI (Anthropic)"
pricing: "Free / open-source (MIT)"
install_method: "Prerequisite: npm install -g @anthropic-ai/claude-code. Then: git clone https://github.com/sagiyaacoby/TeamHero.git my-team; cd my-team; npm install; launch via launch.bat (Windows) or bash launch.sh (Mac/Linux); dashboard opens at http://localhost:3777"
docs_url: "https://github.com/sagiyaacoby/TeamHero"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/sagiyaacoby/TeamHero"
maintained: "active"
sources:
  - "jim"
  - "caramaschi"
what_makes_it_special: "Self-hosted structured AI agent orchestration platform that manages agents like a real team with project-management discipline: every task goes through plan -> review -> execute -> deliver; persistent short/long-term agent memory across sessions; file-scope declarations prevent agents from overwriting each other's work; knowledge base promotes deliverables into a searchable library; dashboard web UI plus integrated Command Center terminal; optional Skills integrations (browser automation, GitHub). Requires Claude Code CLI."
---

TeamHero is the self-hosted, MIT-licensed core of the Kapow managed-agent platform, built on the premise that parallel coding agents fail without management structure. It runs Claude Code as the execution engine and adds an orchestration layer: an orchestrator agent directs the team via a Command Center terminal, every task must produce a plan that is reviewed before any code executes, and finished deliverables are versioned and promoted into a knowledge base for retrieval by later tasks. Coordination hazards are addressed structurally — agents declare file scopes so two workers cannot overwrite the same file, and per-agent short- and long-term memory persists across sessions — while optional skills add browser automation and GitHub integration. A web dashboard at localhost:3777 exposes the whole operation. Solo developers and small teams already paying for Claude Code who want supervised, structured multi-agent execution rather than ad-hoc parallel sessions are the target users.
