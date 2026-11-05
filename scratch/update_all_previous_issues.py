# Update issue 05
with open('ai-newsletter-issue-05.html', 'r', encoding='utf-8') as f:
    c5 = f.read()

old_switcher_5 = """      <div class="issue-switcher">
        <span class="issue-btn active">Issue 05 (Current)</span>
        <a href="ai-newsletter-issue-04.html" class="issue-btn">Issue 04</a>
        <a href="ai-newsletter-issue-03.html" class="issue-btn">Issue 03</a>
        <a href="ai-newsletter-issue-02.html" class="issue-btn">Issue 02</a>
      </div>"""

new_switcher_5 = """      <div class="issue-switcher">
        <a href="ai-newsletter-issue-06.html" class="issue-btn">Issue 06</a>
        <span class="issue-btn active">Issue 05</span>
        <a href="ai-newsletter-issue-04.html" class="issue-btn">Issue 04</a>
        <a href="ai-newsletter-issue-03.html" class="issue-btn">Issue 03</a>
        <a href="ai-newsletter-issue-02.html" class="issue-btn">Issue 02</a>
      </div>"""

c5 = c5.replace(old_switcher_5.replace('\r\n', '\n'), new_switcher_5)
c5 = c5.replace(old_switcher_5, new_switcher_5)

old_banner_5 = """      <div class="issues-nav-left">
        <span class="issues-nav-label">ARCHIVE / ISSUES:</span>
        <a href="ai-newsletter-issue-05.html" class="issues-nav-pill active">
          <strong>Issue 05</strong> · 19 – 25 Oct 2026 (Latest)
        </a>
        <a href="ai-newsletter-issue-04.html" class="issues-nav-pill">
          <strong>Issue 04</strong> · 12 – 18 Oct 2026
        </a>
        <a href="ai-newsletter-issue-03.html" class="issues-nav-pill">
          <strong>Issue 03</strong> · 5 – 11 Oct 2026
        </a>
        <a href="ai-newsletter-issue-02.html" class="issues-nav-pill">
          <strong>Issue 02</strong> · 29 Sep – 4 Oct 2026
        </a>
      </div>"""

new_banner_5 = """      <div class="issues-nav-left">
        <span class="issues-nav-label">ARCHIVE / ISSUES:</span>
        <a href="ai-newsletter-issue-06.html" class="issues-nav-pill">
          <strong>Issue 06</strong> · 26 Oct – 1 Nov 2026 (Latest)
        </a>
        <a href="ai-newsletter-issue-05.html" class="issues-nav-pill active">
          <strong>Issue 05</strong> · 19 – 25 Oct 2026
        </a>
        <a href="ai-newsletter-issue-04.html" class="issues-nav-pill">
          <strong>Issue 04</strong> · 12 – 18 Oct 2026
        </a>
        <a href="ai-newsletter-issue-03.html" class="issues-nav-pill">
          <strong>Issue 03</strong> · 5 – 11 Oct 2026
        </a>
        <a href="ai-newsletter-issue-02.html" class="issues-nav-pill">
          <strong>Issue 02</strong> · 29 Sep – 4 Oct 2026
        </a>
      </div>"""

c5 = c5.replace(old_banner_5.replace('\r\n', '\n'), new_banner_5)
c5 = c5.replace(old_banner_5, new_banner_5)

with open('ai-newsletter-issue-05.html', 'w', encoding='utf-8') as f:
    f.write(c5)
print("Updated ai-newsletter-issue-05.html")


# Update issue 04
with open('ai-newsletter-issue-04.html', 'r', encoding='utf-8') as f:
    c4 = f.read()

old_switcher_4 = """      <div class="issue-switcher">
        <a href="ai-newsletter-issue-05.html" class="issue-btn">Issue 05</a>
        <span class="issue-btn active">Issue 04</span>
        <a href="ai-newsletter-issue-03.html" class="issue-btn">Issue 03</a>
        <a href="ai-newsletter-issue-02.html" class="issue-btn">Issue 02</a>
      </div>"""

new_switcher_4 = """      <div class="issue-switcher">
        <a href="ai-newsletter-issue-06.html" class="issue-btn">Issue 06</a>
        <a href="ai-newsletter-issue-05.html" class="issue-btn">Issue 05</a>
        <span class="issue-btn active">Issue 04</span>
        <a href="ai-newsletter-issue-03.html" class="issue-btn">Issue 03</a>
        <a href="ai-newsletter-issue-02.html" class="issue-btn">Issue 02</a>
      </div>"""

c4 = c4.replace(old_switcher_4.replace('\r\n', '\n'), new_switcher_4)
c4 = c4.replace(old_switcher_4, new_switcher_4)

old_banner_4 = """      <div class="issues-nav-left">
        <span class="issues-nav-label">ARCHIVE / ISSUES:</span>
        <a href="ai-newsletter-issue-05.html" class="issues-nav-pill">
          <strong>Issue 05</strong> · 19 – 25 Oct 2026 (Latest)
        </a>
        <a href="ai-newsletter-issue-04.html" class="issues-nav-pill active">
          <strong>Issue 04</strong> · 12 – 18 Oct 2026
        </a>"""

new_banner_4 = """      <div class="issues-nav-left">
        <span class="issues-nav-label">ARCHIVE / ISSUES:</span>
        <a href="ai-newsletter-issue-06.html" class="issues-nav-pill">
          <strong>Issue 06</strong> · 26 Oct – 1 Nov 2026 (Latest)
        </a>
        <a href="ai-newsletter-issue-05.html" class="issues-nav-pill">
          <strong>Issue 05</strong> · 19 – 25 Oct 2026
        </a>
        <a href="ai-newsletter-issue-04.html" class="issues-nav-pill active">
          <strong>Issue 04</strong> · 12 – 18 Oct 2026
        </a>"""

