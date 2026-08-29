---
name: "supercli"
slug: "supercli"
layout: "agent.njk"
category: "agent"
maker: "yashdev9274"
license: "MIT"
url: "https://github.com/yashdev9274/supercli"
source_code_url: "https://github.com/yashdev9274/supercli"
source_available: "True"
platforms: []
first_released: "2026-01-04"
current_release: "2026-08-18"
stars: "192"
language: "TypeScript"
homepage: "https://supercodeai.vercel.app"
mcp_support: null
plugin_support: "True"
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenRouter, Anthropic Claude, Google Gemini, Vercel Minimax AI Provider"
pricing: "Free / open-source"
install_method: "npm install -g supercode (CLI); monorepo: clone + bun install"
docs_url: "https://supercli.vercel.app"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/supercode"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Full-stack AI-powered SWE agent platform: Next.js dashboard, MDX docs site, terminal web client, and installable CLI coding agent ('supercode' on npm), plus a parallel project fine-tuning its own coding-focused LLMs (Qwen3-8B, GLM-4-9B) via dual-track training (Tinker + Modal/Axolotl). Includes a 'skills' system shared across apps."
---

Supercode is developed as a Bun/Turborepo monorepo spanning the agent CLI published on npm as supercode, a Next.js dashboard for repo management and analytics, an MDX docs site, and a browser terminal client that mirrors the CLI. The agent runs on AI SDK v6 against Anthropic (default), OpenRouter, Gemini, and Minimax providers with file, execution, and search tools, and a shared @super/skills package provides reusable capabilities across apps. A parallel track, supercode-openmodel, fine-tunes Qwen3-8B through Tinker and GLM-4-9B through Modal/Axolotl to produce open coding-tuned weights for the platform. The project is MIT-licensed, Vercel-sponsored, and actively developed with no GitHub releases — distribution is the npm package. It fits developers who want an open, self-hostable agent plus the surrounding product surface.
