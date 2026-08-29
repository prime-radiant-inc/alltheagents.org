---
name: "omnidesk"
slug: "omnidesk"
layout: "agent.njk"
category: "multiplexer"
maker: "carloluisito"
license: "MIT"
url: "https://github.com/carloluisito/omnidesk"
source_code_url: "https://github.com/carloluisito/omnidesk"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Desktop"
first_released: "2026-01-27"
current_release: "2026-07-27"
stars: "109"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code,Codex CLI"
pricing: "Free/open-source"
install_method: "Download prebuilt binaries (.exe/.dmg/.AppImage/.deb) from GitHub Releases; or build from source via npm install and npm run package"
docs_url: "https://github.com/carloluisito/omnidesk/blob/main/docs/repo-index.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/carloluisito/omnidesk/releases"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Electron-based desktop terminal wrapping AI coding CLIs (Claude Code, Codex CLI) with multi-session management, grid layouts, and real-time session sharing; 'attention cockpit' classifies agent session states (working/awaiting-approval/errored/done/idle) from rendered terminal screen content; on-device voice-to-text via local Whisper; one-click Cloudflare tunnel remote access with mobile PWA; session history with cross-session search; per-account quota tracking; local-first with no telemetry."
---

omnidesk is an Electron desktop terminal that organizes Claude Code and Codex sessions around a flat repo-to-session workflow. Sessions run in xterm.js panes with grid or focus layouts, persist across restarts, and auto-rename themselves to the agent's live task summary. An attention cockpit aggregates sessions needing intervention across all repositories, and worktree-aware sessions can bind to branches with optional cleanup. Sessions persist across restarts, and transcript history supports cross-session search with markdown export. Remote access mirrors the UI to a phone through a token-secured tunnel, and push alerts to Telegram, Slack, or Discord carry deep links back into specific sessions. The project is an unofficial community tool, MIT-licensed, with no telemetry.
