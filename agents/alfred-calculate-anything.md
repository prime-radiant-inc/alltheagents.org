---
name: "Alfred-Calculate-Anything"
slug: "alfred-calculate-anything"
layout: "agent.njk"
category: "other"
maker: "biati-digital"
license: "MIT"
url: "https://github.com/biati-digital/alfred-calculate-anything"
source_code_url: "https://github.com/biati-digital/alfred-calculate-anything"
source_available: "True"
platforms: []
first_released: "2019-11-12"
current_release: "2024-02-20"
stars: "599"
language: "PHP"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "alfred"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://alfred.app/workflows/biatidigital/calculate-anything/"
maintained: "dead"
sources:
  - "jim"
what_makes_it_special: "Natural language calculator for Alfred 5 supporting currency (168 currencies), cryptocurrency (5,000+), units, data storage, percentages, px/em/rem/pt, time, and VAT via natural language queries (English, Spanish, Swedish) with customizable keywords and translations"
---

The workflow answers typed queries like '100 usd to eur' or '20% of 250' inside Alfred, using free fixer.io and CoinMarketCap API keys for currency and crypto rates and handling IEC-correct data units (MB vs MiB), VAT, and time/date math. Custom translations extend beyond the bundled English, Spanish, and Swedish. It requires PHP installed locally (brew install php), since Alfred does not manage the runtime. The repo was archived by its maintainer in July 2025 after 311 commits; it still works with Alfred 5 but receives no updates, and the maintained alternative is the community-published AlfredPkg listing.
