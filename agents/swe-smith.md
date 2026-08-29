---
name: "SWE-smith"
slug: "swe-smith"
layout: "agent.njk"
category: "other"
maker: "SWE-bench"
license: "MIT"
url: "https://github.com/SWE-bench/SWE-smith"
source_code_url: "https://github.com/SWE-bench/SWE-smith"
source_available: "yes"
platforms: []
first_released: "2025-05-01"
current_release: "2026-08-17"
stars: "746"
language: "Python"
homepage: "https://swesmith.com/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Task synthesis and training use LLMs/Qwen-class open models; supports fine-tuning and GRPO RL"
pricing: "open-source"
install_method: "pip"
docs_url: "https://swesmith.com/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/swesmith/"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Toolkit that turns any GitHub repo into a SWE-gym with unlimited auto-generated task instances. Produced 52k task instances and 250+ Docker environments. Used to train SWE-agent-LM-32B achieving 40.2% pass@1 on SWE-bench Verified (+32%). NeurIPS 2025 D&B Spotlight. Supports both fine-tuning and GRPO-style reinforcement learning. Requires Docker; Ubuntu 22.04 only (no Windows/macOS)."
---

SWE-smith addresses the training-data bottleneck for software-engineering agents: real, human-written issues are scarce, so supervised and RL training stall. Its pipeline builds an executable environment for a repository, perturbs the code with programmatic and LLM-guided mutations until at least one unit test fails, and then generates a natural-language issue describing the break — yielding an endless supply of verified task instances with ground-truth tests. The released corpus includes 52,000 instances, more than 250 Docker environments, and 26,000 agent trajectories, and the resulting SWE-agent-LM-32B reached 40.2% pass@1 on SWE-bench Verified. The toolkit requires Docker and is developed on Ubuntu (macOS/Windows unsupported), with docs covering instance creation, harnesses, and training recipes. Data engineers and researchers building SWE training sets are its users.
