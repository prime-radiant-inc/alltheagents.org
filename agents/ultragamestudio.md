---
name: "UltraGameStudio"
slug: "ultragamestudio"
layout: "agent.njk"
category: "agent"
maker: "wellingfeng"
license: "MIT"
url: "https://github.com/wellingfeng/UltraGameStudio"
source_code_url: "https://github.com/wellingfeng/UltraGameStudio"
source_available: "True"
platforms: []
first_released: "2026-05-30"
current_release: "2026-08-17"
stars: "289"
language: "TypeScript, Rust"
homepage: "https://github.com/wellingfeng/UltraGameStudio"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "Claude Code, Codex, Gemini, NVIDIA NIM, OpenRouter, GitHub Models, Hugging Face, SambaNova, Together AI, DeepSeek, Mistral, Groq, Fireworks, Cerebras, Ollama, LM Studio, llama.cpp"
pricing: "free"
install_method: "cd app && npm install && npm run dev (web) or npm run desktop; or ./run.sh (macOS/Linux), run.bat (Windows)"
docs_url: "https://github.com/wellingfeng/UltraGameStudio#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/wellingfeng/UltraGameStudio/releases"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "AI coding agent built specifically for game development. Speaks game-engine language (materials, blueprints, terrain, UMG, skeletal animation, packaging), generates all game asset types (images, 3D models, 2D sprites, atlases, audio, rigging, video) from the same chat surface, ships 40+ game-dev expert roles across Unity/Unreal/Godot/Web, and routes routine work through 20+ free/low-cost channels to save premium quota."
---

UltraGameStudio exists because general-purpose coding agents do not speak game engines: they cannot reason about materials, blueprints, or skeletal animation, and they cannot produce the assets games require, forcing developers back to bespoke pipelines for every asset type. The app wraps the coding-agent pattern in a game-first surface: chat requests route to engine-specialist expert roles spanning Unity, Unreal, Godot, and web projects, while slash commands generate sprites, meshes, atlases, music, and video inline. A /studio command assembles a per-task execution harness with parallel subagents, adversarial verification, and acceptance gates, and a local Rust proxy translates between provider protocols so free channels — NVIDIA NIM, OpenRouter, keyless gateways, local runtimes — absorb routine work and fail over automatically. Game developers working in Unity, Unreal, Godot, or web engines use it; it is MIT-licensed, free, and stores sessions and keys locally.
