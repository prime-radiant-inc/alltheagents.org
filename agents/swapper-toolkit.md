---
name: "swapper-toolkit"
slug: "swapper-toolkit"
layout: "agent.njk"
category: "other"
maker: "swapperfinance"
license: "MIT"
url: "https://github.com/swapperfinance/swapper-toolkit"
source_code_url: "https://github.com/swapperfinance/swapper-toolkit"
source_available: "True"
platforms: []
first_released: "2026-03-23"
current_release: "2026-04-07"
stars: "846"
language: "JavaScript/TypeScript"
homepage: "https://swapper.finance"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "yes"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "any (model-agnostic)"
pricing: "open-source"
install_method: "npm (npx skills add)"
docs_url: "https://docs.swapper.finance/ai-agents/skills"
plugin_docs_url: "https://docs.swapper.finance/ai-agents/skills"
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "A DeFi payment layer for AI agents — lets coding assistants deposit fiat/crypto, bridge cross-chain via Chainlink CCIP, and fund DeFi protocols directly. Fiat on-ramp in 170+ countries, 10 chains supported, explicit confirmation model (no auto-approved transactions, keys never stored). Uses the open skills standard."
---

swapper-toolkit addresses the fact that coding agents and autonomous agents have no native way to move money: it ships as Claude-standard skills (installable via npx skills add) that let assistants deposit funds through a fiat on-ramp in 170+ countries, bridge across Ethereum, Base, Arbitrum, Solana, BNB Chain and others through Chainlink CCIP, and fund DeFi protocols directly. Only the deposit skill is live so far — trading and wallet management are listed as coming soon — and every transaction requires explicit user confirmation with keys never stored, using Chainlink CRE and Mastercard rails under the hood. It integrates with Claude Code, Cursor, Windsurf, Copilot, CrewAI, and AutoGPT through the skills standard plus an npm SDK. The repository is young (eight commits), so it is best treated as an early integration layer rather than mature infrastructure.
