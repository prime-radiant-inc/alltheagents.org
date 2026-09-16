---
name: "GraphCode"
slug: "graphcode"
layout: "agent.njk"
category: "multiplexer"
maker: "scgopi"
license: "FSL-1.1-MIT"
url: "https://graphcode.app"
source_code_url: "https://github.com/scgopi/GraphCode"
source_available: "True"
homepage: null
docs_url: "https://graphcode.app/"
download_url: "https://github.com/scgopi/GraphCode/releases/latest/download/graphcode-macos-arm64.dmg"
install_method: "brew install --cask scgopi/graphcode/graphcode, or the signed .dmg from GitHub Releases"
platforms:
  - "CLI"
  - "Desktop"
autonomy_level:
  - "autonomous-background"
specialization: "general"
language: "Swift"
first_released: "2026-07-26"
current_release: "2026-09-09"
maintained: "active"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "Claude Code, GitHub Copilot CLI, Codex CLI, OpenCode (the agent CLIs bring their own providers)"
pricing: "free"
stars: "121"
sources:
  - "github-issue"
date_added: "2026-07-26"
last_verified: "2026-09-11"
what_makes_it_special: "Agent sessions are nodes on a graph and the edges do the coordinating: a hand-off, message, or spawn edge fires when one loop resolves, so a chain of work runs unattended while every node stays a live terminal you can attach to and correct mid-run."
---

GraphCode exists because running one coding-agent session in a terminal is easy and running ten connected ones is not: the moment work fans out, the human becomes the scheduler. It types each loop by what ends it: a turn-based loop pauses for review each turn, a goal-based loop resolves when its done check passes (optionally a shell predicate that exits 0), a time-based loop keeps its cadence inside the agent's own prompt, and a composite loop runs a sub-graph of loops end to end. A launchd daemon fires the edges between loops, polls goal predicates, and keeps unattended sessions alive whether or not the app is open; each terminal is a zmx session that survives quitting the app and rebooting, and the backend's session id is persisted so a relaunch resumes the conversation instead of starting a duplicate. GraphCode bundles no agent: it launches whichever supported CLI is on your PATH, a running loop can create and wire further loops through the bundled graphcode CLI, projects can live on a remote machine over SSH with the Mac only steering, and nothing is ever written inside a project folder you open. Built on Ghostty for terminal rendering and requiring macOS 15 or later on Apple Silicon, it is aimed at developers who already work in Claude Code, Copilot CLI, Codex, or OpenCode and want to hand off whole chains of work and come back to steerable terminals rather than finished logs.
