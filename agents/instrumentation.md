---
name: "instrumentation"
slug: "instrumentation"
layout: "agent.njk"
category: "other"
maker: "brutusin"
license: "Apache-2.0"
url: "https://github.com/brutusin/instrumentation"
source_code_url: "https://github.com/brutusin/instrumentation"
source_available: "True"
platforms: []
first_released: "2015-01-22"
current_release: "2020-03-12"
stars: "48"
language: "Java"
homepage: "http://brutusin.org/instrumentation"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "Free / open source"
install_method: "Maven dependency (org.brutusin:instrumentation) from Maven Central, or build fat-jar with Premain-Class and launch via -javaagent JVM flag"
docs_url: "http://brutusin.org/instrumentation"
plugin_docs_url: null
config_docs_url: null
download_url: "Maven Central Repository"
maintained: "dormant"
sources:
  - "github_topic4"
what_makes_it_special: "An extensible Java agent framework that instruments JVM bytecode at class-loading time, injecting code into methods to notify custom listeners about method start, finish, and error events. README explicitly states it is superseded by https://github.com/ShiftLeftSecurity/bctrace. NOTE: This is a JVM bytecode instrumentation framework, NOT an AI coding agent harness."
---

brutusin/instrumentation is a Java agent in the JVM sense: loaded via -javaagent with a Premain-Class, it rewrites bytecode at class-loading time using ASM so that registered Interceptors hear about method entry, exit, and thrown errors. The design is deliberately minimal — a JRE 1.5+ dependency and one Maven artifact, org.brutusin:instrumentation, with logging-instrumentation as the worked example. Its README now redirects users to ShiftLeftSecurity/bctrace, a more mature continuation by the same lineage, and the project has been inactive since 2020. It contains no AI, no LLM calls, and no coding-agent features.
