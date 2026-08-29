---
name: "DeepSite"
slug: "deepsite"
layout: "agent.njk"
category: "agent"
maker: "DeepSite"
license: "Proprietary"
url: "https://deepsite.dev"
source_code_url: null
source_available: "True"
platforms:
  - "Web"
first_released: "2025"
current_release: "2026"
stars: null
language: "TypeScript"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "DeepSeek, MiniMax, Kimi"
pricing: "Free"
install_method: "Web app at https://huggingface.co/spaces/enzostvs/deepsite; self-hosted fork available via git clone + npm install + npm run dev"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://huggingface.co/spaces/enzostvs/deepsite"
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "AI-powered website builder on Hugging Face Spaces that uses open-source models (DeepSeek, MiniMax, Kimi). Combines AI code generation with free hosting, instant deployment, and multi-page support. A community fork (deepsite-locally) enables self-hosted/offline use."
---

DeepSite targets people who want a website but not a web-dev environment: describe a page, and the Space generates the code, renders it in a live preview, and lets the user iterate conversationally before pushing it live. Iteration is the agentic part — each revision regenerates code against the existing preview rather than starting over, and multi-page support means routing, navigation, and SEO structure are produced together. Deployment is handled inside the Space, so a finished site goes to hosted pages without CI/CD configuration. Non-developers use it to launch small sites; developers use it to scaffold and then export the code.
