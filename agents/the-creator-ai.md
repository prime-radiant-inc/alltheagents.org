---
name: "The-Creator-AI"
slug: "the-creator-ai"
layout: "agent.njk"
category: "agent"
maker: "The-Creator-AI"
license: "MIT"
url: "https://github.com/The-Creator-AI/The-Creator-AI"
source_code_url: "https://github.com/The-Creator-AI/The-Creator-AI"
source_available: "True"
platforms: []
first_released: "2024-06-09"
current_release: "2025-02-21"
stars: "158"
language: "TypeScript"
homepage: "https://marketplace.visualstudio.com/items?itemName=PulkitSingh.the-creator-ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "True"
model_providers: "OpenAI, Google"
pricing: "freemium"
install_method: "VS Code Marketplace (search 'The Creator AI')"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=PulkitSingh.the-creator-ai"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "AI coding assistant for large/complex codebases with UI context chooser for selecting files/folders and a code change planning feature."
---

The-Creator-AI is a VS Code extension built for working with large and complex codebases, where the central problem is giving the model the right slice of context. Its context chooser lets the developer pick files and folders through a UI so those stay in the model's window, and its Code Change Plan feature has the agent generate an implementation plan from a description of the desired change before any edits happen. Chat and a file explorer round out the surface, and the extension runs on user-supplied Gemini or OpenAI API keys rather than a bundled service. It is MIT-licensed, installable from the VS Code Marketplace, and its development pace slowed after early 2025 — the last release was February 2025 — though the repository remains public. Developers on big repos who want explicit context control and plan-first edits are the intended users.
