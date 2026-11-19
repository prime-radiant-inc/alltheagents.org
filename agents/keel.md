---
name: "keel"
slug: "keel"
layout: "agent.njk"
category: "multiplexer"
maker: "daneb"
license: "Apache-2.0, MIT (dual)"
url: "https://github.com/daneb/keel"
source_code_url: "https://github.com/daneb/keel"
source_available: "True"
homepage: "https://daneb.github.io/keel/"
docs_url: "https://github.com/daneb/keel/blob/master/README.md"
download_url: null
install_method: "cargo install keel-harness (installs a binary called keel)"
platforms:
  - "CLI"
autonomy_level: []
specialization: "general"
language: "Rust"
first_released: "2026-08-23"
current_release: "2026-11-10"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "False"
hooks: "True"
plan_mode: "False"
plugin_docs_url: null
config_docs_url: null
model_providers: "agents bring their own providers; keel supplies none (drivers: Claude Code, Codex, Copilot, Kiro, noop)"
pricing: "free"
stars: "2"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "Makes coding agents prove their work: every approval and gate verdict goes into a hash chain that packs into a tamper-evident evidence bundle anyone can verify offline — and a PR check blocks merges that lack the bundle of a passing run of exactly their content."
---

keel is built by Dane Balia around a simple claim: AI coding agents should prove their work. You write a spec with testable criteria (EARS-style, one runnable oracle per criterion), approve it, approve the computed plan, and then an agent does the work — keel drives Claude Code, Codex, Copilot or Kiro through a ~40-line driver adapter — while keel's gates judge the result: buildable, bounded, verified against every oracle, reviewed, and decided by a human before anything counts as done. Every verdict lands in an append-only hash chain, one command exports the chain, the spec, the verdicts and the exact diff as a bundle, and keel bundle verify checks every link offline without access to your repo; a GitHub Action (keel cover) then blocks pull requests that do not carry the bundle of a passing run of exactly their content, and a CI runtime can gate the PR inside a locked-down gVisor container instead. keel is explicit that it is a conductor, not an agent loop: no model adapter, no tool registry, no inference — it sits above the harnesses and owns the two things they do not give you, auditable stopping conditions and durable memory across tools, backed by a per-repository store of steering conventions and lessons that projects into each agent's instruction files (CLAUDE.md, AGENTS.md), a tree-sitter symbol index serving seven retrieval queries, and a learning loop that promotes repeated failures into checks. It suits teams who want agent-produced changes gated by evidence rather than trust.
