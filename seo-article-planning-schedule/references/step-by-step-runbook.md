# Step-by-Step Runbook (Skill 02)

The continuous operating loop, as concrete steps. Each step references the detail file it depends on.

1. **Discovery.** Fill or read `templates/PROJECT.md` (schema in `references/project-discovery.md`).
2. **Niche validation.** Is the niche realistic for the resources? (`references/research.md`).
3. **Competitor analysis.** Direct/indirect competitors, ranking pages, gaps, unique opportunities
   (`references/research.md`, `seo-master`).
4. **Keyword research.** Seeds -> expansion -> collapse to query families -> SERP-check -> score
   (`references/research.md`). Record source, retrieval date, confidence on every figure.
5. **Intent + clusters.** Classify each keyword; build the pillar + cluster topical map
   (`references/topical-authority-and-prioritization.md`).
6. **Prioritise.** Score every candidate with the weighted rubric; volume is one factor, not the only one
   (`references/topical-authority-and-prioritization.md`).
7. **Brief.** Fill `templates/article-brief.md` for each article before any prose.
8. **Write.** Two-step: outline first (gated), then prose. Follow `seo-master` E-E-A-T / AEO direct-answer
   structure and `seo-content-pipeline-automation` for the structure-variation ledger
   (`references/content-production.md`).
9. **Gate.** Run the mechanical gates and the RankMath 95+ score gate (`references/rankmath-95-gate.md`);
   a pass auto-publishes, a fail auto-holds for a fix pass.
10. **Publish + verify.** Publish, then verify the live URL 200 + in the sitemap; IndexNow after deploy
    (`references/publishing-calendar.md`).
11. **Track.** Update the Google Sheets workbook (10 sheets, `references/google-sheets-tracker.md`) and the
    pipeline queue; mark manual vs estimated vs API-retrieved data.
12. **Monitor + refresh.** GSC/GA4 monitoring, decay detection, refresh/consolidate/redirect from evidence
    (`references/performance-monitoring.md`, `references/gsc-ga4-integration.md`).
13. **Report + roadmap.** Monthly report (`templates/monthly-report.md`) and the 30/60/90 roadmap
    (`references/performance-monitoring.md`).
14. **Automate.** Wire the weekly/monthly/quarterly cron jobs (`references/cron-schedule.md`).
