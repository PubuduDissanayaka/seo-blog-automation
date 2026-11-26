# SEO Blog Automation Skills

Two reusable Hermes Agent skills for building and growing AdSense-ready SEO blog websites.
Reference implementation: **MyGreenyGarden** (mygreenygarden.com) - Astro + Cloudflare Pages,
git-connected, human-edit-before-publish, Google Sheets tracking.

## The two skills

| Skill | Purpose |
|---|---|
| `seo-blog-website-development` | End-to-end discovery, architecture, Stitch design, Astro build, technical SEO, performance, accessibility, security, Cloudflare deployment, GitHub workflow, AdSense readiness, QA and maintenance. |
| `seo-article-planning-schedule` | Continuous SEO growth: niche validation, competitor and keyword research, topical authority, article planning, editorial QA, publishing calendars, the Google Sheets tracker, performance monitoring and content refresh. |

Each skill is independently executable. They interoperate through a shared `PROJECT.md` context file.

## Structure

```
seo-blog-automation/
├── README.md
├── seo-blog-website-development/
│   ├── SKILL.md
│   └── references/          (6 files: discovery, architecture, technical-seo,
│                             design, cloudflare-github-security, adsense-qa)
└── seo-article-planning-schedule/
    ├── SKILL.md
    └── references/          (8 files: discovery, research, topical-authority,
                              content-production, publishing-calendar,
                              google-sheets-tracker, performance-monitoring,
                              multica-autopilot)
```

Each `SKILL.md` holds the operating principles, decision rules, workflows and quality gates.
Deep procedural detail lives in `references/`, loaded only when the current phase needs it
(progressive disclosure - keeps token cost down).

## Shared conventions

- **PROJECT.md** - one git-committed context file at the repo root of every site, no secrets.
  Skill 01 writes Identity and Architecture; Skill 02 writes SEO objectives. Both reconcile
  against it before acting.
- **Discovery first** - both skills start with an inspection-first questionnaire with
  category-specific logic (YMYL gets stronger expertise/source/review gates; travel gets
  destination/season questions).
- **Keyword uniqueness** - 1 primary keyword per URL (never reused), 5 secondaries per article,
  a primary is never another article's secondary.
- **Human review is a publish gate** - AI writes drafts; publication defaults to approval-required.
- **No guarantees** - neither skill promises AdSense approval, rankings or revenue.

## Installing into Hermes

Copy each skill directory into the Hermes skills directory:

```bash
cp -r seo-blog-website-development ~/.hermes/skills/seo/
cp -r seo-article-planning-schedule ~/.hermes/skills/seo/
```

Then the skills are loadable via `skill_view` in a new session.

## Design decisions

- Static-first (Astro SSG); Serverless/Workers/databases only when a real requirement forces them.
- Cloudflare Pages (git-connected) as the default host; free tier unless requirements escalate.
- Progressive disclosure; Ponytail ("smallest complete change") for cost and token efficiency.
- Data hygiene: every research figure carries source, retrieval date and confidence; estimated
  third-party data is never mixed with real Search Console/GA4 data.
