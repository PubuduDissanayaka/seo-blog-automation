# Step-by-Step Runbook (Skill 01)

Two scenarios. Commands assume the reference stack (Astro + TypeScript + Tailwind + Cloudflare Pages).
Adapt when discovery chose otherwise. Load `astro-static-site-build` and `cloudflare-pages-hosting` for the
exact config and pitfalls behind each command.

## A. New site from scratch

1. **Discovery.** Answer the questionnaire (`references/project-discovery.md`), fill `templates/PROJECT.md`,
   commit it. Do not code before this is saved.
2. **Scaffold by hand.** `npm init -y` then install `astro @astrojs/check sharp @astrojs/sitemap @astrojs/mdx
   @tailwindcss/vite tailwindcss gsap` + fontsource packages. Write `astro.config.mjs` (site, trailingSlash
   'always', build.format 'directory', sitemap + mdx integrations) and `tsconfig.json` extending
   `astro/tsconfigs/strict`.
3. **Token layer.** `design/tokens.json` + `scripts/gen-tokens.mjs` -> `src/styles/tokens.css`, plus
   `scripts/check-design-tokens.mjs` as the palette gate.
4. **Shell.** `BaseLayout.astro`, `Header.astro`, `Footer.astro`, `src/data/site.ts`, `src/data/head.ts`
   (typed head with env/load/consent fields).
5. **Design.** Generate Stitch concepts (`google-stitch-concepts`), audit the palette to zero off-token
   colours, commit PNG + HTML + NOTES.md under `design/stitch/`, then port into components.
6. **Content collections.** `src/content.config.ts` (Astro 5 glob loader) with strict zod schemas; read the
   real frontmatter before writing the category enum.
7. **Technical SEO.** `src/pages/robots.txt.ts` (from `site`), sitemap with `lastmod`, `src/pages/404.astro`,
   per-page JSON-LD, canonical/OG/robots in the head.
8. **Verify before deploy.** `astro check` + `npm run build`, then drive every route at 1280 and 390 with the
   verify-routes template; run axe on home/article/category/search/404; run the link audit.
9. **Deploy.** Create the git-connected Pages project, set `PUBLIC_*` build env vars, put the gates in the
   Pages build command, attach the domain, swap DNS (delete old A/AAAA, add proxied CNAME). See
   `cloudflare-pages-hosting` for the cutover runbook and `_headers`/`_redirects`.
10. **AdSense readiness + analytics.** `adsense-monetization-readiness` checklist against the live site;
    add GA4 (measurement-only, idle-loaded, PROD-gated) and verify a real `collect` 204.
11. **Postdeploy verify.** robots.txt/sitemap 200, one URL per family 200, headers present, Googlebot UA not
    403, rollback recorded.
12. **Hand off.** Confirm the Architecture + Identity sections of PROJECT.md are complete; Skill 02 reads them
    to plan content.

## B. Existing site: technical SEO audit and improvement (no rebuild)

1. **Inspect first.** Read the repo, PROJECT.md, `git status`; never overwrite existing work.
2. **Audit the BUILT/LIVE HTML, not the source.** Per page type: rendered title length, description length,
   H1 count, canonical, JSON-LD `@type` list, `og:`/`twitter:` tag counts, robots meta.
3. **Crawlability.** Fetch robots.txt and the sitemap index it names; confirm 200 and lastmod ratio; `curl`
   the homepage with a Googlebot UA (WAF not 403).
4. **Fix in order of impact:** indexation first (URL inspection), then metadata (unique titles/descriptions),
   then schema, then internal links/orphans.
5. **Verify each fix in the live output**, not the diff. Re-run the audit table before/after.
6. **Record.** Update PROJECT.md Decisions; leave a dated note of what changed and what is still open.
