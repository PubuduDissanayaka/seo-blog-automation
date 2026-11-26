# UI/UX Design (first-class priority)

Design is not decoration applied after the build. On a content site it decides whether anyone reads the
article, whether the ads earn, and whether the site reads as a designed publication or as the average of
every blog a model has seen.

Rule: **design is specified before markup exists and verified in a real browser before deploy.** A page
that skipped the design phase is not finished, however green the build is.

## The design skill stack (load these, do not reinvent them)

| Skill | Load it for | What it gives you |
|---|---|---|
| `google-stitch-concepts` | **Always, first.** The standing rule: user-visible UI goes through Google Stitch before code. | A generated concept in the project's real palette, committed as PNG + HTML + NOTES.md under `design/stitch/<lane>/`, with the palette audited to zero off-token colours. |
| `ui-ux-pro-max` | Choosing the design system: style, palette, typography, spacing, icons, UX rules. | Searchable local data (79 styles, 192 product palettes, 74 font pairings, 119 UX guidelines, 22 stacks including `astro`). `--design-system` generates a whole system; `--persist` writes `design-system/<slug>/MASTER.md`; dials `--variance/--motion/--density` tune it. |
| `design-taste-frontend` | Any public-facing page: art direction, anti-slop enforcement, look-and-fix loop. | A 10-step run (argument, direction, idea, copy, build, gate, look, motion), house rules, `lint.mjs` + `inspect.mjs` measuring at 1440/768/390, and a juror critique rubric. Not for dashboards. |
| `design-reference-research` | Shortlisting real references before designing. | Named references with evidence, instead of a vibe. |
| `inspo-mcp`, `awwwards-mcp` | Needing live production-site evidence. | Real pages and component examples to learn structure from. |
| `popular-web-designs` | Borrowing a proven system. | 54 real design systems (Stripe, Linear, Vercel and similar) as HTML/CSS. |
| `hallmark` | Auditing for AI-slop tells. | A pass that catches the generic-generated look. |
| `frontend-ui-engineering` | Production implementation of the design. | Accessible, responsive, production-quality front-end patterns. |
| `redesign-existing-projects` | Upgrading an existing site. | Premium-quality upgrade path rather than a rebuild. |

Read the skill you load. Do not paraphrase a capability you have not checked, and do not claim a gate ran
when it did not.

## The design run (order matters, do not skip)

1. **Brief and inventory.** From `PROJECT.md` plus `design-reference-research`: who the reader is, the one
   thing the page must do, the brand assets that really exist, and an inventory of 8 to 12 things that
   belong to this publication and to no competitor. The inventory is where the idea comes from.
2. **Argument before layout.** List the page as claims with their proof, one line per section. Sections
   that carry no claim are deleted. This is what stops the stock sequence of hero, three cards,
   testimonial, newsletter.
3. **Direction.** Stitch concept first (`google-stitch-concepts`). When a full system is needed instead of
   one screen, `ui-ux-pro-max --design-system`, optionally with `--variance/--motion/--density` dials.
   Adopt the direction you were dealt. Redraw only for a reason you can state (a brand constraint, an
   asset that does not exist), and record each redraw.
4. **Design system artifact.** Two files, both committed: `design/tokens.json` as the single source of
   truth, and the direction sheet (`design-system/<slug>/MASTER.md` from `--persist`, or the Stitch
   sheet). Every colour, font, size, leading, radius, shadow and spacing value lives in tokens. Nothing
   downstream invents a value.
5. **Copy deck.** Headlines fit two lines at every width (about 32 characters is safe). One supporting
   sentence. One primary action, named for what it does. Every section carries its full content. Proof is
   never invented.
6. **Build still.** Tokens, then the hero, then each section, then imagery, then the interactive element.
   A page that needs animation to look finished is not finished. Neighbouring sections must not share a
   layout, and no section is a row of identical cards.
7. **Gate, and mean it.** Palette gate plus the inspector (below). Fix every failure.
8. **Look.** Open the screenshots at all three widths, critique them with `design-taste-frontend`'s rubric,
   fix the top three problems, re-run the gate, look again. Three rounds at most. Judge the pictures: if a
   problem is visible in a screenshot it is real, whatever the code says.
9. **Motion last.** Entrance per section, feedback on every control, one signature move. Transform and
   opacity only, with a `prefers-reduced-motion` fallback that keeps the content.
10. **Report.** The direction, any redraws with reasons, deltas between concept and build, and every found
    image with its credit.

## Design gates (hard, measurable, checked in a browser)

- **Palette:** zero colours outside `tokens.json`. A gate script walks the source and fails the build on any
  stray hex. Resolve `var()` before judging, and normalise `rgb()`/hex forms before comparing.
- **Inspector:** `design-taste-frontend` `lint.mjs` plus `inspect.mjs` at 1440, 768 and 390 pixels. No
  `FAIL` may remain. Treat every `WARN` as wrong unless you can defend it to a designer in one sentence.
- **Type:** at most five sizes and two families on a page. Headlines two lines or fewer at every width.
  Body 16px or larger, line-height 1.45 to 1.6, measure 45 to 75 characters.
- **Contrast:** WCAG AA, 4.5:1 for body text and 3:1 for large text and UI. Never dim type with `opacity`
  to soften it on a coloured fill; use the token that passes.
- **Accessibility:** axe on the built site reports zero serious or critical violations per route.
- **No layout shift from design decisions:** reserve space for ads and media, set explicit dimensions.
- **Screenshots reviewed** at all three widths before deploy, by you, not assumed from a green build.

## Anti-slop rules (the tells that make a site read as AI-made)

No eyebrow labels or pill badges above a headline. No gradients. No thin hairline rules as dividers. No
shadows on things at rest. No glass or backdrop blur. No emoji as icons. No monospace outside real code. No
index numbering (01 / 02 / 03). No icon-topped rows of identical cards. No styled accent word inside a
headline. No tiny uppercase letter-spaced labels. No assistant palette (yellow-cream with terracotta, or
violet).

Removing ornament leaves space. Fill it with scale, with the full content, with a picture made for this
subject, or with a field of flat colour. Never with another ornament.

## Blog-specific design priorities

The reader came from search to read one article on a phone. Design for that first.

- **Article template is a reading surface.** Generous measure and leading, one clear H1, a visual rhythm
  that never competes with the text.
- **Ads are reserved, not reacted to.** Fixed slots with reserved height so nothing jumps. Keep ads to
  roughly 30 percent or less of visible content, and never place one above the fold pushing the article
  down.
- **Navigation is a wordmark, three to five plain links, and search.** No mega menus on a blog.
- **Category and index pages get their own composition.** A grid of identical cards is the default to
  avoid; let one item lead.
- **The mobile layout is its own composition**, not a squeezed desktop. Check line counts, not just widths.
- **Images carry the subject.** Real photographs of the place or thing beat stock, and beat abstract shapes.
  A placeholder, an icon or a gradient blob is worse than no image.

## Related

Accessibility implementation detail and the token layer: `references/design-and-accessibility.md`.
Verified metadata and heading order: `references/technical-seo.md`.
