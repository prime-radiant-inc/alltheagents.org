---
name: "Agent 37"
slug: "agent37"
layout: "agent.njk"
category: "multiplexer"
maker: "agent37"
license: "Proprietary"
url: "https://agent37.com"
source_code_url: null
source_available: "False"
homepage: null
docs_url: "https://agent37.com/docs"
download_url: null
install_method: "Hosted service — sign up at agent37.com (dashboard); REST API with X-Agent37-Key. No install"
platforms:
  - "Web"
  - "Autonomous"
autonomy_level:
  - "autonomous-background"
specialization: "general"
language: null
first_released: "2025-12-29"
current_release: null
maintained: "active"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "Hosts coding-agent harnesses in its sandboxes — templates for Hermes, OpenClaw, Claude Code, Codex, Grok, OpenCode, Pi, or bring your own Docker image; agents bring their own providers, and managed model access or BYOK is metered separately"
pricing: "usage"
stars: null
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "YC-backed sandbox hosting that bills agent compute by the minute at roughly a tenth of typical sandbox providers — prepaid metered vCPU/memory/disk with billing paused on auto-sleep — and runs persistent gVisor-isolated Linux sandboxes or full VMs (Docker-in-Docker, Android emulator) with an open Gateway API exposing an OpenAI Responses-compatible schema across harnesses."
---

Agent 37 is a YC F26 company selling cheap compute for agents: persistent Linux sandboxes (gVisor) or full VMs on Hetzner/OVH hardware, each with its own filesystem, quota, authenticated HTTPS URLs, and observability, launched from a dashboard template or the REST API. The pitch is price — the founder cites bursty CPU/RAM packing and non-hyperscaler hosts to charge under 10% of typical sandbox providers, metered per minute from a prepaid balance with compute billing stopped while a sandbox sleeps. Coding-agent harnesses are the first-class workload: one-click templates for Claude Code, Codex, OpenCode, Pi, Grok, Hermes, and OpenClaw, or any custom Docker image; a Gateway API routes model calls across harnesses behind an OpenAI Responses-compatible schema, and cron scheduling runs agents unattended. The company grew out of managed OpenClaw hosting; developers and agent-platform teams who want always-on agent machines without hyperscaler bills are the customers.
