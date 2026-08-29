---
name: "SWE-Gym"
slug: "swe-gym"
layout: "agent.njk"
category: "other"
maker: "SWE-Gym"
license: "Apache-2.0"
url: "https://github.com/SWE-Gym/SWE-Gym"
source_code_url: "https://github.com/SWE-Gym/SWE-Gym"
source_available: "yes"
platforms: []
first_released: "2024-11-04"
current_release: "2025-07-29"
stars: "722"
language: "Python"
homepage: "https://arxiv.org/abs/2412.21139"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "GPT-4o and Claude 3.5 Sonnet trajectories; fine-tunes OpenHands/Moatless 7B/32B agents"
pricing: "open-source"
install_method: "docker"
docs_url: "https://arxiv.org/abs/2412.21139"
plugin_docs_url: null
config_docs_url: null
download_url: "https://huggingface.co/SWE-Gym"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "First open environment for training and verifying real-world software engineering agents. Contains 2.4K real tasks from 11 Python repositories with pre-built Docker images. Achieved a new open state-of-the-art (32% on SWE-Bench Verified, 26% on SWE-Bench Lite). ICML 2025 accepted. Combines repository context, executable environments, and test verification."
---

SWE-Gym was built to give agent researchers what SWE-bench gave evaluators: an executable, verifiable training ground. It packages 2,438 real tasks from 11 popular Python repositories, each with repository context, a pre-built Docker environment, and executable tests that decide success, so agents train against ground-truth reward rather than model judgment. The accompanying work showed that fine-tuning a 32B model on fewer than 500 agent-environment trajectories raised SWE-bench Verified by 14 points, and that verifiers trained on the same trajectories enabled best-of-n inference-time scaling to 32% Verified and 26% Lite — the open state of the art at publication (ICML 2025). Reproduction is documented for both the OpenHands and MoatlessTools scaffolds. ML researchers training or verifying SWE agents are the users, and the environment later seeded task-generation efforts like SWE-smith.
