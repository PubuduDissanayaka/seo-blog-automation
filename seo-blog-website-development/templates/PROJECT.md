# PROJECT.md

Fill this in during discovery. Commit it at the repo root (no secrets). Both the build skill
(`seo-blog-website-development`) and the growth skill (`seo-article-planning-schedule`) read and write it.
Delete the italic guidance as you fill each field.

## Identity

- name: *website name*
- domain: *primary domain*
- purpose: *traffic -> AdSense | lead generation | authority | brand*
- type: *business | personal*
- repo: *github owner/repo, branch*
- hosting: *Cloudflare Pages | other*
- migration: *none | existing URL list + redirect plan*

## Niche and audience

- niche: *e.g. houseplants, travel, personal finance*
- adsense_category: *Google content category*
- primary_country: *ISO or name*
- secondary_countries: *list or none*
- audience: *who, their expertise level, what they need*
- languages: *primary + any additional*
- intent_mix: *informational / commercial / transactional*
- categories: *top-level taxonomy, one per line*

## Monetisation

- adsense_status: *none | applied | approved | existing publisher*
- strategy: *AdSense-first, timeline*
- other_revenue: *affiliate, sponsored, none*
- disclosures_required: *by region*

## Constraints

- dev_budget: *one-off*
- monthly_budget: *operating*
- paid_tools: *available paid tools*
- models_and_apis: *available AI models and API subscriptions*
- publishing_frequency: *target cadence*
- editorial_capacity: *who edits, how fast*
- objective: *long-term goal*

## Architecture *(Skill 01 writes)*

- stack: *Astro + TS + Tailwind + Cloudflare Pages*
- rendering: *SSG*
- content_model: *content collections, markdown/MDX*
- url_structure: *e.g. /blog/<slug>/ and /category/<name>/*
- page_set: *home, blog, category, article, author, about, contact, privacy, terms, 404*
- deploy: *git-connected Pages, branch*
- public_ids: *GA4 measurement id, AdSense publisher id (public only)*

## SEO objectives *(Skill 02 writes)*

- target_clusters: *pillar topics*
- cadence: *posts per week*
- tracking_workbook: *Google Sheets id or URL*
- gsc_property: *Search Console property*
- ga4_property: *GA4 property id*

## Decisions

- *YYYY-MM-DD - one-line decision + rationale*

## Assumptions

- *every non-critical assumption made during discovery*

## Pending

- *open question - owner*
