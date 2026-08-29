---
name: "Harness Starter Kit"
slug: "harness-starter-kit"
layout: "agent.njk"
category: "other"
maker: "harnessworks"
license: "MIT"
url: "https://github.com/harnessworks/harness-starter-kit"
source_code_url: "https://github.com/harnessworks/harness-starter-kit"
source_available: "True"
platforms: []
first_released: "2026-05-26"
current_release: "2026-06-18"
stars: "111"
language: "Markdown,Python"
homepage: "https://harnessworks.github.io/harness-starter-kit/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "agent-agnostic (Claude Code, Codex, Cursor, Copilot)"
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

harness-starter-kit applies the idea that a repository itself can be engineered to make coding agents fail less often. Rather than shipping a tool, it provides a structured kit — instructions, constraints, feedback loops, memory files, evaluation tasks, and governance documents — plus router prompts (/harness doctor, adopt, review, update, refresh) that a developer pastes into their existing agent, or installs as a Claude Code or Codex plugin for convenience. The kit's core loop converts each recurring agent failure into a durable artifact: an instruction, an automated check, a failure record, a memory entry, or a benchmark task, with a taxonomy separating functional, schema, workflow, boundary, timeout, and hidden-access failures. It takes an explicit measurement stance that harness health and agent effectiveness are separate metrics and ships templates for both. Teams adopting it range from solo developers to platform groups standardizing how agents interact with their repos.
