---
name: "Youtrack-Workflows"
slug: "youtrack-workflows"
layout: "agent.njk"
category: "other"
maker: "JetBrains"
license: "Apache-2.0"
url: "https://github.com/JetBrains/youtrack-workflows"
source_code_url: "https://github.com/JetBrains/youtrack-workflows"
source_available: "True"
platforms:
  - "IDE"
first_released: "2012-08-09"
current_release: "2026-03-02"
stars: "229"
language: "JavaScript"
homepage: "http://www.jetbrains.com/youtrack/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "None — workflow scripts, no AI models"
pricing: null
install_method: "Clone repository and register workflows in YouTrack; scripts live in the js/ directory"
docs_url: "https://www.jetbrains.com/help/youtrack/incloud/?topic=Workflow-Guide"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Repository of custom workflows for YouTrack (JetBrains issue tracker) written using the JavaScript-based API. Official JetBrains project."
---

youtrack-workflows is JetBrains' official repository of sample custom workflow scripts for YouTrack, its issue tracker, written against YouTrack's JavaScript workflow API. The samples demonstrate workflow automation patterns — state changes, scheduled actions, notifications, and custom fields — and can be installed directly into a YouTrack instance. It is Apache-2.0 licensed and officially maintained by JetBrains, though activity is modest: 128 commits, no releases, and modest community traction. YouTrack administrators use it as a reference for writing custom workflow automation in JavaScript.
