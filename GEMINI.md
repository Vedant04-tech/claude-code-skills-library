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

## Available Skills (28 total)

### Lead Generation & Enrichment
- `scrape-leads` - Scrape leads via Apify with verification
- `gmaps-leads` - Google Maps lead scraping with deep enrichment
- `classify-leads` - LLM-based lead classification
- `casualize-names` - Convert formal names to casual versions

### Email & Campaigns
- `instantly-campaigns` - Create cold email campaigns in Instantly
- `instantly-autoreply` - Auto-reply to incoming emails
- `welcome-email` - Send welcome sequence to new clients
- `gmail-inbox` - Manage emails across Gmail accounts
- `gmail-label` - Manage Gmail labels and filtering

### Sales & Proposals
- `create-proposal` - Generate PandaDoc proposals
- `upwork-apply` - Scrape Upwork and generate proposals

### Content & Video
- `video-edit` - Remove silences, add 3D transitions
- `pan-3d-transition` - Create 3D swivel effects
- `recreate-thumbnails` - Face-swap YouTube thumbnails
- `cross-niche-outliers` - Find viral videos from adjacent niches
- `youtube-outliers` - Monitor your niche for outliers
- `title-variants` - Generate YouTube title variations

### Community & Research
- `skool-monitor` - Monitor and interact with Skool communities
- `skool-rag` - Query Skool content via RAG pipeline
- `literature-research` - Search academic databases

### Web & Design
- `design-website` - Generate custom websites with Claude

### Reporting & Analytics
- `generate-report` - Create multi-page PDF reports with charts

### Client Onboarding
- `onboarding-kickoff` - Full post-kickoff automation

### Infrastructure (3)
- `add-webhook` - Add new Modal webhooks
- `modal-deploy` - Deploy to Modal cloud
- `local-server` - Run orchestrator locally

### Design & Craft Engineering (Emil Kowalski) (12)
- `emil-design-eng` - Core design-engineering doctrine & tactile UI principles
- `animate` - Motion craft, custom timing curves & property transitions
- `animate-expo` - React Native / Expo motion animations
- `animation-vocabulary` - Reverse lookup from descriptions to technical terms
- `apple-design` - iOS/macOS human interface guidelines & spring physics
- `ask-sonner` - Toast & notification pattern best practices
- `find-animation-opportunities` - Audit UI for meaningful motion placement
- `improve-animations` - Motion audit & prioritized refinement plans
- `pick-ui-library` - Selection matrix for UI frameworks & component sets
- `prototype` - Fast interactive prototype generation
- `review-animations` - Adversarial Motion Craft review against high standards
- `write-swift` - Idiomatic Swift & SwiftUI layout implementation

### Impeccable Design System (pbakaus/impeccable) (1)
- `impeccable` - Anti-pattern design linter, /polish & /audit design commands

### Hallmark (nutlope/hallmark) (1)
- `hallmark` - Watermark & hallmark generator for UI components

## Memory Skills

Persistent memory system (requires `vendor/claude-memory/install.sh` to be run and Supabase credentials configured):
- `memory-capture` - Capture important decisions and learnings
- `memory-cloud-recall` - Recall from cloud memory store
- `memory-session-end` - Save session state at end
- `memory-session-start` - Load session state at start

See `.claude/skills/README.md` for full skill descriptions and install notes.

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
- `.claude/agents/` - Subagents
- `.tmp/` - Intermediate files (never commit)
- `execution/` - Shared utilities and infrastructure
- `vendor/` - Third-party skill repositories (superpowers, claude-memory, awesome-claude-code)
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
