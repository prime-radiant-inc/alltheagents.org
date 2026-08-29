---
name: "JCode"
slug: "jcode"
layout: "agent.njk"
category: "agent"
maker: "1jehuang"
license: "MIT"
url: "https://github.com/1jehuang/jcode"
source_code_url: "https://github.com/1jehuang/jcode"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-01-05"
current_release: "2026-08-19"
stars: null
language: "Rust"
homepage: "https://jcode.sh"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Claude, OpenAI, Google Gemini, GitHub Copilot, Azure OpenAI, Alibaba Cloud, OpenRouter, DeepSeek, Ollama, LM Studio, Fireworks, MiniMax, Meta Muse, Groq, Mistral, Perplexity, Together AI, xAI, Cerebras, Cursor, Antigravity, OpenAI-compatible"
pricing: "Free / open-source (MIT); BYO model/API keys"
install_method: "curl -fsSL https://jcode.sh/install | bash"
docs_url: "https://jcode.sh/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
what_makes_it_special: "Extreme RAM efficiency (6-14x less than competitors), sub-15ms first frame, human-like agent memory system with semantic vector retrieval, multi-agent swarm collaboration in shared repos, self-dev mode for self-modification, built-in browser automation."
---

JCode's engineering thesis is that agent harnesses are needlessly heavy: it holds one session in roughly 28 MB of RAM, adds about 10 MB per additional session, boots in about 14 ms, and renders at 1000+ fps with a custom Rust terminal and Mermaid renderer. On top of that sits a memory system that embeds each turn into a semantic graph, consolidates memories periodically, and retrieves by cosine similarity, with an optional verification sideagent. Swarms run multiple agents in one repository with conflict notifications and agent-to-agent messaging. Self-dev mode lets the agent modify its own source, and OAuth logins cover Claude, Codex, Gemini, and Copilot alongside 30+ API providers and local vLLM endpoints.
