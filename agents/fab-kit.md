---
name: "fab-kit"
slug: "fab-kit"
layout: "agent.njk"
category: "agent"
maker: "sahil87"
license: "MIT"
url: "https://github.com/sahil87/fab-kit"
source_code_url: "https://github.com/sahil87/fab-kit"
source_available: True
platforms:
  - "IDE"
first_released: "2026-02-05"
current_release: "2026-08-19"
stars: "29"
language: "Go"
homepage: "https://shll.ai/fab-kit"
mcp_support: False
plugin_support: True
claude_code_plugin: True
subagents: True
hooks: True
plan_mode: True
model_providers: "Claude Code, Codex, Cursor, Windsurf (plain markdown prompts, no SDK/vendor lock-in)"
pricing: "Free/open source"
install_method: "curl -fsSL https://shll.ai/install | sh (installs entire shll toolkit via Homebrew)"
docs_url: "https://shll.ai/fab-kit"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/sahil87/fab-kit/releases"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Development toolkit for AI-assisted coding with a 6-stage pipeline (intake, apply, review, hydrate, ship, review-PR) using plain markdown prompts — no SDK, no vendor lock-in. Structured thinking-first pipeline: forces intake/plan before code. Assembly-line parallelism via self-contained change folders + git worktree isolation. Shared project memory in docs/memory/ committed to git. SRAD autonomy framework: 4-dimension confidence scoring decides when AI should assume vs. ask. Project constitution (constitution.md) enforces MUST/SHOULD/MUST NOT architectural rules. Self-correcting review loop with sub-agent review (up to 3 cycles)."
---

Development toolkit for AI-assisted coding with a 6-stage pipeline (intake, apply, review, hydrate, ship, review-PR) using plain markdown prompts — no SDK, no vendor lock-in. Structured thinking-first pipeline: forces intake/plan before code. Assembly-line parallelism via self-contained change folders + git worktree isolation. Shared project memory in docs/memory/ committed to git. SRAD autonomy framework: 4-dimension confidence scoring decides when AI should assume vs. ask. Project constitution (constitution.md) enforces MUST/SHOULD/MUST NOT architectural rules. Self-correcting review loop with sub-agent review (up to 3 cycles).
