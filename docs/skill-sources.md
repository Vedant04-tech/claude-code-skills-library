# Skills Sources & Installation Status

This document tracks which skills from the "Best Claude Code Skills" guide have been installed, and which are recommended for future installation.

**Date:** July 22, 2026  
**Guide:** `docs/best-claude-code-skills-guide.md`  
**Completed:** Phase A–E (local reorganization, memory integration, docs)  
**Next:** Plugin marketplace setup + curated skill installations

---

## Summary

| Category | Installed | Recommended | Status |
|----------|-----------|-------------|--------|
| Business (custom) | 26 ✓ | — | Active |
| Memory | 4 ✓ | Setup required | Integrated |
| Official Anthropic | 0 | 5+ | To install |
| Superpowers (obra) | 0 | 1 (v6.1.1) | In vendor/ |
| Frontend (Vercel) | 0 | 3+ | To install |
| Data/ML | 0 | 5+ | To install |
| DevOps/Infra | 0 | 10+ | To install |
| Docs (Diátaxis) | 0 | 2 | To install |
| **Total Current** | **30** | — | — |

---

## Installed Skills (32 total)

### Business Skills (26) — Already Active ✓
- `add-webhook`, `casualize-names`, `classify-leads`, `create-proposal`, `cross-niche-outliers`
- `design-website`, `generate-report`, `gmail-inbox`, `gmail-label`, `gmaps-leads`
- `instantly-autoreply`, `instantly-campaigns`, `literature-research`, `local-server`
- `modal-deploy`, `onboarding-kickoff`, `pan-3d-transition`, `recreate-thumbnails`
- `scrape-leads`, `skool-monitor`, `skool-rag`, `title-variants`, `upwork-apply`
- `video-edit`, `welcome-email`, `youtube-outliers`

### Design Engineering Skills (Emil Kowalski) — Active ✓
- `animate`, `animate-expo`, `animation-vocabulary`, `apple-design`, `ask-sonner`, `emil-design-eng`
- `find-animation-opportunities`, `improve-animations`, `pick-ui-library`, `prototype`, `review-animations`, `write-swift`

### Impeccable Design System Skills (pbakaus/impeccable) — Active ✓
- `impeccable`

### Hallmark Skills (nutlope/hallmark) — Active ✓
- `hallmark`

### Dev Packages & Integrations — Active ✓
- `agentation` (npm devDependency)

---


## To Install by Category (from Guide)

### Stage 1: Foundation (High-Leverage, Recommended Now)

#### 1. Official Anthropic Skills (`anthropics/skills`)
**Source:** github.com/anthropics/skills (149k stars, actively maintained)  
**Install method:** `/plugin marketplace add anthropics/skills`  
**What to add:**
- `skill-creator` — Meta-skill for authoring new skills (highest value)
- `mcp-builder` — Build MCP servers from scratch
- `webapp-testing` — Playwright UI testing (examples)
- `web-artifacts-builder` — React/Tailwind/shadcn artifacts
- `example-skills` — Reference implementations

**Status:** `[ ] Not yet installed`  
**Note:** Some document skills (docx, pdf) are Claude.ai-only, not available in Claude Code.

#### 2. Superpowers (obra/superpowers)
**Source:** github.com/obra/superpowers (257k stars, v6.1.1 July 2 2026)  
**Install method:** `/plugin marketplace add obra/superpowers-marketplace` → `/plugin install superpowers@superpowers-marketplace`  
**What it includes:**
- `brainstorming`, `writing-plans`, `test-driven-development`
- `systematic-debugging`, `using-git-worktrees`, `subagent-driven-development`
- `verification-before-completion`, `writing-skills`

**Status:** `[ ] In vendor/superpowers/ (copy in place, not yet wired to settings.json)`  
**Why:** Core software-development discipline framework — most impactful single install.

#### 3. Vercel Frontend Trio (`vercel-labs/agent-skills`)
**Source:** github.com/vercel-labs/agent-skills  
**Install method:** `npx skills add vercel-labs/agent-skills --skill frontend-design --skill vercel-react-best-practices --skill web-design-guidelines --agent claude-code`  
**What it includes:**
- `frontend-design` — Bold, distinctive UI patterns (avoids "AI slop")
- `vercel-react-best-practices` — React conventions (~185K installs)
- `web-design-guidelines` — General web design + `next-best-practices`

**Status:** `[ ] Not yet installed`  
**Note:** ~185K installs on skills.sh; highest-quality frontend guidance.

---

### Stage 2: AI Engineering Specialization (This Week/Month)

#### 4. Data/ML Skills
**DuckDB** (silvainfm/claude-skills)
- Install: `npx skills add silvainfm/claude-skills --skill duckdb --agent claude-code`
- Use: In-process SQL analytics on DataFrames/CSV/Parquet
- Status: `[ ] Not installed`

**LLM Evaluation** (various)
- Candidates: `evaluating-llms`, `llm-evaluation` (test prompt quality, RAG, hallucination/bias)
- Sources: wshobson/agents, borghei/Claude-Skills
- Status: `[ ] Not installed`

**RAG Engineering** (rag-engineer)
- Use: Chunking, embedding selection, vector-DB, precision@k/recall@k/NDCG
- Sources: wshobson/agents, claude directory
- Status: `[ ] Not installed`

**MLOps** (wshobson/agents or alirezarezvani/claude-skills)
- Includes: MLflow config, model versioning, drift monitoring
- Status: `[ ] Not installed`

