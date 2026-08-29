---
name: "Locus"
slug: "locus"
layout: "agent.njk"
category: "agent"
maker: "r1n7aro"
license: "GPL-3.0-or-later"
url: "https://github.com/r1n7aro/Locus"
source_code_url: "https://github.com/r1n7aro/Locus"
source_available: "yes"
platforms: []
first_released: "2026-04-22"
current_release: "2026-08-18"
stars: "710"
language: "Rust, TypeScript, C#"
homepage: null
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "binary"
docs_url: "https://unity.farlocus.com/en"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/r1n7aro/Locus/releases"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Open-source AI agent for Unity projects — writes C# code, reads/modifies Unity objects & assets. Runs as a standalone Rust/Tauri/Vue.js process (not inside Unity Editor, not an MCP server) enabling capabilities that would be nearly impossible otherwise. Built-in C# hot reload (no domain reload, preserves Play Mode). Rider-grade Roslyn analysis. Proprietary intermediate representation for progressive scene/asset reading. Rust-powered parallel asset scans. Automated knowledge system with L0/L1/L2 context injection. Vue.js editor UI via /view command."
---

Unity's editor APIs cap what in-editor or MCP-based automation can do, so Locus takes the unusual step of running as an independent desktop process that drives Unity from outside. The agent writes and edits C# with Rider-grade Roslyn analysis running in its own process, sees live compiler errors, and verifies changes through hot reload that never forces a domain reload, so Play Mode state survives edits. A proprietary intermediate representation lets it progressively read large scenes and assets rather than loading them whole, Rust-based parallel scans keep asset-database queries fast, and semantic diffs handle Unity's YAML assets. An L0/L1/L2 knowledge system maintains project memory across sessions, and a /view command has the agent build Vue.js editor UIs. Game developers on Windows (Unity 2021+) are the audience, with GPL-3.0 source and installer releases.
