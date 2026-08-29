---
name: "CodeContests"
slug: "codecontests"
layout: "agent.njk"
category: "other"
maker: "google-deepmind"
license: "Apache-2.0"
url: "https://github.com/google-deepmind/code_contests"
source_code_url: "https://github.com/google-deepmind/code_contests"
source_available: "Yes"
platforms: []
first_released: "2022-01-31"
current_release: "2023-10-03"
stars: "2201"
language: "C++"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "binary"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "gs://dm-code_contests"
maintained: "dead"
sources:
  - "brandonhimpfen"
what_makes_it_special: "A competitive programming dataset used to train DeepMind's AlphaCode, containing programming problems from multiple contest sites (Aizu, AtCoder, CodeChef, Codeforces, HackerEarth) with paired test cases and both correct/incorrect human solutions in multiple languages."
---

CodeContests is the dataset DeepMind built to train and evaluate AlphaCode, the competitive-programming system published in Science in 2022. It aggregates problems from five contest platforms — Aizu, AtCoder, CodeChef, Codeforces, and HackerEarth — pairing each problem with test cases and both correct and incorrect human solutions in multiple languages, the negative examples being deliberate: models learn from failed submissions as well as correct ones. The roughly 3 GiB dataset lives on Google Cloud Storage as ContestProblem protocol buffers in Riegeli format with train/validation/test splits, and the repository provides C++ and Python utilities built with Bazel for loading, executing, and evaluating candidate solutions. The repository was archived on December 6, 2024 and is read-only.
