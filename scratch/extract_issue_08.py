import fitz # PyMuPDF
import json
import os

pdf_path = "assets/the-ai-leadership-brief-issue-08.pdf"
doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

# 1. Extract links and text blocks per page
pages_data = []
all_links = []

for pno, page in enumerate(doc):
    text = page.get_text("text")
    blocks = page.get_text("blocks")
    links = page.get_links()
    
    formatted_blocks = []
    for b in blocks:
        formatted_blocks.append({
            "bbox": [round(x, 1) for x in b[:4]],
            "text": b[4].strip()
        })
        
    page_links = []
    for l in links:
        txt = page.get_text("text", clip=l["from"]).strip().replace("\n", " ")
        uri = l.get("uri")
        page_links.append({
            "from": [round(x, 1) for x in l["from"]],
            "text": txt,
            "uri": uri,
            "page": l.get("page")
        })
        if uri:
            all_links.append({"page": pno + 1, "text": txt, "uri": uri})
            
    pages_data.append({
        "page": pno + 1,
        "text": text,
        "blocks": formatted_blocks,
        "links": page_links
    })
    
    with open(f"scratch/issue_08_page_{pno+1}.txt", "w", encoding="utf-8") as f:
        f.write(text)

with open("scratch/issue_08_parsed.json", "w", encoding="utf-8") as f:
    json.dump(pages_data, f, indent=2, ensure_ascii=False)

with open("scratch/issue_08_links.json", "w", encoding="utf-8") as f:
    json.dump(all_links, f, indent=2, ensure_ascii=False)

print(f"Extraction complete! Found {len(all_links)} external links.")

# 2. Extract Cartoon on Page 1
# Let's inspect images or vector rect on page 1
page1 = doc[0]
pix = page1.get_pixmap(dpi=200)
# Look for cartoon bounding box on Page 1
# Based on layout: [34, 140, 290, 240] in pt coords
# Let's render the cartoon area:
# In pt, let's search for "Customer, or bot?"
rects = page1.search_for("Customer, or bot?")
print("Search for 'Customer, or bot?':", rects)
if rects:
    r = rects[0]
    # Cartoon box is roughly from x=34 to 280, y=130 to 240
    # Let's check blocks around there
    cartoon_clip = fitz.Rect(34, 130, 285, 240)
    cartoon_pix = page1.get_pixmap(clip=cartoon_clip, dpi=200)
    cartoon_pix.save("assets/newsletters/issue-08-cartoon.png")
    print("Saved assets/newsletters/issue-08-cartoon.png")

