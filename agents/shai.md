---
name: "shai"
slug: "shai"
layout: "agent.njk"
category: "agent"
maker: "ovh"
license: "Apache-2.0"
url: "https://github.com/ovh/shai"
source_code_url: "https://github.com/ovh/shai"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-07-16"
current_release: "2025-12-18"
stars: "615"
language: "Rust"
homepage: null
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "OVHCloud, OpenAI"
pricing: "open-source"
install_method: "binary"
docs_url: "https://github.com/ovh/shai/wiki"
plugin_docs_url: null
config_docs_url: null
download_url: "https://raw.githubusercontent.com/ovh/shai/main/install.sh"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Terminal-based pair programming agent with headless mode for scripting/automation, HTTP server mode with OpenAI-compatible API and SSE streaming, shell assistant that auto-suggests fixes for failed commands, project context via SHAI.md, and MCP-powered custom agents"
---

OVH built shai as an open-source terminal pair programmer, distinguished by treating the agent as a component: pipe a prompt in for automation with full conversation traces out, or run `shai serve` to expose the agent through OpenAI-compatible HTTP endpoints with SSE streaming and persistent sessions. The shell assistant mode hooks the user's shell so a failed command's context goes to the model and a fix comes back inline. Project context loads from a SHAI.md file at the repo root, custom agents are configurable with MCP servers and OAuth, and OVHcloud provides anonymous rate-limited access as the default provider. It is Apache-2.0, community-maintained under the OVH organization with active issues and CI, and installs via a curl script or cargo. The audience is terminal-first developers and teams wanting a self-hostable agent endpoint.
