#!/usr/bin/env bash
# Preflight check for the SEO blog automation skills.
# Verifies the toolchain, accounts tooling and companion skills the two skills depend on.
#
# Usage: bash scripts/preflight.sh
# Exit:  0 = no hard failures, 1 = at least one FAIL

set -uo pipefail

PASS=0; WARN=0; FAIL=0
ok()   { printf '  \033[32mPASS\033[0m %s\n' "$1"; PASS=$((PASS+1)); }
warn() { printf '  \033[33mWARN\033[0m %s\n' "$1"; WARN=$((WARN+1)); }
bad()  { printf '  \033[31mFAIL\033[0m %s\n' "$1"; FAIL=$((FAIL+1)); }
head_() { printf '\n\033[1m%s\033[0m\n' "$1"; }

SKILLS_DIR="${HERMES_HOME:-$HOME/.hermes}/skills"

head_ "Toolchain"

if command -v git >/dev/null 2>&1; then ok "git $(git --version | awk '{print $3}')"; else bad "git not found (required)"; fi

if command -v node >/dev/null 2>&1; then
  NODE_V=$(node -v | sed 's/^v//')
  NODE_MAJOR=${NODE_V%%.*}
  if [ "${NODE_MAJOR:-0}" -ge 22 ]; then
    ok "node v$NODE_V (>= 22 required for Astro 5 and the design inspector)"
  else
    bad "node v$NODE_V is too old (need >= 22)"
  fi
else
  bad "node not found (required: Astro, design-taste-frontend scripts)"
fi

if command -v npm >/dev/null 2>&1; then ok "npm $(npm -v)"; else bad "npm not found (required)"; fi
if command -v python3 >/dev/null 2>&1; then ok "python3 $(python3 -V 2>&1 | awk '{print $2}') (bundled scripts)"; else bad "python3 not found (required for scripts/)"; fi

CHROME=$(command -v google-chrome || command -v chromium || command -v chromium-browser || command -v microsoft-edge || true)
if [ -n "$CHROME" ]; then ok "Chromium-family browser: $CHROME"; else warn "no Chrome/Chromium found (design inspector, axe and Lighthouse need one)"; fi

if command -v gh >/dev/null 2>&1; then
  if gh auth status >/dev/null 2>&1; then
    ok "gh authenticated as $(gh api user --jq .login 2>/dev/null)"
  else
    warn "gh installed but not authenticated (run: gh auth login)"
  fi
else
  warn "gh CLI not found (optional, but deploys and repo setup are easier with it)"
fi

head_ "The two skills"

for s in seo-blog-website-development seo-article-planning-schedule; do
  if find "$SKILLS_DIR" -type d -name "$s" 2>/dev/null | grep -q .; then ok "$s installed"; else bad "$s NOT installed (copy it into $SKILLS_DIR)"; fi
done

head_ "Companion skills"

CORE="astro-static-site-build cloudflare-pages-hosting cloudflare-security-audit google-stitch-concepts ui-ux-pro-max design-taste-frontend modern-web-guidance static-site-hardening schema site-brand-assets adsense-monetization-readiness seo-master seo-content-pipeline-automation ponytail"
OPTIONAL="design-reference-research inspo-mcp awwwards-mcp popular-web-designs hallmark frontend-ui-engineering redesign-existing-projects vanilla-static-site-build dataforseo-api find-keywords build-clusters keyword-clustering competitor-analysis competitive-landscape beat-competitors seo-content-qa google-search-docs"

NAMES=$(find "$SKILLS_DIR" -name SKILL.md -type f 2>/dev/null \
  | while read -r f; do sed -n 's/^name:[[:space:]]*"\?\([A-Za-z0-9_-]*\)"\?.*/\1/p' "$f" | head -1; done \
  | sort -u)

for s in $CORE; do
  if printf '%s\n' "$NAMES" | grep -qx "$s"; then ok "core: $s"; else bad "core companion missing: $s"; fi
done

MISSING_OPT=""
for s in $OPTIONAL; do
  printf '%s\n' "$NAMES" | grep -qx "$s" || MISSING_OPT="$MISSING_OPT $s"
done
if [ -z "$MISSING_OPT" ]; then ok "all optional companions present"; else warn "optional companions not installed:$MISSING_OPT"; fi

head_ "Accounts you must hold (checked manually, one time)"
printf '  - GitHub account with repo + Actions access\n'
printf '  - Cloudflare account (Pages, DNS) and a domain\n'
printf '  - Google Search Console property (verified) for the site\n'
printf '  - Google Analytics 4 property and measurement ID\n'
printf '  - Google AdSense account (apply only once ~20-30 strong articles are live)\n'
printf '  - Optional: Composio (Cloudflare/GitHub/Sheets/Stitch), DataForSEO (paid keyword + SERP data)\n'

head_ "Result"
printf '  %d pass, %d warn, %d fail\n' "$PASS" "$WARN" "$FAIL"
if [ "$FAIL" -gt 0 ]; then
  printf '\n  \033[31mNot ready.\033[0m Fix the FAIL lines above, then re-run.\n'
  exit 1
fi
printf '\n  \033[32mReady.\033[0m Warnings are optional gaps, not blockers.\n'
