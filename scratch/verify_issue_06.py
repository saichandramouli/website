import re
import os

with open('ai-newsletter-issue-06.html', encoding='utf-8') as f:
    html = f.read()

# Check internal jump links
hrefs = re.findall(r'href=[\"\'](#[a-zA-Z0-9_-]+)[\"\']', html)
ids = set(re.findall(r'id=[\"\']([a-zA-Z0-9_-]+)[\"\']', html))
missing = [h for h in set(hrefs) if h[1:] not in ids]
print('Missing internal anchors:', missing)

# Check images
imgs = re.findall(r'src=[\"\']([^\"\']+\.(?:png|jpg|svg))[\"\']', html)
for img in set(imgs):
    print(f'Image {img} exists:', os.path.exists(img))

# Check PDF
pdfs = re.findall(r'href=[\"\']([^\"\']+\.pdf)[\"\']', html)
for pdf in set(pdfs):
    print(f'PDF {pdf} exists:', os.path.exists(pdf))

print("Total length:", len(html))

