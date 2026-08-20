---
name: "Crewplane"
slug: "crewplane"
layout: "agent.njk"
category: "multiplexer"
maker: "crewplaneai"
license: "Apache-2.0"
url: "https://github.com/crewplaneai/crewplane"
source_code_url: "https://github.com/crewplaneai/crewplane"
source_available: True
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-06-24"
current_release: "2026-08-18"
stars: "33"
language: "Python 3.13+"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: False
subagents: null
hooks: null
plan_mode: True
model_providers: "Claude Code, Codex, Gemini, Copilot CLI, any CLI-based tool; built-in mock provider for deterministic testing"
pricing: "Free / open-source (Apache-2.0)"
install_method: "uv tool install crewplane (recommended); or python -m pip install crewplane; or npm install -g crewplane. Also supports pipx, Homebrew, and an install script. Crewplane does not install or manage provider CLIs or credentials."
docs_url: "https://github.com/crewplaneai/crewplane/blob/master/docs/index.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/crewplaneai/crewplane"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Provider-neutral control plane for human-designed coding-agent workflows; turns AI agent calls into structured, repeatable DAGs defined in Markdown (versioned, reviewable in PRs, shareable); CLI-first design invokes provider CLIs directly instead of wrapping them in vendor SDKs - if a tool has a command line, Crewplane can orchestrate it; saves every input, output, and decision to disk and resumes from validated stage boundaries on failure; mix-and-match providers within a single workflow for provider handoffs; mock mode for zero-config first runs without API keys; optional tmux live dashboard for real-time DAG progress and log tails."
---

Provider-neutral control plane for human-designed coding-agent workflows; turns AI agent calls into structured, repeatable DAGs defined in Markdown (versioned, reviewable in PRs, shareable); CLI-first design invokes provider CLIs directly instead of wrapping them in vendor SDKs - if a tool has a command line, Crewplane can orchestrate it; saves every input, output, and decision to disk and resumes from validated stage boundaries on failure; mix-and-match providers within a single workflow for provider handoffs; mock mode for zero-config first runs without API keys; optional tmux live dashboard for real-time DAG progress and log tails.
