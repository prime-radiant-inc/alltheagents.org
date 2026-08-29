---
name: "Verdent"
slug: "verdent"
layout: "agent.njk"
category: "agent"
maker: "verdent"
license: "Proprietary"
url: "https://plugins.jetbrains.com/plugin/29473-verdent"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-07-03"
current_release: "2026-07-03"
stars: null
language: "Kotlin"
homepage: "https://verdent.ai"
mcp_support: "True"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "yes"
model_providers: "Anthropic, Google Gemini"
pricing: "subscription"
install_method: "Install from the JetBrains Marketplace"
docs_url: "https://plugins.jetbrains.com/plugin/29473-verdent"
plugin_docs_url: "https://plugins.jetbrains.com/plugin/29473-verdent"
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/29473-verdent"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "All-in-one coding agent orchestrating top-tier AI models; high SWE-bench Verified score"
---

Verdent exists to bring autonomous task execution into IntelliJ-family IDEs for professional developers who need more than autocomplete: given a task, it analyzes the codebase, produces a structured plan for review, and then executes multi-step workflows with approval gates on every consequential action. A subagent architecture handles exploration, verification, and code review separately from the primary agent, and scoped checkpoints make every change reviewable — Review Changes diffs show exactly what a turn altered, with rollback available; bash approval dialogs guard dangerous commands, and temp-directory writes are handled carefully to avoid spurious prompts. Codebase context is gathered locally with bundled ripgrep and fd, so code does not leave the machine without explicit action. Professional developers in IntelliJ-family IDEs use it for refactoring, debugging, test generation, and documentation; it is distributed through the JetBrains Marketplace, requires a Verdent account, and updates every few weeks.
