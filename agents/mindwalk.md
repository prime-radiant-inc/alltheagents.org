---
name: "mindwalk"
slug: "mindwalk"
layout: "agent.njk"
category: "other"
maker: "cosmtrek"
license: "MIT"
url: "https://github.com/cosmtrek/mindwalk"
source_code_url: "https://github.com/cosmtrek/mindwalk"
source_available: "True"
platforms: []
first_released: "2026-07-09"
current_release: "2026-08-10"
stars: "1261"
language: "Go"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic, OpenAI"
pricing: "open-source"
install_method: "binary"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "A visualization tool that replays coding-agent sessions on a 3D map of your codebase — draws the repo as a 'night map' and replays sessions as light moving through it (glowing where the agent searched/read/edited, dark elsewhere). Fully local; one Go binary reads Claude Code, Codex, and pi session logs. LLM-judge session evaluation with evidence-anchored findings, deterministic citymap layout, client-side video export."
---

mindwalk addresses the opacity of agent runs: after an agent spends an hour and a budget, the session log is the only record, and it is effectively unreadable. The tool builds a deterministic 3D map of the repository — height from lines of code, a 'night map' aesthetic — and replays sessions as light moving across it, with color separating observation from mutation and deleted files persisting as wireframe ghosts. Playback includes scrubbing, speed control, marks for compactions and subagent launches, subagent lenses for replaying nested traces, and client-side video export for postmortems. An inspector per file reconstructs visit history, and a HUD surfaces friction signals such as error rate, churn, and edits made after the last verification. An optional analyze command sends a session summary through the user's own claude or codex CLI for judge scoring; everything else stays fully local. Teams reviewing agent behavior, auditing spent budgets, or teaching agent mechanics use it as a replay instrument rather than a coding tool.
