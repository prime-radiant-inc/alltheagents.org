---
name: "cmux"
slug: "cmux"
layout: "agent.njk"
category: "multiplexer"
maker: "manaflow-ai"
license: "GPL-3.0-or-later"
url: "https://github.com/manaflow-ai/cmux"
source_code_url: "https://github.com/manaflow-ai/cmux"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2026-01-28"
current_release: "2026-08-20"
stars: "26251"
language: "Swift"
homepage: null
mcp_support: null
plugin_support: "yes (skills, custom commands via cmux.json)"
claude_code_plugin: "yes (cmux claude-teams runs Claude Code's teammate mode; Claude Code hooks/resume supported)"
subagents: "yes"
hooks: "yes (cmux hooks setup for Claude Code, Codex, OpenCode, etc.)"
plan_mode: "no"
model_providers: "BYOK (works with any terminal-based agent: Claude Code, Codex, OpenCode, Gemini CLI, Kiro, Aider, Goose, Amp, Cline, Cursor Agent)"
pricing: "freemium (free/open source; Founder's Edition paid tier)"
install_method: "binary (DMG), brew"
docs_url: "https://cmux.com/docs/getting-started"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg"
maintained: "active"
sources:
  - "author_search"
what_makes_it_special: "A native macOS terminal built on libghostty (not Electron) designed specifically for parallel AI coding agent workflows, with a notification system (blue rings around panes), vertical tabs showing git branch/PR status, a built-in scriptable browser, and agent orchestration as native splits."
---

cmux argues that the right primitive for parallel agent work is a terminal that understands agents rather than another orchestrator: panes get attention rings when an agent needs input, tabs surface branch and PR metadata, and agent subagents appear as native panes. It embeds libghostty as a rendering library rather than forking Ghostty, so existing configs carry over, and a scriptable browser pane lets agents verify web UI changes they just made. Sessions restore across restarts, an iOS app allows monitoring from a phone, and a CLI/socket API makes it scriptable. With tens of thousands of stars it is the most prominent macOS-native agent terminal in this census.
