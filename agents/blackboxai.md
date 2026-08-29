---
name: "BLACKBOX.AI"
slug: "blackboxai"
layout: "agent.njk"
category: "other"
maker: "BLACKBOX.AI"
license: null
url: "https://www.blackbox.ai"
source_code_url: null
source_available: "False"
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: "https://www.blackbox.ai"
mcp_support: "no"
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: "300+ open and closed models (NVIDIA Nemotron, Alibaba Qwen, Minimax, Moonshot AI, etc.)"
pricing: "Per-token pricing (e.g., $0.32-$1.90 per million tokens depending on model); full pricing on website"
install_method: "OpenAI-compatible REST API (change base URL); CLI and VS Code extension available"
docs_url: "https://docs.blackbox.ai"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "toolify"
what_makes_it_special: "Enterprise inference platform and API gateway hosting 300+ open-weight models with end-to-end encryption, zero data retention enforced at the gateway, PII removal for closed models on Enterprise, and single-tenant isolated deployments. OpenAI-compatible endpoint. Claims fastest inference engine (454 tokens/sec for Nemotron 3 Ultra). Also offers Agents API for sending coding agents to repositories over HTTP."
---

BLACKBOX.AI began as a code-completion assistant and has repositioned as an enterprise inference platform. Its core offerings are dedicated single-tenant GPU deployments of open-weight models and a router exposing 300+ models through an OpenAI-compatible endpoint with enforced zero data retention; throughput marketing leans on a verified 454 tokens/second Nemotron deployment. On top of that infrastructure sits an Agents API that dispatches coding agents to repositories over HTTP — create runs, stream logs, open pull requests — with a multi-agent dashboard that can run the same task against Claude Code, Codex, and Gemini and have a 'Chairman LLM' pick the best implementation. A CLI ('agentic terminal') and VS Code extension round out the surface. The buyers are enterprises that need fast inference of open-weight models with compliance controls; the platform is active, with product announcements as recent as August 2026.
