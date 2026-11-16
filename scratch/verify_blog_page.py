import re
import os

with open('technology-hub/why-choose-hyderabad-staffing-partner.html', 'r', encoding='utf-8') as f:
    text = f.read()

srcs = re.findall(r'(?:src|href)=["\']([^"\'#]+)["\']', text)
missing = []
for s in set(srcs):
    if s.startswith('http') or s.startswith('mailto:') or s.startswith('tel:'):
        continue
    target_path = os.path.normpath(os.path.join('technology-hub', s.split('?')[0]))
    if not os.path.exists(target_path):
        missing.append((s, target_path))

print('Missing assets in blog page:', missing)
print('Blog page size:', len(text))
