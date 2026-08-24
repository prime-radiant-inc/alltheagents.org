# Standardized differentiation extraction: Nova / Compass AI (census_slug: nova-compass)

Run 2026-08-24 per STANDARD_PROMPT.md v1. Official materials only (see Sources). Note: the portfolio page was readable only via a summarizing fetch; the npm README is the richest official material.

1. **One-sentence self-description:** The flagship Compass AI coding agent — a terminal CLI that plans, edits, verifies, and ships software in real repositories, integrated with IDEs and the wider Compass enterprise agent suite.

2. **Claimed differentiators:**
   - Built for production work, not demos: long-running sessions, dirty worktrees, real repositories, "teams that need more than a chat box pasted beside an editor" — kind: capability / audience — npm README
   - Guarded execution: file, shell, git, database, and external actions pass explicit safety rules; destructive or externally visible actions require confirmation — kind: trust-safety — npm README
   - Verification-first: passing tests, lint, and type checks are the completion criteria, "not vibes"; dedicated verification agents that check fixes without editing — kind: workflow — npm README
   - Model flexibility: Compass-managed models, Anthropic-compatible providers, OpenAI chat/responses with OAuth, Ollama, and registered custom endpoints — kind: model — npm README
   - One platform, many surfaces: Nova in the terminal/IDE alongside sibling agents in Excel, Outlook, PowerPoint, and Word; enterprise plans with SOC 2 / ISO 27001 / GDPR claims — kind: integration / trust-safety — https://www.compassap.ai/

3. **Stated audience:** Developers ("power users", the "elite of developers") inside teams and enterprises; platform pricing runs €40–€500 per seat per month — https://www.compassap.ai/portfolio/nova.html ; https://www.compassap.ai/

4. **Positioning against others:** No competitor named; category negation only — "more than a chat box pasted beside an editor" and "designed for production software work, not demo prompts" — npm README.

5. **Evidence offered:** "500+ enterprise teams", "99.9% uptime SLA", SOC 2 Type II / ISO 27001 / GDPR badges (company site, no auditor or customer names); no benchmarks, no case studies, no demos with named users — https://www.compassap.ai/

6. **Notable silences:** open source / source availability (MIT badge shown, source location never discussed), sandboxing technology behind "guarded execution", benchmark results, the Compass model proxy's plan gating, who is behind the company (no team page), ACP is documented but not marketed as a differentiator, no community channel.

7. **Confidence:** medium — the npm README is detailed and internally consistent, but the company site is marketing-heavy with unverifiable numbers, the portfolio page was only partially readable, and there is no launch post or changelog narrative to corroborate emphasis.

Sources: https://www.compassap.ai/portfolio/nova.html (summary fetch) ; https://www.compassap.ai/ (summary fetch) ; npm README for @compass-ai/nova@1.1.37 (dated 2026-06-24) ; https://github.com/Compass-Agentic-Platform/nova (README shell)
