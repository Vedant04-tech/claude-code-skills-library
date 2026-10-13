# 📦 Skills Sources & Inventory Tracking

> **Audited and reconciled status of all skills, upstream sources, and installation tracking.**  
> **Last Audited:** October 13, 2026  
> **Status:** Reconciled with 100% Cross-Agent Parity (`.claude/skills` ↔ `.agents/skills` ↔ `agent/skills`)

---

## 📊 Inventory Summary

| Category | Actual Filesystem Count | Upstream Origin / Maintainer | Cross-Agent Parity | Status |
|---|:---:|---|:---:|:---:|
| **Agency Business & Lead Gen** | **24** | Custom Production Agency Stack | 100 / 100 ✓ | Active |
| **Engineering Discipline (Superpowers)** | **14** | `obra/superpowers` (v6.1.1) | 100 / 100 ✓ | Active |
| **Senior Engineering Playbooks** | **9** | `PeterHdd/agent-skills` | 100 / 100 ✓ | Active |
| **Application Security & Pentesting (Strix)** | **9** | `usestrix/strix` (Apache-2.0) | 100 / 100 ✓ | Active |
| **Design Engineering & Motion Craft** | **16** | Emil Kowalski, Pbakaus, Nutlope, Anthropic, Leonxlnx | 100 / 100 ✓ | Active |
| **Anti-Overengineering (Ponytail)** | **5** | `DietrichGebert/ponytail` | 100 / 100 ✓ | Active |
| **Vercel & Next.js Performance** | **7** | `vercel-labs/agent-skills` | 100 / 100 ✓ | Active |
| **Persistent Memory Architecture** | **4** | `vendor/claude-memory` (Supabase Sync) | 100 / 100 ✓ | Active |
| **Systems Craftsmanship & Testing** | **5** | Swift 6 Concurrency, Prose Guidelines, Webapp Testing, MCP Builder | 100 / 100 ✓ | Active |
| **Document Parsing & Knowledge Graphs** | **3** | `firecrawl/anydoc`, `safishamsi/graphify`, PubMed | 100 / 100 ✓ | Active |
| **Meta-Tooling & Discovery** | **3** | `anthropics/skills`, `vercel-labs/skills`, `rebelytics` | 100 / 100 ✓ | Active |
| **Universal Web Retrieval (Agent Reach)** | **1** | `Panniantong/Agent-Reach` | 100 / 100 ✓ | Active |
| **Total Verified Active** | **100** | Multi-Source Curated Library | **100% Sync** | **Production Ready** |

---

## 🗂️ Active Skills Breakdown (100 Skills Verified)

### 1. Senior Engineering Playbooks (PeterHdd — 9 Skills)
- `engineering-senior-developer` — Cross-stack implementation, architecture tradeoffs, and delivery discipline
- `engineering-system-designer` — Distributed systems architecture, scalability, sharding, and ADRs
- `engineering-backend-architect` — Server-side architecture, sub-20ms DB indexing, API contracts, caching
- `engineering-devops-automator` — Terraform IaC, Docker containerization, CI/CD, and canary deployments
- `engineering-frontend-developer` — Modern React/Vue/Svelte UI, Core Web Vitals, accessibility, code-splitting
- `engineering-ml-engineer` — PyTorch, Transformers, LoRA/QLoRA fine-tuning, embeddings, and RAG pipelines
- `engineering-mobile-app-builder` — SwiftUI, Jetpack Compose, Flutter, React Native, and offline-first mobile
- `engineering-rapid-prototyper` — High-velocity MVP development, BaaS integration, and validation
- `engineering-security-engineer` — Threat modeling (STRIDE), OWASP remediation, and security architecture

### 2. Autonomous Application Security & Pentesting (Strix — 9 Skills)
- `penetration-testing-with-strix` — End-to-end autonomous penetration testing with exploit validation
- `find-security-vulnerabilities-in-code` — White-box code vulnerability review with working PoCs
- `owasp-top-10-testing` — Systematic OWASP Top 10:2025 exploitation and validation
- `api-security-testing` — OWASP API Security Top 10 testing for REST, GraphQL, and gRPC
- `application-security-testing` — Cross-stack application security assessment and ranked remediation plans
- `ci-security-scanning-with-strix` — Diff-scoped pre-merge security gates for GitHub Actions & CI/CD
- `fix-security-vulnerabilities-with-strix` — Root-cause vulnerability patching with verification re-scans
- `managed-pentesting-with-strix` — Managed cloud pentesting via app.strix.ai CLI/API
- `web-app-penetration-testing` — Black-box web application testing for live URLs and staging environments

