---
name: "CodeGenHelpers"
slug: "codegenhelpers"
layout: "agent.njk"
category: "other"
maker: "dansiegel"
license: "MIT"
url: "https://github.com/dansiegel/CodeGenHelpers"
source_code_url: "https://github.com/dansiegel/CodeGenHelpers"
source_available: "True"
platforms: []
first_released: "2020-10-31"
current_release: "2024-12-15"
stars: "107"
language: "C#"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: null
subagents: "False"
hooks: "False"
plan_mode: null
model_providers: null
pricing: "Free/open-source"
install_method: "NuGet package AvantiPoint.CodeGenHelpers"
docs_url: "https://github.com/dansiegel/CodeGenHelpers"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.nuget.org/packages/AvantiPoint.CodeGenHelpers/"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Fluent builder library for writing C# Source Generators (Roslyn) instead of raw IndentedStringBuilder string concatenation; typed builders work with native Roslyn types (e.g., ITypeSymbol); automatically handles namespace imports, class/enum/record construction, and source file naming (.g.cs); version 2.0 ships as pre-compiled library by default (with opt-in source-link mode). Not an AI agent harness."
---

CodeGenHelpers is a developer library for people writing C# Roslyn source generators, included in this census only because its name matches code-generation tooling. Writing source generators typically means concatenating output text through IndentedStringBuilder, which produces brittle, hard-to-maintain generator code; CodeGenHelpers replaces that with a fluent builder API that works directly with Roslyn symbols such as ITypeSymbol and handles namespace imports, class/enum/record construction, and .g.cs source-file naming automatically. Version 2.0 ships as a compiled NuGet library (AvantiPoint.CodeGenHelpers) by default, with an opt-in mode that injects the builder source directly into the generator project for scenarios that require source-only distribution. It is a Dan Siegel (AvantiPoint) project with no AI component.
