---
name: "Handshake"
slug: "handshake"
layout: "agent.njk"
category: "multiplexer"
maker: "standing-desks"
license: "MIT"
url: "https://github.com/standing-desks/handshake"
source_code_url: "https://github.com/standing-desks/handshake"
source_available: "True"
homepage: "https://standing-desks.github.io/handshake/"
docs_url: "https://standing-desks.github.io/handshake/documentation/guide/"
download_url: "https://github.com/standing-desks/handshake/releases/latest"
install_method: "brew install --cask standing-desks/tap/handshake (macOS 26+, Apple Silicon); or download the .dmg from the latest release and drag Handshake to Applications"
platforms:
  - "Desktop"
autonomy_level: []
specialization: "general"
language: "Rust"
first_released: "2026-09-26"
current_release: "2026-11-10"
maintained: "active"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: null
plugin_docs_url: null
config_docs_url: "https://standing-desks.github.io/handshake/documentation/guide/#configuration"
model_providers: "Brings no models: runs the coding-agent CLIs you have installed — Codex, Claude Code, pi, OMP, Antigravity, OpenCode v2, Kiro CLI V3 — each with its own providers and auth"
pricing: "free"
stars: "43"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A native macOS workspace that coordinates coding agents through visual agent graphs (adversarial implementer/reviewer, coordinator, custom graphs) with per-step traces, cross-agent memory, and an experimental embedded browser agents can control — it runs the harness CLIs you already use and never edits their configs."
---

Handshake, renamed from Twine in v0.4.0 (2026-10-25) after a name clash forced the change, is a terminal-first collaboration layer for developers who run several coding agents on one task. A session holds top-level workflow tabs, from a plain terminal or single interactive agent to an Adversarial workflow where an implementer hands its completion to a reviewer who approves it or sends changes back, a Coordinator graph with a planner and two workers, or custom agent graphs edited natively and saved as shareable TOML. Each role is filled by an external harness found on PATH — Codex, Claude Code, pi, OMP, Antigravity, OpenCode, or Kiro CLI — and model choice, provider access, and usage charges stay with each harness's own CLI. The Traces panel records LLM calls and terminal steps per agent with SQLite-backed detail storage, cross-agent memory carries context between agents, and an experimental browser-control mode hands agents a CLI over an embedded WebKit browser (Codex and Claude Code receive it as a session-local MCP tool). It requires macOS 26 or later on Apple Silicon, is usable day to day but carries no stability guarantees yet, and does not run workflows unattended or create worktrees — agents run directly in the open folder.
