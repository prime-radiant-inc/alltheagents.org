---
name: "Netlify AI"
slug: "netlify-ai"
layout: "agent.njk"
category: "agent"
maker: "Netlify"
license: "Proprietary"
url: "https://www.netlify.com"
source_code_url: null
source_available: "no"
platforms:
  - "Web"
first_released: "2025"
current_release: "2026"
stars: null
language: null
homepage: "https://www.netlify.com"
mcp_support: null
plugin_support: null
claude_code_plugin: "no"
subagents: null
hooks: null
plan_mode: null
model_providers: "Claude, Codex, Gemini, OpenCode agents; Kimi, DeepSeek, GLM models via AI Gateway"
pricing: "freemium"
install_method: null
docs_url: "https://docs.netlify.com"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Agent-native platform ('Agent Runners') to build/deploy web apps from prompts"
---

Netlify embeds AI agents into its hosting dashboard so that a described task — a bug fix, new page, or config change — can be dispatched to an agent that already sees the project's code, build configuration, and deployment pipeline. Agents run in isolated environments that never touch secrets, and role-based access separates who can propose changes from who can deploy them. Output flows through the standard review flow: a Deploy Preview that a human approves, iterates, or rolls back. Agent runs consume platform credits, with model inference metered separately through the Netlify AI Gateway, which also removes the need for users to manage API keys. The feature is available on the free tier and targets teams already building on Netlify.
