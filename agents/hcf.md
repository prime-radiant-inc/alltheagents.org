---
name: "hcf"
slug: "hcf"
layout: "agent.njk"
category: "agent"
maker: "markshust"
license: "MIT"
url: "https://github.com/markshust/hcf"
source_code_url: "https://github.com/markshust/hcf"
source_available: True
platforms:
  - "Autonomous"
first_released: "2026-03-01"
current_release: "2026-08-18"
stars: "57"
language: "Markdown, YAML, Shell"
homepage: null
mcp_support: False
plugin_support: True
claude_code_plugin: True
subagents: True
hooks: True
plan_mode: True
model_providers: null
pricing: null
install_method: "/plugin marketplace add markshust/hcf then /plugin install hcf@hcf then /reload-plugins"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Separates planning (human-in-the-loop) from execution (fully autonomous parallel TDD workers); auto-detects task dependencies for parallel execution; pure TDD (requirements map directly to test names); convention-over-configuration pipeline with agents self-enrolling via frontmatter."
---

Separates planning (human-in-the-loop) from execution (fully autonomous parallel TDD workers); auto-detects task dependencies for parallel execution; pure TDD (requirements map directly to test names); convention-over-configuration pipeline with agents self-enrolling via frontmatter.
