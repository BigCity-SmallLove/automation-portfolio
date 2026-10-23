"""Dependency-free checks for this buildless project-subpath website."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import re
ROOT=Path(__file__).resolve().parents[1]/'site'
class Page(HTMLParser):
    def __init__(self):super().__init__();self.ids=set();self.refs=[];self.images=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:self.ids.add(attrs['id'])
        for key in ('src','href'):
            if attrs.get(key):self.refs.append(attrs[key])
        if tag=='img':self.images.append(attrs)
page=Page();html=(ROOT/'index.html').read_text(encoding='utf-8');page.feed(html)
for ref in page.refs:
    url=urlsplit(ref)
    if url.scheme:
        assert url.scheme=='https',ref
        assert not url.username and not url.password,ref
    elif url.path:
        assert not url.path.startswith('/'),ref
        path=(ROOT/unquote(url.path)).resolve()
        assert path.is_relative_to(ROOT.resolve()) and path.is_file(),ref
    elif url.fragment:assert url.fragment in page.ids,ref
assert len(page.images)==4
assert all(image.get('alt') and image.get('width') and image.get('height') for image in page.images)
for project in ('sheetforge','folderpilot','logsentry'):
    assert 'https://github.com/BigCity-SmallLove/'+project+'-showcase' in html
assert not re.search(r'untagged-|restricted|Full quick start \(private\)',html,re.I)
assert not (ROOT/'assets/provenance.json').exists()
assert not list(ROOT.rglob('*.json')), 'Only runtime resources belong in the deployed site'
assert 'name="viewport"' in html and '<html lang="en">' in html
print('PASS: relative resources, four real image references, fragments, HTTPS links, current public project links and project-subpath readiness')
