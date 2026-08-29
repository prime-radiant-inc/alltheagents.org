---
name: "QuillCode"
slug: "quillcode"
layout: "agent.njk"
category: "agent"
maker: "Lore-Hex"
license: "Apache-2.0"
url: "https://github.com/Lore-Hex/QuillCode"
source_code_url: "https://github.com/Lore-Hex/QuillCode"
source_available: "True"
platforms:
  - "Desktop"
  - "CLI"
first_released: "2026-06-20"
current_release: null
stars: 17
language: "Swift"
homepage: "https://github.com/Lore-Hex/QuillCode/releases/tag/tester-latest"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "via TrustedRouter model catalog or named profiles"
pricing: "usage"
install_method: "Download the tester release from GitHub Releases, or build with swift run quill-code-desktop (Swift 6, Swift Package Manager)"
docs_url: "https://github.com/Lore-Hex/QuillCode/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Lore-Hex/QuillCode/releases/tag/tester-latest"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A native macOS coding agent written in 100% Swift with no Electron or web shell, combining project-aware chat, local tools, Git workflows, Computer Use, automations, plugins, and an integrated workspace terminal. A locked enterprise variant enforces US/EU processing policies and fails closed."
---

QuillCode is the repo behind Quill Cowork, a SwiftUI-native coding agent and AI coworker inspired by Codex, Claude Code, and Cline, built entirely in Swift 6 rather than wrapping a web view. The desktop app combines multi-project chats with project instructions and memories, file read/search/edit/review, shell commands, Git operations including branches and worktrees, browser sessions, macOS Computer Use, concurrent chats, code reviews, scheduled automations, and a workspace terminal. Skills, plugins, hooks, and MCP servers run with visible approvals and workspace boundaries, and a verified auto-updater checks SHA-256 hashes, validates signatures, and rolls back automatically on failure. Models route through the TrustedRouter catalog with per-task usage limits, and a locked Confidential Cowork variant enforces US/EU processing; it is currently in an early tester stage with ad-hoc signing, shipping macOS universal builds plus CLI variants for macOS and Linux.
