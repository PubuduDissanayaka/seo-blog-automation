# Design and Accessibility

## Design direction

The direction, the design-system workflow, the design skill stack and the design gates live in
`references/ui-ux-design.md`. Run that first. This file covers the token layer and the accessibility
implementation that direction lands on.

Two rules carry over and are not negotiable: the token file is the only place colour, type and spacing
values exist, and every design decision is verified in a real browser rather than asserted.

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

- [ ] Design direction committed and on-palette before markup (see `references/ui-ux-design.md`)
- [ ] axe clean (no serious/critical) on every template type
- [ ] contrast passes on all token colour pairs used for text
- [ ] keyboard-only navigation reaches every link and control
- [ ] reduced-motion path shows all content
- [ ] responsive renders correct at 1280 and 390 without horizontal overflow
