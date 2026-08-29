---
name: "ToM-SWE"
slug: "tom-swe"
layout: "agent.njk"
category: "other"
maker: "OpenHands"
license: "MIT"
url: "https://github.com/OpenHands/ToM-SWE"
source_code_url: "https://github.com/OpenHands/ToM-SWE"
source_available: "True"
platforms: []
first_released: "2025-06-30"
current_release: "2026-08-03"
stars: "119"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "LiteLLM"
pricing: "open-source"
install_method: "pip install tom-swe"
docs_url: "https://docs.google.com/document/d/1P8b1SSF_HYgahK6eO7qSHbOcTv3o3z6SWMH_osyR3_w/edit"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/tom-swe/"
maintained: "dead"
sources:
  - "github_topic2"
what_makes_it_special: "Theory of Mind package that enhances SWE agents with personalized user understanding via three-tier memory (cleaned sessions -> session analyses -> user profiles); LLM-powered psychological insights; TomCodeActAgent integrates with OpenHands; academic research project (ICLR 2026) bridging cognitive science with software engineering AI agents."
---

ToM-SWE, an All Hands AI research project published toward ICLR 2026, applies theory of mind to software-engineering agents: instead of treating every request as context-free, it builds a model of the specific user over time. A three-tier memory pipeline distills raw sessions into cleaned sessions, then session analyses, then cumulative user profiles capturing preferences and working style; agents consult these profiles for personalized guidance, and an LLM layer generates the psychological insights that populate them. The package ships as pip-installable tom-swe, integrates with OpenHands through a TomCodeActAgent that automatically enriches instructions with user context, and works through LiteLLM so any provider can back the modeling. It is a research contribution (ICLR 2026) bridging cognitive science and SWE agents; the repository was archived in August 2026 and is read-only, so the project is complete rather than maintained.
