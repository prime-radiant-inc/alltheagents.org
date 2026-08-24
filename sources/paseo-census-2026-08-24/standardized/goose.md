# Standardized differentiation extraction: goose (census_slug: goose)

Run 2026-08-21 against the maker's own materials only (listed under Sources). "Maker" = Block (originator, author of the launch post and shareholder letters) and the goose project's own site/repo (now under AAIF).

1. One-sentence self-description: A native, open source, general-purpose AI agent that runs on your own machine — as a desktop app, CLI, and API — for code, workflows "and everything in between", working with many LLM providers and extended through MCP. (README; homepage)

2. Claimed differentiators (by prominence):
   - Open source and locally run: Apache-2.0, "runs on your machine", native desktop app for macOS/Linux/Windows plus a full CLI and an embeddable API, built in Rust; governed in the open at the Agentic AI Foundation / Linux Foundation. Kind: openness / capability. https://github.com/aaif-goose/goose ; https://goose-docs.ai/ ; https://goose-docs.ai/blog/2026/04/07/goose-moves-to-aaif/
   - Any model: "15+ providers" (Anthropic, OpenAI, Google, Ollama, OpenRouter, Azure, Bedrock ...), API keys or your existing Claude/ChatGPT/Gemini subscriptions via ACP; governance value "not bound to specific models"; Block: built "to work with any model because betting on a single lab means inheriting its ceiling". Kind: model / openness. https://github.com/aaif-goose/goose ; https://goose-docs.ai/docs/getting-started/providers ; https://github.com/aaif-goose/goose/blob/main/GOVERNANCE.md ; https://s29.q4cdn.com/628966176/files/doc_financials/2026/q2/Q2-2026-Shareholder-Letter.pdf
   - Extensible via the MCP open standard: "70+ extensions", built-in extensions that are themselves MCP servers, MCP Apps with interactive UIs, extension directory and deep links. Kind: integration / capability. https://github.com/aaif-goose/goose ; https://goose-docs.ai/ ; https://goose-docs.ai/docs/getting-started/using-extensions
   - Beyond code and beyond suggestions: a general-purpose agent for research, writing, automation, data analysis; "goes beyond code suggestions - install, execute, edit, and test". Kind: audience / capability. https://goose-docs.ai/ ; https://github.com/aaif-goose/goose (repo description)
   - Workflow packaging and parallelism with safety controls: Recipes (portable YAML workflows, subrecipes, deep links), subagents for parallel tasks, and security features — prompt-injection detection, "sandbox mode", adversary mode, extension allowlists, permission modes. Kind: workflow / trust-safety. https://goose-docs.ai/ ; https://goose-docs.ai/docs/guides/recipes/ ; https://goose-docs.ai/docs/guides/security/ ; https://goose-docs.ai/docs/guides/managing-tools/goose-permissions

3. Stated audience: developers first — launch post says the "first use cases" are software engineering, for Block developers and the open source community (https://block.xyz/inside/block-open-source-introduces-codename-goose); homepage/README widen it to anyone who needs research, writing, automation or data analysis ("not just for code") (https://goose-docs.ai/ ; https://github.com/aaif-goose/goose). No team-size or language/stack targeting claimed.

4. Positioning against others: no competitor named. Allusions: "goes beyond code suggestions" (vs. autocomplete-style assistants) — https://github.com/aaif-goose/goose ; "Not just for code" — https://goose-docs.ai/ ; Block's letter contrasts single-lab tools: "betting on a single lab means inheriting its ceiling" — https://s29.q4cdn.com/628966176/files/doc_financials/2026/q2/Q2-2026-Shareholder-Letter.pdf ; ACP providers pitched as using goose with existing Claude Code / ChatGPT subscriptions "no per-token API costs" — https://goose-docs.ai/docs/guides/acp-providers

5. Evidence the maker offers:
   - Community counters on the homepage: "45,000+ GitHub stars", "500+ contributors", "70+ MCP extensions" — https://goose-docs.ai/
   - Badges in README: Linux Foundation Insights health score, Discord, Trendshift — https://github.com/aaif-goose/goose
   - Block internal usage (Block shareholder letters): began developing goose in early 2024, "first agentic harness" for enterprise work; production code changes per engineer up >2.5x vs January (mid-April 2026); Builderbot (built from goose) reviewed >90% of production code-change requests and made 15% of production changes nearly autonomously; in June 2026 agentic AI helped write and review "nearly all" production code changes — https://s29.q4cdn.com/628966176/files/doc_financials/2026/q1/Block_Q1-2026-Shareholder-Letter.pdf ; https://s29.q4cdn.com/628966176/files/doc_financials/2026/q2/Q2-2026-Shareholder-Letter.pdf
   - Block blog posts on internal use (detection engineering with Panther MCP; "MCP in the Enterprise: Real World Adoption at Block") — https://goose-docs.ai/blog/
   - No benchmarks, no named external customers, no download figures in the product materials.

6. Notable silences: no benchmark results (SWE-bench/Terminal-Bench); no named external customers or logos; no pricing page (free/BYO-key implied, not stated as a claim); plan mode exists in docs but is not marketed on homepage/README; no enterprise admin/SSO/policy story beyond allowlists and custom distributions; no SDK in a specific language (only "API"); hooks and plugins are docs-only, not headline claims; no statement of who maintains goose day-to-day post-donation (Block's ongoing role not spelled out on the move post); sandboxing is mentioned by name on the homepage but not detailed in the security index.

7. Confidence: high — README, homepage, quickstart, launch post, governance, and Block's shareholder letters are consistent (open source, local, any-model, MCP-extensible, general-purpose); the only tension is stale homepage counters (45k+ stars vs 53k observable) and an llms.txt line that still says "MIT licensed".

Sources:
- https://github.com/aaif-goose/goose (README, repo description)
- https://goose-docs.ai/ (homepage)
- https://goose-docs.ai/docs/quickstart
- https://goose-docs.ai/docs/getting-started/installation
- https://goose-docs.ai/docs/getting-started/providers
- https://goose-docs.ai/docs/getting-started/using-extensions
- https://goose-docs.ai/docs/guides/recipes/
- https://goose-docs.ai/docs/guides/security/
- https://goose-docs.ai/docs/guides/managing-tools/goose-permissions
- https://goose-docs.ai/docs/guides/acp-providers
- https://goose-docs.ai/docs/guides/context-engineering/plugins
- https://goose-docs.ai/llms.txt
- https://goose-docs.ai/blog/2026/04/07/goose-moves-to-aaif/
- https://goose-docs.ai/blog/authors
- https://github.com/aaif-goose/goose/blob/main/GOVERNANCE.md
- https://block.xyz/inside/block-open-source-introduces-codename-goose (launch post, 2025-01-28)
- https://s29.q4cdn.com/628966176/files/doc_financials/2026/q1/Block_Q1-2026-Shareholder-Letter.pdf (2026-05-07)
- https://s29.q4cdn.com/628966176/files/doc_financials/2026/q2/Q2-2026-Shareholder-Letter.pdf (2026-08-05)
