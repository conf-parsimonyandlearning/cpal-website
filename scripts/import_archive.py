#!/usr/bin/env python3
"""Import the 2026 build (built with --baseurl /2026) and isolate its links."""
from pathlib import Path
import re
import shutil
import sys
source = Path(sys.argv[1]).resolve()
target = Path(__file__).resolve().parents[1] / '2026'
shutil.copytree(source, target, dirs_exist_ok=True)
for path in list(target.rglob('*')):
    if path.is_file() and (path.name == 'CLAUDE.md' or 'todo' in path.relative_to(target).parts):
        path.unlink()
for path in target.rglob('*.html'):
    text = path.read_text()
    def isolate(match):
        prefix, url, quote = match.groups()
        if url == 'https://cpal.cc': url += '/'
        if url.startswith('https://cpal.cc/'):
            url = url.removeprefix('https://cpal.cc')
        if url.startswith('/') and not url.startswith(('//', '/2026/', '/2026#')) and url != '/2026':
            url = '/2026' + url
        if url == 'marco.schubert@tuebingen-info.de': url = 'mailto:' + url
        if prefix.startswith('content=') or (prefix.startswith('href=') and 'rel="canonical"' in match.string[max(0, match.start()-30):match.start()]):
            url = 'https://cpal.cc' + url if url.startswith('/') else url
        return prefix + url + quote
    text = re.sub(r'((?:href|src|content)=[\"\'])([^\"\']+)([\"\'])', isolate, text)
    path.write_text(text)
print('Imported isolated 2026 archive')
