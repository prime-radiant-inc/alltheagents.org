---
name: "oi"
slug: "oi"
layout: "agent.njk"
category: "agent"
maker: "oi-overide"
license: "GPL-2.0"
url: "https://github.com/oi-overide/oi"
source_code_url: "https://github.com/oi-overide/oi"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2024-09-26"
current_release: "2025-07-26"
stars: "192"
language: "TypeScript"
homepage: "https://www.npmjs.com/package/overide"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, DeepSeek, Groq"
pricing: "Free / open-source"
install_method: "npm install -g overide (or pnpm install -g overide)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/overide"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Lightweight, IDE-agnostic CLI that integrates AI code generation into any workflow by live-monitoring files in any text editor for simple //> <// prompt patterns and automatically generating and inserting code; requires no editor extensions."
---

oi (published as overide) integrates AI code generation into any editor through a comment-based workflow rather than a chat panel. Developers write prompts inline using a simple syntax, and a file watcher sends them to OpenAI, DeepSeek, or Groq for generation, inserting results with an accept/reject confirmation. Project setup via overide init creates an oi-config.json with project name and ignore patterns, and the tool stays out of the way otherwise. The approach trades conversation context for zero workflow change, which suits quick function-level generation inside an existing IDE workflow. A roadmap toward multi-file edits and unified diffs suggests evolution toward fuller agentic behavior.
