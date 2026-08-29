---
name: "Qodo"
slug: "qodo"
layout: "agent.njk"
category: "other"
maker: null
license: null
url: "https://www.qodo.ai/"
source_code_url: null
source_available: "False"
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: null
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic, Azure OpenAI, self-hosted (BYOK)"
pricing: "Pro Team: $0.012/credit (2,500-20,000 credit tiers); 14-day free trial; Enterprise with SSO/BYOK/on-prem"
install_method: "IDE plugins (VS Code, JetBrains, Visual Studio) and Git provider integration (GitHub, GitLab, Bitbucket, Azure DevOps, Gerrit)"
docs_url: "https://docs.qodo.ai/qodo-documentation"
plugin_docs_url: "https://marketplace.visualstudio.com/items?itemName=Codium.codium"
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=Codium.codium"
maintained: "active"
sources:
  - "caramaschi"
what_makes_it_special: "AI code review and governance platform with highest F1-score on AI code review benchmark; Context Engine pulls across rules, codebase, PR history; Cross-Repo Review across dependent repos and Git providers; Living Rules System auto-mines enforceable rules from PR history; SOC 2 Type II, zero data retention."
---

Qodo targets the quality side of AI-assisted development: as coding agents produce more code, someone still has to verify it, and Qodo builds that verification layer. Its Git product runs multi-agent review on pull requests across GitHub, GitLab, Bitbucket, Azure DevOps, and Gerrit, with specialized agents checking bugs, rule violations, ticket compliance, and duplicated logic. A Context Engine indexes the codebase, PR history, rules, and business requirements so review reasons from the full system rather than the diff alone, enabling cross-repo and cross-provider review of interdependent services. A self-learning Rules Miner converts reviewer comments into enforceable standards, and a governance portal tracks risk and audit trails across the organization. The same context engine and rules power IDE plugins, Git review, and CLI surfaces, and the platform also governs third-party AI coding agents by enforcing skill review standards. Enterprise customers adopt it for SOC 2-aligned, zero-retention review with BYOK and on-premises deployment options.
