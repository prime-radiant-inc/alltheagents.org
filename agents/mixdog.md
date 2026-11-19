---
name: "Mixdog"
slug: "mixdog"
layout: "agent.njk"
category: "agent"
maker: "tribgames"
license: "Apache-2.0"
url: "https://github.com/tribgames/mixdog"
source_code_url: "https://github.com/tribgames/mixdog"
source_available: "True"
homepage: "https://mixdog.ai/"
docs_url: "https://github.com/tribgames/mixdog#readme"
download_url: "https://github.com/tribgames/mixdog/releases"
install_method: "Desktop download from GitHub Releases (Windows .exe, macOS .dmg Apple Silicon/Intel, Linux AppImage/.deb; installers code-signed); or npm install -g mixdog (Node.js 22.19+/24+); then sign in with a ChatGPT, Claude, Grok, or Muse Code account, or paste an API key"
platforms:
  - "Desktop"
  - "CLI"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "JavaScript"
first_released: "2026-06-25"
current_release: "2026-11-03"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "False"
plugin_docs_url: null
config_docs_url: null
model_providers: "Anthropic (API keys or Claude OAuth), OpenAI (API keys or ChatGPT/Codex OAuth), Google Gemini, xAI (Grok OAuth), Muse Code (Meta OAuth), OpenRouter, DeepSeek, OpenCode Go, and a built-in Local Provider (Windows x64 with NVIDIA GPU)"
pricing: "BYOK"
stars: "256"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "An open-source desktop coding agent that mixes models by role — a strong lead model plans while cheaper models search, edit, and review in parallel — with an auto-reasoning-effort judge (a 150 MB model running locally on the CPU) that sizes each message and tool step in about 0.1 s, and published Terminal-Bench 2.1 runs reporting large token savings at the same success rate."
---

Mixdog is a desktop coding agent built around spending tokens where they matter: a lead model steers each session while cheaper models do the searching, editing, and reviewing, sessions scale from one model to a swarm via orchestration modes (none, focused, balanced, swarm), and every message and tool step is assigned a reasoning effort by a small local judge model, on by default. The workspace around the loop is a full desktop app — editor, terminals, Git and GitHub integration, code graph, language servers — plus bots with their own models and permissions, group rooms where they talk, goals and schedules and webhooks that keep it working unattended, and end-to-end-encrypted continuation from a phone. It verifies its claims in public: Terminal-Bench 2.1 runs against Codex CLI and Claude Code, with every verdict, log, and script published in the repo. Users sign in with a Claude, ChatGPT, Grok, or Muse Code subscription they already have, or paste an API key, or run local models on their own GPU; the Windows app is the primary target, with macOS and Linux builds alongside. The Apache-2.0 project is developed by tribgames and actively maintained, with a detailed public changelog.
