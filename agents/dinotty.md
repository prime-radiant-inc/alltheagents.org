---
name: "dinotty"
slug: "dinotty"
layout: "agent.njk"
category: "multiplexer"
maker: "xichan96"
license: "MIT"
url: "https://github.com/xichan96/dinotty"
source_code_url: "https://github.com/xichan96/dinotty"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
first_released: "2026-05-12"
current_release: "2026-08-18"
stars: "537"
language: "Rust, TypeScript, Vue"
homepage: "https://xichan96.github.io/dinotty/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: "Download platform installer from GitHub Releases (.dmg macOS / .deb Linux / .exe Windows); or build from source with pnpm + cargo"
docs_url: "https://xichan96.github.io/dinotty/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Server-side VTE terminal server for AI coding agents with multi-device sync (phone/iPad/desktop, one session), lightweight pure-text transmission (~1-10 KB/s), pane-based UI where terminals/plugins/files/SSH/git are all draggable splittable panes, built-in SSH/SFTP, file browser, and web preview."
---

Terminal coding agents bind you to the machine and window where the session started, and losing SSH connectivity mid-task means losing context. dinotty runs the terminal server-side and streams a compact text protocol (~1-10 KB/s) to any device, so a session started on a desktop continues on a phone or tablet and restores after disconnects. Everything is a pane — terminals, file browser, SSH sessions, web previews, and hot-reloadable JS plugins — arranged by drag-and-drop across phone, tablet, and desktop layouts. Split-broadcast typing, command bookmarks, and an SFTP-backed file browser round out a desktop client comparable to a full terminal emulator. Its users are developers running agents on servers who want to supervise them from any device.
