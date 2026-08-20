---
name: "SceneGenAgent"
slug: "scenegenagent"
layout: "agent.njk"
category: "agent"
maker: "THUDM"
license: "Apache-2.0"
url: "https://github.com/THUDM/SceneGenAgent"
source_code_url: "https://github.com/THUDM/SceneGenAgent"
source_available: True
platforms: []
first_released: "2024-10-29"
current_release: "2024-11-29"
stars: "37"
language: "Python (generates C# code)"
homepage: null
mcp_support: null
plugin_support: False
claude_code_plugin: False
subagents: False
hooks: null
plan_mode: null
model_providers: "GPT-4o, Llama3.1-70B (fine-tuned via SceneInstruct); API-based and offline models"
pricing: "Free / open-source (research project)"
install_method: "git clone https://github.com/THUDM/SceneGenAgent.git; cd SceneGenAgent; pip install -r requirements.txt"
docs_url: "https://arxiv.org/abs/2410.21909"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/THUDM/SceneGenAgent"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "LLM agent that generates industrial scenes through executable C# code with precise quantitative control (measurements/positioning), structured/calculable format, layout verification, and iterative refinement; ships SceneInstruct, a dataset for fine-tuning open-source LLMs that lifts Llama3.1-70B to approach GPT-4o performance; achieves up to 81.0% success rate on real-world industrial tasks. ACL 2025 Main paper."
---

LLM agent that generates industrial scenes through executable C# code with precise quantitative control (measurements/positioning), structured/calculable format, layout verification, and iterative refinement; ships SceneInstruct, a dataset for fine-tuning open-source LLMs that lifts Llama3.1-70B to approach GPT-4o performance; achieves up to 81.0% success rate on real-world industrial tasks. ACL 2025 Main paper.
