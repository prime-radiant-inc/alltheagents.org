# Standardized differentiation extraction: TRAE CLI / Trae Agent (census_slug: trae-agent)

Run 2026-08-24 against the makers' own materials only (listed under Sources). NOTE: this slug covers two distinct ByteDance products (see dossier section 0); the schema is answered for **TRAE CLI (TraeCode CLI), the commercial product Paseo drives**, with a short appendix for the open-source trae-agent repo.

## A. TRAE CLI (TraeCode CLI)

1. One-sentence self-description: A dedicated terminal Code Agent for TRAE Enterprise (flagship-tier) customers that takes natural-language instructions to write and modify code, run tests and lint, and automate Git workflows, extensible via MCP. (docs.trae.cn/cli_what-is-trae-cli)

2. Claimed differentiators (by prominence):
   - Dedicated "Code Agent" that automates repetitive development work (coding, testing, Git) so developers can focus on higher-value creative work. Kind: capability / workflow. https://docs.trae.cn/cli_what-is-trae-cli
   - Ready to use with minimal configuration; auto-updates on startup. Kind: workflow. https://docs.trae.cn/cli_what-is-trae-cli ; https://docs.trae.cn/cli_get-started-with-trae-cli
   - Multiple built-in large language models plus OpenAI/Claude model support, defaulting to "Max mode". Kind: model. https://docs.trae.cn/cli_what-is-trae-cli
   - Highly extensible: MCP servers (stdio/SSE/streamable HTTP, OAuth), skills (SKILL.md), custom agents with automatic task delegation, custom slash commands. Kind: integration / capability. https://docs.trae.cn/cli_model-context-protocol ; https://docs.trae.cn/cli_skills ; https://docs.trae.cn/cli_agent
   - Fits enterprise/CI automation: headless `-p/--json`, allowed/disallowed tool lists, git-worktree isolation, permission modes incl. plan mode; first-party ACP server (`traecli acp serve`) for use inside other clients. Kind: workflow / integration / trust-safety. https://docs.trae.cn/cli_use-cases ; https://docs.trae.cn/cli_permission-mode ; https://docs.trae.cn/cli_acp

3. Stated audience: customers of the TRAE Enterprise Edition flagship tier (企业版旗舰版套餐); developers working in terminals and CI. https://docs.trae.cn/cli_what-is-trae-cli — no role/stack breakdown claimed.

4. Positioning against others: not claimed. No competitor is named in the CLI docs. (The broader TRAE materials position IDE Mode vs SOLO Mode as complementary rather than against rivals: 2025-09-23 launch press release, www.trae.ai.)

5. Evidence the maker offers: none offered in the CLI docs (no benchmarks, user counts, or customer names). Product-family evidence elsewhere: Trae "2025 Product Report" — 6M+ registered users, 1.6M+ MAU, ~100B lines of code generated in 2025 (maker report, 2025-12-29, as relayed by its own report coverage); SWE-bench Verified 75.20% Pass@1 claimed for the research agent (arXiv 2507.23370).

6. Notable silences: no pricing for the CLI itself (bundled with enterprise flagship tier); no open-source claim (it is closed); no sandboxing claim; no hooks; no SDK; no BYO API keys; no model-vendor lock-in discussion; no security/enterprise-controls page in the CLI doc set read; no international (trae.ai) availability — CLI docs exist only on docs.trae.cn.

7. Confidence: medium — the CLI doc set (docs.trae.cn/cli_*) is coherent and current ("TraeCode CLI 1.0") but China-only, marketing-light, and there is no launch post or pricing page for the CLI; positioning is inferred from docs rather than a maker manifesto.

## B. Appendix: trae-agent (github.com/bytedance/trae-agent)

1. One-sentence self-description: An open-source (MIT) LLM-based agent for general-purpose software-engineering tasks with a CLI that executes natural-language instructions using multiple LLM providers. (README)
2. Claimed differentiators: transparent, modular, "research-friendly design" for studying agent architectures and ablation studies (kind: openness / audience, README); multi-LLM support — OpenAI, Anthropic, Doubao, Azure, OpenRouter, Ollama, Gemini (kind: model, README); Lakeview concise step summaries (kind: capability, README); trajectory recording for debugging/analysis (kind: capability, README); test-time scaling ensemble ranked first on SWE-bench Verified at 75.20% (kind: performance, arXiv 2507.23370).
3. Stated audience: researchers, academic and open-source communities, developers extending the agent. (README)
4. Positioning against others: yes — a "Difference with Other CLI Agents" README section: unlike other CLI agents, it is a platform for research and modification rather than a product. (README)
5. Evidence offered: arXiv technical report 2507.23370 with SWE-bench Verified 75.20% Pass@1, claimed first place.
6. Notable silences: no ACP, no hooks, no plan mode, no skills/plugins, no sandboxing beyond Docker mode, no pricing (free), no user numbers.
7. Confidence: high — README + paper are explicit; but note repo activity stopped 2026-02-05.

Sources:
- https://docs.trae.cn/cli_what-is-trae-cli
- https://docs.trae.cn/cli_get-started-with-trae-cli
- https://docs.trae.cn/cli_use-cases
- https://docs.trae.cn/cli_slash-commands
- https://docs.trae.cn/cli_agent
- https://docs.trae.cn/cli_skills
- https://docs.trae.cn/cli_model-context-protocol
- https://docs.trae.cn/cli_acp
- https://docs.trae.cn/cli_permission-mode
- https://www.trae.ai/ (product split: TraeWork / TraeCode)
- TRAE global launch press release, 2025-09-23 (Reuters-carried)
- https://github.com/bytedance/trae-agent (README)
- https://arxiv.org/abs/2507.23370
