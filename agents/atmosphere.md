---
name: "atmosphere"
slug: "atmosphere"
layout: "agent.njk"
category: "agent-sdk"
maker: "Atmosphere"
license: "Apache-2.0"
url: "https://github.com/Atmosphere/atmosphere"
source_code_url: "https://github.com/Atmosphere/atmosphere"
source_available: "Yes"
platforms:
  - "Web"
first_released: "2010-06-30"
current_release: "2026-08-17"
stars: "3794"
language: "Java"
homepage: "https://async-io.live"
mcp_support: "yes (atmosphere-mcp module; MCP 2026-07-28 spec with Tasks, MCP Apps, OAuth resource server; transports over WebSocket/SSE/gRPC)"
plugin_support: "yes"
claude_code_plugin: "n/a"
subagents: "yes"
hooks: "yes"
plan_mode: "yes"
model_providers: "OpenAI, Google, Anthropic, Cohere, Ollama, DashScope, local, BYOK"
pricing: "open-source"
install_method: "brew"
docs_url: "https://atmosphere.github.io/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Atmosphere/atmosphere/releases"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Real-time engine for AI agents on the JVM with deep-agent defaults (memory, plan, virtual filesystem, sub-agent delegation) and governance/compliance (OWASP Agentic Top 10, EU AI Act, HIPAA) built in."
---

Atmosphere is a real-time event-driven framework for running AI agents on the JVM, rebuilt on the long-standing Atmosphere real-time project. An @Agent annotation with @Prompt, @Command, and @AiTool annotations defines agent behavior, while an AgentRuntime SPI supports 12 runtime adapters (Spring AI, LangChain4j, Google ADK, Koog, Semantic Kernel, AgentScope, Embabel, Anthropic, Cohere, CrewAI, and others) that can be swapped without rewriting agent code. Token streaming flows from providers like OpenAI, Anthropic, Cohere, and Ollama to clients over WebSocket, SSE, gRPC, and WebTransport, with modules auto-registering browser, MCP, A2A, and AG-UI endpoints. Governance sits on the critical path: policy admission, human-in-the-loop approvals, PII redaction, cost ceilings, and compliance mappings for OWASP Agentic Top 10, EU AI Act, and HIPAA. Java teams building governed, production-grade agent services use it via Maven Central or Spring Boot starter.
