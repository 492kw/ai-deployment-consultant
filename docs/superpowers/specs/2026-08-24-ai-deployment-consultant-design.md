# AI Deployment Consultant — Design Specification

Date: 2026-08-24
Status: approved for implementation

## Acceptance contract

Build a public, GitHub Pages-compatible one-page site for Brisbane and remote Australian SMBs. It positions an owner-operated consultant in first-person singular, uses `enzo491kw@gmail.com` as the only published contact email, and offers scoped engagements quoted after assessment. It must not claim client outcomes, publish prices, promise a free service, imply a team, or make universal ROI/statistical claims.

## Audience and job

The audience is an SMB owner or operations lead with recurring admin work, disconnected tools, or an AI idea that has not made it into the real workflow. The page turns a vague AI enquiry into a well-scoped email assessment.

## Alternatives considered

1. Product-dashboard/SaaS visual language: rejected because this is a consultative service, not software for sale.
2. Generic warm-card consultancy page: rejected because it would not explain the work or distinguish the service.
3. Dark technical/AI aesthetic: rejected because it conflicts with the established light, practical commercial family.
4. Workflow field map: removed because abstract grids, routes, gates and tiny labels compete with the message and duplicate the later 30-day method.
5. Selected: a bottleneck-to-rollout deployment brief. It is a concrete scoped working artefact that makes the diagnostic, first change, human safeguard and operational outcome legible at a glance.

## Selected design system

### Tokens

- Paper: `#F6F1E8`
- Surface: `#FFFDFC`
- Ink: `#18221F`
- Muted ink: `#4B5651`
- Copper: `#7E3E1E`
- Copper dark: `#5E2913`
- Sage: `#607763`
- Ochre highlight: `#D9B35F`
- Rule: `#D9D0C2`

### Type

- Display: Georgia, Cambria, "Times New Roman", serif — compact sentence-case headings with an editorial character.
- Body: Inter, ui-sans-serif, system-ui, sans-serif — readable, local-safe system fallbacks.
- Utility: ui-monospace, SFMono-Regular, Consolas, monospace — labels, calculator values and scoped status markers.

### Layout

A centred 1180px canvas uses an asymmetrical hero: copy at left and a self-contained HTML deployment brief at right. The brief is a warm surface card with a fine copper header rule, offset warm shadow, three content sections separated by thin rules, and a distinct sage operational-outcome panel. Its content remains in the same order at every viewport; tablet and mobile stack naturally without changing the concept. Sections elsewhere alternate between open paper and light outlined surfaces. The calculator remains an instrument panel rather than a marketing pricing card.

### Signature: bottleneck-to-rollout deployment brief

The hero artefact is a semantic `figure` with a labelled brief title, grouped HTML sections and a caption. It carries the exact hierarchy:

- Utility label: “AI deployment brief / 01”
- Brief title: “Move one bottleneck into a safe first rollout.”
- The bottleneck: “Enquiries arrive incomplete and scattered across email, forms and call notes.”
- The first useful change: “Prepare a reviewable intake with the key details, missing information and recommended next step.”
- The safeguard: “Hold unusual, incomplete or sensitive cases for a person to check before anything is sent or recorded.”
- Operational outcome: “A clear next action: reply, booking or CRM update.”
- Caption: “A bounded deployment—not automation for its own sake.”

Small status marks—Scoped, Human-reviewed and Ready for rollout—clarify deployment scope. They are not decoration. There are no SVG diagrams, coordinate grids, routes, arrows, feedback loops, stage circles, diamond gates or alternative mobile sequences. Decorative rules are only boundaries between content groups and never sit behind text.

## Content and claims guardrails

- Say “I”, “my”, “you” and “your business”; never “we”, “our team”, “staff” or enterprise-team language.
- Explain last-mile integration as fitting a useful tool into the steps, hand-offs and approvals already used in a business.
- Forward Deployed Engineering may appear only in the FAQ as secondary context. It does not imply a team being embedded with a client.
- The intake scenario is explicitly labelled “Illustrative scenario”, describes a hypothetical service-business enquiry flow, and does not cite a result.
- Calculator wording is “potentially returned”, “indicative” and “illustrative, not a guarantee”. It sends no data.
- No invented testimonials, logos, client names, case studies, performance statistics, price, or “free” offer.

## Architecture

- `index.html`: semantic one-page document, metadata, JSON-LD and HTML deployment brief.
- `assets/site.css`: responsive tokens, layout, focus/reduced-motion styles and responsive deployment-brief styling.
- `assets/site.js`: nav state, calculator, accessible validation and mailto composition.
- `404.html`, `favicon.svg`, `social-card.png`, `robots.txt`, `sitemap.xml`: Pages/SEO support.
- `scripts/verify.py`: deterministic structural, claims, hero-contract, assets and calculator/mailto checks without third-party packages.
- `README.md`: local serving and verification instructions.

## Test and visual audit plan

1. Run `python3 scripts/verify.py`.
2. Serve the directory with Python HTTP server and inspect link/asset responses.
3. Exercise calculator calculations and the assessment form's invalid and valid paths in a real browser.
4. Capture and inspect full pages at 1440, 1024, 768 and 390 CSS pixels; repair material layout, contrast, overflow or focus issues.
5. On deployment, repeat content, asset, browser and capture checks against the cache-busted Pages URL.

## Acceptance criteria

- The full page has sticky navigation, hero CTAs, the deployment brief, last-mile explanation, bottlenecks, four-week method, guardrails/evals, illustrative scenario, calculator, fit, FAQ, accessible email assessment form and footer.
- The hero brief is standalone and concrete: all meaningful content is real HTML text, grouped in the approved diagnostic/deployment order, and contains the visible human-review safeguard and operational outcome.
- All contact and structured metadata use exactly `enzo491kw@gmail.com`.
- The site is dependency-free, responsive, keyboard usable, reduced-motion aware and GitHub Pages safe.
- Every required public artifact exists; deterministic verification passes; no unfinished-placeholder markers, removed workflow-map material or contradictory commercial statements remain.