c4 = c4.replace(old_banner_4.replace('\r\n', '\n'), new_banner_4)
c4 = c4.replace(old_banner_4, new_banner_4)

with open('ai-newsletter-issue-04.html', 'w', encoding='utf-8') as f:
    f.write(c4)
print("Updated ai-newsletter-issue-04.html")


# Update issue 03
with open('ai-newsletter-issue-03.html', 'r', encoding='utf-8') as f:
    c3 = f.read()

old_switcher_3 = """      <div class="issue-switcher">
        <a href="ai-newsletter-issue-05.html" class="issue-btn">Issue 05</a>
        <a href="ai-newsletter-issue-04.html" class="issue-btn">Issue 04</a>
        <span class="issue-btn active">Issue 03</span>
        <a href="ai-newsletter-issue-02.html" class="issue-btn">Issue 02</a>
      </div>"""

new_switcher_3 = """      <div class="issue-switcher">
        <a href="ai-newsletter-issue-06.html" class="issue-btn">Issue 06</a>
        <a href="ai-newsletter-issue-05.html" class="issue-btn">Issue 05</a>
        <a href="ai-newsletter-issue-04.html" class="issue-btn">Issue 04</a>
        <span class="issue-btn active">Issue 03</span>
        <a href="ai-newsletter-issue-02.html" class="issue-btn">Issue 02</a>
      </div>"""

c3 = c3.replace(old_switcher_3.replace('\r\n', '\n'), new_switcher_3)
c3 = c3.replace(old_switcher_3, new_switcher_3)

old_banner_3 = """      <div class="issues-nav-left">
        <span class="issues-nav-label">ARCHIVE / ISSUES:</span>
        <a href="ai-newsletter-issue-05.html" class="issues-nav-pill">
          <strong>Issue 05</strong> · 19 – 25 Oct 2026 (Latest)
        </a>
        <a href="ai-newsletter-issue-04.html" class="issues-nav-pill">
          <strong>Issue 04</strong> · 12 – 18 Oct 2026
        </a>"""

new_banner_3 = """      <div class="issues-nav-left">
        <span class="issues-nav-label">ARCHIVE / ISSUES:</span>
        <a href="ai-newsletter-issue-06.html" class="issues-nav-pill">
          <strong>Issue 06</strong> · 26 Oct – 1 Nov 2026 (Latest)
        </a>
        <a href="ai-newsletter-issue-05.html" class="issues-nav-pill">
          <strong>Issue 05</strong> · 19 – 25 Oct 2026
        </a>
        <a href="ai-newsletter-issue-04.html" class="issues-nav-pill">
          <strong>Issue 04</strong> · 12 – 18 Oct 2026
        </a>"""

c3 = c3.replace(old_banner_3.replace('\r\n', '\n'), new_banner_3)
c3 = c3.replace(old_banner_3, new_banner_3)

with open('ai-newsletter-issue-03.html', 'w', encoding='utf-8') as f:
    f.write(c3)
print("Updated ai-newsletter-issue-03.html")


# Update issue 02
with open('ai-newsletter-issue-02.html', 'r', encoding='utf-8') as f:
    c2 = f.read()

old_switcher_2 = """      <div class="issue-switcher">
        <a href="ai-newsletter-issue-05.html" class="issue-btn">Issue 05</a>
        <a href="ai-newsletter-issue-04.html" class="issue-btn">Issue 04</a>
        <a href="ai-newsletter-issue-03.html" class="issue-btn">Issue 03</a>
        <span class="issue-btn active">Issue 02</span>
      </div>"""

new_switcher_2 = """      <div class="issue-switcher">
        <a href="ai-newsletter-issue-06.html" class="issue-btn">Issue 06</a>
        <a href="ai-newsletter-issue-05.html" class="issue-btn">Issue 05</a>
        <a href="ai-newsletter-issue-04.html" class="issue-btn">Issue 04</a>
        <a href="ai-newsletter-issue-03.html" class="issue-btn">Issue 03</a>
        <span class="issue-btn active">Issue 02</span>
      </div>"""

c2 = c2.replace(old_switcher_2.replace('\r\n', '\n'), new_switcher_2)
c2 = c2.replace(old_switcher_2, new_switcher_2)

old_banner_2 = """      <div class="issues-nav-left">
        <span class="issues-nav-label">ARCHIVE / ISSUES:</span>
        <a href="ai-newsletter-issue-05.html" class="issues-nav-pill">
          <strong>Issue 05</strong> · 19 – 25 Oct 2026 (Latest)
        </a>
        <a href="ai-newsletter-issue-04.html" class="issues-nav-pill">
          <strong>Issue 04</strong> · 12 – 18 Oct 2026
        </a>"""

new_banner_2 = """      <div class="issues-nav-left">
        <span class="issues-nav-label">ARCHIVE / ISSUES:</span>
        <a href="ai-newsletter-issue-06.html" class="issues-nav-pill">
          <strong>Issue 06</strong> · 26 Oct – 1 Nov 2026 (Latest)
        </a>
        <a href="ai-newsletter-issue-05.html" class="issues-nav-pill">
          <strong>Issue 05</strong> · 19 – 25 Oct 2026
        </a>
        <a href="ai-newsletter-issue-04.html" class="issues-nav-pill">
          <strong>Issue 04</strong> · 12 – 18 Oct 2026
        </a>"""

c2 = c2.replace(old_banner_2.replace('\r\n', '\n'), new_banner_2)
c2 = c2.replace(old_banner_2, new_banner_2)

with open('ai-newsletter-issue-02.html', 'w', encoding='utf-8') as f:
    f.write(c2)
print("Updated ai-newsletter-issue-02.html")

