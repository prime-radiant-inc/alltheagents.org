# Dossier: fast-agent (proposed census_slug: fast-agent)

Compiled 2026-08-21 (data fetched same day). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". NOT currently in the census — proposed new-entry frontmatter at the end. Central question addressed: framework vs shipping coding agent.

## 1. Identity

- name: fast-agent (PyPI packages `fast-agent-mcp` and wrapper `fast-agent-acp`)
- maker: individual — GitHub user **evalstate**, public author name "Shaun Smith" (PyPI author field; contact fastagent@llmindset.co.uk) [S3][S4] (as-of 2026-08-21). "llmindset" appears only as an email domain; no company entity found (researched, absent).
- product URL: https://fast-agent.ai | repo URL: https://github.com/evalstate/fast-agent [S1][S3]
- license: Apache-2.0 (GitHub API license field; both PyPI packages) [S1][S3][S4]. One README badge reportedly reads MIT — see section 6.
- open source? True. source_available: True — full source on GitHub, published on PyPI [S1][S3].
- first public: repo created 2025-01-18 [S1]; first PyPI release `fast-agent-mcp` 0.0.7 on 2025-02-22 [S4]. Acknowledged as building on lastmile-ai's `mcp-agent` by Sarmad Qadri [S2].
- latest release: `fast-agent-mcp` 0.10.10, 2026-08-23 (PyPI); repo last push 2026-08-23 — actively maintained [S4][S1]. ACP wrapper `fast-agent-acp` latest 0.4.52, 2026-02-11 (see section 6).
- what it is:
  - Form factor: CLI-first Python framework with an interactive terminal/TUI shell mode; also runs as an ACP server (Zed etc.), MCP server, and A2A endpoint [S2][S5][S1-topics].
  - Primarily an MCP-native agent FRAMEWORK ("build custom, multi-agent experiences in a few lines of code") that also ships a default interactive coding-agent surface: shell mode with file and command execution (`-x` flag), permission prompts, subagents, skills [S5][S2][S6] (maker-described).
  - Models: BYO multi-provider — native Anthropic, OpenAI, Google; Azure, Ollama, Deepseek, llama.cpp auto-config, OpenAI-compatible endpoints, "dozens via TensorZero" [S2][S6].
  - Pricing: free, open source, BYO API keys [S2].
  - Install: `uv tool install -U fast-agent-mcp` or `uvx fast-agent-mcp@latest -x`; Paseo's catalog command is `uvx --from fast-agent-acp fast-agent-acp -x` [S2][S5][task brief].
  - Default autonomy: in ACP mode tool calls "prompt for permission by default"; `-x` grants shell/terminal access [S5] (maker-described, not independently tested).
  - Language: Python [S1].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 3,901 | 2026-08-21 | [S1] | independently observable |
| GitHub forks | 438 | 2026-08-21 | [S1] | independently observable |
| GitHub watchers (subscribers) | 22 | 2026-08-21 | [S1] | independently observable |
| GitHub open issues | 30 | 2026-08-21 | [S1] | independently observable |
| PyPI downloads `fast-agent-mcp` | 178,427/month; 34,950/week | 2026-08-21 | [S7] | independently observable (PyPI counts include CI/mirror noise) |
| PyPI downloads `fast-agent-acp` | 5,057/month; 1,274/week | 2026-08-21 | [S7] | independently observable |
| Discord | server exists (discord.gg/xg5cJ7ndN6, linked from PyPI); member count not researched (null) | 2026-08-21 | [S4] | independently observable (existence only) |
| Maker usage claims | none found — no user/customer numbers on homepage or README | 2026-08-21 | [S2][S6] | researched, absent |
| Funding / customers / press | none found | 2026-08-21 | [S2][S6] | researched, absent |
| Ecosystem listing: Paseo | in Paseo's ACP catalog ("code and build agents with comprehensive multi-provider support") | 2026-08-21 | task brief | independently observable |
| Benchmark placements | none researched beyond homepage accuracy/cost-efficiency claims (maker-claimed, no third-party board found) | 2026-08-21 | [S6] | null/absent |

## 3. Plugin interface (PRI-2925)

