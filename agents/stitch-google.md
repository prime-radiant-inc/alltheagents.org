---
name: "Stitch (Google)"
slug: "stitch-google"
layout: "agent.njk"
category: "other"
maker: "Google"
license: "Proprietary"
url: "https://stitch.withgoogle.com"
source_code_url: null
source_available: "False"
platforms:
  - "Web"
first_released: "2025"
current_release: null
stars: null
language: null
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Google"
pricing: "Free (Google Labs experiment)"
install_method: "Web app (browser, no install)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "bing_ddg_chinese"
what_makes_it_special: "Google Labs experiment that generates UI designs from text prompts or images and can export them as frontend code. Not a coding agent harness."
---

Stitch, announced at Google I/O 2025, occupies the gap between wireframing tools and code generators: a natural-language prompt or a screenshot produces editable UI designs for web and mobile, refined through follow-up prompts and rendered with Gemini models in a faster Flash mode for iteration. Output can be exported as HTML/CSS for frontend work or pasted into Figma for design handoff, which makes it useful for teams that start in design rather than in an editor. It does not plan tasks, edit repositories, run tools, or iterate on code — implementation happens elsewhere, in an editor or an agent. Its role in this census is as a recurring miscategorized result: design-to-code is adjacent to, but distinct from, a coding agent harness.
