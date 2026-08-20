---
name: "Awel"
slug: "awel"
layout: "agent.njk"
category: "agent"
maker: "MarsZ42"
license: "MIT (README) / Apache-2.0 (repo metadata - conflicting)"
url: "https://github.com/MarsZ42/Awel"
source_code_url: "https://github.com/MarsZ42/Awel"
source_available: True
platforms:
  - "IDE"
first_released: "2026-01-31"
current_release: "2026-02-07"
stars: "38"
language: "TypeScript, JavaScript (Node.js)"
homepage: "https://awel.sh/"
mcp_support: null
plugin_support: null
claude_code_plugin: False
subagents: False
hooks: null
plan_mode: True
model_providers: "Claude Code (Claude CLI), Anthropic API, OpenAI, Google AI, MiniMax, Zhipu AI, Vercel Gateway, OpenRouter"
pricing: "Free / open-source"
install_method: "Set at least one AI provider env var, then: npx awel create (new project) or cd existing-next-app && npx awel dev"
docs_url: "https://awel.sh/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/MarsZ42/Awel"
maintained: "active"
sources:
  - "github_final"
what_makes_it_special: "AI dev overlay/proxy that lives inside your running Next.js app rather than a separate IDE or CLI; runs a proxy on :3001 in front of the dev server on :3000 and injects an isolated Shadow-DOM chat button; element inspector attaches clicked DOM elements as context; screenshot annotator with shapes/arrows/text; one-click undo of all file changes from a session; pauses HMR/WebSocket traffic during agent edits; creation mode scaffolds and builds an app from scratch via full-page AI chat."
---

AI dev overlay/proxy that lives inside your running Next.js app rather than a separate IDE or CLI; runs a proxy on :3001 in front of the dev server on :3000 and injects an isolated Shadow-DOM chat button; element inspector attaches clicked DOM elements as context; screenshot annotator with shapes/arrows/text; one-click undo of all file changes from a session; pauses HMR/WebSocket traffic during agent edits; creation mode scaffolds and builds an app from scratch via full-page AI chat.
