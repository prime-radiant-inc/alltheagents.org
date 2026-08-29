---
name: "GLM-5"
slug: "glm-5"
layout: "agent.njk"
category: "other"
maker: "zai-org"
license: "Apache-2.0"
url: "https://github.com/zai-org/GLM-5"
source_code_url: "https://github.com/zai-org/GLM-5"
source_available: "True"
platforms: []
first_released: "2026-02-09"
current_release: "2026-08-11"
stars: "7007"
language: "Python"
homepage: "https://z.ai/blog/glm-5.2"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Z.ai API platform, z.ai chat, open weights on Hugging Face/ModelScope"
pricing: "open-source"
install_method: "binary"
docs_url: "https://docs.z.ai/guides/llm/glm-5.2"
plugin_docs_url: null
config_docs_url: null
download_url: "https://huggingface.co/zai-org/GLM-5"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Series of large language models (GLM-5/5.1/5.2) targeting complex systems engineering and long-horizon agentic tasks. GLM-5.2 delivers a solid 1M-token context, 744B params (40B active), IndexShare architecture reducing per-token FLOPs 2.9x at 1M context, and DeepSeek Sparse Attention. Best-in-class open-source coding/agentic performance."
---

The GLM-5 series (GLM-5, 5.1, 5.2, 5.3, 5.3-Flash) is Z.ai's open-weight model line aimed squarely at coding and long-horizon agentic workloads, with 28.5T pre-training tokens, DeepSeek Sparse Attention, and an IndexShare architecture that cuts per-token FLOPs 2.9x at million-token context. The repository ships weights (BF16 and FP8 variants on Hugging Face and ModelScope) plus serving and fine-tuning recipes for SGLang, vLLM, Transformers, and KTransformers, with hosted access via the Z.ai API platform. Benchmarks position it as the leading open-source model for coding and long-horizon agent tasks. In this census it is a model, not a harness: the agentic loops live in downstream tools that consume these weights.
