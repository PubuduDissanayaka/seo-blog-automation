# RankMath 95+ Gate (programmatic, pre-publish)

Every article must clear this gate before it publishes, automatically. On WordPress sites, read the ACTUAL
RankMath score from the plugin (never report a score you cannot verify - see
`seo-content-pipeline-automation`). On Astro/static sites there is no plugin, so the pipeline computes the
same checks itself (the mechanical half is already in that skill's `article_gates.py`).

Target: 95+/100. RankMath scores across four categories; 100/100 means every test at its max threshold.
95+ means every test passes AND the readability tests sit at their high thresholds, not their pass floor.

## The 28 checks (machine-checkable thresholds)

### Basic SEO (all must pass; foundation)
1. Focus keyword in the SEO title (first 50-60 chars).
2. Focus keyword in the meta description (within 160 chars).
3. Focus keyword in the URL slug.
4. Focus keyword in the first 10% of content (first ~100 words).
5. Focus keyword in the body, 3-5 natural occurrences.
6. Content length >= 2500 words (600 is the floor; 2500 is the 100% mark).

### Additional SEO
7. Keyword in subheadings: primary in 1 H2; each of the 5 related keywords in an H3 or body section.
8. Keyword in image alt text: 2-3 images.
9. Keyword density: primary 1-1.5%, related 0.5-1%.
10. URL length <= 75 chars.
11. External links >= 1 (2-3 for 100%).
12. Followed (dofollow) external links >= 1 (2-3 for 100%).
13. Internal links >= 1 (3-5 for 100%).
14. Focus keyword unique - not used on any other post (`site:domain "keyword"`).
15. All 5 related keywords unique site-wide.

### Title Readability
16. Title length 40-60 chars (45-55 is the sweet spot).
17. Title contains a number.
18. Title contains a power word.
19. Positive or neutral sentiment.
20. Focus keyword in the first 50-55 chars of the title.

### Content Readability
21. No paragraph over 6 sentences (2-4 for 100%).
22. Average sentence <= 25 words (15-20 for 100%).
23. Transition words present (3-5 per section for 100%).
24. Passive voice < 15% (< 10% for 100%).
25. Subheading every 200-350 words.
26. Images/video >= 1 (4+ for 100%).
27. Flesch reading ease > 40 (60-80 for 100%; aim 55+).
28. No 4+ consecutive sentences starting with the same word (2 max).

## Hard pitfalls that silently drop the score

- A long-tail focus keyword (4+ words) needs 7-10+ body occurrences. 2 occurrences at 0.06% FAILS density.
- Title <= 60 chars and meta <= 160 chars are HARD. 65 and 209 both fail. Shorten years ("2026-2027" ->
  "2026-27") and "and" -> "&".
- Links must be baked into the HTML: internal >= 5, dofollow external >= 3. A placeholder comment fails.
- The focus keyword must appear VERBATIM, not as a grammatical variant ("getting around X" does not satisfy
  "how to get around X"; singular/plural mismatches fail too).
- Readability metrics are measured on prose only: strip tables and heading text first, or a fares table reads
  as one giant sentence and the numbers lie.

## Enforcement (automated)

The pipeline measures every check, reports the score as evidence, and then:
- **Pass (>= 95)** -> publish automatically, no human step.
- **Fail (< 95)** -> set the item to `held`, run a fix pass, re-gate, and only publish on a pass.

Never skip a gate for speed, and never report a score the pipeline did not actually compute. A pipeline that
publishes a failing article is worse than one that stops.
