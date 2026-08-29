---
name: "Monk"
slug: "monk"
layout: "agent.njk"
category: "agent"
maker: "monk"
license: "Provided license"
url: "https://open-vsx.org/extension/monk/vscode-monk"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-07-13"
current_release: null
stars: null
language: null
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "Install from Open VSX"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://open-vsx.org/extension/monk/vscode-monk"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Autonomous DevOps agent working inside the IDE"
---

Monk places DevOps automation inside the editor where the infrastructure code already lives, rather than in a separate console or CLI. The agent reads the workspace — manifests, configuration files, deployment scripts — plans the required operations, and executes them, covering cloud resources and pipeline definitions alongside the application code that depends on them. Distribution runs through Open VSX, which makes it available to VS Code, VSCodium, Cursor, and other VS Code-compatible editors rather than Microsoft's marketplace alone. Its dependency on the Red Hat YAML extension reflects the manifest-heavy workloads it targets, and its 31,000 downloads since July 2026 indicate an installed base despite no public source repository. Developers and platform teams use it to provision and modify infrastructure from the same editor where they write application code.
