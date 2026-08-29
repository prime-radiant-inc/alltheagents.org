---
name: "Continue"
slug: "continue"
layout: "agent.njk"
category: "agent"
maker: "continuedev"
license: "Apache-2.0"
url: "https://github.com/continuedev/continue"
source_code_url: "https://github.com/continuedev/continue"
source_available: "True"
platforms:
  - "IDE"
  - "CLI"
first_released: "2023-05-24"
current_release: "2026-08-19"
stars: null
language: "TypeScript"
homepage: "https://continue.dev"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: "True"
model_providers: "Any (BYOK via configurable providers: Anthropic, OpenAI, Ollama, and others)"
pricing: "Free / open source"
install_method: "VS Code Marketplace, OpenVSX, npm (@continuedev/cli), GitHub Releases (JetBrains)"
docs_url: "https://docs.continue.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/continuedev/continue/releases"
maintained: "dormant"
sources:
  - "jqueryscript"
  - "brad"
  - "jim"
  - "brandonhimpfen"
  - "ishandutta"
  - "tiennm"
what_makes_it_special: "Pioneering open-source coding agent available as CLI, VS Code extension, and JetBrains plugin. The repository is no longer actively maintained and is read-only; a final 2.0.0 release was published as a foundation for others."
---

Continue spent 2023-2026 as the default open-source answer to commercial coding assistants, letting developers point one interface at any model provider across a CLI, a VS Code extension, and a JetBrains plugin. Its agent loop handled multi-file edits, plan mode structured larger changes, and MCP support connected external tools. In 2026 the maintainers ended development: the repository became read-only, and a final 2.0.0 release removed anonymous telemetry, stripped out mandatory authentication, and fixed lingering bugs specifically so the Apache-2.0 codebase would be clean to fork. The team recommended the CLI as the most durable component for anyone continuing with the code. Teams that need an in-house agent base still fork it, and its extension ecosystem influenced the generation of open-source agents that followed.
