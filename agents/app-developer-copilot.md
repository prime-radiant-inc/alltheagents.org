---
name: "App Developer Copilot"
slug: "app-developer-copilot"
layout: "agent.njk"
category: "agent"
maker: "Sinduja Ramaraj"
license: null
url: "https://marketplace.visualstudio.com/items?itemName=sindujaramaraj.app-developer-copilot"
source_code_url: null
source_available: "Yes"
platforms:
  - "IDE"
first_released: "2024-12-04"
current_release: "2025-05-23"
stars: null
language: null
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic, Google Gemini"
pricing: "free"
install_method: "Install from the VS Code Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=sindujaramaraj.app-developer-copilot"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "App developer agent for creating web and mobile apps"
---

The extension targets developers who want app scaffolding without leaving VS Code: a /create command triggers prompt analysis, feature listing, design reference ingestion (images or Figma links), architecture generation, TypeScript code generation, and dependency installation, followed by /run to execute the result. It ships as two Copilot Chat participants — mobile (React Native + Expo) and web (React + Next.js, optional Supabase) — and works through GitHub Copilot's model picker (Claude 3.5, GPT-4o, Gemini 2.5 Pro recommended) or BYOK credentials. Independent publisher Sinduja Ramaraj maintains it open source (~9,300 installs, v2.0.9), with the honest caveat that generated apps may need manual TypeScript and dependency fixes.
