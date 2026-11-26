# Article Briefs, Writing Standards and Editorial QA

## Article briefs (before any prose)

Generate a structured brief for every article. Fields:

1. Article ID (stable, unique).
2. Proposed title (within limits, primary keyword near the front).
3. Primary keyword (exactly 1) and 5 secondary keywords.
4. Search intent (classified).
5. Target audience and region.
6. Content purpose (what the reader gets).
7. Main questions the article must answer.
8. Required research (facts to verify and where).
9. Authoritative sources to use.
10. Competitor observations (what the SERP winners do and their gaps).
11. Recommended structure (H2/H3 skeleton).
12. Heading suggestions with the keyword placement plan (which heading carries each keyword).
13. Internal linking opportunities (existing URLs, verified to exist).
14. External references (dofollow, authoritative).
15. Suggested images (subject + alt text).
16. Metadata (title, description, canonical).
17. Schema recommendation (BlogPosting, FAQPage where a real FAQ exists).
18. Editorial considerations (E-E-A-T, disclosures).
19. Fact-checking requirements and the date each fact is checked.
20. Estimated word count from actual content requirements (never an artificial quota).
21. Publishing priority (from the scoring model).

Do not impose artificial word counts or keyword densities. Do not target a density number; write the
content the intent needs.

## AI writing standards

Prioritise: originality, human usefulness, accuracy, clarity, intent satisfaction, appropriate depth and
expertise, first-hand experience where genuinely available, trustworthy evidence, readability, natural
language, logical structure.

Avoid: repetitive AI content, keyword stuffing, generic introductions, artificially extended articles,
unsupported claims, fabricated statistics, fake author experiences, fabricated quotations, fake
references, plagiarism, misleading titles, mass-generated low-value pages.

Research and cite authoritative sources; keep source links and research notes. Every article needs at
least 3 original-value elements (own data, first-hand observation with place/date, an original decision
table, a documented conversation) - see `adsense-monetization-readiness` for the menu. For YMYL, require
an expert review pass. AI assists quality; it does not replace editorial responsibility.

Load `seo-master` (E-E-A-T template, AEO/GEO direct-answer structure, SERP analysis) and
`seo-content-pipeline-automation` (two-step outline-then-article, article gates, structure variation
ledger) for the full writing procedure. Follow the two-step production: outline first (gated), then prose;
never jump straight to a full draft.

## Editorial QA gate (automated, pre-publish)

A configurable scoring rubric PLUS the RankMath 95+ score (see `references/rankmath-95-gate.md`); any
hard-fail condition blocks publication. Score originality, accuracy, source quality, intent match,
readability, completeness, title quality, heading structure, internal links, external references, metadata,
image quality, accessibility, policy compliance, overall usefulness.

**Hard-fail conditions (never publish):**

- Fabricated or unverifiable factual claims, statistics, quotes, references or author experience.
- Plagiarism or substantive copying without adding value.
- Keyword stuffing or scaled-content patterns (a page whose primary purpose is manipulation).
- A title that does not match the content (misleading).
- Missing required disclosures (affiliate, sponsorship, health/finance claims).
- YMYL content without the required expert review (the one content class that is NOT auto-published).
- Any failure of the mechanical gates in `seo-content-pipeline-automation` (article_gates.py).

The gate runs automatically in the pipeline before publish: a pass auto-publishes, a fail auto-holds. Report
both the editorial score and the RankMath score as evidence. A pipeline that publishes a failing article is
worse than one that stops - a held item stays held until the gate passes. Never skip a gate for speed.
