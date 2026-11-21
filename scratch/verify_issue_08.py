import re
import os

with open('ai-newsletter-issue-08.html', 'r', encoding='utf-8') as f:
    c = f.read()

print('File size:', len(c))
for p in range(1, 8):
    assert f'id="page-{p}"' in c, f'Missing page-{p}'
    print(f'Page {p} found')

# Check links
links = re.findall(r'href=["\']([^"\']+)["\']', c)
print(f'Total links found: {len(links)}')
external_links = [l for l in links if l.startswith('http')]
print(f'External links: {len(external_links)}')

# Check cartoon image
assert 'assets/newsletters/issue-08-cartoon.png' in c
assert os.path.exists('assets/newsletters/issue-08-cartoon.png')
print('Cartoon image correctly referenced and exists!')

# Check PDF download
assert 'assets/the-ai-leadership-brief-issue-08.pdf' in c
assert os.path.exists('assets/the-ai-leadership-brief-issue-08.pdf')
print('PDF download button correctly linked and exists!')

# Check canonical redirect
with open('ai-newsletter.html', 'r', encoding='utf-8') as f:
    redir = f.read()
assert 'ai-newsletter-issue-08.html' in redir
print('ai-newsletter.html redirect validated!')

print('\nALL VALIDATIONS PASSED FOR ISSUE 08!')
