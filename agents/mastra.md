---
name: "Mastra"
slug: "mastra"
layout: "agent.njk"
category: "agent-sdk"
maker: "mastra-ai"
license: "NOASSERTION"
url: "https://github.com/mastra-ai/mastra"
source_code_url: "https://github.com/mastra-ai/mastra"
source_available: "Yes"
platforms:
  - "CLI"
  - "Web"
first_released: "2024-08-06"
current_release: "2026-08-20"
stars: "27318"
language: "TypeScript"
homepage: "https://mastra.ai"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "40+ providers via unified model routing (OpenAI, Anthropic, Google, Groq, Cohere, local)"
pricing: "open-source"
install_method: "npm (npx create-mastra)"
docs_url: "https://mastra.ai/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/mastra"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "It is a TypeScript-native agent framework from the Gatsby creators: graph-based workflows with durable human-in-the-loop suspend/resume, Observational Memory, a Harness subsystem (workspace, shell tools, task tracking) for building coding agents, and MCP support in both directions - exposing Mastra agents as MCP servers and consuming external MCP servers."
---

Mastra gives TypeScript teams the primitives usually associated with Python agent frameworks: agents with tool calling and stopping conditions, workflows composed with .then()/.branch()/.parallel() that can suspend for human approval and resume with durable state, and memory that spans conversation history and retrieval. Model routing abstracts 40+ providers behind one interface, Mastra Studio provides a local UI for inspecting and testing agents, and evals integrate with deployment. A dedicated Harness subsystem packages workspace, shell tools, memory, and task tracking for building coding agents, and Mastracode skills integrate with Claude Code and Cursor. YC-backed and very actively maintained (27k+ stars), it targets product engineers embedding agents in applications.
