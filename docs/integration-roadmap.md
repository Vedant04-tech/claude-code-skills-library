# 🗺️ Agent Skills Integration Roadmap

> **Living document tracking upstream skill, plugin, and tool audits, verifications, overlap analyses, and phased integrations.**  
> **Last Updated:** October 13, 2026  
> **Target Environments:** Google Antigravity & Claude Code  

---

## 📊 Priority Matrix & Phased Plan

| Priority | Track | Focus Areas | Status |
|:---:|---|---|:---:|
| **P0** | **Inventory & Parity Audit** | Reconcile filesystem counts, fix `.agents/skills/` 30-skill discrepancy, update `skill-sources.md`. | **Installed & Verified ✓** |
| **P1** | **Core Discipline & Official Tooling** | `superpowers` (v6.1.1), official Anthropic skills (`skill-creator`, `mcp-builder`, `webapp-testing`), Vercel `frontend-design`, official `code-review` & `claude-code-setup`. | **Installed & Verified ✓** |
| **P2** | **Cognitive & Developer Productivity** | `Ponytail` (anti-overengineering), `Taste` (anti-slop UI), `Headroom` (context compression), `Find Skills` (discovery), `AnyDoc` (office document parser), `Graphify` (AST codebase graph), `Task Observer`. | **Installed & Verified ✓** |
| **P3** | **Security, Web & Advanced Memory** | `claude-mem` (progressive disclosure memory audit vs Supabase), `Agent Reach` (web research with TOS audit), `Strix` (sandboxed penetration testing), `PeterHdd/agent-skills` (senior engineering). | **Next Batch Planned** |

---

## 🔍 Upstream Sources Verification Registry

