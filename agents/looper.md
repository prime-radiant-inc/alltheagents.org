---
name: "looper"
slug: "looper"
layout: "agent.njk"
category: "agent"
maker: "nexu-io"
license: "MIT"
url: "https://github.com/nexu-io/looper"
source_code_url: "https://github.com/nexu-io/looper"
source_available: True
platforms:
  - "Autonomous"
first_released: "2026-04-11"
current_release: "2026-08-17"
stars: "106"
language: "Go"
homepage: null
mcp_support: null
plugin_support: True
claude_code_plugin: True
subagents: True
hooks: null
plan_mode: True
model_providers: "opencode, claude-code, codex, cursor-cli, grok-build, pi, omp"
pricing: "Free / open source (MIT)"
install_method: "curl -fsSL https://raw.githubusercontent.com/nexu-io/looper/main/scripts/install.sh | sh then looper bootstrap"
docs_url: "https://github.com/nexu-io/looper/tree/main/docs"
plugin_docs_url: null
config_docs_url: "https://github.com/nexu-io/looper/blob/main/docs/configuration.md"
download_url: "https://github.com/nexu-io/looper/releases/latest"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Loop-based agents with success criteria (not fixed steps); forge is source of truth (no external tracker/YAML); parallel-safe git worktrees; local/inspectable/stoppable daemon; multi-repo support; bring-your-own-agent with no vendor lock-in"
---

Loop-based agents with success criteria (not fixed steps); forge is source of truth (no external tracker/YAML); parallel-safe git worktrees; local/inspectable/stoppable daemon; multi-repo support; bring-your-own-agent with no vendor lock-in
