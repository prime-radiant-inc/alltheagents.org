---
name: "codinit-dev"
slug: "codinit-dev"
layout: "agent.njk"
category: "agent"
maker: "codinit-dev"
license: "MIT"
url: "https://github.com/codinit-dev/codinit-dev"
source_code_url: "https://github.com/codinit-dev/codinit-dev"
source_available: "True"
platforms:
  - "Web"
  - "Desktop"
first_released: "2025-10-04"
current_release: "2026-04-10"
stars: "260"
language: "TypeScript"
homepage: "https://codinit.dev/download"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI, Anthropic, Google, Groq, xAI, DeepSeek, Cohere, Mistral, Together, Perplexity, HuggingFace, OpenRouter, Ollama, LM Studio, OpenAI-compatible local endpoints (19+ providers)"
pricing: "Free / open-source"
install_method: "Download prebuilt desktop release (macOS/Windows/Linux); or clone repo + npm install + pnpm run dev; or Docker (npm run dockerbuild + docker compose --profile development up)"
docs_url: "https://codinit.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/codinit-dev/codinit-dev/releases/latest"
maintained: "active"
sources:
  - "github_final"
what_makes_it_special: "Open-source, local-first AI full-stack app builder with hybrid web + desktop (Electron) support. Vendor-neutral architecture with dynamic switching between 19+ cloud and local AI providers. Production-ready Dockerization with presets for Vercel/Netlify/GitHub Pages. Integrated dev suite with semantic search, diff visualization, and file-locking. Native Supabase integration."
---

Hosted app generators keep both the project and the model access inside a vendor's cloud, which conflicts with local development workflows and data-control requirements. CodinIT.dev is the open-source counterexample: a Bolt-style builder that runs as an Electron desktop app, a web app, or a Docker container, generating Node.js web and mobile applications with the edit loop happening on local files. Model access is vendor-neutral - nineteen-plus providers including OpenAI, Anthropic, Google, Groq, and OpenRouter, plus local runtimes via Ollama and LM Studio - switchable per task. Around the generation loop it adds project-management scaffolding: semantic code search, diff visualization, file locking for concurrent edits, voice commands, and deploy presets that push finished projects to Vercel, Netlify, or GitHub Pages. Supabase integration covers backend services. Developers and small teams wanting an open, local-first alternative to hosted app builders are its users.
