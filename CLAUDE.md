# Agent Instructions

> This file is mirrored across CLAUDE.md, AGENTS.md, and GEMINI.md so the same instructions load in any AI environment.

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+ and npm
- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed
- [Modal](https://modal.com/) account (for cloud webhooks)
- Google Cloud project with OAuth credentials (for Gmail/Sheets skills)

### Setup

1. **Clone and install dependencies:**
   ```bash
   cd claude-code-skills-library
   npm install
   ```

2. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and fill in your API keys for each service you plan to use. Not all keys are required — only fill in what you need:
   - `ANTHROPIC_API_KEY` — Required. Get from [console.anthropic.com](https://console.anthropic.com/)
   - `APIFY_API_TOKEN` — For lead scraping skills. Get from [apify.com](https://apify.com/)
   - `INSTANTLY_API_KEY` — For cold email campaigns. Get from [instantly.ai](https://instantly.ai/)
   - `PANDADOC_API_KEY` — For proposal generation. Get from [pandadoc.com](https://pandadoc.com/)
   - `OPENAI_API_KEY` — For embeddings in RAG pipeline. Get from [platform.openai.com](https://platform.openai.com/)
   - `PINECONE_API_KEY` — For vector search in RAG. Get from [pinecone.io](https://pinecone.io/)
   - See `.env.example` for the full list.

3. **Configure Gmail (optional):**
   ```bash
   cp gmail_accounts.json.example gmail_accounts.json
   ```
   - Create OAuth credentials in [Google Cloud Console](https://console.cloud.google.com/) (Desktop app type)
   - Download as `credentials.json`
   - Edit `gmail_accounts.json` with your email addresses and token file paths
   - Run any Gmail skill once to complete the OAuth flow and generate token files

4. **Deploy to Modal (optional):**
   ```bash
   modal deploy execution/modal_webhook.py
   ```
   Update the webhook URLs in this file and SKILL.md files with your Modal username.

5. **Run Claude Code:**
   ```bash
   claude
   ```
   Skills auto-activate based on your requests. Try: "Scrape leads for marketing agencies in New York" or "Label my Gmail inbox".

---

You operate using Claude Code Skills - bundled capabilities that combine instructions with deterministic scripts. This architecture separates probabilistic decision-making from deterministic execution to maximize reliability.

## The Skills Architecture

**Layer 1: Skills (Intent + Execution bundled)**
- Live in `.claude/skills/`
- Each Skill = `SKILL.md` instructions + `scripts/` folder
- Claude auto-discovers and invokes based on task context
- Self-contained: each Skill has everything it needs

**Layer 2: Orchestration (Decision making)**
- This is you. Your job: intelligent routing.
- Read SKILL.md, run bundled scripts in the right order
- Handle errors, ask for clarification, update Skills with learnings
- You're the glue between intent and execution

**Layer 3: Shared Utilities**
- Common scripts in `execution/` (sheets, auth, webhooks)
- Infrastructure code (Modal webhooks, local server)
- Used across multiple Skills when needed

**Why this works:** if you do everything yourself, errors compound. 90% accuracy per step = 59% success over 5 steps. The solution is push complexity into deterministic code. That way you just focus on decision-making.

## Available Skills (100 total)

> Full directory with triggers and compatibility: [`docs/skill-catalog.md`](docs/skill-catalog.md)  
> All 100 skills are mirrored across `.claude/skills/`, `.agents/skills/`, and `agent/skills/`.

### 1. Senior Engineering Playbooks (PeterHdd — 9)
- `engineering-senior-developer` - Senior implementation judgment, architecture tradeoffs, review checklists
- `engineering-system-designer` - Distributed architecture, scalability, sharding, and ADR creation
- `engineering-backend-architect` - Schema design, sub-20ms DB indexing, API contracts, caching
- `engineering-devops-automator` - Terraform IaC, Docker containerization, CI/CD, canary deployments
- `engineering-frontend-developer` - Modern React/Vue/Svelte UI, Core Web Vitals, accessibility
- `engineering-ml-engineer` - PyTorch, HuggingFace, LoRA/QLoRA, embeddings, RAG pipelines
- `engineering-mobile-app-builder` - SwiftUI, Jetpack Compose, Flutter, React Native, offline-first
- `engineering-rapid-prototyper` - High-speed MVP prototyping, BaaS integration, hypothesis testing
- `engineering-security-engineer` - Threat modeling (STRIDE), OWASP remediation, security headers

### 2. Autonomous Application Security & Pentesting (Strix — 9)
- `penetration-testing-with-strix` - End-to-end autonomous pentesting with exploit validation (Docker sandboxed)
- `find-security-vulnerabilities-in-code` - White-box code vulnerability review with working proof-of-concepts
- `owasp-top-10-testing` - Systematic OWASP Top 10:2025 assessment and validation
- `api-security-testing` - OWASP API Security Top 10 testing for REST, GraphQL, and gRPC
- `application-security-testing` - Cross-stack AppSec assessment and ranked remediation plans
- `ci-security-scanning-with-strix` - Diff-scoped pre-merge security gates for CI/CD pipelines
- `fix-security-vulnerabilities-with-strix` - Root-cause vulnerability patching with verification re-scans
- `managed-pentesting-with-strix` - Managed cloud pentesting via app.strix.ai CLI/API
- `web-app-penetration-testing` - Black-box web application testing for live URLs and staging environments

### 3. Universal Web Retrieval & Research (Agent Reach & Literature — 2)
- `agent-reach` - Universal internet content router across 15+ services (GitHub, Reddit, Twitter, YouTube, Exa, V2EX)
- `literature-research` - Search academic databases (PubMed, arXiv) and synthesize literature reviews

### 4. Software Engineering Discipline (Superpowers v6.1.1 — 14)
- `test-driven-development` - Red-green-refactor cycle before writing production code
- `systematic-debugging` - Root-cause tracing, test pressure, defense-in-depth bug isolation
- `writing-plans` / `executing-plans` - Bite-sized implementation plans with checkpoints
- `subagent-driven-development` - Independent implementer and reviewer subagents
- `verification-before-completion` - Strict verification commands before claiming success
- `brainstorming` / `dispatching-parallel-agents` / `finishing-a-development-branch`
- `receiving-code-review` / `requesting-code-review` / `using-git-worktrees` / `using-superpowers` / `writing-skills`

### 5. Pragmatic Anti-Overengineering (Ponytail — 5)
- `ponytail` - Decision ladder for simplest standard library solution and YAGNI adherence
- `ponytail-review` - Code review focused on stripping unneeded abstractions and dependencies
- `ponytail-audit` - Repository-wide sweep for over-engineering
- `ponytail-debt` / `ponytail-gain` - Tech debt ledger and code reduction scoreboard

### 6. Design Engineering, Motion & Craft (16)
- `emil-design-eng` - Core design-engineering doctrine & tactile UI principles
- `design-taste-frontend` - Strict anti-slop rules, design intensity dials, OKLCH palettes
- `frontend-design` - Non-templated typography, layouts, and distinctive frontend direction
- `apple-design` - iOS/macOS human interface guidelines & spring physics
- `web-design-guidelines` - Design checklists for accessibility, contrast, and layout
- `impeccable` / `hallmark` - High-polish micro-details and UI signature standards
- `prototype` / `pick-ui-library` / `design-website` - Interactive UI prototyping and library selection
- `animate` / `animate-expo` / `animation-vocabulary` - Physics-based motion and easing curves
- `find-animation-opportunities` / `improve-animations` / `review-animations` - Animation auditing

### 7. Document Parsing & Knowledge Systems (2)
- `convert-documents-to-markdown` (AnyDoc) - Converts DOCX, PPTX, XLSX, PDF, EPUB to Markdown
- `graphify` (Graphify) - Codebase knowledge graph via Tree-sitter AST and interactive visualizer

### 8. Meta-Tooling, Discovery & Evolution (3)
- `skill-creator` (Anthropic) - Author, evaluate, and benchmark agent skills
- `find-skills` (Vercel Labs) - On-demand skill registry search
- `task-observer` (One Skill) - Real-time friction capture and skill drafting

### 9. Agency Automation & Lead Generation (24)
- `scrape-leads` / `gmaps-leads` / `classify-leads` / `casualize-names` - B2B lead generation
- `instantly-campaigns` / `instantly-autoreply` / `welcome-email` - Cold outreach automation
- `gmail-inbox` / `gmail-label` - Multi-account unified Gmail triage
- `create-proposal` / `upwork-apply` / `onboarding-kickoff` - Sales, bidding, and onboarding
- `video-edit` / `pan-3d-transition` / `recreate-thumbnails` - Programmatic video engineering
- `cross-niche-outliers` / `youtube-outliers` / `title-variants` - YouTube content intelligence
- `skool-monitor` / `skool-rag` - Community monitoring and semantic knowledge search
- `generate-report` / `add-webhook` / `modal-deploy` / `local-server` - Reporting & infrastructure

### 10. Vercel, React & Performance (7)
- `vercel-react-best-practices` / `vercel-composition-patterns` / `vercel-optimize`
- `vercel-cli-with-tokens` / `deploy-to-vercel` / `vercel-react-view-transitions` / `vercel-react-native-skills`

### 11. Systems Craftsmanship & Testing (4)
- `mcp-builder` - FastMCP & Node MCP SDK development guide
- `webapp-testing` - Playwright testing harness and server lifecycle runner
- `write-swift` - Modern Swift 6 strict concurrency implementation
- `writing-guidelines` - Technical documentation prose review

### 12. Persistent Memory System (4)
- `memory-capture` / `memory-cloud-recall` / `memory-session-end` / `memory-session-start`
  *(Opt-in Supabase memory via `vendor/claude-memory` or local SQLite/Chroma via `claude-mem`)*

## Subagents

Subagents are lightweight agents (Sonnet 4.5) with self-contained contexts, defined in `.claude/agents/`. They're cheaper, unbiased (no parent context leakage), and keep the parent context clean.

### Available Subagents
- `code-reviewer` - Unbiased code review with zero context. Returns issues by severity with a PASS/FAIL verdict.
- `research` - Deep research via web search, file reads, and codebase exploration. Returns concise sourced findings.
- `qa` - Generates tests for a code snippet, runs them, and reports pass/fail results.
- `email-classifier` - Classifies Gmail emails into Action Required, Waiting On, Reference.

### Design & Build Workflow

When building or modifying any non-trivial code (scripts, features, refactors), follow this loop:

1. **Write/edit the code** — Make your changes.
2. **Code Review** — Spawn `code-reviewer` subagent with the changed file(s). It reports issues back — it does NOT fix anything itself.
3. **QA** — Spawn `qa` subagent with the code. It generates tests, runs them, and reports results back — it does NOT fix anything itself.
4. **Fix** — The parent agent (you) reads the review and QA reports and applies all fixes.
5. **Ship** — Only after review passes and tests pass.

**Important:** Subagents are read-only reporters. All code changes happen in the parent agent.

For research-heavy tasks, spawn `research` subagent first to gather context without polluting the main conversation.

**Parallel execution:** When reviewing + QA'ing independent files, spawn both subagents in parallel using `run_in_background: true`.

## Operating Principles

**1. Skills auto-activate**
Claude picks the right Skill based on your request. Each Skill's description tells Claude when to use it.

**2. Scripts are bundled**
Each Skill has its own `scripts/` folder. Run scripts from there:
```bash
python3 .claude/skills/scrape-leads/scripts/scrape_apify.py ...
```

**3. Self-anneal when things break**
- Read error message and stack trace
- Fix the script and test it again
- Update SKILL.md with what you learned
- System is now stronger

**4. Update Skills as you learn**
Skills are living documents. When you discover API constraints, better approaches, or edge cases—update the SKILL.md. But don't create new Skills without asking.

## Self-annealing loop

Errors are learning opportunities. When something breaks:
1. Fix the script
2. Test it
3. Update SKILL.md with new flow
4. System is now stronger

## File Organization

**Deliverables vs Intermediates:**
- **Deliverables**: Google Sheets, Google Slides, or other cloud-based outputs
- **Intermediates**: Temporary files needed during processing

**Directory structure:**
- `.claude/skills/` - Skills (SKILL.md + scripts/)
- `.claude/agents/` - Subagents (code-reviewer, qa, research, email-classifier)
- `prompts/` - Workflow prompts and templates
- `.tmp/` - Intermediate files (never commit)
- `execution/` - Shared utilities and infrastructure
- `vendor/` - Third-party repos (superpowers, claude-memory, awesome-claude-code for reference)
- `.env` - Environment variables and API keys
- `credentials.json`, `token.json` - Google OAuth credentials

**Key principle:** Local files are only for processing. Deliverables live in cloud services where the user can access them.

## Cloud Webhooks (Modal)

The system supports event-driven execution via Modal webhooks.

**Deploy:** `modal deploy execution/modal_webhook.py`

**Endpoints** (replace `your-modal-username` with your Modal username):
- `https://your-modal-username--claude-orchestrator-list-webhooks.modal.run` - List webhooks
- `https://your-modal-username--claude-orchestrator-directive.modal.run?slug={slug}` - Execute
- `https://your-modal-username--claude-orchestrator-test-email.modal.run` - Test email

**Available tools for webhooks:** `send_email`, `read_sheet`, `update_sheet`

## Summary

You work with Skills that bundle intent (SKILL.md) with execution (scripts/). Read instructions, make decisions, run scripts, handle errors, continuously improve the system.

Be pragmatic. Be reliable. Self-anneal.
