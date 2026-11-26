# Publishing Calendar and Velocity

## Article statuses (every article has one)

Use this status set; never leave an article statusless:

Idea · Research Pending · Researching · Brief Ready · Drafting · Fact Checking · Editing · SEO Review ·
Approval Required · Approved · Scheduled · Published · Performance Monitoring · Refresh Required · Archived.

A status change is a tracker write, not a chat message. Keep the tracker and the pipeline queue in sync
(the tracker is derived from the same gate the build enforces - see `seo-content-pipeline-automation`).

## Scheduling

Build practical schedules from real capacity, not arbitrary quotas:

- **7-day plan**: the concrete next actions (which articles, which stage each is at).
- **30-day calendar**: articles to publish this month, with dates and assigned work.
- **60-day plan**: the next two months' pipeline with dependencies.
- **90-day roadmap**: quarterly objectives, activities, deliverables, KPIs, risks.
- **Annual strategy**: editorial themes, cluster completion, seasonal coverage.

Consider publishing frequency, available writers, research and editorial capacity, content dependencies,
seasonal demand, topical clusters and consistency. Schedule seasonal content ~8 weeks before its peak.

## Publishing velocity (policy, not preference)

Volume is not itself a violation; thin pages manufactured at speed are. Follow
`adsense-monetization-readiness` and `seo-content-pipeline-automation`:

- 3-5 per week before AdSense approval (approval needs ~20-30 strong articles).
- ~2 per day after approval, and only while indexation holds above ~80%.
- 3-4 per day only with a real data-driven page layer and an editor who can reject work.
- Halt publishing when indexed/published drops below ~70%.
- 1-2 posts/week is the safe steady state for most AdSense sites; 20-30% of monthly effort goes to
  refreshing existing articles, not adding URLs.

The finite resource is intents, not production capacity. The honest ceiling for a single topic in one
language is far lower than the raw keyword count.

## Publish verification

After publishing, do not log "published" on trust: verify the live URL returns 200, appears in the sitemap,
and (after the deploy) report indexing status honestly - "accepted for crawling" is not "indexed". Submit
via IndexNow after the deploy (fetch the key file first and refuse if it 404s or differs). Keep Search
Console metrics separate from GA4 metrics in all reporting.
