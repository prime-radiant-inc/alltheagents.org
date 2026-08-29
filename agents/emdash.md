---
name: "Emdash"
slug: "emdash"
layout: "agent.njk"
category: "multiplexer"
maker: "generalaction"
license: "Apache-2.0"
url: "https://github.com/generalaction/emdash"
source_code_url: "https://github.com/generalaction/emdash"
source_available: "True"
platforms:
  - "IDE"
first_released: "2025-08-28"
current_release: "2026-08-19"
stars: "5446"
language: "TypeScript"
homepage: "https://emdash.com"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "Claude Code, Codex, Cursor, OpenCode, Amp, Devin, Qwen Code, Droid, GitHub Copilot"
pricing: "open-source"
install_method: "binary"
docs_url: "https://emdash.sh/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Open-source desktop app (YC W26) for running multiple AI coding agents in parallel, each isolated in its own Git worktree/branch. Provider-agnostic — bring any CLI agent. Local-first with SQLite storage, remote SSH/SFTP support, issue tracker integrations (Linear, Jira, GitHub, GitLab, Asana), and unified diff review/PR/CI/merge workflow."
---

Emdash came out of General Action's YC W26 batch to solve the coordination problem of running several coding agents at once: tasks step on each other, diffs pile up unreviewed, and nobody remembers which agent did what. Each task gets its own git worktree and branch so agents cannot collide, the desktop app shows diffs, CI checks, and PR state in one place, and installed agent CLIs (Claude Code, Codex, Cursor, OpenCode, Amp, Devin, Qwen Code, Droid, Copilot) are auto-detected. Issue trackers feed tasks in directly, and local projects can be complemented by remote machines over SSH/SFTP. State lives in local SQLite with no code or chats leaving the machine, which makes it usable in environments that prohibit cloud developer tools.
