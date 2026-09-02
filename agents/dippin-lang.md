---
name: "Dippin"
slug: "dippin-lang"
layout: "agent.njk"
category: "agent-sdk"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/dippin-lang"
source_code_url: "https://github.com/2389-research/dippin-lang"
source_available: "True"
platforms:
  - "CLI"
first_released: null
current_release: null
stars: "24"
language: "Go"
homepage: "https://dippin.org"
mcp_support: "no"
plugin_support: "yes (VS Code extension, LSP server)"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes (human gate node type)"
plan_mode: "yes (branching logic, manager_loop node type)"
model_providers: null
pricing: "free"
install_method: "go install"
docs_url: "https://dippin.org"
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "DSL and toolchain for authoring AI pipeline workflows with first-class syntax for prompts, shell scripts, model config, branching logic, and node types (agent, tool, human, parallel, subgraph, manager_loop). Ships a full toolchain: parser, validator/linter, formatter, DOT exporter, simulator, cost/coverage analyzers, LSP server, VS Code extension, .dipx packaging, and WASM playground."
---

Dippin is a DSL and toolchain for authoring AI pipeline workflows, intended to replace hand-edited Graphviz DOT as the format people actually write and review. Its first-class syntax covers prompts, shell scripts, model config, and branching logic, and its node types — agent, tool, human, parallel, subgraph, and manager_loop — map directly onto the constructs a multi-agent pipeline needs, including human gates and manager loops. A full toolchain ships around the language: parser, validator and linter, formatter, DOT exporter, simulator, cost and coverage analyzers, an LSP server, a VS Code extension, .dipx packaging, and a WASM playground. Dippin describes pipelines; a separate runtime, such as Tracker, executes them. The audience is anyone designing reviewable, version-controlled AI workflows who wants a real language for the job instead of YAML or DOT.
