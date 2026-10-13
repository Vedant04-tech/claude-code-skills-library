# Prompts Library

Custom prompts for specialized workflows. These are templates and standalone instructions used across projects.

## Workflow Prompts (3 files)

### 1. gmaps_lead_pipeline_builder.md
**Purpose:** Automate the Google Maps lead generation pipeline end-to-end.
**Use when:** You need to scrape leads from Google Maps, enrich them with contact info, and bulk-load into Google Sheets for outreach.
**Key steps:** Scrape → Extract websites → Find contact emails → Classify → Tag in Sheets

### 2. upwork_pipeline_builder.md
**Purpose:** Automate Upwork job scraping, proposal generation, and application submission.
**Use when:** You're running Upwork cold outreach and need to scale proposal creation.
**Key steps:** Scrape jobs → Match to skills → Generate proposal → Submit

### 3. instantly_campaign_creator.md
**Purpose:** Build and test cold email campaign workflows in Instantly.
**Use when:** You need to create multi-step email sequences with A/B testing.
**Key steps:** Generate emails → Test HTML formatting → Create campaigns → Verify in Instantly UI
**Technical notes:** Documents Instantly API v2 constraints (HTML wrapping, timezone enums, sequence structure).

---

For more, see `.claude/skills/README.md` for skill-level automation.
