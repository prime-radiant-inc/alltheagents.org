---
name: "SIFT"
slug: "sift"
layout: "agent.njk"
category: "other"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/sift"
source_code_url: "https://github.com/2389-research/sift"
source_available: "True"
platforms:
  - "IDE"
first_released: null
current_release: null
stars: "0"
language: null
homepage: null
mcp_support: "no"
plugin_support: "yes (Agent Skill format, npx skills add)"
claude_code_plugin: "yes (runs inside Claude Code and similar agents)"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "npx skills add 2389-research/sift"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Structural Inspection for Technical Simplification — a read-only Agent Skill that audits a whole codebase for material simplifications (data structures, state, algorithms, control flow, schemas, lifecycle/concurrency, ownership). Produces a coverage contract, partitions the repo into subsystem reviews, validates findings, and outputs a prioritized report. Does not edit code or run tests."
---

SIFT — Structural Inspection for Technical Simplification — is a read-only Agent Skill that runs inside host agents such as Claude Code rather than as a standalone tool. It audits an entire codebase for material simplifications across data structures, state, algorithms, control flow, schemas, lifecycle and concurrency, and ownership. The skill first produces a coverage contract so the audit's scope is explicit, partitions the repository into subsystem reviews, validates each finding, and emits a prioritized report. It does not edit code or run tests; its output is a map of where the codebase can be made simpler and why. The audience is engineers who want a structured, repeatable simplification pass driven by the host agent they already use, without the skill touching anything.
