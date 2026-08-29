---
name: "HttpClientCodeGenerator"
slug: "httpclientcodegenerator"
layout: "agent.njk"
category: "other"
maker: "Jalalx"
license: "MIT"
url: "https://github.com/Jalalx/HttpClientCodeGenerator"
source_code_url: "https://github.com/Jalalx/HttpClientCodeGenerator"
source_available: "True"
platforms:
  - "CLI"
first_released: "2021-07-25"
current_release: "2024-11-16"
stars: "47"
language: "C# / .NET"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "none"
pricing: "Free / open-source"
install_method: "dotnet add package HttpClientGenerator (NuGet)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.nuget.org/packages/HttpClientGenerator"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Uses Roslyn source generators to produce HttpClient code on the fly at compile time without writing files to disk. No runtime dependency on third-party libraries. Supports flexible HttpClient injection via fields, properties, or resolver methods. NOTE: This is a .NET code generator, NOT an AI coding agent harness."
---

HttpClientCodeGenerator is a C# Roslyn source generator that removes hand-written HttpClient plumbing from service clients. Developers declare partial classes with attributed methods such as [HttpGet("todos/{id}")], and the generator emits the full implementation — URL construction, query strings, headers, serialization — at compile time in memory, leaving no generated files in the repository or any runtime dependency on external libraries. Generated code composes with IHttpClientFactory for the usual injection patterns, and the approach keeps repositories free of checked-in generated code. The project dates from the early Roslyn source-generator era, with known IDE tooling friction, and has seen no commits since late 2024.
