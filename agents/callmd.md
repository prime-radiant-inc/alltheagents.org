---
name: "call.md"
slug: "callmd"
layout: "agent.njk"
category: "other"
maker: "video-db"
license: "MIT"
url: "https://github.com/video-db/call.md"
source_code_url: "https://github.com/video-db/call.md"
source_available: "True"
platforms: []
first_released: "2026-02-25"
current_release: "2026-08-19"
stars: "1121"
language: "TypeScript"
homepage: "https://docs.videodb.io/examples-and-tutorials/ai-copilots/call-md"
mcp_support: "yes (stdio, HTTP)"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "VideoDB (OpenAI-compatible API)"
pricing: "open-source"
install_method: "binary"
docs_url: "https://docs.videodb.io"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Turns meetings into live agent loops: records, dual-channel transcribes, and analyzes meetings with real-time AI intelligence. MCP auto-triggering detects information needs from conversation context and calls tools automatically during calls. Local-first SQLite storage with encrypted credentials, AI coaching nudges during calls, and post-meeting summaries with workflow webhook export."
---

call.md, built by VideoDB, addresses the gap between what gets said in a meeting and the information you need while it is happening. The desktop app records dual-channel audio (local mic plus system audio), transcribes in real time through VideoDB, and runs an intelligence layer that computes conversation metrics, delivers live coaching nudges, and — its distinguishing mechanic — auto-triggers MCP tools when the detected conversational intent calls for them, surfacing results inline during the call. Meetings are stored locally in SQLite with encrypted credentials, and post-meeting summaries, action items, and webhook exports (n8n, Zapier, CRMs) close the loop. It is distributed as an installable desktop app (macOS first, with Windows and Linux support varying by feature) and is open source under MIT. Sales, success, and recruiting teams use it for live call assistance and automated post-meeting follow-up rather than as a coding tool.
