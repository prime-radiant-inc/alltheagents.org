---
name: "Logonomic"
slug: "logonomic"
layout: "agent.njk"
category: "multiplexer"
maker: "Varinomics"
license: "Proprietary"
url: "https://varinomics.com/logonomic/"
source_code_url: null
source_available: "False"
homepage: null
docs_url: "https://varinomics.com/docs/logonomic/"
download_url: "https://varinomics.com/logonomic/downloads/"
install_method: "Windows installer (.exe) or portable .zip; Linux .deb, AppImage, or .run installer; macOS portable .zip (preview) — from the downloads page"
platforms:
  - "Desktop"
autonomy_level: []
specialization: "general"
language: null
first_released: "2026-11-11"
current_release: "2026-11-11"
maintained: "active"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: null
subagents: "True"
hooks: "False"
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "Brings no models: runs the coding CLIs you already have installed — Codex, Claude Code, Antigravity, Kimi Code, OpenCode, Grok Build, Qwen Code — each keeping its existing accounts, models, and configuration"
pricing: "freemium"
stars: null
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A C++/Qt desktop workspace that groups coding-agent sessions by repository and puts code changes, Git history, and CI results beside each conversation, with commits linked back to the session that made them; a phone Companion mirrors and controls the running sessions, and the Soter crash-recovery process keeps terminals alive when the main window dies."
---

Logonomic is built for developers who run several coding agents across many repositories and lose track of what needs attention. The desktop workspace groups terminal sessions of coding CLIs by repository — Codex, Claude Code, Antigravity, Kimi Code, OpenCode, Grok Build, and Qwen Code, each installed and signed in separately with its own accounts and models — and surrounds them with the repository's Git history, CI results from GitHub and GitLab, and a codebase overview. Agents stamp their commits with a session trailer, so a commit opens the conversation behind it and a session can be resumed; a review pane shows the diff beside the agent conversation that produced it. Coordination goes both ways: 'Continue in' carries a discussion into a different CLI, delegation starts one-shot implementation or read-only-review child sessions in a specified checkout, and peer messages let running sessions report results or ask each other questions. The Android/iOS Companion shows the same live sessions on a phone to answer questions and approve changes, and a separate terminal process (Soter) keeps sessions alive through a main-window crash. Varinomics, a Cyprus company, develops it in C++ with Qt; the application is proprietary with several core components published open-source, and the free edition is complemented by a perpetual Logonomic Pro licence (self-managed GitLab, multiple Companion devices, higher task limits).
