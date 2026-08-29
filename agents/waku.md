---
name: "Waku"
slug: "waku"
layout: "agent.njk"
category: "multiplexer"
maker: "egoist"
license: "GPL-3.0"
url: "https://waku.sh"
source_code_url: "https://github.com/egoist/waku"
source_available: "True"
platforms:
  - "Desktop"
first_released: "2026-07-31"
current_release: "2026-08-24"
stars: 1278
language: "Rust"
homepage: "https://waku.sh"
mcp_support: null
plugin_support: null
claude_code_plugin: "no"
subagents: null
hooks: null
plan_mode: "no"
model_providers: "delegates to the connected agent CLIs"
pricing: "free"
install_method: "Download from waku.sh (signed, notarized, auto-updated via Sparkle)"
docs_url: "https://github.com/egoist/waku/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://waku.sh"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A native desktop app for all your coding agents, built in Rust with GPUI (the GPU-accelerated framework behind Zed, explicitly not Electron): it connects to each agent via its strongest native interface (stream-json, JSON-RPC, live events), normalizes sessions into a provider-neutral model, and snapshots the working tree under a hidden git ref at every prompt so code and conversation rewind together."
---

Waku is a native macOS app from EGOIST that aggregates the coding agent CLIs you already run into a single window it calls graphite. It connects to each agent through its strongest native protocol and normalizes sessions, transcripts, tool activity, and checkpoints into a provider-neutral model, so the interface stays the same regardless of which agent is underneath. Every prompt snapshots your working tree under a hidden git ref, which lets you roll back the code and the provider conversation together — the checkpoint is tied to the turn, not just the filesystem. It is local-first with no account, no telemetry, and no cloud service, requires no new API keys, and its keyboard-first interactions (cmd+N for a new session, return to queue follow-ups, cmd+return to steer mid-turn) target developers who live in these loops all day. The app is signed and notarized with Sparkle auto-updates, and the site notes it is not YC-backed.
