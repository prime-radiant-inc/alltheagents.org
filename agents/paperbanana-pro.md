---
name: "PaperBanana-Pro"
slug: "paperbanana-pro"
layout: "agent.njk"
category: "other"
maker: "elpsykongloo"
license: "Apache-2.0"
url: "https://github.com/elpsykongloo/PaperBanana-Pro"
source_code_url: "https://github.com/elpsykongloo/PaperBanana-Pro"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2026-03-11"
current_release: "2026-05-19"
stars: "95"
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: "False"
subagents: "True"
hooks: null
plan_mode: null
model_providers: "Gemini, OpenAI, OpenRouter, Evolink, custom OpenAI-compatible"
pricing: "Free / open-source (users supply their own API keys)"
install_method: "git clone, uv sync --locked, uv tool install --editable . --force"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Production-grade multi-agent academic illustration engine (full Chinese UI) that generates scientific illustrations and statistical plots from paper method sections; 6 sub-agents (Retriever, Planner, Stylist, Visualizer, Critic, Polish); 21 rounds of engineering polish + 70+ unit tests; Bundle v1 portable format (.bundle.json); 2K/4K refinement with tree-structured version chains and rollback; fault-tolerant retry with Pro-to-Flash model tier degradation; Pipeline Registry for one-line workflow extension. NOTE: Google holds a patent on the multi-agent pipeline methodology; commercial use prohibited."
---

PaperBanana-Pro automates the illustrations and statistical plots researchers otherwise draw by hand from a paper's method section. Six pipeline stages retrieve few-shot references, plan a structured visual description, enforce stylistic consistency, render images or Matplotlib code, critique across multiple rounds, and apply final polish, with a full-Chinese Streamlit GUI and CLI front ends. Outputs ship in a portable Bundle v1 format with tree-structured 2K/4K refinement chains and rollback, and a registry allows new pipelines to be registered in one line. The project is Apache-2.0 licensed but non-commercial, since the multi-agent pipeline methodology was developed during the author's Google internship and is patent-pending by Google. Its users are researchers preparing figures, mostly in Chinese-language academia.
