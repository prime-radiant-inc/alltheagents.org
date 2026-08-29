---
name: "codeflash"
slug: "codeflash"
layout: "agent.njk"
category: "agent"
maker: "codeflash-ai"
license: "BSL-1.1"
url: "https://github.com/codeflash-ai/codeflash"
source_code_url: "https://github.com/codeflash-ai/codeflash"
source_available: "True"
platforms:
  - "IDE"
first_released: "2025-02-13"
current_release: "2026-08-17"
stars: "246"
language: "Python"
homepage: "https://www.codeflash.ai"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Codeflash's LLMs (via API key)"
pricing: "freemium"
install_method: "pip install codeflash"
docs_url: "https://docs.codeflash.ai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/codeflash/"
maintained: "active"
sources:
  - "github_topic5"
what_makes_it_special: "A general-purpose Python code optimizer that uses LLMs to generate multiple optimization ideas, tests them for correctness, benchmarks for performance, and creates merge-ready pull requests with the best optimization found. Used by teams at Pydantic, Roboflow, Unstructured, Langflow. Excels at optimizing AI agents, computer vision algorithms, PyTorch code, numerical code, and backend code. Available as VS Code Extension and GitHub Action."
---

Codeflash automates performance work that ordinarily waits for a human to profile, rewrite, and benchmark by hand. The tool generates multiple optimization candidates for Python functions with LLMs, checks each candidate against the existing test suite for correctness, benchmarks runtime against the original, and opens a pull request containing the fastest verified optimization. Teams run it continuously through a GitHub Action so new code gets optimized in every pull request, or run one-off optimizations over an existing codebase or script from the CLI and a VS Code extension. It focuses on performance rather than general development: typical targets include AI agent code, computer vision, PyTorch, numerical, and backend Python, and teams such as Pydantic, Roboflow, Unstructured, and Langflow use it. Access requires an API key from Codeflash's hosted service.
