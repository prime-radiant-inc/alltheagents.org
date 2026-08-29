---
name: "construct"
slug: "construct"
layout: "agent.njk"
category: "multiplexer"
maker: "construct-worlds"
license: "MIT"
url: "https://github.com/construct-worlds/construct"
source_code_url: "https://github.com/construct-worlds/construct"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-05-16"
current_release: "2026-08-19"
stars: "15"
language: "Rust"
homepage: "https://discord.gg/89fPgTKsRF"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: null
model_providers: "OpenAI, Anthropic, Google Gemini, xAI Grok, Ollama, ChatGPT (Codex OAuth), Claude (Claude Code CLI)"
pricing: "open-source"
install_method: "curl -fsSL https://raw.githubusercontent.com/construct-worlds/construct/main/install.sh | sh (or cargo build --workspace from source)"
docs_url: "https://github.com/construct-worlds/construct/tree/main/docs"
plugin_docs_url: "https://github.com/construct-worlds/construct/blob/main/docs/plugins.md"
config_docs_url: "https://github.com/construct-worlds/construct/blob/main/docs/configuration.md"
download_url: "https://github.com/construct-worlds/construct/releases"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Terminal-native agentic development environment (ADE) — 'tmux for agent fleets.' Manages multiple AI coding agent sessions (Codex, Claude Code, OpenCode, Antigravity, Grok, Muse, Prime Agent, smith) from the terminal. Sessions persist in a daemon (survives SSH drops/sleep). Features session branching/forking (Lineage), executable Markdown Playbooks, agent-to-agent orchestration, generative widgets, remote phone/browser control, and an extensible JSON-RPC harness protocol. Single Rust binary."
---

Agent CLI sessions die when SSH connections drop or laptops sleep, and running several agents in parallel means juggling terminal windows with no shared history. Construct runs a background daemon that owns every agent session - Codex, Claude Code, OpenCode, Antigravity, Grok, and others - persisting state and serving a terminal UI that reattaches with full scrollback after disconnection. Sessions form a lineage tree: users fork a session, even across different harnesses, to try approaches in parallel and merge the results back. Collaborative Markdown playbooks, agent-generated UI widgets, MCP-based agent-to-agent task handoff, and an ACP server round out the environment, while the wrapped agent CLIs remain separately installed and authenticated. Platform engineers juggling multiple agent sessions across local and remote environments are the target users.
