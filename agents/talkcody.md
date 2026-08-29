---
name: "talkcody"
slug: "talkcody"
layout: "agent.njk"
category: "agent"
maker: "talkcody"
license: "MIT"
url: "https://github.com/talkcody/talkcody"
source_code_url: "https://github.com/talkcody/talkcody"
source_available: "True"
platforms: []
first_released: "2025-11-07"
current_release: "2026-05-25"
stars: "464"
language: "TypeScript, Rust"
homepage: "https://talkcody.com"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "n/a"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Google, Ollama, LM Studio"
pricing: "Free / open-source; can leverage ChatGPT Plus/Pro and GitHub Copilot subscriptions"
install_method: "Download installer (macOS, Windows, Linux AppImage) or build from source"
docs_url: "https://www.talkcody.com/docs/introduction/quick-start"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.talkcody.com/docs/introduction/client-downloads"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Free, open-source AI coding agent with four-level parallelism (project, task, agent, tool), 100% local storage, offline capable, no vendor lock-in, with an agents & skills marketplace"
---

TalkCody is an open-source desktop coding agent aimed at users who want agent capability without sending code to a hosted service or adopting a single vendor. Built on Rust/Tauri with a React frontend, it runs tasks with parallelism at four levels — multiple projects, multiple tasks per project, multiple agents per task, and concurrent tool calls — and keeps all sessions, indexes, and settings on local disk, which also enables offline use with Ollama or LM Studio. Agent behavior is extensible through an agents-and-skills marketplace where community agents and workflows are downloaded and shared, and MCP servers extend the tool surface. Model access is deliberately flexible: OpenAI, Anthropic, Google, GitHub Copilot, or existing ChatGPT subscriptions, plus local models for fully offline operation. The installers cover macOS (both architectures), Windows, and Linux, and the project documents itself through talkcody.com/docs. Privacy-conscious individual developers and small teams are the primary users.
