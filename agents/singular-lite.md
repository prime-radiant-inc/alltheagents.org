---
name: "Singular"
slug: "singular-lite"
layout: "agent.njk"
category: "multiplexer"
maker: "alex-reysa"
license: "GPL-3.0"
url: "https://github.com/alex-reysa/singular-lite"
source_code_url: "https://github.com/alex-reysa/singular-lite"
source_available: "True"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2026-06-10"
current_release: null
stars: 37
language: "Shell"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "delegates to the installed runner CLIs (claude, codex)"
pricing: "free"
install_method: "./install.sh installs to ~/.singular with a per-repo version pin; requires bash >= 4, python3, git"
docs_url: "https://github.com/alex-reysa/singular-lite/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A three-tier local orchestration engine — L0 origin scheduler running reconcile cycles (import, recover, integrate, dispatch, snapshot), L1 area planners, and L2 worker agents each in an isolated git worktree — with durable per-task leases, gate commands whose results feed an auditor model, and a decider mapping failures to retry, amend-scope, escalate, or park."
---

Singular (repo singular-lite) is a bash-and-python orchestration engine for running many autonomous coding agents against one repository. Its three-tier scheduling model puts an L0 origin scheduler through a reconcile cycle — import, recover, integrate, dispatch, snapshot — with L1 area planners decomposing work and L2 worker agents each executing one task in an isolated git worktree on a per-task branch, using whatever runner CLI is on PATH such as claude or codex. Coordination is durable rather than ad hoc: per-task leases prevent collision, state packets track owned files and changes, gate commands like npm test feed results to an auditor model, and a decider maps failures to retry, amend-scope, escalate, or park. Workers dispatch detached by default with a reaper attributing completions and crashes on later cycles, and the autonomy loop supports human approval gates and context continuity through capsules, findings ledgers, and session affinity. It targets macOS and Linux operators running long-lived agent fleets in a single repo.
