---
name: "DeepGame"
slug: "deepgame"
layout: "agent.njk"
category: "other"
maker: "ismorphism"
license: "MIT"
url: "https://github.com/ismorphism/DeepGame"
source_code_url: "https://github.com/ismorphism/DeepGame"
source_available: "True"
platforms: []
first_released: "2019-04-02"
current_release: "2023-02-11"
stars: "42"
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "Clone rllab repo, sudo pip3 install -e . for rllab and maci plus dependencies"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/ismorphism/DeepGame"
maintained: "dormant"
sources:
  - "github_topic4"
what_makes_it_special: "Multi-agent reinforcement learning based on game theory. Implements Vanilla Q-learning and Nash Q-learning (Nash-equilibrium-seeking) algorithms in a grid world environment. NOTE: This is a reinforcement learning research project, not a coding agent harness."
---

DeepGame is a small research codebase for multi-agent reinforcement learning grounded in game theory, comparing vanilla Q-learning (each agent independently optimal) with Nash Q-learning, where agents seek Nash equilibria. Agents act in a configurable grid world through run_grid_game.py, with parameters for grid size, discounting, exploration, and learning rate, built on NumPy, Nashpy, and the mapr2/rllab stack. The README states plainly that the project is no longer actively developed, and the code was only ever tested with two agents. Its inclusion in a harness census is definitional only: no tool loop, no software construction, and no maintenance.
