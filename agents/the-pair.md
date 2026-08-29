---
name: "the-pair"
slug: "the-pair"
layout: "agent.njk"
category: "agent"
maker: "timwuhaotian"
license: "Apache-2.0"
url: "https://github.com/timwuhaotian/the-pair"
source_code_url: "https://github.com/timwuhaotian/the-pair"
source_available: "True"
platforms:
  - "Desktop"
first_released: "2026-03-22"
current_release: "2026-08-11"
stars: "354"
language: "TypeScript, Rust"
homepage: "https://apps.timwuhaotian.dev/"
mcp_support: "no"
plugin_support: "False"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "opencode, Anthropic (Claude Code), OpenAI (Codex), Google (Gemini/Antigravity), Kimi, Ollama"
pricing: "Free/open-source (user pays own AI provider API costs; zero cost with Ollama local models)"
install_method: "Download from GitHub Releases (.zip macOS / .exe Windows / .AppImage Linux); or build from source: git clone, npm install, npm run build:mac|win|linux (requires Node.js 22.22+ and Rust)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/timwuhaotian/the-pair/releases"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Dual-agent cross-validation desktop app where a read-only Mentor agent plans and reviews everything a separate Executor agent produces, catching AI hallucinations before they reach the codebase. Model-agnostic: mix and match any providers (e.g., Claude as Mentor + Codex as Executor)."
---

The Pair addresses a specific failure mode of single-agent coding tools: one model that both writes code and reviews it will often approve its own hallucinations. Its desktop app (Tauri 2, Rust + React) runs two roles on every task — a Mentor agent with read-only access that plans and reviews, and an Executor agent that writes code and runs commands — looping through mentoring, execution, and review cycles until work completes or a flat 20-iteration default triggers a pause for human inspection. Because the roles are CLI-backed, any combination of opencode, Claude Code, Codex, Gemini/Antigravity, Kimi, or local Ollama models can be assigned per role, letting users cross-validate with different model families; quality gates, stall detection, per-agent resource monitoring, and git-diff tracking round out the harness. It is free Apache-2.0 software for macOS, Windows, and Linux, with a pair-code CLI for terminal use, and users pay only their own provider costs. Developers burned by hallucinated single-agent edits are the intended users.
