---
name: "MLE-STAR-Open"
slug: "mle-star-open"
layout: "agent.njk"
category: "agent"
maker: "WalkingDevFlag"
license: "MIT"
url: "https://github.com/WalkingDevFlag/MLE-STAR-Open"
source_code_url: "https://github.com/WalkingDevFlag/MLE-STAR-Open"
source_available: "True"
platforms: []
first_released: "2025-08-10"
current_release: "2026-06-16"
stars: "33"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "False"
model_providers: "OpenRouter (free-tier), Ollama (planned/deferred)"
pricing: "Free/open source; OpenRouter free-tier ~50 requests/day"
install_method: "git clone + conda env (Python 3.12) + pip install -r requirements.txt"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/WalkingDevFlag/MLE-STAR-Open"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Google-free, local-friendly unofficial reimplementation of MLE-STAR. No API keys required for search (DuckDuckGo) and leverages free-tier LLMs via OpenRouter, making multi-agent AutoML experimentation accessible without enterprise infrastructure. Multi-agent pipeline stages: initialization, refinement, ensembling, submission."
---

MLE-STAR demonstrated that search-and-refine loops make LLM agents competitive at machine-learning engineering, but the reference implementation depended on Google infrastructure. MLE-STAR-Open reimplements the pipeline for constrained setups: an initialization agent produces a first solution for a tabular task, refinement agents target specific components identified through web search (DuckDuckGo, no API key), an ensembling stage merges the best candidates, and a submission stage formats predictions.csv for Kaggle. Runs execute through OpenRouter's OpenAI-compatible API on free-tier models, with automated data-leakage and usage checks guarding the generated pipelines and a minimal low-token runner for cheap iteration. Each task gets a workspace directory holding init, refine, ensemble, predictions, and logs. Kaggle competitors and ML practitioners use it to experiment with agent-driven AutoML on a budget, accepting its constraints — roughly 50 free requests per day, an eight-commit codebase from a single maintainer, and an Ollama adapter still deferred.
