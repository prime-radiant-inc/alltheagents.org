---
name: "Extension-Ci-Tools"
slug: "extension-ci-tools"
layout: "agent.njk"
category: "other"
maker: "duckdb"
license: null
url: "https://github.com/duckdb/extension-ci-tools"
source_code_url: "https://github.com/duckdb/extension-ci-tools"
source_available: "True"
platforms: []
first_released: "2024-02-26"
current_release: "2026-08-10"
stars: "52"
language: "YAML, Shell, Makefile"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: null
pricing: "Free / open-source"
install_method: "N/A - referenced by DuckDB extension repositories, not a standalone installable package"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Reusable CI/CD components (GitHub Actions workflows, Docker configs, makefiles, scripts, vcpkg ports) for building, testing, and deploying DuckDB extensions across multiple DuckDB versions and platforms."
---

Building a DuckDB extension means compiling against multiple DuckDB versions across Linux, macOS, and Windows with matching toolchains — a configuration burden that used to be duplicated in every extension repository and drifted out of sync with DuckDB's own build changes. extension-ci-tools centralizes that into reusable GitHub Actions workflows, Docker configurations, Makefiles, build scripts, and vcpkg ports that the DuckDB Extension Template and downstream extension repos consume by reference. Versioned branches (v1.4.x, v1.5.x) track DuckDB releases, with the latest two versions actively maintained and older branches retired on a schedule. Its users are DuckDB extension authors; the repository contains no AI or agent functionality whatsoever.
