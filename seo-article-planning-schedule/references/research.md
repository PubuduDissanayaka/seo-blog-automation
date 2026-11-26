# Niche, Competitor and Keyword Research

Everything here follows the data-hygiene rule: record SOURCE, RETRIEVAL DATE and CONFIDENCE on every
figure. Never invent volumes, difficulty, CPC, traffic or revenue. Estimated third-party data and actual
Search Console/GA4 data are different things - label them differently and never mix them.

## Niche validation

Evaluate before committing months of work:

- Demand: search interest and trend (Google Trends), not a single volume number.
- Competition: who ranks, how strong, how entrenched.
- Audience characteristics and what they actually search.
- Search intent spread and commercial potential.
- Geographic opportunities (under-served regions/languages).
- Content production difficulty (can the team actually make original, useful content here?).
- Monetisation opportunities (AdSense RPM band, affiliate, etc. - see `adsense-monetization-readiness`).
- Long-term topical expansion room.

Verdict: is the niche realistic for the available resources and target market? For YMYL topics, apply
stronger evidence, expertise and editorial requirements up front. Say plainly when a niche is not viable
with the budget rather than recommending a doomed plan.

## Competitor analysis

Structured, never copied:

1. Identify direct and indirect competitors, established and newer sites.
2. Map their content categories and ranking pages (their sitemap + SERPs).
3. For each ranking page: search intent, content depth, internal linking, freshness.
4. Backlink profile where reliable data is available (do not invent it).
5. Find content gaps - topics competitors rank for that the site has no page for (a gap is a term, not a
   ranking; it proves nobody on our side is even trying).
6. Find unique opportunities - angles, formats, original data none of them publish.

Load `competitor-analysis`, `competitive-landscape` and `beat-competitors` for the detailed workflows, and
`seo-master` Part 7 for the deconstruction framework. Read the SERP before the brief: the SERP features,
the format the ranking titles share, and the content gaps are what tell you the shape the page must take.

## Keyword research methodology

1. **Seeds**: 5-10 seed keywords from the niche and the site's own navigation/H1/H2 copy.
2. **Expand**: autocomplete, People Also Ask, related searches, a Google Ads ideas dump (cheapest way to
   see a whole niche - see `seo-content-pipeline-automation`), question-based tools, entity/related terms.
3. **Categorise** (see intent below) and **collapse to query families** before planning: normalise tokens,
   merge variants that carry the same volume and overlap in tokens; one family = one article. Report the
   family count, never the raw row count.
4. **SERP-check before assigning**: look at what Google actually ranks for the query. Do not depend on
   third-party volume alone. One SERP per intent cluster is enough; reuse it for every article in the
   cluster.
5. **Score and prioritise** (see topical-authority reference).

Use the credit-aware, cache-first DataForSEO client (`dataforseo-api` + `seo-content-pipeline-automation`
references/dataforseo-research-notes.md): batch volumes (one request covers up to 1,000 keywords), standard
SERP tasks over live endpoints, Labs only in monthly discovery, an append-only cost ledger and a per-run
cap. Free-first: official sources, competitor pages, our own cached SERP.

## Search intent classification

Classify every keyword before assigning content:

| Intent | Signal | Content type |
|---|---|---|
| Informational | "how to", "what is", "guide", "tips" | Blog post, guide, tutorial |
| Commercial investigation | "best", "vs", "review", "alternative" | Comparison, review, roundup |
| Transactional | "buy", "price", "discount", "near me" | Product/landing page |
| Navigational | brand names, specific URLs | brand pages |
| Local | "near me", geo-modifiers | local pages |
| Mixed | several of the above | match the dominant intent |

An informational keyword does not get a sales page. Determine the best content type per keyword, and say
which SERP features the page is competing for.
