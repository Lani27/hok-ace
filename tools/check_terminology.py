"""Check published text and subtitle copy against the reviewed patch glossary.

Usage: python tools/check_terminology.py --glossary /path/to/hok_terminology.py
This checks audited English aliases; image lettering requires a separate visual/OCR review.
"""
import argparse
import ast
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unicodedata

from beginner_content import RULES, TACTICIANS, KEYWORDS, VIDEOS
from beginner_lineups import LINEUPS, CARD_EFFECTS
from build_launch_page import GROUPS

ROOT = Path(__file__).resolve().parents[1]


def normalized(text):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', text)
                  .replace('’', "'").replace('‘', "'")).casefold()


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings(item)
    elif isinstance(value, (tuple, list)):
        for item in value:
            yield from strings(item)


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag in ('style', 'script'):
            self.hidden += 1
        for key, value in attrs:
            if key in ('alt', 'aria-label', 'placeholder') and value:
                self.text.append(value)

    def handle_endtag(self, tag):
        if tag in ('style', 'script'):
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden:
            self.text.append(data)


def check(glossary):
    terms = {}
    # Read literal dictionaries without executing the external Python module.
    for node in ast.parse(glossary.read_text(encoding='utf-8')).body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.value, ast.Dict):
            terms.update(ast.literal_eval(node.value))
    aliases = json.loads((ROOT / 'tools/glossary_aliases.json').read_text(encoding='utf-8'))
    missing = set(aliases.values()) - terms.keys()
    if missing:
        raise ValueError(f'Glossary is missing reviewed source terms: {sorted(missing)}')
    # Protect valid full names, e.g. Zhang Liang must not match the old alias Liang.
    canonical = {normalized(value) for value in terms.values()}
    canonical |= {value + 's' for value in canonical}
    protect = re.compile(r'(?<!\w)(?:' + '|'.join(re.escape(t) for t in sorted(canonical, key=len, reverse=True)) + r')(?!\w)')
    patterns = [(old, terms[chinese], re.compile(r'(?<!\w)' + re.escape(normalized(old)) + r'(?!\w)'))
                for old, chinese in aliases.items()]
    sources = {
        'beginner_content.py': [RULES, TACTICIANS, KEYWORDS, VIDEOS],
        'beginner_lineups.py': [LINEUPS, CARD_EFFECTS],
        'build_launch_page.py': GROUPS,
        'keyword_subtitles.json': json.loads((ROOT / 'tools/keyword_subtitles.json').read_text(encoding='utf-8')),
    }
    repairs = json.loads((ROOT / 'tools/image_lettering_repairs.json').read_text(encoding='utf-8'))
    sources['image_lettering_repairs.json'] = [item['text'] for items in repairs.values() for item in items if 'text' in item]
    for path in sorted((ROOT / 'docs/assets/beginner-guide/keyword-videos').glob('*.srt')):
        sources[str(path.relative_to(ROOT))] = path.read_text(encoding='utf-8')
    for path in sorted((ROOT / 'docs').rglob('*.html')):
        parsed = VisibleText()
        parsed.feed(path.read_text(encoding='utf-8'))
        sources[str(path.relative_to(ROOT))] = parsed.text
    failures = set()
    for source, content in sources.items():
        for text in strings(content):
            text = protect.sub(' ', normalized(text))
            for old, expected, pattern in patterns:
                if pattern.search(text):
                    failures.add(f'{source}: {old} -> {expected}')
    if failures:
        raise SystemExit('\n'.join(sorted(failures)))
    review_path = ROOT / 'tools/image_glossary_review.json'
    image_count = 0
    if review_path.exists():
        review = json.loads(review_path.read_text(encoding='utf-8'))
        if hashlib.sha256(glossary.read_bytes()).hexdigest() != review['glossary_sha256']:
            raise SystemExit('Glossary changed since image review; review affected image lettering again.')
        for file, digest in review['images'].items():
            if hashlib.sha256((ROOT / 'docs/assets' / file).read_bytes()).hexdigest() != digest:
                raise SystemExit(f'Image changed since glossary review: {file}')
        image_count = len(review['images'])
    print(f'PASS: {len(aliases)} reviewed aliases checked across {len(sources)} source/page groups.')
    if image_count:
        print(f'PASS: {image_count} images match the visually reviewed glossary revision.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--glossary', type=Path, required=True)
    check(parser.parse_args().glossary)
