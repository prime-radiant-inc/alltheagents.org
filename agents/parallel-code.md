---
name: "Parallel Code"
slug: "parallel-code"
layout: "agent.njk"
category: "multiplexer"
maker: "johannesjo"
license: "MIT"
url: "https://github.com/johannesjo/parallel-code"
source_code_url: "https://github.com/johannesjo/parallel-code"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Desktop"
first_released: "2026-02-18"
current_release: "2026-08-18"
stars: "981"
language: "TypeScript"
homepage: "https://parallelcode.app"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, Codex CLI, Gemini CLI, Antigravity CLI, Copilot CLI, MiniMax M2.7"
pricing: "free"
install_method: "binary"
docs_url: "https://parallelcode.app"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/johannesjo/parallel-code/releases/latest"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Desktop app that runs multiple AI coding agents in true parallel execution, each in its own automatic git worktree/branch for isolated, reviewable code changes. Unified GUI for diff review and merge management, AI Arena for head-to-head agent racing, keyboard-first control, mobile monitoring via QR code, and per-task Docker sandboxing."
---

Parallel Code emerged to solve the isolation problem in multi-agent development: when several coding CLIs edit the same checkout, they clobber each other and reviewing the outcome means diffing by hand. The Electron desktop app runs each agent in its own automatically created git worktree and branch, then presents all results in one review surface with inline comments, merge controls, and keyboard-first navigation. An AI Arena mode runs the same task through multiple agents head-to-head for comparison, per-task Docker sandboxing contains untrusted runs, and a QR code mirrors session state to a phone for monitoring away from the desk. The app is free, MIT-licensed, and requires the user's own agent subscriptions, running on macOS and Linux with prebuilt binaries. Its users are developers who race or fan out multiple agent CLIs and need a review surface for the results.
