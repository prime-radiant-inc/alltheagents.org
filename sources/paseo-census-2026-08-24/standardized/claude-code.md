# Standardized differentiation extraction: Claude Code (census_slug: claude-code)

Run 2026-08-21 against the maker's own materials only (listed under Sources).

1. One-sentence self-description: An agentic coding tool from Anthropic that lives in the terminal (and IDE, desktop, web, Slack), reads your codebase, edits files, runs commands and git workflows, and integrates with your development tools through natural-language instructions. (README; docs overview)

2. Claimed differentiators (by prominence):
   - Terminal-native and composable: works in your terminal, follows the Unix philosophy (pipe logs in, run in CI, chain with other tools via `claude -p`). Kind: workflow. https://github.com/anthropics/claude-code ; https://code.claude.com/docs/en/overview
   - One engine, every surface: the same CLAUDE.md, settings and MCP servers work across terminal, VS Code/JetBrains, desktop app, web/mobile, Slack, GitHub/GitLab CI; sessions move between surfaces (Remote Control, teleport, /desktop). Kind: integration. https://code.claude.com/docs/en/overview ; https://claude.com/product/claude-code
   - Deep codebase understanding with multi-file edits: maps and explains entire codebases via agentic search, plans and implements across files, verifies. Kind: capability. https://claude.com/product/claude-code ; https://code.claude.com/docs/en/overview
   - Extensible and customizable: CLAUDE.md + auto memory, skills, hooks, plugins and marketplaces, MCP, subagents, agent teams, dynamic workflows, Agent SDK for custom agents. Kind: capability / openness (of the extension surface, not the source). https://code.claude.com/docs/en/overview ; https://code.claude.com/docs/en/plugins ; https://code.claude.com/docs/en/agent-sdk/overview
   - Autonomy with control: runs locally and asks permission before changes (product page); permission modes incl. plan mode, sandboxing, managed enterprise settings, auto mode with a safety classifier; background/cloud/scheduled agents. Kind: trust-safety / workflow. https://claude.com/product/claude-code ; https://code.claude.com/docs/en/permission-modes

3. Stated audience: developers ("helps you code faster"); individual developers on Pro, teams and enterprises on Max/Team/Enterprise; "power users in larger codebases"; enterprises needing Bedrock/Vertex/Foundry and managed policy. https://github.com/anthropics/claude-code ; https://claude.com/product/claude-code ; https://code.claude.com/docs/en/setup

4. Positioning against others: not claimed by name. Closest: product page says it works "alongside existing tools" without changing workflow; the Agent SDK page distinguishes itself from the Client SDK (where "you implement the tool loop yourself") and from Managed Agents. https://claude.com/product/claude-code ; https://code.claude.com/docs/en/agent-sdk/overview

5. Evidence the maker offers:
   - Run-rate revenue >$2.5B, more than doubled since start of 2026; weekly active users doubled since Jan 1 (2026-02-12). https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation
   - $1B run-rate six months after GA; named users Netflix, Spotify, KPMG, L'Oreal, Salesforce (2025-12-03). https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone
   - Customer stories: Rakuten (7-hour autonomous run, 24->5 days, 79% faster TTM), Ramp (1M+ lines in 30 days, 50% weekly-active engineers); logos Ramp, Intercom, Notion, GitLab, Stripe, Sentry, AWS, Datadog, GitHub, Vercel etc. https://claude.com/customers/rakuten ; https://claude.com/customers/ramp ; https://claude.com/product/claude-code
   - Launch claim: single-pass completion of tasks that "would normally take 45+ minutes" (2025-02-24). https://www.anthropic.com/news/claude-3-7-sonnet
   - Usage research on ~400k sessions (2026-06-16). https://www.anthropic.com/research/claude-code-expertise
   - No benchmark scores on the product page, README, or docs overview.

6. Notable silences: no benchmark results (SWE-bench/Terminal-Bench) in the product materials; no open-source/source-availability claim (license is all-rights-reserved, not highlighted); no multi-model/BYO-model support beyond Anthropic models via Bedrock/Vertex/Foundry; no Agent Client Protocol (ACP) mention; no absolute user counts (only growth multiples); no pricing per token on the product page.

7. Confidence: high — materials are extensive (README, docs overview, product page, pricing, three dated Anthropic announcements with numbers, customer pages), and the claims are consistent across them; the one tension is the product page's "asks permission" framing versus docs making auto mode the default on paid plans.

Sources:
- https://github.com/anthropics/claude-code (README)
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/setup
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/agent-sdk/overview
- https://claude.com/product/claude-code
- https://claude.com/pricing
- https://www.anthropic.com/news/claude-3-7-sonnet
- https://www.anthropic.com/news/claude-4
- https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation
- https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone
- https://www.anthropic.com/research/claude-code-expertise
- https://claude.com/customers/rakuten
- https://claude.com/customers/ramp
