---
name: seo-article-planning-schedule
description: "Plan and run SEO growth for blogs: keywords to publishing."
version: 1.0.0
author: Pubudu Dissanayaka (DevTenent), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [seo, content-strategy, keyword-research, editorial, publishing, growth, adsense]
    related_skills: [seo-blog-website-development, seo-master, seo-content-pipeline-automation, adsense-monetization-readiness, dataforseo-api, find-keywords, build-clusters]
---

# SEO Article Planning, Scheduling and Overall SEO Growth

Operate a continuous SEO growth process for a blog: niche validation, competitor analysis, keyword
research, topical authority, article planning, editorial calendars, publishing schedules, content quality,
performance monitoring, content refreshes and long-term organic growth. This is a running system, not a
one-off list of keywords.

It does NOT build or host the website - that is `seo-blog-website-development`. The two share the
PROJECT.md context file, so this skill knows the site's URL structure, content schema and publishing
method before it plans anything.

Reference implementation to imitate: MyGreenyGarden (mygreenygarden.com) - Astro + Cloudflare Pages,
AdSense goal, human-edit-before-publish, Google Sheets tracking.

## When to Use

- "Plan the SEO for this site", "what should we write", "build an editorial calendar".
- Keyword research, competitor analysis, topic clusters, content strategy.
- Setting up the Google Sheets tracking workbook or the publishing pipeline.
- Monitoring rankings/traffic and deciding what to refresh, consolidate or prune.
- Monthly SEO reporting and 30/60/90-day roadmaps.

Do NOT use for:
- Building/deploying the site - load `seo-blog-website-development`.
- One-off keyword list with no strategy behind it - this skill refuses that and builds the process instead.

## Operating Principles (non-negotiable)

1. **Evidence over volume.** Never invent search volumes, keyword difficulty, CPC, traffic or revenue
   estimates. Record source, retrieval date and confidence for every research figure. Distinguish estimated
   data from real Search Console/GA4 data, and never mix them.
2. **Intent before content type.** Classify intent first; an informational keyword gets a guide, not a
   sales page. Investigate the SERP before assigning a keyword - understand what Google actually ranks.
3. **One intent, one page.** Never publish multiple articles targeting essentially the same search intent.
   Collapse keyword variants into query families before planning.
4. **Keyword uniqueness enforced.** Exactly 1 primary keyword per URL (never reused), exactly 5
   secondaries per article (each used once site-wide), and a primary can never be another article's
   secondary. Verify against the live site before publishing AND before planning the next piece.
5. **Never promise rankings or revenue.** State realistic, evidence-based targets; no guarantees.
6. **Automated publishing with programmatic gates.** Articles publish automatically once they pass the
   mechanical gates and the RankMath 95+ score gate - no human-approval step in the happy path. The gates,
   not a human eyeball, are what block bad content, and they run in the pipeline on every article. Human
   review is the exception path only: YMYL content, a `held` item, or a gate failure.
7. **Continuous, not stop-at-publish.** Tracking, decay detection and refresh are part of the loop, not an
   optional extra.

## Prerequisites and Tools

- **Reference skills to load and delegate to, not duplicate:** `seo-master` (SEO strategy, AEO/GEO,
  E-E-A-T, SERP analysis, RankMath thresholds), `seo-content-pipeline-automation` (pipeline architecture,
  keyword-uniqueness guards, article gates, cron jobs - the operational backbone),
  `adsense-monetization-readiness` (the money gate and policy risk),
  `dataforseo-api` (credit-aware keyword/SERP data - cache-first, batched),
  `find-keywords`, `keyword-clustering`, `build-clusters`, `competitor-analysis`, `competitive-landscape`,
  `brief`, `seo-content-qa`, `google-search-docs` (policy audits).
- **Composio** for Google Sheets, Google Drive, Search Console, GitHub where authorised. Discover with
  `composio search`, read schemas with `--get-schema`, verify connections with a real call.
- Official docs at execution time: Google Search Central, Search Console, GA4, AdSense policies.

## Shared Project Context (PROJECT.md)

Read PROJECT.md first, every activation. It carries the site's URL structure, content schema, categories
and publishing method (written by Skill 01), so this skill never plans against a wrong architecture. Write
back the SEO objectives, keyword mappings, cadence and tracking workbook id. Full schema:
`references/project-discovery.md`.

## Project Discovery (phase 0)

Collect or retrieve: website identity, niche and audience, monetisation, business and resource
constraints. Use `references/project-discovery.md`, including category-specific logic (YMYL finance/health
gets stronger expertise, source and editorial safeguards; travel gets destination/audience/season
questions). Inspect existing files and any existing Google Sheet first; never ask twice; assume and
document non-critical gaps. This skill is the current assignment only when actually running a site's SEO -
never block the two skills' own creation on these questions.

## Core Operating Loop

Run as a continuous cycle. Each stage has a completion criterion; a stage that fails its gate does not
advance.

1. **Niche validation** - demand, competition, audience, intent, commercial potential, production
   difficulty, monetisation, long-term expansion. Is the niche realistic for the resources? Details:
   `references/research.md`.
2. **Competitor analysis** - direct/indirect competitors, ranking pages, intent, depth, gaps, unique
   opportunities. Never copy; find gaps to fill with better original content. Details: `references/research.md`.
3. **Keyword research** - seeds to long-tail, questions, informational/commercial/transactional, local,
   seasonal, emerging, entity-based. Investigate SERPs; do not lean on third-party volumes alone; record
   source/date/confidence. Collapse variants to query families. Details: `references/research.md`.
4. **Intent classification and topical authority** - classify each keyword; build pillar + cluster
   architecture; maintain a topical map; find missing subjects and redundant articles. Details:
   `references/topical-authority-and-prioritization.md`.