- mcp_support: **both (client + server)** — repo topics `mcp-client`/`mcp-server`; claims "first framework with complete, end-to-end tested MCP Feature support including Sampling and Elicitations"; in ACP mode "MCP Servers supplied by the Client are attached to the Agent" [S1][S2][S5]. Evidence: https://fast-agent.ai
- plugin_support: **True** — Agent Skills system with a registry/marketplace: `/skills add` browses and installs; three default registries (fast-agent Skills, HuggingFace Skills, Anthropic Skills); skills configure LSP, hooks, compaction, automation; skill dirs/registries set in `fast-agent.yaml` [S8] (as-of 2026-08-21). Evidence: https://fast-agent.ai/agents/skills/
- claude_code_plugin: **partial** — consumes the open Agent Skills `SKILL.md` format shared with Claude Code and ships an "Anthropic Skills" registry by default; no evidence it reads `.claude/` dirs or implements the Claude Code plugin/marketplace format [S8] (as-of 2026-08-21).
- subagents: **True** — "built-in subagents", agent chaining, multi-agent workflows; in ACP each defined Agent appears as a Mode [S2][S5].
- hooks: **True** — "Agent and Tool Hooks" set up via the skills registry [S8][S2].
- plan_mode: **True (qualified)** — README lists "Plan mode (full/iterative orchestration)"; ACP docs mention an "Iterative Planner" reporting progress; whether it is a read-only gate like Claude Code's plan mode was not verified [S2][S5].
- plugin_docs_url: https://fast-agent.ai/agents/skills/ | config_docs_url: https://fast-agent.ai (fast-agent.yaml reference; exact page not pinned)
- ACP support: **yes, first-party** — "comprehensive support for Zed Industries Agent Client Protocol"; `agent-client-protocol` is a direct dependency; Zed config example in docs; `fast-agent-acp` is a thin convenience wrapper around `fast-agent-mcp`'s ACP entrypoint [S5][S4][S3].
- Other protocols: A2A (repo topics/description), MCP Apps, OpenAI Apps SDK integration [S1][S2].
- SDK: **yes** — this IS the SDK: a Python framework (decorator-based agent definitions) published on PyPI [S2][S4].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (homepage): "The harness your model deserves. Same model, better results." [S6]; repo description: "Code, Build and Evaluate agents - excellent Model and Skills/MCP/ACP/A2A Support" [S1].
- maker claims (paraphrased):
  1. First framework with complete end-to-end-tested MCP feature support, including Sampling and Elicitations [S2].
  2. Multi-provider model coverage: Anthropic/OpenAI/Google native, plus Azure, Ollama, Deepseek, llama.cpp, TensorZero [S2][S6].
  3. Accuracy and cost-efficiency via context management ("Same model, better results") [S6].
  4. Quad-play protocol surface: MCP (client+server), ACP, A2A, Agent Skills [S1][S2].
  5. Skills marketplace with three default registries (fast-agent, HuggingFace, Anthropic) [S8].
  6. Diagnostics: "only tool that allows you to inspect Streamable HTTP Transport usage" [S2].
  7. Coding-agent shell mode with subagents, LSP, hooks, compaction, permissions [S2][S5].
  8. Multimodal: structured outputs, vision, PDF [S2].
- audience: developers and automation engineers building agentic workflows, coding assistants, eval platforms [S2][S6]; also positions the default shell as a usable coding agent for end users [S2].

## 5. Company & contact targets (PRI-2929)

- Not a company. Individual maintainer: GitHub **evalstate**, public name "Shaun Smith" (PyPI author field), project email fastagent@llmindset.co.uk [S3][S4]. Public repo identity only recorded per instruction.
- Contact paths the project offers: GitHub issues, Discord (discord.gg/xg5cJ7ndN6) [S4].
- Funding stage: none found (researched, absent).

## 6. Open questions / conflicts

