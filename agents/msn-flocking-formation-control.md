---
name: "MSN-Flocking-Formation-Control"
slug: "msn-flocking-formation-control"
layout: "agent.njk"
category: "other"
maker: "arjunhw97"
license: null
url: "https://github.com/arjunhw97/MSN-Flocking-Formation-Control"
source_code_url: "https://github.com/arjunhw97/MSN-Flocking-Formation-Control"
source_available: "True"
platforms: []
first_released: "2020-08-31"
current_release: "2021-01-06"
stars: "44"
language: "MATLAB"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "Free / open source"
install_method: "Install MATLAB, copy Source Code directory to MATLAB directory, run files MSN1.m through MSN5.m"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/arjunhw97/MSN-Flocking-Formation-Control"
maintained: "dormant"
sources:
  - "github_topic4"
what_makes_it_special: "MATLAB program implementing multi-agent flocking control for Mobile Sensor Networks (MSN), including target following and obstacle avoidance. Simulates flocking of 100 sensor nodes across 5 scenarios: network fragmentation, quasi-lattice formation with static target, dynamic target following sine wave trajectory, dynamic target following circular trajectory, obstacle avoidance. NOTE: This is a robotics/sensor-network simulation, NOT an AI coding agent harness."
---

This entry is a census false positive: the word 'agent' in its name refers to mobile sensor nodes, not AI agents. The repository implements a multi-agent flocking control algorithm from a control-theory paper in MATLAB, simulating 100 sensor nodes that maintain formation spacing while tracking a target node across five scenarios — network fragmentation, static and dynamic target following, and obstacle avoidance. Each scenario runs as a standalone MATLAB script (MSN1.m through MSN5.m) requiring nothing beyond a MATLAB installation; there are no LLMs, no tool loops, and no software-engineering capability anywhere in the code. The project dates from 2020 with its last change in January 2021 and serves students studying formation control. For the census's purposes it belongs to neither the agent nor multiplexer categories — it is robotics simulation captured by a keyword-driven crawl.