#### 5. Diátaxis Documentation
**Source:** sammcj/agentic-coding → `writing-documentation-with-diataxis` (136 stars, ~475 installs)  
OR `pfeff/claude-skills` → `diataxis`  
**Install:** `npx skills add sammcj/agentic-coding --skill writing-documentation-with-diataxis --agent claude-code`  
**Use:** Structure docs as tutorials / how-tos / reference / explanation  
**Status:** `[ ] Not installed`

---

### Stage 3: Extended (Lower-Priority, Reference)

#### 6. DevOps/Infrastructure Skills

**Official HashiCorp Skills**
- Terraform, Packer expertise
- Status: `[ ] Verify availability & install method`

**Official Pulumi Skills** (pulumi/agent-skills)
- pulumi-esc, pulumi-best-practices, ComponentResource patterns
- Status: `[ ] Not installed`

**Comprehensive DevOps Bundles** (reference for later, large scope)
- `akin-ozer/cc-devops-skills` (31 skills: Ansible, Docker, K8s, Terraform, Helm, CI/CD)
- `j4flmao/agent-skills` (55+ skills: Docker, K8s, Terraform, ArgoCD, chaos, FinOps)
- `BagelHole/DevOps-Security-Agent-Skills` (160+ skills: SOC2, HIPAA, GDPR, PCI-DSS)
- Status: `[ ] Keep in vendor/ as reference; do NOT install yet (scope too large, low immediate need)`

**Best practice:** Set `disable-model-invocation: true` for any skill with real side effects (deploys).

#### 7. Code Review & Testing
**playwright-skill** (lackeyjb)
- Model-invoked browser testing
- Status: `[ ] Not installed`

**PICT Pairwise Test-case Generation** (omkamal/pypict-claude-skill)
- Status: `[ ] Not installed`

---

### Curated Lists (Browse-Later References)

**Do NOT install — just bookmark:**
- **ComposioHQ/awesome-claude-skills** (68k stars, 1000+ skills)
- **VoltAgent/awesome-agent-skills** (28.3k stars, 1000+ curated)
- **davila7/claude-code-templates** (28.2k stars; also a plugin marketplace)
- **travisvn/awesome-claude-skills**, **BehiSecc/awesome-claude-skills**, **rohitg00/awesome-claude-code-toolkit**

URLs in `vendor/awesome-claude-code/README.md` if needed.

---

## Installation Roadmap

### Immediate (Next Hour)
1. ✓ ~~Local filesystem reorg~~ (done)
2. ✓ ~~Integrate memory skills~~ (done)
3. ✓ ~~Create `.claude/settings.json`~~ (minimal for now, see step 5)
4. [ ] Create `.claude/settings.json` with plugin marketplaces registered

### Short-term (This Week)
1. [ ] `/plugin marketplace add anthropics/skills` → install `skill-creator`, `mcp-builder`, `webapp-testing`, `web-artifacts-builder`
2. [ ] `/plugin marketplace add obra/superpowers-marketplace` → install `superpowers@superpowers-marketplace`
3. [ ] `npx skills add vercel-labs/agent-skills --skill frontend-design --skill vercel-react-best-practices --skill web-design-guidelines --agent claude-code`
4. [ ] Verify plugin installs work and skills load

### Medium-term (This Month)
1. [ ] Add data/ML skills (DuckDB, LLM eval, RAG engineer, MLOps)
2. [ ] Add Diátaxis documentation skill
3. [ ] Run `npx skills check` / `npx skills update` periodically

### Long-term (As Needed)
1. [ ] DevOps skills if infra work is added to portfolio
2. [ ] Review `vendor/` repos for any skills worth extracting and adapting
3. [ ] Write 2–3 custom skills encoding your own conventions (commit to `.claude/skills/`)

---

## Notes

- **Marketplace registration:** All plugin-based skills (Anthropic, Superpowers, Vercel, wshobson, pulumi, HashiCorp) go in `.claude/settings.json` as marketplace URLs, NOT cloned into `.claude/skills/`. This keeps them updateable and avoids duplication.
- **Individual skill installs:** Single-skill repos (DuckDB, Diátaxis, etc.) use `npx skills add <repo> --skill <name> --agent claude-code`, which places the skill directly in `.claude/skills/`.
- **Vendor repos:** Full clones (superpowers, claude-memory, awesome-claude-code) live in `vendor/` as reference/source-of-truth copies. Do NOT auto-load them — only extract what you need.
- **Security:** Review skill contents before install — especially anything running bash or touching secrets. Prefer official (Anthropic, Vercel, HashiCorp, Pulumi, obra) and high-install-count skills.

---

## Files to Update Next

1. `.claude/settings.json` — Register plugin marketplaces
2. `.claude/settings.local.json` — (If needed) Local-only overrides
3. `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` — Update "Available Skills" count as new ones are added
4. This file — Mark installations as complete

---

## References

- **Best Claude Code Skills Guide:** `docs/best-claude-code-skills-guide.md`
- **Skills Specification:** agentskills.io / agentskills.io/specification
- **Claude Code Docs:** code.claude.com/docs/en/skills
- **Agent Skills Docs:** platform.claude.com/docs/en/agents-and-tools/agent-skills/
- **npx skills CLI:** github.com/vercel-labs/skills (v1.5.19 or later)
