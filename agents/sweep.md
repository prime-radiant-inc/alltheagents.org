---
name: "Sweep"
slug: "sweep"
layout: "agent.njk"
category: "agent"
maker: "sweepai"
license: "MIT (Free Software) + Enterprise Edition (EE License)"
url: "https://github.com/sweepai/sweep"
source_code_url: "https://github.com/sweepai/sweep"
source_available: "True"
platforms:
  - "IDE"
  - "Web"
first_released: "2023-06-14"
current_release: "2025-09-18"
stars: "7700"
language: "Python"
homepage: "https://sweep.dev"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI"
pricing: "freemium"
install_method: "jetbrains"
docs_url: "https://sweep.dev"
plugin_docs_url: "https://plugins.jetbrains.com/plugin/26860-sweep-ai"
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/26860-sweep-ai"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Originally a GitHub-app AI coding assistant; pivoted to an AI coding assistant for JetBrains IDEs, distributed as a JetBrains plugin. Dual-licensed: MIT for the free software portion, EE License for the enterprise portion."
---

Sweep began in 2023 as a GitHub app that behaved like a junior developer: assign it an issue and it planned changes, edited files across the repository, and opened a draft pull request for review. That workflow ran on GPT-4 with a repo-map and sandboxed validation loop, and the project drew roughly 7.7k stars as one of the first open-source autonomous-PR agents. The team subsequently pivoted to building an AI coding assistant distributed as a JetBrains Marketplace plugin, leaving the original GitHub-app codebase without active development while sweep.dev now points at the plugin. The repository remains available under a dual license — MIT for the free components with an Enterprise Edition license covering commercial parts — and is still referenced as a reference implementation of issue-to-PR automation. JetBrains users wanting an agent inside IntelliJ-based IDEs are its current audience.
