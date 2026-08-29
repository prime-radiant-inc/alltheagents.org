---
name: "nefi"
slug: "nefi"
layout: "agent.njk"
category: "agent"
maker: "Blazity"
license: "MIT"
url: "https://github.com/Blazity/nefi"
source_code_url: "https://github.com/Blazity/nefi"
source_available: "True"
platforms: []
first_released: "2024-12-17"
current_release: "2026-03-16"
stars: "66"
language: "TypeScript"
homepage: "https://nefi.ai/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic"
pricing: "free"
install_method: "npm (npx nefi / global install); requires an Anthropic API key"
docs_url: "https://nefi.ai/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "AI agent that automates code management and feature integration in Next.js codebases (primarily the next-enterprise boilerplate) through natural language commands, handling tasks like git operations, package management, and file modifications. Eliminates manual boilerplate configuration (e.g., 'remove storybook from my project')."
---

nefi grew out of Blazity's maintenance of its next-enterprise Next.js boilerplate, where routine customization tasks consumed disproportionate time. It exposes natural-language commands that the agent translates into git operations, package management, and file edits against the project. The tool runs from the command line in the target repository and is built on the Vercel AI SDK with Claude models. Its scope is deliberately narrow: Next.js 14/15 codebases, primarily the next-enterprise template, rather than general-purpose coding. The repository has had no releases and modest activity, positioning it as an early-stage companion to the boilerplate.
