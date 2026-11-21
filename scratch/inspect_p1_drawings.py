import fitz

doc = fitz.open('assets/the-ai-leadership-brief-issue-08.pdf')
p1 = doc[0]

print("Page size:", p1.rect)
drawings = p1.get_drawings()
print(f"Total drawings: {len(drawings)}")

# Find key boxes like section banners, cards, etc.
for d in drawings:
    r = [round(x, 1) for x in d['rect']]
    # check interesting boxes
    if r[2] - r[0] > 100:
        print(f"Drawing box: {r}, fill={d.get('fill')}, color={d.get('color')}")
