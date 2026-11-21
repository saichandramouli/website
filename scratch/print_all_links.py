import json

with open("scratch/issue_08_parsed.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

for p in pages:
    print(f"=== PAGE {p['page']} ===")
    links = [l for l in p['links'] if l.get('uri')]
    print(f"  Total external links: {len(links)}")
    for l in links:
        print(f"   [{l['text']}] -> {l['uri']}")
