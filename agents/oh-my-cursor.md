---
name: "oh-my-cursor"
slug: "oh-my-cursor"
layout: "agent.njk"
category: "other"
maker: "tmcfarlane"
license: "MIT"
url: "https://github.com/tmcfarlane/oh-my-cursor"
source_code_url: "https://github.com/tmcfarlane/oh-my-cursor"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-02-07"
current_release: "2026-07-02"
stars: "107"
language: "Markdown config, shell scripts"
homepage: null
mcp_support: "no"
plugin_support: "False"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Cursor model pool (composer-2.5-fast, claude-opus-4.8-thinking-high, gemini-3.1-pro, claude-4.6-opus-high-thinking, claude-4.6-sonnet-medium-thinking, claude-fable-5-thinking-high, gpt-5.3-codex-high-fast, gpt-5.5-medium, kimi-k2.5)"
pricing: "Free / open source"
install_method: "curl -fsSL https://raw.githubusercontent.com/tmcfarlane/oh-my-cursor/main/install.sh | bash (macOS/Linux); irm https://raw.githubusercontent.com/tmcfarlane/oh-my-cursor/main/install.ps1 | iex (Windows)"
docs_url: "https://github.com/tmcfarlane/oh-my-cursor/tree/main/docs"
plugin_docs_url: null
config_docs_url: "https://github.com/tmcfarlane/oh-my-cursor/tree/main/docs"
download_url: "https://github.com/tmcfarlane/oh-my-cursor"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Avatar: The Last Airbender-themed 8-agent team; pure Markdown config with zero runtime/CLI wrapper; per-agent model routing; hooks that deterministically block destructive commands and bad commits; Cactus Juice swarm mode (up to 10 parallel workers); cross-tool support (Cursor/Claude Code/Codex)"
---

oh-my-cursor turns Cursor's native subagent system into a themed eight-agent team using only Markdown configuration files, hooks, and slash commands — no plugin system or external runtime. Each specialist agent routes to a specific model chosen for its role, such as a multimodal model for image generation work. An orchestrator rule keeps the root thread dispatching while specialists execute, and cactus-juice swarm mode spawns up to ten parallel workers. Hooks deterministically block destructive shell commands and low-quality commits, while a permissions policy reduces approval prompts. The same files can also install for Claude Code and Codex, and a validation culture with per-build model-slug verification guards against Cursor's silent model downgrade behavior.
