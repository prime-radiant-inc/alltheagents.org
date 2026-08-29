---
name: "hive"
slug: "hive"
layout: "agent.njk"
category: "multiplexer"
maker: "tt-a1i"
license: "BSL-1.1"
url: "https://github.com/tt-a1i/hive"
source_code_url: "https://github.com/tt-a1i/hive"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-04-19"
current_release: "2026-06-18"
stars: "466"
language: "TypeScript"
homepage: "https://hivehq.dev"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "hosted agents' own providers (Claude Code, Codex, Gemini CLI, OpenCode, Qwen, Cursor, Grok, custom)"
pricing: "open-source"
install_method: "npm install -g @tt-a1i/hive; then run hive"
docs_url: "https://hivehq.dev/en/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@tt-a1i/hive"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Local-first browser workbench that runs multiple CLI coding agents (Claude Code, Codex, Gemini, OpenCode, Qwen, etc.) as a visible team via real PTY processes. An Orchestrator plans and delegates to workers using an injected 'team' command; shared markdown task graph stored in .hive/tasks.md. Features Auto-staff, experimental Workflows, optional end-to-end encrypted remote phone access, and PWA install support. Template marketplace of community-maintained prompt libraries."
---

hive turns a local machine into a supervised team of coding agents. A browser-based workbench spawns an Orchestrator agent and worker agents — Claude Code, Codex, Gemini CLI, OpenCode, Qwen, or custom CLIs — each as a real PTY process visible in the UI, with a team command injected into their shells so the Orchestrator dispatches tasks and workers report progress through a shared markdown task graph at .hive/tasks.md. Workers take role presets (coder, reviewer, tester, custom), an experimental auto-staff mode spins up temporary workers as needed, and sessions persist across disconnects with background PTY preservation. Team memory and a task-graph editor with conflict handling keep the plan inspectable and editable by hand. It targets developers who want to watch and steer a multi-agent build locally, running in alpha with an optional end-to-end-encrypted remote gateway.
