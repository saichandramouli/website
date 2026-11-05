import json

with open('scratch/issue_06_links.json', encoding='utf-8') as f:
    data = json.load(f)

lines = []
for p, links in data.items():
    lines.append(f'=== {p} ===')
    for l in links:
        if l.get('uri'):
            lines.append(f'  "{l.get("text")}" -> {l["uri"]}')
        elif l.get('page') is not None:
            lines.append(f'  "{l.get("text")}" -> Page {l["page"]+1}')

with open('scratch/issue_06_links_clean.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('Saved issue_06_links_clean.txt')

