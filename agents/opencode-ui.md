---
name: "OpenCode_UI"
slug: "opencode-ui"
layout: "agent.njk"
category: "other"
maker: "LaiZhou"
license: "MIT"
url: "https://github.com/LaiZhou/OpenCode_UI"
source_code_url: "https://github.com/LaiZhou/OpenCode_UI"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-01-11"
current_release: "2026-03-17"
stars: "48"
language: "Kotlin (JetBrains plugin, Gradle)"
homepage: "https://plugins.jetbrains.com/plugin/29744-opencode-ui"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "inherited from the OpenCode server (none configured by the plugin)"
pricing: "Free / open-source"
install_method: "JetBrains Marketplace: Settings -> Plugins -> Marketplace -> Search 'OpenCode' -> Install. Requires OpenCode CLI: npm install -g opencode-ai"
docs_url: "https://opencode.ai/docs"
plugin_docs_url: null
config_docs_url: "https://opencode.ai/docs"
download_url: "https://plugins.jetbrains.com/plugin/29744-opencode-ui"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "JetBrains IDE plugin integrating OpenCode AI coding agent. Native diff viewer with chronological navigation, smart file path links in terminal, automatic session persistence, and seamless context sharing from editor/project view directly to AI terminal."
---

OpenCode runs in a terminal, which leaves JetBrains users copying file paths by hand and reviewing agent changes in raw git diffs. This Kotlin plugin bridges the gap: Quick Launch attaches to a running OpenCode server (with optional password) or spawns a local terminal via Cmd+Esc, and Add to Terminal sends the current file or selection as context with Opt+Cmd+K. Diff review uses the IDE's native viewer with accept/reject actions that stage through git add, agent output renders file paths as clickable links, and sessions auto-resume with notifications when tasks complete. It installs from the JetBrains Marketplace, requires the opencode-ai CLI alongside, and works across IntelliJ IDEA, WebStorm, and PyCharm on 2025.2+. Its README candidly notes it lacks diagnostic sharing compared to Claude Code's plugin, since OpenCode relies on built-in LSP. JetBrains users who adopted OpenCode and want it embedded in their IDE are the audience.
