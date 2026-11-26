---
name: seo-blog-website-development
description: "Build SEO blog websites on Astro, Cloudflare, AdSense-ready."
version: 1.0.0
author: Pubudu Dissanayaka (DevTenent), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [seo, astro, cloudflare, blog, technical-seo, adsense, deployment]
    related_skills: [seo-article-planning-schedule, astro-static-site-build, cloudflare-pages-hosting, cloudflare-security-audit, google-stitch-concepts, adsense-monetization-readiness]
---

# SEO Blog Website Development

Build a complete, professional, SEO-optimised, performant, secure, responsive and monetisation-ready blog
website, end to end: discovery, architecture, design, Astro implementation, technical SEO, performance,
accessibility, security, Cloudflare deployment, GitHub workflow, QA and ongoing maintenance.

It does NOT do SEO growth after launch (keyword research, article planning, publishing cadence, ranking
monitoring) - that is the `seo-article-planning-schedule` skill. The two share a project context convention
(see below) so a site built here is immediately operable by the growth skill.

Default stack, unless discovery justifies otherwise: Astro (static output), TypeScript, content collections
(markdown/MDX), Tailwind, Cloudflare Pages (git-connected), GitHub. Reference implementation to imitate:
MyGreenyGarden (mygreenygarden.com) - Astro + Cloudflare Pages, AdSense goal, human-edit-before-publish.

## When to Use

- "Build me a blog / content site that ranks" - new site from scratch.
- Extending or re-platforming an existing blog (Astro or migration target).
- Making an existing site AdSense-ready or fixing its technical SEO.
- A site must be fast, indexable, accessible and cheap to run long-term.

Do NOT use for:
- SEO strategy, keyword research, article writing, editorial calendars - load
  `seo-article-planning-schedule` instead.
- A one-page tool or link hub with no build step - use `vanilla-static-site-build`.
- WordPress sites - use the `wordpress-*` skills.

## Operating Principles (non-negotiable)

1. **Static-first.** Static generation is the default for content publishing. SSR, Workers, databases or
dynamic code only when a real requirement forces them. Never introduce a database "because you can".
2. **Discovery before code.** Never scaffold, design or build until the discovery questionnaire is answered
and saved. Never overwrite existing project work without checking it first.
3. **Never hallucinate capabilities.** Do not invent Cloudflare/Composio/Stitch/AdSense features, API
endpoints, or integration availability. Verify against the actual tool schema or official docs before relying
on it.
4. **Secrets never touch source or context files.** API keys, tokens, publisher IDs, service-account
credentials live in GitHub Secrets / Cloudflare env vars / a local env file that is git-ignored. Never in
`PROJECT.md`, never committed.
5. **Verification over green builds.** A passing `npm run build` proves nothing about rendering, SEO or
indexability. Every gate below checks the BUILT or LIVE output, not the source.
6. **Never guarantee AdSense approval or income.** State policy requirements and readiness checks; approval is
Google's decision.
7. **Least privilege and no destructive action without approval.** Security config changes, DNS changes,
billing, infra changes are approval-gated (see Autonomy).
8. **Genuine user value beats technical tricks.** Readability, navigation and search intent over keyword
manipulation, artificial internal links or misleading schema.

## Prerequisites and Tools

- **Reference skills to load and delegate to, not duplicate:** `astro-static-site-build` (Astro + content
collections + tokens + verification templates), `cloudflare-pages-hosting` (Pages deploy, cutover, DNS,
`_headers`/`_redirects`), `cloudflare-security-audit` (security audit workflow), `google-stitch-concepts`
(Stitch design workflow), `modern-web-guidance` (native platform patterns - run its `search`/`retrieve`
before writing HTML/CSS/client JS), `static-site-hardening` (headers), `schema` (structured data),
`site-brand-assets` (logo/favicon/brand).
- **Composio** for Cloudflare, GitHub, Google Sheets/Drive integrations where authorised. Discover with
`composio search`, read schemas with `--get-schema`, never assume a connection exists (verify with a real
call).
- **Google Stitch** (optional design tool) via the `google-stitch-concepts` skill and Composio.
- Official docs to consult at execution time (never from memory): Astro docs, Google Search Central, Chrome
Modern Web Guidance, Cloudflare docs, GitHub docs, AdSense publisher policies.

## Shared Project Context (PROJECT.md)

Both skills read and write one project context file: `PROJECT.md` at the repo root (git-committed, no
secrets). This is the single source of truth for identity, niche, audience, monetisation, architecture and
SEO objectives. Full schema and the discovery questionnaire that fills it:
`references/project-discovery.md`.

