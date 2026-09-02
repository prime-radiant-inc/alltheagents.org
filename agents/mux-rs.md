---
name: "Mux (Rust)"
slug: "mux-rs"
layout: "agent.njk"
category: "agent-sdk"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/mux-rs"
source_code_url: "https://github.com/2389-research/mux-rs"
source_available: "True"
platforms: []
first_released: null
current_release: null
stars: "0"
language: "Rust"
homepage: null
mcp_support: "yes (MCP client integration)"
plugin_support: "yes (extensible tool definitions)"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "cargo install"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Agent SDK / agentic infrastructure library for Rust providing tool execution with structured input/output, MCP client integration, permission-gated approval flows via a policy engine, and async-first architecture on tokio. Type-safe tool definitions using Rust's type system, with an FFI crate (mux-ffi) for cross-language use."
---

Mux is an agentic infrastructure library for Rust, not a coding agent. It provides the building blocks — tool execution with structured input and output, MCP client integration to pull in external tools, and a permission-gated approval flow run through a policy engine — so that an agent built on top of it can ask a human before risky actions and stay async-first on tokio. Tool definitions are type-safe, expressed in Rust's type system rather than loose JSON, and an FFI crate (mux-ffi) exposes the same primitives to other languages. Mux ships no coding agent of its own; developers compose it into their own agent or harness. The audience is Rust developers who want a foundation for agent tooling and approval flows without reinventing the glue.
