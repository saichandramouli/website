with open('landingpage/hyderabad/best-staffing-company-in-hyderabad.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace relative paths:
# ../../ -> empty (root level)
content = content.replace('../../', '')

# Replace images/ -> assets/landingpage/hyderabad/
content = content.replace('images/hero-main.png', 'assets/landingpage/hyderabad/hero-main.png')
content = content.replace('images/staffing-solutions.png', 'assets/landingpage/hyderabad/staffing-solutions.png')
content = content.replace('images/hire-professionals.png', 'assets/landingpage/hyderabad/hire-professionals.png')
content = content.replace('images/trusted-partner.png', 'assets/landingpage/hyderabad/trusted-partner.png')

with open('best-staffing-company-in-hyderabad.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created best-staffing-company-in-hyderabad.html at root! Size:", len(content))
