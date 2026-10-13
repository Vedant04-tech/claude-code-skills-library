# 🛡️ Security Review & Operational Safeguards

> **Security standards, privacy boundaries, and operational constraints for the Claude Code Skills Library.**  
> **Last Audited:** October 13, 2026  

---

## 🔒 1. Secrets & Credentials Policy

- **Zero Committed Secrets**: No live API keys, personal access tokens (PATs), OAuth secrets, or connection strings are ever committed to this repository.
- **Template Isolation**: All environment variable requirements are documented in [`.env.example`](../.env.example).
- **Git Ignore Safeguards**: [`.gitignore`](../.gitignore) explicitly excludes all `.env*` variants, `.pem`, `.key`, and credential stores.
- **Auditing Protocol**: Periodic regex and entropy scans are run against the codebase before publishing to upstream remotes.

---

---

## 🛑 2. Application Security Tooling (Strix Operational Guardrails)

The library bundles 9 autonomous application security and penetration testing skills powered by **Strix** (`usestrix/strix`):
- `penetration-testing-with-strix`
- `find-security-vulnerabilities-in-code`
- `owasp-top-10-testing`
- `api-security-testing`
- `application-security-testing`
- `ci-security-scanning-with-strix`
- `fix-security-vulnerabilities-with-strix`
- `managed-pentesting-with-strix`
- `web-app-penetration-testing`

### Mandatory Security Policies:
1. **Explicit Authorization Required**: Active vulnerability scanning and penetration testing must **ONLY** target applications, domains, and repositories that the operator owns or has received documented, written authorization to test. Testing against unauthorized third-party infrastructure is strictly prohibited.
2. **Local Sandbox Isolation**: The open-source CLI executes all vulnerability validation payloads inside isolated **Docker containers**. Operators must run tests against local repositories mounted to clean working trees or isolated staging hosts (`localhost`, `127.0.0.1`, staging environments).
3. **Execution Guardrails for AI Agents**:
   - Always run in non-interactive mode (`strix -n ...`) to prevent interactive TUI hangs in automated agents.
   - Always set an explicit LLM spend cap (e.g. `--max-budget 15`).
   - Use `--scope-mode diff` on large repositories or pull requests to avoid wasteful scans on unchanged code.
4. **Non-Destructive Payloads**: Agents must never simulate denial-of-service, execute raw `DROP TABLE` or destructive data mutations, or exhaust production server resources.
5. **Report Sanitization**: Output artifacts in `strix_runs/` (such as `penetration_test_report.md` and `findings.sarif`) must be redacted before sharing externally to scrub internal infrastructure IPs and authentication secrets.

---

## 🌐 3. Web Retrieval & Scraping Constraints (Agent Reach & Scrapers)

The library integrates **Agent Reach** (`Panniantong/Agent-Reach`) along with specialized web retrieval tools:
- `agent-reach`: Universal internet content retrieval and multi-platform research across 15+ services (GitHub, Reddit, Twitter/X, YouTube, Jina Reader, Exa, V2EX, etc.).

### Operational Boundaries:
1. **Zero Exploitation / No Bypass Claims**: Web retrieval tools rely on public endpoints, open-source CLIs, and voluntary local session cookies. They do not claim or attempt to bypass Cloudflare Turnstile, CAPTCHAs, or paywalls.
2. **Rate Limiting & Politeness**: Agents must enforce delay backoffs between consecutive queries. Rapid polling or aggressive parallel scraping that risks IP blacklisting is prohibited.
3. **Local Credential Seclusion**: For platforms requiring browser cookies (e.g. Reddit, X/Twitter), cookies are stored strictly on the operator's local machine in `~/.agent-reach/config.yaml` and are never transmitted to external telemetry servers.
4. **Compliance with Platform Terms**: Data extracted must strictly be utilized for research, indexing, and synthesis within the operator's active project workspace.

---

## 💾 4. Agent Memory Architecture & Coexistence Guidelines

This repository provides clear architectural options for persistent memory across coding sessions:

| Memory Solution | Architecture | Storage Engine | Scope & Best Fit | Multi-Agent Conflict Risk |
|---|---|---|---|:---:|
| **MCP Memory (`server-memory`)** | Local MCP Server | Entity-Relation Graph (local JSON) | Standard single-machine agent memory | None (Independent tool) |
| **Cloud-Synced Memory (`vendor/claude-memory`)** | Agent Skills + SQL | Remote **Supabase** (pgvector) | Team collaboration, multi-machine sync, enterprise control | ⚠️ High if run with claude-mem |
| **`claude-mem` (`thedotmack/claude-mem`)** | Claude Plugin | Local SQLite + Chroma Vector DB | Local-first, zero cloud credentials, automated session compression | ⚠️ High if run with Supabase |

> [!CAUTION]
> **Mutual Exclusivity Rule**: Do NOT enable `vendor/claude-memory` (Supabase) and `claude-mem` (local SQLite/Chroma) at the same time. Simultaneous operation results in duplicate vector indexing, high token overhead, and conflicting contextual recall. Choose **one** persistent memory backend for your engineering workflow.

---

## 📦 5. Script & Hook Execution Discipline

1. **No Blind Script Execution**: All installation and build scripts must be statically reviewed before running.
2. **Deterministic Code Separation**: Following the Agent Skills standard, deterministic tasks are handled by audited scripts in `scripts/`, while probabilistic tasks remain with the LLM.
3. **Subprocess Sandboxing**: Playwright and browser scripts execute in scoped sandboxes without root/administrator privileges.
