---
name: "Mistral Vibe"
slug: "mistral-vibe"
layout: "agent.njk"
category: "agent"
maker: "mistralai"
license: "Apache-2.0"
url: "https://github.com/mistralai/mistral-vibe"
source_code_url: "https://github.com/mistralai/mistral-vibe"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-12-08"
current_release: "2026-08-18"
stars: null
language: "Python"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Mistral (default); Mistral-compatible domains/deployments"
pricing: null
install_method: "curl -LsSf https://mistral.ai/vibe/install.sh | bash"
docs_url: "https://github.com/mistralai/mistral-vibe/blob/main/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
what_makes_it_special: "Mistral's official open-source CLI agent with subagents, hooks (pre_tool/post_tool/post_agent), Skills system following Agent Skills specification, voice mode, git worktree integration, multimodal image support, OpenTelemetry tracing, Agent Client Protocol (ACP) for IDE integration, and programmatic mode with cost/token/turn budgets."
---

Mistral Vibe gives the Mistral ecosystem a first-party terminal agent comparable to Claude Code: the model plans with a todo list, edits and patches files, runs shell commands, and searches with ripgrep under per-profile permission approval, with compaction managing context across long sessions. Delegation runs through a task tool whose subagents work independently — including a read-only explore agent for codebase reconnaissance — and custom subagents are defined as agent-type config files that inherit the parent's hooks. Hooks themselves are shell commands wired at pre_tool, post_tool, and post_agent points, able to deny or fully rewrite tool inputs and outputs. Skills follow the agentskills.io specification, adding tools and user-invocable slash commands from SKILL.md directories, and MCP servers attach over stdio or streamable HTTP with static or OAuth auth. Programmatic mode caps cost, tokens, and turns for scripted CI use, and Agent Client Protocol integration reaches Zed and VS Code. Developers use it interactively in the terminal and teams run it headless in CI against Mistral models.
