---
name: "Arcgentic"
slug: "arcgentic"
layout: "agent.njk"
category: "other"
maker: "Arch1eSUN"
license: "MIT"
url: "https://github.com/Arch1eSUN/Arcgentic"
source_code_url: "https://github.com/Arch1eSUN/Arcgentic"
source_available: "True"
platforms: []
first_released: "2026-05-12"
current_release: "2026-08-12"
stars: "302"
language: "Python, JavaScript"
homepage: "https://pypi.org/project/arcgentic/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "OpenAI (Codex), Anthropic (Claude Code)"
pricing: "open-source"
install_method: "npm install -g arcgentic; pipx install arcgentic; /plugin marketplace add Arch1eSUN/Arcgentic; git clone + scripts/install-codex-local.sh"
docs_url: "https://pypi.org/project/arcgentic/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/arcgentic/"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Harness engineering layer for AI coding agents (Codex & Claude Code). Turns ad-hoc prompting into a gated engineering workflow with fixed roles (Orchestrator, Planner, Developer, Test, Auditor), stop states, audit gates, and evidence-based pass/fix decisions. Features a configurable role-routing topology engine."
---

Ad-hoc prompting of coding agents produces drift: silent scope changes, skipped tests, and unverified done claims. Arcgentic is a layer installed into Codex or Claude Code that structures each session into an Orchestrator dispatching fixed Planner, Developer, Test, and Auditor roles through plan, build, self-audit, and independent-audit gates, with NEEDS_FIX loops and stop states enforced at each handoff. Role routing runs through a topology engine overridable via state.yaml, with an optional MCP server exposing a live status panel of round progress and verdicts. It ships as a Claude Code plugin, Codex plugin, and pipx/npm CLI, requiring no model keys of its own. It targets developers running Claude Code or Codex who want audit-grade discipline on personal or small-team projects.
