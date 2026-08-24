# Implementation Plan — AI Deployment Consultant

## Scope

Build and publish a dependency-free GitHub Pages marketing site for a solo SMB AI deployment consultant. Implement all copy, interaction, visual and SEO requirements in the design specification.

## Files and tasks

1. `index.html`
   - Add semantic landmarks, sticky navigation, hero, workflow map, all required sections, FAQ, assessment form and footer.
   - Add canonical, Open Graph, Twitter metadata and LocalBusiness/ProfessionalService JSON-LD using only `enzo491kw@gmail.com`.
2. `assets/site.css`
   - Define the paper/copper/sage token system; build responsive grids, workflow presentation, calculator panel, accessible focus states and reduced-motion behaviour.
3. `assets/site.js`
   - Implement mobile nav state, calculator maths/formatting, inline form errors, mailto subject/body composition and no-transmission statement.
4. `404.html`, `favicon.svg`, `social-card.png`
   - Provide matching fallback/brand assets. Generate the social card locally without a network asset dependency.
5. `robots.txt`, `sitemap.xml`, `README.md`
   - Supply crawl directives, canonical sitemap and reproducible instructions.
6. `scripts/verify.py`
   - Check required files, semantic strings, email/canonical/JSON-LD, prohibited public copy, referenced local assets, calculator contract and form mailto logic.
7. Local visual evidence
   - Serve locally, execute verification, capture 1440/1024/768/390 full-page renders, inspect, repair and recapture.
8. Publication (blocked pending identity)
   - Re-verify active GitHub identity equals `492kw`; create public `492kw/ai-deployment-consultant`, push `main`, enable Pages, inspect build and live artefacts. Do not use `enzo491kw-design`.

## Checks

- `python3 scripts/verify.py`
- HTTP 200 for all local assets.
- Browser exercise: calculator, invalid/valid form flow, keyboard focus, reduced motion, console and overflow checks.
- Full-page visual capture at 1440, 1024, 768 and 390 CSS pixels.
- Before any publication, verify `gh api user --jq .login` returns `492kw`.
- After publication, confirm HEAD parity, Pages API state, cache-busted HTML content, live asset status/content types and the same browser checks.
