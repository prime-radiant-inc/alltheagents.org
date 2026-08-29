---
name: "multi-agent-training-grpo"
slug: "multi-agent-training-grpo"
layout: "agent.njk"
category: "other"
maker: "FareedKhan-dev"
license: "MIT"
url: "https://github.com/FareedKhan-dev/multi-agent-training-grpo"
source_code_url: "https://github.com/FareedKhan-dev/multi-agent-training-grpo"
source_available: "True"
platforms: []
first_released: "2026-02-09"
current_release: "2026-02-09"
stars: "57"
language: "Python"
homepage: "https://medium.com/@fareedkhandev/building-modern-ai-agentic-systemagentic-system-optimization-for-effective-planning-and-tool-f698e831d730"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "vLLM (local), OpenAI API, Google Gemini API, Qwen models"
pricing: "Free/open source (educational)"
install_method: "pip install dependencies (vllm, openai, pydantic, tenacity, beautifulsoup4, wikipedia, google-genai, transformers, peft, etc.)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Implements GRPO (Generalized Reinforced Policy Optimization) algorithm to train multi-agent systems, improving planning and reducing hallucinations in long-horizon tasks through group-based trajectory evaluation and relative advantage learning."
---

The repository teaches a specific technique: reinforcement learning applied to the planning component of an agent system, using GRPO's group-relative advantage computation to improve long-horizon task performance. Three notebooks walk the full path — combining DeepMath-103K math problems with Natural Questions queries into training data, building a Planner/Executor/Verifier agent system over a vLLM-hosted Qwen model with sandboxed Python execution and search tools, and then training the planner with GRPO where GPT-4o scores trajectory outcomes and group-relative advantages drive policy updates through QLoRA on a single A100. The demo deliberately shows the untrained planner hallucinating — wrong tool order, wrong conclusions — before training. It is a blog-post companion from a prolific tutorial author, six commits and dormant, intended for readers learning how RL fits into agentic systems rather than for any production use.
