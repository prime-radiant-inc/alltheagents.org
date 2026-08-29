---
name: "Forge"
slug: "forge"
layout: "agent.njk"
category: "agent"
maker: "LucasDuys"
license: "MIT"
url: "https://github.com/LucasDuys/forge"
source_code_url: "https://github.com/LucasDuys/forge"
source_available: "True"
platforms:
  - "IDE"
  - "Autonomous"
first_released: "2026-03-21"
current_release: "2026-07-15"
stars: "55"
language: "JavaScript"
homepage: "https://lucasduys.github.io/forge/"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Anthropic (Claude only)"
pricing: "open-source"
install_method: "claude plugin marketplace add LucasDuys/forge then claude plugin install forge@forge-marketplace (requires Claude Code v1.0.33+)"
docs_url: "https://lucasduys.github.io/forge/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "5-phase autonomous loop (brainstorm->plan->execute->review+verify->backprop); state persisted on disk in .forge/ not conversation memory; crash-recoverable via lock file + checkpoints; per-task git worktrees with TDD and atomic squash-merge; hard token budgets; backpropagation turns runtime failures into new acceptance criteria + regression tests; multiplayer mode via distributed claim queue."
---

Forge turns Claude Code into a brainstorm-to-commit pipeline built for long, token-hungry runs: an idea becomes an R-numbered spec with testable acceptance criteria, a dependency-ordered task DAG, TDD execution in per-task git worktrees, then review and four-level verification (existence, substantive, wired, runtime). Because state lives in .forge/ on disk instead of the context window, crashes and context resets resume from checkpoints, and a backprop phase converts runtime failures into new acceptance criteria plus regression tests that re-enter the loop. Seven hooks enforce token budgets, trim Bash output, cache reads, and compress tool output, which the project measures at roughly 29% real-token savings on filterable workloads. Approval-gated by default with a full mode for trusted runs, it appeals to Claude Code subscribers running multi-hour feature development.
