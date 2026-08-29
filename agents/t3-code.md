---
name: "T3 Code"
slug: "t3-code"
layout: "agent.njk"
category: "multiplexer"
maker: "pingdotgg"
license: "MIT"
url: "https://t3.codes"
source_code_url: "https://github.com/pingdotgg/t3code"
source_available: "True"
platforms: []
first_released: "2026-02-08"
current_release: "2026-08-20"
stars: "19621"
language: "TypeScript"
homepage: "https://t3.codes"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, Codex, Cursor, Grok Build, OpenCode"
pricing: "Free / open-source"
install_method: "CLI/Web: npx t3@latest; Desktop: winget install T3Tools.T3Code (Windows), brew install --cask t3-code (macOS), yay -S t3code-bin (Arch Linux), or GitHub Releases"
docs_url: "https://t3.codes"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/pingdotgg/t3code/releases"
maintained: "active"
sources:
  - "toolify"
what_makes_it_special: "Agent harness control surface enabling control of AI coding agents via mobile, web, or desktop app. Unified, performant, remote-ready control surface to manage multiple existing AI coding agent subscriptions across mobile, web, and desktop, while remaining completely open-source and forkable. iOS/Android apps and web app at app.t3.codes."
---

T3 Code came out of Theo Browne's ping.gg to solve a specific operational problem: people now pay for several AI coding agents and have no unified way to see, steer, and review what those agents are doing across machines. The product is a control surface, not an agent — it attaches to Claude Code, Codex, Cursor, Grok, and OpenCode using the user's own authenticated subscriptions rather than proxying tokens, and surfaces per-thread branches, diffs, and one-click commit/push/PR flows in a unified workspace. Native apps cover macOS, Windows, and Linux, with iOS, Android, and web clients for remote monitoring and intervention from a phone. The whole system is MIT-licensed and forkable, with GitHub Releases distributing desktop builds and app stores handling mobile. Its users are developers running multiple agent subscriptions who want one cross-device cockpit over them.
