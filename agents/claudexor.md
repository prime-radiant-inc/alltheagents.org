---
name: "Claudexor"
slug: "claudexor"
layout: "agent.njk"
category: "multiplexer"
maker: "razzant"
license: "MIT"
url: "https://github.com/razzant/claudexor"
source_code_url: "https://github.com/razzant/claudexor"
source_available: "True"
platforms:
  - "CLI"
  - "Desktop"
first_released: "2026-06-05"
current_release: "2026-08-20"
stars: "416"
language: "TypeScript, Swift"
homepage: "https://claudexor.ai/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "Codex CLI, Claude Code, Cursor CLI, OpenCode, Antigravity CLI (agy), OpenAI, Anthropic"
pricing: "Free / open-source (MIT); users pay for their own underlying AI vendor subscriptions/API usage"
install_method: "CLI via npm install -g claudexor; macOS app via signed DMG from GitHub Releases; or build from source using pnpm"
docs_url: "https://claudexor.ai/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/razzant/claudexor/releases"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Multi-harness control plane for AI coding agents that runs them behind one typed interface with quota-aware rotation, shared thread context, and cross-model review; best-of-N races with independent reviewers/arbitration, honest budget/quota accounting (never reports unknown cost as $0), deterministic gates, multi-account credential profiles with live quota tracking, no telemetry"
---

Claudexor targets the practitioner holding several paid agent subscriptions who wants them as interchangeable capacity rather than separate tools. A local daemon routes turns to a chosen harness, resumes native sessions for continuity, and turns write requests into inspectable patches; quota rotation switches accounts only on typed vendor-limit signals, and best-of-N races select winners through independent, ideally cross-family, review rather than self-grading. A --council mode has multiple harnesses draft competing plans that a primary merges. Everything runs locally with file-based artifacts, and the v3.8.0 release's missing signing documents were the one notable supply-chain stumble. Solo power users running multi-agent setups are the audience.
