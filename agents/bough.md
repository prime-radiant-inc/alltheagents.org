---
name: "bough"
slug: "bough"
layout: "agent.njk"
category: "agent"
maker: "andreylukin"
license: "Apache-2.0"
url: "https://github.com/andreylukin/bough"
source_code_url: "https://github.com/andreylukin/bough"
source_available: "True"
homepage: null
docs_url: "https://github.com/andreylukin/bough/blob/main/go/README.md"
download_url: "https://github.com/andreylukin/bough/releases"
install_method: "curl -fsSL https://raw.githubusercontent.com/andreylukin/bough/main/install.sh | sh (macOS and Linux, x86-64 and arm64); or brew tap andreylukin/bough https://github.com/andreylukin/bough && brew install bough; or go build ./cmd/bough (Go 1.27+)"
platforms:
  - "CLI"
  - "Web"
autonomy_level:
  - "agentic"
specialization: "general"
language: "Go"
first_released: "2026-06-18"
current_release: "2026-09-15"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: null
plugin_docs_url: "https://github.com/andreylukin/bough/blob/main/go/docs/PLUGINS.md"
config_docs_url: null
model_providers: "Anthropic, OpenAI, OpenRouter, or Cerebras (your own API keys)"
pricing: "BYOK"
stars: "9"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "The model acts by writing one JavaScript program per step — patch, bash, spawn, and every MCP tool are ordinary functions inside it — so a patch and its test run can be one step that branches on results in code instead of one tool call per round trip."
---

bough is the terminal coding agent its author built to replace Claude Code at work, and its difference is architectural: instead of exposing a list of tools and looping once per call, bough exposes one program runner — the model writes a ```js block that calls tools.view, tools.patch, tools.bash, tools.spawn and any MCP tool as ordinary functions, and what it prints goes back to the model. From the author's own sessions, 52% of programs made more than one tool call and 30% branched or looped on results, work that would otherwise cost a round trip per call. Everything is a plugin — the provider, the loop, the tools, the UI, MCP, hooks and skills are rows in a YAML file that can be swapped or re-mounted mid-session — and sessions are append-only JSONL under ~/.bough/history, so resume, search, and switching models mid-conversation work. A bough session started in a git checkout can write only there; a --project session runs every shell command inside a Linux container (Apple container on macOS, rootless podman on Linux) against git worktrees with per-turn checkpoints and /undo, for work that needs an enforced boundary. The author positions it beside Claude Code, opencode and pi — borrowing their conventions (AGENTS.md, skills, hooks, MCP, subagents) — and it ships a one-person project in daily use with named gaps: no Windows build, no per-turn checkpoints in local sessions, and a shell that runs unsandboxed by default. Developers who want the model to batch and branch its tool use in code, and who like a small replaceable kernel over an application, are the audience.
