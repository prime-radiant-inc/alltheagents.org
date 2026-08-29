---
name: "local-coding-agent"
slug: "local-coding-agent"
layout: "agent.njk"
category: "other"
maker: "LongNgn204"
license: "AGPL-3.0-or-later"
url: "https://github.com/LongNgn204/local-coding-agent"
source_code_url: "https://github.com/LongNgn204/local-coding-agent"
source_available: "True"
platforms:
  - "Web"
  - "Desktop"
first_released: "2026-06-28"
current_release: "2026-08-16"
stars: "43"
language: "JavaScript"
homepage: null
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "git clone then scripts/lca install (macOS/Linux) or scripts/lca.cmd install (Windows); optional tray app .exe from Releases"
docs_url: "https://github.com/LongNgn204/local-coding-agent#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/LongNgn204/local-coding-agent/releases/download/v5.0.0/LocalCodingAgentTray-5.0.0-win-x64.exe"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Local-first MCP server with a live dashboard showing health metrics. Compact & Resume feature for context handoff across ChatGPT sessions. Named multi-root permission profiles with per-path rights. Optional Chrome Companion and Windows tray app with DPAPI-encrypted key storage. Works with any MCP client."
---

The project addresses the trust gap that opens when cloud agents are allowed to operate on a real workstation. Every capability - file reads and patches, command execution, git inspection, bounded browser preview - is exposed as an MCP tool bounded by permission profiles, with a balanced policy that routes risky actions through a local approval request. A dashboard at localhost shows health scores, latency, tool calls, and git diffs in real time, and compact/resume prompts let ChatGPT sessions hand context across conversation boundaries. An Electron tray app supervises the server with secrets held in Windows DPAPI or macOS Keychain. Developers who want Claude Code, Codex, Cursor, or ChatGPT to work on their machine under explicit, revocable permissions are the target users.
