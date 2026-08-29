---
name: "Strands Agents SDK"
slug: "strands-agents-sdk"
layout: "agent.njk"
category: "agent-sdk"
maker: "strands-agents"
license: "Apache-2.0"
url: "https://github.com/strands-agents/sdk-python"
source_code_url: "https://github.com/strands-agents/sdk-python"
source_available: "True"
platforms:
  - "Web"
first_released: "2025-05-14"
current_release: "2026-08-19"
stars: "6956"
language: "Python, TypeScript"
homepage: "http://strandsagents.com/"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "n/a"
subagents: "yes"
hooks: "yes"
plan_mode: "no"
model_providers: "Amazon Bedrock, Anthropic, OpenAI, Google Gemini, Ollama"
pricing: "open-source"
install_method: "pip, npm"
docs_url: "https://strandsagents.com/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jim"
  - "caramaschi"
what_makes_it_special: "Model-driven SDK taking a minimal-code approach to building agents. Model-agnostic (any model, any cloud; swap backends without code changes). Agent loop traces every decision; hooks intercept any step to log/validate/redirect; guardrails catch mistakes before execution with self-correction via steering handlers. Built-in MCP, streaming, multi-agent patterns, and structured output. Dual Python and TypeScript SDKs."
---

Strands takes a model-driven position: instead of orchestrating explicit workflows, the developer writes a few lines, the model chooses tools, and the SDK runs the loop with production controls around it — turn limits, token budgets, cancellation, stop-reason handling, structured output, streaming, session memory, and guardrails that catch mistakes before execution. Hooks intercept any step for logging, validation, or redirection, and steering handlers let an agent self-correct rather than fail; multi-agent patterns are first-class alongside a dedicated strands-mcp server package. First-class providers are Amazon Bedrock (default), Anthropic, OpenAI, and Gemini, with the SDK running entirely in-process and no hosted control plane. The Python and TypeScript SDKs share a monorepo with a docs site at strandsagents.com, and the project evolved from an internal AWS tool into a broadly used open-source framework.
