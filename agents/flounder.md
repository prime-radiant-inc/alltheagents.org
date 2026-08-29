---
name: "flounder"
slug: "flounder"
layout: "agent.njk"
category: "agent"
maker: "adshao"
license: "AGPL-3.0"
url: "https://github.com/adshao/flounder"
source_code_url: "https://github.com/adshao/flounder"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2026-06-05"
current_release: "2026-08-18"
stars: "329"
language: "TypeScript"
homepage: "https://flounders.xyz"
mcp_support: null
plugin_support: "True"
claude_code_plugin: "True"
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI (Codex), Anthropic (Claude Code)"
pricing: "Free/open-source (AGPL-3.0)"
install_method: "npx skills add adshao/flounder --skill flounder -g -a codex -a claude-code; or from source: nvm use, npm install, npm run build, npm run sandbox:build (requires Node 24 LTS)"
docs_url: "https://github.com/adshao/flounder/blob/main/docs/USAGE.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/adshao/flounder"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Autonomous white-hat security auditor that turns coding agents (Codex, Claude Code) into an end-to-end security audit pipeline (Prepare->Map->Dig->Synthesize->Verify->Confirm->Report). Audit strategy comes from the model, not hardcoded rules; findings require execution-grounded proof (must cite passing local commands). Sandboxed OCI execution with network-sealed discovery; strong fit for Solidity/EVM and ZK targets."
---

Flounder addresses the gap between chat-based vulnerability discussions and real audits: security work needs hours of sustained, skeptical investigation, containerized tooling, and evidence rather than plausible prose. It runs a seven-phase pipeline (prepare, map, dig, synthesize, verify, confirm, report) around the coding agent, supplying an OCI/Apple container sandbox with network sealing and read-only rootfs, a command policy, SQLite-backed durable state, and execution gates; the model chooses audit strategy while Flounder enforces the boundary. Findings require passing local proof tests with differential confirmation and refutation checks, so false positives get filtered before reporting. Security researchers use it for blind capability audits, incident investigation from transaction hashes, bug bounties, and disclosure preparation, with particular depth in Solidity/EVM, Cairo/Starknet, and TON.
