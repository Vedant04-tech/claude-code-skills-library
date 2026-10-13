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

## 🛑 2. Application Security Tooling (Strix Policy)

When evaluating or using automated security testing skills like **Strix** (`usestrix/strix`):

1. **Authorization Prerequisite**: Strix or similar active vulnerability assessment tools MUST only be executed against applications and domains explicitly owned by the operator or where documented, written permission has been obtained.
2. **Isolation First**: Testing must be conducted against locally running instances or isolated staging environments. Testing against third-party production systems is strictly prohibited.
3. **Non-Destructive Payloads**: Exploitation simulations must avoid destructive operations (e.g., dropping databases, denial of service, resource exhaustion).
4. **Redacted Reports**: Pentest reports and vulnerability summaries must automatically redact sensitive environment variables, internal IP ranges, and authentication tokens.

---

## 🌐 3. Web Retrieval & Scraping Constraints (Agent Reach & Scrapers)

When using web research tools (`Agent Reach`, Apify scrapers, PubMed clients):

1. **No Universal Access Claims**: Web scrapers do not bypass Cloudflare Turnstile, CAPTCHAs, or authentication barriers without explicit session cookies.
2. **Rate Limiting & Politeness**: Agents must respect rate limits, adhere to `robots.txt` guidelines, and include backoff delays to prevent IP bans.
3. **Terms of Service**: Scraping must comply with target platform Terms of Service. Unofficial scrapers rely on public endpoints and may break if upstream UI layouts change.
4. **Data Hygiene**: Scraped prospect data must be stored locally in designated workspaces or secure user spreadsheets, never committed to public repositories.

---

## 💾 4. Agent Memory & Privacy Boundaries

This repository supports two memory models:

1. **Local Model Context Protocol Memory (`@modelcontextprotocol/server-memory`)**:
   - Stores knowledge graph entities and relations entirely on the local machine.
   - Zero external cloud synchronization.
2. **Cloud-Synced Memory (`vendor/claude-memory`)**:
   - Synchronizes semantic vectors to a user-owned **Supabase** instance.
   - Credentials (`SUPABASE_URL`, `SUPABASE_SERVICE_KEY`) remain in local environment variables.
   - Operators can wipe stored memory at any time directly through their Supabase console.

> [!WARNING]
> Do NOT enable competing persistent memory plugins (`claude-mem` and `claude-memory`) simultaneously. Choose either local SQLite or Supabase cloud sync to prevent duplicate token injection.

---

## 📦 5. Script & Hook Execution Discipline

1. **No Blind Script Execution**: All installation and build scripts must be statically reviewed before running.
2. **Deterministic Code Separation**: Following the Agent Skills standard, deterministic tasks are handled by audited scripts in `scripts/`, while probabilistic tasks remain with the LLM.
3. **Subprocess Sandboxing**: Playwright and browser scripts execute in scoped sandboxes without root/administrator privileges.
