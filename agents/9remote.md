---
name: "9remote"
slug: "9remote"
layout: "agent.njk"
category: "multiplexer"
maker: "decolua"
license: "Proprietary"
url: "https://github.com/decolua/9remote"
source_code_url: "https://github.com/decolua/9remote"
source_available: "False"
platforms:
  - "CLI"
  - "Web"
  - "Desktop"
first_released: "2026-04-18"
current_release: "2026-04-20"
stars: "521"
language: "TypeScript, JavaScript"
homepage: "https://9remote.cc"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "agents bring their own providers; 9remote supplies none"
pricing: "free"
install_method: "npm install -g 9remote  (also Desktop App via Tauri, Mobile App iOS/Android, Web Client at 9remote.cc)"
docs_url: "https://docs.9remote.cc"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/9remote"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "All-in-one remote access (terminal + remote desktop + file explorer + code editor + git integration) from any phone or browser; QR-based pairing; auto Cloudflare tunnel (no port forwarding); persistent PTY sessions; <50ms latency; LAN-first mode; works with AI coding tools from anywhere. Source not yet public (proprietary until star milestone reached)."
---

Long-running AI coding sessions keep working after you leave the desk, but checking on them from a phone usually means SSH apps, port forwarding, and half-broken mobile terminals. 9remote packages the whole remote path: install the npm package, scan a QR code, and the tool opens a Cloudflare tunnel automatically, giving a phone or browser a persistent terminal, remote desktop, file explorer, code editor, and git views with sub-50ms interaction on LAN. Sessions persist server-side so agents keep working between visits, and a LAN-first mode covers no-internet setups. It is free during development, proprietary until a GitHub-star milestone triggers MIT open-sourcing, and targets developers who steer Claude Code, Codex, Cursor, or Gemini CLI sessions from their phone.
