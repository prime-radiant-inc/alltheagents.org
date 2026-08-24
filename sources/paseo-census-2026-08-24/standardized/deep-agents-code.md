# Standardized differentiation extraction: Deep Agents Code (deep-agents-code)

Extracted 2026-08-24 from official LangChain materials only, per STANDARD_PROMPT v1.

1. **One-sentence self-description:** An open-source terminal coding agent (`dcode`) built on the Deep Agents SDK — LangChain's "batteries-included" agent harness — that works with any tool-calling LLM and lets you switch providers, with persistent memory, customizable skills, and approval controls gating code execution. (https://docs.langchain.com/oss/deepagents/code/overview, https://github.com/langchain-ai/deepagents)

2. **Claimed differentiators:**
   - "The coding agent you own": bring your own model, customize the harness, and control how execution is approved, traced, and run — vs a fixed coding assistant. (openness / trust-safety) — https://www.langchain.com/dcode
   - Model-agnostic: any tool-calling LLM — frontier (OpenAI, Anthropic, Google), open-weight, or local — with mid-session model switching that retains conversation state. (model) — https://www.langchain.com/dcode, https://docs.langchain.com/oss/deepagents/code/overview
   - Persistent memory across sessions and agents: AGENTS.md files plus auto-saved memories under a "memory-first protocol"; configurable and shareable. (capability) — https://www.langchain.com/blog/introducing-deepagents-cli, https://docs.langchain.com/oss/deepagents/code/memory-and-skills
   - Claude-compatible customization surface: "Claude-compatible hooks and plugins", Claude- and Codex-style plugin manifests and marketplaces, skills. (integration) — https://www.langchain.com/dcode, https://docs.langchain.com/oss/deepagents/code/plugins
   - Production stack: opinionated harness "tuned for long-horizon, multi-step work" on LangGraph (streaming, persistence, checkpointing), extensible "without forking", with LangSmith tracing/evals and remote sandbox execution. (capability / workflow) — https://github.com/langchain-ai/deepagents, https://docs.langchain.com/oss/deepagents/code/remote-sandboxes

3. **Stated audience:** Teams that need inspectable, configurable agents — control over models, tools, memory, approvals, and execution environment (dcode page); developers building LLM-powered agents and applications (SDK docs); terminal-first developers wanting persistent-memory agents (CLI launch post). — https://www.langchain.com/dcode, https://docs.langchain.com/oss/javascript/deepagents/overview

4. **Positioning against others:** Yes — the repo README calls dcode "similar to Claude Code or Cursor, powered by any LLM" (https://github.com/langchain-ai/deepagents); the dcode page contrasts owning the agent with a "fixed coding assistant" (https://www.langchain.com/dcode). The FAQ also positions Deep Agents within LangChain's own stack vs LangGraph and `create_agent`.

5. **Evidence offered for claims:** No benchmarks or adoption numbers offered for dcode itself. Company-level evidence on langchain.com: "35% of the Fortune 500", 1B+ open source downloads, 1B+ LangSmith events/day (https://www.langchain.com/about); customer logos on the dcode page (Klarna, Rippling, Lyft, Nvidia, LinkedIn, Coinbase, etc.) are company-wide, not dcode-specific (https://www.langchain.com/dcode). A demo video appears on the docs overview page.

6. **Notable silences:** No plan mode / read-only planning mode for the CLI; no sandboxing-by-default claim for local runs (sandboxes are opt-in remote); no first-party IDE extension or web/desktop surface (editors reached via ACP); no enterprise controls (SSO/policy) for the agent itself (those live in LangSmith); no benchmark results (SWE-bench etc.); no Windows support; ACP support is documented but not marketed as a differentiator; MCP support documented but not headlined.

7. **Confidence:** High — materials are plentiful and consistent (dedicated product page with an explicit tagline, launch blog, full docs set, README with positioning and FAQ); the only blur is that SDK-level claims and CLI-level claims are interleaved across the same materials.

Sources: https://www.langchain.com/dcode ; https://github.com/langchain-ai/deepagents (README) ; https://docs.langchain.com/oss/deepagents/code/overview ; https://docs.langchain.com/oss/deepagents/code/quickstart ; https://docs.langchain.com/oss/deepagents/code/plugins ; https://docs.langchain.com/oss/deepagents/code/memory-and-skills ; https://docs.langchain.com/oss/javascript/deepagents/overview ; https://www.langchain.com/blog/introducing-deepagents-cli ; https://www.langchain.com/about ; https://www.langchain.com/pricing
