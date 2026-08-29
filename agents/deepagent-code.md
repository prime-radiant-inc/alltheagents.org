---
name: "deepagent-code"
slug: "deepagent-code"
layout: "agent.njk"
category: "agent"
maker: "deepagent-ltd"
license: "AGPL-3.0-or-later (derived from opencode under MIT)"
url: "https://github.com/deepagent-ltd/deepagent-code"
source_code_url: "https://github.com/deepagent-ltd/deepagent-code"
source_available: "True"
platforms: []
first_released: "2026-06-23"
current_release: "2026-08-14"
stars: "437"
language: "TypeScript"
homepage: "https://ai.deepagent.ltd/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "OpenAI, Anthropic, DeepSeek, Google, xAI, ZhipuAI/GLM, OpenAI-compatible, Anthropic-compatible (75+ providers via AI SDK + models.dev)"
pricing: null
install_method: "curl -fsSL https://deepagent.ltd/install | bash (macOS/Linux); or desktop app; npm package not yet publicly published"
docs_url: "https://deepagent-code.ai/docs/providers/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://deepagent.ltd/install"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "AI coding agent/workspace with durable governed memory (typed, versioned documents with provenance); four-graph unified store (code + knowledge + memory + docs); live steering during running tasks; three collaboration modes (Auto/Loop/Design); Expert Panel for high-risk decisions; LSP-based AI IDE with 38 language servers"
---

deepagent-code targets work that spans more than one prompt: long-running tasks where the agent must remember decisions, constraints, and past failures across sessions. It builds on opencode and adds a control plane where project memory is stored as typed, versioned documents with provenance rather than prompt text, and where four graph stores (code symbols, knowledge, memory, documents) feed a shared context assembly with admission gates. During execution, users can steer live goals without aborting in-flight work, and subagents run in isolated worktrees under a generation-fenced lifecycle with review sessions; an Expert Panel mode runs bounded adversarial debate between specialist lenses. It is AGPL-3.0 with a separate enterprise distribution, BYO-model-keys across 75+ providers, and targets teams who need auditable, steerable agent behavior over codebases.
