---
name: "tmux"
slug: "tmux"
layout: "agent.njk"
category: "other"
maker: "tmux"
license: "ISC"
url: "https://github.com/tmux/tmux"
source_code_url: "https://github.com/tmux/tmux"
source_available: "True"
platforms:
  - "CLI"
first_released: "2015-06-03"
current_release: "2026-08-19"
stars: "48734"
language: "C"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "Free (open source)"
install_method: "Binary packages (platform-specific), from release tarball (./configure && make && sudo make install), or from version control (git clone, sh autogen.sh, ./configure && make)"
docs_url: "https://github.com/tmux/tmux/wiki"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Terminal multiplexer that lets multiple terminals be created, accessed, and controlled from a single screen; sessions detach and keep running in the background, then reattach later. Runs on OpenBSD, FreeBSD, NetBSD, Linux, macOS, and Solaris. Not a coding agent harness; a foundational terminal tool. README does not describe a plugin system (third-party TPM exists but is not mentioned in the repo)."
---

tmux is a terminal multiplexer in the classic sense: it lets one screen create, access, and control many terminal sessions, with sessions detaching and continuing to run on a background server so work survives disconnections, SSH drops, and reboots. It is written in C against libevent and ncurses, runs on OpenBSD, FreeBSD, NetBSD, Linux, macOS, and Solaris, and is licensed ISC; sessions, windows, and panes are scriptable, which is why nearly every terminal agent workflow — including dedicated plugins like tmux-assistant-resurrect — treats tmux as the substrate for keeping coding agents alive across reboots and for watching several agent sessions at once. The project itself has no agent features, no plugin API beyond its configuration format (third-party TPM exists outside the repo), and no knowledge of AI tools; it is included in this census because practitioners overwhelmingly run harnesses inside it. Its role is foundational infrastructure rather than agent software.
