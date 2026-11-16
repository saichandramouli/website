import fitz

doc = fitz.open('c:/Users/Sai chandra Mouli/Downloads/AI_Leadership_Brief_Edition_07 (2) 1.pdf')
with open('scratch/issue_07_parsed_links.txt', 'w', encoding='utf-8') as out:
    for pno in range(6):
        page = doc[pno]
        links = page.get_links()
        out.write(f"=== PAGE {pno+1} ({len(links)} links) ===\n")
        for l in links:
            rect = [round(x, 1) for x in l['from']]
            uri = l.get('uri')
            dest = l.get('page')
            txt = page.get_text('text', clip=l['from']).strip().replace('\n', ' ')
            out.write(f"  {rect}: text='{txt}' -> uri={uri} | page_dest={dest}\n")

print("Parsed links successfully written to scratch/issue_07_parsed_links.txt")

