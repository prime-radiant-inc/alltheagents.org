---
name: "Tonkotsu"
slug: "tonkotsu"
layout: "agent.njk"
category: "multiplexer"
maker: "Tonkotsu"
license: null
url: "https://tonkotsu.ai"
source_code_url: null
source_available: null
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: "https://tonkotsu.ai"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Anthropic (Claude Code, via the user's existing Anthropic plan)"
pricing: "free"
install_method: null
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://tonkotsu.ai"
maintained: "dormant"
sources:
  - "toolify"
what_makes_it_special: "A GUI that manages parallel Claude Code agents through a structured plan-code-verify document: Tonkotsu drafts a plan for human sign-off, delegates dozens of coding tasks at once across multiple repos with task dependencies, and runs test plans and code review in one place — with no commits until the human approves. Codes in isolated repo clones on the developer's own machine; free during early access, SOC 2 Type I audited."
---

Tonkotsu addresses the monitoring burden of running many Claude Code agents at once: unattended terminals stall, merge into each other, and require constant babysitting. Its workflow moves planning into a shareable document — the human approves or edits the plan, then Tonkotsu delegates the resulting tasks to parallel Claude Code sessions across multiple repositories, respecting declared dependencies and running test plans before review. Nothing is committed until the developer approves, and all execution happens in isolated clones on the local machine rather than a hosted environment. Developers managing concurrent features use it to run agent work with intermediate-level-team turnaround; the site is currently returning 503, with the last archived captures in April 2026.
