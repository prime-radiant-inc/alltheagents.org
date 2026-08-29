---
name: "context-engineering-intro"
slug: "context-engineering-intro"
layout: "agent.njk"
category: "other"
maker: "coleam00"
license: "MIT"
url: "https://github.com/coleam00/context-engineering-intro"
source_code_url: "https://github.com/coleam00/context-engineering-intro"
source_available: "Yes"
platforms: []
first_released: "2025-07-02"
current_release: "2026-03-16"
stars: "13787"
language: "Python (examples)"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a (uses Claude Code custom slash commands, not a plugin)"
subagents: "no"
hooks: "no"
plan_mode: "no (has a PRP workflow with planning steps, not a formal plan mode)"
model_providers: "Anthropic (via Claude Code); strategy applies to any AI coding assistant"
pricing: "open-source (MIT)"
install_method: "binary (git clone)"
docs_url: "https://docs.anthropic.com/en/docs/claude-code"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/coleam00/context-engineering-intro"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "A comprehensive template for Context Engineering — a methodology that provides AI coding assistants with structured context (rules, examples, documentation, validation) via a PRP (Product Requirements Prompt) workflow, claiming to be 10x better than prompt engineering and 100x better than vibe coding."
---

Agents fail most often not from weak models but from missing context, and prompt tweaks do not fix structural gaps. This repository packages a context-engineering workflow as a cloneable template: a developer writes a feature request in INITIAL.md, runs a /generate-prp command that researches the codebase and assembles a PRP (Product Requirements Prompt) with relevant documentation and validation criteria, then runs /execute-prp to implement it through validation gates that iterate until tests pass. Global rules templates in CLAUDE.md, feature-request formats, and example code patterns round out the kit, and a multi-agent variant exists for larger work. The templates target Claude Code but the method ports to other assistants, and adoption means copying the templates into a project rather than installing a tool. It is used by teams institutionalizing disciplined agent workflows.
