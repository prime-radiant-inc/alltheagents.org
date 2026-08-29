---
name: "hcf"
slug: "hcf"
layout: "agent.njk"
category: "agent"
maker: "markshust"
license: "MIT"
url: "https://github.com/markshust/hcf"
source_code_url: "https://github.com/markshust/hcf"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2026-03-01"
current_release: "2026-08-18"
stars: "57"
language: "Markdown, YAML, Shell"
homepage: null
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Claude Code (any supported model)"
pricing: "open-source"
install_method: "/plugin marketplace add markshust/hcf then /plugin install hcf@hcf then /reload-plugins"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/markshust/hcf"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Separates planning (human-in-the-loop) from execution (fully autonomous parallel TDD workers); auto-detects task dependencies for parallel execution; pure TDD (requirements map directly to test names); convention-over-configuration pipeline with agents self-enrolling via frontmatter."
---

hcf (Halt and Catch Fire) is a Claude Code plugin that imposes a two-phase discipline on agent-driven development. During planning, a plan-create skill explores the codebase, asks clarifying questions, and decomposes the work into task files with explicit dependencies, where each requirement is written directly as a test name in strict red-green-refactor style. Execution then runs through plan-orchestrate, which reads the dependency graph and runs tasks in parallel batches rather than sequentially, with each task required to pass tests before completion; failures retry three times before being blocked while others continue. A pipeline of eight hook points lets agents enroll by declaring a phase in their frontmatter, with built-in plan-review and code-standards enforcement available. State persists in plan files so interrupted runs resume cleanly, and the plugin never pushes or opens PRs without permission.
