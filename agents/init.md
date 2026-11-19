---
name: "INIT"
slug: "init"
layout: "agent.njk"
category: "agent"
maker: "nagisanzenin"
license: "Apache-2.0"
url: "https://github.com/nagisanzenin/INIT-Agent"
source_code_url: "https://github.com/nagisanzenin/INIT-Agent"
source_available: "True"
homepage: "https://initlabs.si"
docs_url: "https://github.com/nagisanzenin/INIT-Agent/blob/main/docs/guide.md"
download_url: "https://github.com/nagisanzenin/INIT-Agent/releases"
install_method: "curl -fsSL https://github.com/nagisanzenin/INIT-Agent/releases/latest/download/get.sh | sh, then run init-agent (macOS 14+ Apple silicon; Linux x86_64 experimental, needs bubblewrap; the installer includes a Rust toolchain so INIT can rebuild itself)"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
specialization: "general"
language: "Rust"
first_released: "2026-10-23"
current_release: "2026-11-11"
maintained: "active"
mcp_support: null
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: "https://github.com/nagisanzenin/INIT-Agent/blob/main/docs/provider-configuration.md"
model_providers: "DeepSeek (live-tested on the release bundle) and OpenAI (qualified live on v0.5.4); experimental: OpenAI-compatible gateways, Anthropic Messages, local model servers, Sign in with ChatGPT (preview); native Gemini/Ollama/Bedrock/Azure/Vertex auth not built"
pricing: "BYOK"
stars: "25"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A coding agent that can rewrite its own harness while it works — prompts, skills, Wasm tools, and the compiled Rust core itself — gated by build/test/self-map/boot/self-edit checks and hot-swapped into the same conversation, while a separate model-inaccessible Root process holds the keys, signs every change, and can roll the system back."
---

INIT starts from the bitter lesson: hand-built harness structure becomes a ceiling once a model outgrows its designers, so INIT makes its own harness editable by the agent that runs in it. The harness is layered — T0 prompts and skills edit now, T1 tools are Wasm components, and T2 is the compiled Rust core and its loop — and a change to the compiled core goes through four gates: build/tests/clippy, a byte-for-byte self-map regeneration, booting the new binary beside the live one, and proving the new version can still complete a self-edit. Pass them and the new core hot-swaps in at a turn boundary, keeping the same conversation log and most of the prompt cache (87.9% on a measured swap); fail anything and the live body never stopped. The fixed part is the Root, a separate process the agent cannot write: it holds the API keys and adds them to each model call, composes the sandbox the agent runs in (Seatbelt on macOS, bubblewrap on Linux), snapshots the start folder for /undo, watches twelve harm signals, and can roll the whole system back to a known-good version with a signed record. INIT 0.6 is a research preview and says so plainly: it publishes what it has done (wrote itself a delegate tool, swapped its core mid-conversation, refused and rolled back its own change) and what it has not shown (that self-changes make a model better), with every measurement receipted in the repo. The intended users are researchers and frontier-model operators who want an agent whose scaffolding can grow with the model instead of capping it, on macOS Apple silicon or experimental Linux.
