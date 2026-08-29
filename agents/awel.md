---
name: "Awel"
slug: "awel"
layout: "agent.njk"
category: "agent"
maker: "MarsZ42"
license: "MIT (README) / Apache-2.0 (repo metadata - conflicting)"
url: "https://github.com/MarsZ42/Awel"
source_code_url: "https://github.com/MarsZ42/Awel"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-01-31"
current_release: "2026-02-07"
stars: "38"
language: "TypeScript, JavaScript (Node.js)"
homepage: "https://awel.sh/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "False"
hooks: "no"
plan_mode: "True"
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

Awel puts an AI dev agent inside the running Next.js app rather than beside it: a proxy on port 3001 fronts the dev server on 3000, intercepts HTML responses, and injects a Shadow-DOM script that mounts a floating chat button. Opening it reveals a full-page chat dashboard (in an iframe) where an agent reads, writes, and edits project files, with HMR traffic paused during edits to avoid reload interference. Tools cover file ops, bash, code search, web search/fetch, plan proposals, and dev-server restarts, backed by the Vercel AI SDK across Anthropic, OpenAI, Google, MiniMax, Zhipu, OpenRouter, and Claude CLI (YOLO mode). Element inspection and screenshot annotation attach DOM context directly. It is MIT/Apache-2.0 licensed (the two disagree in-repo), installed via npx awel create|dev, and suits Next.js developers who want in-app agent assistance without leaving the browser tab.
