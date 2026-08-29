---
name: "ai-website-builder"
slug: "ai-website-builder"
layout: "agent.njk"
category: "other"
maker: "builtbyV"
license: "MIT"
url: "https://github.com/builtbyV/ai-website-builder"
source_code_url: "https://github.com/builtbyV/ai-website-builder"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2025-07-16"
current_release: "2026-04-20"
stars: "76"
language: "JavaScript"
homepage: "https://oss.v.ee/ai-website-builder/"
mcp_support: null
plugin_support: "True"
claude_code_plugin: "yes (installs as a Claude Code skill to ~/.claude/skills/ai-website-builder/)"
subagents: null
hooks: null
plan_mode: null
model_providers: "Claude (Anthropic), Codex (OpenAI), Gemini (Google)"
pricing: null
install_method: "Skill install: curl -fsSL https://raw.githubusercontent.com/builtbyV/ai-website-builder/main/skill/install.sh | bash; or git clone && bash setup.sh"
docs_url: "https://oss.v.ee/ai-website-builder/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: null
sources:
  - "github_final"
what_makes_it_special: "Website template + self-contained 'skill' package that lets non-technical users build and update websites by conversing with AI coding agents (Claude Code, Codex CLI, Gemini CLI, Cursor, VS Code Copilot). Includes starter templates, publish scripts, and style guides. Responsive, SEO-friendly, with one-click publishing to GitHub Pages, Cloudflare Pages, Netlify, Vercel. Not a coding agent harness itself; it's a skill that agents use."
---

The project exists to let people who cannot code build and maintain websites by talking to whichever AI coding assistant they already have. A Vite-based starter template is bundled with a skill directory containing the instructions and deployment scripts an agent needs; a setup.sh installs the chosen CLI and starts a live preview server alongside the agent session. Publishing happens conversationally, with the agent pushing to GitHub Pages, Cloudflare Pages, Netlify, or Vercel. The template is MIT-licensed and free, with costs coming from the underlying agent subscriptions; it is a young single-maintainer project (15 commits) aimed at small businesses and freelancers.
