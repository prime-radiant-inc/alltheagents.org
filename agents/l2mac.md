---
name: "L2MAC"
slug: "l2mac"
layout: agent.njk
category: agent
maker: "samholt"
license: "MIT"
url: "https://github.com/samholt/l2mac"
source_code_url: "https://github.com/samholt/l2mac"
source_available: "Yes"
platforms: []
first_released: "2024-03-08"
current_release: "2024-12-27"
stars: 158
language: "Python"
homepage: "https://samholt.github.io/L2MAC/"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: null
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: null
sources:
  - "e2b"
---

L2MAC is a multi-agent generation framework that, a single input prompt can generate an extensive unbounded output, such as an entire codebase or an entire book. - L2MAC can create near unbounded outputs that align exactly with the user input prompt over very long generation tasks - It achieves strong empirical performance of state-of-the-art generation for large codebase tasks and is in the top 3 for the HumanEval coding global benchmark. As L2MAC can detect invalid code and failing unit tests when generating code and automatically error corrects them. - Internally persists a complete file-store memory that enables LLM agents to read files and write to files, creating a large output over many iterations - It can be instructed to follow an exact prompt program - As it generates the output one part at a time, it enables an LLM with a fixed context token limit to be bypassed - The paper, peer-reviewed and recently accepted and published at ICLR 2024, introduces L2MAC.
