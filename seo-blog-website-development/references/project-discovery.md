# Project Discovery

Run this phase FIRST, before any architecture, design, code or content work. Never scaffold, generate
articles or create an editorial calendar before the discovery answers are saved to PROJECT.md.

## Inspection-first rules

1. Inspect existing project files before asking anything: a `PROJECT.md`, a `README.md`, an existing repo,
   a content folder, a previous context file, a Google Sheet the owner already maintains.
2. Reuse previously provided information. Never ask a question whose answer is already on disk.
3. Distinguish MANDATORY (blocking - the architecture or strategy materially changes without it) from
   OPTIONAL (safe to assume and document).
4. Ask multiple related questions in one organised batch, not one at a time.
5. Offer a recommended option first; provide plain-language examples for non-technical owners.
6. Assume sensible defaults for non-critical missing info, and record each assumption in PROJECT.md under
   an "Assumptions" section.
7. Ask for clarification only when a missing answer changes architecture or strategy. Do not pepper the
   owner with questions they cannot answer.
8. Save confirmed answers into PROJECT.md as they come; never overwrite an existing field without
   confirming a change.

## The questionnaire

### A. Website identity (both skills)

- Website name.
- Domain (existing, purchased, or to be chosen).
- New site or existing site (with URL, repo, hosting, CMS).
- Business or personal project.
- Website purpose (traffic -> AdSense, lead generation, authority building, brand).
- Brand identity: logo, colours, fonts, voice, any existing assets and where they live.
- Existing repository URL and branch.
- Existing hosting provider and any migration requirements.

### B. Niche and audience (both skills)

- Primary niche and AdSense content category.
- Primary target country; secondary countries.
- Target audience (who, what they need, their level of expertise).
- Primary language; additional languages and whether a true multi-language build is wanted.
- User search intent mix (informational / commercial / transactional).
- Main content categories (the top-level taxonomy).

### C. Monetisation (both skills)

- AdSense account status: none, applied, approved, or existing publisher account.
- Intended AdSense strategy and timeline (be realistic; never promise approval or income).
- Affiliate marketing, sponsored content, other revenue streams.
- Advertising and disclosure requirements by target region.

### D. Business and resource constraints (both skills)

- Development and monthly operating budget.
- Paid tools available vs preferred free tools.
- Available AI models, API subscriptions, integrations.
- Expected publishing frequency and editorial capacity (who edits, how fast).
- Long-term business objective (this drives the whole roadmap).

## Category-specific discovery logic

Do NOT use one generic questionnaire for every niche. Branch on the primary niche and ask the questions
that actually change the plan.

**Travel** - target destinations and regions; travel audience (budget vs luxury, solo vs family);
informational vs commercial searches (itineraries vs "tour" / "book" queries); seasonality by region;
intended article categories (guides, itineraries, comparison, cost); image sourcing (own photos vs licensed).

**Finance / Health / Legal / other YMYL** - introduce STRONGER safeguards up front: named expert author or
reviewer with verifiable credentials; stricter source requirements (government, academic, official); an
editorial review gate before publication; no first-person medical/financial claims without qualification;
stronger disclosure language. State these as requirements in discovery, not after writing begins.

**E-commerce / product review** - product data source and update cadence; whether prices/availability are
live or static; affiliate disclosure; review authenticity (real testing or aggregation); merchant/Product
schema needs.

**News / time-sensitive** - freshness requirements; publication velocity; whether date stamps must be
prominent; crawl frequency expectations.

**Multi-language / multi-country** - whether this is a true hreflang build or separate sites; translation
quality bar (human vs machine); who owns the translated content.

## PROJECT.md schema (the shared context file)

One file at the repo root, git-committed, no secrets. Both skills read and write it. Suggested structure;
adjust to the project but keep the section names stable so both skills find them.

```markdown
# PROJECT.md

## Identity
- name, domain, purpose, business/personal
- repo, branch, hosting, CMS/migration

## Niche and audience
- niche, adsense category, primary/secondary countries, audience, languages
- intent mix, main categories

## Monetisation
- adsense status, strategy, affiliate/sponsored, disclosures

## Constraints
- budgets, tools, models, publishing frequency, editorial capacity, objective

## Architecture (Skill 01 writes)
- stack, rendering, content model, URL structure, page set
- deploy target, env vars, analytics ids (public only), adsense publisher id (public only)

## SEO objectives (Skill 02 writes)
- target keywords/clusters, publishing cadence, tracking workbook id, GSC/GA4 property ids

## Decisions
- dated one-line decisions with rationale

## Assumptions
- every non-critical assumption made during discovery

## Pending
- open questions and who owns them
```

Never store credentials, API keys, service-account files or secrets here. Public publisher/analytics IDs
are fine; tokens are not.

## Handoff between the two skills

Skill 01 writes the Architecture and Identity sections; Skill 02 reads them to know the URL structure,
content schema, publishing method and technical limits before planning content. Skill 02 writes the SEO
objectives section; Skill 01 reads it to know categories, keyword mappings and publishing requirements
before changing templates or taxonomy. Both skills must reconcile against PROJECT.md before acting, so
they never operate on inconsistent assumptions.
