# Multi-Agent (Multica) Autopilot Architecture

Design specialised agents with clear responsibilities, but avoid unnecessary agent multiplication - one
agent may hold several compatible responsibilities when that is cheaper. Inspect the actual workspace
capabilities before assuming any are available.

## Website Development Department (Skill 01)

Project Manager · Requirements Analyst · Market Researcher · UI/UX Designer · Google Stitch Designer ·
Astro Architect · Frontend Developer · Technical SEO Engineer · Cloudflare Engineer · Security Auditor ·
DevOps Engineer · QA Engineer · Accessibility Reviewer.

## SEO Growth Department (Skill 02)

SEO Strategist · Competitor Researcher · Keyword Researcher · Search Intent Analyst · Topic Cluster
Architect · Content Planner · Article Brief Specialist · AI Article Writer · Fact Checker · Editorial
Reviewer · SEO Optimiser · Publishing Manager · Search Console Analyst · GA4 Analyst · Backlink
Researcher · Content Refresh Specialist · Reporting Analyst.

Each role has a defined input and output; handoffs are concise structured summaries, never full codebases
or raw research dumps.

## Autopilot workflows

Development: requirements collection · research · design planning · development tasks · code review ·
technical SEO audits · security audits · deployment · post-deployment verification.

SEO growth: keyword discovery · topic-cluster updates · calendar generation · article research ·
drafting · fact verification · editorial QA · RankMath gate · automated publishing · publishing verification · search
performance collection · monthly reporting · refresh recommendations.

## Autonomy levels (human approval gates)

- **L1**: research and recommendations only.
- **L2**: create drafts and proposed changes.
- **L3**: execute approved changes.
- **L4**: execute predefined low-risk automation independently.

Article publication is NOT approval-gated: it runs autonomously once the mechanical gates and the RankMath
95+ gate pass, with `held` items surfaced to a human. Require human approval only for: removal/consolidation
of indexed content, production infrastructure changes, destructive file operations, DNS modifications,
billing changes, security configuration changes, and changes that affect publisher policies. YMYL content
stays approval-gated. Never allow unrestricted autonomous execution beyond these boundaries.

## Automation reliability

- **Idempotency**: re-running a step must not duplicate articles, records or side effects.
- **Retry limits** with backoff; error handling that records the failure, not just the exception.
- **Duplicate prevention**: dedupe on slug, published URL and keyword before any write.
- **Execution logs**: every run writes to the Automation Execution Log (sheet 10) with start/end, agent,
  result, retry count, error details and a verification step.
- **Notifications**: failures and approval requests reach a human, not silently a queue.
- **State persistence and recovery**: a killed run resumes from the last checkpoint without redoing work.
- **Verification steps**: a claimed publish, write or deploy is verified against the live target before
  being reported as done. See `seo-content-pipeline-automation` for the queue/drain-verification rules.
