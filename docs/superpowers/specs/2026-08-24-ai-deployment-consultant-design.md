# AI Deployment Consultant — Design Specification

Date: 2026-08-24
Status: approved for implementation

## Acceptance contract

Build a public, GitHub Pages-compatible one-page site for Brisbane and remote Australian SMBs. It must position an owner-operated consultant in first-person singular, use `enzo491kw@gmail.com` as the only published contact email, and offer scoped engagements quoted after assessment. It must not claim client outcomes, publish prices, promise a free service, imply a team, or make universal ROI/statistical claims.

## Audience and job

The audience is an SMB owner or operations lead with recurring admin work, disconnected tools, or an AI idea that has not made it into the real workflow. The page's job is to turn a vague AI enquiry into a well-scoped email assessment.

## Alternatives considered

1. Product-dashboard/SaaS visual language: rejected because this is a consultative service, not software for sale.
2. Generic warm-card consultancy page: rejected because it would not explain the work or distinguish the service.
3. Dark technical/AI aesthetic: rejected because it conflicts with the established light, practical commercial family.
4. Selected: a field-notebook inspired workflow map. It turns the last-mile method into the memorable visual and keeps every other element quiet and useful.

## Selected design system

### Tokens

- Paper: `#F6F1E8`
- Surface: `#FFFDFC`
- Ink: `#18221F`
- Muted ink: `#4B5651`
- Copper: `#A95F32`
- Copper dark: `#7E3E1E`
- Sage: `#607763`
- Ochre highlight: `#D9B35F`
- Rule: `#D9D0C2`

### Type

- Display: Georgia, Cambria, "Times New Roman", serif — compact sentence-case headings with an editorial character.
- Body: Inter, ui-sans-serif, system-ui, sans-serif — readable, local-safe system fallbacks.
- Utility: ui-monospace, SFMono-Regular, Consolas, monospace — labels, calculator values and process coordinates.

### Layout

A centred 1180px canvas uses an asymmetrical hero: copy at left and a real SVG workflow field map at right. Sections alternate between open paper and light outlined surfaces. Process stages carry a meaningful 01–04 sequence. The calculator is an instrument panel rather than a marketing pricing card.

### Signature: workflow field map

The bespoke accessible SVG maps messy inputs through Observe, Scope, Build/Test and Roll Out. It includes human approval gates, feedback loops and measurable outputs. It is an explanatory diagram with text alternatives, not decorative art.

## Content and claims guardrails

- Say “I”, “my”, “you” and “your business”; never “we”, “our team”, “staff” or enterprise-team language.
- Explain last-mile integration as fitting a useful tool into the steps, hand-offs and approvals already used in a business.
- Forward Deployed Engineering may appear only in the FAQ as secondary context. It does not imply a team being embedded with a client.
- The intake scenario is explicitly labelled “Illustrative scenario”, describes a hypothetical service-business enquiry flow, and does not cite a result.
- Calculator wording is “potentially returned”, “indicative” and “illustrative, not a guarantee”. It sends no data.
- No invented testimonials, logos, client names, case studies, performance statistics, price, or “free” offer.

## Architecture

- `index.html`: semantic one-page document, metadata, JSON-LD, content and SVG.
- `assets/site.css`: responsive tokens, layout, focus/reduced-motion styles.
- `assets/site.js`: nav state, calculator, accessible validation and mailto composition.
- `404.html`, `favicon.svg`, `social-card.png`, `robots.txt`, `sitemap.xml`: Pages/SEO support.
- `scripts/verify.py`: deterministic structural, claims, assets and calculator/mailto checks without third-party packages.
- `README.md`: local serving and verification instructions.

## Test and visual audit plan

1. Run `python3 scripts/verify.py`.
2. Serve the directory with Python HTTP server and inspect link/asset responses.
3. Exercise calculator calculations and the assessment form's invalid and valid paths in a real browser.
4. Capture and inspect full pages at 1440, 1024, 768 and 390 CSS pixels; repair material layout, contrast, overflow or focus issues.
5. On deployment, repeat content, asset, browser and capture checks against the cache-busted Pages URL.

## Acceptance criteria

- The full page has sticky navigation, hero CTAs, last-mile explanation, bottlenecks, four-week method, guardrails/evals, illustrative scenario, calculator, fit, FAQ, accessible email assessment form and footer.
- All contact and structured metadata use exactly `enzo491kw@gmail.com`.
- The site is dependency-free, responsive, keyboard usable, reduced-motion aware and GitHub Pages safe.
- Every required public artifact exists; deterministic verification passes; no unfinished-placeholder markers or contradictory commercial statements remain.