5. **Content prioritisation** - a transparent, configurable score (relevance, intent, demand, competition,
   business value, authority value, effort, source availability, freshness, seasonality, existing coverage).
   Volume is never the only factor. Details: `references/topical-authority-and-prioritization.md`.
6. **Article briefs** - per-article: ID, title, keywords, intent, audience, region, purpose, questions,
   research, sources, structure, headings, internal links, external refs, images, metadata, schema, editorial
   and fact-checking requirements, honest word-count, priority. Details: `references/content-production.md`.
7. **Writing and editorial QA** - originality, accuracy, intent satisfaction, depth, E-E-A-T, readability;
   no fabricated stats, quotes, references or fake experience. A configurable scoring rubric with hard fail
   conditions that block publication. Details: `references/content-production.md`.
8. **Publishing calendar** - statuses for every article, practical 7/30/60/90-day and annual schedules,
   velocity policy. Details: `references/publishing-calendar.md`.
9. **Tracking** - the master Google Sheets workbook (10 sheets), kept in sync with the pipeline.
   Details: `references/google-sheets-tracker.md`.
10. **Performance monitoring and refresh** - Search Console and GA4 kept separate; content decay detection;
    refresh/consolidate/redirect decisions from evidence; monthly reporting; 30/60/90 roadmap.
    Details: `references/performance-monitoring.md`.

## Key Rules

- **Data hygiene**: mark every figure manual / estimated / API-retrieved; never overwrite manually
  maintained data with automated data.
- **No fake freshness**: never bump a publication date without substantive changes.
- **Velocity, not volume**: finite resource is intents, not production capacity; see the velocity policy in
  `references/publishing-calendar.md` and `adsense-monetization-readiness`.
- **RankMath 95+ gate**: every article is scored against the RankMath post-test checklist before automated
  publish; only a passing score publishes. See `references/rankmath-95-gate.md`.
- **Cache-first research**: never pay twice for the same data; batch volumes, one SERP per intent cluster.
- **Backlinks**: legitimate only (digital PR, original research, useful resources, relevant contributions).
  Never purchased links, PBNs, spam comments or mass guest posts.

## Google Sheets Master Tracker

One workbook per site, inspected before a new one is created (never create a duplicate). Ten sheets:
Dashboard, Content Master, Keyword Map, Topic Clusters, Editorial Calendar, Publishing Log, Performance
Snapshots, Content Refresh Queue, Technical SEO Issues, Automation Execution Log. Use batch operations, data
validation, freeze panes, conditional formatting, formula summaries, and consistent date formats. Full
column spec and implementation rules: `references/google-sheets-tracker.md`.

## Automation and Autonomy (Multica / multi-agent)

Autonomy levels: L1 research/recommendations · L2 draft/propose · L3 execute approved · L4 predefined
low-risk automation independently. Article publication is L4: it runs automatically once the article passes
the mechanical gates and the RankMath 95+ gate, with no human-approval step in the happy path. Human approval
is required only for: removal/consolidation of indexed content, production infra changes, destructive ops,
publisher-policy-affecting changes, and any article the gate sets to `held`. Agent roles and workflow details: `references/multica-autopilot.md`. Inspect the actual workspace
capabilities before assuming them.

## Token and Cost Optimisation (Ponytail)

Follow `ponytail`: smallest complete change. Cache research (TTL'd); dedupe across runs; send concise
structured handoffs, never full codebases or raw research dumps. Batch API requests; reuse connections;
targeted SEO checks instead of full crawls. Before paid tools: name why, the free alternative, expected
usage, cost, and get approval for recurring spend. Read only the reference the current stage needs.

## References

Load only the file the current stage needs:
- `references/project-discovery.md` - discovery questionnaire, category logic, PROJECT.md schema.
- `references/research.md` - niche validation, competitor analysis, keyword research, intent classification.
- `references/topical-authority-and-prioritization.md` - clusters, topical map, prioritisation scoring.
- `references/content-production.md` - article briefs, AI writing standards, editorial QA gate.
- `references/publishing-calendar.md` - statuses, schedules, publishing velocity policy.
- `references/google-sheets-tracker.md` - the 10-sheet workbook spec.
- `references/performance-monitoring.md` - GSC/GA4, decay and refresh, backlinks, reporting, roadmap.
- `references/multica-autopilot.md` - agent roles, workflows, autonomy levels, reliability.
- `references/rankmath-95-gate.md` - the programmatic RankMath 95+ scoring gate enforced before automated publish.
- `references/cron-schedule.md` - the weekly/monthly/quarterly cron jobs that run the loop.
- `references/gsc-ga4-integration.md` - Search Console and GA4 data access, kept separate.
- `references/step-by-step-runbook.md` - the operating loop as ordered steps.
- `templates/article-brief.md` - fillable per-article brief; `templates/monthly-report.md` - report skeleton.
- `scripts/check-keyword-uniqueness.py` - the 1-primary + 5-secondary uniqueness guard.

## Verification

- [ ] PROJECT.md read and reconciled before planning
- [ ] every research figure carries source + retrieval date + confidence; estimated vs actual data separated
- [ ] keyword uniqueness guards asserted (primaries unique, secondaries unique, no primary-as-secondary)
- [ ] every article has a brief and a status in the tracker
- [ ] editorial QA gate run; any hard-fail condition blocks publication
- [ ] tracking workbook inspected before create; no duplicate sheets; manual vs automated data distinguished
- [ ] published URLs verified live and in the sitemap before being logged as published
- [ ] monthly report compares equivalent periods and separates GSC from GA4
- [ ] no ranking or revenue guarantees made anywhere
