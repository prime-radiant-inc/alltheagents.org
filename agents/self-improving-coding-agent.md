---
name: "self_improving_coding_agent"
slug: "self-improving-coding-agent"
layout: "agent.njk"
category: "agent"
maker: "MaximeRobeyns"
license: "MIT"
url: "https://github.com/MaximeRobeyns/self_improving_coding_agent"
source_code_url: "https://github.com/MaximeRobeyns/self_improving_coding_agent"
source_available: "True"
platforms: []
first_released: "2025-04-11"
current_release: "2025-04-23"
stars: "385"
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: "False"
subagents: "True"
hooks: null
plan_mode: null
model_providers: "Anthropic, OpenAI, Gemini, Vertex (GCP), Fireworks AI, DeepSeek, Modal"
pricing: "Free / open-source"
install_method: "git clone, export API keys, make image, pip install -r base_agent/requirements.txt"
docs_url: "https://openreview.net/pdf?id=rShJCyLsOr"
plugin_docs_url: null
config_docs_url: "base_agent/src/config.py"
download_url: "https://github.com/MaximeRobeyns/self_improving_coding_agent"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Self-improving coding agent that runs an iterative loop (evaluate on benchmarks, store results, modify its own codebase, repeat), bootstrapping capabilities without human intervention. Research artifact from ICLR 2025 Workshop."
---

The project operationalizes a simple question: if a coding agent can modify code, what happens when its own source is the task? Each iteration evaluates the current agent on benchmark tasks, stores the results, then has the agent edit its repository to improve, with the loop repeating without human intervention; an ICLR 2025 workshop paper documents the method. The base agent is intentionally minimal — no tree-sitter, LSP, or sophisticated planning — because the point is to observe bootstrapped specialization on the bundled SWE-bench-style tasks, not to ship a product. Everything runs inside a provided Docker image because the agent executes arbitrary shell commands, and the authors are explicit about that safety boundary. Providers span Anthropic, OpenAI, Gemini, Vertex, Fireworks, and DeepSeek. As a frozen two-commit research artifact with a citable paper, its audience is researchers studying self-improvement, not practitioners.
