# Search Console and GA4 Data Access

Verify current endpoints and scopes against the official docs at execution time; do not invent them. The
capability level below is stable; the exact API surface changes.

## Google Search Console (search performance and indexing)

Access requires an authorised account (OAuth user token or service account) on a VERIFIED property, or a
Composio Search Console integration where one is connected. What you can pull:

- **Performance** (Search Analytics query): clicks, impressions, CTR, average position, per query, page,
  country, device, date, and search appearance; filter by web search; date range up to ~16 months. Position
  is an AVERAGE, never an exact fixed rank - say so in reports.
- **URL Inspection**: the indexing state of a single URL - whether it is indexed, the page-fetch state, the
  user-declared canonical, robots block, and crawl/indexing errors. This is how you answer "is this URL
  actually indexed" (a sitemap entry is not proof).
- **Sitemaps**: list, submit and delete sitemaps. Submit the INDEX, never a child. Verify the property
  exists before promising a submission.
- **Indexing (Page Indexing report)**: why pages are or are not indexed, by reason.

Usage rules: cache results (TTL'd) so you never pay twice for the same query; mark Search Console data as
API-retrieved and keep it SEPARATE from GA4 data in the tracker and reports; never mix estimated third-party
volumes with these actual figures.

## Google Analytics 4 (behaviour)

Access via the GA4 Data API v1 (`runReport`) with a property id and OAuth, or a Composio GA4 integration
where connected. Pull: organic sessions, engaged sessions, engagement rate, conversions, landing pages,
returning vs new, geography, device, session source/medium. Analytics measures behaviour; Search Console
measures search performance - never merge the two into one number.

## Which answers which question

| Question | Source |
|---|---|
| How many clicks/impressions, where do we rank | Search Console |
| Is this URL indexed, and why not | Search Console URL Inspection |
| How do visitors behave once they land | GA4 |
| What did our content earn this month | GA4 (sessions/engagement) |
| Which keyword moved toward page one | Search Console (position, with the average caveat) |

## Integration

Prefer Composio when a connected integration already exists (discover with `composio search`, read the
schema with `--get-schema`, verify with a real call). Use direct APIs when they are better documented or
maintainable. Never assume a connection exists because the tool name looks right - do the call.
