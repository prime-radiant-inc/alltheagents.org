---
name: "Monocle"
slug: "monocle"
layout: "agent.njk"
category: "other"
maker: "arphanetx"
license: "GPL-3.0"
url: "https://github.com/arphanetx/Monocle"
source_code_url: "https://github.com/arphanetx/Monocle"
source_available: "True"
platforms: []
first_released: "2024-04-10"
current_release: "2024-04-10"
stars: "165"
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Mistral AI (Mistral-7B-Instruct-v0.2)"
pricing: "Free/open-source"
install_method: "pip install -r requirements.txt && python -m pip install . (requires Nvidia CUDA and Ghidra)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "LLM-backed natural-language search over compiled target binaries; uses Ghidra headless decompilation plus an in-built Mistral-7B-Instruct model to identify and score (0-10) functions matching natural-language search criteria, with an explanation for each finding."
---

Monocle addresses the cold-start problem in reverse engineering: facing an unknown binary, an analyst needs to locate code of interest — authentication logic, vulnerability patterns, password handling — without any prior map of the program. The tool runs Ghidra in headless mode to decompile the target, then passes the decompiled functions through a locally hosted Mistral-7B-Instruct model that scores each function 0-10 against the user's natural-language criteria and explains every nonzero score. Output arrives as a live-sorted table, so an analyst can steer the investigation as results appear rather than waiting for a batch run. It targets security researchers and reverse engineers with GPU-equipped workstations (Nvidia CUDA recommended, 16 GB RAM), and it runs entirely offline — an intentional property for analyzing untrusted or sensitive binaries. The repository saw a single burst of activity in April 2024 with no releases since, so it survives as a niche research artifact.
