---
name: "Gadfly"
slug: "gadfly"
layout: "agent.njk"
category: "agent"
maker: "Touchpoint-Labs"
license: "MIT"
url: "https://github.com/Touchpoint-Labs/Gadfly"
source_code_url: "https://github.com/Touchpoint-Labs/Gadfly"
source_available: True
platforms: []
first_released: "2026-07-01"
current_release: "2026-07-15"
stars: "45"
language: "Python 3.11+"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: True
hooks: True
plan_mode: null
model_providers: "Anthropic (Claude Code subscription or Anthropic API)"
pricing: "Free (open source, MIT); uses your existing Claude Code subscription"
install_method: "pip install gadfly-ai, then 'gadfly init' in your project, then 'gadfly status'"
docs_url: "https://github.com/Touchpoint-Labs/Gadfly#readme"
plugin_docs_url: null
config_docs_url: "https://github.com/Touchpoint-Labs/Gadfly/blob/main/spec.md"
download_url: "https://github.com/Touchpoint-Labs/Gadfly"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "A Socratic supervision layer for AI coding agents. Sits inside Claude Code's live tool-call loop, intercepting every PreToolUse hook before execution. Two independent supervisors (Architect on Opus, Code Reviewer on Sonnet) deliver one of four verdicts (allow/question/surface/block). Self-improving via append-only edit-ledger and idle-time extractor that distills corrections into durable memory. Enforces spec-driven development, catches drift and bugs pre-execution. Zero dependencies. Autonomy dial (autonomous/balanced/collaborative)."
---

A Socratic supervision layer for AI coding agents. Sits inside Claude Code's live tool-call loop, intercepting every PreToolUse hook before execution. Two independent supervisors (Architect on Opus, Code Reviewer on Sonnet) deliver one of four verdicts (allow/question/surface/block). Self-improving via append-only edit-ledger and idle-time extractor that distills corrections into durable memory. Enforces spec-driven development, catches drift and bugs pre-execution. Zero dependencies. Autonomy dial (autonomous/balanced/collaborative).
