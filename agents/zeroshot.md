---
name: "zeroshot"
slug: "zeroshot"
layout: "agent.njk"
category: "agent"
maker: "the-open-engine"
license: "MIT"
url: "https://github.com/the-open-engine/zeroshot"
source_code_url: "https://github.com/the-open-engine/zeroshot"
source_available: True
platforms:
  - "CLI"
first_released: "2025-12-25"
current_release: "2026-08-19"
stars: "1703"
language: "TypeScript/Node.js + Rust components"
homepage: "https://www.theopenengine.com"
mcp_support: null
plugin_support: "yes - custom workflows as JSON files; provider registry"
claude_code_plugin: "n/a - Claude is a supported provider; .claude/CLAUDE.md present"
subagents: "yes - conductor, executor, planner, worker, validators, meta-coordinator, investigator, fixer, tester, completion-detector"
hooks: "yes - cluster-hooks/ directory"
plan_mode: "partial - planner agent in full-workflow"
model_providers: "Claude, Codex, bundled Gateway, Gemini, OpenCode, Pi, OMP, Kiro, Copilot"
pricing: "open-source"
install_method: "npm"
docs_url: "https://www.theopenengine.com"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Independent executor-verifier orchestration: 'The agent that wrote the code shouldn't be the one that says it works.' Verifiers don't share the executor's session, must reproduce failures independently, and approve/reject with specific objections. Complexity-based workflow routing (TRIVIAL through CRITICAL with escalating validator counts), git worktree isolation, crash-safe SQLite ledger, and a message-driven multi-agent architecture. 'Layer 01 - Verification' of The Open Engine."
---

Independent executor-verifier orchestration: 'The agent that wrote the code shouldn't be the one that says it works.' Verifiers don't share the executor's session, must reproduce failures independently, and approve/reject with specific objections. Complexity-based workflow routing (TRIVIAL through CRITICAL with escalating validator counts), git worktree isolation, crash-safe SQLite ledger, and a message-driven multi-agent architecture. 'Layer 01 - Verification' of The Open Engine.
