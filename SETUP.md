# Setup Guide: From Scratch

Everything you need before the first line of a site exists, in the order you need it. Follow it top to bottom
once; after that, `scripts/preflight.sh` is the only check you need to re-run.

---

## 0. What you are actually setting up

Three separate things, often confused:

| Thing | What it is | Where it lives |
|---|---|---|
| **The skills** | Two `SKILL.md` packs that tell an agent how to build and grow a site | `~/.hermes/skills/` |
| **Your site** | One Astro repository per website you publish | its own Git repo |
| **The accounts** | GitHub, Cloudflare, Google Search Console, GA4, AdSense | external, one-time |

The skills repository is not your website. Keep them apart: one skills checkout can drive many sites, and
each site keeps its own `PROJECT.md`.

---

## 1. Prerequisites

### 1.1 The machine

| Requirement | Version | Why |
|---|---|---|
| **Node.js** | 22 or newer | Astro 5 and the `design-taste-frontend` inspector scripts require it |
| **npm** | Bundled with Node | Package install and build |
| **Python 3** | 3.8+ | The bundled scripts (`validate.py`, `check-keyword-uniqueness.py`) |
| **git** | Any recent | Version control, deploys, history |
| **Chrome, Chromium or Edge** | Current | The design inspector, axe accessibility runs and Lighthouse all drive a real browser |
| **OS** | Linux or macOS (Windows via WSL) | The preflight script is bash |

A working internet connection and roughly 1 GB free for `node_modules` per site.

### 1.2 Check it in one command

```bash
git clone https://github.com/PubuduDissanayaka/seo-blog-automation.git ~/seo-blog-automation
bash ~/seo-blog-automation/scripts/preflight.sh
```

It prints PASS, WARN or FAIL per item and exits non-zero on any FAIL. Warnings are optional gaps. Do not start
a build with FAIL lines outstanding.

### 1.3 Accounts, and when each one is actually needed

You do not need all of these on day one. This is the honest ordering.

| Account | Needed for | When | Cost |
|---|---|---|---|
| **GitHub** | The site repo, Actions, secrets, deploys | Before you build | Free |
| **Cloudflare** | Pages hosting, DNS, TLS, caching, WAF | Phase 6 (deploy) | Free tier covers a static content site |
| **A domain** | The site's address | Before the DNS cutover | Roughly 10 to 15 USD per year |
| **Google Search Console** | Indexing status, real queries, click and impression data | Straight after the first deploy | Free |
| **Google Analytics 4** | Behaviour: sessions, engagement, conversions | Straight after the first deploy | Free |
| **Google AdSense** | Advertising revenue | Only after roughly 20 to 30 strong articles are live | Free, revenue share |
| **Composio** (optional) | Cloudflare, GitHub, Google Sheets and Stitch actions without hand-rolled tokens | When you automate | Free tier, paid above it |
| **Google Stitch** (optional) | Design concepts in Phase 2 | Phase 2 | Free via Composio |
| **Google Sheets** (optional) | The 10-sheet SEO tracker | When growth starts | Free |
| **DataForSEO** (optional) | Search volumes, difficulty, SERP reads | Growth, once you need real numbers | Paid, cents per request |
| **Multica** (optional) | Running the work as a multi-agent team | When one agent is not enough | Varies |

Two things worth knowing before you plan:

- **AdSense is not a first-week task.** Google sets no minimum traffic or domain age, but the commonest
  rejection is low-value content. Apply with 20 to 30 genuinely useful articles, a real author, working
  privacy, terms, contact and an editorial policy. Approval is Google's decision and no skill can promise it.
- **Search Console cannot be skipped.** It is the only source of truth for what you already rank for, and it
  is free. Every "what should we write next" answer starts there.

### 1.4 Companion skills (a hard requirement)

The two skills deliberately name deeper skills instead of duplicating them. If a core companion is missing,
that handoff points at nothing and the workflow stalls at the worst moment.

**Core, required (14):**

