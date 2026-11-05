import re

with open('ai-newsletter-issue-05.html', 'r', encoding='utf-8') as f:
    content_05 = f.read()

# Extract head
head_match = re.search(r'(<!DOCTYPE html>.*?<style>.*?</style>.*?</head>)', content_05, re.DOTALL)
if not head_match:
    raise ValueError("Could not find head section in ai-newsletter-issue-05.html")

head_html = head_match.group(1)

head_html = head_html.replace(
    '<title>The AI Leadership Brief · Issue 05 | People Prime Worldwide</title>',
    '<title>The AI Leadership Brief · Issue 06 | People Prime Worldwide</title>'
)

old_meta_desc = '<meta name="description" content="The AI Leadership Brief (Edition 05 · 19–25 October 2026) — The week’s AI developments that matter to CXOs and decision-makers by Jayaraman (Jay) Ganapathi. Frontier models cross cloud lines, llm-d v1.0, agentic intrusions, oversight suppression, Australia data center power gap, and SEC disclosure shadow.">'
new_meta_desc = '<meta name="description" content="The AI Leadership Brief (Edition 06 · 26 Oct–1 Nov 2026) — The week’s AI developments that matter to CXOs and senior leaders by Jayaraman (Jay) Ganapathi, People Prime Worldwide. Demand shows up in results, SK hynix & Intel supply, OpenAI GPT-6.1 Terra, Gemini 4 Carbon, agent decision gates, prompt injection trust regions, and FuriosaAI $620M.">'
head_html = head_html.replace(old_meta_desc, new_meta_desc)

# Extra CSS rules for Issue 06 (business-lens, ask-team, badges, etc.)
extra_css_06 = """
    /* ISSUE 06 SPECIFIC ENHANCEMENTS */
    .business-lens-box {
      background: #f4f6f0;
      border-left: 3px solid #2d5a3f;
      padding: 6px 10px;
      font-size: 11px;
      line-height: 1.4;
      color: #1a2820;
      border-radius: 0 3px 3px 0;
    }
    .business-lens-label {
      font-size: 9.5px;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: #2d5a3f;
      text-transform: uppercase;
      margin-bottom: 2px;
    }
    .ask-team-box {
      background: #fdfbf7;
      border-left: 3px solid #b45309;
      padding: 6px 10px;
      font-size: 11px;
      line-height: 1.4;
      color: #292524;
      border-radius: 0 3px 3px 0;
    }
    .ask-team-label {
      font-size: 9.5px;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: #b45309;
      text-transform: uppercase;
      margin-bottom: 2px;
    }
    .lens-questions-list {
      list-style: disc;
      margin-left: 16px;
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .badge-restricted {
      background: #fef2f2;
      color: #991b1b;
      border: 1px solid #fecaca;
    }
    .badge-patch {
      background: #fef3c7;
      color: #92400e;
      border: 1px solid #fde68a;
    }
    .badge-model {
      background: #eff6ff;
      color: #1e40af;
      border: 1px solid #bfdbfe;
    }
    .lens-grid-pair {
      display: flex;
      flex-direction: column;
      gap: 5px;
      margin-top: auto;
      padding-top: 5px;
    }
"""

head_html = head_html.replace('</style>', extra_css_06 + '\n  </style>')

# Extract tracking script
tracking_match = re.search(r'(<!-- GOOGLE ANALYTICS INTERACTION & READING TRACKING -->.*?)</body>', content_05, re.DOTALL)
if not tracking_match:
    raise ValueError("Could not find tracking script")
tracking_script = tracking_match.group(1)

print("Head and styles prepared successfully!")

