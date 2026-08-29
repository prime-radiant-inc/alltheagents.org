---
name: "AgentsMesh"
slug: "agentsmesh"
layout: "agent.njk"
category: "multiplexer"
maker: "AgentsMesh"
license: "BSL-1.1"
url: "https://github.com/AgentsMesh/AgentsMesh"
source_code_url: "https://github.com/AgentsMesh/AgentsMesh"
source_available: "Source-visible (no OSS license)"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-02-28"
current_release: "2026-08-03"
stars: "2324"
language: "Go"
homepage: "https://agentsmesh.ai"
mcp_support: "partial (.mcp.json and mcp-e2e tests present in repo; not detailed in README)"
plugin_support: null
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic, OpenAI, Google, BYOK, local"
pricing: "BYOK"
install_method: "binary"
docs_url: "https://agentsmesh.ai/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "AI agent workforce platform that runs a hundred self-hosted coding agents across your own machines with workspace isolation (git worktree pods), autopilot self-healing, mesh channels, and a single console (web/desktop/iOS)."
---

One operator can meaningfully supervise only a couple of coding agents before workspace collisions, stalled runs, and credential management take over. AgentsMesh addresses this with AgentPods — isolated execution environments pairing a PTY terminal with a dedicated git worktree and private credentials — scheduled across self-hosted runner daemons so code never leaves the operator's infrastructure. An autopilot control agent watches each pod, sends the next instruction on idle with iteration caps, and hands control back to a human on request, while mesh channels and tickets bind pods into a collaborating, human-visible topology. The stack splits an orchestration control plane (gRPC/mTLS) from a stateless terminal relay, with a shared Rust core powering web, Electron desktop, and SwiftUI iOS clients. Supported agents include Claude Code, Codex CLI, Gemini CLI, Aider, and OpenCode on a BYOK basis, licensed as BSL-1.1 with production use requiring a commercial license until the 2030 conversion to GPL.
