---
name: "SWE-agent Paper"
slug: "swe-agent-paper"
layout: "agent.njk"
category: "other"
maker: null
license: "arXiv paper (code MIT at swe-agent.com)"
url: "https://arxiv.org/abs/2405.15793"
source_code_url: null
source_available: "True"
platforms: []
first_released: null
current_release: null
stars: null
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
install_method: null
docs_url: "https://arxiv.org/abs/2405.15793"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brandonhimpfen"
what_makes_it_special: "Introduces Agent-Computer Interface (ACI) tailored to LM agents for software engineering; achieved SOTA on SWE-bench (12.5% pass@1) and HumanEvalFix (87.7% pass@1); demonstrates that ACI design significantly affects agent behavior and performance."
---

The SWE-agent paper (Yang, Jimenez, Wettig, Lieret, Yao, Narasimhan, Press; Princeton) argued that language models acting on code repositories are a new class of computer user and therefore need purpose-built interfaces, analogous to how IDEs serve human developers. It formalized the Agent-Computer Interface concept: compact file viewers, search tools with bounded output, and guarded edit commands that constrain the agent away from error-prone interaction patterns. The resulting system set state-of-the-art results at publication — 12.5% pass@1 on SWE-bench and 87.7% on HumanEvalFix — and the paper demonstrated that interface design choices materially change agent performance independent of the underlying model. The paper seeded the SWE-agent codebase, the SWE-bench ecosystem, and the ACI design vocabulary that subsequent open-source harnesses still build on.
