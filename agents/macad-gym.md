---
name: "macad-gym"
slug: "macad-gym"
layout: "agent.njk"
category: "other"
maker: "praveen-palanisamy"
license: "MIT"
url: "https://github.com/praveen-palanisamy/macad-gym"
source_code_url: "https://github.com/praveen-palanisamy/macad-gym"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2019-05-14"
current_release: "2023-05-20"
stars: "373"
language: "Python"
homepage: "https://arxiv.org/abs/1911.04175"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "Free / open-source"
install_method: "pip install macad-gym (PyPI)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.python.org/pypi/macad-gym/"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Training platform for Multi-Agent Connected Autonomous Driving built on the CARLA simulator; OpenAI Gym-compatible environments for Deep RL in homogeneous/heterogeneous, communicating/non-communicating multi-agent driving settings; JSON-like configuration; multi-GPU support. (Not a coding agent — it's an autonomous driving RL environment.)"
---

MACAD-Gym packages the environment layer from a NeurIPS 2019 workshop paper on multi-agent connected autonomous driving, letting RL researchers train and evaluate driving policies in CARLA without writing simulator glue. Scenarios are configured declaratively, sensor and reward setups compose across homogeneous or heterogeneous agent populations, and the Gym-compatible interface means standard deep-RL training loops run unmodified. Autonomous-driving researchers reproducing or extending multi-agent RL experiments are the audience; the platform requires CARLA 0.9.x alongside the pip install. Development has been stable but inactive since 2023.
