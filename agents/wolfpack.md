---
name: "Wolfpack"
slug: "wolfpack"
layout: "agent.njk"
category: "multiplexer"
maker: "almogdepaz"
license: "MIT"
url: "https://github.com/almogdepaz/wolfpack"
source_code_url: "https://github.com/almogdepaz/wolfpack"
source_available: True
platforms:
  - "CLI"
  - "Web"
  - "Desktop"
  - "Autonomous"
first_released: "2026-01-30"
current_release: "2026-08-19"
stars: "37"
language: "TypeScript, JavaScript (Bun), Rust (PTY broker)"
homepage: "https://get-wolfpack.netlify.app/"
mcp_support: null
plugin_support: True
claude_code_plugin: False
subagents: True
hooks: null
plan_mode: True
model_providers: "Claude Code, Codex, Gemini, arbitrary shell/custom commands on PATH"
pricing: "Free / open-source (MIT)"
install_method: "curl -fsSL https://raw.githubusercontent.com/almogdepaz/wolfpack/main/install.sh | bash; or bunx wolfpack-bridge@latest; or npx --yes wolfpack-bridge@latest. Verify with wolfpack doctor. Uninstall with wolfpack uninstall --yes"
docs_url: "https://almogdepaz.github.io/wolfpack/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/almogdepaz/wolfpack"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Self-hosted browser terminal manager for AI coding agents; persistent PTY-backed sessions live in a Rust broker (not the web server) so server restarts/upgrades don't kill running agents; fully self-hosted with direct private Tailnet access and no Wolfpack-hosted relay or account; multi-machine control room with handshake-verified peers; phone PWA, desktop terminal grid, and direct wolfpack attach; Agent Skills (wolfpack-tailnet-control) and Pi task-delegation integrations."
---

Self-hosted browser terminal manager for AI coding agents; persistent PTY-backed sessions live in a Rust broker (not the web server) so server restarts/upgrades don't kill running agents; fully self-hosted with direct private Tailnet access and no Wolfpack-hosted relay or account; multi-machine control room with handshake-verified peers; phone PWA, desktop terminal grid, and direct wolfpack attach; Agent Skills (wolfpack-tailnet-control) and Pi task-delegation integrations.
