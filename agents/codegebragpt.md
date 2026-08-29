---
name: "Codegebragpt"
slug: "codegebragpt"
layout: "agent.njk"
category: "other"
maker: "sr5434"
license: "MIT"
url: "https://github.com/sr5434/CodegebraGPT"
source_code_url: "https://github.com/sr5434/CodegebraGPT"
source_available: "True"
platforms: []
first_released: "2023-12-17"
current_release: "2023-12-29"
stars: null
language: "Jupyter Notebook"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Upstage SOLAR-10.7B-Instruct-v1.0"
pricing: "free"
install_method: null
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Fine-tunes SOLAR-10.7B-Instruct-v1.0 using QLoRA on ~100k STEM samples (math, physics, chemistry, biology, CS/ML, code). Not a coding agent harness -- it is an LLM fine-tuning project."
---

CodegebraGPT is a student-scale fine-tuning project aiming to adapt the SOLAR-10.7B-Instruct model to STEM reasoning. The plan combined roughly 100,000 samples from MetaMath, Camel-AI science datasets, arXiv math and physics/CS subsets, GSM8K, MMLU, Evol Instruct Code, and Glaive Code Assistant into a training corpus published separately at sr5434/CodegebraGPT_data, with QLoRA chosen so a single consumer GPU could run the training. The repository consists mainly of two notebooks — dataset preparation and QLoRA training — plus a README describing the procedure as planned, and no fine-tuned model release is evident. The name continues the author's earlier Codegebra equation-solving program, repositioned around a natural-language interface.
