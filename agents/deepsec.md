---
name: "deepsec"
slug: "deepsec"
layout: "agent.njk"
category: "other"
maker: "vercel-labs"
license: "Apache-2.0"
url: "https://github.com/vercel-labs/deepsec"
source_code_url: "https://github.com/vercel-labs/deepsec"
source_available: "True"
platforms: []
first_released: "2026-04-30"
current_release: "2026-08-18"
stars: "7757"
language: "TypeScript"
homepage: "https://deepsec.sh/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Vercel AI Gateway, OpenAI, Anthropic, custom HTTPS provider"
pricing: "BYOK"
install_method: "npm"
docs_url: "https://deepsec.sh"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/deepsec"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Agent-powered vulnerability scanner for on-demand review of large-scale repos. Resumable execution (skips already-analyzed files on re-run), fans out work across Vercel Sandbox microVM worker machines in parallel, tunable AI thinking levels, keeps API keys host-side (injected into sandboxes rather than baked in)."
---

deepsec is Vercel Labs' agent-powered vulnerability scanner for on-demand, whole-repository security review rather than continuous linting. A free regex pre-pass filters the codebase, then AI models at maximum reasoning effort review what remains, fanning out across worker machines — optionally Vercel Sandbox microVMs — so large codebases parallelize; runs are resumable, skipping files already analyzed when interrupted. Workflows run through npx commands (init, scan, process, revalidate, export), with findings exportable as markdown directories and a SKILL.md exposed so coding agents can operate the scanner. Billing goes through Vercel AI Gateway or the user's own OpenAI/Anthropic keys, and large scans can cost thousands of dollars, which suits security teams auditing big repositories on demand.