`astro-static-site-build` · `cloudflare-pages-hosting` · `cloudflare-security-audit` ·
`google-stitch-concepts` · `ui-ux-pro-max` · `design-taste-frontend` · `modern-web-guidance` ·
`static-site-hardening` · `schema` · `site-brand-assets` · `adsense-monetization-readiness` ·
`seo-master` · `seo-content-pipeline-automation` · `ponytail`

**Optional, task-specific (14):**

`design-reference-research` · `inspo-mcp` · `awwwards-mcp` · `popular-web-designs` · `hallmark` ·
`frontend-ui-engineering` · `redesign-existing-projects` · `vanilla-static-site-build` ·
`dataforseo-api` · `find-keywords` · `build-clusters` · `keyword-clustering` · `competitor-analysis` ·
`competitive-landscape` · `beat-competitors` · `seo-content-qa` · `google-search-docs`

If any core skill is missing, install it before starting. They are free and widely available; several are
bundled with Hermes Agent.

---

## 2. Install the skills

```bash
git clone https://github.com/PubuduDissanayaka/seo-blog-automation.git
mkdir -p ~/.hermes/skills/seo
cp -r seo-blog-automation/seo-blog-website-development   ~/.hermes/skills/seo/
cp -r seo-blog-automation/seo-article-planning-schedule  ~/.hermes/skills/seo/
```

Verify the checkout is intact before trusting it:

```bash
cd seo-blog-automation && python3 scripts/validate.py
# PASS: both skills valid, all referenced files exist
```

Then confirm the whole environment:

```bash
bash scripts/preflight.sh
```

In Hermes Agent, load either skill by name:

```
skill_view(name='seo-blog-website-development')
skill_view(name='seo-article-planning-schedule')
```

Skills register at session start. If a skill does not appear, start a new session (`/reset` in the CLI,
`/restart` for the gateway) rather than assuming the copy failed.

---

## 3. Create the site (Skill 01)

### Step 1: a new repository for the site

One repo per website, separate from the skills repo:

```bash
mkdir my-site && cd my-site
git init -b main
```

### Step 2: run Skill 01 and let discovery fill `PROJECT.md`

Load the skill and state the goal. The first thing it does is discovery, not code. Expect grouped questions
about identity, niche and audience, monetisation, and your budget and capacity. It inspects what already
exists first, reuses anything on disk, and asks only what changes the plan.

```bash
cp ~/seo-blog-automation/seo-blog-website-development/templates/PROJECT.md .
```

Fill `PROJECT.md` from that template and commit it. Every later phase reads it, and Skill 02 depends on it
being honest about your categories, URL structure and publishing capacity.

### Step 3: phases 1 to 10

The skill runs architecture, design, implementation, technical SEO, performance and accessibility,
deployment, security, AdSense readiness, QA and maintenance. Two of those are hard gates worth knowing about
in advance:

- **Design (Phase 2) blocks implementation.** No markup is written before a direction and a token file exist.
  It needs a Chromium browser for the inspector, and optionally a Composio connection for Stitch concepts.
- **AdSense readiness (Phase 8) is evidence, not opinion.** It checks the live site, not your intentions.

### Step 4: what you must supply during the build

- The domain, and DNS access at cutover.
- Brand assets, or an explicit "no brand, choose a direction".
- Real content facts: names, prices, timetables. The skill will not invent them.

---

## 4. Wire the accounts

### Cloudflare Pages

Create the project **Git-connected** so every push builds. Framework preset None, output directory `dist`.
Set `PUBLIC_*` values as build environment variables, because Astro inlines them at build time and a missing
one fails silently.

Put the gates in the build command so a broken commit cannot ship:

```
npm ci && npm run check && npm test && npm run build
```

### Search Console

Verify ownership with the **meta tag** method, not an HTML file. Cloudflare Pages canonicalises `.html`
paths, so a file-based token answers a 308 and a verifier that does not follow redirects fails you while the
file is demonstrably correct. Submit the **sitemap index**, never a numbered child.

### Analytics

