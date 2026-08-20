---
name: "opencode-plusplus"
slug: "opencode-plusplus"
layout: "agent.njk"
category: "agent"
maker: "whut09"
license: "MIT"
url: "https://github.com/whut09/opencode-plusplus"
source_code_url: "https://github.com/whut09/opencode-plusplus"
source_available: True
platforms:
  - "IDE"
first_released: "2026-05-24"
current_release: "2026-08-19"
stars: "109"
language: "TypeScript"
homepage: null
mcp_support: True
plugin_support: True
claude_code_plugin: False
subagents: False
hooks: True
plan_mode: null
model_providers: null
pricing: "Free/open-source (MIT)"
install_method: "Download opencode-plusplus-setup-win-x64.exe from GitHub Releases; quit OpenCode Desktop; double-click EXE; reopen OpenCode Desktop (no admin rights needed, writes to %USERPROFILE%/.config/opencode)"
docs_url: "https://github.com/whut09/opencode-plusplus/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/whut09/opencode-plusplus/releases"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Narrow-scope reliability harness/plugin for OpenCode Desktop (Windows) that patches the command dispatcher (only 3 exact command names) to enable model-free local state control; adds guard rails (edit boundaries, dangerous command blocking, protected paths), evidence capture (redacted, hashed), and a closed-loop verify-and-repair workflow via /plusplus-task and /plusplus-verify slash commands; user-level Windows plugin requiring no admin privileges and no second desktop shell; ships internal dev/test-only MCP server."
---

Narrow-scope reliability harness/plugin for OpenCode Desktop (Windows) that patches the command dispatcher (only 3 exact command names) to enable model-free local state control; adds guard rails (edit boundaries, dangerous command blocking, protected paths), evidence capture (redacted, hashed), and a closed-loop verify-and-repair workflow via /plusplus-task and /plusplus-verify slash commands; user-level Windows plugin requiring no admin privileges and no second desktop shell; ships internal dev/test-only MCP server.
