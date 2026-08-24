# Standardized differentiation extraction: Junie (census_slug: junie-cli)

Run 2026-08-21 against the maker's own materials only (listed under Sources).

1. One-sentence self-description: An LLM-agnostic AI coding agent by JetBrains that works from the terminal, inside JetBrains IDEs, and in CI/CD pipelines, planning before it codes and running on any model the user chooses. (README; junie.jetbrains.com; GA post)

2. Claimed differentiators (by prominence):
   - Works with any model you choose: LLM-agnostic, "without lock-in" — subscription credits, Junie API key, BYOK at "provider-rate pricing, zero markup" (OpenAI, Anthropic, Google, xAI, OpenRouter, Copilot), or local runtimes (Ollama, LM Studio, LiteLLM). Kind: model / price. https://junie.jetbrains.com/ ; https://github.com/JetBrains/junie ; https://junie.jetbrains.com/blog/junie-coding-agent-out-of-beta
   - Powered by the IDE ("IntelliJ IDEA Engine"): uses the IDE's semantic index, build and test configurations, database connections, and the real debugger — including agentic debugging with breakpoints and runtime-state inspection — instead of approximations. Kind: capability / integration. https://junie.jetbrains.com/ ; https://junie.jetbrains.com/blog/junie-coding-agent-out-of-beta
   - Plans before it codes: Advanced Plan Mode produces a structured, editable design document (requirements, design, delivery, testing) stored in .junie/plans and committable; the maker frames it as fewer wasted tokens and "plan on a strong model; implement on a cheap one". Kind: workflow / price. https://junie.jetbrains.com/blog/junie-coding-agent-out-of-beta ; https://junie.jetbrains.com/
   - Benchmark performance: "Top performer on SWE-Rebench" (site badge); at GA, the number-one coding agent on the latest SWE-Rebench run with 61.6% resolved and 72.7% pass@5, quoted from Nebius' research lead. Kind: performance. https://junie.jetbrains.com/ ; https://junie.jetbrains.com/blog/junie-coding-agent-out-of-beta
   - Control plus asynchrony: human-in-the-loop approvals with a dynamic Action Allowlist and graded Brave mode; Live Prompting to steer mid-task (labeled an "Exclusive feature"); Remote Control to start a task on a laptop and monitor from a phone; one engine across AI chat, IDE tool window, and CLI via ACP. Kind: trust-safety / workflow. https://junie.jetbrains.com/ ; https://junie.jetbrains.com/blog/junie-coding-agent-out-of-beta

3. Stated audience: professional developers, with JetBrains IDE users foregrounded (the IDE plugin is "the recommended way"; deep debugger/database features require JetBrains IDEs with an AI subscription); the CLI targets terminal, "any IDE", and CI/CD (GitHub/GitLab) users; free tier pitched at individuals ("No card or subscription required"), AI Ultimate "Recommended for Junie", organizations via org billing. https://junie.jetbrains.com/ ; https://www.jetbrains.com/help/junie/junie-ide-plugin.html

4. Positioning against others: no competitor named. Clear allusions: "Stop switching tools", "Hassle-Free Migration — switch from other AI coding agents in seconds", supports "any model... without lock-in", and a contrast with agents that guess — "most coding agents add log statements. Junie opens the debugger" (paraphrase-adjacent). Docs advertise importing .claude/, .cursor/, and .codex/ skills and agents. https://junie.jetbrains.com/ ; https://junie.jetbrains.com/blog/junie-coding-agent-out-of-beta ; https://www.jetbrains.com/help/junie/agent-skills.html

5. Evidence the maker offers:
   - SWE-Rebench: #1 coding agent on the GA-time run, 61.6% resolved / 72.7% pass@5, with a quote attributed to Alexander Golubev, Research Lead at Nebius. https://junie.jetbrains.com/blog/junie-coding-agent-out-of-beta
   - "343K Junie users" and "1M+ AI-assisted actions completed"; 240% YoY growth in active paid AI users (Q4 2024 - Q4 2025). https://www.jetbrains.com/lp/annualreport-2026/
   - Internal model evaluation: on a private benchmark of real recent commits, Gemini 3.7 Flash "matched the solve rate" of the premium Sonnet-5 midtier at roughly a third of the cost. https://junie.jetbrains.com/blog/junie-gemini-3-7-flash
   - SOC 2 certification claim for JetBrains tools. https://junie.jetbrains.com/
   - No customer names or case studies specific to Junie.

6. Notable silences: no open-source claim (license all-rights-reserved, not discussed); no sandboxing/isolation story for shell commands (only approval prompts and allowlists); no SDK for embedding the agent; no absolute pricing-per-token disclosure beyond credits; no enterprise-control detail on the Junie site itself (AI Enterprise mentioned only in docs); MCP, hooks, subagents, and extensions are documented but barely marketed on the homepage; no uptime/security whitepaper linked; no named team or leadership on the product site.

7. Confidence: high — materials are consistent and dated (product site, README, two launch posts, GA post, docs), and the differentiation story (model-agnosticism + IDE power + plan-first) repeats across all of them; the main caveat is that adoption numbers live in a company-wide annual report rather than Junie-specific announcements.

Sources:
- https://junie.jetbrains.com/
- https://github.com/JetBrains/junie (README)
- https://junie.jetbrains.com/blog/junie-coding-agent-out-of-beta
- https://junie.jetbrains.com/blog/junie-gemini-3-7-flash
- https://junie.jetbrains.com/whats-new
- https://www.jetbrains.com/help/junie/junie-cli.html
- https://www.jetbrains.com/help/junie/junie-cli-acp.html
- https://www.jetbrains.com/help/junie/junie-cli-extensions.html
- https://www.jetbrains.com/help/junie/agent-skills.html
- https://www.jetbrains.com/help/junie/junie-ide-plugin.html
- https://blog.jetbrains.com/junie/2026/03/junie-cli-the-llm-agnostic-coding-agent-is-now-in-beta/
- https://blog.jetbrains.com/junie/2025/01/meet-junie-your-coding-agent-by-jetbrains/
- https://www.jetbrains.com/lp/annualreport-2026/