Rules: inspect it first on every activation; reuse what is already there; never overwrite without checking;
save confirmed answers into it as you go; document assumptions explicitly when you make them.

## Project Discovery (phase 0)

Before ANY other work, collect or retrieve: website identity, niche and audience, monetisation, business and
resource constraints. Use the questionnaire in `references/project-discovery.md`, which includes
category-specific logic (YMYL finance/health gets stronger expertise and source requirements; travel gets
destination/audience/season questions). Rules: inspect existing files first, never ask twice, separate
mandatory from optional, offer recommendations, assume only non-critical missing info (and document it), and
ask only when a missing answer changes architecture or strategy. This skill is the current assignment only
when actually building a site - never block the two skills' own creation on these questions.

## Core Workflow

Run phases in order. Each has a completion criterion; do not skip a phase's verification.

**Phase 1 - Architecture and technical plan.** Evaluate requirements, recommend tech, pick rendering
strategy, plan site architecture, navigation, categories, URL structure, templates, components, design
system, SEO architecture, deployment, infra cost estimate. Decision rules and the page-architecture and URL
conventions: `references/architecture-and-astro.md`. Output: decisions recorded in PROJECT.md, a written
architecture summary. Completion: every architectural decision has an explicit, justified answer.

**Phase 2 - Design and design system (Stitch-first).** Per `google-stitch-concepts` and the standing rule:
user-visible UI goes through Google Stitch first. Brand -> niche research -> reference analysis -> visual
direction -> palette/type/spacing -> responsive layouts -> components -> accessibility/navigation review ->
convert to Astro components. Details: `references/design-and-accessibility.md`. Completion: committed Stitch
concept (PNG + HTML) with the palette audited to zero off-token colours.

**Phase 3 - Astro implementation.** Production coding standards, component/layout architecture, content
collections with strict schemas, reusable SEO components, nav/footer, responsive images, self-hosted fonts,
metadata, dynamic categories, related articles, breadcrumbs, pagination, search. Load `astro-static-site-build`
and follow it; it carries the pitfalls that ship blank pages (motion rules, `image()` schema, `getStaticPaths`
scoping, cache-clearing on plugin edits). Details: `references/architecture-and-astro.md`. Completion:
`astro check` passes, build is green, routes verified at 1280 and 390 in a real browser.

**Phase 4 - Technical SEO implementation.** robots.txt (generated from canonical origin), XML sitemap + index
with real `lastmod`, canonical URLs, meta robots, redirects, custom 404 with a real status, metadata (title,
description, OG, article:*), heading hierarchy, structured data (validate in built HTML), internal linking,
hreflang when multi-language. Full procedure and the schema eligibility rules: `references/technical-seo.md`.
Completion: crawlability and metadata checks in the built output all pass (see Quality Gates).

**Phase 5 - Performance and accessibility.** Core Web Vitals (LCP <= 2.5s, INP <= 200ms, CLS <= 0.1), modern
image formats, lazy loading, font optimisation, reduced client JS, caching/compression/CDN, mobile
performance. WCAG 2.2: semantic HTML, keyboard, contrast, focus, alt text, reduced motion. Run
`modern-web-guidance` for any HTML/CSS/JS pattern. Details: `references/design-and-accessibility.md`.
Completion: performance budget met (measured, not guessed) and axe reports zero serious/critical violations
per route.

**Phase 6 - Cloudflare deployment and GitHub workflow.** DNS/SSL, Pages vs Workers decision, caching,
`_headers`/`_redirects`, security settings, env vars, preview deploys, branch/commit/PR/Actions, secret
scanning, dependency auditing, deploy + rollback. Follow `cloudflare-pages-hosting` and `static-site-hardening`.
Details: `references/cloudflare-github-security.md`. Completion: production serves the verified build; cache
and header rules confirmed on the custom domain; rollback path written down.

**Phase 7 - Security audit.** Run `cloudflare-security-audit` (guidance mode for focused review, full mode when
a full audit is requested). Cover Cloudflare config, DNS, TLS, headers, WAF, bot protection, endpoints,
auth, rate limits, secrets, dependencies, GitHub config, deploy config. Never execute destructive remediation
without approval; recommend the smallest effective fix. Completion: findings recorded, remediation
verified or needs-validation stated honestly.

