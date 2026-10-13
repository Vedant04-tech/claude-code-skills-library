# The Best Claude Code Skills to Add to Your Setup (July 2026)

## TL;DR
- **Start with three things:** install Anthropic's official `anthropics/skills` (149k stars) for the `skill-creator` meta-skill and document/example skills; add **obra/superpowers** (257k stars — the most-starred skills framework, which enforces TDD/planning/debugging discipline); and install **Vercel's `frontend-design` + `vercel-react-best-practices`** skills via the `npx skills` CLI. These three cover the highest-leverage gaps for an AI-engineering portfolio.
- **Use the `npx skills` CLI (vercel-labs/skills) or Claude Code's `/plugin marketplace` as your installer** — skills are just folders with a `SKILL.md` file that live in `~/.claude/skills/` (personal, all projects) or `.claude/skills/` (project, committed to git). Because they follow the open Agent Skills standard, the same skill also works in Cursor, Codex, Gemini CLI, and Copilot.
- **Curate, don't hoard.** SkillsBench analyzed 47,150 public skills and found an average quality score of just 6.2 out of 12, while curated skills raised agent pass rates by an average of 16.2 percentage points (Agentman, "The Agent Skills Ecosystem in 2026"). Snyk's "ToxicSkills" audit detected prompt injection in 36% of tested skills. Install 5–10 vetted skills from reputable authors (Anthropic, Vercel, wshobson, obra, HashiCorp, Pulumi) and treat every community skill like an npm dependency you'd review before adding.

## Key Findings

**Skills are a genuine, well-supported capability, not a beta experiment.** Anthropic introduced Agent Skills in October 2025 and published them as an open standard at agentskills.io on December 18, 2025. Within 48 hours Microsoft integrated it into VS Code and OpenAI added it to both ChatGPT and Codex CLI; by March 2026, 32 tools from competing companies — including Google's Gemini CLI, JetBrains' Junie, AWS's Kiro, and Block's Goose — all read the same `SKILL.md` files. As of June 2026 the official agentskills.io showcase lists roughly 40 skills-compatible products. Claude Code has first-class support: skills auto-load from the filesystem, and there's a full plugin/marketplace distribution layer.

**A `SKILL.md` is just YAML frontmatter (`name` + `description`) plus Markdown instructions.** The key mechanism is "progressive disclosure": at session start Claude reads only each skill's ~100-token name/description; the full body (typically under 5,000 tokens) loads only when the skill is judged relevant, and bundled `scripts/`/`references/`/`assets/` load on demand. This lets you host many skills without bloating context.

**The ecosystem is enormous but uneven in quality.** SkillsMP alone lists about 1.9 million public skills scraped from GitHub — but catalog size is not a quality or safety signal. Curated skills from reputable authors are what matter.

## Details

### 1. Official Anthropic skills & documentation

