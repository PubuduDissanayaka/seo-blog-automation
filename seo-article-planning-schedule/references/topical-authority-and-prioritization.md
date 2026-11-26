# Topical Authority and Prioritisation

## Topic clusters and topical authority

Build a pillar + cluster architecture; do not publish a flat list of unrelated articles.

- **Pillar topic**: the broad topic with a comprehensive page.
- **Supporting articles**: subtopics, each targeting its own primary keyword.
- **Subtopics and entity relationships**: map entities (people, places, concepts, products) that belong
  together and link them.
- **Content clusters**: groups of related articles that link to the pillar and each other.
- **Category architecture**: clusters map to the site's category taxonomy (from PROJECT.md).
- **Internal linking**: pillar links out to every cluster page; every cluster page links back to the
  pillar and 2-3 siblings.

Maintain a **topical map** (a table in the tracker): cluster id, pillar topic, category, supporting
subtopics, related keywords, planned vs published, missing coverage, cluster completion, internal-linking
progress. Identify missing subjects and redundant articles from this map, not from memory.

Rules: avoid publishing multiple articles that target essentially identical intent without a strategic
reason; collapse variants to one page per intent; a pillar may MENTION child topics in body text but never
use them as its secondary targets (that creates cannibalisation). Load `build-clusters` and
`keyword-clustering` for the detailed cluster workflows.

## Content prioritisation (transparent, configurable)

Score every candidate against a weighted rubric; explain why an article is prioritised. Volume is ONE
factor, never the only one.

Suggested weights (tune per project and record the weights in PROJECT.md):

| Factor | Question | Weight |
|---|---|---|
| Relevance | does it serve the niche and business? | high |
| Search intent | clear intent, winnable content type | high |
| Search demand | measured volume/interest (labelled estimated) | medium |
| Competition | realistic to rank given the site's authority | medium |
| Business value | monetisation or conversion potential | high |
| Topical authority | fills a cluster gap, strengthens the map | medium |
| Production effort | cost to produce original, useful content | medium |
| Source availability | can facts be sourced authoritatively | high (YMYL: critical) |
| Freshness / seasonality | time-sensitive or seasonal demand | low-medium |
| Existing coverage | does the site already answer this? | gate (skip if yes) |

Priority score = weighted sum; record it in the tracker with the inputs, so the choice is auditable.
Seasonal content is scheduled ~8 weeks before peak (publish-by = peak month minus 2).

## Cannibalisation guard

Before publishing AND before planning the next piece, re-check the live site:
`site:<domain> "<keyword>"` plus a token grep over the sitemaps. A page can be live and ranking with no
tracker record. Two pages targeting one query compete with each other; fix by choosing one target and
consolidating.
