---
name: "Melty"
slug: "melty"
layout: "agent.njk"
category: "agent"
maker: "meltylabs"
license: "MIT"
url: "https://github.com/meltylabs/melty"
source_code_url: "https://github.com/meltylabs/melty"
source_available: "True"
platforms:
  - "IDE"
  - "Desktop"
first_released: "2024-09-02"
current_release: "2024-11-14"
stars: null
language: "TypeScript"
homepage: "https://docs.google.com/forms/d/e/1FAIpQLSc6uBe0ea26q7Iq0Co_q5fjW2nypUl8G_Is5M_6t8n7wZHuPA/viewform"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "Early access waitlist; build from source per CONTRIBUTING.md"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
what_makes_it_special: "Every chat message is automatically a git commit — enabling revert, branch, reset, and squash of AI conversations; watches changes in real-time like a pair programmer; integrates with compiler, terminal, debugger, Linear, and GitHub; first AI editor designed for big multi-file changes."
---

Melty treated the AI coding session as a first-class git object: because each message landed as a commit, a bad suggestion could be reverted exactly like a bad merge, and multi-file changes could be squashed into clean history before leaving the editor. Built as a VS Code fork, it watched changes in real time like a pair programmer and integrated with the compiler, terminal, debugger, Linear, and GitHub, targeting the large cross-file refactors that chat-only assistants handled poorly. The MIT-licensed repository drew roughly five thousand stars and, by its own README, was writing about half of its own code. Development stopped in November 2024 after the team shifted toward a packaged early-access product that never broadly shipped; the commit-per-message idea remains its lasting contribution to editor design.
