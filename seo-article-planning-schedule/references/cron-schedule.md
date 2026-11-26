# Cron Schedule (recurring jobs)

Run these with `cronjob_manage`. Deliver to a messaging platform (e.g. `telegram:<chat_id>`), never
`origin` - cron output is not delivered back into a CLI session. Set `workdir=<project>` and
`continuity=true` so each run sees the previous run's output and can dedupe. Write PUBLISH MODE, spend caps
and the queue path as literal lines in the job prompt - a run cannot ask questions.

## Weekly - article production + auto-publish

Take the next `pending` queue item, produce it two-step (outline then prose), run the mechanical gates and
the RankMath 95+ gate, and auto-publish on a pass. On a fail, set `held` with a reason and report it - never
publish a failing article. Enforce the keyword-uniqueness guard (`scripts/check-keyword-uniqueness.py`)
before writing. Spend cap per run.

## Monthly - refresh + rank snapshot

Pull the latest ranking/traffic snapshot, detect decay, update 1-3 ageing posts, re-run the cannibalisation
check. Refresh is from evidence; never bump a publication date without substantive change.

## Quarterly - re-plan

Fresh volumes/discovery, re-cluster, extend the spec, rebuild the queue and keyword map. Idempotent against
production state - never reset published rows to pending.

## Monthly / quarterly - maintenance (Skill 01)

Dependency updates (audited), security review, broken-link sweep, sitemap + robots check, crawlability
check, analytics verification. Quarterly: performance review, AdSense policy re-read, template improvements.

## Reliability rules for every job

Idempotent steps, retry with backoff, dedupe on slug/URL/keyword, log to the Automation Execution Log
(sheet 10), notify on failure, resume from checkpoint, and verify any publish/write against the live target
before reporting it done.
