---
name: "vibe-coding-template"
slug: "vibe-coding-template"
layout: "agent.njk"
category: "other"
maker: "humanstack"
license: "MIT"
url: "https://github.com/humanstack/vibe-coding-template"
source_code_url: "https://github.com/humanstack/vibe-coding-template"
source_available: "True"
platforms: []
first_released: "2025-03-27"
current_release: "2025-09-04"
stars: "245"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI, Anthropic"
pricing: "Free / open-source"
install_method: "git clone + ./first-time.sh + make dev"
docs_url: "https://github.com/humanstack/vibe-coding-template/blob/main/AGENTS.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/humanstack/vibe-coding-template"
maintained: "active"
sources:
  - "github_final"
what_makes_it_special: "Full-stack starter template optimized specifically for AI coding agents (Cursor & AGENTS.md) with context-aware Cursor Rules, code templates, and built-in best practices — designed to save tokens and boilerplate effort when vibe coding. FastAPI backend + Next.js frontend with Supabase integration."
---

The template addresses the cost and inconsistency of pointing a coding agent at an empty repository: the agent invents project structure, rewrites boilerplate, and drifts from the intended stack with every session. Vibe-coding-template ships the structure instead — a FastAPI backend with Supabase integration (Google/LinkedIn/email auth, realtime, storage, migrations) and Qdrant vector search with a local fallback, a Next.js/Tailwind frontend with complete auth flows, and Docker Compose for development and production — paired with Cursor rules and an AGENTS.md that encode the architecture, conventions, and reusable code templates so Cursor or any AGENTS.md-aware agent generates code that already fits. Founders and small teams starting AI-built full-stack apps clone it as their base; it is MIT-licensed starter code with a small number of commits rather than an actively developed tool.
