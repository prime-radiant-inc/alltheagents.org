# Standardized differentiation extraction: Mistral Vibe (census_slug: mistral-vibe)

Run 2026-08-21 against the maker's own materials only (listed under Sources). Scope note: the materials cover both the open-source Vibe CLI harness and, from May 2026, the rebranded "Vibe" product it sits inside; answers focus on the coding harness and flag product-wide claims.

1. One-sentence self-description: Mistral's open-source command-line coding assistant, powered by Mistral's models, that gives a conversational natural-language interface to explore, modify, and run code in your projects through a set of tools — usable in the terminal or, via the Agent Client Protocol, in editors, and (since May 2026) as the Code mode of Mistral's unified "Vibe" agent. (README; devstral-2-vibe-cli launch post; vibe-agent post)

2. Claimed differentiators (by prominence):
   - Open source and open models: the CLI is "Mistral's open-source CLI coding assistant" (Apache-2.0), launched alongside open-weight Devstral 2 / Devstral Small 2 coding models; the product page frames it as intelligence you own, with data-residency options. Kind: openness. https://github.com/mistralai/mistral-vibe ; https://mistral.ai/news/devstral-2-vibe-cli ; https://mistral.ai/products/vibe/
   - Cost efficiency of the model pairing: Devstral 2 claimed "7x more cost-efficient" than Claude Sonnet at real-world tasks, with competitive SWE-bench Verified (72.2%) at 5-28x fewer parameters than rivals; API prices $0.40/$2.00 per M tokens. Kind: price / performance. https://mistral.ai/news/devstral-2-vibe-cli
   - Local and self-hosted operation: Devstral Small 2 runs on consumer GPUs or CPU-only machines; docs state the CLI works with local models without Mistral services; Medium 3.5 self-hostable on four GPUs. Kind: capability / openness. https://mistral.ai/news/devstral-2-vibe-cli ; https://docs.mistral.ai/mistral-vibe/introduction ; https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5
   - One harness across surfaces, local-to-cloud: CLI, VS Code extension, and web Code Mode run "the same harness"; remote agents run sessions asynchronously in isolated cloud sandboxes, launchable from CLI or Le Chat, with "teleport" migrating a local session to the cloud keeping history and approval state. Kind: integration / workflow. https://mistral.ai/news/vibe-agent/ ; https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5
   - Agentic customization with clarify-first workflow: custom subagents, multi-choice clarifying questions before execution, slash-command skills (Agent Skills spec), unified agent modes combining tools and permissions, hooks, MCP servers, automatic updates. Kind: capability / workflow. https://mistral.ai/news/mistral-vibe-2-0/ ; https://github.com/mistralai/mistral-vibe

3. Stated audience: developers (README, PyPI classifiers); Vibe 2.0 post targets full-time developers on Le Chat Pro ("all-day coding"), teams with advanced needs, and students (50% Pro discount); product page adds teams and enterprises, with European data-residency emphasis. https://mistral.ai/news/mistral-vibe-2-0/ ; https://mistral.ai/pricing ; https://mistral.ai/products/vibe/

4. Positioning against others: Devstral 2 launch names competitors at the model level — "7x more cost-efficient than Claude Sonnet", 5x smaller than DeepSeek V3.2, 8x smaller than Kimi K2; no competing harness (Claude Code, Codex, Cursor) is named in the materials. https://mistral.ai/news/devstral-2-vibe-cli

5. Evidence the maker offers:
   - Benchmarks: Devstral 2 72.2% and Devstral Small 2 68.0% SWE-bench Verified (2025-12-09); Mistral Medium 3.5 77.6% SWE-bench Verified, 91.4 τ³-Telecom (2026-05-22). https://mistral.ai/news/devstral-2-vibe-cli ; https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5
   - Partner testimonials at launch: Kilo Code (17B tokens through Devstral 2 in first 24 hours), Cline (tool-calling success on par with best closed models); Zed integration, NVIDIA NIM support noted. https://mistral.ai/news/devstral-2-vibe-cli
   - Customer logos on the Vibe product page (product-wide, not CLI-specific): ASML, BNP Paribas, Luxembourg Government, CMA CGM, Abanca, Stellantis, La Banque Postale, SNCF. https://mistral.ai/products/vibe/
   - No CLI usage numbers (users, sessions, downloads) offered anywhere in the materials.

6. Notable silences: no usage/adoption numbers for the harness; no sandboxing story for local execution (only trust folders and approval prompts; sandboxes exist only for cloud remote agents); no enterprise policy/managed-settings marketing (admin config exists in changelog/docs but is not pitched); no SDK (only programmatic CLI mode); no plugin marketplace; no security-review or benchmark claims for the harness itself (all benchmark claims attach to the models); Windows support explicitly second-class ("officially support and target UNIX").

7. Confidence: high — materials are plentiful and consistent (README, three dated launch posts, product and pricing pages, docs), and the positioning (open source + open weights + cost + European ownership) repeats across all of them; the main reading risk is the May 2026 rebrand blurring CLI claims with whole-product claims, which this extraction separates explicitly.

Sources:
- https://github.com/mistralai/mistral-vibe (README)
- https://mistral.ai/news/devstral-2-vibe-cli (2025-12-09 launch)
- https://mistral.ai/news/mistral-vibe-2-0/ (2026-01-27)
- https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5 (2026-05-22)
- https://mistral.ai/news/vibe-agent/ (2026-05-28 rebrand)
- https://help.mistral.ai/en/articles/682992-le-chat-is-now-vibe
- https://mistral.ai/products/vibe/
- https://mistral.ai/pricing
- https://docs.mistral.ai/mistral-vibe/introduction
- https://docs.mistral.ai/vibe/code/cli/configuration
- https://github.com/mistralai/mistral-vibe/blob/main/docs/acp-setup.md
