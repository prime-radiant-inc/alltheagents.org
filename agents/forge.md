---
name: "Forge"
slug: "forge"
layout: "agent.njk"
category: "agent"
maker: "LucasDuys"
license: "MIT"
url: "https://github.com/LucasDuys/forge"
source_code_url: "https://github.com/LucasDuys/forge"
source_available: True
platforms:
  - "IDE"
  - "Autonomous"
first_released: "2026-03-21"
current_release: "2026-07-15"
stars: "55"
language: "JavaScript"
homepage: "https://lucasduys.github.io/forge/"
mcp_support: False
plugin_support: True
claude_code_plugin: True
subagents: True
hooks: True
plan_mode: True
model_providers: "Anthropic (Claude only)"
pricing: null
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

5-phase autonomous loop (brainstorm->plan->execute->review+verify->backprop); state persisted on disk in .forge/ not conversation memory; crash-recoverable via lock file + checkpoints; per-task git worktrees with TDD and atomic squash-merge; hard token budgets; backpropagation turns runtime failures into new acceptance criteria + regression tests; multiplayer mode via distributed claim queue.
