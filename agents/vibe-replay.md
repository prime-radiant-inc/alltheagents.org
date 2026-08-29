---
name: "vibe-replay"
slug: "vibe-replay"
layout: "agent.njk"
category: "other"
maker: "tuo-lei"
license: "MIT"
url: "https://github.com/tuo-lei/vibe-replay"
source_code_url: "https://github.com/tuo-lei/vibe-replay"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-03-05"
current_release: "2026-08-10"
stars: "33"
language: "TypeScript"
homepage: "https://vibe-replay.com"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "False"
plan_mode: "False"
model_providers: "Supported session providers: Claude Code, Claude Desktop, Claude Cowork, Codex, Cursor, OpenCode, Hermes, Pi"
pricing: "Free/open source"
install_method: "CLI: npx vibe-replay; Plugin: /plugin marketplace add tuo-lei/vibe-replay; Agent Skills: npx skills add tuo-lei/vibe-replay --skill replay -g; Manual: curl SKILL.md into ~/.claude/skills/replay/"
docs_url: "https://vibe-replay.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/vibe-replay"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Turns AI coding sessions into shareable, interactive self-contained HTML replays — animating every prompt, thought, tool call, and code diff. One command, zero config, offline-ready. Secret redaction built in. Live mode streams a running Claude Code or Codex session in real time. Deep analytics: token burn, cost over time, context window usage, cache hit rates, tool call distribution. Claude Code plugin auto-embeds replay context into PR descriptions. No wrappers/proxies — reads existing session logs after the fact."
---

AI coding sessions disappear when the terminal closes: reviewers see only the final diff, and the prompts, dead ends, and tool calls that produced it are lost. Vibe-replay converts session logs from Claude Code, Codex, Cursor, OpenCode, and other harnesses into one self-contained HTML file that animates the whole run — prompts, model thinking, tool calls, and code diffs — without proxies or wrappers since it reads session logs afterward; secret redaction runs before export, and Live mode streams a session in progress. A companion dashboard indexes past sessions with token, cost, and context-window analytics and filters by repo, tool, or MCP server. Developers use it to review their own agent runs, attach reproducible evidence to pull requests and issue reports, and audit what an autonomous session actually did; a Claude Code plugin inserts replay links directly into pull requests.
