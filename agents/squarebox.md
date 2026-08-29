---
name: "squarebox"
slug: "squarebox"
layout: "agent.njk"
category: "other"
maker: "SquareWaveSystems"
license: "MIT"
url: "https://github.com/SquareWaveSystems/squarebox"
source_code_url: "https://github.com/SquareWaveSystems/squarebox"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-04-04"
current_release: "2026-08-13"
stars: "70"
language: "Shell"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "Free/open-source (MIT)"
install_method: "curl -fsSL https://github.com/SquareWaveSystems/squarebox/releases/latest/download/install.sh | bash (Linux/macOS); irm install.ps1 | iex (Windows PowerShell); docker compose up -d (server)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/SquareWaveSystems/squarebox/releases/latest/download/install.sh"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Curated set of modern CLI/TUI tools and AI coding assistants packaged in a single Docker/Podman container with batteries included, one-line install, interactive first-run setup, and sensible defaults. Run the same box anywhere (desktop, VPS, Codespace) and SSH in from any device. Bundles Claude Code, Copilot CLI, Gemini CLI, Codex CLI, opencode, Pi, Oh My Pi."
---

squarebox solves environment drift for people who work across laptops, servers, and cloud shells: a one-line installer pulls a digest-verified image, runs an interactive wizard to pick optional AI assistants (Claude Code, Copilot CLI, Gemini CLI, Codex, opencode, Pi), editors, TUIs, and mise-managed SDKs, then mounts host code from ~/squarebox/workspace with persistent state in a Docker volume. The box suspends on exit and resumes on start, SSH in from any device, and sqrbx-update upgrades in place while sqrbx-rebuild replaces the image wholesale. Security posture is explicit — checksum-pinned downloads, fail-closed digest verification, a documented trust model. It is MIT-licensed and designed to be forked as a personal base image; at roughly 900 MB plus optional toolchains it trades disk for reproducibility.