**Phase 8 - AdSense readiness and analytics.** Treat monetisation readiness as a dedicated objective. Load
`adsense-monetization-readiness` for policy requirements and the consent/CMP rules. Add GA4, Search Console,
Bing Webmaster Tools, with privacy-conscious, performance-aware tags. Details:
`references/adsense-analytics-qa-maintenance.md`. Completion: readiness checklist answered with evidence
against the live site; analytics hit verified (a real `collect` request, not the tag's presence).

**Phase 9 - QA, deploy, verify, hand over.** Run the predeploy and postdeploy checklists in
`references/adsense-analytics-qa-maintenance.md`. Never report success from a local build alone - verify the
live production host. Record the handover: what Skill 02 needs (categories, URL structure, publishing
method, content schema) is in PROJECT.md. Completion: full checklist green on production.

**Phase 10 - Maintenance (recurring).** Dependency updates, security audits, performance reviews, broken-link
and sitemap checks, crawlability checks, analytics verification, backup/restore testing. Schedule with
`cronjob_manage`; keep a running log. Completion: a dated maintenance log entry with results and any
follow-ups.

## Quality Gates (abridged; full checklist in references/adsense-analytics-qa-maintenance.md)

Predeploy: build success · every route renders · responsive at 1280/390 · no broken internal links · unique
titles/meta per page type · canonical correct · sitemap + robots valid · schema validates in built HTML ·
axe clean · performance budget met · analytics tag present in PROD only · redirects land on real pages.
Postdeploy (on the custom domain, not the preview URL): robots.txt and sitemap fetch 200 · one URL from each
URL family 200 · headers present (CSP/HSTS) · schema in served HTML · `curl` with a Googlebot UA not 403 ·
DNS cutover complete (no stale A/AAAA) · rollback recorded.

## Security Rules

Least privilege everywhere. Secrets only in GitHub Secrets / Cloudflare env vars / git-ignored local env.
Never commit a token. Inspect before modifying any existing repo. Never overwrite user work. Dependency
auditing and secret scanning in CI. For destructive or infra-changing actions, get approval first.

## Automation and Autonomy

Autonomy levels: L1 research/recommendations only · L2 draft/propose changes · L3 execute approved changes ·
L4 execute predefined low-risk automation independently. Require human approval for: production infra
changes, DNS modifications, billing, security config changes, destructive file ops. Agent roles (when run
under a multi-agent workspace like Multica): Project Manager, Requirements Analyst, UI/UX + Stitch Designer,
Astro/Frontend Developer, Technical SEO Engineer, Cloudflare Engineer, Security Auditor, QA. One agent may
hold several roles when that is cheaper. Inspect the actual workspace capabilities before assuming them.

## Token and Cost Optimisation (Ponytail)

Follow the `ponytail` skill: the smallest complete change; do not build what nobody asked for. Prefer free
services when reliable (Cloudflare Pages free tier, GitHub Actions). Before any paid tool: name why, the free
alternative, expected usage and cost, and get approval for recurring spend. Use progressive disclosure: read
only the reference file the current phase needs, never all of them. Reuse cached research and existing
authenticated connections. Do not re-crawl the whole site without a reason.

## References

Load only the file the current phase needs:
- `references/project-discovery.md` - full discovery questionnaire, category-specific logic, PROJECT.md schema.
- `references/architecture-and-astro.md` - tech evaluation, Astro architecture, content collections, page and URL architecture.
- `references/technical-seo.md` - crawling/indexing, metadata, structured data, internal linking, hreflang.
- `references/design-and-accessibility.md` - Stitch workflow, design system, WCAG 2.2.
- `references/cloudflare-github-security.md` - Cloudflare deploy, GitHub workflow, security audit integration.
- `references/adsense-analytics-qa-maintenance.md` - AdSense readiness, analytics, full QA checklists, maintenance.
- `references/runbook.md` - step-by-step commands for a new build and an existing-site audit.
- `templates/PROJECT.md` - the shared project-context skeleton; copy and fill during discovery.

## Verification

- [ ] PROJECT.md exists and records every discovery answer and architectural decision
- [ ] Stitch concept committed and on-palette before any markup
- [ ] Build green AND routes verified in a real browser at 1280 and 390
- [ ] robots.txt, sitemap, canonical, schema, unique metadata all verified in the BUILT or LIVE output
- [ ] axe clean; performance budget met with measured (not quoted) numbers
- [ ] Production host verified, not just the local build; rollback recorded
- [ ] No secrets in source, context files, or commits
- [ ] Handover data for `seo-article-planning-schedule` present in PROJECT.md
