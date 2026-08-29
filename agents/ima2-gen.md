---
name: "ima2-gen"
slug: "ima2-gen"
layout: "agent.njk"
category: "other"
maker: "lidge-jun"
license: "MIT"
url: "https://github.com/lidge-jun/ima2-gen"
source_code_url: "https://github.com/lidge-jun/ima2-gen"
source_available: "yes"
platforms:
  - "IDE"
first_released: "2026-04-21"
current_release: "2026-08-19"
stars: "703"
language: "TypeScript"
homepage: "https://lidge-jun.github.io/ima2-gen/"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Grok, Gemini, Antigravity, AtlasCloud, MiniMax, Runway, Higgsfield"
pricing: "freemium"
install_method: "npm"
docs_url: "https://lidge-jun.github.io/ima2-gen/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/ima2-gen"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Local-first visual generation runtime and studio for people and coding agents, with reproducible image and video workflows across multiple providers. Combines local-first privacy with multi-provider generation. Modes: Classic, Node (branching), Multimode batches, Storyboard, Canvas cleanup. Ships production-grade agent skills for AI coding agents. Supports OAuth (free ChatGPT/Grok login) and API-key paths. Fail-closed default model policy prevents silent provider/billing switches. NOTE: This is an image/video generation studio, not a coding agent harness — included for completeness."
---

ima2-gen solves reproducibility for visual asset generation: a coding agent working on a site or game needs consistent images and video, and ad-hoc API calls produce neither auditability nor cost control. The local studio exposes Classic, Node (branching trees), multimode batch, Storyboard, and Canvas modes over a single SSE event stream, with every job observable and rerunnable. OAuth paths let agents use free ChatGPT and Grok logins, while API keys cover Gemini, AtlasCloud, MiniMax, and others; a fail-closed NO_DEFAULT_MODEL policy blocks silent provider or billing switches. Three installable skills teach coding agents the generation and frontend-asset workflows, and Docker, Nix, and launchd/systemd service modes support headless deployment.
