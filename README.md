# SEO Blog Automation

**Two production-ready AI agent skills that take a blog from empty repository to compounding organic traffic.**

![License](https://img.shields.io/badge/license-MIT-2563eb)
![Skills](https://img.shields.io/badge/skills-2-0f766e)
![References](https://img.shields.io/badge/deep--dive%20references-21-7c3aed)
![Publish gate](https://img.shields.io/badge/publish%20gate-RankMath%2095%2B-d97706)

Give either skill to a capable agent (Hermes Agent, Claude Code, Codex, a multi-agent workspace) and it arrives with the decisions, workflows, quality gates and reference material already in place. No re-briefing, no improvised architecture, no checklist theatre.

The defaults are distilled from building and running a live AdSense travel publication on Astro and Cloudflare Pages, not from a blog post about SEO.

---

## The two skills

| | Skill | Owns |
|:--|:--|:--|
| **01** | [`seo-blog-website-development`](seo-blog-website-development/SKILL.md) | **Building the asset.** Discovery, architecture, Stitch design, Astro implementation, technical SEO, performance, accessibility, security audit, Cloudflare deployment, AdSense readiness, QA, maintenance. |
| **02** | [`seo-article-planning-schedule`](seo-article-planning-schedule/SKILL.md) | **Growing the asset.** Niche validation, competitor and keyword research, topical authority, briefs, editorial QA, automated publishing, the Google Sheets tracker, performance monitoring, content refresh, reporting. |

Zero overlap. Each skill is independently executable. Together they cover a blog's entire life.

---

## Start here

```bash
git clone https://github.com/PubuduDissanayaka/seo-blog-automation.git
cp -r seo-blog-automation/seo-blog-website-development    ~/.hermes/skills/seo/
cp -r seo-blog-automation/seo-article-planning-schedule   ~/.hermes/skills/seo/
```

Then load either one:

```
skill_view(name='seo-blog-website-development')
skill_view(name='seo-article-planning-schedule')
```

Both begin with **discovery, not code**. The skill inspects the repository, reads any existing project context, and asks only the questions whose answers change the plan. It never asks the same thing twice.

Validate the checkout at any time:

```bash
python3 scripts/validate.py
# PASS: both skills valid, all referenced files exist
```

---

## Design principles

**Design is a gate, not a phase.** No markup is written before a direction and a token file exist, and no
deploy happens before the design gates pass. Palette, inspector, type, contrast and axe are measured in a
real browser. Design is wired to a real stack rather than improvised: Stitch for the concept, `ui-ux-pro-max`
for the system, `design-taste-frontend` for art direction and the anti-slop gates.

**Static-first.** Static generation is the default for content publishing. Server rendering, Workers, databases and dynamic code appear only when a real requirement forces them, and the skill records which requirement in the project file. Nobody adds a database because they can.

**Progressive disclosure.** Each `SKILL.md` carries the decisions, rules and gates. The 21 reference files hold the depth, loaded only when the current phase needs them. You pay for the phase you are in, not the whole library.

**Verified, never asserted.** A green `npm run build` proves nothing about rendering, indexability or schema. Every gate in these skills inspects the built output, the live host, or a real API response. "Deployed" means the production host answered, not that the local build passed.

**No invented data.** Search volumes, difficulty scores and traffic estimates are never fabricated. Every research figure carries its source, retrieval date and confidence, and estimated third-party data is never blended with real Search Console or GA4 numbers.

**Automated publishing with real gates.** Articles publish without a human approval step once they clear the mechanical gates and a RankMath 95+ score. The gates block bad content, not a reviewer's calendar. Human review is the exception path for YMYL content and gate failures.

**One shared project file.** Both skills read and write a single `PROJECT.md`. The build skill records the architecture; the growth skill records the strategy. Neither operates on assumptions the other would contradict.

---

## Repository layout

```
seo-blog-automation/
├── scripts/
│   └── validate.py                          frontmatter + dangling-reference validator
│
├── seo-blog-website-development/
│   ├── SKILL.md                             phases, decision rules, quality gates
│   ├── templates/
│   │   └── PROJECT.md                       shared project-context skeleton
│   └── references/                          9 deep dives
│       ├── ui-ux-design.md                  design-first: skill stack, 10-step run, design gates, slop rules
│       ├── design-and-accessibility.md      token layer, WCAG 2.2 implementation
│       ├── project-discovery.md             questionnaire + category logic (YMYL, travel, commerce)
│       ├── architecture-and-astro.md        stack choice, content collections, URL + page architecture
│       ├── technical-seo.md                 crawl, index, metadata, schema, internal links, hreflang
│       ├── heading-hierarchy-verification.md one H1, no skipped levels, checked in built HTML
│       ├── cloudflare-github-security.md    Pages deploy, DNS, headers, GitHub workflow, security audit
│       ├── adsense-analytics-qa-maintenance.md  monetisation gate, analytics, QA checklists, upkeep
│       └── runbook.md                       ordered commands for a new build and an existing-site audit
│
└── seo-article-planning-schedule/
    ├── SKILL.md                             operating loop, rules, publish gate
    ├── templates/
    │   ├── article-brief.md                 21-field brief, filled before any prose
    │   └── monthly-report.md                report skeleton with data-hygiene prompts
    ├── scripts/
    │   └── check-keyword-uniqueness.py      the 1-primary + 5-secondary guard, tested
    └── references/                          12 deep dives
        ├── project-discovery.md             shared discovery, SEO-specific intake
        ├── research.md                      niche, competitor, keyword, intent classification
        ├── topical-authority-and-prioritization.md  clusters, topical map, weighted scoring
        ├── content-production.md            briefs, writing standards, editorial QA gate
        ├── rankmath-95-gate.md              the 28-check scoring gate, thresholds and pitfalls
        ├── publishing-calendar.md           statuses, schedules, velocity policy
        ├── cron-schedule.md                 weekly / monthly / quarterly automation jobs
        ├── google-sheets-tracker.md         the 10-sheet workbook specification
        ├── performance-monitoring.md        decay, refresh, backlinks, reporting, roadmap
        ├── gsc-ga4-integration.md           Search Console vs GA4, kept separate
        ├── step-by-step-runbook.md          the operating loop as ordered steps
        └── multica-autopilot.md             agent roles, autonomy levels, reliability
```

---

## Skill 01: from nothing to production

Ten phases, each with a completion criterion that is checked rather than assumed.

| Phase | Output |
|:--|:--|
| Discovery | Populated `PROJECT.md`, all assumptions recorded |
| Architecture | Stack, rendering strategy, URL structure, page set, cost estimate |
| Design | Committed direction artifact and tokens, palette and inspector gates green |
| Implementation | Astro build with typed content collections and strict schemas |
| Technical SEO | Crawl, index, canonical, metadata, schema, internal links |
| Performance and accessibility | Core Web Vitals budget met, axe clean per route |
| Deployment | Cloudflare Pages live on the custom domain, rollback recorded |
| Security | Audit findings, remediation verified or honestly flagged |
| Monetisation | AdSense readiness evidenced against the live site |
| Handover | Architecture recorded for the growth skill to read |

Runs two scenarios end to end: a new site from scratch, and a technical SEO audit of an existing site that must not be rebuilt. See [`references/runbook.md`](seo-blog-website-development/references/runbook.md).

---

## Skill 02: from publish to compound

A continuous operating loop, not a keyword list.

```
discovery -> niche -> competitors -> keywords -> intent
    -> clusters -> prioritise -> brief -> write -> gate
    -> publish (automated) -> track -> monitor -> refresh
```

| Stage | What it produces |
|:--|:--|
| Research | Query families collapsed from raw keyword dumps, SERP-checked, sourced |
| Topical authority | Pillar and cluster map with gap detection and cannibalisation guards |
| Prioritisation | Weighted score across demand, business value, effort and coverage |
| Briefs | 21 fields fixed before writing, including link and schema plans |
| Production | Two-step: gated outline, then prose |
| Publish gate | Mechanical checks plus RankMath 95+, then automatic publication |
| Tracking | 10-sheet workbook, manual vs estimated vs API data kept distinct |
| Growth | Decay detection, refresh queue, monthly report, 30/60/90 roadmap |

---

## The publish gate

Every article is scored before it goes live. A pass publishes automatically. A fail sets the item to `held`, triggers a fix pass, and re-gates.

The gate implements the full RankMath post-test checklist across four categories, with the numeric thresholds that actually move the score:

- **Basic SEO.** Keyword in title, meta, slug, first 100 words, 3 to 5 body mentions, 2,500+ words.
- **Additional SEO.** All 6 keywords in headings, image alt text, density 1 to 1.5 percent, internal and external links, site-wide uniqueness.
- **Title readability.** 45 to 55 characters, a number, a power word, keyword in the first 50 characters.
- **Content readability.** Paragraph and sentence limits, transition words, passive voice under 10 percent, Flesch 55+.

Full specification and the hard pitfalls that silently cost points: [`rankmath-95-gate.md`](seo-article-planning-schedule/references/rankmath-95-gate.md).

---

## Bundled tooling

| Artifact | Purpose |
|:--|:--|
| `scripts/validate.py` | Validates both skills and every referenced file. Stdlib only, runs on a fresh clone. |
| `templates/PROJECT.md` | The shared context skeleton both skills depend on. |
| `templates/article-brief.md` | 21-field brief. Filled before any draft exists. |
| `templates/monthly-report.md` | Report skeleton that forces period comparison and data labelling. |
| `scripts/check-keyword-uniqueness.py` | Enforces 1 primary per URL, 5 secondaries each, no primary reused as a secondary. Order-independent, optionally checks a live sitemap. |

```bash
python3 seo-article-planning-schedule/scripts/check-keyword-uniqueness.py \
  --map keywords.json --sitemap https://example.com/sitemap-index.xml
```

---

## Compatibility

These are plain `SKILL.md` packs with YAML frontmatter, so they load anywhere that indexes skills by directory. They were built for and tested with Hermes Agent.

Reference skills are named rather than duplicated: where a deeper skill exists on the host (Astro builds, Cloudflare Pages, security auditing, Stitch design, structured data), these skills hand off to it instead of restating it.

---

## Licence

MIT. Use them, fork them, adapt them to another stack.
