#!/usr/bin/env python3
"""Check built HTML links, fragments, assets, canonical URLs and organizer portraits."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
import re
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.refs, self.ids, self.portraits, self.canonical = [], set(), [], []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'): self.ids.add(a['id'])
        for key in ('href', 'src', 'poster'):
            if a.get(key): self.refs.append(a[key])
        if tag == 'img' and 'organizer-photo' in a.get('class', '').split():
            self.portraits.append(a.get('src', ''))
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical.append(a.get('href'))

pages = {p: Page(p.read_text()) for p in root.rglob('*.html')}
errors, legacy = set(), set()
checked = 0
for path, page in pages.items():
    rel = path.relative_to(root).as_posix()
    archive = rel.startswith('2026/')
    report = legacy if archive else errors
    url = 'https://cpal.cc/' + rel.removesuffix('index.html')
    text = path.read_text()
    if not archive:
        if re.search(r'dakebu\.github\.io/cpal-website-2027|/cpal-website-2027', text, re.I):
            report.add(f'{rel}: preview path remains')
        if not page.canonical or any(not v.startswith('https://cpal.cc/') for v in page.canonical):
            report.add(f'{rel}: incorrect canonical URL')
    for ref in page.refs:
        target = urlsplit(urljoin(url, ref))
        if target.scheme not in ('https', 'http') or target.netloc != 'cpal.cc': continue
        checked += 1
        dest = root / unquote(target.path).lstrip('/')
        if dest.is_dir(): dest /= 'index.html'
        if not dest.is_file():
            report.add(f'{rel}: missing {ref}')
        elif target.fragment and dest in pages and unquote(target.fragment) not in pages[dest].ids:
            report.add(f'{rel}: missing fragment {ref}')
    for src in page.portraits:
        if not src.startswith('/assets/images/organizers/'):
            report.add(f'{rel}: nonlocal portrait {src}')
committee = pages.get(root/'organization_committee/index.html')
if not committee or len(committee.portraits) != 24: errors.add('Expected 24 organizer portraits')
for route in ('', 'call_for_papers', 'deadlines', 'organization_committee', 'venue', 'registration', 'openreview', 'past', '2026', 'cfp', 'other_years'):
    if root/route/'index.html' not in pages: errors.add(f'Missing main page: /{route}')
if (root/'CNAME').read_text().strip() != 'cpal.cc': errors.add('Incorrect CNAME')
print(f'{len(pages)} HTML pages; {checked} internal references; {len(committee.portraits) if committee else 0} organizer portraits')
for e in sorted(errors): print('ERROR:', e)
for e in sorted(legacy): print('ARCHIVE:', e)
print(f'{len(errors)} current-site errors; {len(legacy)} archive issues')
sys.exit(bool(errors or legacy))
