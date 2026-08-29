---
name: "agentcookie"
slug: "agentcookie"
layout: "agent.njk"
category: "other"
maker: "mvanhorn"
license: "MIT"
url: "https://github.com/mvanhorn/agentcookie"
source_code_url: "https://github.com/mvanhorn/agentcookie"
source_available: "True"
platforms:
  - "Web"
  - "Desktop"
first_released: "2026-05-16"
current_release: "2026-08-14"
stars: "769"
language: "Go"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "none (cookie/session sync utility; no LLM integration)"
pricing: "open-source"
install_method: "binary, go install"
docs_url: "https://github.com/mvanhorn/agentcookie/blob/main/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/mvanhorn/agentcookie/releases"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Cookie session sync tool for AI agents — continuously syncs Mac's Chrome cookie sessions to a Linux box (or second Mac) where agents run, over Tailscale, so agents wake up already authenticated. Handles the hard parts: macOS Keychain decryption, Chrome App-Bound Encryption on source, live CDP injection into Chrome's in-memory store on Linux sink. Pairing-derived per-peer keys, AES-256-GCM, per-CLI secrets bus for bearer tokens/API keys."
---

Coding agents that drive a browser hit a login wall the moment they run on a machine where the human never signed in, and headless re-authentication defeats bot defenses. agentcookie keeps a Linux box's Chrome cookie store in sync with a Mac's continuously over Tailscale, decrypting the macOS Keychain on the source and injecting cookies live over the Chrome DevTools Protocol into the sink's in-memory session, so Puppeteer, Playwright, or browserUse automations wake up already authenticated. Transport is end-to-end encrypted (AES-256-GCM with pairing-derived per-peer keys), and a secrets bus carries bearer tokens and API keys to CLIs separately. Developers running browser-driving agents on remote machines are the users; DBSC-bound sessions like Google deliberately do not sync.
