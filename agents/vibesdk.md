---
name: "vibesdk"
slug: "vibesdk"
layout: "agent.njk"
category: "agent"
maker: "cloudflare"
license: "MIT"
url: "https://github.com/cloudflare/vibesdk"
source_code_url: "https://github.com/cloudflare/vibesdk"
source_available: "True"
platforms:
  - "Web"
first_released: "2025-08-25"
current_release: "2026-08-19"
stars: "5323"
language: "TypeScript"
homepage: "https://build.cloudflare.dev"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Cloudflare AI Gateway (routes to multiple providers)"
pricing: "open-source"
install_method: "binary"
docs_url: "https://github.com/cloudflare/vibesdk/blob/main/docs/setup.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/cloudflare/vibesdk"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Open-source agentic platform by Cloudflare for building full-stack apps entirely on the Cloudflare stack (Durable Objects, Dynamic Workers, Artifacts, AI Gateway). No long-running dev server — previews load as Dynamic Workers on demand. Human-in-the-loop clarification, reversible Artifacts-backed history, signed branch-scoped preview URLs, bash disabled for safety."
---

VibeSDK packages the stack behind Cloudflare's own app-building experience as a deployable product: organizations that want a Lovable-style builder under their own brand, models, and data boundaries can run one entirely on Cloudflare's platform rather than assembling a code-generation API, a code-execution sandbox, and hosting separately. A user describes an application; the agent plans, edits files through explicit tools, and deploys each iteration as a Dynamic Worker serving a live preview with no long-running dev server. It reads the preview's console output to detect runtime errors, repairs them, and redeploys, and it asks structured clarifying questions when the request is underspecified. Every generated app gets isolated SQLite storage in a Durable Object facet and reversible version history in Cloudflare Artifacts, with model calls routed through AI Gateway for observability and caching. Teams building internal builders or AI product prototypes self-host it; production previews require Workers Paid and Workers for Platforms.
