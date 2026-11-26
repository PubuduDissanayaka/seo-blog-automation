# Heading Hierarchy Verification

One H1 per page and no skipped levels. Heading order is a real accessibility issue (screen reader users
navigate by heading list) and a real SEO signal, so it is checked in the BUILT HTML, never in the source
markdown. A component that renders a card title at the wrong level shows up on one template only.

## Procedure

1. Build the site, then walk the built HTML per template type, not just the home page. The templates that
   differ are home, article, category archive, search and 404.
2. Extract every heading in document order with its level:

   ```bash
   python3 - <<'PY'
   import re, pathlib
   for p in sorted(pathlib.Path("dist").rglob("*.html"))[:5]:
       html = p.read_text()
       hs = [(int(m.group(1)), re.sub(r"<[^>]+>", "", m.group(2)).strip()[:48])
             for m in re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", html, re.S | re.I)]
       levels = [h[0] for h in hs]
       h1 = levels.count(1)
       skips = [f"{a}->{b}" for a, b in zip(levels, levels[1:]) if b > a + 1]
       print(f"{p}: h1={h1} skips={skips or 'none'}")
       for lvl, text in hs[:12]:
           print(f"   h{lvl}  {text}")
   PY
   ```

3. Fail the page when `h1 != 1`, when the sequence skips a level (an H2 followed directly by an H4), or
   when the first heading is not the H1.

## What usually causes it

- A card component hardcodes `<h3>` and is reused inside a section whose parent is already an H3.
- A sidebar or related-posts widget renders its own H1.
- A Markdown article starts at `###` because the template already emits the H1.
- The site logo or wordmark is marked up as an H1 in the header, so every page has two.

## Fixes

Make the level a property of the component, not a literal: pass a `level` prop and render `h${level}`.
Where a widget genuinely has no place in the outline (a related-posts label), use a styled `<p>` or
`<div>`, not a heading.
