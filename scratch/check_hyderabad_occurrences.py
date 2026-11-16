with open('best-staffing-company-in-hyderabad.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'hyderabad', text, re.IGNORECASE)]
print(f'Occurrences of hyderabad: {len(matches)}')

for m in re.finditer(r'(.{0,40}hyderabad.{0,40})', text, re.IGNORECASE):
    print('  -->', m.group(0).strip())
