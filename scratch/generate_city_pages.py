def generate_city_page(city_name):
    with open('best-staffing-company-in-hyderabad.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Title
    content = content.replace(
        '<title>Best Staffing Company in Hyderabad | People Prime Worldwide</title>',
        f'<title>Best Staffing Company in {city_name} | People Prime Worldwide</title>'
    )
    
    # Meta description
    content = content.replace(
        'emerging digital domains in Hyderabad. Contract, flexible, and permanent staffing.',
        f'emerging digital domains in {city_name}. Contract, flexible, and permanent staffing.'
    )
    
    # Meta keywords
    content = content.replace(
        'content="Staffing Company in Hyderabad, IT Staffing Hyderabad, Tech recruitment Hyderabad, Contract Staffing, Permanent Hiring, People Prime Worldwide"',
        f'content="Staffing Company in {city_name}, IT Staffing {city_name}, Tech recruitment {city_name}, Contract Staffing, Permanent Hiring, People Prime Worldwide"'
    )
    
    # CSS comment
    content = content.replace(
        'Landing Page: Best Staffing Company in Hyderabad',
        f'Landing Page: Best Staffing Company in {city_name}'
    )
    
    # Hero Title
    content = content.replace(
        '<h1 class="hero-main-title">Best Staffing Company in Hyderabad</h1>',
        f'<h1 class="hero-main-title">Best Staffing Company in {city_name}</h1>'
    )
    
    # Section paragraphs (all occurrences of "in Hyderabad" in text)
    content = content.replace(
        'Looking for the best staffing company in Hyderabad?',
        f'Looking for the best staffing company in {city_name}?'
    )
    
    content = content.replace(
        'Looking for the best staffing company in Hyderabad to hire',
        f'Looking for the best staffing company in {city_name} to hire'
    )
    
    content = content.replace(
        'looking for the best staffing company in Hyderabad. We',
        f'looking for the best staffing company in {city_name}. We'
    )
    
    slug_name = city_name.lower().replace(' ', '-')
    out_file = f'best-staffing-company-in-{slug_name}.html'
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated {out_file}")

generate_city_page('Bangalore')
generate_city_page('Chennai')
