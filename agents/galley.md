---
name: "Galley"
slug: "galley"
layout: "agent.njk"
category: "multiplexer"
maker: "shinpr"
license: "MIT"
url: "https://github.com/shinpr/galley"
source_code_url: "https://github.com/shinpr/galley"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-05-07"
current_release: "2026-08-19"
stars: "17"
language: "Go"
homepage: null
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "no"
plan_mode: "no"
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

Unattended agent work fails when the same model both writes and grades the code. Galley is a Go CLI and daemon that takes a task YAML with acceptance criteria, runs an executor backend — Claude Code, Codex, or Grok Build — inside an isolated worktree, then has a separately configured supervisor model review the result against those criteria before opening a PR. Executor and supervisor pairs are set per task or repo, evidence files capture diffs, model output, and verdicts for audit, and retry budgets bound runaway sessions. It installs as a marketplace skill for Claude Code, Codex, and Grok Build, and roughly half of Galley's own merged PRs were produced by Galley-managed task branches.
