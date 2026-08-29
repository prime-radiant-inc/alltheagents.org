---
name: "building-intelligent-apps-with-anaconda"
slug: "building-intelligent-apps-with-anaconda"
layout: "agent.njk"
category: "other"
maker: "Anaconda-Labs"
license: "MIT"
url: "https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda"
source_code_url: "https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda"
source_available: "True"
platforms: []
first_released: "2026-04-13"
current_release: "2026-08-17"
stars: "228"
language: "Python"
homepage: "https://www.anaconda.com/docs/getting-started"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: "Anthropic,AI Navigator,vLLM,Anaconda Platform,NVIDIA Nemotron"
pricing: "Free curriculum"
install_method: "conda env create -f <module>/environment.yml per module"
docs_url: "https://www.anaconda.com/docs/getting-started"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda"
maintained: "active"
sources:
  - "github_final"
what_makes_it_special: "Hands-on 10-part curriculum for building production-grade intelligent applications using the Anaconda ecosystem, covering data analysis, AI agents, multi-agent orchestration, deployment, GPU acceleration, and native/web app delivery."
---

This repository is a structured, hands-on curriculum for building production-grade AI applications on the Anaconda stack, produced by Anaconda Labs as demonstration material for PyCon US 2026. Its ten modules walk from environment management and data ingestion through a first LangGraph agent, multi-agent orchestration with a Metaflow supervisor, deployment and inference (AI Navigator, vLLM, Anaconda Platform), GPU acceleration with CUDA and Nemotron, and delivery as native or web apps — each module a short narrated demo with pre-run outputs or a run script. The intended audience is engineers and data scientists evaluating the Anaconda ecosystem for real projects, and the material doubles as Anaconda's own showcase of its tooling (conda, AI Navigator, Anaconda Platform) in agentic workloads. As a curriculum it ships no tool of its own; the code exists to be studied and adapted, which places it in the census as educational 'other' rather than an agent.