GA4, measurement-only by default, loaded after the load event rather than blocking first paint, and gated on
a production build so it never fires in local preview. Update the privacy page in the same commit that adds
the tag, or the page becomes a false statement.

### AdSense

Apply once the content exists, not before. A Google-certified CMP with IAB TCF is required before serving ads
to EEA, UK or Swiss visitors. Publish `ads.txt` after approval.

---

## 5. Start growing (Skill 02)

Load `seo-article-planning-schedule`. It reads `PROJECT.md` so it plans against the site you actually built.

1. **Research.** Niche validation, competitors, keyword research. Real numbers only, each with source, date
   and confidence.
2. **Structure.** Clusters and a topical map, with a weighted priority score.
3. **Briefs.** One per article from `templates/article-brief.md`, before any prose.
4. **Write and gate.** Two-step (gated outline, then prose), then mechanical gates plus the RankMath 95+
   score.
5. **Publish.** Automated on a pass; `held` on a fail.
6. **Track.** The 10-sheet workbook. Inspect an existing one before creating a new one.
7. **Monitor and refresh.** Search Console and GA4, kept separate, feeding a refresh queue and a monthly
   report from `templates/monthly-report.md`.

Guard the keyword map as you go:

```bash
python3 ~/seo-blog-automation/seo-article-planning-schedule/scripts/check-keyword-uniqueness.py \
  --map keywords.json --sitemap https://your-domain.com/sitemap-index.xml
```

It enforces one primary keyword per URL, exactly five secondaries each, and no primary reused as another
article's secondary.

---

## 6. Verify the whole setup

Run this once end to end. Every line should be true before you call the environment ready.

- [ ] `python3 scripts/validate.py` passes
- [ ] `bash scripts/preflight.sh` exits 0 with no FAIL
- [ ] Both skills load in a new session
- [ ] The site's `PROJECT.md` exists, is committed, and contains no secrets
- [ ] A design direction artifact and `design/tokens.json` are committed before any markup
- [ ] The build is green AND the routes render in a real browser at 1280 and 390
- [ ] The production host answers, with security headers, on the custom domain
- [ ] Search Console shows the sitemap accepted
- [ ] A GA4 `collect` request returns 204 on a real visit
- [ ] `robots.txt` and the sitemap it names both return 200
- [ ] A `curl` with a Googlebot user agent is not blocked with 403
- [ ] The keyword map passes the uniqueness guard

---

## 7. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| A skill does not appear after copying | Skills load at session start | New session (`/reset`, or `/restart` for the gateway) |
| A skill names a companion that will not load | Companion not installed | Install the missing core skill, re-run preflight |
| `validate.py` reports a dangling reference | A file referenced from `SKILL.md` is missing | Restore the file or fix the reference, then re-validate |
| The design inspector fails to launch | No Chrome/Chromium, or a root/headless host | Install Chromium, or follow the inspector's host notes for `--no-sandbox` |
| Astro build fails on an unknown API | Node older than 22 | Upgrade Node |
| Analytics is missing in production | `PUBLIC_*` set only locally | Set it as a Pages build env var and assert it in the served HTML |
| A deployed page keeps old copy | Edge cache | Purge the zone after any header or copy change |
| Self-canonical plus noindex seems ignored | Rank Math strips the canonical from noindex pages | That is the plugin's behaviour, not a bug |
| RankMath gate never reaches 95 | Long-tail keyword with too few occurrences, or over-length title and meta | Count occurrences (7 to 10 for a long-tail), keep title at or under 60 and meta at or under 160 |

---

## 8. What it costs to run

**Free path:** GitHub, Cloudflare Pages (static requests are free and unlimited), Search Console, GA4, Google
Sheets, Stitch via Composio. A content blog with no server functions costs nothing but the domain.

**Paid only when you choose:** DataForSEO for volumes and SERP data (cents per batched request), Composio
above its free tier, and any AI model tokens.

The skills refuse to add paid infrastructure without naming why, the free alternative, and the expected
cost first.
