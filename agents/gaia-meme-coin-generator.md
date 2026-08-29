---
name: "Gaia-Meme-Coin-Generator"
slug: "gaia-meme-coin-generator"
layout: "agent.njk"
category: "other"
maker: "harishkotra"
license: "MIT"
url: "https://github.com/harishkotra/gaia-meme-coin-generator"
source_code_url: "https://github.com/harishkotra/gaia-meme-coin-generator"
source_available: "True"
platforms: []
first_released: "2024-11-24"
current_release: "2024-11-24"
stars: "2"
language: "JavaScript"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Gaia AI node (llama3b via https://llama3b.gaia.domains/v1)"
pricing: "Free / open-source (MIT)"
install_method: "git clone https://github.com/harishkotra/gaia-meme-coin-generator && cd gaia-meme-coin-generator && npm install; create .env with GAIA_URL, GAIA_MODEL, BASE_NODE_URL, PRIVATE_KEY; npm start"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/harishkotra/gaia-meme-coin-generator"
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "AI-powered creative token naming and automatic tokenomics generation using Gaia's AI Agent. Deploys secure ERC20 contracts with built-in anti-whale protections (max transaction limits, max wallet limits, CEX/DEX exclusions). Full deployment record saved to JSON. Built for Base Sepolia testnet. Only 3 commits — hackathon/proof-of-concept project."
---

The tool automates the mechanical parts of launching a testnet meme token: a Gaia-hosted Llama 3B node proposes the branding and supply limits, and a fixed contract template with max-transaction, max-wallet, and exchange-exclusion guards is compiled and deployed to Base Sepolia. Configuration flows through environment variables for the Gaia endpoint, model, RPC node, and deployer key, and the full deployment record lands in a JSON file. Three commits, no releases, and a testnet-only disclaimer mark it as a November 2024 hackathon proof of concept demonstrating Gaia node integration rather than a maintained product.
