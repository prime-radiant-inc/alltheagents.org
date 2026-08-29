---
name: "valuecell"
slug: "valuecell"
layout: "agent.njk"
category: "other"
maker: "ValueCell-ai"
license: "Apache-2.0"
url: "https://github.com/ValueCell-ai/valuecell"
source_code_url: "https://github.com/ValueCell-ai/valuecell"
source_available: "True"
platforms: []
first_released: "2025-09-01"
current_release: "2026-03-09"
stars: "11003"
language: "Python, React"
homepage: "https://valuecell.ai"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenRouter, SiliconFlow, Azure, OpenAI, Google, DeepSeek"
pricing: "BYOK"
install_method: "binary"
docs_url: "https://github.com/ValueCell-ai/valuecell/blob/main/docs/CONFIGURATION_GUIDE.md"
plugin_docs_url: null
config_docs_url: "https://github.com/ValueCell-ai/valuecell/blob/main/docs/CONFIGURATION_GUIDE.md"
download_url: "https://github.com/ValueCell-ai/valuecell"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Community-driven multi-agent platform for financial applications (stock selection, research, tracking, trading). Live exchange routing (Binance, OKX, Hyperliquid) with built-in guardrails. All sensitive user data stored locally. Multi-agent system with DeepResearch, Strategy, and News Retrieval agents. Plugin architecture and Agent Registry planned for third-party agents."
---

ValueCell applies the multi-agent pattern to investing rather than software development: specialized agents perform fundamental document research, execute multi-strategy trading across crypto assets, and deliver scheduled personalized news, coordinated on a platform the community extends. Market data covers US, crypto, Hong Kong, and China markets, with live routing to Binance, OKX, and Hyperliquid (Coinbase, Gate.io, and MEXC partially tested) under built-in guardrails, and agents interoperate with LangChain and Agno through the A2A protocol. Sensitive data — LanceDB vectors, SQLite, the knowledge base — stays on the user's machine, while a hosted instance at valuecell.ai serves A-share research. Retail and semi-professional traders, particularly in Chinese markets, use it for research and strategy execution; it is Apache-2.0 licensed (original code), Python 3.12+ with a React frontend, and actively developed.
