---
name: "Packnplay"
slug: "packnplay"
layout: "agent.njk"
category: "other"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/packnplay"
source_code_url: "https://github.com/2389-research/packnplay"
source_available: "True"
platforms:
  - "CLI"
first_released: null
current_release: null
stars: "0"
language: "Go"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "go install"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Containerization wrapper that launches coding agents (Claude Code, Codex, Gemini) inside isolated Docker containers with automated git worktree and dev container management. Handles credential mounting (git, SSH, GitHub CLI, GPG, npm, AWS), port mapping, macOS Keychain integration, and devcontainer.json support. No introspection or access control — sandboxed execution only."
---

Packnplay is a containerization wrapper that launches coding agents — Claude Code, Codex, Gemini — inside isolated Docker containers so they run sandboxed rather than on the host. It automates the tedious parts of that setup: creating a git worktree, provisioning a dev container, mounting credentials (git, SSH, GitHub CLI, GPG, npm, AWS), mapping ports, and integrating with macOS Keychain and devcontainer.json. It deliberately does no introspection or access control — it is a sandboxed execution environment, not a supervisor — and the agent loop belongs entirely to the agent it wraps. The audience is developers who want their coding agent to run in a clean, credential-equipped container without hand-rolling the Docker and worktree plumbing each time.
