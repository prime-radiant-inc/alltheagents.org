---
name: "Needle2"
slug: "needle2"
layout: "agent.njk"
category: "other"
maker: "cactus-compute"
license: "Apache-2.0"
url: "https://cactuscompute.com/needle"
source_code_url: "https://github.com/cactus-compute/needle"
source_available: "True"
platforms: []
first_released: "2026-02-24"
current_release: null
stars: 9588
language: "Python"
homepage: "https://cactuscompute.com/needle"
mcp_support: null
plugin_support: null
claude_code_plugin: "no"
subagents: null
hooks: null
plan_mode: "no"
model_providers: "locked"
pricing: "free"
install_method: "Python package or single dependency-free C++ binary from the repo"
docs_url: "https://cactuscompute.com/needle"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/cactus-compute/needle"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A 45M-parameter open-weights model shipped as a single 14MB dependency-free C++ binary purpose-built for tool calling, device use, and structured extraction on tiny hardware — trained natively at CQ2-bit quantization with a hashed n-gram engram memory and grammar-constrained decoding, running from Raspberry Pi 5 and Quest 3S down to ESP32-S3 microcontrollers and WebAssembly."
---

Needle2 is Cactus Compute's foundation model for tiny devices — phones, wearables, smart home, and robots — not a coding agent or framework. It is a 45M-parameter model specialized for agentic tool calling, device use, and schema-driven structured extraction, distributed as a single dependency-free C++ binary (~28MB session RAM) that auto-selects CPU kernels for NEON, SDOT, AVX2, RISC-V, and WASM SIMD, and it runs everywhere from a Raspberry Pi 5 at roughly 500 tokens per second to Meta Quest headsets, sub-$200 phones, STM32 microcontrollers, and the browser via WebAssembly. It is trained natively at CQ2-bit quantization rather than post-hoc, returns an empty call plus a learned confidence score for off-topic requests so apps can escalate to the cloud, and is designed for local fine-tuning via the needle finetune command. It belongs in the census as a model an agent harness could call rather than a harness itself.
