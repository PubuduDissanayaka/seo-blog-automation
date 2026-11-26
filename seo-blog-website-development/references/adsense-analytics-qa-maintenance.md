# AdSense Readiness, Analytics, QA and Maintenance

## AdSense readiness (a dedicated objective, not an afterthought)

Load `adsense-monetization-readiness` for the policy detail, the consent/CMP rules and the honest revenue
maths. This skill owns the site-readiness half. Summary of the checklist to verify against the LIVE site:

- [ ] Original, useful content by a real named author (bio, credentials, `sameAs`).
- [ ] No placeholder/demo or "under construction" pages anywhere (including the sitemap).
- [ ] Substantial Privacy Policy (names cookies and third-party vendors, AdSense disclosure, opt-out),
      Terms, Cookie notice, About, working Contact, Editorial Policy, Affiliate/Advertising Disclosure.
- [ ] Google-certified CMP with IAB TCF before serving ads to EEA/UK/CH visitors (required since 16 Jan
      2024; CH 31 Jul 2024). Non-certified CMP traffic is only eligible for limited ads.
- [ ] Clear navigation, working sitemap, an engagement surface (comments or similar).
- [ ] `ads.txt` published after approval; account created in the owner's identity; Search Console ownership
      verified.
- [ ] Roughly 20-30 genuinely useful articles before applying (judgement call, not a Google rule).
- [ ] ads placement <= ~30% of visible content, none above the fold pushing content down, LCP/CLS protected.

Do NOT guarantee approval or income. Do NOT use deceptive layouts, accidental-click placements,
incentivised interactions or artificial traffic - these are policy violations that disable ads and can
remove the site from search.

Check current official AdSense publisher policies at execution time; they change.

## Analytics and monitoring integration

- **GA4**: measurement-only by default (`anonymize_ip`, no Google signals, no ad personalisation signals)
  unless the owner asks for advertising features. Load the tag after the load event / idle frame, not
  blocking first paint. Update the privacy page in the SAME commit (naming `_ga`, `_ga_<ID>`, retention,
  what is recorded, how to refuse). Gate the script on `import.meta.env.PROD`.
- **Search Console**: verify ownership (meta tag method - Cloudflare Pages canonicalises `.html` files, so
  a file-based token answers 308 and a non-redirect-following verifier fails). Verify the property exists
  in the account before promising a submission.
- **Bing Webmaster Tools**: IndexNow is the channel the pipeline can drive alone (key file at root, no
  OAuth). Submit after deploy; report `200`/`202` as "accepted for crawling", never "indexed".
- Privacy-conscious and performance-aware: tracking must not damage CWV or violate consent requirements.

## Full QA checklists

### Predeploy (built output)

- [ ] `npm run build` green AND `astro check` clean
- [ ] every route renders (drive at 1280 and 390 in a real browser, not just curl)
- [ ] no broken internal links; no bare `href="#"`
- [ ] unique title/meta per page type, within limits
- [ ] canonical correct and unique; one H1 per page
- [ ] sitemap index + robots.txt valid; lastmod emitted from content
- [ ] schema parses in built HTML with expected @type per route
- [ ] og/twitter tags once each; og:image resolves
- [ ] axe clean; performance budget met (measured, not quoted)
- [ ] analytics tag present in PROD only; ads markup absent until approved
- [ ] redirects land on existing pages
- [ ] no placeholder/TBD/OWNER TO SUPPLY strings in built HTML

### Postdeploy (custom domain, not the pages.dev preview)

- [ ] robots.txt and sitemap fetch 200 and agree
- [ ] one URL from each URL family returns 200
- [ ] security headers present (CSP/HSTS) on the custom domain
- [ ] schema present in the served HTML
- [ ] `curl` with a Googlebot UA returns 200 (WAF/bot rule not 403)
- [ ] DNS cutover complete (no stale A/AAAA); rollback recorded
- [ ] GA4 `collect` request fires with a 204 on a real browser visit

Never report a successful deployment from a local build alone. Verify the production host.

## Maintenance (recurring, schedule with cronjob_manage)

- Monthly: dependency updates (audited), security review, broken-link sweep, sitemap + robots check,
  crawlability check, analytics verification.
- Quarterly: performance review against the budget, content template improvements, technical SEO
  improvements, AdSense policy re-read (policies change).
- Ongoing: backup verification and restore testing.

Record each run with a date and result. A maintenance run that finds nothing still writes a log entry.
