#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RECIPIENT = 'enzo491kw@gmail.com'
required = ['index.html', '404.html', 'favicon.svg', 'social-card.png', 'robots.txt', 'sitemap.xml', 'README.md', 'assets/site.css', 'assets/site.js']
fail = []


def need(condition, message):
    if not condition:
        fail.append(message)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.text = []
        self.visible_attrs = []
        self.links = []
        self.active_link = None

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        attrs = dict(attrs)
        if tag == 'a':
            self.links.append([attrs.get('href', ''), ''])
            self.active_link = len(self.links) - 1
        for name in ('alt', 'title', 'aria-label'):
            if name in attrs:
                self.visible_attrs.append(attrs[name])

    def handle_startendtag(self, tag, attrs):
        for name, value in attrs:
            if name in ('alt', 'title', 'aria-label'):
                self.visible_attrs.append(value or '')

    def handle_endtag(self, tag):
        if tag == 'a':
            self.active_link = None
        if tag in self.stack:
            self.stack = self.stack[:len(self.stack) - 1 - self.stack[::-1].index(tag)]

    def handle_data(self, data):
        if 'script' not in self.stack and 'style' not in self.stack:
            self.text.append(data)
        if self.active_link is not None:
            self.links[self.active_link][1] += data


for path in required:
    need((ROOT / path).is_file(), f'missing {path}')

html = (ROOT / 'index.html').read_text()
js = (ROOT / 'assets/site.js').read_text()
page_404 = (ROOT / '404.html').read_text()

for contract in ['<main id="main">', '<nav ', 'id="calculator-title"', 'id="assessment-form"', 'application/ld+json', 'https://492kw.github.io/ai-deployment-consultant/']:
    need(contract in html, f'missing required HTML contract: {contract}')

parser = PageParser()
parser.feed(html)
visible_text = ''.join(parser.text)
visible_metadata = ' '.join(parser.visible_attrs)
visible_text_normalized = re.sub(r'\s+', ' ', visible_text).strip()

brief_required = [
    'AI deployment brief / 01',
    'Move one bottleneck into a safe first rollout.',
    'The bottleneck',
    'Enquiries arrive incomplete and scattered across email, forms and call notes.',
    'The first useful change',
    'Prepare a reviewable intake with the key details, missing information and recommended next step.',
    'The safeguard',
    'Hold unusual, incomplete or sensitive cases for a person to check before anything is sent or recorded.',
    'Operational outcome',
    'A clear next action: reply, booking or CRM update.',
    'A bounded deployment—not automation for its own sake.',
]
for text in brief_required:
    need(text in visible_text_normalized, f'missing deployment brief content: {text}')

need('<figure' in html and 'class="deployment-brief"' in html, 'semantic deployment brief figure is missing')
need('aria-labelledby="brief-title"' in html and 'aria-describedby="brief-caption"' in html, 'deployment brief accessible labelling is missing')
for removed in [
    'Workflow field map',
    'You know the work.',
    'svg class="workflow-map"',
    'class="map-wrap"',
    'class="map-mobile"',
    'class="map-grid"',
    'class="route"',
    'class="feedback"',
    'class="stage"',
    'class="gate"',
    'class="input"',
    'class="output"',
]:
    need(removed not in html, f'removed workflow-map markup/text remains: {removed}')
for removed_selector in ['.workflow-map', '.map-wrap', '.map-mobile', '.map-grid', '.route', '.feedback', '.stage', '.gate', '.input rect', '.output rect']:
    need(removed_selector not in (ROOT / 'assets/site.css').read_text(), f'removed workflow-map CSS remains: {removed_selector}')

need(RECIPIENT not in visible_text, 'email address appears in a visible index.html text node')
need(RECIPIENT not in visible_metadata, 'email address appears in index.html alt, title or aria-label text')
need(RECIPIENT not in page_404, 'email address appears in 404.html')
mail_links = [(href, label.strip()) for href, label in parser.links if href.startswith('mailto:')]
need(len(mail_links) >= 2, 'expected assessment and footer mailto links')
need(all(href.split(':', 1)[1].split('?', 1)[0] == RECIPIENT for href, _ in mail_links), 'mail link recipient is not exact')
need(any(label == 'Email Simon' and 'subject=Workflow%20assessment%20enquiry' in href for href, label in mail_links), 'assessment Email Simon mailto subject is missing')
need(any(label in ('Simon', 'Email Simon') and href == f'mailto:{RECIPIENT}' for href, label in mail_links), 'footer Simon/Email Simon mail link is missing')

for banned in [r'\bour team\b', r'\bwe\b', r'\bfree\b', r'85%\+', r'\b10x\b', r'twice as fast', r'thousands of hours', r'\bstaff\b', r'\benterprise\b']:
    need(not re.search(banned, html, re.I), f'forbidden public claim/language: {banned}')

for asset in re.findall(r'(?:href|src)="([^"]+)"', html):
    if not re.match(r'^(https?:|mailto:|#)', asset):
        need((ROOT / asset).is_file(), f'missing referenced local asset: {asset}')

need('Math.min(95' in js and 'Intl.NumberFormat' in js, 'calculator range or AUD formatting missing')
need(f"window.location.href = 'mailto:{RECIPIENT}" in js, 'mailto composition missing')
need('form.checkValidity()' in js, 'form validation missing')

try:
    json_ld_match = re.search(r'<script\s+type="application/ld\+json"\s*>(.*?)</script>', html, re.S)
    if not json_ld_match:
        raise ValueError('JSON-LD script not found')
    json_ld = json.loads(json_ld_match.group(1))
    serialized = json.dumps(json_ld)
    need(RECIPIENT not in serialized, 'JSON-LD contains the email address')
    need('email' not in serialized.lower() and 'contactpoint' not in serialized.lower(), 'JSON-LD retains email/contactPoint metadata')
except Exception as exc:
    fail.append(f'JSON-LD invalid: {exc}')

if fail:
    print('FAIL')
    print('\n'.join('- ' + item for item in fail))
    sys.exit(1)
print('PASS: %d required artifacts; visible-email, mailto recipient/labels, JSON-LD privacy, metadata, accessibility contracts, copy guardrails, calculator and form checks passed.' % len(required))
