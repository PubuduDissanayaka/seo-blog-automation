# Technical SEO Implementation

Verify every item in the BUILT or LIVE output, never in source. A template can define metadata and never
render it; grep the generated HTML.

## Crawling and indexing

- **robots.txt**: generate from the canonical origin (`site`), never commit as static. Include the sitemap
  index. Block genuinely low-value paths only; do not block CSS/JS.
- **XML sitemap**: `@astrojs/sitemap` writes `sitemap-index.xml` + child files. Submit the INDEX, never a
  child. Emit `<lastmod>` from content dates (there is no page mtime at build). Never add `changefreq` or
  `priority`. Exclude noindex pages via both `filter(page)` and a `serialize(item)` noindex check. Never
  list a noindex URL in the sitemap.
- **Canonical URLs**: one per page, absolute, derived from `site` + route. Self-referencing.
- **Meta robots**: `index, follow, max-image-preview:large, max-snippet:-1` on indexable pages;
  `noindex, follow` on non-indexable ones.
- **HTTP status**: article 200, category 200, 404 page returns a real 404 status.
- **Redirects**: every old URL or changed slug gets a 301 in `_redirects` to a page that exists. A 301 to a
  404 is worse than none. `_redirects` honours only 301/302/303/307/308 (a 410 line is parsed but not
  applied).
- **Duplicate content**: one canonical form per page, no trailing-slash duplicates, no query-string
  variants, staging host noindexed via `X-Robots-Tag` in `_headers`.
- **Orphaned pages**: every page reachable by an internal link; sweep with the link audit.
- **JS rendering**: static HTML means no rendering dependency; keep any client JS progressive enhancement
  so content is present without it.

## Metadata

- **Title**: <= 60 chars including brand, unique per page, primary keyword near the front. Skip the brand
  suffix when the title already contains it. Measure the RENDERED length after HTML entity decoding.
- **Meta description**: <= 160 chars, unique, contains the keyword, answers the intent with a reason to
  click.
- **Heading hierarchy**: one H1 per page; H2/H3 descriptive and ordered; no skipped levels.
- **Open Graph / Twitter**: og:title, og:description, og:url, og:type, og:image (must resolve to a real
  file), og:locale, og:image:type/width/height/alt; twitter:title/description/image/image:alt (Twitter does
  NOT inherit og values). Assert each tag appears exactly once per page. Article pages add
  `article:published_time`, `modified_time`, `author`, `section`.
- **Image alt**: descriptive, keyword where natural, on every content image.

## Structured data (validate in built HTML, and only mark up what users can see)

Eligible types for a blog, applied per page:

- **BlogPosting / Article** on articles: headline, author, datePublished, dateModified, image, publisher.
- **Organization** on about/home: name, url, logo, sameAs, contactPoint.
- **Person** on author pages: name, sameAs, jobTitle.
- **BreadcrumbList** where breadcrumbs are shown.
- **WebSite** with SearchAction (when the site has search) on home.
- **FAQPage** ONLY when a real FAQ is visible on the page. Do not mark up hidden Q&A.

Rules: use `@graph` to nest types; generate schema data-driven from the content file (e.g. `faq: [{q,a}]`
in the schema) so markup and visible content share one source; never mark up information a user cannot see;
validate each `application/ld+json` block by parsing it in the built HTML and printing the `@type` list per
route (a null or a missing type is the finding). Do not ship misleading schema.

## Internal linking

- Contextual links in article body to related articles and the cluster/pillar.
- Related-articles blocks, category linking, breadcrumbs.
- Every article links to its pillar and at least 2-3 siblings.
- Detect orphans with the link audit; every page reachable from the nav or another page.
- No artificial links purely to inflate counts.

## International SEO (only when a true multi-language build exists)

- Language-specific URLs (`/`, `/es/`, ...) or separate domains - pick one and be consistent.
- `hreflang` (link tags or sitemap, one method) with self-referencing tags and `x-default`, no redirects as
  targets, reciprocal return tags.
- Localised metadata and content; never machine-translate and ship without human review for indexed
  content.

## Verification checklist (technical SEO)

- [ ] robots.txt 200 and names the sitemap index; fetch the sitemap URL it names and confirm 200
- [ ] sitemap index + child files list every indexable URL; lastmod ratio (grep -o) is honest
- [ ] canonical absolute and unique per page; noindex pages absent from sitemap
- [ ] title/meta unique per page type, within limits, measured on rendered output
- [ ] one H1 per page; heading order valid
- [ ] og/twitter tags present once each; og:image resolves (fetch it)
- [ ] schema present and parses in built HTML with the expected @type per route
- [ ] every internal link resolves; no orphan pages
- [ ] `curl` homepage with a Googlebot UA returns 200 (WAF/bot rule not 403)
