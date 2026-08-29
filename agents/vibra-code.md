---
name: "vibra-code"
slug: "vibra-code"
layout: "agent.njk"
category: "agent"
maker: "sa4hnd"
license: "AGPL-3.0"
url: "https://github.com/sa4hnd/vibra-code"
source_code_url: "https://github.com/sa4hnd/vibra-code"
source_available: "True"
platforms: []
first_released: "2026-03-06"
current_release: "2026-03-06"
stars: "120"
language: "TypeScript"
homepage: "https://mintlify.wiki/sa4hnd/vibra-code"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude,Cursor,Gemini"
pricing: "Free/open-source (self-hostable)"
install_method: "git clone --recurse-submodules, npm install (backend); macOS/Xcode/CocoaPods for mobile app"
docs_url: "https://mintlify.wiki/sa4hnd/vibra-code"
plugin_docs_url: null
config_docs_url: null
download_url: "https://apps.apple.com/us/app/vibra-code-ai-app-builder/id6752743077"
maintained: "active"
sources:
  - "github_final"
what_makes_it_special: "First open-source AI mobile app builder (open-source alternative to Lovable/Bolt.new/Rork); describes app in plain English and generates code in E2B cloud sandbox with real-time native preview on phone; customizable AI prompts and provider swapping; entire project (backend + 60fps native iOS chat UI via Texture/IGListKit) built by a single 19-year-old using Claude Code."
---

Vibra Code exists to open mobile app creation to people who describe rather than program, as an open-source counterpart to closed builders like Lovable, Bolt.new, and Rork that anyone can self-host and modify. A user describes an app in plain English (or voice/image input) on their phone; a Next.js/Convex backend spawns an E2B cloud sandbox where a coding agent — Claude Code by default, Cursor or Gemini selectable via environment variable — writes the application, Inngest orchestrates the work, and Convex streams every change back to a native 60fps iOS chat interface built on Texture and IGListKit, with live preview through a tunnel URL and optional GitHub push of the finished project. Indie developers and hobbyists who want an open, self-hostable mobile app builder use it; it is AGPL-3.0 licensed, early-stage (7 commits), and was built end-to-end by a single developer working with Claude Code.
