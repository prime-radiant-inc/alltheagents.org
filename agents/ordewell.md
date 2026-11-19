---
name: "Ordewell"
slug: "ordewell"
layout: "agent.njk"
category: "agent"
maker: "ordewell"
license: "Apache-2.0"
url: "https://github.com/ordewell/ordewell"
source_code_url: "https://github.com/ordewell/ordewell"
source_available: "True"
homepage: "https://ordewell.ai"
docs_url: "https://ordewell.ai/docs"
download_url: "https://ordewell.ai/download"
install_method: "curl -fsSL https://ordewell.ai/install.sh | sh (standalone terminal binary); npm install -g ordewell; brew install ordewell/tap/ordewell; desktop app from ordewell.ai/download (dmg/exe/AppImage/deb); VS Code extension from the Marketplace"
platforms:
  - "CLI"
  - "Desktop"
  - "IDE"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "TypeScript"
first_released: "2026-07-31"
current_release: "2026-11-18"
maintained: "active"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
plugin_docs_url: null
config_docs_url: "https://ordewell.ai/docs"
model_providers: "Claude Code, Codex, OpenCode, GitHub Copilot CLI, Qwen Code, Cline, Gemini CLI, Cursor (installed agents bring their own providers); built-in in-process runner on OpenRouter, Anthropic, Google, DeepSeek, Moonshot/Kimi, xAI, or any OpenAI-compatible endpoint via API key"
pricing: "free"
stars: "211"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "Turns one goal into an editable plan graph of tasks that each get their own runner, model and effort — installed coding-agent CLIs run in parallel git worktrees side by side with Ordewell's own in-process runner, which needs only a provider API key, and a task passes only on evidence reported through task_complete."
---

Ordewell grew out of the juggling problem of running several coding agents at once: instead of a wall of tabs, one planner conversation reads the repository, asks what is vague, and writes a plan graph whose tasks carry dependencies, runners, models, effort levels and modes that you can edit before anything runs. Independent tasks execute in parallel, each in its own git worktree, dependent tasks wait, and a merge conflict gets a repair attempt before it reaches you; a task passes only when its agent reports through task_complete or a script exits cleanly, with check-and-fix loops that repeat a check and its fix until it passes or hits a round limit. Two kinds of model do the work: a harness planner (a coding agent planning on its own sign-in) or an API planner on your key, and runners — either installed coding-agent CLIs such as Claude Code, Codex, OpenCode, Copilot CLI, Qwen Code, Cline, Gemini CLI or Cursor, or Ordewell's built-in in-process runner that calls a provider API with the key Ordewell already holds and needs no installed CLI. Autonomy is a dial: by default you approve the plan, answer checkpoints and merge, and turning on autorun with automatic merging lets it run and merge on its own. The same plans drive the desktop app, the terminal UI, a VS Code extension and a command-line workflow, and repository skills share a team's instructions across every runner. It is pre-1.0, Apache-2.0, and intended for developers coordinating multi-agent work on real repositories.
