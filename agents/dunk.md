---
name: "dunk"
slug: "dunk"
layout: "agent.njk"
category: "other"
maker: "amix"
license: "MIT"
url: "https://github.com/amix/dunk"
source_code_url: "https://github.com/amix/dunk"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-05-10"
current_release: "2026-08-01"
stars: "30"
language: "TypeScript/JavaScript (Node.js 18+)"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: null
pricing: "Free/open source"
install_method: "npm i -g dunkdiff (Node.js 18+, Git)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/amix/dunk"
maintained: "active"
sources:
  - "github_topic5"
what_makes_it_special: "Terminal UI to review git diffs, leave hunk-anchored inline comments (saved to .dunk/comments.json), and let a coding agent read and fix those comments. Human-agent review loop: one human in a terminal reviewing diffs and one coding agent in another terminal fixing flagged issues — comments are hunk-anchored (not line-scoped) and survive small edits via a context hash. No daemon / no MCP (hard fork of hunk that stripped the heavy infrastructure). Live watch mode. Git-native (can be set as git's pager). Ships a skill at skills/dunk-review/SKILL.md for Claude Code."
---

Code review between a human and an agent usually happens through PRs, which are slow and lose the working-tree context. dunk puts the review in the terminal: press a on a hunk to leave a comment, and it lands in .dunk/comments.json as a hunk-scoped note that Claude Code or Codex can read, fix, and delete when resolved. With --watch the diff reloads as the agent commits, and drifted anchors surface at the top instead of silently breaking. It stays deliberately thin — no daemon, no MCP, no session broker — treating the JSON file as the whole contract. The workflow targets developers who review agent output locally, one human terminal next to one agent terminal.
