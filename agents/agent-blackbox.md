---
name: "Agent-Blackbox"
slug: "agent-blackbox"
layout: "agent.njk"
category: "other"
maker: "TaewoooPark"
license: "MIT"
url: "https://github.com/TaewoooPark/Agent-Blackbox"
source_code_url: "https://github.com/TaewoooPark/Agent-Blackbox"
source_available: "True"
platforms: []
first_released: "2026-06-16"
current_release: "2026-07-26"
stars: "72"
language: "TypeScript"
homepage: "https://www.npmjs.com/package/@taewooopark/agent-blackbox"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "no"
model_providers: "Ollama, OpenAI-compatible"
pricing: "Free (open source, MIT, no API key required)"
install_method: "npx @taewooopark/agent-blackbox up --host claude-code (or codex, or all); or git clone + npm install + npm run build:cli"
docs_url: "https://github.com/TaewoooPark/Agent-Blackbox/blob/main/docs/analysis.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@taewooopark/agent-blackbox"
maintained: "active"
sources:
  - "github_topic5"
what_makes_it_special: "Local-first flight recorder and context-efficiency profiler for coding agents that turns every agent run into a live, replayable operational graph reconstructed from observed events (not agent self-summary). Scores runs on 11 context-efficiency metrics with task-tailored scoring, can write fixes back to CLAUDE.md/AGENTS.md, and offers an in-run optimizer cutting ~94-96% of re-read tokens. Host-agnostic (Claude Code, Codex, OpenCode)."
---

When a coding agent wastes half its context re-reading files or repeating failed approaches, nothing in the transcript explains the pattern, so Agent-Blackbox records runs externally and reconstructs what actually happened from observed events — files read, edits, commands, subagent delegations. Each run gets scored on eleven context-efficiency metrics plus outcome, and the tool can write a reversible memory block into CLAUDE.md or AGENTS.md so future runs avoid the same waste; an in-run optimizer trims redundant reads by roughly 94–96%. It runs via npx against Claude Code, Codex, or OpenCode sessions, needs no API key, and keeps everything local. Developers tuning agent cost and reliability use it as a profiler rather than a harness.
