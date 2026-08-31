---
name: "Gadfly"
slug: "gadfly"
layout: "agent.njk"
category: "other"
maker: "Touchpoint-Labs"
license: "MIT"
url: "https://github.com/Touchpoint-Labs/Gadfly"
source_code_url: "https://github.com/Touchpoint-Labs/Gadfly"
source_available: "True"
platforms: []
first_released: "2026-07-01"
current_release: "2026-07-15"
stars: "45"
language: "Python 3.11+"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "True"
plan_mode: "no"
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

Coding agents drift from their specifications and commit subtle bugs mid-task, and post-hoc review catches these too late. Gadfly intercepts Claude Code's PreToolUse hook so each action is judged before execution, with a deterministic filter auto-approving safe commands and two read-only LLM supervisors handling the rest. It enforces spec-driven development through a required spec.md, an optional midwife pass asks clarifying questions before building, and an idle-time extractor distills out-of-band user corrections from an append-only edit ledger into durable rules. The autonomy dial (autonomous, balanced, collaborative) sets how often it interrupts, configuration lives in gadfly.toml, and it runs on an existing Claude Code subscription or the Anthropic API.
