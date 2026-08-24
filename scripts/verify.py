#!/usr/bin/env python3
from pathlib import Path
import re, sys, json
ROOT=Path(__file__).resolve().parents[1]
required=['index.html','404.html','favicon.svg','social-card.png','robots.txt','sitemap.xml','README.md','assets/site.css','assets/site.js']
fail=[]
def need(cond,msg):
    if not cond: fail.append(msg)
for p in required: need((ROOT/p).is_file(),f'missing {p}')
html=(ROOT/'index.html').read_text()
js=(ROOT/'assets/site.js').read_text()
for s in ['<main id="main">','<nav ','role="img"','id="calculator-title"','id="assessment-form"','mailto:enzo491kw@gmail.com','application/ld+json','https://492kw.github.io/ai-deployment-consultant/']:
    need(s in html,f'missing required HTML contract: {s}')
need(html.count('enzo491kw@gmail.com')>=5,'contact email is not consistently present')
for banned in [r'\bour team\b',r'\bwe\b',r'\bfree\b',r'85%\+',r'\b10x\b',r'twice as fast',r'thousands of hours',r'\bstaff\b',r'\benterprise\b']:
    need(not re.search(banned,html,re.I),f'forbidden public claim/language: {banned}')
for asset in re.findall(r'(?:href|src)="([^"]+)"',html):
    if not re.match(r'^(https?:|mailto:|#)',asset): need((ROOT/asset).is_file(),f'missing referenced local asset: {asset}')
need('Math.min(95' in js and 'Intl.NumberFormat' in js,'calculator range or AUD formatting missing')
need("window.location.href = 'mailto:enzo491kw@gmail.com" in js,'mailto composition missing')
need('form.checkValidity()' in js,'form validation missing')
try:
    data=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',html).group(1)); need(data['email']=='enzo491kw@gmail.com','JSON-LD email incorrect')
except Exception as e: fail.append(f'JSON-LD invalid: {e}')
if fail:
    print('FAIL'); print('\n'.join('- '+x for x in fail)); sys.exit(1)
print('PASS: %d required artifacts; metadata, accessibility contracts, copy guardrails, calculator and mailto checks passed.'%len(required))