### 3. Universal Web Retrieval & Research (Agent Reach — 1 Skill)
- `agent-reach` — Internet content retrieval and multi-platform research across 15+ services (GitHub, Reddit, Twitter, YouTube, Jina Reader, Exa, RSS, V2EX)

### 4. Software Engineering Discipline (Superpowers v6.1.1 — 14 Skills)
- `brainstorming`, `dispatching-parallel-agents`, `executing-plans`, `finishing-a-development-branch`
- `receiving-code-review`, `requesting-code-review`, `subagent-driven-development`, `systematic-debugging`
- `test-driven-development`, `using-git-worktrees`, `using-superpowers`, `verification-before-completion`
- `writing-plans`, `writing-skills`

### 5. Pragmatic Anti-Overengineering (Ponytail — 5 Skills)
- `ponytail` — Decision ladder for simplest solution and YAGNI adherence
- `ponytail-review` — Code review focused on stripping excess logic
- `ponytail-audit` — Repository-wide sweep for over-engineering
- `ponytail-debt` — Ledger for deferred shortcuts
- `ponytail-gain` — Scoreboard tracking code reduction

### 6. Design Engineering, Motion & Craft (16 Skills)
- `animate`, `animate-expo`, `animation-vocabulary`, `apple-design`, `ask-sonner`
- `design-taste-frontend` (Taste Skill), `emil-design-eng`, `find-animation-opportunities`
- `frontend-design` (Anthropic), `hallmark`, `impeccable`, `improve-animations`
- `pick-ui-library`, `prototype`, `review-animations`, `design-website`

### 7. Document Parsing & Knowledge Systems (3 Skills)
- `convert-documents-to-markdown` (AnyDoc by Firecrawl) — Converts DOCX, PPTX, XLSX, PDF, EPUB to Markdown
- `graphify` (Graphify) — Codebase knowledge graph via Tree-sitter AST
- `literature-research` — Scientific paper review via PubMed/arXiv

### 8. Meta-Tooling, Discovery & Evolution (3 Skills)
- `skill-creator` (Anthropic) — Author, evaluate, and benchmark agent skills
- `find-skills` (Vercel Labs) — On-demand skill registry search
- `task-observer` (One Skill / Rebelytics) — Real-time friction capture and skill drafting

### 9. Agency Automation & Lead Generation (24 Skills)
- `add-webhook`, `casualize-names`, `classify-leads`, `create-proposal`, `cross-niche-outliers`
- `generate-report`, `gmail-inbox`, `gmail-label`, `gmaps-leads`, `instantly-autoreply`
- `instantly-campaigns`, `local-server`, `modal-deploy`, `onboarding-kickoff`, `pan-3d-transition`
- `recreate-thumbnails`, `scrape-leads`, `skool-monitor`, `skool-rag`, `title-variants`
- `upwork-apply`, `video-edit`, `welcome-email`, `youtube-outliers`

### 10. Vercel, Next.js & Performance (7 Skills)
- `deploy-to-vercel`, `vercel-cli-with-tokens`, `vercel-composition-patterns`, `vercel-optimize`
- `vercel-react-best-practices`, `vercel-react-native-skills`, `vercel-react-view-transitions`
- `web-design-guidelines`

### 11. Systems Craftsmanship & Testing (5 Skills)
- `mcp-builder` — FastMCP & Node MCP SDK development guide
- `webapp-testing` — Playwright testing harness and server lifecycle runner
- `write-swift` — Modern Swift 6 strict concurrency
- `writing-guidelines` — Technical documentation prose review

### 12. Persistent Memory System (4 Skills)
- `memory-capture`, `memory-cloud-recall`, `memory-session-end`, `memory-session-start`

---

## 🔄 Phased Roadmap Tracking

See [docs/integration-roadmap.md](integration-roadmap.md) for complete roadmap delivery and lifecycle audits.
