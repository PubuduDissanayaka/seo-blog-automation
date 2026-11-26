# Project Discovery (SEO Growth)

Run FIRST, before any keyword research, article plan or editorial calendar. Never plan content for a site
whose identity, audience and constraints are not recorded in PROJECT.md.

## Inspection-first rules

1. Inspect first: PROJECT.md, README, the repo, an existing Google Sheet, existing Search Console/GA4
   access, and the live site's existing content and sitemap.
2. Reuse what is on disk; never ask twice.
3. Mandatory vs optional: only mandatory answers block planning; assume and document the rest.
4. Batch questions; recommend an option first; give plain-language examples.
5. Ask for clarification only when a missing answer changes the strategy.
6. Save confirmed answers to PROJECT.md as they come; never overwrite without confirming a change.

## Questionnaire

### A. Website identity

- Website name, domain, purpose, business or personal.
- New or existing site; if existing, the current URL set, repo, hosting and CMS.
- Existing content inventory and any migration requirements.
- Brand voice and any assets.

### B. Niche and audience

- Primary niche and AdSense content category.
- Primary and secondary target countries; audience and expertise level.
- Primary language and any additional languages.
- Search intent mix (informational / commercial / transactional).
- Main content categories.

### C. Monetisation

- AdSense account status (none / applied / approved / existing publisher).
- Intended AdSense strategy and realistic timeline (never promise approval or income).
- Affiliate, sponsored content, other revenue.
- Disclosure requirements by region.

### D. Business and resource constraints

- Development and monthly operating budgets.
- Paid tools vs preferred free tools; available AI models and API subscriptions.
- Expected publishing frequency and editorial capacity.
- Long-term business objective.

### E. SEO-specific (this skill adds)

- Existing Search Console and GA4 property access (or need to set up).
- Existing Google Sheets tracking workbook (URL or id) - inspect before creating a new one.
- Existing keyword research or content plan already produced.
- Publishing method (Astro markdown via git, a CMS, an API) - read from PROJECT.md Architecture.
- Baseline performance: current indexed pages, clicks, impressions (from Search Console, not estimated).

## Category-specific discovery logic

Branch on the niche; do not use one generic questionnaire.

**Travel** - destinations/regions; audience (budget/luxury, solo/family); informational vs commercial;
seasonality by region; article categories; image sourcing.

**Finance / Health / Legal / YMYL** - require a named expert author or reviewer with verifiable
credentials; stricter source requirements (government, academic, official); a mandatory editorial review
gate; no unqualified first-person medical/financial claims; stronger disclosure. State these as
requirements during discovery.

**E-commerce / product review** - product data source and update cadence; live vs static price data;
affiliate disclosure; review authenticity; Product/Review schema needs.

**News / time-sensitive** - freshness and velocity requirements; prominent date stamps; crawl frequency.

**Multi-language / multi-country** - hreflang vs separate sites; translation quality bar; content owner.

## PROJECT.md (shared context)

One file at the repo root, git-committed, no secrets. Same schema as in
`seo-blog-website-development` references/project-discovery.md. Skill 01 writes Identity and Architecture;
this skill reads those to know URL structure, content schema, categories and publishing method, and writes
the SEO objectives section (target keywords/clusters, cadence, tracking workbook id, GSC/GA4 ids).

Reconcile against PROJECT.md before every planning action so the plan matches the actual site.
