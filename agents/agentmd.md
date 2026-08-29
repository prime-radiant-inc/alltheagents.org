---
name: "agent.md"
slug: "agentmd"
layout: "agent.njk"
category: "other"
maker: "agentmd"
license: "MIT"
url: "https://github.com/agentmd/agent.md"
source_code_url: "https://github.com/agentmd/agent.md"
source_available: "True"
platforms: []
first_released: "2025-07-09"
current_release: "2025-07-10"
stars: "89"
language: "Markdown"
homepage: "https://agent.md"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "Free / open spec (MIT)"
install_method: "Place an AGENT.md file at the repository root; optionally symlink existing CLAUDE.md/.cursorrules-style files to it for backward compatibility"
docs_url: "https://agent.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "A specification defining AGENT.md, a standardized vendor-neutral Markdown configuration file that lets codebases communicate project conventions to any agentic coding tool; replaces fragmented config files (.cursorrules, .windsurfrules, CLAUDE.md, etc.) with one universal file any AI coding agent can parse; supports hierarchical files and @-mentions for file references; backward-compatible migration via symlinks so existing tools keep working. Authored by Geoffrey Huntley at Sourcegraph, Inc. Not a software package."
---

Every agentic coding tool grew its own instruction-file convention, so a repository supporting several agents accumulates near-duplicate configuration. The AGENT.md specification proposes one vendor-neutral Markdown file with RFC 2119 semantics, hierarchical resolution (root, subdirectory, and user-global files), @-mentions for composing other files, and documented symlink migrations from .cursorrules, CLAUDE.md, .clinerules, and similar files. It was authored by Geoffrey Huntley of Sourcegraph and published as an informational proposal in July 2025 rather than through a formal standards body. Adoption has been modest, with the competing AGENTS.md convention seeing wider industry uptake, so the document mostly matters as one position in the instruction-file standardization contest.
