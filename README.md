# ⚡ Claude Code Skills Library & Cross-Agent Engineering Toolkit

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-6366f1?style=for-the-badge&logo=anthropic)](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)
[![Antigravity](https://img.shields.io/badge/Antigravity-100%25%20Parity-4285f4?style=for-the-badge)](https://github.com/Vedant04-tech/claude-code-skills-library)
[![Skills Count](https://img.shields.io/badge/Production%20Skills-81%20Verified-10b981?style=for-the-badge)](docs/skill-catalog.md)
[![Subagents](https://img.shields.io/badge/Specialized%20Subagents-4-f59e0b?style=for-the-badge)](https://github.com/Vedant04-tech/claude-code-skills-library)
[![MCP Enabled](https://img.shields.io/badge/MCP%20Servers-5%20Bundled-8b5cf6?style=for-the-badge)](docs/plugin-catalog.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

> **A curated, battle-tested agency automation and engineering skills library with 100% parity across Claude Code, Google Antigravity, Cursor, and Codex.**

This repository serves as a turnkey, production-ready engineering toolkit. Built and maintained for **Claude Code**, **Google Antigravity**, and **Agentic IDEs**, it packages **81 verified skills**, 4 high-focus subagents, 3 turnkey pipeline blueprints, 5 Model Context Protocol (MCP) servers, official Anthropic meta-skills, Jesse Vincent's Superpowers v6.1.1 discipline framework, Ponytail's anti-overengineering suite, AnyDoc document conversion, and Graphify's AST knowledge graph.

---

## 📚 Core Documentation Indexes

- 📖 **[Skills Catalog (81 Skills)](docs/skill-catalog.md)** — Exhaustive directory of all 81 skills with trigger phrases, upstream sources, and cross-agent compatibility.
- 🔌 **[Plugins & MCP Servers Catalog](docs/plugin-catalog.md)** — Pre-configured MCP servers (`context7`, `playwright`, `filesystem`, `memory`, `fetch`, `headroom`), official Claude plugins (`code-review`, `claude-code-setup`), and marketplace registries.
- 🗺️ **[Integration Roadmap](docs/integration-roadmap.md)** — Living tracker for phased upstream integrations (P0, P1, and P2 verified; P3 scheduled).
- 🛡️ **[Security Review & Safeguards](docs/security-review.md)** — Application testing policies (Strix), web retrieval constraints, and memory privacy boundaries.
- 📦 **[Skills Sources Tracking](docs/skill-sources.md)** — Category breakdown and upstream origin audits.

---

## 📑 Table of Contents

- [✨ Key Highlights](#-key-highlights)
- [📂 Repository Architecture](#-repository-architecture)
- [🚀 Quick Start](#-quick-start)
- [🧠 Active Skills Directory (81 Verified)](#-active-skills-directory-81-verified)
  - [1. Pragmatic Anti-Overengineering (Ponytail)](#1-pragmatic-anti-overengineering-ponytail)
  - [2. Software Engineering Discipline (Superpowers v6.1.1)](#2-software-engineering-discipline-superpowers-v611)
  - [3. Codebase Knowledge Graph & Document Parsing](#3-codebase-knowledge-graph--document-parsing)
  - [4. Meta-Tooling, Discovery & Evolution](#4-meta-tooling-discovery--evolution)
  - [5. Design Engineering, Animation & Craft UI](#5-design-engineering-animation--craft-ui)
  - [6. B2B Lead Generation & Market Intelligence](#6-b2b-lead-generation--market-intelligence)
  - [7. Cold Outreach & Email Automation](#7-cold-outreach--email-automation)
  - [8. Sales, Proposals & Client Onboarding](#8-sales-proposals--client-onboarding)
  - [9. Video Engineering & Content Intelligence](#9-video-engineering--content-intelligence)
  - [10. Community Intelligence & Research](#10-community-intelligence--research)
  - [11. Vercel, Next.js & Performance Optimization](#11-vercel-nextjs--performance-optimization)
  - [12. Persistent Memory Architecture](#12-persistent-memory-architecture)
- [🤖 Autonomous Subagents](#-autonomous-subagents)
- [📋 Turnkey Workflow Blueprints](#-turnkey-workflow-blueprints)
- [🔌 MCP Servers Suite](#-mcp-servers-suite)
- [🛡️ Key Principles & Self-Annealing](#-key-principles--self-annealing)
- [📄 License](#-license)

---

## ✨ Key Highlights

- **⚡ 100% Cross-Agent Parity**: Skills are mirrored across `.claude/skills/`, `.agents/skills/`, and `agent/skills/`, ensuring that **Google Antigravity**, **Claude Code**, **Cursor**, and **Codex** discover all 81 skills natively.
- **🧘 Pragmatic Anti-Overengineering**: Integrated **Ponytail** decision ladder ("The best code is the code you never wrote") to cut token waste and eliminate unneeded dependencies.
- **📄 Universal Document Parsing**: Integrated **AnyDoc** (`convert-documents-to-markdown`) to convert Word, Excel, PowerPoint, EPUB, and PDFs directly into LLM-ready Markdown.
- **🕸️ Local Codebase Knowledge Graph**: Integrated **Graphify** for deterministic Tree-sitter AST structural mapping, producing interactive HTML graphs and GraphRAG JSON without external API dependencies.
- **🛡️ Battle-Tested Engineering Discipline**: Includes Jesse Vincent's **Superpowers (v6.1.1)** suite (`test-driven-development`, `systematic-debugging`, `writing-plans`, `subagent-driven-development`, and `verification-before-completion`).
- **🧰 Official Anthropic Meta-Tooling**: Integrated `skill-creator`, `mcp-builder`, and `webapp-testing` with Playwright lifecycle testing.
- **🎨 Elite Design Engineering Craft Bar**: Built with Emil Kowalski motion principles, Apple HIG, View Transitions API, `impeccable`, and Anthropic `frontend-design` & Leon Lin's `design-taste-frontend`.
- **💼 Full-Cycle Agency Stack**: Scrape leads from Google Maps and Apify, qualify ICP with LLMs, orchestrate multi-variant Instantly cold campaigns, and close deals with automated PandaDoc proposals.
- **🧠 Cross-Session Long-Term Memory**: 4 memory skills backed by local SQLite vector storage and Supabase cloud synchronization.

---

## 📂 Repository Architecture

```
.
├── .claude/
│   ├── skills/                  # 81 active agent skills (auto-discovered by Claude Code)
│   ├── agents/                  # 4 specialized subagents
│   │   ├── code-reviewer.md     # Zero-context code review
│   │   ├── qa.md                # Edge-case test generation & execution
│   │   ├── research.md          # Multi-source deep research
│   │   └── email-classifier.md  # High-volume Gmail triage
│   └── settings.json            # Plugin marketplace & MCP server config
├── .agents/skills/              # 81 skills mirrored for Google Antigravity & Agent standards
├── agent/skills/                # 81 skills mirrored for CLI and alternative runners
├── prompts/                     # 3 production workflow blueprints
│   ├── gmaps_lead_pipeline_builder.md
│   ├── upwork_pipeline_builder.md
│   └── instantly_campaign_creator.md
├── docs/                        # Complete technical documentation
│   ├── skill-catalog.md         # 81-skill directory with trigger phrases
│   ├── plugin-catalog.md        # MCP servers and Claude plugins
│   ├── integration-roadmap.md   # Phased rollout and upstream tracking
│   ├── security-review.md       # Guardrails, Strix policy, and data hygiene
│   └── skill-sources.md         # Upstream inventory tracking
├── vendor/                      # Reference repositories & upstream frameworks
│   ├── superpowers/             # obra/superpowers (v6.1.1)
│   ├── claude-memory/           # Persistent vector memory system (Supabase sync)
│   └── awesome-claude-code/     # Curated community skill references
├── .mcp.json                    # Bundled Model Context Protocol configurations
├── CLAUDE.md                    # Workspace instruction rules for Claude Code
├── AGENTS.md                    # Open agent standards specification
├── GEMINI.md                    # Google Gemini / Antigravity workspace rules
├── package.json                 # Project configuration & dependencies
└── LICENSE                      # MIT Open Source License
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Vedant04-tech/claude-code-skills-library.git
cd claude-code-skills-library
npm install
```

### 2. Launch in Google Antigravity or Claude Code
- **In Google Antigravity**: All 81 skills in `.agents/skills/` are loaded automatically.
- **In Claude Code**:
  ```bash
  claude
  ```
  Claude Code auto-discovers all 81 skills in `.claude/skills/`.

### 3. Try Sample Prompts
```bash
# Anti-Overengineering (Ponytail)
> "Use ponytail to implement this feature with the simplest possible standard library code"

# Document Conversion (AnyDoc)
> "Convert client_brief.docx and financials.xlsx to markdown"

# Codebase Knowledge Graph (Graphify)
> "Run /graphify to generate an interactive structural graph of this repository"

# Engineering Discipline (Superpowers)
> "Use test-driven-development to implement the authentication token refresh logic"

# Meta-Skill (Anthropic)
> "Use skill-creator to design a new agent skill for Stripe webhook handling"
```

---

## 🧠 Active Skills Directory (81 Verified)

*(See [`docs/skill-catalog.md`](docs/skill-catalog.md) for the full 81-skill index).*

### 1. Pragmatic Anti-Overengineering (Ponytail)
| Skill | Trigger / Use Case | Description |
|---|---|---|
| [`ponytail`](.claude/skills/ponytail) | *"Be lazy", "simplest solution", "yagni"* | Enforces decision ladder: smallest change that solves the task, zero unnecessary packages. |
| [`ponytail-review`](.claude/skills/ponytail-review) | *"Review for bloat"* | Strips over-engineered abstractions and redundant helper classes. |
| [`ponytail-audit`](.claude/skills/ponytail-audit) | *"Audit codebase bloat"* | Sweeps repository for over-engineering and suggests code reductions. |
| [`ponytail-debt`](.claude/skills/ponytail-debt) | *"Harvest tech debt"* | Collects deferred shortcut comments into an actionable ledger. |
| [`ponytail-gain`](.claude/skills/ponytail-gain) | *"Check code reduction"* | Displays a scoreboard tracking lines of code saved and speed improvements. |

### 2. Software Engineering Discipline (Superpowers v6.1.1)
| Skill | Trigger / Use Case | Description |
|---|---|---|
| [`test-driven-development`](.claude/skills/test-driven-development) | *"Write tests first"* | Enforces strict TDD discipline: red, green, refactor cycle before writing code. |
| [`systematic-debugging`](.claude/skills/systematic-debugging) | *"Debug this failure"* | Root-cause tracing, test pressure, and defense-in-depth bug isolation. |
| [`writing-plans`](.claude/skills/writing-plans) | *"Plan this feature"* | Creates bite-sized, reviewable implementation plans before touching code. |
| [`executing-plans`](.claude/skills/executing-plans) | *"Execute the plan"* | Executes plans step-by-step with checkpoints and verification gates. |
| [`subagent-driven-development`](.claude/skills/subagent-driven-development) | *"Dispatch subagents"* | Dispatches isolated implementer and reviewer subagents for tasks. |
| [`verification-before-completion`](.claude/skills/verification-before-completion) | *"Verify before PR"* | Requires running verification commands and confirming evidence before claims. |
| [`brainstorming`](.claude/skills/brainstorming) | *"Brainstorm architecture"* | Explores user intent, requirements, and design before implementation. |
| [`dispatching-parallel-agents`](.claude/skills/dispatching-parallel-agents) | *"Run parallel tasks"* | Dispatches 2+ independent tasks without shared state. |
| [`finishing-a-development-branch`](.claude/skills/finishing-a-development-branch) | *"Complete feature branch"* | Guides branch integration, PR creation, and worktree cleanup. |
| [`receiving-code-review`](.claude/skills/receiving-code-review) | *"Process PR review"* | Rigorous verification of review feedback; avoids performative agreement. |
| [`requesting-code-review`](.claude/skills/requesting-code-review) | *"Request review"* | Validates work against requirements before merge. |
| [`using-git-worktrees`](.claude/skills/using-git-worktrees) | *"Isolate workspace"* | Sets up clean git worktrees for isolated task execution. |
| [`using-superpowers`](.claude/skills/using-superpowers) | *"Start session"* | Establishes how to find and use skills before responding. |
| [`writing-skills`](.claude/skills/writing-skills) | *"Author a skill"* | Guides authoring and verifying skills before deployment. |

### 3. Codebase Knowledge Graph & Document Parsing
| Skill | Trigger / Use Case | Description |
|---|---|---|
| [`graphify`](.claude/skills/graphify) | *"/graphify", "map codebase"* | Converts repository into a Tree-sitter AST knowledge graph with HTML visualizer. |
| [`convert-documents-to-markdown`](.claude/skills/convert-documents-to-markdown) | *"Convert docx, pptx, xlsx, pdf"* | AnyDoc CLI parser converting Office docs, sheets, presentations, and PDFs to Markdown. |
| [`literature-research`](.claude/skills/literature-research) | *"Research papers"* | Queries scientific databases (PubMed/arXiv) and synthesizes literature reviews. |

### 4. Meta-Tooling, Discovery & Evolution
| Skill | Trigger / Use Case | Description |
|---|---|---|
| [`skill-creator`](.claude/skills/skill-creator) | *"Create a new skill"* | Official Anthropic framework for authoring, evaluating, and benchmarking skills. |
| [`find-skills`](.claude/skills/find-skills) | *"Find a skill for X"* | Vercel Labs discovery utility to search and install skills from registries. |
| [`task-observer`](.claude/skills/task-observer) | *"Observe workflow", "record friction"* | Continuous session observer capturing patterns, corrections, and drafting skills. |
| [`mcp-builder`](.claude/skills/mcp-builder) | *"Build an MCP server"* | Complete engineering guide for creating FastMCP and Node MCP SDK servers. |
| [`webapp-testing`](.claude/skills/webapp-testing) | *"Test web application"* | Playwright UI test harness with `with_server.py` lifecycle runner. |

### 5. Design Engineering, Animation & Craft UI
| Skill | Trigger / Use Case | Description |
|---|---|---|
| [`design-taste-frontend`](.claude/skills/design-taste-frontend) | *"Design non-slop landing page"* | Taste Skill: strict anti-slop rules, design intensity dials, and OKLCH palettes. |
| [`frontend-design`](.claude/skills/frontend-design) | *"Distinctive UI design"* | Anthropic design lead guidelines for non-templated typography and layout. |
| [`emil-design-eng`](.claude/skills/emil-design-eng) | *"Elevate component craft"* | Enforces Emil Kowalski design engineering principles: springs, physics, and polish. |
| [`apple-design`](.claude/skills/apple-design) | *"Apple HIG design"* | Applies Apple Human Interface Guidelines: typography, spacing, depth, and blur. |
| [`web-design-guidelines`](.claude/skills/web-design-guidelines) | *"Audit UI against design rules"* | Checklists for accessibility, contrast ratios, and layout stability. |
| [`hallmark`](.claude/skills/hallmark) & [`impeccable`](.claude/skills/impeccable) | *"Add signature polish"* | Visual excellence standards that elevate generic templates to award-winning tiers. |
| [`prototype`](.claude/skills/prototype) | *"Build 3 UI variants"* | Generates multiple distinct layout variants behind an interactive switcher. |
| [`pick-ui-library`](.claude/skills/pick-ui-library) | *"Pick UI component library"* | Opinionated recommendation engine for OTPs, virtualization, drag & drop, and charts. |
| [`animate`](.claude/skills/animate) | *"Add micro-animations"* | Precision CSS & Tailwind keyframe transitions, spring curves, and hover states. |
| [`animate-expo`](.claude/skills/animate-expo) | *"Animate React Native screen"* | Reanimated and gesture-handler patterns for native mobile performance. |
| [`animation-vocabulary`](.claude/skills/animation-vocabulary) | *"Define easing curves"* | Motion design taxonomy covering durations, dampening, overshoot, and stagger. |
| [`find-animation-opportunities`](.claude/skills/find-animation-opportunities) | *"Find motion moments"* | Audits static interfaces to identify delightful interaction moments. |
| [`improve-animations`](.claude/skills/improve-animations) | *"Refine abrupt animation"* | Tunes abrupt linear movements into natural, physics-governed spring animations. |
| [`review-animations`](.claude/skills/review-animations) | *"Audit motion performance"* | Flags layout thrashing, non-composited properties, and frame jank. |

### 6. B2B Lead Generation & Market Intelligence
| Skill | Trigger / Use Case | Description |
|---|---|---|
| [`scrape-leads`](.claude/skills/scrape-leads) | *"Scrape SaaS leads"* | Apify lead scraping, LLM classification, email enrichment, and Sheets export. |
| [`gmaps-leads`](.claude/skills/gmaps-leads) | *"Google Maps leads"* | Local business discovery with website and LinkedIn contact enrichment. |
| [`classify-leads`](.claude/skills/classify-leads) | *"Qualify leads"* | LLM-based lead scoring and ICP categorization in Google Sheets. |
| [`casualize-names`](.claude/skills/casualize-names) | *"Clean first names"* | Converts formal names to natural conversational outreach names. |

### 7. Cold Outreach & Email Automation
| Skill | Trigger / Use Case | Description |
|---|---|---|
| [`instantly-campaigns`](.claude/skills/instantly-campaigns) | *"Create cold campaign"* | 3-step sequence campaigns in Instantly with multi-angle A/B test variants. |
| [`instantly-autoreply`](.claude/skills/instantly-autoreply) | *"Reply to prospect"* | Classifies inbound positive/negative responses and crafts context-aware replies. |
| [`welcome-email`](.claude/skills/welcome-email) | *"Send welcome sequence"* | Automated client onboarding email sequence. |
| [`gmail-inbox`](.claude/skills/gmail-inbox) | *"Triage emails"* | Multi-account unified Gmail inbox triage. |
| [`gmail-label`](.claude/skills/gmail-label) | *"Label inbox"* | Rules-based Gmail labeling and folder filtering workflows. |

### 8. Sales, Proposals & Client Onboarding
| Skill | Trigger / Use Case | Description |
|---|---|---|
| [`create-proposal`](.claude/skills/create-proposal) | *"Build proposal"* | Generates PandaDoc proposals dynamically using Sheets pricing & scope data. |
| [`upwork-apply`](.claude/skills/upwork-apply) | *"Write Upwork bid"* | Scrapes Upwork listings and tailors high-converting cover letters and bids. |
| [`onboarding-kickoff`](.claude/skills/onboarding-kickoff) | *"Kickoff client"* | Orchestrates project workspaces, document templates, and initial tasks. |

### 9. Video Engineering & Content Intelligence
| Skill | Trigger / Use Case | Description |
|---|---|---|
| [`video-edit`](.claude/skills/video-edit) | *"Edit video silences"* | Neural Voice Activity Detection (VAD) to trim dead air and stitch jump cuts. |
| [`pan-3d-transition`](.claude/skills/pan-3d-transition) | *"Add 3D swivel"* | Programmatic Remotion 3D pan and camera transition renderer. |
| [`recreate-thumbnails`](.claude/skills/recreate-thumbnails) | *"Swap thumbnail face"* | AI face-swapping pipeline for YouTube thumbnail CTR optimization. |
| [`youtube-outliers`](.claude/skills/youtube-outliers) | *"Find viral videos"* | Detects anomalous high-view videos exceeding average channel view baselines. |
| [`cross-niche-outliers`](.claude/skills/cross-niche-outliers) | *"Cross-niche viral angles"* | Discovers breakout video angles from adjacent industries for adaptation. |
| [`title-variants`](.claude/skills/title-variants) | *"Generate YouTube titles"* | High-CTR title variations engineered around curiosity gaps and tension hooks. |

### 10. Community Intelligence & Research
| Skill | Trigger / Use Case | Description |
|---|---|---|
| [`skool-monitor`](.claude/skills/skool-monitor) | *"Monitor Skool community"* | Tracks member posts, unanswered questions, and engagement velocity. |
| [`skool-rag`](.claude/skills/skool-rag) | *"Search Skool knowledge"* | Semantic vector search across historical community threads and masterminds. |

### 11. Vercel, Next.js & Performance Optimization
| Skill | Trigger / Use Case | Description |
|---|---|---|
| [`vercel-react-best-practices`](.claude/skills/vercel-react-best-practices) | *"Optimize React rendering"* | Vercel Engineering rules for Server Components, memoization, and waterfalls. |
| [`vercel-composition-patterns`](.claude/skills/vercel-composition-patterns) | *"Refactor component tree"* | Clean compound component architecture and state colocation best practices. |
| [`vercel-optimize`](.claude/skills/vercel-optimize) | *"Reduce Vercel compute bills"* | Diagnoses cold starts, data transfer overhead, Edge config, and Core Web Vitals. |
| [`vercel-cli-with-tokens`](.claude/skills/vercel-cli-with-tokens) | *"Deploy headless Vercel"* | Scripted deployments using auth tokens, environment variable binding, and aliasing. |
| [`deploy-to-vercel`](.claude/skills/deploy-to-vercel) | *"Ship to Vercel"* | Streamlined zero-configuration production deployment execution. |
| [`vercel-react-view-transitions`](.claude/skills/vercel-react-view-transitions) | *"Implement view transitions"* | Native React View Transition API (`<ViewTransition>`) without bulky libraries. |
| [`vercel-react-native-skills`](.claude/skills/vercel-react-native-skills) | *"Cross-platform React"* | Shared architectural patterns between web and React Native codebases. |

### 12. Persistent Memory Architecture
| Skill | Trigger / Use Case | Description |
|---|---|---|
| [`memory-capture`](.claude/skills/memory-capture) | *"Save architecture decision"* | Records technical insights and conventions into vector memory during sessions. |
| [`memory-cloud-recall`](.claude/skills/memory-cloud-recall) | *"Recall decision from last week"* | Queries remote Supabase memory when local context window is cleared. |
| [`memory-session-start`](.claude/skills/memory-session-start) | *"Resume session context"* | Ingests recent learnings, active branch goals, and user preferences on startup. |
| [`memory-session-end`](.claude/skills/memory-session-end) | *"Wrap up session"* | Compiles structured summaries and commits progress checkpoints. |

---

## 🤖 Autonomous Subagents

Located in [`.claude/agents/`](.claude/agents):

1. **`code-reviewer`** ([`code-reviewer.md`](.claude/agents/code-reviewer.md)): Senior staff engineer persona; zero previous conversational context for complete objectivity.
2. **`qa`** ([`qa.md`](.claude/agents/qa.md)): Boundary value exploration, failure injection, test generation (Jest/Vitest/Playwright).
3. **`research`** ([`research.md`](.claude/agents/research.md)): Deep web scraping, API documentation analysis, and feasibility synthesis.
4. **`email-classifier`** ([`email-classifier.md`](.claude/agents/email-classifier.md)): High-throughput communication triage for Gmail inboxes.

---

## 🔌 MCP Servers Suite

Pre-configured in [`.mcp.json`](.mcp.json) and [`.claude/settings.json`](.claude/settings.json):
- **`context7`**: High-performance semantic vector search.
- **`playwright`**: Full browser automation, screenshots, and visual testing.
- **`filesystem`**: Secure, scoped directory manipulation.
- **`memory`**: Local knowledge graph entity and relationship tracking.
- **`fetch`**: High-speed web scraping and markdown conversion.
- **`headroom`**: Local prompt compression and CCR cache alignment (optional).

---

## 🛡️ Key Principles & Self-Annealing

1. **Auto-Discovery by Intent**: Every skill contains a curated description in its `SKILL.md`. Agents route requests autonomously based on intent.
2. **The Self-Annealing Loop**: When external APIs change or scripts fail, the agent repairs the implementation and updates `SKILL.md` with the learned fix.
3. **Multi-Environment First**: Rules are mirrored across `CLAUDE.md`, `AGENTS.md`, and `GEMINI.md`, ensuring identical performance across Claude Code and Google Antigravity.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — free to use, modify, and distribute in commercial and private projects.

---

<p align="center">
  <b>Maintained by <a href="https://github.com/Vedant04-tech">Vedant04-tech</a></b><br>
  <i>Empowering developers and agencies with autonomous AI engineering workflows.</i>
</p>