**anthropics/skills** (github.com/anthropics/skills) — **149k stars, ~41 commits, actively maintained (verified July 22, 2026).** The canonical reference repo. Contains:
- **Document skills** (`docx`, `pdf`, `pptx`, `xlsx`) — the production skills powering Claude's file creation. Source-available (not open source). Note: these pre-built document skills run on Claude.ai and the API but are **not available inside Claude Code** — in Claude Code you get the open-source `claude-api` skill bundled instead.
- **`skill-creator`** — Anthropic's official meta-skill that scaffolds new skills: it walks Claude through generating a properly structured `SKILL.md` with frontmatter plus supporting scripts/resources. The single best starting point for authoring your own.
- **Example skills**: `web-artifacts-builder` (React/Tailwind/shadcn artifacts), `mcp-builder` (build MCP servers), `webapp-testing` (Playwright UI testing), `brand-guidelines`, `algorithmic-art`, `canvas-design`, `slack-gif-creator`, `internal-comms`.
- A `template/` folder and the `spec/` (Agent Skills specification).
- **Install in Claude Code:** `/plugin marketplace add anthropics/skills` then `/plugin install document-skills@anthropic-agent-skills` or `/plugin install example-skills@anthropic-agent-skills`. [github](https://github.com/anthropics/skills)

**Bundled Claude Code skills** (ship in every session unless disabled via `disableBundledSkills`): `/doctor`, `/code-review`, `/batch`, `/debug`, `/loop`, `/claude-api`, plus `/run` and `/verify`. [Claude Code Docs](https://code.claude.com/docs/en/skills) There's also a bundled `dataviz` skill for charts. Requires Claude Code v2.1.203+ for symlinked skill directories. [Claude Code Docs](https://code.claude.com/docs/en/skills)

**Official documentation to read:**
- Claude Code skills guide: code.claude.com/docs/en/skills ("Extend Claude with skills")
- Agent Skills overview + best practices: platform.claude.com/docs/en/agents-and-tools/agent-skills/
- Engineering blog: "Equipping agents for the real world with Agent Skills" (anthropic.com/engineering, published Oct 16, 2025, by Barry Zhang, Keith Lazuka, and Mahesh Murag)
- Help center: "Use skills in Claude" and "Creating custom skills" (support.claude.com)
- Open standard: agentskills.io / agentskills.io/specification

### 2. Coding / software-engineering skills

**obra/superpowers** (github.com/obra/superpowers) — **257k stars, latest release v6.1.1 (July 2, 2026), very actively maintained.** By Jesse Vincent (obra). The most-starred skills framework in the ecosystem. It's a complete software-development methodology packaged as composable, auto-triggering skills: `brainstorming` (refine requirements before code), `writing-plans`, `test-driven-development` (enforces red-green-refactor — write the failing test, watch it fail, then minimal code), `systematic-debugging` (root-cause before fixes), `using-git-worktrees`, `subagent-driven-development` (with code-review checkpoints), `finishing-a-development-branch`, and `writing-skills`. Strongly recommended for a student building disciplined engineering habits.
- **Install:** `/plugin marketplace add obra/superpowers-marketplace` then `/plugin install superpowers@superpowers-marketplace`. (Also on the official marketplace as `superpowers@claude-plugins-official`.) [github](https://github.com/obra/superpowers)

**wshobson/agents** (github.com/wshobson/agents) — **35.6k stars, actively maintained (updated for Opus 4.7/Sonnet 4.6/Haiku 4.5).** By Seth Hobson. A large multi-harness collection: currently ~185 agents, ~153 skills, ~100 commands, and 16 workflow orchestrators across ~80 focused plugins. Highly granular, so you install only what you need. Popular coding skills include `code-review-excellence`, `typescript-advanced-types`, `python-testing-patterns`, `git-advanced-workflows`, `api-design-principles`, `error-handling-patterns`, and `architecture-patterns`. Caveat: single-maintainer, no versioned releases — you track `main`, and component counts change substantially between updates.
- **Install:** `npx skills add wshobson/agents --agent claude-code` (or via its plugin marketplace).

**Engineering-workflow skills worth noting individually:** `mhattingpete/claude-skills-marketplace` (engineering-workflow plugin: `git-pushing`, `review-implementing`, `test-fixing`), and `NeoLabHQ/context-engineering-kit` (`software-architecture` — Clean Architecture/SOLID; `subagent-driven-development`; `prompt-engineering`).

**Code-review / testing specifics:** `pypict-claude-skill` (omkamal — PICT pairwise test-case generation), `playwright-skill` (lackeyjb — model-invoked browser testing), and Anthropic's bundled `/code-review`.

### 3. Data science / ML / AI-engineering skills

This is the most relevant category for an AI-engineering portfolio.

- **DuckDB skill** (silvainfm/claude-skills) — in-process SQL analytics on DataFrames/CSV/Parquet; `npx skills add silvainfm/claude-skills --skill duckdb`.
- **Anthropic `sql-queries`** — official; covers 5 SQL dialects with optimization hints.
- **K-Dense-AI / claude-scientific-skills** — 139+ scientific skills (RDKit, Scanpy, BioPython) for computational research; MIT-licensed, redistributed in davila7's catalog.
- **wshobson/agents ML skills:** `mlflow`, `pytorch-fsdp`, `statsmodels`, `data-storytelling`, `backtesting-frameworks`, plus RAG/MLOps skills (`rag-engineer`, `ai-ml-data-science`).
- **borghei/Claude-Skills** — `data-scientist` skill (algorithm selection, feature engineering, A/B tests, SHAP/LIME) within a large 343-skill library.
- **AI/LLM-engineering skills** (from collections like microck/ordinary-claude-skills and maximem's roundup): `ai-llm-engineering` (LLM architecture/eval/deploy), `evaluating-llms` / `llm-evaluation` (test prompt quality, RAG pipelines, hallucination/bias/toxicity), `llm-patterns`, `prompt-caching`, and `rag-engineer` (chunking, embedding, vector-DB selection, precision@k/recall@k/NDCG). [Claude Directory](https://www.claudedirectory.org/skills/topic/rag)
- **alirezarezvani/claude-skills** — `senior-ml-engineer` (MLOps scripts: MLflow config, model versioning, drift monitoring; LLM integration builder; RAG system builder). [GitHub](https://github.com/alirezarezvani/claude-skills/blob/main/engineering-team/CLAUDE.md) Installable as a plugin marketplace: `/plugin marketplace add alirezarezvani/claude-skills`.

### 4. DevOps / infrastructure skills

- **akin-ozer/cc-devops-skills** — 31 generator/validator skills for Ansible, Docker, Kubernetes, Terraform, Helm, GitHub Actions, GitLab CI, Jenkins, Azure Pipelines, and PromQL.
- **j4flmao/agent-skills** — 55+ DevOps skills (Docker, K8s, Terraform, Ansible, ArgoCD, Vault, chaos engineering, FinOps, all major clouds). [AI Builder Club](https://www.aibuilderclub.com/blog/claude-code-for-devops-skills-guide)
- **BagelHole/DevOps-Security-Agent-Skills** — 160+ skills with production configs and compliance frameworks (SOC2, HIPAA, GDPR, PCI-DSS). [AI Builder Club](https://www.aibuilderclub.com/blog/claude-code-for-devops-skills-guide)
- **pulumi/agent-skills** — official Pulumi skills (`pulumi-esc`, `pulumi-best-practices`, ComponentResource patterns, and migration from Terraform/CDK/CloudFormation/ARM).
- **HashiCorp Agent Skills** — official Terraform and Packer expertise. [DevOps Daily](https://devops-daily.com/posts/best-claude-code-plugins-devops-2026)
- **wshobson/agents:** `terraform-module-library`, `github-actions-templates`, `k8s-security-policies`.
- **jeffallan/claude-skills** — `devops-engineer` persona [Pulumi](https://www.pulumi.com/blog/top-8-claude-skills-devops-2026/) plus `incident-runbook-templates`.
- **Best practice for DevOps skills:** set `disable-model-invocation: true` in frontmatter for anything with real side effects (deploys) so it only runs on explicit invocation; commit team-wide infra conventions to `.claude/skills/` and state safety steps (plan before apply, dry-run first) in the body.

### 5. Web / frontend skills

- **Vercel `frontend-design`** (vercel-labs/agent-eval; also bundled in anthropics/claude-code) — produces distinctive, production-grade UI that avoids generic "AI slop" aesthetics by committing to a bold aesthetic direction before coding. `npx skills add vercel-labs/agent-skills --skill frontend-design`.
- **Vercel `vercel-react-best-practices`, `web-design-guidelines`, `next-best-practices`** (vercel-labs/agent-skills) — React/Next.js conventions from Vercel; the react skill reports ~185K installs on skills.sh. Install several at once: `npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices --skill web-design-guidelines --skill frontend-design -a claude-code`. [GitHub](https://github.com/vercel-labs/skills)
- **web-artifacts-builder** (anthropics/skills) — React/Tailwind/shadcn artifacts.
- **wshobson/agents:** `tailwind-design-system` (the most-installed skill in the repo), `nextjs-app-router-patterns`, `responsive-design`, `design-system-patterns`, `fastapi-templates`, `nodejs-backend-patterns`, `postgresql-table-design`.
- **anydesign** (uxKero) and **swiftui-design-skill** (wholiver) for design-to-code.

### 6. Technical writing / documentation

- **Diátaxis documentation skills** — several implementations of the four-quadrant framework (tutorials / how-to / reference / explanation): [Claudemarketplaces](https://claudemarketplaces.com/skills/sammcj/agentic-coding/writing-documentation-with-diataxis) `sammcj/agentic-coding` → `writing-documentation-with-diataxis` (136 stars, ~475 installs) and `pfeff/claude-skills` → `diataxis`. [GitHub](https://github.com/pfeff/claude-skills/blob/main/skills/diataxis/SKILL.md) Install: `npx skills add sammcj/agentic-coding --skill writing-documentation-with-diataxis --agent claude-code`. [Claudemarketplaces](https://claudemarketplaces.com/skills/sammcj/agentic-coding/writing-documentation-with-diataxis)
- **changelog-generator** (ComposioHQ) — turns git commits into user-facing release notes. [github](https://github.com/ComposioHQ/awesome-claude-skills)
- **wshobson/agents:** `openapi-spec-generation`, `data-storytelling`.
- **Skill Seekers** (yusufkaraaslan) — automatically converts any documentation website into a Claude skill.

### 7. General productivity & meta / skill-building resources

- **Curated lists:** **ComposioHQ/awesome-claude-skills** (68k stars, 1000+ skills), **VoltAgent/awesome-agent-skills** (28.3k stars; curates 1000+ headline / badge shows ~1,497 official + community skills from Anthropic, Vercel, Stripe, Cloudflare, Microsoft, Google, Figma, and more), **travisvn/awesome-claude-skills**, **BehiSecc/awesome-claude-skills**, and **rohitg00/awesome-claude-code-toolkit**.
- **davila7/claude-code-templates** (28.2k stars, latest release v1.28.3 Nov 15 2025) — CLI (`npx claude-code-templates@latest`) and web browser (aitmpl.com) for 100+ agents/commands/MCPs/skills; also usable as a plugin marketplace (`/plugin marketplace add davila7/claude-code-templates`). Includes a Skills Manager dashboard that detects personal/project/plugin skills.
- **Installers/tooling:** **vercel-labs/skills** (26.7k stars, the `npx skills` CLI, v1.5.19 July 16 2026) — a package manager for the open skills ecosystem (`add`/`list`/`find`/`update`/`init`), [Vercel](https://vercel.com/kb/guide/agent-skills-creating-installing-and-sharing-reusable-agent-context) backed by the skills.sh directory; **antfu/skills-cli** (same `npx skills` interface); and `add-skill` (add-skill.org).
- **Skill-authoring best-practice references:** `mgechev/skills-best-practices` (professional-grade skill writing + LLM validation) and Anthropic's official best-practices doc.

### Best practices for organizing your skill library

1. **Locations:** `~/.claude/skills/` for personal skills across all projects; `.claude/skills/` (committed to git) for project/team skills. [Totalum](https://www.totalum.app/blog/claude-code-skills-totalum) Enterprise and plugin locations also exist.
2. **Naming:** `name` must be lowercase-with-hyphens; it becomes the `/slash-command` route.
3. **Description is everything:** it's the only text Claude sees during routing [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/03/claude-skills-custom-skills-on-claude-code/) (max ~1,024 chars). Write it like a search/router string with concrete triggers and, ideally, "negative triggers" — e.g. "Use when the user has a CSV/TSV/Excel file and wants to explore, transform, or visualize data, even if they don't say 'analysis'."
4. **Keep `SKILL.md` lean (<500 lines):** push schemas/cheatsheets to `references/`, fragile repeatable operations to tiny CLI `scripts/`, and templates to `assets/`. Use just-in-time loading ("see references/x.md for…") and relative forward-slash paths.
5. **Frontmatter controls:** `disable-model-invocation: true` (manual-only — use for anything with side effects); `user-invocable: false` (background knowledge Claude applies automatically — good for conventions/style guides); `allowed-tools` (restrict to read-only for research skills); `context: fork` (run in an isolated subagent for high-volume/noisy tasks).
6. **Reference vs. task skills:** reference skills add always-applied knowledge (conventions, patterns); task skills are step-by-step procedures (deploy, create PR). [Vanja Petreski](https://vanja.io/claude-code-skills-guide/)
7. **When to build vs. reuse:** the community rule of thumb — "if you find yourself typing the same prompt across conversations, [Strapi](https://strapi.io/blog/what-are-agent-skills-and-how-to-use-them) make it a skill." Reuse reputable existing skills for generic tasks; write custom skills to encode *your* team/project conventions (naming, tagging, review checklists), which is where the highest value is.
8. **Skills vs. CLAUDE.md vs. subagents vs. MCP:** CLAUDE.md = always-on rules; Skills = on-demand expertise; [Medium](https://medium.com/@sharanharsoor/agent-skills-the-quiet-standard-thats-changing-how-we-build-ai-agents-53118b633401) Subagents = isolated agents with restricted tools (which can themselves use skills); MCP = connections/tools. They compose.

## Recommendations

**Stage 1 — Foundation (do today):**
1. `/plugin marketplace add anthropics/skills` and install `example-skills` (gets you `skill-creator`, `mcp-builder`, `webapp-testing`, `web-artifacts-builder`).
2. Install Superpowers: `/plugin marketplace add obra/superpowers-marketplace` → `/plugin install superpowers@superpowers-marketplace`. This alone will most improve output quality by enforcing planning + TDD.
3. Set up the `npx skills` CLI workflow and add Vercel's frontend trio (`frontend-design`, `vercel-react-best-practices`, `web-design-guidelines`).

**Stage 2 — Specialize for AI engineering (this week):**
4. Add data/ML skills matching your stack: DuckDB, an LLM-eval skill (`evaluating-llms`), a `rag-engineer` skill, and MLflow/MLOps skills from wshobson/agents or alirezarezvani/claude-skills.
5. Add a Diátaxis documentation skill so your portfolio repos ship professional docs.

**Stage 3 — Make it yours (ongoing):**
6. Use `skill-creator` to write 2–3 custom skills encoding your own conventions (your preferred project scaffold, your code-review checklist, your portfolio README style). Commit project skills to `.claude/skills/` in each portfolio repo — this both keeps behavior consistent and demonstrates the skill to anyone reviewing your code.
7. Periodically run `npx skills check` / `npx skills update`. [Vercel](https://vercel.com/kb/guide/agent-skills-creating-installing-and-sharing-reusable-agent-context)

**Thresholds that change the plan:**
- If context/token usage feels bloated → prune skills; move rarely-used ones out or use `context: fork`.
- If a skill triggers when it shouldn't → tighten its `description` or set `disable-model-invocation: true`. [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/03/claude-skills-custom-skills-on-claude-code/)
- If you move to a team → shift infra/convention skills into repo `.claude/skills/` and consider a private plugin marketplace.

## Caveats

- **Security is a real, measured concern.** Skills can execute bundled scripts with your privileges. Snyk's "ToxicSkills" audit (scanning 3,984 skills from ClawHub and skills.sh as of Feb 5, 2026) detected prompt injection in 36% of skills tested, found 1,467 malicious payloads, and reported that 13.4% of skills contain a critical security flaw, including confirmed credential-theft and backdoor-installation payloads. A broader audit of 22,511 skills across four sources surfaced 140,963 issues (~6.3 per skill). Only install from trusted authors (Anthropic, Vercel, obra, wshobson, HashiCorp, Pulumi), and read a skill's contents before use — especially anything that runs bash or touches secrets.
- **Quality varies widely.** Catalog counts (SkillsMP lists ~1.9 million scraped skills) are not a quality signal; SkillsBench found the average public skill scores 6.2/12, and only top-quartile curated skills meaningfully improve results. Prefer curated, high-install, recently-updated skills.
- **Star counts and component counts move fast.** Figures verified July 22, 2026; several repos (superpowers, wshobson/agents) grow rapidly, and third-party aggregators lag the source READMEs. Notably, obra/superpowers has grown far beyond earlier ~93k figures to 257k.
- **Document skills (`docx`/`pptx`/`xlsx`/`pdf`) are not available in Claude Code** — only on Claude.ai and via the API. Some third-party guides conflate this.
- **Naming drift:** older docs kept "commands" (`.claude/commands/`) and "skills" (`.claude/skills/`) separate; both now create `/slash-command` interfaces, but new work should use the skills format.
- **The `vercel-labs/agent-skills` star count could not be independently verified**; its individual skills report high install numbers on skills.sh, but the repo-level star figure is unconfirmed.