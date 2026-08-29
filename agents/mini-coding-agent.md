---
name: "mini-coding-agent"
slug: "mini-coding-agent"
layout: "agent.njk"
category: "agent"
maker: "rasbt"
license: "Apache-2.0"
url: "https://github.com/rasbt/mini-coding-agent"
source_code_url: "https://github.com/rasbt/mini-coding-agent"
source_available: "True"
platforms: []
first_released: "2026-04-02"
current_release: "2026-04-07"
stars: "1111"
language: "Python"
homepage: "https://magazine.sebastianraschka.com/p/components-of-a-coding-agent"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Ollama"
pricing: "open-source"
install_method: "binary"
docs_url: "https://magazine.sebastianraschka.com/p/components-of-a-coding-agent"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Intentionally minimal and readable coding agent harness designed for educational purposes to explain the six core components of a coding agent (live repo context, prompt cache reuse, structured tools/permissions, context reduction, transcripts/memory/resumption, bounded subagents). No runtime dependencies beyond the Python standard library. Runs locally via Ollama."
---

Raschka wrote mini-coding-agent as the runnable companion to his essay on the components of a coding agent, with the constraint that the entire harness fit in one readable file with no dependencies beyond the Python standard library. The loop sends prompts to a local Ollama model (qwen3.5:4b by default) that must answer with either a tool call or a final answer; tools cover repo-context gathering, file operations, and shell commands, each validated and gated by an approval mode (ask, auto, never) so risky actions require consent. The implementation demonstrates the standard efficiency patterns directly: a stable prompt prefix for cache reuse, clipped outputs and deduplicated reads for context reduction, durable transcripts with distilled working memory, and subagents scoped to bounded subtasks. Sessions persist under .mini-coding-agent/sessions and resume by ID. Readers use it alongside the essay to understand agent internals rather than to ship code with it — fifteen commits and a default six-step cap signal its educational scope.
