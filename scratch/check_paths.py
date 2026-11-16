import re

with open('landingpage/hyderabad/best-staffing-company-in-hyderabad.html', 'r', encoding='utf-8') as f:
    text = f.read()

rel_paths = re.findall(r'(\.\./[^\s"\'\)]+)', text)
print("Relative paths with ../:")
for p in sorted(set(rel_paths)):
    print(" ", p)

img_paths = re.findall(r'(images/[^\s"\'\)]+)', text)
print("Image paths:")
for p in sorted(set(img_paths)):
    print(" ", p)
