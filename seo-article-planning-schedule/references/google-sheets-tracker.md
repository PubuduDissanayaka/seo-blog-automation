# Google Sheets Master Tracker (10 sheets)

One workbook per site. INSPECT an existing workbook before creating a new one (never create a duplicate).
Use Composio for Google Sheets when authorised; a direct API is fine when better documented. Use batch
operations, not one call per cell.

Data hygiene: three distinct classes of data - manual (human-entered), estimated (research tool output),
API-retrieved (Search Console/GA4). Mark the class in a column or colour convention and never overwrite
manual data with automated data.

## Sheet 1 - Dashboard

Total articles · published · scheduled · pending · needing updates · total clicks · total impressions ·
average CTR · average position · organic sessions · top-performing articles · keyword growth · content
production progress · monthly performance · publishing consistency · monetisation metrics (where
available). Drive these with formula summaries (COUNTIF/QUERY) over the other sheets, not hand-typed
numbers.

## Sheet 2 - Content Master

Columns: Article ID · Website · Category · Topic cluster · Title · URL slug · Primary keyword · Secondary
keywords · Search intent · Target region · Search volume · Keyword difficulty · Research source · Volume
retrieval date · Priority score · Assigned agent · Status · Creation date · Planned publication date ·
Actual publication date · Published URL · Last updated · Next review date · Quality score · SEO review
status.

## Sheet 3 - Keyword Map

Keyword ID · Keyword · Parent topic · Search intent · Target URL · Supporting URL · Search volume ·
Keyword difficulty · CPC (where available) · Region · Research source · Priority · Ranking status ·
Cannibalisation flag.

## Sheet 4 - Topic Clusters

Cluster ID · Pillar topic · Category · Supporting topics · Related keywords · Planned articles · Published
articles · Missing coverage · Cluster completion · Internal linking progress.

## Sheet 5 - Editorial Calendar

Article ID · Working title · Publishing date · Assigned writer · Editor · Research status · Draft status ·
Approval status · Publishing status · Target keyword · Cluster · Priority.

## Sheet 6 - Publishing Log

Article ID · Published URL · Publication date · Publication time · Publishing status · CMS/publishing
method · Verification status · Sitemap verification · Indexing status · Last checked · Error details.

## Sheet 7 - Performance Snapshots

Date · URL · Query · Clicks · Impressions · CTR · Average position · Organic sessions · Engagement
(where configured) · Conversion (where configured). Keep Search Console metrics distinct from GA4 metrics
(separate columns or separate tables; never one merged number).

## Sheet 8 - Content Refresh Queue

Article ID · URL · Last updated · Declining performance indicators · Outdated information · Missing topics ·
Broken references · Recommended changes · Priority · Assigned agent · Review status.

## Sheet 9 - Technical SEO Issues

Issue ID · Page URL · Issue type · Severity · Source · Date discovered · Recommended fix · Assigned agent ·
Status · Verification date.

## Sheet 10 - Automation Execution Log

Execution ID · Workflow · Trigger · Start time · End time · Agent · Result · Status · Retry count · Error
details · Verification result.

## Implementation rules

- Unique IDs per row (article, keyword, cluster, issue, execution).
- Data validation and dropdowns for every status/priority/severity column.
- Freeze header rows; add filters; conditional formatting for status and stale-date cells.
- Formula-based summaries on the Dashboard; pivot tables and charts where useful.
- Consistent date format everywhere (ISO `YYYY-MM-DD`); timezone stated on the Dashboard.
- Duplicate detection on slug, published URL and keyword before insert.
- Scalable and human-readable; do not over-complicate. A sheet that needs a manual to read has failed.

Transport and the derived-tracker pattern (publish the plan where the owner reads it, derived from the
gate rather than retyped): `seo-content-pipeline-automation` references/sheets-content-log.md.
