---
name: "rosetta"
slug: "rosetta"
layout: "agent.njk"
category: "other"
maker: "griddynamics"
license: "Apache-2.0"
url: "https://github.com/griddynamics/rosetta"
source_code_url: "https://github.com/griddynamics/rosetta"
source_available: "True"
platforms: []
first_released: "2026-02-10"
current_release: "2026-08-19"
stars: "335"
language: "Python"
homepage: "https://griddynamics.github.io/rosetta/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Agent-agnostic: Claude Code, Cursor, Copilot, Codex, Antigravity, OpenCode, VS Code, JetBrains, Windsurf, any MCP-compatible"
pricing: "Free/open-source (Apache-2.0)"
install_method: "Install via plugin (recommended) or MCP; pip install rosetta-cli / rosetta-mcp (PyPI); then initialize and configure workspace"
docs_url: "https://griddynamics.github.io/rosetta/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/rosetta-cli/"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Agent-agnostic engineering governance and context layer that loads shared, versioned, layered (core/organization/project) instructions into every AI coding session. Discipline-encoded workflows (Prepare->Research->Plan->Act->Validate) with HITL approval gates, fresh-context review subagents, execution-backed validation, and Git-controlled instruction delivery by tag (not semantic search). No source code leaves your perimeter."
---

Grid Dynamics built Rosetta to solve the consistency problem when dozens of engineers use different agents: each session starts from whatever context the individual remembered to paste. A workspace initialized with rosetta loads the layered instruction stack into every session, classifies the request into one of thirteen SDLC workflow types (coding, security, test generation, requirements authoring, and others), and executes each through a Prepare, Research, Plan, Act, Validate pattern with approval gates. Skills cover planning, orchestration of subagent teams, reverse engineering, and security review, while a MEMORY.md file lets sessions accumulate project-specific learning. Enforcement is structural — dangerous-action detection, PII and secrets handling rules, deviation control with fresh-context reviewers — rather than advisory. Enterprise platform teams adopt it to make agent behavior auditable and uniform across tools.
