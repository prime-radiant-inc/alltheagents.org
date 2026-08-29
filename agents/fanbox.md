---
name: "fanbox"
slug: "fanbox"
layout: "agent.njk"
category: "other"
maker: "alchaincyf"
license: "MIT"
url: "https://github.com/alchaincyf/fanbox"
source_code_url: "https://github.com/alchaincyf/fanbox"
source_available: "True"
platforms: []
first_released: "2026-06-10"
current_release: "2026-08-18"
stars: "991"
language: "JavaScript"
homepage: "https://github.com/alchaincyf/fanbox/releases/latest"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, Codex, Hermes Agent, OpenClaw, Kimi Code, ZCode, opencode, pi, CodeBuddy, WorkBuddy, Qoder CLI"
pricing: "free"
install_method: "binary"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/alchaincyf/fanbox/releases/latest"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Local-first, zero-config, zero-runtime-dependency desktop cockpit for coding agents that unifies the entire vibe-coding loop (find files, preview, light edit, command agent, see what changed) into a single window. No cloud, no accounts, no remote — data never leaves your machine. Live dashboard where file cards ripple/glow as the agent writes them, follow mode, session replay timeline, 5 independent reviewer subagents that must score >=90, and three distinct themed skins."
---

FanBox came out of indie developer Huashu's observation that agents now create projects faster than humans can track them — ten projects in an afternoon, and no way to see what changed where. The Electron app bundles a fuzzy-searching file browser with previews (Markdown, live HTML, code, images, video, PDF, archives), a real embedded terminal (node-pty + xterm.js), and a dashboard where agent file-writes light up cards in real time, with a cross-project inbox collecting changes across every running agent. Eleven built-in agent launchers cover Claude Code, Codex, Hermes Agent, OpenClaw, Kimi Code, opencode, pi, and other CLIs, extensible through ~/.fanbox/config.json. It targets individual developers juggling several concurrent agent sessions who need orientation and review rather than another agent.
