---
name: "am-i-vibing"
slug: "am-i-vibing"
layout: "agent.njk"
category: "other"
maker: "ascorbic"
license: "MIT"
url: "https://github.com/ascorbic/am-i-vibing"
source_code_url: "https://github.com/ascorbic/am-i-vibing"
source_available: "True"
platforms:
  - "IDE"
first_released: "2025-07-17"
current_release: "2026-08-18"
stars: "346"
language: "TypeScript"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: null
pricing: "Free/open-source (MIT)"
install_method: "npm install am-i-vibing (library) or npx am-i-vibing (CLI)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/ascorbic/am-i-vibing"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Library and CLI that detects whether code is being executed by AI coding agents/editors (16+ tools: Aider, Bolt, Claude Code, Codex CLI, Cursor, Gemini CLI, Copilot, Jules, opencode, Pi, Replit, Warp, Windsurf, Zed, etc.) via environment variables and optional process-tree inspection, so tools can adapt output for agentic vs human consumption."
---

Libraries and CLIs increasingly need to know whether their output is being read by a human or fed back into an agent, since error messages, logging verbosity, and formatting differ. am-i-vibing exposes detectAgenticEnvironment() plus quick checks (isAgent, isInteractive, isHybrid) and a CLI (npx am-i-vibing, exit-code based) that classify the current process against 16 known tools via environment variables, with optional process-tree inspection for tools like Octofriend that leave no env traces. Detection returns the tool id, name, and environment type, with documented caveats about false positives. Matt Kane maintains it actively (125 commits, changesets, Renovate) as MIT-licensed TypeScript on npm.
