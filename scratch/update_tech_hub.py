with open('technology-hub/technology-hub.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = '<div class="tech-hub-grid">'

new_tile = '''<div class="tech-hub-grid">
      <div class="tech-hub-tile">
        <img class="tech-tile-img" src="../assets/images/hyderabad-staffing-partner-1.jpg"
          alt="Why Choose a Hyderabad-Based Staffing Partner?" />
        <div class="tech-tile-content">
          <p class="timeStamp">
            <i class="fa-regular fa-clock"></i> 16/11/2026
          </p>
          <h3 class="mb-3">
            Why Choose a Hyderabad-Based Staffing Partner?
          </h3>
          <p class="mb-3">
            Finding the right talent is still one of the biggest challenges faced by businesses nowadays. Discover how a Hyderabad-based staffing partner provides local market knowledge, faster access to skilled talent, and flexible hiring solutions.
          </p>
          <a href="why-choose-hyderabad-staffing-partner.html" class="btn btn-primary gView mt-3">Read More</a>
        </div>
      </div>'''

if target in c:
    c = c.replace(target, new_tile, 1)
    with open('technology-hub/technology-hub.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Successfully added tile to technology-hub.html!")
else:
    print("Target not found")
