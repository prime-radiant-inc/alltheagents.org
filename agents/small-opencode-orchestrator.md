---
name: "small-opencode-orchestrator"
slug: "small-opencode-orchestrator"
layout: "agent.njk"
category: "agent"
maker: "tempont"
license: "MIT"
url: "https://github.com/tempont/small-opencode-orchestrator"
source_code_url: "https://github.com/tempont/small-opencode-orchestrator"
source_available: "True"
platforms: []
first_released: "2026-05-02"
current_release: "2026-06-21"
stars: "31"
language: "TypeScript"
homepage: null
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "DeepSeek V4 Pro / GLM 5.2 (primary agents), DeepSeek V4 Flash (subagents)"
pricing: "open-source"
install_method: "Clone to ~/.config/opencode, then npm install"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/tempont/small-opencode-orchestrator"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Lightweight OpenCode configuration implementing an orchestrator pattern for AI-assisted software development. Intentionally minimal — not a general-purpose agent platform, but a small, understandable orchestrator pattern with token-conscious delegation (subagents get focused tasks, not full context) and approval-gated planning. Pairs strong models for coordination/primary agents with cheap models for scoped subagent tasks to optimize cost and quality. Subagents: plan-runner, code-executor, test-verifier, code-reviewer, docs-reviewer, security-reviewer, spec-critic, api-docs-researcher, host-security-investigator."
---

The project is a configuration rather than a binary: cloned into ~/.config/opencode, it defines an orchestrator agent that routes work to plan-runner, code-executor, test-verifier, code-reviewer, docs-reviewer, security-reviewer, and other scoped subagents. Plans are written to .opencode/plans and a post-approval plugin routes the session from planning into build mode, keeping subagent prompts focused instead of shipping them the full context. Model routing is explicit and editable in opencode.jsonc, pairing expensive reasoning models with cheap execution models to control cost. It fits OpenCode users who want a readable, hackable multi-agent setup they can audit line by line rather than an agent platform.
