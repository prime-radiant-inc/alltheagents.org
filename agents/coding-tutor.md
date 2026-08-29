---
name: "Coding-Tutor"
slug: "coding-tutor"
layout: "agent.njk"
category: "other"
maker: "iwangjian"
license: "Apache-2.0"
url: "https://github.com/iwangjian/Coding-Tutor"
source_code_url: "https://github.com/iwangjian/Coding-Tutor"
source_available: "True"
platforms: []
first_released: "2025-01-23"
current_release: "2025-06-02"
stars: "91"
language: "Python"
homepage: "https://arxiv.org/abs/2502.13311"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Azure, open-weight backbone models"
pricing: null
install_method: "conda create -n coding-tutor python=3.10, pip install -r requirements.txt"
docs_url: "https://arxiv.org/abs/2502.13311"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/iwangjian/Coding-Tutor"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Research project (ACL 2025 Findings paper) proposing Trace-and-Verify (Traver), an agent workflow combining knowledge tracing and turn-by-turn verification for LLM task-tutoring agents using coding tutoring as a scenario; introduces DICT (Dialogue for Coding Tutoring), a novel evaluation protocol combining student simulation and coding tests. Not a production coding agent harness."
---

LLM tutors that teach programming lack a way to measure whether their teaching actually works, and dialogue quality metrics do not capture learning. This project, the research code for an ACL 2025 Findings paper, proposes Traver (Trace-and-Verify): a tutoring agent workflow that traces what the student knows and verifies turn by turn whether the dialogue is helping, using a trained verifier model released as a 7B checkpoint on Hugging Face. The accompanying DICT protocol evaluates tutoring agents by simulating students, running the tutoring dialogue, and scoring pre/post coding tests against the EvoCodeBench benchmark. The repository includes dialogue simulation, verifier training scripts, and evaluation pipelines. Researchers studying LLM-based tutoring and education use it; it is not a tool for developers writing production software.
