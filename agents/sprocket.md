---
name: "Sprocket"
slug: "sprocket"
layout: "agent.njk"
category: "agent"
maker: "spikonado"
license: "FSL-1.1-ALv2 (Functional Source License, converts to Apache-2.0)"
url: "https://github.com/spikonado/sprocket"
source_code_url: "https://github.com/spikonado/sprocket"
source_available: "True"
platforms:
  - "Web"
  - "Desktop"
  - "CLI"
first_released: "2026-04-13"
current_release: "2026-08-28"
stars: 19
language: "TypeScript"
homepage: "https://spikonado.com"
mcp_support: null
plugin_support: null
claude_code_plugin: "no"
subagents: null
hooks: null
plan_mode: "no"
model_providers: "BYOK (self-hosted setup requires model-provider API keys)"
pricing: "free"
install_method: "npx @spikonado/sprocket (also Electron desktop installers for Linux, macOS, Windows; state in $HOME/.sprocket)"
docs_url: "https://github.com/spikonado/sprocket/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/spikonado/sprocket/releases"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "Markets itself as the only AI agent for developing both hardware and software: it retrieves best-in-class context from the web, buys parts and subscriptions from any site on request, creates detailed schematics, generates a BOM, and writes assembly instructions."
---

Sprocket is Spikonado's agent for building complete technology systems — apps, robots, devices, and the glue between them — rather than just code. It retrieves web context for everything it does and can purchase hardware parts or SaaS subscriptions from any website when asked, then produce the concrete artifacts of hardware development: detailed schematics, a bill of materials, and assembly instructions. It runs as a browser-based UI by default (the local app launches a Rust-based server on port 17731), as Electron desktop installers for Linux, macOS, and Windows, or via npx, with state stored locally in $HOME/.sprocket. The repo is public under the Functional Source License, and self-hosted development needs a Convex deployment plus model-provider API keys, so users bear their own model costs.
