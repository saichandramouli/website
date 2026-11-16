import os
import re

issues = [
    ('ai-newsletter-issue-06.html', '06', '26 Oct – 1 Nov 2026'),
    ('ai-newsletter-issue-05.html', '05', '19 – 25 Oct 2026'),
    ('ai-newsletter-issue-04.html', '04', '12 – 18 Oct 2026'),
    ('ai-newsletter-issue-03.html', '03', '5 – 11 Oct 2026'),
    ('ai-newsletter-issue-02.html', '02', '29 Sep – 4 Oct 2026')
]

for filename, issue_num, issue_dates in issues:
    if not os.path.exists(filename):
        print(f"Skipping {filename} - not found")
        continue

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build new switcher for this issue
    switcher_links = []
    switcher_links.append('        <a href="ai-newsletter-issue-07.html" class="issue-btn">Issue 07</a>')
    for num in ['06', '05', '04', '03', '02']:
        if num == issue_num:
            switcher_links.append(f'        <span class="issue-btn active">Issue {num}</span>')
        else:
            switcher_links.append(f'        <a href="ai-newsletter-issue-{num}.html" class="issue-btn">Issue {num}</a>')
    
    new_switcher = '      <div class="issue-switcher">\n' + '\n'.join(switcher_links) + '\n      </div>'

    # Build new banner for this issue
    banner_items = [
        ('07', '2 – 8 Nov 2026', True),
        ('06', '26 Oct – 1 Nov 2026', False),
        ('05', '19 – 25 Oct 2026', False),
        ('04', '12 – 18 Oct 2026', False),
        ('03', '5 – 11 Oct 2026', False),
        ('02', '29 Sep – 4 Oct 2026', False)
    ]
    banner_links = []
    for num, dates, is_latest in banner_items:
        active_cls = ' active' if num == issue_num else ''
        latest_str = ' (Latest)' if is_latest else ''
        banner_links.append(f"""        <a href="ai-newsletter-issue-{num}.html" class="issues-nav-pill{active_cls}">
          <strong>Issue {num}</strong> · {dates}{latest_str}
        </a>""")

    new_banner = '      <div class="issues-nav-left">\n        <span class="issues-nav-label">ARCHIVE / ISSUES:</span>\n' + '\n'.join(banner_links) + '\n      </div>'

    # Replace switcher
    content = re.sub(r'<div class="issue-switcher">.*?</div>', new_switcher, content, flags=re.DOTALL)
    # Replace banner
    content = re.sub(r'<div class="issues-nav-left">.*?</div>', new_banner, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully updated {filename}")

print("All previous issues updated with Issue 07 switcher and archive links!")

