---
name: "secure-ai-agent-boundary"
slug: "secure-ai-agent-boundary"
layout: "agent.njk"
category: "other"
maker: "Atrayee-dev"
license: "MIT"
url: "https://github.com/Atrayee-dev/secure-ai-agent-boundary"
source_code_url: "https://github.com/Atrayee-dev/secure-ai-agent-boundary"
source_available: "True"
platforms: []
first_released: "2026-06-28"
current_release: "2026-08-20"
stars: "115"
language: "HTML"
homepage: "https://atrayee-dev.github.io/secure-ai-agent-boundary/"
mcp_support: null
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: "True"
plan_mode: null
model_providers: "claude-opus,gpt-5-5,local-llm"
pricing: "Free/open-source (MIT)"
install_method: "Create .codeboundary.yml at repository root (decoupled configuration layer overlaying Git workflows; no daemon or kernel patching required)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://atrayee-dev.github.io/secure-ai-agent-boundary/"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "CodeBoundary: zero-trust AI co-development sandbox enforcing a compartment model where AI models operate in isolated ephemeral containers with strictly bounded data exposure via YAML/JSON 'data-boundary contracts'; 'diplomat's pouch' philosophy treats every AI interaction as a negotiated, auditable, ephemeral transaction; syntax-aware boundary checks (ASTs for 12+ languages), real-time secret redaction, hybrid routing (local models never see full context, frontier models never see credentials), immutable audit trail."
---

The project proposes a zero-trust compartment model for AI-assisted development: models run in isolated ephemeral containers, their file and symbol access bounded by data-boundary contracts, with regex and ML redaction stripping secrets before prompts leave, and every exchange written to an immutable audit trail. The README describes syntax-aware boundary enforcement across a dozen languages, hybrid local/frontier-model routing by sensitivity, and staged outputs requiring explicit approval. What the repository does not contain is any implementation — no source, package, CLI, or license file accompanies the 798-commit README and GitHub Pages landing site, and claims of "Level IV Verified" status are unverifiable. Community engagement is limited to a single author with no forks or issues. It should be treated as a concept document for AI co-development governance, not working software.
