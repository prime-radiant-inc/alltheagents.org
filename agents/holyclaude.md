---
name: "HolyClaude"
slug: "holyclaude"
layout: "agent.njk"
category: "other"
maker: "CoderLuii"
license: "MIT"
url: "https://github.com/CoderLuii/HolyClaude"
source_code_url: "https://github.com/CoderLuii/HolyClaude"
source_available: "Yes"
platforms:
  - "CLI"
  - "Web"
  - "Autonomous"
first_released: "2026-03-22"
current_release: "2026-08-16"
stars: "2505"
language: "Shell"
homepage: "https://holyclaude.coderluii.dev"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "Anthropic, Google, OpenAI, OpenRouter, Ollama, BYOK"
pricing: "open-source"
install_method: "docker"
docs_url: "https://github.com/CoderLuii/HolyClaude/blob/master/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/CoderLuii/HolyClaude"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Containerized AI development workstation bundling Claude Code + 8 AI CLIs + headless browser (Chromium/Playwright) + 50+ dev tools, all pre-configured and ready via one `docker compose up` command."
---

HolyClaude packages a full AI development environment into a single docker compose command. The container runs the genuine Claude Code CLI behind a browser-based web UI, alongside eight other AI CLIs, a headless Chromium with Playwright for browser tasks, and roughly fifty preconfigured development tools, so an agent can edit code, run tests, and drive a browser without host setup. The project's value is in the operational details it has already solved: correct shared-memory sizing for Chromium, UID/GID mapping for volume permissions, SQLite locking on NAS mounts, and supervision via s6-overlay, plus Apprise notifications when agents finish. It uses the user's own Anthropic subscription or API keys directly rather than proxying them, ships multi-arch images with a slim variant, and targets self-hosting enthusiasts running on macOS, Linux, WSL2, and NAS hardware.
