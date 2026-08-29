---
name: "Flare"
slug: "flare"
layout: "agent.njk"
category: "other"
maker: "AlgoNoRhythm"
license: "MIT"
url: "https://github.com/AlgoNoRhythm/Flare"
source_code_url: "https://github.com/AlgoNoRhythm/Flare"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-08-02"
current_release: "2026-08-16"
stars: "112"
language: "TypeScript"
homepage: "https://github.com/AlgoNoRhythm/Flare"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: null
model_providers: "Claude,Codex,OpenCode,Aider"
pricing: "Free/open-source (MIT)"
install_method: "Dev from source: npm install, npm run build, npm start (Node 20+); or download prebuilt installers from GitHub releases; or npm run serve for browser mode"
docs_url: "https://github.com/AlgoNoRhythm/Flare"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/AlgoNoRhythm/Flare/releases"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Graph-first IDE for agentic coding with live dependency graph (files as nodes, imports as edges); built-in MCP server on localhost exposing graph/file/dependency/impact tools; shadow history (separate git repo auto-commits every change burst for one-click undo); 10 lenses recolor graph by Clusters/Activity/Hotspots/Risk/Tests/Coverage/Instability/Reuse/Unread/Cycles; agent-aware review cockpit classifies files by review priority and detects 'agent smells'; comprehension debt tracking via 'Unread' lens; multi-agent board with cross-agent tracking; adds Stop hook to .claude/settings.local.json to keep agents working."
---

Flare rethinks the IDE around the reality that agents, not humans, now write much of the code: its main surface is a live dependency graph of files and imports, with switchable lenses (Activity, Hotspots, Risk, Cycles, Coverage, Unread) over three view geometries. A built-in MCP server on localhost exposes graph tools — impact_of, dependents, verification_status, record_intent — so agents consult structure before editing, while process-tree watching attributes every file change to the specific agent that made it. A review cockpit groups changes into bursts with risk tiers and agent 'smells' detection, shadow history auto-commits each burst to a hidden git repo for rollback, and a kanban board holds tasks and decisions designed for handoff to agents. Developers running multiple agents against one codebase use it to keep oversight without reading every diff.
