# Design and Accessibility

## Google Stitch workflow (design-first)

Standing rule: user-visible UI goes through Google Stitch before any markup is written. Load
`google-stitch-concepts` and follow it - this reference only maps the workflow to blog builds.

1. Understand brand identity (from PROJECT.md or discovery).
2. Research 3-5 real niche websites; analyse reference designs for structure, not to copy.
3. Develop the visual direction (accent, restraint vs invention, type pairing).
4. Define the palette, typography, spacing and layout scale as a token file.
5. Design desktop, tablet and mobile layouts for each key template (home, article, category).
6. Design reusable components (card, header, footer, article meta, FAQ, CTA).
7. Review accessibility and navigation against the concept before coding.
8. Convert into Astro components, matching the concept pixel-for-pixel where it matters.

Prioritise premium, modern, professional and readable. Avoid unnecessary animation, heavy libraries and
bulky effects. The site must serve readability, navigation, content discovery, search and advertising UX -
not just look attractive. For every Stitch concept, audit the palette to zero off-token colours and record
deltas in NOTES.md (see `google-stitch-concepts`).

## Design system

- Token file is the single source of truth; regenerate CSS from it, never hand-write hexes into styles.
- A palette gate fails the build on any colour outside the token set (resolve `var()` and normalise colour
  forms before comparing).
- Self-host fonts (`@fontsource`); no CDN font requests, no FOUT.
- Responsive, mobile-first; check headline line count at 390, not just width.
- Respect `prefers-reduced-motion`; never hide content by default (a reveal that fails leaves blank
  sections).

## Accessibility (WCAG 2.2, part of development and QA, not a final step)

- Semantic HTML: `header`/`main`/`footer`/`nav`/`article`, one H1, ordered headings.
- Keyboard navigation and visible focus states; no focus traps except real modals.
- Colour contrast: AA minimum for text, 3:1 for large text and UI components; audit with axe.
- Accessible forms: labels, `aria-describedby` for errors synced to `aria-invalid`, `novalidate` kept when
  the handler presents its own errors.
- Image descriptions: meaningful alt on content images, empty alt for decorative.
- Screen-reader compatibility: live regions for changing counts, focus handed to revealed content.
- Reduced motion honoured, including any scroll animation.
- Tables get `scope="col"`, a caption and a focusable scroll wrapper (build-time rehype plugin).
- Run axe-core on the BUILT site per route (home, article, category, search, 404); report violations per
  route, not a verdict. Zero serious/critical is the gate.

## Verification

- [ ] Stitch concept committed and on-palette before markup
- [ ] axe clean (no serious/critical) on every template type
- [ ] contrast passes on all token colour pairs used for text
- [ ] keyboard-only navigation reaches every link and control
- [ ] reduced-motion path shows all content
- [ ] responsive renders correct at 1280 and 390 without horizontal overflow
