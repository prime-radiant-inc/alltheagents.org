---
name: "Java-Ai-Sbus-Test"
slug: "java-ai-sbus-test"
layout: "agent.njk"
category: "other"
maker: "abhikt48"
license: null
url: "https://github.com/abhikt48/java-ai-sbus-test"
source_code_url: "https://github.com/abhikt48/java-ai-sbus-test"
source_available: "Yes"
platforms: []
first_released: "2024-05-08"
current_release: "2024-05-08"
stars: null
language: "Java"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: "Download applicationinsights-agent-3.5.2.jar, run with -javaagent VM argument"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/abhikt48/java-ai-sbus-test"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "A minimal test case for integrating Azure Application Insights codeless agent with Azure ServiceBus dependency tracking, using the Java agent for telemetry."
---

The repository exists to confirm that the applicationinsights-agent-3.5.2.jar captures Azure Service Bus dependency telemetry correctly. The README walks through dropping the agent JAR into an agent/ folder, pointing applicationinsights.json at an App Insights connection string, and launching the sample with -javaagent to watch the dependency tree appear in the portal. There is no AI coding functionality, no LLM, and no tool loop; the name simply collides with agent-harness terminology. It is retained in the census as a categorization error rather than a harness.
