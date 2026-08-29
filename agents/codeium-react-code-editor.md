---
name: "codeium-react-code-editor"
slug: "codeium-react-code-editor"
layout: "agent.njk"
category: "other"
maker: "Exafunction"
license: "MIT"
url: "https://github.com/Exafunction/codeium-react-code-editor"
source_code_url: "https://github.com/Exafunction/codeium-react-code-editor"
source_available: "True"
platforms:
  - "IDE"
first_released: "2023-12-11"
current_release: "2024-04-24"
stars: "274"
language: "TypeScript"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Codeium"
pricing: "free"
install_method: "npm install @codeium/react-code-editor"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@codeium/react-code-editor"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Free, open-source code editor React component wrapping Monaco editor with unlimited AI autocomplete powered by Codeium. No account required. Supports multi-document context for smarter autocompletion (up to 10 documents)."
---

This package exists for developers who need to embed a working code editor with AI completion into a web application without building the integration themselves. It wraps monaco-react — the React Monaco wrapper behind VS Code's editor — and adds Codeium's autocomplete service on top, requiring no user account and carrying no usage charge. Completions can reference up to ten additional documents through the otherDocuments prop, giving suggestions context beyond the visible file. The package exposes the underlying Monaco editor instance for direct API access and ships ESM and CommonJS builds, published as @codeium/react-code-editor on npm. It is a side utility from Exafunction, whose main product lines are the Windsurf plugin and editor, and its update cadence has been slow since 2024.
