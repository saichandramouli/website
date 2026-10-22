import os
import re

files = [
    'aiml-tech-services.html',
    'aiml-engineering-mlops.html',
    'ai-model-training.html',
    'enterprise-ai-agents.html',
    'ai-ml-talent-services.html',
    'ai-ml-model-development.html'
]

for f in files:
    with open(f, 'r', encoding='utf-8') as fl:
        content = fl.read()

    if 'AI Experience Center' in content:
        print(f + ' already contains AI Experience Center')
        continue

    # 1. Desktop nav: exactly 12 spaces before <a href="ai-newsletter-issue-04.html">AI News Letter</a>
    desktop_pattern = r'(\n {12}<a href="ai-newsletter-issue-03\.html">AI News Letter</a>)'
    desktop_replacement = r'\n            <a href="invoice-to-pay/">AI Experience Center</a>\1'

    # 2. Drawer nav: exactly 10 spaces before <a href="ai-newsletter-issue-04.html">AI News Letter</a>
    drawer_pattern = r'(\n {10}<a href="ai-newsletter-issue-03\.html">AI News Letter</a>)'
    drawer_replacement = r'\n          <a href="invoice-to-pay/">AI Experience Center</a>\1'

    content, n_desk = re.subn(desktop_pattern, desktop_replacement, content, count=1)
    content, n_draw = re.subn(drawer_pattern, drawer_replacement, content, count=1)

    if n_desk == 1 and n_draw == 1:
        with open(f, 'w', encoding='utf-8') as fl:
            fl.write(content)
        print(f'Successfully updated {f} (desktop: {n_desk}, drawer: {n_draw})')
    else:
        print(f'Failed for {f}: desktop={n_desk}, drawer={n_draw}')
