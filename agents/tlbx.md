---
name: "tlbx"
slug: "tlbx"
layout: "agent.njk"
category: "multiplexer"
maker: "tlbx-ai"
license: "AGPL-3.0"
url: "https://github.com/tlbx-ai/tlbx"
source_code_url: "https://github.com/tlbx-ai/tlbx"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
  - "Desktop"
first_released: "2025-12-29"
current_release: "2026-08-18"
stars: "102"
language: ".NET 10 Native AOT, TypeScript, xterm.js"
homepage: "https://tlbx.ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Agent CLIs (Codex, Claude Code, Gemini CLI, Grok Build, OpenCode, Copilot CLI, Antigravity CLI)"
pricing: "Self-hosted, open source (commercial licensing available)"
install_method: "curl -fsSL https://get.tlbx.ai/install.sh | bash (macOS/Linux); irm https://get.tlbx.ai/install.ps1 | iex (Windows); npx @tlbx-ai/midterm for ephemeral trial"
docs_url: "https://tlbx.ai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/tlbx-ai/tlbx/releases/latest"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Browser is the control surface, not the runtime-agents, PTYs, tests, and servers persist across browser disconnects/device changes; one independent instance per host; works with any terminal app not just agents; private remote access via Tailscale/WireGuard (no cloud relay); runs multiple agents simultaneously on same project"
---

tlbx (formerly MidTerm) is a self-hosted terminal multiplexer whose browser UI is only a control surface: close the tab, switch devices, or lose connectivity and the underlying PTYs, tests, servers, and agent sessions keep running on the host, ready to reattach from any device. Each host runs one independent instance, so there is no central cloud — remote access goes over the user's own network path, with Tailscale or WireGuard recommended and Cloudflare Tunnel or plain LAN also supported, keeping repositories and credentials on the host. Two session types coexist in a workspace: real persistent PTYs running any shell or terminal program, and Agent Controller sessions that give structured UI (turns, tool calls, diffs, approvals) to ACP-speaking coding agents such as Codex, Grok Build, OpenCode, Gemini CLI, and Copilot CLI, while multiple agents can work the same project concurrently. The implementation is .NET 10 Native AOT with an xterm.js frontend, AGPL-3.0 licensed with commercial licensing available, and installers cover macOS, Linux, and Windows. Developers who run long-lived agent sessions across several machines and refuse to route them through a vendor cloud are the audience.
