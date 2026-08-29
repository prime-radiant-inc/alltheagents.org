---
name: "claudecode-orchestrator"
slug: "claudecode-orchestrator"
layout: "agent.njk"
category: "agent"
maker: "darrenapfel"
license: null
url: "https://github.com/darrenapfel/claudecode-orchestrator"
source_code_url: "https://github.com/darrenapfel/claudecode-orchestrator"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2025-06-28"
current_release: "2026-04-21"
stars: "38"
language: "TypeScript, JavaScript (shell script entry point)"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code"
pricing: "Free / open-source"
install_method: "./orchestrator.sh global (replaces ~/.claude/claude.md); ./orchestrator.sh local in any project"
docs_url: "https://github.com/darrenapfel/claudecode-orchestrator/wiki"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/darrenapfel/claudecode-orchestrator"
maintained: "dormant"
sources:
  - "agent_infra"
what_makes_it_special: "Orchestration framework that runs Claude Code as a 12-persona software team (Orchestrator, PM, Architect, SWE, UX, SDET, Test, Integration, Performance, Security, DevOps, Docs) working in parallel; enforces evidence-based validation where every task produces an EVIDENCE.md; milestones end with a live, running service started and smoke-tested for the user; documented fix cycles on validation failures; structured human feedback loop. DEPRECATED in favor of limeriq.ai."
---

The framework imposes software-team process on a single agent: personas with explicit file-ownership boundaries prevent two roles from editing the same area, and the orchestrator is required to dispatch independent work simultaneously, with a parallel-execution detector flagging lapses into sequential behavior. Milestones structure work from discovery through requirements, parallel implementation, integration, validation, and fix cycles, with every task producing evidence files and automatic git commits so progress is auditable. The author has deprecated the project in favor of a commercial successor (limeriq.ai), so it no longer receives maintenance.
