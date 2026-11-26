#!/usr/bin/env python3
"""Check the SEO keyword-uniqueness guards (stdlib only).

Rules enforced (from seo-article-planning-schedule):
  1. exactly 1 primary keyword per article, never reused
  2. exactly 5 secondaries per article, each used once site-wide
  3. a keyword that is one article's primary can never be another article's secondary
  4. (optional) flag keywords whose main token already appears in a live sitemap slug

Usage:
  python3 check-keyword-uniqueness.py --map keywords.json
  python3 check-keyword-uniqueness.py --map keywords.json --sitemap https://site/sitemap-index.xml

keywords.json is a list of objects:
  [{"article_id": "A-001", "primary": "snake plant care", "secondaries": ["...", ...]}]
"""
import argparse
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET


def normalize(kw: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", kw.lower()).strip()


def fetch_sitemap_urls(url: str, seen=None) -> set:
    seen = seen or set()
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        root = ET.fromstring(resp.read())
    urls = set()
    for elem in root.iter():
        if elem.tag.split("}")[-1] == "loc" and elem.text:
            u = elem.text.strip()
            if u.endswith(".xml") and u not in seen:
                seen.add(u)
                urls |= fetch_sitemap_urls(u, seen)
            else:
                urls.add(u)
    return urls


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--map", required=True, help="path to keywords.json")
    ap.add_argument("--sitemap", help="live sitemap index URL (optional)")
    args = ap.parse_args()

    with open(args.map, encoding="utf-8") as f:
        articles = json.load(f)

    errors = []

    # Pass 1: collect all primaries, flag duplicates (order-independent).
    primaries = {}
    for a in articles:
        aid = a.get("article_id", "?")
        pk = normalize(a["primary"])
        if pk in primaries:
            errors.append(f"DUPLICATE PRIMARY '{a['primary']}' (also {primaries[pk]})")
        else:
            primaries[pk] = aid

    # Pass 2: check secondaries against the complete primaries set (order-independent).
    secondaries = {}
    for a in articles:
        aid = a.get("article_id", "?")
        secs = [normalize(s) for s in a.get("secondaries", [])]
        if len(secs) != 5:
            errors.append(f"COUNT {aid}: {len(secs)} secondaries (need 5)")
        for s in secs:
            if s in primaries:
                errors.append(f"PRIMARY-AS-SECONDARY '{s}' in {aid} (primary of {primaries[s]})")
            if s in secondaries:
                errors.append(f"REUSED SECONDARY '{s}' ({secondaries[s]} and {aid})")
            else:
                secondaries[s] = aid

    # Optional: flag keywords whose main token already appears in a live slug (heuristic, WARNING).
    live_tokens = set()
    if args.sitemap:
        for u in fetch_sitemap_urls(args.sitemap):
            live_tokens.add(normalize(u.rstrip("/").split("/")[-1]))
    if live_tokens:
        for a in articles:
            for kw in [a["primary"]] + a.get("secondaries", []):
                main = normalize(kw).split(" ")[0]
                if main and any(main in t for t in live_tokens):
                    errors.append(f"LIVE WARNING: main token '{main}' of '{kw}' already appears in a live slug")

    print(f"checked {len(articles)} articles, {len(primaries)} primaries, {len(secondaries)} secondaries")
    if errors:
        print("FAIL:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("PASS: primaries unique, 5 secondaries each, no primary-as-secondary")
    return 0


if __name__ == "__main__":
    sys.exit(main())
