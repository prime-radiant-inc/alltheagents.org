---
name: "dmux"
slug: "dmux"
layout: "agent.njk"
category: "multiplexer"
maker: "standardagents"
license: "MIT"
url: "https://github.com/standardagents/dmux"
source_code_url: "https://github.com/standardagents/dmux"
source_available: "True"
platforms: []
first_released: "2025-08-20"
current_release: "2026-08-16"
stars: "1744"
language: "TypeScript / Node.js"
homepage: "https://dmux.ai"
mcp_support: "no - .playwright-mcp dir present but not a documented feature"
plugin_support: "no - extensibility via lifecycle hooks only"
claude_code_plugin: "n/a - Claude Code is a first-class supported agent, not a plugin target"
subagents: "no"
hooks: "yes - lifecycle hooks (.dmux-hooks/ dir): worktree create, pre-merge, post-merge"
plan_mode: "partial - 'goal launches' optionally start agents in goal mode"
model_providers: "API-key providers, OpenAI-compatible endpoints, Codex/ChatGPT login, Grok Build/SpaceXAI login"
pricing: "open-source"
install_method: "npm"
docs_url: "https://dmux.ai"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "tmux-based multiplexer for parallel AI coding agents in isolated git worktrees. Each agent gets its own tmux pane + worktree + branch, preventing file conflicts. Agent-agnostic with 12+ supported CLIs (Claude Code, Codex, OpenCode, Gemini CLI, etc.). Durable/resumeable terminals, smart merging with GitHub PR creation, AI-generated branch/commit names, multi-project sessions, and a built-in file browser."
---

dmux treats a coding task as a tmux pane with an isolated worktree: press n, type the prompt, pick one or more agents, and it creates the branch, worktree, and agent launch, then merges or opens a GitHub PR when the work finishes. It stays agent-agnostic — Claude Code, Codex, OpenCode, Cline, Gemini, Qwen, Amp, Cursor CLI, Copilot CLI, Crush and more — and never intercepts the agent's protocol, so MCP servers and permission flows keep working. Durable terminals resume the tracked agent conversation when a pane is recreated, and lifecycle hooks run scripts around worktree creation and merges. Solo developers running several tasks at once are the target user.