| Project | Canonical Upstream | Tool Type | Licence | OS / Prerequisites | Security & Privacy Risk | Overlap Analysis | Status |
|---|---|---|---|---|---|---|:---:|
| **Superpowers** | [`obra/superpowers`](https://github.com/obra/superpowers) | Agent Skills & Hooks | MIT | Cross-platform | Local-only execution; safe. | Core TDD/planning framework. 14 discipline skills active. | **Installed & Verified ✓** |
| **Official Anthropic Skills** | [`anthropics/skills`](https://github.com/anthropics/skills) | Agent Skills (`SKILL.md`) | MIT | Cross-platform, Python, Playwright | Safe; official Anthropic references. | `skill-creator`, `mcp-builder`, `webapp-testing`. | **Installed & Verified ✓** |
| **Official Code Review Plugin** | [`anthropics/claude-plugins-official`](https://github.com/anthropics/claude-plugins-official) | Claude Code Plugin | MIT | Claude Code CLI | Read-only code inspection. | Overlaps with `.claude/agents/code-reviewer.md`. Configured in `.claude/settings.json`. | **Configured ✓** |
| **Claude Code Setup** | [`anthropics/claude-plugins-official`](https://github.com/anthropics/claude-plugins-official) | Claude Code Plugin | MIT | Claude Code CLI | Inspects manifests in read-only mode. | Configured in `.claude/settings.json`. | **Configured ✓** |
| **Vercel Frontend Design** | [`anthropics/skills`](https://github.com/anthropics/skills) / [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills) | Agent Skill (`SKILL.md`) | Apache-2.0 / MIT | Cross-platform | Static prompt/rules guidance. | Distinctive non-slop design system guidelines. | **Installed & Verified ✓** |
| **Ponytail** | [`DietrichGebert/ponytail`](https://github.com/DietrichGebert/ponytail) | Agent Skills & Rules | MIT | Cross-platform | Static rules enforcement; zero risk. | Distinct capability: enforces YAGNI (5 skills installed). | **Installed & Verified ✓** |
| **Taste** | [`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill) | Agent Skill (`SKILL.md`) | MIT | Cross-platform | Static UI rules; safe. | Synergizes with `emil-design-eng` and `impeccable`. | **Installed & Verified ✓** |
| **Find Skills** | [`vercel-labs/skills`](https://github.com/vercel-labs/skills) | Agent Skill (`SKILL.md`) | MIT | Node.js (`npx skills`) | Queries public skill registries; safe. | Replaces manual skill hunting with automated lookup. | **Installed & Verified ✓** |
| **AnyDoc** | [`firecrawl/anydoc`](https://github.com/firecrawl/anydoc) | Agent Skill + Rust CLI | MIT | Node 20+ (`@firecrawl/anydoc`) | Local document parsing; local execution. | Converts Word, Excel, PPTX, EPUB, PDF into Markdown. | **Installed & Verified ✓** |
| **Headroom** | [`headroomlabs-ai/headroom`](https://github.com/headroomlabs-ai/headroom) | CLI / Proxy / MCP Server | Apache-2.0 | Node/Python | Local compression; caches tool outputs locally. | Configured in `.claude/settings.json` and docs. | **Configured ✓** |
| **Task Observer** | [`rebelytics/one-skill-to-rule-them-all`](https://github.com/rebelytics/one-skill-to-rule-them-all) | Agent Skill (`SKILL.md`) | MIT | Cross-platform | Local observation logging; safe. | Continuous observer capturing friction & drafting skills. | **Installed & Verified ✓** |
| **Graphify** | [`safishamsi/graphify`](https://github.com/safishamsi/graphify) | Agent Skill + CLI | MIT | Python / `uv`, Tree-sitter | Deterministic local AST parsing; safe. | Codebase structural map (`graph.json`, `graph.html`). | **Installed & Verified ✓** |
| **claude-mem** | [`thedotmack/claude-mem`](https://github.com/thedotmack/claude-mem) | Claude Code Plugin | MIT | Node.js, SQLite, Chroma | Stores observations locally. | Significant overlap with existing `vendor/claude-memory` (Supabase). Requires opt-in design. | **Planned (P3)** |
| **Agent Reach** | [`Panniantong/Agent-Reach`](https://github.com/Panniantong/Agent-Reach) | Agent Skill / Scraper | MIT | Python / Node | Scrapes public endpoints without API keys. Prone to rate limits & TOS violations. | Overlaps with Apify `scrape-leads` and `research` subagent. | **Planned (P3)** |
| **Strix** | [`usestrix/strix`](https://github.com/usestrix/strix) | Security Agent Skill / MCP | AGPL-3.0 / MIT | Docker / Kali Sandbox | Active vulnerability scanning; high impact if pointed at unauthorized targets. | Strictly sandboxed testing only. Non-destructive, user-owned targets only. | **Planned (P3)** |
| **Senior Engineering Skills** | [`PeterHdd/agent-skills`](https://github.com/PeterHdd/agent-skills) | Agent Skills (`SKILL.md`) | MIT | Cross-platform | Architectural decision rules; safe. | Complements `superpowers` with explicit senior developer playbooks. | **Planned (P3)** |

---

## ⚖️ Overlap Analysis

1. **Persistent Memory Conflict (`claude-mem` vs `vendor/claude-memory` vs `@modelcontextprotocol/server-memory`)**:
   - *Risk*: Running competing memory hooks creates duplicate token storage, conflicting recall context, and disk bloat.
   - *Strategy*: Keep `vendor/claude-memory` as the cloud-backed Supabase option, keep `@modelcontextprotocol/server-memory` as standard MCP, and provide `claude-mem` as a documented local-only alternative with clear mutually exclusive configuration toggles.
2. **Code Review Redundancy (`.claude/agents/code-reviewer.md` vs Superpowers `requesting-code-review` vs Official `code-review` Plugin)**:
   - *Analysis*: The local `.claude/agents/code-reviewer.md` subagent is lightweight, prompt-driven, and works inside Google Antigravity. The official plugin is designed specifically for Claude Code CLI PR reviews. Superpowers provides process discipline.
   - *Strategy*: Retain `.claude/agents/code-reviewer.md` for fast, cross-agent inline code review; document the official plugin for Claude Code CLI users.
3. **Frontend & Design System Overlap (`emil-design-eng` vs `impeccable` vs `Taste` vs `Vercel frontend-design`)**:
   - *Analysis*: `emil-design-eng` focuses on physics, springs, and motion. `impeccable` focuses on high-polish micro-details. `Taste` enforces anti-slop aesthetic parameters. `frontend-design` provides Vercel's production React conventions.
   - *Strategy*: These four reinforce each other without conflict; they cover distinct layers of the frontend stack.

---

## 🛡️ Security & Privacy Guardrails

1. **No External Secret Leaks**: All integration configs must use environment variables (`.env.example`) and never hardcode tokens.
2. **Safe Code Execution**: No arbitrary downloaded binary scripts executed without source auditing.
3. **Authorized Pentesting Only**: Strix security workflows must include mandatory pre-flight authorization guards.
4. **Local-First Processing**: AST parsing (`Graphify`), document conversions (`AnyDoc`), and token compression (`Headroom`) run locally without transmitting source code to third-party endpoints.
