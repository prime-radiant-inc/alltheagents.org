---
name: "Harness Starter Kit"
slug: "harness-starter-kit"
layout: "agent.njk"
category: "agent"
maker: "harnessworks"
license: "MIT"
url: "https://github.com/harnessworks/harness-starter-kit"
source_code_url: "https://github.com/harnessworks/harness-starter-kit"
source_available: True
platforms: []
first_released: "2026-05-26"
current_release: "2026-06-18"
stars: "111"
language: "Markdown,Python"
homepage: "https://harnessworks.github.io/harness-starter-kit/"
mcp_support: True
plugin_support: True
claude_code_plugin: True
subagents: True
hooks: null
plan_mode: null
model_providers: null
pricing: "Free/open-source (MIT)"
install_method: "Prompt-first (paste adoption prompt into coding agent); optional Python installer (python scripts/apply_harness.py --target . --profile generic --dry-run); or native plugin install for Codex (codex plugin marketplace add) or Claude Code (claude plugin install harness-agent-skills@harnessworks)"
docs_url: "https://harnessworks.github.io/harness-starter-kit/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/harnessworks/harness-starter-kit"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Prompt-first starter kit that reframes the problem from 'prompt engineering the agent' to 'engineering the repository'; converts recurring agent failures into durable artifacts (instruction, constraint, check, memory record, drift check) for a continuous improvement loop grounded in repository evidence; separates failure types (functional, schema, workflow, boundary, timeout, hidden-access) instead of reducing to pass/fail; ships runtime-native skills for Codex and Claude Code; supports read-only reviewer subagent via /harness review sub-agent."
---

Prompt-first starter kit that reframes the problem from 'prompt engineering the agent' to 'engineering the repository'; converts recurring agent failures into durable artifacts (instruction, constraint, check, memory record, drift check) for a continuous improvement loop grounded in repository evidence; separates failure types (functional, schema, workflow, boundary, timeout, hidden-access) instead of reducing to pass/fail; ships runtime-native skills for Codex and Claude Code; supports read-only reviewer subagent via /harness review sub-agent.
