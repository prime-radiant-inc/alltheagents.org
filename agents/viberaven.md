---
name: "VibeRaven"
slug: "viberaven"
layout: "agent.njk"
category: "multiplexer"
maker: "ohad6k"
license: "MIT"
url: "https://github.com/ohad6k/VibeRaven"
source_code_url: "https://github.com/ohad6k/VibeRaven"
source_available: "True"
platforms: []
first_released: "2026-06-09"
current_release: "2026-07-12"
stars: "31"
language: "TypeScript/JavaScript"
homepage: "https://viberaven.dev"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "AI agents: Claude Code, Codex, Gemini CLI. Service providers: Supabase, Vercel, GitHub, Stripe, Sentry, Resend, Clerk, Upstash, Auth.js, PostHog"
pricing: "Free/open source (MIT). No login, no API key, no telemetry, no scan quota"
install_method: "npx -y viberaven"
docs_url: "https://viberaven.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/viberaven"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Open-source local cockpit for AI-built apps. Local-first philosophy: runs entirely on your machine — no login, no API key, no telemetry. 'Can I ship?' verdict: offline checks produce a gated score with blockers/warnings before deploy. Multi-agent cockpit drives Codex, Claude Code, and Gemini CLI from one local UI. Markdown on disk: all context lives in .viberaven/ as plain files readable by any agent and versioned by git. Six-skill pack routes agents through architecture, version forensics, and launch proof."
---

VibeRaven exists for the gap between 'the agent says it's done' and 'this is safe to deploy': AI-built apps routinely miss production essentials like auth wiring, service-role key exposure, webhook configuration, and monitoring. Running entirely locally with no login or telemetry, it connects the coding agent to the app's real context — stack and provider detection, release timeline, architecture map — and produces a gated ship-readiness verdict from offline checks covering auth/RLS, secret exposure, webhooks, and deploy readiness; a CI mode exits nonzero on blockers. Its agent cockpit drives Codex, Claude Code, or Gemini CLI from one UI with ask/approve/full access modes, and every artifact lives as plain markdown under .viberaven/, versioned by git and readable by any agent. Indie developers and small teams shipping AI-built apps use it as a pre-deploy gate; note the core product code is developed in a private repository, with the public repo carrying the CLI and agent integration surface.
