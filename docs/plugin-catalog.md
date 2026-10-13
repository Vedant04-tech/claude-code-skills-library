# 🔌 Plugins & MCP Servers Catalog

> **Reference catalog for configured Model Context Protocol (MCP) servers, official Claude Code plugins, and registered marketplaces.**  
> **Last Audited:** October 13, 2026  

---

## 🛠️ Bundled Model Context Protocol (MCP) Servers

Configured in [`.mcp.json`](../.mcp.json) and [`.claude/settings.json`](../.claude/settings.json):

| MCP Server | Package / Command | Primary Functionality | Required Credentials | Status |
|---|---|---|---|:---:|
| **`context7`** | `@upstash/context7-mcp@latest` | Fast semantic vector search and external retrieval | None (local mode) / Upstash token | Active ✓ |
| **`playwright`** | `@playwright/mcp@latest` | Headless browser execution, UI verification, DOM inspection | None (local Playwright) | Active ✓ |
| **`filesystem`** | `@modelcontextprotocol/server-filesystem` | Scoped, permission-controlled filesystem read/write | None | Active ✓ |
| **`memory`** | `@modelcontextprotocol/server-memory` | Local entity-relationship knowledge graph memory | None | Active ✓ |
| **`fetch`** | `mcp-fetch-server` | URL content fetching and Markdown conversion | None | Active ✓ |
| **`headroom`** | `headroom mcp serve` | Local context compression, CCR, and cache alignment | `pip install "headroom-ai[mcp]"` | Optional / Ready |

---

## 🧩 Claude Code Plugins Directory

Registered in [`.claude/settings.json`](../.claude/settings.json):

### 1. `code-review@claude-plugins-official`
- **Origin:** Official Anthropic (`anthropics/claude-plugins-official`)
- **Installation Command:**
  ```bash
  /plugin install code-review@claude-plugins-official
  ```
- **Capabilities:**
  - Parallelized multi-agent pull request and diff review.
  - Confidence scoring filter (suppresses low-confidence false positives).
  - Enforces repository-specific rules from `CLAUDE.md`.

### 2. `claude-code-setup@claude-plugins-official`
- **Origin:** Official Anthropic (`anthropics/claude-plugins-official`)
- **Installation Command:**
  ```bash
  /plugin install claude-code-setup@claude-plugins-official
  ```
- **Capabilities:**
  - Inspects project dependencies and codebase structure in read-only mode.
  - Recommends tailored skills, subagents, and MCP configurations.

### 3. `commit-commands@claude-plugins-official`
- **Origin:** Official Anthropic (`anthropics/claude-plugins-official`)
- **Installation Command:**
  ```bash
  /plugin install commit-commands@claude-plugins-official
  ```
- **Capabilities:**
  - Generates conventional semantic git commit messages based on staged diffs.

---

## 🌐 Registered Plugin Marketplaces

| Marketplace Key | Upstream Registry URL | Description | Enabled |
|---|---|---|:---:|
| **`claude-plugins-official`** | `https://registry.anthropic.com/anthropics/claude-plugins-official` | Official Anthropic plugins repository | `true` |
| **`anthropics`** | `https://registry.anthropic.com/anthropics/skills` | Official Anthropic skills collection | `true` |
| **`superpowers`** | `https://registry.anthropic.com/obra/superpowers-marketplace` | Superpowers engineering discipline plugin | `true` |
| **`vercel`** | `https://registry.anthropic.com/vercel-labs/agent-skills` | Vercel frontend design and React skills | `false` (installed locally) |
| **`wshobson`** | `https://registry.anthropic.com/wshobson/agents` | Large developer and DevOps skills library | `false` (on-demand) |
| **`alirezarezvani`** | `https://registry.anthropic.com/alirezarezvani/claude-skills` | Machine learning and MLOps skills library | `false` (on-demand) |
