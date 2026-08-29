---
name: "marg-reviewer"
slug: "marg-reviewer"
layout: "agent.njk"
category: "other"
maker: "allenai"
license: "Apache-2.0"
url: "https://github.com/allenai/marg-reviewer"
source_code_url: "https://github.com/allenai/marg-reviewer"
source_available: "True"
platforms: []
first_released: "2023-12-20"
current_release: "2026-03-05"
stars: "64"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "no"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI"
pricing: "Free / open source (Apache-2.0)"
install_method: "Docker (docker compose up --build, requires OPENAI_API_KEY in .env)"
docs_url: "https://arxiv.org/pdf/2401.04259"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/allenai/marg-reviewer"
maintained: "dormant"
sources:
  - "github_topic4"
what_makes_it_special: "MARG (Multi-Agent Review Generation) — generates peer reviews for scientific papers using multiple AI agent strategies (SARG-B, LiZCa, MARG-S)"
---

The repository accompanies Allen AI's study of whether multi-agent LLM pipelines can produce useful scientific peer reviews, providing the web interface used in the paper's user study alongside scripts that reproduce its alignment experiments on the ARIES dataset. A reviewer submits a paper through the Dockerized web interface, and the backend generates reviews through one of three agent strategies whose outputs the paper compares. It also includes the GPT request cache and configurations needed to replicate the paper's metrics. The artifact serves NLP researchers studying review generation; it has seen only seven commits and no maintenance since.
