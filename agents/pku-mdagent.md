---
name: "PKU_MDAgent"
slug: "pku-mdagent"
layout: "agent.njk"
category: "agent"
maker: "FredericVAN"
license: "GPL-3.0"
url: "https://github.com/FredericVAN/PKU_MDAgent"
source_code_url: "https://github.com/FredericVAN/PKU_MDAgent"
source_available: "True"
platforms: []
first_released: "2025-03-03"
current_release: "2026-06-19"
stars: "40"
language: "Python"
homepage: "https://www.nature.com/articles/s41598-025-92337-6"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "OpenAI, Ollama, Qwen"
pricing: "open-source"
install_method: "pip install -r requirements.txt (Python 3.11 recommended)"
docs_url: "https://fredericvan.github.io/PKU_MDAgent/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/FredericVAN/PKU_MDAgent"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Molecular Dynamics Agent — a fine-tuned LLM-based multi-agent system for generating, executing, and refining LAMMPS thermodynamic simulation code in materials science. Uses Actor-Critic model (Worker + Evaluator loop) with human-in-the-loop. Achieves 42.22% reduction in task time. Curated LAMMPS fine-tuning datasets. Supports fine-tuning and RAG. Built on AutoGen. Published in Scientific Reports. NOTE: This is a domain-specific research agent, not a general coding agent harness."
---

MDAgent came out of Peking University to automate molecular-dynamics simulation setup, where materials scientists otherwise hand-write and iteratively debug LAMMPS scripts to extract thermodynamic parameters like heat capacity and thermal conductivity. Built on Microsoft AutoGen, a Planner decomposes the task, a Worker agent generates LAMMPS code executed in Docker containers, and an Evaluator scores each script on a 0–10 deduction rubric, looping until scripts score at least 8, with humans able to intervene mid-loop. Domain knowledge enters through QLoRA fine-tuning on a published 167-script LAMMPS dataset (with an expert-scored benchmark, LEQS, alongside) and optional RagFlow-based retrieval. The paper reports a 42.22% reduction in task time, and the code, datasets, and a Panel web UI shipped alongside the Scientific Reports publication. Its users are computational materials-science researchers, and the code is a research artifact rather than a maintained product.
