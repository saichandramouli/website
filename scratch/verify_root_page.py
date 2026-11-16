import re
import os

with open('best-staffing-company-in-hyderabad.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Checking for ../ in root file:', re.findall(r'(\.\./[^\s"\'\)]+)', text))

srcs = re.findall(r'(?:src|href)=["\']([^"\'#]+)["\']', text)
missing = []
for s in set(srcs):
    if s.startswith('http') or s.startswith('mailto:') or s.startswith('tel:'):
        continue
    clean_s = s.split('?')[0]
    if not os.path.exists(clean_s):
        missing.append(s)

print('Missing local assets:', missing)
print('All OK!' if not missing else 'Found missing assets')
