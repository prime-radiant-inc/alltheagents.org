---
name: "Binary RE"
slug: "binary-re"
layout: "agent.njk"
category: "other"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/binary-re"
source_code_url: "https://github.com/2389-research/binary-re"
source_available: "True"
platforms:
  - "IDE"
first_released: null
current_release: null
stars: "15"
language: null
homepage: null
mcp_support: "no"
plugin_support: "yes (Claude Code skill/plugin)"
claude_code_plugin: "yes"
subagents: "no"
hooks: "yes (human-in-the-loop gates for risky operations)"
plan_mode: "yes (hypothesis-driven analysis workflow)"
model_providers: "Claude (via Claude Code)"
pricing: "free"
install_method: "/plugin marketplace add 2389-research/claude-plugins, then /plugin install binary-re@2389-research"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Agentic binary reverse engineering Claude Code plugin for ELF binaries (ARM64, ARMv7, x86_64, MIPS) using radare2, Ghidra, GDB, and QEMU. Hypothesis-driven analysis where the LLM forms hypotheses from evidence, designs experiments, and a human approves risky operations via human-in-the-loop gates. Targets firmware/IoT binary analysis when source code is unavailable."
---

Binary RE is a Claude Code skill that turns the agent into an agentic binary reverse engineer for ELF binaries across ARM64, ARMv7, x86_64, and MIPS. The loop belongs to Claude Code; this plugin supplies the domain method. Analysis is hypothesis-driven: the LLM forms a hypothesis from the evidence it has, designs an experiment to test it, and a human-in-the-loop gate approves any risky operation before it runs. External tools — radare2, Ghidra, GDB, and QEMU — are the instruments the agent drives, and the skill knows how to invoke them and read their output. The target is firmware and IoT binary analysis when source code is unavailable, the kind of work that is otherwise slow and manual. The audience is security researchers and reverse engineers who want Claude Code to carry the tedious parts of a structured RE workflow.
