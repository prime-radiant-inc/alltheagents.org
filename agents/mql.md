---
name: "Mql"
slug: "mql"
layout: "agent.njk"
category: "other"
maker: "shurutech"
license: "MIT"
url: "https://github.com/shurutech/mql"
source_code_url: "https://github.com/shurutech/mql"
source_available: "True"
platforms: []
first_released: "2023-09-08"
current_release: "2026-02-25"
stars: "213"
language: "Python, Node.js"
homepage: "https://shurutech.com/mql-sql-from-natural-language-with-85-accuracy/"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI"
pricing: null
install_method: "Docker (make install) or local setup (./setup.sh)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/shurutech/mql"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "MQL (My Query Language) transforms natural language queries into executable SQL queries; users connect their database or upload schema, ask queries in natural language, and receive generated SQL."
---

MQL, from Shuru, addressed the analyst's recurring bottleneck: querying a database requires SQL fluency that most business users lack. Users connect a PostgreSQL database or upload a schema, type questions in plain language, and receive generated SQL, with pgvector-based retrieval over schema context improving generation quality and an OpenAI API key supplying the model. A built-in accuracy harness against a sample e-learning database — 43 of 50 queries correct, about 74% executing cleanly — made the tool unusually honest about its limits, publishing its own failure rate. The web dashboard supports user login and query review, and Docker or a setup script handles deployment. The roadmap items listed in the README (query execution, MySQL support, visualizations, Slack integration) were never implemented, and the repository has seen no sustained activity since its 2023 debut, leaving it as an early NL-to-SQL prototype rather than a maintained product.
