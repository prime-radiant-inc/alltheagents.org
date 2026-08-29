---
name: "Xcode Coding Intelligence"
slug: "xcode-coding-intelligence"
layout: "agent.njk"
category: "agent"
maker: "Apple"
license: null
url: "https://developer.apple.com/xcode/"
source_code_url: null
source_available: null
platforms:
  - "IDE"
  - "Desktop"
first_released: "2025"
current_release: "2026"
stars: null
language: "Swift"
homepage: "https://developer.apple.com/xcode/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Apple on-device completion model; Anthropic (Claude) and OpenAI (ChatGPT) cloud backends"
pricing: "free"
install_method: "Included with Xcode 26+ from the Mac App Store; third-party models configured in Xcode settings"
docs_url: "https://developer.apple.com/documentation/xcode/setting-up-coding-intelligence"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Xcode 26 built-in coding agent with ChatGPT/Claude backends and Swift Assist"
---

Xcode 26 introduced coding intelligence that pairs an on-device predictive completion model, trained specifically for Swift and Apple SDKs, with third-party cloud LLMs: developers can choose among Anthropic and OpenAI's coding models and agents directly in the IDE, alongside local on-device completion that needs no network. Coding Tools bring Writing-Tools-style rewriting, documentation, and error fixing into the source editor, and agentic coding arrived with Xcode 26.3 and expands in Xcode 27, where coding agents run powered by the model of the user's choice. All of this is built into Xcode rather than delivered through an extension, at no extra cost beyond the applicable model subscriptions. Its audience is Apple-platform developers already working in Xcode.
