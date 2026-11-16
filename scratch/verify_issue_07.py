import re

with open('ai-newsletter-issue-07.html', 'r', encoding='utf-8') as f:
    c = f.read()

print('File size:', len(c))
for p in range(1, 7):
    assert f'id="page-{p}"' in c, f'Missing page-{p}'
    print(f'Page {p} found')

# Check links
links = re.findall(r'href=["\']([^"\']+)["\']', c)
print(f'Total links found: {len(links)}')
external_links = [l for l in links if l.startswith('http')]
print(f'External links: {len(external_links)}')
for el in external_links:
    print(' ', el)

# Check cartoon image
assert 'assets/newsletters/issue-07-cartoon.png' in c
print('Cartoon image correctly referenced!')

# Check PDF download
assert 'assets/the-ai-leadership-brief-issue-07.pdf' in c
print('PDF download button correctly linked!')
print('\nALL VALIDATIONS PASSED!')

