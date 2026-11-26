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

## 3. Runtime and workspace

The skills are instructions; something has to run them. Three layers, only the first is required.

### 3.1 Hermes Agent (the runtime)

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
hermes setup      # pick provider, model, enter keys
hermes doctor     # health check
```

| Path | Holds | Rule |
|---|---|---|
| `~/.hermes/config.yaml` | Settings | Never secrets. Change it with `hermes config set KEY VAL`, never by hand: a stray indent corrupts the live gateway. |
| `~/.hermes/.env` | API keys and secrets ONLY | `chmod 600`, never committed, never synced. |
| `$HERMES_HOME/skills/` | Installed skills | Where these two go. |
| `~/.hermes/state.db` | Session store | Back it up. Never sync it between hosts. |
| `~/.hermes/profiles/<name>/` | Isolated instances | Resolve the home from `$HERMES_HOME`, never hardcode `~/.hermes`. |

Two install traps that cost hours on a fresh server:

- **`libatomic1` missing on minimal Ubuntu** makes every node binary fail, and the installer then reports a
  false *"Node.js is too old (requires >=26)"* and appears to hang. `apt-get install -y libatomic1`, re-run.
- **The real Node floor is 22.22.0, not 26.** A system Node at or above that passes and the installer skips
  its managed download entirely.
- A `browser (system dependency not met)` warning in `hermes doctor` is **expected** when the browser backend
  is `browser-use`. It is not a fault.

Skills load at session start. After installing a skill, start a new session (`/reset` in the CLI, `/restart`
for the gateway) before concluding the copy failed.

Optional surfaces worth knowing: `hermes dashboard` (web admin), `hermes desktop`, a messaging gateway
(Telegram, Discord, Slack) so jobs report into chat, and the cron scheduler for the recurring SEO work.

### 3.2 Multica (multi-agent workspace), optional

What it adds: issues as the unit of work, agents with their own model and skills, squads that route work,
autopilots on a schedule or webhook, and projects bound to a repository or local directory.

When these two skills benefit from it: once one agent can no longer hold build and growth at once, or when
you want the growth roles (writer, fact checker, editor, publishing manager) running as separate lanes with
approval gates.

**The auth model, and the trap that matters.** Agent runs execute as daemon tasks and receive a task-scoped
`mat_` token in the worker environment. That is the credential that writes as the agent. The CLI also holds a
workspace-owner token (`mul_`) in `$HOME/.multica/config.json`, and running `cd /root && multica ...` silently
falls back to it, at which point every comment is filed as the owner rather than the agent. That is an
integrity defect, not a cosmetic one: never use that fallback for anything written in an agent's voice.

If a task shell reports *"requires MULTICA_TOKEN to be a task-scoped mat_ token"*, the shell did not inherit
the worker environment. Recover it per invocation, never by exporting once:

```bash
bash ~/.hermes/skills/multica-platform/scripts/multica_task_env.sh multica issue list --output json
```

That helper resolves its config root by walking up from `$PWD`, so a stray `cd` into a project directory makes
it exit 97 with empty stdout. Return to the task workdir first.

**The `HERMES_HOME` trap, which will bite you exactly once.** Multica exports `HERMES_HOME` per task to a
task-scoped home. Any skill sync run from inside a task therefore mirrors the task-scoped tree instead of your
real one, and the sync reports `nothing changed` while your edit never travels. Always be explicit:

```bash
HERMES_HOME=/root/.hermes bash hermes-sync.sh push
```

To put these skills into a workspace, use the platform's own skill import (URL or local archive). Read
`multica-platform` references/skill-import.md for the current contract rather than guessing flags.

### 3.3 Keeping skills in sync across machines

If you work from more than one machine, converge on a **private git repo**, not ad-hoc copies.

- Sync: `skills/`, `memories/`, `config.yaml`, `SOUL.md`.
- Never sync: `.env`, `auth.json`, `state.db`, `sessions/`, `logs/`, `node/`, `cache/`, `cron/`.
- Push **before** pull. A pull-first script reverts edits you made but did not push, and the symptom is a file
  behaving like its previous version.
- Hold an edit lock (or use `rsync -u`) across any batch of edits, or the next scheduled pull can land inside
  your own change.

### 3.4 Composio and MCP integrations

- **Composio** for Cloudflare, GitHub, Google Sheets, Google Stitch and similar: `composio search`, read the
  schema with `--get-schema`, then `composio execute`. Verify a connection with a real call before building a
  plan on it; a listed connection can still be dead.
- **MCP servers** natively: `hermes mcp add <name> --command "..."` for stdio or `--url` for HTTP, and
  `hermes mcp install <name>` for the catalog. The OpenSEO MCP (projects, keyword data, SERP, Search Console)
  is what the growth skill's research and monitoring lean on.
- **Google** data: Search Console and GA4 through Composio where connected, or direct APIs. Keep the two
  sources separate in everything you report.

## 4. Create the site (Skill 01)

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

## 5. Wire the accounts

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

## 6. Start growing (Skill 02)

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

## 7. Verify the whole setup

Run this once end to end. Every line should be true before you call the environment ready.

- [ ] `python3 scripts/validate.py` passes
- [ ] `bash scripts/preflight.sh` exits 0 with no FAIL
- [ ] `hermes doctor` reports no unexplained failures (a `browser (system dependency not met)` warning is expected)
- [ ] `HERMES_HOME` points at your real home, not a task-scoped one, when you run a skill sync
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

## 8. Troubleshooting

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

## 9. What it costs to run

**Free path:** GitHub, Cloudflare Pages (static requests are free and unlimited), Search Console, GA4, Google
Sheets, Stitch via Composio. A content blog with no server functions costs nothing but the domain.

**Paid only when you choose:** DataForSEO for volumes and SERP data (cents per batched request), Composio
above its free tier, and any AI model tokens.

The skills refuse to add paid infrastructure without naming why, the free alternative, and the expected
cost first.
