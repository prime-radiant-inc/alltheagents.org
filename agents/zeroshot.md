---
name: "zeroshot"
slug: "zeroshot"
layout: "agent.njk"
category: "agent"
maker: "the-open-engine"
license: "MIT"
url: "https://github.com/the-open-engine/zeroshot"
source_code_url: "https://github.com/the-open-engine/zeroshot"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-12-25"
current_release: "2026-08-19"
stars: "1703"
language: "TypeScript/Node.js + Rust components"
homepage: "https://www.theopenengine.com"
mcp_support: "no"
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

zeroshot rests on a specific claim: the agent that wrote code is structurally unfit to certify it, since shared context produces shared blind spots. The tool is a CLI that orchestrates clusters of agents over a message bus, with a conductor classifying each task by complexity and type and selecting a matching workflow — a debug workflow, a lone worker, a worker-plus-validator pair, or the full pipeline where critical tasks get a planner, four validators in two stages, and a meta-coordinator. The load-bearing rule is verifier independence: validation agents receive none of the executor's session or reasoning, must reproduce any reported failure from scratch, and can reject with concrete objections, which forces code that survives to have been checked by an agent that never saw the author's rationale. Runs persist every step to a crash-safe SQLite ledger so interrupted runs resume; tasks enter from GitHub, GitLab, Jira, Azure DevOps, or Linear, and completed work ships through git flows gated by quality checks that fail closed. Agents — conductor, planner, worker, validators, fixer, tester, investigator, completion-detector — are wired through JSON workflow templates that teams can rewrite, and cycles between agents are legal with escape logic for rings. Distributed as an npm CLI under MIT with pluggable provider registries (Claude, Codex, Gemini, Copilot, and others, with no keys stored), it is Layer 01 of a larger Open Engine architecture, aimed at teams that want unattended code production with adversarial verification rather than self-graded output.
