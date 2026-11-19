---
name: "Autolith"
slug: "autolith"
layout: "agent.njk"
category: "agent"
maker: "lambda-symbolics"
license: "ISC"
url: "https://github.com/lambda-symbolics/autolith"
source_code_url: "https://github.com/lambda-symbolics/autolith"
source_available: "True"
homepage: "https://autolith.rocks"
docs_url: "https://lambda-symbolics.com/autolith/docs"
download_url: "https://github.com/lambda-symbolics/autolith/releases/latest"
install_method: "curl -fsSL https://sh.lambda-symbolics.com/autolith | sh (standalone binary for Linux, macOS, BSDs, Windows); nix run github:lambda-symbolics/autolith; or build from a source checkout"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "Common Lisp"
first_released: "2026-07-11"
current_release: "2026-11-17"
maintained: "active"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
plugin_docs_url: null
config_docs_url: null
model_providers: "ChatGPT, GitHub Copilot, Gemini, Grok, Nous, Anthropic, Fireworks, OpenCode, OpenRouter, Mistral, Vertex Gemini, Vertex Anthropic, local models via OpenAI-compatible endpoints (auth via autolith auth <provider>)"
pricing: "free"
stars: "566"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A terminal agent living inside a live Common Lisp image that can introspect and rewrite its own running code — including itself — and roll back through self-created image generations when a modification goes wrong, recovering into a rescue image to diagnose the failure."
---

Autolith, or AL, is a terminal agent built as a live Common Lisp image rather than a program that talks to an editor: because the agent's own code is loaded in the same image it works in, it can observe its live state, introspect what it is doing, and modify its own source — adapting itself to the task or the user's preferences — where a conventional harness would need a restart. The design leans on image generations: you or AL checkpoint the running image, and a bad self-modification (the docs call it 'a full frontal lobotomy') rolls back to the prior generation or reloads into a recovery image that diagnoses and optionally repairs the damage. Around that core sit practical ergonomics — XDG-conforming configuration, a bounded catalog of Skills loaded on demand via skill.load, child agents in channels up to three levels deep, mission schedules that wake the agent for background work, an independent tool-less reviewer pass over changed snapshots, and MCP clients joined per channel — with a deliberate nod to the Lisp Machine it is 'pretty close' to. Model access is broad: web-flow or API-key auth for ChatGPT, Copilot, Gemini, Grok, Nous, Anthropic, Fireworks, OpenCode, OpenRouter, Mistral and Vertex, all switched with autolith auth. It ships as a standalone binary for Linux, macOS, the BSDs and Windows, runs on Raspberry Pi-class hardware, and suits developers who want an agent they can read, hack and even let rewrite itself.
