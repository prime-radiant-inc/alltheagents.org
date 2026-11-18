---
name: "YYLO"
slug: "yylo"
layout: "agent.njk"
category: "multiplexer"
maker: "yylo-dev"
license: "MIT"
url: "https://yylo.dev"
source_code_url: "https://github.com/yylo-dev/yylo"
source_available: "True"
homepage: null
docs_url: "https://yylo.dev/docs/yylo"
download_url: null
install_method: "npm install --global @yylo/cli@latest"
platforms:
  - "CLI"
autonomy_level:
  - "pair-programmer"
  - "autonomous-background"
specialization: "general"
language: "Python"
first_released: "2026-01-06"
current_release: "2026-11-04"
maintained: "active"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "False"
plugin_docs_url: "https://yylo.dev/skills"
config_docs_url: null
model_providers: "Pi, Claude Code, Codex, Gemini (agent CLIs bring their own providers)"
pricing: "free"
stars: "69"
sources:
  - "github-issue"
last_verified: "2026-11-18"
date_added: "2026-11-18"
what_makes_it_special: "Ships equivalent yylo and yy launchers, a live terminal agent mode (ypl, short for yy pi --live), and receipt-backed repository changes behind typed task, validation, merge, and release-readiness boundaries. Its yy ledger and yy benchmark commands delegate to the independently installed YYLO Ledger and YYLO Benchmark packages rather than bundling their implementations."
---

YYLO grew out of the "Ralph method" of looping a coding agent until the job is done, and exists to make that loop bounded and auditable: iteration counts cap both the outer workflow and each agent invocation, task state lives in the Git-native YYLO Ledger rather than markdown files, and runs leave session, validation, and merge evidence behind as receipts. It initializes a workspace and a dedicated per-task worktree, delegates the actual coding to external agent CLIs (Pi, Claude Code, Codex, Gemini) that bring their own provider credentials, then verifies and merges the result through explicit task and merge commands without editing product code itself. It is aimed at developers who want a quick agent loop and at project operators who need delivery they can inspect; the maker, Juno AI INC., develops it alongside a separate proprietary inference-optimization product, YYLO OS.
