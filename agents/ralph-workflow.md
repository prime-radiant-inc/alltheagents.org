---
name: "Ralph Workflow"
slug: "ralph-workflow"
layout: "agent.njk"
category: "multiplexer"
maker: "Ralph-Workflow"
license: "AGPL-3.0-or-later"
url: "https://github.com/Ralph-Workflow/Ralph-Workflow"
source_code_url: "https://github.com/Ralph-Workflow/Ralph-Workflow"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-01-13"
current_release: "2026-08-20"
stars: "5"
language: "Python"
homepage: "https://ralphworkflow.com"
mcp_support: "no"
plugin_support: null
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "True"
model_providers: "Claude Code, Codex, OpenCode, Nanocoder, AGY (Google Anti Gravity), Pi, Cursor, Kimi Code (9 built-in agent backends)"
pricing: "Free / open-source (AGPL-3.0-or-later)"
install_method: "From ralph-workflow/ directory: make install (stable) or make dev (dev build). Also available via PyPI."
docs_url: "https://ralphworkflow.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/ralph-workflow/"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Independent reference implementation of the Ralph Loop pattern (attributed to Geoffrey Huntley). Multi-agent orchestrator supporting 9 coding agent backends. Local-first. Ralph loop workflow: plan → build → verify → fix. 5,923 commits with CI via Woodpecker."
---

Ralph Workflow turns the Ralph loop — popularized as a blog technique for running coding agents in iterative cycles — into an installable orchestrator with operator-grade documentation. You hand it one well-specified task and it runs a plan, build, verify, fix loop against an agent backend of your choice: Claude Code, Codex, OpenCode, Nanocoder, AGY, Pi, Cursor, or Kimi Code, authenticated once locally. The tool ships an opinionated default workflow built around spec-driven development, intended to be adopted as-is and extended later, rather than a bare loop script. Install hygiene matters to the design: a separate rdev launcher avoids shadowing an existing global ralph installation, and the project ships Sphinx documentation, CI configs, and Docker support unusual for scripts in this genre. Developers who want the Ralph pattern without hand-rolling bash loops use it for coding tasks too large to babysit and too risky to run unattended without verification.