- License conflict: GitHub API + both PyPI packages say Apache-2.0 [S1][S3][S4]; the README fetch reported an MIT badge [S2]. Apache-2.0 is the safe record; the badge reading may be a summarization artifact — verify LICENSE file directly if it matters.
- ACP wrapper staleness: `fast-agent-acp` latest is 0.4.52 (2026-02-11) pinning `fast-agent-mcp==0.4.52`, while `fast-agent-mcp` is at 0.10.10 (2026-08-23) [S3][S4]. Paseo's `uvx --from fast-agent-acp` command therefore launches a ~6-month-old build; the current docs instead say `uvx fast-agent-acp@latest --model …` / install `fast-agent-mcp` [S5]. Worth flagging to Paseo.
- fast-agent.ai/agents/skills/ returned 404 to direct fetch but is indexed with full content by search [S8] — possibly fetch-blocking; content taken from search snippets.
- Discord member count, contributor count, and commit cadence: null (not researched, budget).
- "First framework with complete MCP support", "only tool" for HTTP transport inspection: maker-claimed superlatives, not independently verified.
- Repo history: evalstate/fast-agent began as a fork/derivative of lastmile-ai/mcp-agent (acknowledged in README) [S2]; PyPI report lists repository URL "evalstate/fast-agent-mcp" [S4] which now resolves to evalstate/fast-agent — old name.

## 7. Sources

1. [S1] https://api.github.com/repos/evalstate/fast-agent — stars, forks, license, dates, topics, description
2. [S2] https://raw.githubusercontent.com/evalstate/fast-agent/main/README.md — claims, features, install, mcp-agent acknowledgment
3. [S3] https://pypi.org/pypi/fast-agent-acp/json — wrapper package, versions, pin, owner
4. [S4] https://pypi.org/pypi/fast-agent-mcp/json — versions, author, license, deps, Discord link
5. [S5] https://fast-agent.ai/acp/ — ACP support, permissions, modes, commands
6. [S6] https://fast-agent.ai/ — tagline, positioning, providers
7. [S7] https://pypistats.org/api/packages/fast-agent-mcp/recent and /fast-agent-acp/recent — downloads
8. [S8] web search of fast-agent.ai/agents/skills/ — skills format, registries, /skills command

## Inclusion check (Jesse's test)

**Yes** — fast-agent is primarily an agent framework, but it ships its own agentic loop (native multi-provider LLM infrastructure, tool calling, subagents) and a first-party default coding-agent surface (interactive shell with file/command execution, permissions, skills); its ACP package exposes that native loop, not another vendor's agent [S2][S5][S6]. Include as `category: agent`, with the framework nature noted in the body.

## Proposed census frontmatter (per hc/agents/_TEMPLATE.md — do not write into hc/)

```yaml
name: "fast-agent"
slug: "fast-agent"
layout: "agent.njk"
category: "agent"            # framework that ships a first-party coding agent + ACP server
maker: "evalstate"           # individual: Shaun Smith (GitHub evalstate)
license: "Apache-2.0"
url: "https://fast-agent.ai"
source_code_url: "https://github.com/evalstate/fast-agent"
source_available: true
homepage: "https://fast-agent.ai"
docs_url: "https://fast-agent.ai"
download_url: "https://pypi.org/project/fast-agent-mcp/"
install_method: "uv tool install fast-agent-mcp; uvx fast-agent-mcp@latest -x; ACP via fast-agent-acp"
platforms: ["CLI"]
autonomy_level: ["agentic"]
specialization: "general"
language: "Python"
first_released: "2025-02-22"   # first PyPI release (repo created 2025-01-18)
current_release: "2026-08-23"
maintained: "active"
mcp_support: "both (client incl. sampling/elicitations; server mode)"
plugin_support: "yes — Agent Skills with registry/marketplace (/skills add; fast-agent, HuggingFace, Anthropic registries)"
claude_code_plugin: "partial (Agent Skills SKILL.md format; not .claude/ dirs or plugin marketplace)"
subagents: "yes"
hooks: "yes (agent/tool hooks via skills)"
plan_mode: "yes (iterative planner/orchestration)"
plugin_docs_url: "https://fast-agent.ai/agents/skills/"
config_docs_url: "https://fast-agent.ai"
model_providers: "Anthropic, OpenAI, Google, Azure, Ollama, Deepseek, llama.cpp, TensorZero, OpenAI-compatible"
pricing: "BYOK"
github_stars: 3901
sources: ["paseo-acp-catalog"]
last_verified: "2026-08-21"
what_makes_it_special: "An MCP-native Python agent framework that doubles as a coding agent: claims the most complete MCP feature support (sampling, elicitations), speaks ACP/A2A, and installs skills from fast-agent, HuggingFace, and Anthropic registries."
```
