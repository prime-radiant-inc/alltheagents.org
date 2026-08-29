---
name: "ggez"
slug: "ggez"
layout: "agent.njk"
category: "other"
maker: "vibe-stack"
license: "MIT"
url: "https://github.com/vibe-stack/ggez"
source_code_url: "https://github.com/vibe-stack/ggez"
source_available: "True"
platforms: []
first_released: "2026-03-09"
current_release: "2026-04-19"
stars: "233"
language: "TypeScript/JavaScript (Bun)"
homepage: "https://vibe-stack.github.io/ggez/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Fal API"
pricing: "Free"
install_method: "Clone repo, bun install, bun run start"
docs_url: "https://vibe-stack.github.io/ggez/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/vibe-stack/ggez"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Framework for vibe-coding Three.js games ('Next.js for Three.js games'); provides world editor, animation editor, runtime packages, and orchestrator app for game development."
---

ggez packages the pieces a Three.js game usually lacks: a blockout/brush world editor with mesh and material tools, an animation graph editor with clip import/export, an orchestrator app that coordinates the tools with a running game, and runtime packages for loading authored content. OpenAI Codex is embedded across the editors ('Codex everywhere') so building a scene or tweaking a graph is a conversation, and an optional Fal API key unlocks AI-assisted generation, but the framework itself has no agentic loop, MCP, plugin, or hook machinery. It is MIT-licensed and Bun-based, installed by cloning the monorepo. It is a public alpha with acknowledged outdated docs and breaking changes, aimed at developers prototyping Three.js games with AI assistance in the editor rather than an agent harness.
