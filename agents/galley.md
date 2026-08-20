---
name: "Galley"
slug: "galley"
layout: "agent.njk"
category: "multiplexer"
maker: "shinpr"
license: "MIT"
url: "https://github.com/shinpr/galley"
source_code_url: "https://github.com/shinpr/galley"
source_available: True
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-05-07"
current_release: "2026-08-19"
stars: "17"
language: "Go"
homepage: null
mcp_support: null
plugin_support: True
claude_code_plugin: True
subagents: null
hooks: null
plan_mode: null
model_providers: "Claude Code, OpenAI Codex, GLM (Z.AI), Kimi, Grok"
pricing: "Free / open-source (MIT)"
install_method: "Plugin marketplace (/plugin marketplace add shinpr/galley), or curl installer script, or go install github.com/shinpr/galley/cmd/galley@latest"
docs_url: "https://github.com/shinpr/galley/blob/main/docs/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/shinpr/galley/releases"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Local runtime for supervised, multi-model AI coding — decouples executor and supervisor models so you can use cheap/fast/specialized models for implementation while a different model independently reviews against explicit acceptance criteria. Runs tasks in isolated git worktrees, records evidence (diffs, model output, verdicts), and hands accepted work off as pull requests for unattended (AFK) multi-model coding."
---

Local runtime for supervised, multi-model AI coding — decouples executor and supervisor models so you can use cheap/fast/specialized models for implementation while a different model independently reviews against explicit acceptance criteria. Runs tasks in isolated git worktrees, records evidence (diffs, model output, verdicts), and hands accepted work off as pull requests for unattended (AFK) multi-model coding.
