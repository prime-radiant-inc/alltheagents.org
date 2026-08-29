---
name: "shotgun"
slug: "shotgun"
layout: "agent.njk"
category: "agent"
maker: "shotgun-sh"
license: "MIT"
url: "https://github.com/shotgun-sh/shotgun"
source_code_url: "https://github.com/shotgun-sh/shotgun"
source_available: "yes"
platforms: []
first_released: "2025-08-05"
current_release: "2026-06-02"
stars: "684"
language: "Python"
homepage: "https://shotgun.sh/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "yes"
model_providers: "OpenAI, Anthropic, Google Gemini"
pricing: "freemium"
install_method: "pip"
docs_url: "https://shotgun.sh"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Spec-driven development CLI/TUI that reads your entire codebase (tree-sitter indexing), plans features upfront, and splits them into staged PRs with file-by-file instructions for AI coding agents (Cursor, Claude Code, Codex). Multi-phase structured workflow (Research, Specify, Plan, Tasks, Export) with dedicated sub-agents per phase managed by a Router. Starts with research to discover existing solutions/patterns before writing specs, preventing duplicate work. Exports tool-agnostic AGENTS.md files. Two execution modes: Planning (default, with checkpoints) and Drafting (runs full plan). BYOK or Shotgun credits. Install via uvx/uv."
---

Large features derail coding agents because context arrives piecemeal; Shotgun front-loads the work by reading the entire repository, researching before specifying, and producing a full plan split into staged pull requests with file-by-file instructions. Internally a Router dispatches specialized sub-agents through Research, Specify, Plan, Tasks, and Export phases, and the user controls exactly two execution modes — planning with checkpoints, or drafting end-to-end. The index lives in ~/.shotgun-sh, telemetry is minimal and anonymous, and BYOK covers OpenAI, Anthropic, and Gemini or prepaid Shotgun credits. It installs via uvx as a Python TUI/CLI, integrates Context7 experimentally for current library docs, and targets teams handing substantial features to Cursor, Codex, or Claude Code who need the plan to survive the handoff.
