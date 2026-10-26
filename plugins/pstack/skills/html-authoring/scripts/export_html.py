#!/usr/bin/env python3
"""Inline local CSS/JS in a trusted author-owned HTML file; no dependencies."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re

class Resources(HTMLParser):
    def __init__(self):
        super().__init__()
        self.styles = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('style'):
            self.styles.append(attrs['style'])
        for key in ('src', 'srcset', 'poster', 'data'):
            value = attrs.get(key)
            if value and not value.startswith(('data:', '#')):
                raise ValueError(f'Unembedded {tag} {key}: {value}')
        if tag == 'link' and attrs.get('rel') != 'canonical':
            raise ValueError('Unembedded link resource')
        if tag in ('image', 'use'):
            value = attrs.get('href', attrs.get('xlink:href', ''))
            if value and not value.startswith(('data:', '#')):
                raise ValueError(f'Unembedded SVG resource: {value}')

def embed(source):
    text = source.read_text()
    def replace(match):
        tag = match.group(0)
        parser = HTMLParser()
        attributes = {}
        parser.handle_starttag = lambda _, attrs: attributes.update(attrs)
        parser.feed(tag)
        name = 'href' if tag.lower().startswith('<link') else 'src'
        if name == 'href' and attributes.get('rel') != 'stylesheet':
            return tag
        location = attributes.get(name, '')
        if not location or ':' in location or location.startswith('//'):
            raise ValueError(f'Expected local resource: {location}')
        content = (source.parent / location).read_text()
        kind = 'style' if name == 'href' else 'script'
        if re.search(rf'</{kind}\b', content, re.I):
            raise ValueError(f'Cannot safely inline closing {kind} tag')
        if name == 'href' and set(attributes) - {'href', 'rel'}:
            raise ValueError('Stylesheet attributes need explicit adaptation before export')
        if name == 'src' and set(attributes) - {'src'}:
            raise ValueError('Script attributes need explicit adaptation before export')
        return f'<{kind}>\n{content}\n</{kind}>'
    text = re.sub(r'<link\b[^>]*>|<script\b[^>]*\bsrc\s*=\s*["\'][^"\']+["\'][^>]*>\s*</script\s*>', replace, text, flags=re.I)
    resources = Resources()
    resources.feed(text)
    css = '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', text, re.I | re.S))
    css += '\n' + '\n'.join(resources.styles)
    if re.search(r'@import\b', css, re.I):
        raise ValueError('CSS imports must be embedded before export')
    for value in re.findall(r'url\(([^)]*)\)', css, re.I):
        if not value.strip().strip("\"'").startswith(('data:', '#')):
            raise ValueError('CSS resources must be embedded before export')
    if re.search(r'\b(?:fetch|import)\s*\(|\bXMLHttpRequest\b', text):
        raise ValueError('Dynamic resources require manual offline packaging')
    return text

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    try:
        if args.source.resolve() == args.output.resolve():
            raise ValueError('Keep output separate from editable source')
        result = embed(args.source)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result)
        print(args.output)
    except (ValueError, OSError) as error:
        parser.exit(1, f'{error}\n')
