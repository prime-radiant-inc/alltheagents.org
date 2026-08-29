---
name: "BHIL-AI-First-Development-Toolkit"
slug: "bhil-ai-first-development-toolkit"
layout: "agent.njk"
category: "other"
maker: "PolymathWizard"
license: "MIT"
url: "https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit"
source_code_url: "https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit"
source_available: "True"
platforms: []
first_released: "2026-03-27"
current_release: "2026-03-28"
stars: "130"
language: "Markdown, Bash"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: "False"
subagents: "True"
hooks: "yes (.claude/hooks shipped in-repo for Claude Code sessions)"
plan_mode: null
model_providers: "Claude Code"
pricing: "Free (MIT)"
install_method: "git clone; chmod +x tools/scripts/*.sh; ./tools/scripts/init.sh; then run claude"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/PolymathWizard/BHIL-AI-First-Development-Toolkit"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Production-grade methodology repository for building AI-native applications using iterative sprints where AI coding agents are primary implementors; provides traceable artifact chain (PRD -> SPEC -> ADR -> TASK -> CODE -> REVIEW -> DEPLOY); optimized for Claude Code with custom subagents in .claude/agents/"
---

The BHIL toolkit's central claim is that the bottleneck in AI-assisted development is specification quality, not code generation, so it packages a complete methodology for spec-driven sprints where AI agents implement and humans architect and review. Every sprint produces artifacts in a chain from PRD through SPEC, ADR, TASK, CODE, REVIEW, and DEPLOY, linked by asymmetric traceability IDs in YAML frontmatter (PRD-NNN, SPEC-NNN, ADR-NNN, and so on) so any artifact traces back to its parent requirement. AI-native ADR extensions cover model selection benchmarks, prompt strategy versioning with eval thresholds, and orchestration patterns such as orchestrator-worker and swarm. The repository ships guides, templates, a worked end-to-end example, shell scripts for artifact validation, and a .claude directory with hooks, rules, and skills that wire the methodology into Claude Code. It targets solo practitioners building LLM-powered applications with Claude Code as the primary implementor.
