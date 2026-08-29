---
name: "video-use"
slug: "video-use"
layout: "agent.njk"
category: "other"
maker: "browser-use"
license: "MIT"
url: "https://github.com/browser-use/video-use"
source_code_url: "https://github.com/browser-use/video-use"
source_available: "Yes"
platforms:
  - "IDE"
first_released: "2026-04-12"
current_release: "2026-07-01"
stars: "21136"
language: "Python"
homepage: "https://github.com/browser-use/video-use"
mcp_support: "no"
plugin_support: "yes (skills-based; symlinks into agent skill directories)"
claude_code_plugin: "yes (via ~/.claude/skills/video-use)"
subagents: "yes (spawns parallel sub-agents for animations)"
hooks: "no"
plan_mode: "yes (asks for strategy approval before executing)"
model_providers: "Claude Code, Codex, Hermes, Openclaw, any shell-access agent"
pricing: "open-source (MIT); requires ElevenLabs API key (BYOK)"
install_method: "pip"
docs_url: "https://github.com/browser-use/video-use/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/browser-use/video-use"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Enables coding agents to edit raw video footage by reading word-level audio transcripts and on-demand visual composites instead of processing every frame, achieving precise word-boundary cuts with minimal token usage and a self-evaluation loop at every cut boundary."
---

Raw video has been beyond coding agents: minutes of footage mean tens of thousands of frames, orders of magnitude beyond any context window, so automated editing stayed outside the agent ecosystem. video-use, from the browser-use team ('browser-use, but for video'), makes footage legible by substituting representation for pixels: an ElevenLabs Scribe transcript with word-level timestamps and speaker diarization is packed into a small markdown file, and a timeline_view tool renders filmstrip and waveform composites only when the agent needs to inspect a moment. The agent plans an edit decision list over that text — filler-word removal, dead-space cuts, per-segment color grading, burned-in subtitles — and a rendering pipeline executes it with ffmpeg, self-evaluating output at every cut boundary and retrying up to three times; animation overlays run as parallel sub-agents. Creators and developers already working in Claude Code or Codex use it to batch-edit talking-head video from the terminal; it requires an ElevenLabs key and ffmpeg.
