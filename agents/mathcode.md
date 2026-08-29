---
name: "mathcode"
slug: "mathcode"
layout: "agent.njk"
category: "agent"
maker: "math-ai-org"
license: "Apache-2.0"
url: "https://github.com/math-ai-org/mathcode"
source_code_url: "https://github.com/math-ai-org/mathcode"
source_available: "yes"
platforms: []
first_released: "2026-04-02"
current_release: "2026-08-19"
stars: "706"
language: "TypeScript, Python"
homepage: "https://math-ai-org.github.io/mathcode"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "yes"
plan_mode: "yes"
model_providers: "OpenAI, Anthropic, Bedrock, Vertex, Foundry, OpenRouter"
pricing: "open-source"
install_method: "binary"
docs_url: "https://math-ai-org.github.io/mathcode"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Mathematical coding agent focused on formal theorem proving in Lean. Atomic Lean tools (LeanGoal, LeanCheck, LeanSearch, LeanVerify) for interactive proof construction with strict verification. Persistent Lean feedback backends (in-process Lean REPL, optional Kimina Lean Server). Theorem Library (/theorem-store) and Axiom Library (/axiomatize). Obsidian Theorem Graph for visualizing dependencies. Agentic Lean (free subgoal decomposition, no fixed planner). Three plugin mechanisms: Skills, Tools, Plugins."
---

MathCode brings the agentic coding workflow to formal mathematics, where a proof is machine-checkable and verification is unambiguous. The agent inspects goals at explicit source positions, compiles candidate proofs with structured feedback, and treats only LeanVerify's verified flag as completion, with optional in-process REPL and Kimina Lean Server backends feeding the loop. Persistent theorem and axiom libraries store verified results transactionally, an Obsidian graph visualizes theorem dependencies, and three extension mechanisms (project-local skills, auto-discovered Python tools, plugin folders with commands/skills/agents/MCP servers/hooks) let formalization teams add domain tooling. Checksum-verified release binaries ship with a setup script that installs and health-checks Lean and Mathlib; mathematicians and formalization teams are the users.
