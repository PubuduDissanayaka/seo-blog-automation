# Cloudflare, GitHub and Security

## Cloudflare infrastructure (preferred)

Use Cloudflare as the default. Evaluate and pick per project; do not create paid services or infrastructure
nobody asked for. State free-tier limits before promising anything.

- **DNS + SSL/TLS**: proxied records (orange cloud) so WAF/bot protection apply; Universal SSL. A DNS-only
  record is a gap, not a choice.
- **Pages vs Workers**: static content site -> Cloudflare Pages (git-connected) with no Functions, which is
  free and unlimited for static requests. Any Pages Function moves the project onto Workers request
  metering; keep it static unless a real endpoint (form) needs a Function, then scope it narrowly.
- **Caching**: `_headers` per-path rules; keep `Cache-Control` on asset paths (`/_astro/*`, `/fonts/*`),
  never `/*`. Set the zone `browser_cache_ttl` to 0 (Respect Existing Headers) or it silently rewrites
  every origin `Cache-Control`.
- **`_redirects`**: single-page fallback, 301s for changed/retired URLs, scoped wildcards that never shadow
  a real page. Every redirect target must exist.
- **Security settings**: WAF, bot fight mode, rate limiting as appropriate; security headers via `_headers`
  (CSP, HSTS, `X-Frame-Options`, `Permissions-Policy`, COOP) - start from `static-site-hardening` and the
  `cloudflare-pages-hosting` templates.
- **Environment variables**: set `PUBLIC_*` build vars in the Pages project (deployment_configs.production.env_vars), because Astro inlines them at build time and a missing one fails silently.
- **Preview deployments**: staging branch -> preview URL, noindexed, with the cutover order documented
  (delete noindex -> flip `site` -> attach domain -> move DNS).

The full deploy mechanics, the DNS cutover runbook, the domain-attach ordering, the custom-domain cache
pitfalls and the `_headers`/`_redirects` semantics live in `cloudflare-pages-hosting` - follow it, do not
re-derive it.

## GitHub development workflow

- Inspect the repo before modifying; never overwrite existing work; read `git status` before committing.
- Branch management: feature branches, PRs for anything touching shared code; direct pushes only for
  content/typos where the team allows it.
- Commit standards: conventional, small, one logical change per commit; a real message, not "fix".
- Code review before merge on code changes; automated build checks and tests in CI.
- GitHub Actions: build + lint + typecheck + test gates run before a deploy is promoted. Put the gates in
  the Pages build command too so a broken commit cannot ship.
- Secrets: GitHub Secrets or Cloudflare env vars only. Never commit tokens. Enable secret scanning and
  dependency auditing (Dependabot).
- Deploy workflow: git-connected Pages deploys on push to production branch; direct-upload deploys are
  refused for git-connected projects (they race Cloudflare's own build).
- Rollback: the previous `A`/`AAAA` record values or the previous deployment is the rollback; write it down
  before a cutover.

## Security audit

Use `cloudflare-security-audit` (the Cloudflare security-audit skill, installed under that name). Guidance
mode for focused reviews; full mode when a full audit is requested. Cover: Cloudflare config, DNS exposure,
SSL/TLS, security headers, WAF, bot protection, API endpoints, auth, access controls, rate limits, secrets,
dependencies, GitHub config, deploy config.

Rules: least privilege; recommend the smallest effective fix; never execute destructive remediation
without approval; record findings, remediation and remaining risks; verify remediation rather than
asserting it. A candidate without a concrete affected principal and observable result is not a finding.

## Verification

- [ ] Production serves the verified build on the custom domain (not the pages.dev URL)
- [ ] `_headers` and `_redirects` live at the upload root and the security headers are present on the host
- [ ] cache headers correct on the custom domain after a zone purge
- [ ] DNS cutover complete (no stale A/AAAA), rollback recorded
- [ ] no secrets in source, context or commits; secret scanning + dependency audit on
- [ ] security audit findings recorded, remediated or honestly needs-validation
