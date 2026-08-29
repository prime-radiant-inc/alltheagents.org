---
name: "Perplexity-Inspired LLM Answer Engine"
slug: "perplexity-inspired-llm-answer-engine"
layout: "agent.njk"
category: "other"
maker: "developersdigest"
license: "MIT"
url: "https://github.com/developersdigest/llm-answer-engine"
source_code_url: "https://github.com/developersdigest/llm-answer-engine"
source_available: "True"
platforms: []
first_released: "2024-03-07"
current_release: "2026-04-29"
stars: "5038"
language: "TypeScript"
homepage: "https://developersdigest.tech"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Groq, OpenAI, Ollama, Portkey AI Gateway (Azure, Anyscale, Google, Anthropic, Cohere, Together, Perplexity, Mistral, Nomic, AI21, Stability, DeepInfra)"
pricing: "open-source"
install_method: "npm"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/developersdigest/llm-answer-engine"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Perplexity-like answer engine returning sources, answers, images, videos, and follow-up questions. Combines web search (Brave/Serper) with LLMs (Groq/OpenAI/Ollama), function calling (maps, shopping, stocks, Spotify), semantic caching via Upstash, rate limiting, AI gateway support for 15+ providers, dynamic UI rendering, and dual deployment (Next.js or Express-only)."
---

This repository emerged from the early-2024 wave of Perplexity clones as a teachable, single-repo implementation of an answer engine: Brave and Serper supply search results, the content gets scraped and embedded, and a hosted LLM synthesizes answers with sources, images, videos, and suggested follow-ups. Function calling extends it to maps, shopping, stock data, and Spotify, while a Portkey gateway route adds a dozen additional inference providers and an Upstash layer adds semantic caching and rate limits. Deployment paths cover Vercel, Docker, and a standalone Express API. The project's value is educational — it has 5,000+ stars and an accompanying YouTube walkthrough — but development stalled on a Next.js 14 stack with Groq's deprecated Mixtral model ID, and its issues and pull requests have gone unanswered. It is studied rather than operated.
