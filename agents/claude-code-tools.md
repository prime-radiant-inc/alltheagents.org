---
name: "Claude Code Tools"
slug: "claude-code-tools"
layout: "agent.njk"
category: "other"
maker: "pchalasani"
license: "MIT"
url: "https://github.com/pchalasani/claude-code-tools"
source_code_url: "https://github.com/pchalasani/claude-code-tools"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2025-07-30"
current_release: "2026-08-19"
stars: "1979"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "yes"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "BYOK (alt-llm-providers integration)"
pricing: "open-source"
install_method: "pip"
docs_url: "https://pchalasani.github.io/claude-code-tools/"
plugin_docs_url: "https://pchalasani.github.io/claude-code-tools/"
config_docs_url: "https://pchalasani.github.io/claude-code-tools/"
download_url: "https://pypi.org/project/claude-code-tools/"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Practical productivity toolkit spanning multiple CLI coding agents (Claude Code, Codex-CLI, and similar), offering tools like aichat-search, voxtype voice input, tmux-cli, amux, agent-tunnel, session porting between Claude and Codex, inter-agent messaging, Google Docs/Sheets integrations, and safety hooks."
---

The toolkit solves context loss and operational friction across CLI agents: histories and sessions are trapped inside each tool, so aichat-search indexes them for retrieval, and the session-porting tool converts a Claude Code conversation into a Codex session and vice versa, letting work migrate between agents mid-task. Around that core, voxtype adds voice input, amux runs multiple agents concurrently, agent-tunnel exposes remote access, and github-watch wakes agents when PR comments arrive. Components are pip/crates-installable and integrate through Claude Code's plugin, hook, and skill mechanisms rather than replacing the agents. Developers running multi-agent workflows use it; it is MIT-licensed and actively maintained with roughly two thousand stars.
