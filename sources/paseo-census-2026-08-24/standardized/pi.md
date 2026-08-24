# Standardized differentiation extraction — Pi (census_slug: pi)

Run 2026-08-21 against official materials only (README, pi.dev homepage, docs landing, launch post, Earendil announcement/benchmark posts). No pricing page exists.

1. One-sentence self-description: Pi is a minimal terminal coding-agent harness that ships with a small core (four tools, short system prompt) and is meant to be adapted to the user's workflow through TypeScript extensions, skills, prompt templates, themes, and shareable packages rather than through built-in features.

2. Claimed differentiators (ordered by prominence):
   - Minimal core that deliberately omits features other harnesses bake in (MCP, sub-agents, plan mode, permission popups, built-in to-dos, background bash); users build or install them instead. Kind: capability / workflow. Sources: https://pi.dev/ ; https://github.com/earendil-works/pi/blob/main/packages/coding-agent/README.md#philosophy
   - Extensibility as the core product: TypeScript extensions with tools, commands, UI, and ~35 lifecycle events; skills (Agent Skills standard); prompt templates; themes; "Pi packages" shareable via npm/git; the agent can extend itself. Kind: capability / openness. Sources: https://pi.dev/ ; https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md
   - Multi-provider, bring-your-own model: subscription logins (Claude, ChatGPT/Codex, GitHub Copilot), ~30 API-key providers, local llama.cpp, mid-session model switching. Kind: model. Sources: https://github.com/earendil-works/pi/blob/main/packages/coding-agent/README.md#providers--models ; https://pi.dev/
   - Context efficiency and cost: minimal system prompt and "context engineering"; maker cites the Databricks benchmark (same pass rate as vendor harnesses at roughly half the cost, ~3x less context per turn). Kind: performance. Sources: https://earendil.com/posts/pi-autoresearch-and-databricks/ ; https://pi.dev/
   - Four run modes (interactive, print/JSON, RPC, SDK) making Pi embeddable as building blocks; OpenClaw cited as built on Pi components. Kind: integration. Sources: https://github.com/earendil-works/pi/blob/main/packages/coding-agent/README.md ; https://earendil.com/posts/announcing-pi-and-lefos/

3. Stated audience: developers who want to adapt the harness to their own workflows and keep full observability of what the agent does; no role seniority, team size, or language/stack stated. Sources: https://pi.dev/ ("Adapt Pi to your workflows, not the other way around") ; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/

4. Positioning against others: yes — the homepage and README contrast Pi with agents that "bake in" features, and the launch post contrasts Pi with Claude Code (described as having become a "spaceship" of unused features) and names Codex, opencode and Cursor as alternatives. Sources: https://pi.dev/ ("Features that other agents bake in, you can build yourself") ; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/ ; README "Philosophy"

5. Evidence offered:
   - Databricks benchmark on its multi-million-line codebase (cost/quality vs Claude Code and Codex) — https://earendil.com/posts/pi-autoresearch-and-databricks/ (linking https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase)
   - OpenClaw as a downstream user of Pi components — https://earendil.com/posts/announcing-pi-and-lefos/
   - Token-count comparisons for MCP vs CLI tools (225 tokens vs 13.7k–18k) — https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/
   - Site demos/screenshots and "50+ examples" of extensions; published own session dataset on Hugging Face — https://pi.dev/ ; README
   - No customer logos, user counts, or download figures published.

6. Notable silences: no enterprise controls (SSO, audit, policy) mentioned; no built-in sandboxing or permission system (explicitly absent, containerization documented instead); no ACP or IDE integration in official materials; no pricing or commercial tier; no native MCP, sub-agents, or plan mode (explicitly declined rather than silent); no benchmark numbers of its own beyond citing Databricks; no statements about data retention or telemetry beyond the install-ping note in README.

7. Confidence: high — materials are extensive (README, full docs, homepage, a long launch post, and company posts) and consistent with each other on positioning; the only gap is that some claims (OpenClaw relationship, benchmark interpretation) appear in company blog posts rather than product docs.

Sources:
- https://pi.dev/
- https://github.com/earendil-works/pi/blob/main/README.md
- https://github.com/earendil-works/pi/blob/main/packages/coding-agent/README.md
- https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/index.md
- https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md
- https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md
- https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/security.md
- https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/
- https://mariozechner.at/posts/2026-04-08-ive-sold-out/
- https://earendil.com/posts/announcing-pi-and-lefos/
- https://earendil.com/posts/pi-autoresearch-and-databricks/
