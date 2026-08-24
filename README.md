# AI Deployment Consultant

A dependency-free static site for GitHub Pages.

## Local run

```sh
cd /home/simon/ai-deployment-consultant
python3 scripts/verify.py
python3 -m http.server 4173
```

Open `http://127.0.0.1:4173/`.

## Verification

`python3 scripts/verify.py` checks required artefacts, copy guardrails, metadata, internal references, calculator math contract and the email form implementation. Browser visual and interaction checks are recorded separately in the delivery evidence.

## Deployment

Deploy `main` to the public repository `492kw/ai-deployment-consultant` and configure GitHub Pages from the repository root. The canonical Pages URL is `https://492kw.github.io/ai-deployment-consultant/`.
