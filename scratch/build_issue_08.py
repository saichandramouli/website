import re

# Read head from ai-newsletter-issue-07.html
with open('ai-newsletter-issue-07.html', 'r', encoding='utf-8') as f:
    content_07 = f.read()

head_match = re.search(r'(<!DOCTYPE html>.*?<style>.*?</style>.*?</head>)', content_07, re.DOTALL)
if not head_match:
    raise ValueError("Could not find head section in issue 07")

head_html = head_match.group(1)

# Update title and meta description for Issue 08
head_html = head_html.replace(
    '<title>The AI Leadership Brief · Issue 07 | People Prime Worldwide</title>',
    '<title>The AI Leadership Brief · Issue 08 | People Prime Worldwide</title>'
)

old_meta_desc_07 = '<meta name="description" content="The AI Leadership Brief (Edition 07 · 2–8 Nov 2026) — The week’s AI developments that matter to CXOs and senior leaders by Jayaraman (Jay) Ganapathi, People Prime Worldwide. Buyers of AI wait for return, AMD & CDW results, Tencent Hy4, OpenAI GPT-6 Cyber, agent architecture cost preprint, OCC bank AI framework, and fal $1.3B Series F.">'
new_meta_desc_08 = '<meta name="description" content="The AI Leadership Brief (Edition 08 · 9–15 Nov 2026) — The week’s AI developments that matter to CXOs and senior leaders by Jayaraman (Jay) Ganapathi, People Prime Worldwide. Nvidia CEO transition, checkout agent decisions (United Airlines & ChatGPT Wallet), FBI ARTEX intrusion alert, 22-industry sector index, and EU AI Act sandboxes.">'
head_html = head_html.replace(old_meta_desc_07, new_meta_desc_08)

# Additional CSS specific for Issue 08 (such as tag unq, 7-page grid, etc.)
extra_css_08 = """
    /* ISSUE 08 SPECIFIC ENHANCEMENTS */
    .badge-unqualified {
      background: #fef3c7;
      color: #92400e;
      border: 1px solid #fde68a;
      font-size: 8.5px;
      font-weight: 800;
      padding: 1px 4px;
      border-radius: 2px;
      margin-right: 4px;
      display: inline-block;
      vertical-align: middle;
      letter-spacing: 0.5px;
    }
    .badge-restricted {
      background: #fef2f2;
      color: #991b1b;
      border: 1px solid #fecaca;
    }
    .badge-model {
      background: #eff6ff;
      color: #1e40af;
      border: 1px solid #bfdbfe;
    }
    .sector-index-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 11px;
      line-height: 1.35;
    }
    .sector-index-table th {
      background: #f1f5f9;
      color: #1e293b;
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 5px 8px;
      border-bottom: 2px solid #cbd5e1;
      text-align: left;
    }
    .sector-index-table td {
      padding: 4px 8px;
      border-bottom: 1px solid #e2e8f0;
      vertical-align: top;
      color: #1e293b;
    }
    .sector-index-table tr:nth-child(even) {
      background-color: #fafbfc;
    }
    .sector-num {
      font-weight: 700;
      color: #64748b;
      font-size: 10px;
      width: 20px;
    }
    .sector-name {
      font-weight: 700;
      color: #0f172a;
      width: 140px;
    }
    .sector-source {
      width: 130px;
      font-size: 10.5px;
    }
    .highlight-finding-box {
      background: #fdfbf7;
      border: 1px solid #fcd34d;
      border-radius: 3px;
      padding: 8px 12px;
      margin: 8px 0;
    }
    .highlight-finding-title {
      font-size: 10px;
      font-weight: 800;
      color: #92400e;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 3px;
    }
    .quote-box-p3 {
      background: #f8fafc;
      border-left: 3px solid #0284c7;
      padding: 8px 12px;
      margin-bottom: 6px;
      border-radius: 0 3px 3px 0;
    }
    .quote-text-p3 {
      font-family: 'Newsreader', Georgia, serif;
      font-size: 14px;
      font-style: italic;
      color: #0f172a;
      line-height: 1.35;
      margin-bottom: 3px;
    }
    .quote-src-p3 {
      font-size: 10px;
      color: #475569;
      line-height: 1.3;
    }
"""

head_html = head_html.replace('</style>', extra_css_08 + '\n  </style>')

# Google Analytics tracking script
tracking_match = re.search(r'(<!-- GOOGLE ANALYTICS INTERACTION & READING TRACKING -->.*?)</body>', content_07, re.DOTALL)
tracking_script = tracking_match.group(1) if tracking_match else ""
tracking_script = tracking_script.replace('Issue 07', 'Issue 08').replace('issue_07', 'issue_08').replace('issue-07', 'issue-08')

# Now let's build the complete HTML body
body_html = """<body>

  <!-- TOP TOOLBAR: Quick Reader Controls -->
  <header class="reader-toolbar" role="banner">
    <div class="toolbar-left">
      <a href="aiml-tech-services.html" class="toolbar-btn" title="Back to AIML Tech Services">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        <span class="btn-text-full">Back to Website</span>
        <span class="btn-text-short">Back</span>
      </a>
      <span class="toolbar-title">The AI Leadership Brief</span>
      <div class="issue-switcher">
        <span class="issue-btn active">Issue 08 (Current)</span>
        <a href="ai-newsletter-issue-07.html" class="issue-btn">Issue 07</a>
        <a href="ai-newsletter-issue-06.html" class="issue-btn">Issue 06</a>
        <a href="ai-newsletter-issue-05.html" class="issue-btn">Issue 05</a>
        <a href="ai-newsletter-issue-04.html" class="issue-btn">Issue 04</a>
        <a href="ai-newsletter-issue-03.html" class="issue-btn">Issue 03</a>
        <a href="ai-newsletter-issue-02.html" class="issue-btn">Issue 02</a>
      </div>
    </div>

    <div class="toolbar-center">
      <div class="page-jump-links" role="navigation" aria-label="Page navigation">
        <span class="jump-label">Jump to:</span>
        <a href="#page-1" class="page-jump-link"><span class="page-label-full">Page 1</span><span class="page-label-short">P1</span></a>
        <a href="#page-2" class="page-jump-link"><span class="page-label-full">Page 2</span><span class="page-label-short">P2</span></a>
        <a href="#page-3" class="page-jump-link"><span class="page-label-full">Page 3</span><span class="page-label-short">P3</span></a>
        <a href="#page-4" class="page-jump-link"><span class="page-label-full">Page 4</span><span class="page-label-short">P4</span></a>
        <a href="#page-5" class="page-jump-link"><span class="page-label-full">Page 5</span><span class="page-label-short">P5</span></a>
        <a href="#page-6" class="page-jump-link"><span class="page-label-full">Page 6</span><span class="page-label-short">P6</span></a>
        <a href="#page-7" class="page-jump-link"><span class="page-label-full">Page 7</span><span class="page-label-short">P7</span></a>
      </div>
    </div>

    <div class="toolbar-right">
      <a href="assets/the-ai-leadership-brief-issue-08.pdf" download class="toolbar-btn" title="Download Original PDF">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        <span class="btn-text-full">Download PDF</span>
        <span class="btn-text-short">PDF</span>
      </a>
      <button onclick="window.print()" class="toolbar-btn primary" title="Print document or save as PDF">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
        <span class="btn-text-full">Print / Save PDF</span>
        <span class="btn-text-short">Print</span>
      </button>
    </div>
  </header>

  <!-- PUBLICATION CONTENT: 7 PAGE SHEETS -->
  <main class="publication-container">

    <!-- ALL ISSUES ARCHIVE / SELECTOR BANNER -->
    <div class="issues-nav-banner">
      <div class="issues-nav-left">
        <span class="issues-nav-label">ARCHIVE / ISSUES:</span>
        <a href="ai-newsletter-issue-08.html" class="issues-nav-pill active">
          <strong>Issue 08</strong> · 9 – 15 Nov 2026 (Latest)
        </a>
        <a href="ai-newsletter-issue-07.html" class="issues-nav-pill">
          <strong>Issue 07</strong> · 2 – 8 Nov 2026
        </a>
        <a href="ai-newsletter-issue-06.html" class="issues-nav-pill">
          <strong>Issue 06</strong> · 26 Oct – 1 Nov 2026
        </a>
        <a href="ai-newsletter-issue-05.html" class="issues-nav-pill">
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
      </div>
      <div class="issues-nav-right">
        <span>Published Weekly by Jayaraman (Jay) Ganapathi, People Prime Worldwide</span>
      </div>
    </div>

    <!-- ==================== PAGE 1 OF 7 ==================== -->
    <article id="page-1" class="page-sheet">
      <!-- Issue Header -->
      <div class="issue-top-header">
        <span>W E E K L Y · E D I T I O N 0 8</span>
        <span>9 – 1 5 N O V 2 0 2 6 · P A G E 1 O F 7</span>
      </div>

      <!-- Masthead -->
      <div class="issue-title-block">
        <h1 class="masthead-title">The AI Leadership Brief</h1>
        <p class="masthead-subtitle">Edition 08 · 9–15 Nov 2026 · By Jayaraman (Jay) Ganapathi, People Prime Worldwide · For CXOs and senior leaders</p>
      </div>

      <!-- Cartoon & Top News Container -->
      <div class="two-col-equal" style="margin-top: 4px; gap: 14px;">
        <!-- Left: Cartoon -->
        <section id="sec-cartoon-week" style="flex: 1;">
          <div class="section-banner">
            <div class="section-banner-title">
              <span class="banner-theme-tag">01 GROWTH · P1</span>
              <span>CARTOON &amp; TOP NEWS</span>
            </div>
            <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
          </div>

          <div class="cartoon-container" style="margin-top: 6px;">
            <div class="cartoon-layout" style="flex-direction: column; align-items: center;">
              <div class="cartoon-img-wrap" style="width: 100%; text-align: center;">
                <img src="assets/newsletters/issue-08-cartoon.png" alt="Cartoon: Customer, or bot? Yes." class="cartoon-real-img" style="max-height: 140px; object-fit: contain; width: auto;">
              </div>
              <div class="cartoon-text-side" style="padding: 6px 4px 0 4px;">
                <div class="cartoon-dialogue" style="font-size: 11px; line-height: 1.4; color: #1e293b;">
                  <strong>Behind the cartoon:</strong> on 11 November an airline barred unauthorised third-party AI agents from completing a purchase on its channels; on 13 November a leading AI developer published what merchants must change before an agent can pay. An agent is a customer and an automated visitor at the same time, and most checkout defences were built to tell those two apart. <a href="#sec-lead-checkout" class="brief-link">Lead story, page 4 ›</a> · <a href="https://skift.com/2026/11/11/united-airlines-moves-to-block-personal-ai-agents-from-booking-flights/" target="_blank" rel="noopener noreferrer" class="src-link">Skift</a> · <a href="https://openai.com/index/introducing-chatgpt-wallet/" target="_blank" rel="noopener noreferrer" class="src-link">Developer’s announcement</a>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Right: 60-Second Summary -->
        <section id="sec-60-sec-summary" style="flex: 1.1;">
          <div class="section-banner">
            <div class="section-banner-title">
              <span class="banner-theme-tag">TOP NEWS THIS WEEK</span>
              <span>60-SECOND SUMMARY</span>
            </div>
            <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
          </div>

          <div class="summary-list" style="margin-top: 6px;">
            <div class="summary-item-row">
              <div class="summary-num-circle">1</div>
              <div class="summary-text">
                <strong>Nvidia's chief executive resigned and the CFO took over on an interim basis.</strong> Its filing speaks directly to customer commitments and the product roadmap. <a href="https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm" target="_blank" rel="noopener noreferrer" class="src-link">NVIDIA 8-K</a>
              </div>
            </div>
            <div class="summary-item-row">
              <div class="summary-num-circle">2</div>
              <div class="summary-text">
                <strong>Five models changed status in four days.</strong> One introductory price ends on 30 November, doubling from 1 December. <a href="https://www.anthropic.com/claude-fable-and-mythos-5-2" target="_blank" rel="noopener noreferrer" class="src-link">Anthropic</a> · <a href="https://research.meta.ai/blog/muse-ember" target="_blank" rel="noopener noreferrer" class="src-link">Meta</a> · <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/" target="_blank" rel="noopener noreferrer" class="src-link">Google</a>
              </div>
            </div>
            <div class="summary-item-row">
              <div class="summary-num-circle">3</div>
              <div class="summary-text">
                <strong>The FBI named ten sectors already targeted by an open-source AI intrusion framework,</strong> and named partner portals among the entry points. <a href="https://www.infosecurity-magazine.com/news/fbi-growing-abuse-ai-pentesting/" target="_blank" rel="noopener noreferrer" class="src-link">FBI alert</a>
              </div>
            </div>
            <div class="summary-item-row">
              <div class="summary-num-circle">4</div>
              <div class="summary-text">
                <strong>Regulators in four jurisdictions moved on AI in one week,</strong> two of them financial. <a href="https://eur-lex.europa.eu/eli/reg_impl/2026/2487/oj/eng" target="_blank" rel="noopener noreferrer" class="src-link">EUR-Lex</a> · <a href="https://finreg-e.com/weekly-regulatory-round-up-15-november-2026/" target="_blank" rel="noopener noreferrer" class="src-link">Regulatory summary</a>
              </div>
            </div>
            <div class="summary-item-row">
              <div class="summary-num-circle">5</div>
              <div class="summary-text">
                <strong>A labour-market preprint puts the early effects of AI in who is employed, not how many.</strong> Its authors decline to call it cause and effect. <a href="https://arxiv.org/abs/2507.08244" target="_blank" rel="noopener noreferrer" class="src-link">arXiv preprint</a>
              </div>
            </div>
          </div>
        </section>
      </div>

      <!-- Agenda Box -->
      <nav id="agenda" class="agenda-container" aria-label="Newsletter Agenda" style="margin-top: 10px;">
        <div class="agenda-header-bar">
          <div class="agenda-title">
            <span>AGENDA</span>
            <span style="font-size: 11px; font-weight: 500; color: #a4c9b1;">5 THEMES · TAP TO JUMP</span>
          </div>
          <div class="agenda-hint">Short on time? <a href="#sec-60-sec-summary">60-second summary</a> → <a href="#sec-roles-week">Your role</a> → <a href="#sec-leadership-actions">Leadership actions</a></div>
        </div>

        <div class="agenda-grid">
          <!-- Col 1 -->
          <div class="agenda-col">
            <span class="agenda-badge c1">01 GROWTH</span>
            <div class="agenda-subtitle">Where is new revenue coming from?</div>
            <ul class="agenda-links">
              <li><a href="#sec-sector-index">P2 Sector index · 22 industries</a></li>
              <li><a href="#sec-lead-checkout">P4 Lead · The checkout decision</a></li>
            </ul>
          </div>

          <!-- Col 2 -->
          <div class="agenda-col">
            <span class="agenda-badge c2">02 COST</span>
            <div class="agenda-subtitle">What does it cost to run?</div>
            <ul class="agenda-links">
              <li><a href="#sec-model-releases">P5 Model releases and prices</a></li>
              <li><a href="#sec-infrastructure">P7 Infrastructure &amp; capacity</a></li>
            </ul>
          </div>

          <!-- Col 3 -->
          <div class="agenda-col">
            <span class="agenda-badge c3">03 RISK</span>
            <div class="agenda-subtitle">What could go wrong?</div>
            <ul class="agenda-links">
              <li><a href="#sec-laws-guidance">P6 Laws, rules &amp; guidance</a></li>
              <li><a href="#sec-vendor-risk">P6 Vendor &amp; security risk</a></li>
            </ul>
          </div>

          <!-- Col 4 -->
          <div class="agenda-col">
            <span class="agenda-badge c4">04 CAPITAL</span>
            <div class="agenda-subtitle">Where is money going?</div>
            <ul class="agenda-links">
              <li><a href="#sec-supplier-risk">P5 Supplier &amp; governance risk</a></li>
              <li><a href="#sec-investments">P7 Investments · $100M+</a></li>
            </ul>
          </div>

          <!-- Col 5 -->
          <div class="agenda-col">
            <span class="agenda-badge c5">05 PEOPLE</span>
            <div class="agenda-subtitle">Who does the work?</div>
            <ul class="agenda-links">
              <li><a href="#sec-workforce-talent">P7 Workforce &amp; talent</a></li>
              <li><a href="#sec-leaders-said">P3 Leaders said · One year ago on P3</a></li>
            </ul>
          </div>
        </div>
      </nav>

      <!-- Agenda Notice Bar -->
      <div class="agenda-notice-bar">
        <span>Also in this issue: <a href="#sec-key-numbers" class="pdf-link">Key numbers</a> · <a href="#sec-regional-index" class="pdf-link">Regional index</a> · <a href="#sec-caution-note" class="pdf-link">Caution note</a>. <em>Not in this issue: upcoming events — no date could be confirmed against two independent listings or an organiser's own page. Every source name is a link to the original.</em></span>
      </div>

      <!-- Section: This Week For Your Role -->
      <section id="sec-roles-week" style="margin-top: 6px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE · P1</span>
            <span>THIS WEEK FOR YOUR ROLE</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div class="roles-grid-6" style="margin-top: 6px;">
          <!-- CEO -->
          <div class="role-card">
            <div>
              <div class="role-title">CEO</div>
              <p class="role-desc">Agent traffic at your checkout is a commercial policy question, not an IT one — and it is being decided by default.</p>
            </div>
            <a href="#sec-lead-checkout" class="role-go">›</a>
          </div>

          <!-- CFO -->
          <div class="role-card">
            <div>
              <div class="role-title">CFO</div>
              <p class="role-desc">One model's introductory price ends on 30 November, doubling from 1 December. Check whether any budget you approved assumes the introductory rate.</p>
            </div>
            <a href="#sec-model-releases" class="role-go">›</a>
          </div>

          <!-- CIO / CTO -->
          <div class="role-card">
            <div>
              <div class="role-title">CIO / CTO</div>
              <p class="role-desc">Five models changed status in four days; one moved from restricted to general availability. Re-check your approved-model list.</p>
            </div>
            <a href="#sec-model-releases" class="role-go">›</a>
          </div>

          <!-- CISO -->
          <div class="role-card">
            <div>
              <div class="role-title">CISO</div>
              <p class="role-desc">The FBI points at partner portals and third-party integrations — the estate you watch least. Some intrusions reached privileged access in under three hours.</p>
            </div>
            <a href="#sec-vendor-risk" class="role-go">›</a>
          </div>

          <!-- CHRO -->
          <div class="role-card">
            <div>
              <div class="role-title">CHRO</div>
              <p class="role-desc">A preprint finds the early labour effects in composition — hours, age, education — not headcount.</p>
            </div>
            <a href="#sec-workforce-talent" class="role-go">›</a>
          </div>

          <!-- COO / Sales -->
          <div class="role-card">
            <div>
              <div class="role-title">COO / Sales</div>
              <p class="role-desc">If an agent cannot buy on your site, you may be losing orders you never see. If it can, decide who you refund.</p>
            </div>
            <a href="#sec-lead-checkout" class="role-go">›</a>
          </div>
        </div>
      </section>

      <!-- Section: Leadership Actions This Week -->
      <section id="sec-leadership-actions" style="margin-top: 6px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE · P1</span>
            <span>LEADERSHIP ACTIONS THIS WEEK</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div class="actions-grid-2" style="margin-top: 6px;">
          <div class="action-item-card">
            <div class="action-circle-num">1</div>
            <div>
              <strong>Decide your agent policy explicitly.</strong> Name the executive who owns whether AI agents may browse, buy and manage accounts on your channels. <a href="#sec-lead-checkout" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">2</div>
            <div>
              <strong>Find out what your site does today.</strong> Your firewall and bot rules already answer this question, with no policy behind them. <a href="#sec-lead-checkout" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">3</div>
            <div>
              <strong>Write down who you refund</strong> when an agent buys on a customer's behalf and the order is disputed. <a href="#sec-lead-checkout" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">4</div>
            <div>
              <strong>Inventory your partner and supplier portals</strong> against the FBI's list of entry points, not just your main estate. <a href="#sec-vendor-risk" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">5</div>
            <div>
              <strong>Check every AI line item against current list prices,</strong> including any that are introductory and expire this month. <a href="#sec-model-releases" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">6</div>
            <div>
              <strong>Ask whether your AI roadmap depends on one supplier's leadership,</strong> and what your contract says about continuity. <a href="#sec-supplier-risk" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">7</div>
            <div>
              <strong>If you operate in the EU,</strong> name who would own an AI Act sandbox application ahead of the regulation's 1 December date of effect. <a href="#sec-laws-guidance" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">8</div>
            <div>
              <strong>Ask HR for hours, age and education trends</strong> in your most exposed roles, not just headcount. <a href="#sec-workforce-talent" class="action-tag-link">›</a>
            </div>
          </div>
        </div>
      </section>

      <!-- Page 1 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 08 · Page 1 of 7</div>
      </footer>
    </article>


    <!-- ==================== PAGE 2 OF 7 ==================== -->
    <article id="page-2" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>9–15 NOV 2026 · PAGE 2 OF 7</span>
      </div>

      <!-- Section: Sector Index · Top 22 Industries -->
      <section id="sec-sector-index">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag">01 GROWTH · P2</span>
            <span>SECTOR INDEX · TOP 22 INDUSTRIES</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <p style="font-size: 11px; line-height: 1.4; color: #334155; margin-bottom: 6px;">
            Twenty-two sectors are swept each week against eight item types; all twenty-two carry an item this week, 9 of them tagged. A row tagged <span class="badge-unqualified">UNQUALIFIED</span> rests on trade or secondary reporting we could not trace to a first-party release or filing: it is published so the sector is covered, and should be weighed as weaker than the rest of the issue.
          </p>

          <div class="table-wrap">
            <table class="sector-index-table">
              <thead>
                <tr>
                  <th style="width: 20px;">#</th>
                  <th style="width: 150px;">SECTOR</th>
                  <th>THIS WEEK</th>
                  <th style="width: 140px;">SOURCE</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="sector-num">01</td>
                  <td class="sector-name">Banking</td>
                  <td>Financial services, which covers banking, is named among the ten sectors targeted by the ARTEX framework in the FBI's 13 Nov alert. Abu Dhabi Global Market's regulator issued a notice pairing AI governance with cyber risk.</td>
                  <td class="sector-source"><a href="https://www.infosecurity-magazine.com/news/fbi-growing-abuse-ai-pentesting/" target="_blank" rel="noopener noreferrer" class="src-link">FBI alert</a> · <a href="https://finreg-e.com/weekly-regulatory-round-up-15-november-2026/" target="_blank" rel="noopener noreferrer" class="src-link">ADGM notice</a></td>
                </tr>
                <tr>
                  <td class="sector-num">02</td>
                  <td class="sector-name">Mortgage &amp; lending</td>
                  <td><span class="badge-unqualified">UNQUALIFIED</span> Dark Matter Technologies acquired the AI agent platform and intellectual property of House Numbers, whose agents work loan conditions and contact borrowers, and named its co-founder chief AI officer. Terms were not disclosed, and sources date the announcement variously to 30 Oct and the week of 13 Nov.</td>
                  <td class="sector-source"><a href="https://www.housingwire.com/articles/exclusive-dark-matter-acquires-house-numbers-agentic-ai-platform/" target="_blank" rel="noopener noreferrer" class="src-link">HousingWire</a> · <a href="https://nationalmortgageprofessional.com/news/dark-matter-expands-ai-ambitions-house-numbers-acquisition" target="_blank" rel="noopener noreferrer" class="src-link">Natl Mortgage Prof</a></td>
                </tr>
                <tr>
                  <td class="sector-num">03</td>
                  <td class="sector-name">Insurance</td>
                  <td>IBM and Microsoft announced Imagine Enterprise on 10 Nov, an agentic platform for building, running and governing AI agents, launching with industry frameworks for financial services, insurance and retail. IBM Consulting contributes more than 6,000 pre-built agents; Microsoft provides the AI, cloud and security technology.</td>
                  <td class="sector-source"><a href="https://newsroom.ibm.com/2026-11-10-ibm-and-microsoft-announce-a-new-ai-agent-platform-designed-for-industry-specific-transformation" target="_blank" rel="noopener noreferrer" class="src-link">IBM Newsroom</a></td>
                </tr>
                <tr>
                  <td class="sector-num">04</td>
                  <td class="sector-name">Capital markets &amp; asset mgmt</td>
                  <td>The Ontario Securities Commission published findings from its examination of how registered firms use and govern AI, including weaknesses in governance and training and instances of possible “AI washing”.</td>
                  <td class="sector-source"><a href="https://www.osc.ca/en/news-events/news/osc-highlights-importance-governance-and-oversight-ai-adoption" target="_blank" rel="noopener noreferrer" class="src-link">OSC release</a></td>
                </tr>
                <tr>
                  <td class="sector-num">05</td>
                  <td class="sector-name">Healthcare providers</td>
                  <td>Google Cloud launched Gemini for healthcare on 10 Nov in US preview, connecting electronic health records, billing platforms, clinical guidelines and CMS datasets, with launch customers including HCA Healthcare, Northwell Health and Optum. Separately, research among 182 operators reports 52.7% already running a live agentic workflow; it is published by a firm that sells into the market it surveyed.</td>
                  <td class="sector-source"><a href="https://www.googlecloudpresscorner.com/2026-11-10-Google-Cloud-Launches-Gemini-for-Healthcare" target="_blank" rel="noopener noreferrer" class="src-link">Google Cloud</a> · <a href="https://www.accessnewswire.com/newsroom/en/healthcare-and-pharmaceutical/healthcare-leaders-identify-priorities-for-agentic-ai-adoption-in-202-1249788" target="_blank" rel="noopener noreferrer" class="src-link">Black Book</a></td>
                </tr>
                <tr>
                  <td class="sector-num">06</td>
                  <td class="sector-name">Pharma &amp; life sciences</td>
                  <td><span class="badge-unqualified">UNQUALIFIED</span> Pierre Fabre engaged XtalPi’s AI and robotics platform on 10 Nov to design small molecules for undisclosed oncology targets, with Pierre Fabre taking any resulting candidates into the clinic.</td>
                  <td class="sector-source"><a href="https://www.worldpharma.ai/insights" target="_blank" rel="noopener noreferrer" class="src-link">World Pharma AI</a></td>
                </tr>
                <tr>
                  <td class="sector-num">07</td>
                  <td class="sector-name">Manufacturing &amp; industrials</td>
                  <td>Agile Robots, a Munich physical-AI company whose robots automate industrial work, raised a $500M Series F on 12 Nov led by SoftBank, with NVIDIA, Hitachi and T.Capital named as participants. The company says its German plant can build up to 10,000 legged and wheeled humanoid robots a year.</td>
                  <td class="sector-source"><a href="https://www.automate.org/robotics/news/physical-ai-leader-agile-robots-raises-500-million-series-f-at-8-5-billion-valuation-to-accelerate-global-growth" target="_blank" rel="noopener noreferrer" class="src-link">Agile Robots announcement</a></td>
                </tr>
                <tr>
                  <td class="sector-num">08</td>
                  <td class="sector-name">Automotive &amp; mobility</td>
                  <td><span class="badge-unqualified">UNQUALIFIED</span> Executives at Nexperia and STMicroelectronics said on 10 Nov that chip capacity moving to AI data centres and robotics is tightening supply of the mature-node components used in vehicles and industrial equipment, pointing manufacturers towards longer procurement horizons. This is an AI-driven supply constraint, not an adoption item.</td>
                  <td class="sector-source"><a href="https://ayokasystems.com/news/ayoka-daily-briefing-2026-11-10/" target="_blank" rel="noopener noreferrer" class="src-link">Mfg briefing</a></td>
                </tr>
                <tr>
                  <td class="sector-num">09</td>
                  <td class="sector-name">Retail &amp; e-commerce</td>
                  <td>OpenAI's wallet asks retailers not to block agents and to make risk systems recognise them, while one major travel merchant went the other way. The <a href="https://newsroom.ibm.com/2026-11-10-ibm-and-microsoft-announce-a-new-ai-agent-platform-designed-for-industry-specific-transformation" target="_blank" rel="noopener noreferrer" class="src-link">IBM–Microsoft platform</a> also covers retail.</td>
                  <td class="sector-source"><a href="https://openai.com/index/introducing-chatgpt-wallet/" target="_blank" rel="noopener noreferrer" class="src-link">OpenAI</a> · <a href="https://newsroom.ibm.com/2026-11-10-ibm-and-microsoft-announce-a-new-ai-agent-platform-designed-for-industry-specific-transformation" target="_blank" rel="noopener noreferrer" class="src-link">IBM</a></td>
                </tr>
                <tr>
                  <td class="sector-num">10</td>
                  <td class="sector-name">Consumer goods</td>
                  <td><span class="badge-unqualified">UNQUALIFIED</span> The president of Lowes Foods told a grocery conference, reported 10 Nov, that AI use among shoppers is already widespread, citing a projection that 80% of shoppers will interact with AI by 2030 and putting the 2026 figure at 74%. Both are projections he cited, not his company’s data. Coty was separately reported piloting AI discovery across six brands.</td>
                  <td class="sector-source"><a href="https://consumergoods.com/lowes-foods-discusses-how-ai-will-change-consumer-behavior" target="_blank" rel="noopener noreferrer" class="src-link">Consumer Goods</a></td>
                </tr>
                <tr>
                  <td class="sector-num">11</td>
                  <td class="sector-name">Energy &amp; utilities</td>
                  <td>At the BNEF Houston Summit on 11 Nov a consultant advising the Utilize Coalition argued AI tools let grid planners see capacity they could not see before. One adviser’s view, not a deployment; she also advises an AI data-centre flexibility startup. Energy is named in the FBI’s targeted list.</td>
                  <td class="sector-source"><a href="https://www.utilitydive.com/news/utility-tech-officials-see-opportunities-to-increase-grid-utilization/874644/" target="_blank" rel="noopener noreferrer" class="src-link">Utility Dive</a> · <a href="https://www.infosecurity-magazine.com/news/fbi-growing-abuse-ai-pentesting/" target="_blank" rel="noopener noreferrer" class="src-link">FBI alert</a></td>
                </tr>
                <tr>
                  <td class="sector-num">12</td>
                  <td class="sector-name">Oil, gas &amp; chemicals</td>
                  <td><span class="badge-unqualified">UNQUALIFIED</span> Dated just before this window: on 3 Nov at ADIPEC, ADNOC agreed with G42 and OpenAI to become the first energy company to deploy OpenAI Frontier, a platform for coordinating AI agents across operations.</td>
                  <td class="sector-source"><a href="https://www.wam.ae/en/article/c32irwb-adipec-2026-agents-reshape-oil-and-gas-operations" target="_blank" rel="noopener noreferrer" class="src-link">WAM</a></td>
                </tr>
                <tr>
                  <td class="sector-num">13</td>
                  <td class="sector-name">Telecommunications</td>
                  <td>Telecommunications is named among the ten sectors the FBI says have been targeted by the ARTEX framework since at least August 2026.</td>
                  <td class="sector-source"><a href="https://www.infosecurity-magazine.com/news/fbi-growing-abuse-ai-pentesting/" target="_blank" rel="noopener noreferrer" class="src-link">FBI alert</a></td>
                </tr>
                <tr>
                  <td class="sector-num">14</td>
                  <td class="sector-name">Media &amp; entertainment</td>
                  <td><span class="badge-unqualified">UNQUALIFIED</span> Disney and Adobe announced a multi-year partnership on 9 Nov to build generative AI models tailored to Disney’s properties via Adobe’s Firefly Foundry, trained on character attributes, environments and visual styles to produce what the companies call commercially safe output.</td>
                  <td class="sector-source"><a href="https://www.thewrap.com/industry-news/business/disney-adobe-ai-strategic-partnership/" target="_blank" rel="noopener noreferrer" class="src-link">TheWrap</a></td>
                </tr>
                <tr>
                  <td class="sector-num">15</td>
                  <td class="sector-name">Technology &amp; software</td>
                  <td>Nvidia reported a chief-executive transition in an 8-K filing. Technology is one of the ten sectors on the FBI's targeted list.</td>
                  <td class="sector-source"><a href="https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm" target="_blank" rel="noopener noreferrer" class="src-link">NVIDIA 8-K</a> · <a href="https://www.infosecurity-magazine.com/news/fbi-growing-abuse-ai-pentesting/" target="_blank" rel="noopener noreferrer" class="src-link">FBI alert</a></td>
                </tr>
                <tr>
                  <td class="sector-num">16</td>
                  <td class="sector-name">Semiconductors &amp; hardware</td>
                  <td>Fractile raised $720 million for inference chips integrating memory with logic, with UK state funds participating. Semiconductors are also named in the FBI's targeted sector list.</td>
                  <td class="sector-source"><a href="https://siliconangle.com/2026/11/11/inference-chip-developer-fractile-raises-720m-in-funding/" target="_blank" rel="noopener noreferrer" class="src-link">SiliconANGLE</a> · <a href="https://www.infosecurity-magazine.com/news/fbi-growing-abuse-ai-pentesting/" target="_blank" rel="noopener noreferrer" class="src-link">FBI alert</a></td>
                </tr>
                <tr>
                  <td class="sector-num">17</td>
                  <td class="sector-name">Professional &amp; legal services</td>
                  <td>Addleshaw Goddard said on 9 Nov it will distribute chatbot software from Harvey, a legal AI company, firmwide to more than 3,400 lawyers and business services staff. Legal is also among the ten sectors in the FBI’s 13 Nov alert.</td>
                  <td class="sector-source"><a href="https://www.law360.com/legalindustry/articles/2547781" target="_blank" rel="noopener noreferrer" class="src-link">Law360</a> · <a href="https://www.infosecurity-magazine.com/news/fbi-growing-abuse-ai-pentesting/" target="_blank" rel="noopener noreferrer" class="src-link">FBI alert</a></td>
                </tr>
                <tr>
                  <td class="sector-num">18</td>
                  <td class="sector-name">Logistics &amp; supply chain</td>
                  <td><span class="badge-unqualified">UNQUALIFIED</span> DHL Supply Chain announced on 9 Nov the next phase of its digitalisation strategy, adding AI orchestration to live warehouse operations to coordinate equipment, staff and workflows; it reports more than 9,000 robots across its network. GXO expanded a robotics partnership with Apptronik on 12 Nov.</td>
                  <td class="sector-source"><a href="https://www.globaltrademag.com/fourth-party-logistics-shifts-to-ai-driven-supply-chains/" target="_blank" rel="noopener noreferrer" class="src-link">Global Trade</a> · <a href="https://logisticsviewpoints.com/2026/11/17/freight-costs-rise-as-warehouse-ai-advances-supply-chain-logistics-news-of-the-week/" target="_blank" rel="noopener noreferrer" class="src-link">Logistics Viewpoints</a></td>
                </tr>
                <tr>
                  <td class="sector-num">19</td>
                  <td class="sector-name">Construction &amp; real estate</td>
                  <td><span class="badge-unqualified">UNQUALIFIED</span> A Federation of Master Builders and CIOB survey reported on 10 Nov found 57% of construction businesses had increased AI use over 12 months, mostly for administration, with 33% using it in site operations, health and safety or quality management. The FMB’s chief executive said technology alone would not solve the industry’s wider challenges.</td>
                  <td class="sector-source"><a href="https://www.sustainableconstruction.blog/article/2026/11/10/fmb-ciob-survey-ai-adoption" target="_blank" rel="noopener noreferrer" class="src-link">Sustainable Construction</a></td>
                </tr>
                <tr>
                  <td class="sector-num">20</td>
                  <td class="sector-name">Agriculture &amp; livestock</td>
                  <td>GEA showed DairyNet Intelligence at EuroTier on 11 Nov, an AI layer over its DairyNet herd management system summarising a cow’s health from milk yield, activity, somatic cell count and conductivity. GEA says it is in testing, does not yet recommend actions, and reaches selected farms in late 2026 or early 2027.</td>
                  <td class="sector-source"><a href="https://www.gea.com/en/news/press-releases/2026/eurotier-dairynet-intelligence.jsp" target="_blank" rel="noopener noreferrer" class="src-link">GEA trade press release</a></td>
                </tr>
                <tr>
                  <td class="sector-num">21</td>
                  <td class="sector-name">Food &amp; beverages</td>
                  <td><span class="badge-unqualified">UNQUALIFIED</span> IFF launched CONCEPT MUSE, an AI platform that generates food and beverage concepts from consumer insights, flavour expertise and market intelligence, producing product ideas and visual mock-ups. Its claim to shorten early-stage development is the company’s own.</td>
                  <td class="sector-source"><a href="https://www.newfoodmagazine.com/news/247192/iff-concept-muse-ai-fnb/" target="_blank" rel="noopener noreferrer" class="src-link">New Food Magazine</a></td>
                </tr>
                <tr>
                  <td class="sector-num">22</td>
                  <td class="sector-name">Public sector, defence &amp; education</td>
                  <td>Government and defence are both named in the FBI alert. The EU set common rules for AI Act regulatory sandboxes; the requirement on each member state to run one comes from the AI Act timeline, not this instrument.</td>
                  <td class="sector-source"><a href="https://www.infosecurity-magazine.com/news/fbi-growing-abuse-ai-pentesting/" target="_blank" rel="noopener noreferrer" class="src-link">FBI alert</a> · <a href="https://eur-lex.europa.eu/eli/reg_impl/2026/2487/oj/eng" target="_blank" rel="noopener noreferrer" class="src-link">EUR-Lex</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- Page 2 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 08 · Page 2 of 7</div>
      </footer>
    </article>


    <!-- ==================== PAGE 3 OF 7 ==================== -->
    <article id="page-3" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>9–15 NOV 2026 · PAGE 3 OF 7</span>
      </div>

      <!-- Notice -->
      <div style="font-size: 10px; color: #475569; font-style: italic; margin-bottom: 4px;">
        Every sector shows its own source. Where a sector has no item it is marked and shows no source, because there is no source for an absence; no sector is blank this week. The cross-sector items in this issue still bear on every sector.
      </div>

      <!-- Section: Regional Index -->
      <section id="sec-regional-index">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag">01 GROWTH · P3</span>
            <span>REGIONAL INDEX</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 4px;">
          <table class="regional-index-table">
            <tbody>
              <tr>
                <td style="width: 120px; font-weight: 700; color: #1e3a5f;">Global</td>
                <td>Four frontier model releases in four days; the agent-at-checkout question <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/" target="_blank" rel="noopener noreferrer" class="src-link">Google</a> · <a href="https://openai.com/index/introducing-chatgpt-wallet/" target="_blank" rel="noopener noreferrer" class="src-link">OpenAI</a></td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #1e3a5f;">United States</td>
                <td>Airline agent restrictions; a chipmaker's CEO transition; agent payments; an export rule on remote access to AI chips <a href="https://skift.com/2026/11/11/united-airlines-moves-to-block-personal-ai-agents-from-booking-flights/" target="_blank" rel="noopener noreferrer" class="src-link">Skift</a> · <a href="https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm" target="_blank" rel="noopener noreferrer" class="src-link">8-K</a> · <a href="https://openai.com/index/introducing-chatgpt-wallet/" target="_blank" rel="noopener noreferrer" class="src-link">OpenAI</a><br>
                <em>Adoption:</em> <span class="badge-unqualified">UNQUALIFIED</span> Disney and Adobe agreed on 9 Nov to build generative AI models trained on Disney’s own characters and environments. <a href="https://www.thewrap.com/industry-news/business/disney-adobe-ai-strategic-partnership/" target="_blank" rel="noopener noreferrer" class="src-link">TheWrap</a></td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #1e3a5f;">Europe</td>
                <td>Common EU rules for AI Act regulatory sandboxes. <em>Adoption:</em> <span class="badge-unqualified">UNQUALIFIED</span> France’s Pierre Fabre engaged XtalPi’s AI platform on 10 Nov for oncology drug design (<a href="https://www.worldpharma.ai/insights" target="_blank" rel="noopener noreferrer" class="src-link">World Pharma AI</a>); Germany’s GEA showed AI herd-management functions at EuroTier on 11 Nov (<a href="https://www.gea.com/en/news/press-releases/2026/eurotier-dairynet-intelligence.jsp" target="_blank" rel="noopener noreferrer" class="src-link">GEA</a>) <a href="https://eur-lex.europa.eu/eli/reg_impl/2026/2487/oj/eng" target="_blank" rel="noopener noreferrer" class="src-link">EUR-Lex</a></td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #1e3a5f;">United Kingdom</td>
                <td>A $720M inference-chip round with state funds participating. <em>Adoption:</em> <span class="badge-unqualified">UNQUALIFIED</span> Addleshaw Goddard said on 9 Nov it will put Harvey’s legal AI before more than 3,400 staff firmwide. <a href="https://www.law360.com/legalindustry/articles/2547781" target="_blank" rel="noopener noreferrer" class="src-link">Law360</a> · <a href="https://siliconangle.com/2026/11/11/inference-chip-developer-fractile-raises-720m-in-funding/" target="_blank" rel="noopener noreferrer" class="src-link">SiliconANGLE</a></td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #1e3a5f;">Middle East</td>
                <td>ADGM notice pairing AI governance with cyber risk. <em>Adoption:</em> <span class="badge-unqualified">UNQUALIFIED</span> Gulf banks’ AI adoption was ranked on 11 Nov by a London market-intelligence firm; among GCC banks listed, First Abu Dhabi Bank placed third, Al Rajhi ninth and Mashreq tenth. The ranking is the firm’s own and it sells into the market it measures. <a href="https://fortune.com/middle-east/2026/11/11/gcc-banks-ai-adoption-ranking-2026/" target="_blank" rel="noopener noreferrer" class="src-link">Fortune</a> · <a href="https://finreg-e.com/weekly-regulatory-round-up-15-november-2026/" target="_blank" rel="noopener noreferrer" class="src-link">Regulatory summary</a></td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #1e3a5f;">Canada</td>
                <td>Ontario's securities regulator publishes what its AI governance examination found <a href="https://www.osc.ca/en/news-events/news/osc-highlights-importance-governance-and-oversight-ai-adoption" target="_blank" rel="noopener noreferrer" class="src-link">OSC release</a></td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #64748b;">India</td>
                <td style="color: #64748b; font-style: italic;">No item located in this window, including in secondary sources.</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #1e3a5f;">Japan</td>
                <td><span class="badge-unqualified">UNQUALIFIED</span> KDDI, which reports almost 73 million mobile customers, began a multi-year programme with Ciena’s Blue Planet and Accenture to automate network operations — starting with fixed networks, extending to mobile in 2028 — after lab trials of AI-driven alarm handling and fault remediation. No contract value was disclosed. <a href="https://www.sdxcentral.com/articles/news/kddi-ciena-blue-planet-accenture-ai-automation/2026/11/" target="_blank" rel="noopener noreferrer" class="src-link">SDxCentral</a> · <a href="https://www.telecomtv.com/content/access-evolution/kddi-picks-blue-planet-accenture-for-oss-transformation-52014/" target="_blank" rel="noopener noreferrer" class="src-link">TelecomTV</a></td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #1e3a5f;">Australia</td>
                <td>Reserve Bank of Australia Assistant Governor (Economic) Sarah Hunter told the UBS Australasia Conference in Sydney on 9 Nov there is limited evidence AI has materially lifted productivity, while data-centre investment has risen tenfold in three years from a low base and could cause sharp repricing in equities and corporate debt if returns disappoint. RBA staff estimate more than 5% of Australian households’ financial wealth sits in AI-related shares, mainly through superannuation. <a href="https://www.rba.gov.au/speeches/2026/sp-ag-2026-11-09.html" target="_blank" rel="noopener noreferrer" class="src-link">RBA speech</a></td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Section: One Year Ago -->
      <section id="sec-one-year-ago" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag money">04 CAPITAL · P3</span>
            <span>ONE YEAR AGO</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="background: #fdfcf9; border: 1px solid #e2e8f0; border-radius: 3px; padding: 8px 12px; margin-top: 4px; font-size: 11px; line-height: 1.4; color: #1e293b;">
          <p style="margin-bottom: 4px;">
            In the same week of 2025, S&amp;P Global Market Intelligence published a digest whose subject was a cluster of major AI agent releases; we cite it for its title and date, not having read the full note. A year on, the question is no longer whether agents ship but whether merchants will let them pay.
          </p>
          <div style="font-size: 10px; color: #64748b;">
            Open: <a href="https://www.spglobal.com/market-intelligence/en/news-insights/blog/generative-ai-digest-major-ai-agent-releases" target="_blank" rel="noopener noreferrer" class="src-link">S&amp;P Global Market Intelligence, “Generative AI Digest: Major AI agent releases”, 13 Nov 2025, by Melissa Incera and Alex Johnston</a>. Only one item from that week met our sourcing rules; the others we found were carried only in round-ups.
          </div>
        </div>
      </section>

      <!-- Section: Leaders Said -->
      <section id="sec-leaders-said" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE · P3</span>
            <span>LEADERS SAID</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="display: flex; flex-direction: column; gap: 6px; margin-top: 6px;">
          <div class="quote-box-p3">
            <div class="quote-text-p3">
              “The Board has full confidence in Colette and the leadership team.”
            </div>
            <div class="quote-src-p3">
              Harvey C. Jones, newly appointed Chair of the Board, Nvidia, in the company's filing of 12 Nov 2026, which adds that it expects “operations, customer commitments and product roadmap to continue without interruption”. <a href="https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm" target="_blank" rel="noopener noreferrer" class="src-link">NVIDIA Form 8-K, 12 Nov 2026</a>
            </div>
          </div>

          <div class="quote-box-p3">
            <div class="quote-text-p3">
              “No doubt” more data centres will be built in the United States.
            </div>
            <div class="quote-src-p3">
              Christian Bruch, Chief Executive, Siemens Energy, speaking to CNBC on 11 Nov 2026 as the company reported record quarterly revenue. <a href="https://www.cnbc.com/2026/11/10/stock-market-today-live-updates.html" target="_blank" rel="noopener noreferrer" class="src-link">CNBC, 11 Nov 2026</a>
            </div>
          </div>

          <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 2px;">
            Two statements met our rule that a quotation be verbatim, attributed to a named person with title and date, and taken from a primary filing or a bylined report read at source. A third, from a cloud executive on a healthcare launch, was dropped because it reached us only through a republished copy of the original report.
          </div>
        </div>
      </section>

      <!-- Page 3 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 08 · Page 3 of 7</div>
      </footer>
    </article>


    <!-- ==================== PAGE 4 OF 7 ==================== -->
    <article id="page-4" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>9–15 NOV 2026 · PAGE 4 OF 7</span>
      </div>

      <!-- Section: Lead: The Checkout Decision -->
      <section id="sec-lead-checkout">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag">01 GROWTH · P4</span>
            <span>LEAD: THE CHECKOUT DECISION</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <div style="font-size: 10px; font-weight: 800; color: #1e3a5f; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px;">
            AGENTIC COMMERCE · 11–13 NOV 2026 · UNITED STATES, GLOBAL
          </div>
          <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 15.5px; font-weight: 800; line-height: 1.25; color: #122119; margin-bottom: 6px;">
            Within 48 hours, one airline locked unauthorised third-party AI agents out of its checkout and OpenAI set out what merchants must change to accept agent payments — a decision and a requirement, landing two days apart
          </h2>

          <div class="two-col-equal" style="gap: 12px; margin-bottom: 6px;">
            <div style="font-size: 11px; line-height: 1.45; color: #1c2e24;">
              <p style="margin-bottom: 4px;">
                On 11 November United Airlines said it would restrict “unauthorized, third-party personal AI agents or assistants” from its website and app, and indirectly through travel agencies and aggregators. The settled part is the transaction: reports of its revised contract say an agent may not book, change or service a ticket, or buy seats, upgrades or extras — and that this holds even where the passenger supervises and approves every step. United has said that a consumer granting an agent access does not by itself mean the agent can transact. Accounts differ on whether searching and displaying fares are also restricted: some report that search remains open, others that the terms reach it, and we have not resolved it. Separately, its website terms prohibit using its pricing, schedules and availability data to train or evaluate machine learning models. United gave account security, unintended transactions and regulatory concerns as its reasons.
              </p>
              <p>
                On 13 November OpenAI launched ChatGPT Wallet, which lets agents complete purchases with user approval, using tokenised cards. It was built with American Express, Mastercard and Visa, and is limited at launch to ChatGPT Pro subscribers in the United States aged 18 or over with eligible US-issued cards. OpenAI says it does not hold customer funds. OpenAI also published a playbook for merchants. It says that to accept payment from the wallet, websites need to ensure agents are “not inadvertently blocked”, and that payment and risk systems need to recognise legitimate purchases made by agents. It points merchants at their CDN and firewall settings and at Web Bot Auth, which lets an agent sign its requests.
              </p>
            </div>

            <!-- Our Summary Box -->
            <div>
              <div class="business-lens-box" style="background: #f0fdf4; border-left: 3px solid #16a34a; padding: 8px 12px;">
                <div class="business-lens-label" style="color: #166534;">OUR SUMMARY · WHY THIS IS THE WEEK'S LEAD</div>
                <p style="margin-bottom: 4px; font-size: 11px; line-height: 1.4; color: #14532d;">
                  Both point at one question: <strong>is an AI agent at the checkout a customer or an intruder?</strong> Only the airline has answered it. OpenAI has not — it has set out what a merchant must change in order to answer yes, which is a condition of doing this business, not a decision of its own.
                </p>
                <p style="margin-bottom: 4px; font-size: 11px; line-height: 1.4; color: #14532d;">
                  Where a business has not taken this decision explicitly, it is being settled anyway — by bot-detection rules, CDN settings and fraud scoring configured before agents could buy anything. That is a commercial policy set by default, by systems nobody briefed.
                </p>
                <p style="font-size: 11px; line-height: 1.4; color: #14532d;">
                  The unglamorous question underneath it is liability: when an agent buys on a customer's behalf and the charge is disputed, who is refunded, and on whose authority.
                </p>
              </div>
            </div>
          </div>

          <div style="font-size: 10.5px; color: #444; margin-bottom: 6px;">
            Open: <a href="https://skift.com/2026/11/11/united-airlines-moves-to-block-personal-ai-agents-from-booking-flights/" target="_blank" rel="noopener noreferrer" class="src-link">Skift on United, 11 Nov</a> · <a href="https://www.cio.com/article/4248161/united-airlines-becomes-the-latest-enterprise-to-shut-its-door-to-customer-bots-2.html" target="_blank" rel="noopener noreferrer" class="src-link">CIO</a> · <a href="https://www.phocuswire.com/news/technology/united-blocks-third-party-ai-agents-from-app-website" target="_blank" rel="noopener noreferrer" class="src-link">PhocusWire, for United’s Digital Trust Center wording</a> · <a href="https://openai.com/index/introducing-chatgpt-wallet/" target="_blank" rel="noopener noreferrer" class="src-link">OpenAI, 13 Nov</a> · <a href="https://www.digitalcommerce360.com/2026/11/16/openai-chatgpt-wallet-for-ai-purchases-through-retailer-checkouts/" target="_blank" rel="noopener noreferrer" class="src-link">Digital Commerce 360</a> · <a href="https://finance.yahoo.com/technology/ai/articles/openai-debuts-chatgpt-payment-method-170611135.html" target="_blank" rel="noopener noreferrer" class="src-link">Bloomberg</a>
          </div>

          <div class="table-wrap">
            <table class="brief-table">
              <thead>
                <tr>
                  <th style="width: 140px;">PARTY · DATE</th>
                  <th>POSITION ON AGENTS AT THE CHECKOUT</th>
                  <th style="width: 80px;">SOURCE</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>United Airlines</strong><br><span style="font-size: 10px; color: #555;">11 Nov · airline</span></td>
                  <td>Restricts unauthorised third-party personal AI agents across its own platforms and indirectly through agencies and aggregators. An agent may not book, change or service a ticket, or buy extras, even where the passenger approves each step. Accounts differ on whether display and search are also restricted. Terms bar use of its pricing and schedule data to train or evaluate models.</td>
                  <td><a href="https://skift.com/2026/11/11/united-airlines-moves-to-block-personal-ai-agents-from-booking-flights/" target="_blank" rel="noopener noreferrer" class="src-link">Skift</a></td>
                </tr>
                <tr>
                  <td><strong>OpenAI</strong><br><span style="font-size: 10px; color: #555;">13 Nov · model maker</span></td>
                  <td>Launched ChatGPT Wallet so agents can complete purchases with user approval, using tokenised cards and a security check on every purchase. OpenAI says existing card protections are preserved and that it does not hold customer funds. Its merchant playbook sets conditions for accepting these payments: sites must not inadvertently block agents, and risk systems must recognise agent purchases.</td>
                  <td><a href="https://openai.com/index/introducing-chatgpt-wallet/" target="_blank" rel="noopener noreferrer" class="src-link">OpenAI</a></td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 3px;">
            Positions as described by each organisation or by the reports linked. Others in the same sector could not be placed: <a href="https://cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights" target="_blank" rel="noopener noreferrer" class="src-link">Southwest has made its flight inventory viewable to ChatGPT users</a>, and <a href="https://thepaypers.com/payments/news/united-airlines-moves-to-restrict-ai-agents-access-to-its-platforms" target="_blank" rel="noopener noreferrer" class="src-link">Expedia and Booking are reported to be working with OpenAI</a>, but neither source says whether either lets an agent complete a purchase — the step that matters here. Travel carries the clearest examples this week; the same question faces any business that sells through a website.
          </div>

          <!-- One Measured Finding Box -->
          <div class="highlight-finding-box" style="margin-top: 6px;">
            <div class="highlight-finding-title">ONE MEASURED FINDING, WITH ITS CONFLICT STATED</div>
            <p style="font-size: 11px; line-height: 1.4; color: #1e293b; margin-bottom: 3px;">
              In research reported by PhocusWire, two named agent products navigated 176 scripted booking requests as far as the payment step, with no captchas or login walls stopping them. The requests included airline bookings but were not limited to them. The research is Propellic's, a travel marketing agency selling services in the market it tested; the figure is its own and has not been independently replicated. Treat it as an indication that existing defences do not reliably tell agents apart, not a measure of your own estate.
            </p>
            <div style="font-size: 10px; color: #64748b;">
              Open: <a href="https://www.phocuswire.com/news/technology/united-blocks-third-party-ai-agents-from-app-website" target="_blank" rel="noopener noreferrer" class="src-link">PhocusWire</a>
            </div>
          </div>

          <!-- Ask Your Leadership Team box -->
          <div class="ask-team-box" style="margin-top: 6px;">
            <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTIONS</div>
            <ul class="lens-questions-list">
              <li>If an AI agent tried to buy from us today, what would happen — and does anyone here actually know?</li>
              <li>Who owns the decision: commercial, security, or whoever last configured the bot rules?</li>
              <li>When an agent buys and the customer disputes the charge, who do we refund, and what evidence do we have of authority?</li>
              <li>Are we losing orders right now from agents our defences silently turned away?</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Page 4 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 08 · Page 4 of 7</div>
      </footer>
    </article>


    <!-- ==================== PAGE 5 OF 7 ==================== -->
    <article id="page-5" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>9–15 NOV 2026 · PAGE 5 OF 7</span>
      </div>

      <!-- Section: Supplier & Governance Risk -->
      <section id="sec-supplier-risk">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag money">04 CAPITAL · P5</span>
            <span>SUPPLIER &amp; GOVERNANCE RISK</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <div style="font-size: 10px; font-weight: 800; color: #1e3a5f; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px;">
            CEO TRANSITION · 12 NOV 2026 · UNITED STATES
          </div>
          <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 15.5px; font-weight: 800; line-height: 1.25; color: #122119; margin-bottom: 6px;">
            Nvidia's chief executive resigned and the CFO took the role on an interim basis — the board's filing addresses the part buyers care about
          </h2>
          <p style="font-size: 11.5px; line-height: 1.45; color: #1c2e24; margin-bottom: 4px;">
            In a filing dated 12 November, Nvidia said Jensen Huang had resigned as President, Chief Executive Officer and a board member, effective immediately. Colette Kress, Executive Vice President and Chief Financial Officer, will serve as Interim Chief Executive Officer and continue as CFO until a permanent successor is named. The board is searching for one and will consider internal and external candidates. Harvey C. Jones was appointed the company's first-ever Chair of the Board. Kress has been CFO since September 2013, after nearly 25 years in finance roles at technology companies including Cisco and Microsoft.
          </p>
          <p style="font-size: 11.5px; line-height: 1.45; color: #1c2e24; margin-bottom: 4px;">
            The filing gives no reason. It followed widely reported allegations about the former chief executive's personal conduct, which the filing does not address and this brief does not report on. What the filing does address is continuity: the chair's statement speaks to operations, customer commitments and the product roadmap, quoted below.
          </p>
          <div style="font-size: 10.5px; color: #444; margin-bottom: 6px;">
            Open: <a href="https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm" target="_blank" rel="noopener noreferrer" class="src-link">NVIDIA Form 8-K, 12 Nov 2026</a> · <a href="https://www.cnn.com/2026/11/12/tech/jensen-huang-nvidia-resigns" target="_blank" rel="noopener noreferrer" class="src-link">CNN</a>
          </div>

          <!-- Business Lens & Ask Your Leadership Team pair -->
          <div class="lens-grid-pair">
            <div class="business-lens-box">
              <div class="business-lens-label">OUR SUMMARY · WHAT A BUYER SHOULD TAKE FROM IT</div>
              A board that names continuity of customer commitments in its first statement is telling you where it expects the questions to come from. For buyers the exposure is not the person; it is concentration. If your AI roadmap assumes one supplier's parts, prices and cadence, a leadership change there is a change to your plan.
            </div>
            <div class="ask-team-box">
              <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTIONS</div>
              <ul class="lens-questions-list">
                <li>Which parts of our AI roadmap assume one supplier, and what would a twelve-month delay there cost us?</li>
                <li>Do our contracts say anything about continuity of roadmap or supply, or only about price?</li>
                <li>Who here is responsible for watching supplier governance, not just supplier pricing?</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- Section: New LLM Releases or Security Patch Releases -->
      <section id="sec-model-releases" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag" style="background: #143826;">02 COST · P5</span>
            <span>NEW LLM RELEASES OR SECURITY PATCH RELEASES</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <p style="font-size: 11px; line-height: 1.4; color: #334155; margin-bottom: 6px;">
            Five models from three makers changed status between 9 and 12 November: four were released, one became generally available. Reported here as a cost and access question rather than a capability one. Figures are list prices per million tokens, as reported by the sources linked, and we did not verify each maker’s own price list.
          </p>

          <div class="table-wrap">
            <table class="brief-table">
              <thead>
                <tr>
                  <th style="width: 110px;">DATE · MAKER</th>
                  <th style="width: 220px;">WHAT CHANGED</th>
                  <th>PRICE AND ACCESS</th>
                  <th style="width: 80px;">SOURCE</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Anthropic</strong><br><span style="font-size: 10px; color: #555;">9 Nov</span></td>
                  <td>Released Claude Fable 5.2 and Claude Mythos 5.2 on the same day.</td>
                  <td>Fable 5.2 reported at $8 input / $40 output per million tokens, which the reports linked put at 20% below its predecessor.</td>
                  <td><a href="https://www.anthropic.com/claude-fable-and-mythos-5-2" target="_blank" rel="noopener noreferrer" class="src-link">Anthropic</a></td>
                </tr>
                <tr>
                  <td><strong>Meta</strong><br><span style="font-size: 10px; color: #555;">9 Nov</span></td>
                  <td>Released Muse Ember, described as the smallest and cheapest model in its Muse family, distilled from a larger model and aimed at repetitive agentic work such as tool calls and extraction.</td>
                  <td>Reported at $0.10 input / $0.50 output per million tokens, with availability via the Meta Model API and several cloud gateways.</td>
                  <td><a href="https://research.meta.ai/blog/muse-ember" target="_blank" rel="noopener noreferrer" class="src-link">Meta</a></td>
                </tr>
                <tr>
                  <td><strong>Google</strong><br><span style="font-size: 10px; color: #555;">10 Nov</span></td>
                  <td>Gemini 4 Carbon became generally available to paying developers and enterprises, having previously been in preview for cybersecurity defenders.</td>
                  <td>Introductory $2 uncached input / $10 output until 30 November, then $4 / $20, per Google's own footnote, which limits the change to the publicly available Carbon model. Cached input is discounted 95%.</td>
                  <td><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/" target="_blank" rel="noopener noreferrer" class="src-link">Google</a></td>
                </tr>
                <tr>
                  <td><strong>Google</strong><br><span style="font-size: 10px; color: #555;">12 Nov</span></td>
                  <td>Gemini 4 Hydrogen released, reported as Google’s everyday model for agentic workflows. We did not retrieve Google’s own page for this model.</td>
                  <td>Reported at $1.50 / $7.50 per million tokens. Sources differ on the release date, giving 12 or 13 November.</td>
                  <td><a href="https://www.vals.ai/models/anthropic_claude-fable-5-2" target="_blank" rel="noopener noreferrer" class="src-link">Vals AI index</a></td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 3px;">
            Prices as reported by the sources linked; we did not verify each maker's own price list. Our view: the access change matters as much as the prices — a model once restricted to security defenders is now generally available, which is a question for whoever maintains your approved-model list. Anthropic, which appears in this table, also makes the AI assistant used to research and draft this brief; see the <a href="#sec-caution-note" class="pdf-link">caution note</a>.
          </div>
        </div>
      </section>

      <!-- Page 5 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 08 · Page 5 of 7</div>
      </footer>
    </article>


    <!-- ==================== PAGE 6 OF 7 ==================== -->
    <article id="page-6" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>9–15 NOV 2026 · PAGE 6 OF 7</span>
      </div>

      <!-- Section: Laws, Rules & Guidance -->
      <section id="sec-laws-guidance">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag risk">03 RISK · P6</span>
            <span>LAWS, RULES &amp; GUIDANCE</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <p style="font-size: 11px; line-height: 1.4; color: #334155; margin-bottom: 6px;">
            Four regulators acted inside one week, in four different postures: the EU set operating rules, Abu Dhabi issued a supervisory notice, the United States imposed licensing, and Ontario’s securities regulator published what an inspection had already found.
          </p>

          <div class="table-wrap">
            <table class="brief-table">
              <thead>
                <tr>
                  <th style="width: 140px;">JURISDICTION · DATE</th>
                  <th>WHAT WAS ISSUED, AND WHAT IT REQUIRES</th>
                  <th style="width: 110px;">SOURCE</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>European Union</strong><br><span style="font-size: 10px; color: #555;">10–11 Nov</span></td>
                  <td>Commission Implementing Regulation (EU) 2026/2487, adopted 10 November and published in the Official Journal on 11 November, lays down common rules for the establishment, operation and supervision of the AI regulatory sandboxes required by the AI Act. The Official Journal entry gives a date of effect of 1 December 2026 and records entry into force as pending notification. The 2 August 2027 deadline for member states to run a national sandbox comes from the AI Act timeline as amended, not from this instrument.</td>
                  <td><a href="https://eur-lex.europa.eu/eli/reg_impl/2026/2487/oj/eng" target="_blank" rel="noopener noreferrer" class="src-link">EUR-Lex, OJ L 2026/2487</a></td>
                </tr>
                <tr>
                  <td><strong>UAE · ADGM</strong><br><span style="font-size: 10px; color: #555;">10 Nov</span></td>
                  <td>The Financial Services Regulatory Authority issued FCCP Notice No. 222 of 2026 on Artificial Intelligence and Cyber Risk Management, pairing AI governance and cyber risk in a single supervisory instrument for firms in the financial free zone. Our view: the structural choice is the notable part — the two are supervised together rather than separately.</td>
                  <td><a href="https://finreg-e.com/weekly-regulatory-round-up-15-november-2026/" target="_blank" rel="noopener noreferrer" class="src-link">FinReg-E summary</a></td>
                </tr>
                <tr>
                  <td><strong>Canada · Ontario</strong><br><span style="font-size: 10px; color: #555;">12 Nov</span></td>
                  <td>The Ontario Securities Commission published Staff Notice 33-763, setting out what its examination of registered firms found about AI use and governance. It reports most firms early in adoption, with weaknesses in governance and training and instances of possible “AI washing” — marketing claims about AI that firms could not substantiate. The OSC is a provincial regulator; Canada has no single national securities regulator. Our view: findings from a completed examination are a different thing from guidance — they show what a regulator actually found when it looked.</td>
                  <td><a href="https://www.osc.ca/en/news-events/news/osc-highlights-importance-governance-and-oversight-ai-adoption" target="_blank" rel="noopener noreferrer" class="src-link">OSC release, 12 Nov</a></td>
                </tr>
                <tr>
                  <td><strong>United States · BIS</strong><br><span style="font-size: 10px; color: #555;">15 Nov</span></td>
                  <td>The Commerce Department's Bureau of Industry and Security issued an interim final rule extending export licensing requirements to remote access to advanced AI chips in data centres outside the United States that supply large amounts of compute to companies headquartered in certain jurisdictions, and formally rescinding the earlier AI Diffusion Rule. Our view: the practical question for any business is whether compute it rents abroad now falls inside a licensing requirement.</td>
                  <td><a href="https://www.lexology.com/library/detail.aspx?g=8f4f2d82-e275-4764-8c2e-19f3bafcc3cf" target="_blank" rel="noopener noreferrer" class="src-link">Law firm analysis</a></td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 3px;">
            Qualification: the EU regulation is taken from the Official Journal text itself and the Ontario notice from the commission's own release. The ADGM notice is reported from a regulatory summary rather than the regulator's own page, which we were unable to open for this issue; its date and instrument number are as that source gives them, so confirm with the issuing regulator before acting. The US measure is an interim final rule, which takes effect while comment is still open, and is reported here only for its compliance effect.
          </div>
        </div>
      </section>

      <!-- Section: Vendor & Security Risk -->
      <section id="sec-vendor-risk" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag risk">03 RISK · P6</span>
            <span>VENDOR &amp; SECURITY RISK</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <div style="font-size: 10px; font-weight: 800; color: #7f1d1d; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px;">
            FBI FLASH-20261113-001 · 13 NOV 2026 · TEN SECTORS
          </div>
          <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 15px; font-weight: 800; line-height: 1.25; color: #122119; margin-bottom: 6px;">
            The FBI named ten sectors already targeted by an open-source AI intrusion framework, and pointed at the systems companies watch least
          </h2>

          <div class="two-col-equal" style="gap: 12px;">
            <div style="font-size: 11px; line-height: 1.45; color: #1c2e24;">
              <p style="margin-bottom: 4px;">
                On 13 November the FBI issued FLASH-20261113-001, “Threat Overview of ARTEX Autonomous Penetration Testing Framework”. ARTEX is an open-source, model-driven penetration-testing framework published on GitHub in July 2026. The bureau says a variety of malicious actors have used it since at least August 2026 to “automate multiple phases of cyber intrusions at machine speed”, from reconnaissance through to data exfiltration.
              </p>
              <p style="margin-bottom: 4px;">
                The alert names ten targeted sectors: financial services, government, technology, defence, semiconductors, energy, healthcare, manufacturing, telecommunications and legal. It reports that some intrusions reached privileged access in under three hours, and singles out partner and supplier portals, mobile backends, sales-support systems, legacy services and third-party integrations as the entry points it names. Incidents described in the accounts linked below include attacks on financial institutions in South Korea involving personal information of roughly 67,000 individuals, and a supply-chain compromise affecting customers of a cloud backup product.
              </p>
              <div style="font-size: 10px; color: #64748b;">
                Open: <a href="https://www.infosecurity-magazine.com/news/fbi-growing-abuse-ai-pentesting/" target="_blank" rel="noopener noreferrer" class="src-link">Infosecurity Magazine (Kevin Poireault)</a> · <a href="https://www.secureworld.io/industry-news/fbi-artex-flash-ai-attacks" target="_blank" rel="noopener noreferrer" class="src-link">SecureWorld</a> · <a href="https://www.safebreach.com/blog/artex-ai-attack-framework-fbi-flash-alert-20261113-001-safebreach-coverage/
" target="_blank" rel="noopener noreferrer" class="src-link">SafeBreach</a>. The FLASH itself is distributed to recipients rather than published at a public URL; these are bylined accounts of it. SafeBreach sells breach-simulation software and has a commercial interest in this subject.
              </div>
            </div>

            <!-- What Makes This a Board Item -->
            <div>
              <div class="ask-team-box" style="background: #fffbeb; border-left: 3px solid #f59e0b; padding: 8px 12px;">
                <div class="ask-team-label" style="color: #b45309;">WHAT MAKES THIS A BOARD ITEM</div>
                <p style="margin-bottom: 4px; font-size: 11px; line-height: 1.4; color: #78350f;">
                  The entry points the FBI names are not the systems most security budgets defend. Partner portals, supplier integrations and sales-support tools are typically owned by a business function, built by someone else, and inventoried nowhere.
                </p>
                <p style="margin-bottom: 4px; font-size: 11px; line-height: 1.4; color: #78350f;">
                  <strong>Our view:</strong> the three-hour figure changes the planning assumption more than the framework does. A response process that assumes a day or two of dwell time before privileged access is a process built for a different attacker.
                </p>
                <p style="font-size: 10px; line-height: 1.35; color: #92400e;">
                  A separate count by Censys put publicly exposed ARTEX consoles above 1,600 in early November. That is a count of exposed consoles, not of breaches, and it is Censys's figure rather than the bureau's.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Section: Key Numbers -->
      <section id="sec-key-numbers" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag risk">03 RISK · P6</span>
            <span>KEY NUMBERS</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div class="numbers-grid-6-clean" style="margin-top: 6px;">
          <div class="stat-card-p5">
            <div>
              <div class="stat-val-p5">10</div>
              <div class="stat-desc-p5">sectors named as targeted in the FBI's 13 Nov alert (<a href="https://www.infosecurity-magazine.com/news/fbi-growing-abuse-ai-pentesting/" target="_blank" rel="noopener noreferrer" class="src-link">FBI alert</a>)</div>
            </div>
            <a href="#sec-vendor-risk" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
          </div>

          <div class="stat-card-p5">
            <div>
              <div class="stat-val-p5">&lt;3 hrs</div>
              <div class="stat-desc-p5">from targeting to privileged access in some intrusions, per that alert (<a href="https://www.infosecurity-magazine.com/news/fbi-growing-abuse-ai-pentesting/" target="_blank" rel="noopener noreferrer" class="src-link">FBI alert</a>)</div>
            </div>
            <a href="#sec-vendor-risk" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
          </div>

          <div class="stat-card-p5">
            <div>
              <div class="stat-val-p5">1,600+</div>
              <div class="stat-desc-p5">publicly exposed consoles counted by Censys in early Nov — its figure, not breaches (<a href="https://www.infosecurity-magazine.com/news/fbi-growing-abuse-ai-pentesting/" target="_blank" rel="noopener noreferrer" class="src-link">FBI alert</a>)</div>
            </div>
            <a href="#sec-vendor-risk" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
          </div>

          <div class="stat-card-p5">
            <div>
              <div class="stat-val-p5">$720M</div>
              <div class="stat-desc-p5">raised by one UK inference-chip maker, ahead of a 2027 product (<a href="https://siliconangle.com/2026/11/11/inference-chip-developer-fractile-raises-720m-in-funding/" target="_blank" rel="noopener noreferrer" class="src-link">SiliconANGLE</a>)</div>
            </div>
            <a href="#sec-investments" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
          </div>

          <div class="stat-card-p5">
            <div>
              <div class="stat-val-p5">52.7%</div>
              <div class="stat-desc-p5">of 182 surveyed healthcare operators report a live agentic workflow (<a href="https://www.accessnewswire.com/newsroom/en/healthcare-and-pharmaceutical/healthcare-leaders-identify-priorities-for-agentic-ai-adoption-in-202-1249788" target="_blank" rel="noopener noreferrer" class="src-link">Black Book</a>)</div>
            </div>
            <a href="#sec-sector-index" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
          </div>

          <div class="stat-card-p5">
            <div>
              <div class="stat-val-p5">2×</div>
              <div class="stat-desc-p5">the list price of one model from 1 Dec, when its introductory rate ends, per <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/" target="_blank" rel="noopener noreferrer" class="src-link">Google</a></div>
            </div>
            <a href="#sec-model-releases" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
          </div>
        </div>
      </section>

      <!-- Page 6 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 08 · Page 6 of 7</div>
      </footer>
    </article>


    <!-- ==================== PAGE 7 OF 7 ==================== -->
    <article id="page-7" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>9–15 NOV 2026 · PAGE 7 OF 7</span>
      </div>

      <!-- Section: Investments · $100M and Above -->
      <section id="sec-investments">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag money">04 CAPITAL · P7</span>
            <span>INVESTMENTS · $100M AND ABOVE</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <div style="font-size: 10px; color: #475569; font-style: italic; margin-bottom: 4px;">
            Only rounds of $100 million or more are reported. Valuations are excluded as a standing rule, because they can be contested by the parties.
          </div>

          <div class="table-wrap">
            <table class="brief-table">
              <thead>
                <tr>
                  <th style="width: 130px;">COMPANY · DATE</th>
                  <th>AMOUNT AND BACKERS</th>
                  <th>WHAT IT FUNDS</th>
                  <th style="width: 120px;">SOURCE</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Fractile</strong><br><span style="font-size: 10px; color: #555;">11 Nov · UK</span></td>
                  <td>$720M Series C. The UK government confirmed the round on 11 November, with its Sovereign AI Venture Fund and the British Business Bank among backers in a round it put at more than £500 million. Reported lead-investor lists differ between accounts and we could not reconcile them.</td>
                  <td>Inference chips that integrate DRAM memory with logic to reduce data movement. First commercial chip planned for 2027. Our view: the money is ahead of the product.</td>
                  <td><a href="https://siliconangle.com/2026/11/11/inference-chip-developer-fractile-raises-720m-in-funding/" target="_blank" rel="noopener noreferrer" class="src-link">SiliconANGLE</a> · <a href="https://www.silicon.co.uk/cloud/ai/fractile-funding-round-2-632302" target="_blank" rel="noopener noreferrer" class="src-link">Silicon UK</a></td>
                </tr>
                <tr>
                  <td><strong>Agile Robots</strong><br><span style="font-size: 10px; color: #555;">12 Nov · Germany</span></td>
                  <td>$500M Series F led by SoftBank Group. The company’s announcement names NVIDIA, Hitachi, Hitachi Ventures and T.Capital among participants and does not disclose how the amount splits between them. It puts total capital raised to date at $2bn.</td>
                  <td>Physical-AI robots for industrial work, US expansion and production capacity. The company says its German plant can build up to 10,000 legged and wheeled humanoid robots a year.</td>
                  <td><a href="https://www.automate.org/robotics/news/physical-ai-leader-agile-robots-raises-500-million-series-f-at-8-5-billion-valuation-to-accelerate-global-growth" target="_blank" rel="noopener noreferrer" class="src-link">Agile Robots announcement</a></td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 3px;">
            Why two rounds are listed. At least three further rounds of $100 million or more were reported in this window. The only sources we could find for them were funding trackers and aggregated round lists, which our sourcing rules exclude, so they are not reported here. Fractile is listed because two bylined outlets and a government confirmation carry it, and Agile Robots because its own announcement does. Even there, we could not locate the company's own announcement, amounts agree across accounts but investor lists do not, and the disagreement is stated above rather than resolved by picking one. Separately, Anthropic began an IPO roadshow on 11 November; reported offering sizes vary widely, so no figure is given, and Anthropic makes the AI assistant used to produce this brief.
          </div>
        </div>
      </section>

      <!-- Section: Workforce & Talent · Research -->
      <section id="sec-workforce-talent" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE · P7</span>
            <span>WORKFORCE &amp; TALENT · RESEARCH</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div class="two-col-equal" style="margin-top: 6px; gap: 12px;">
          <div>
            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 14.5px; font-weight: 800; line-height: 1.25; color: #122119; margin-bottom: 4px;">
              A labour-market preprint finds the early effects of AI in who is working, not how many are working
            </h2>
            <p style="font-size: 11px; line-height: 1.45; color: #1c2e24; margin-bottom: 4px;">
              A revised preprint posted to arXiv on 10 November examines how labour outcomes have changed across occupations as AI capability advanced from chatbots to reasoning models and agents. The authors build an occupational AI exposure score from task-level assessments against O*NET task data and link it to US Current Population Survey records. In the revised version, part-time work declined, weekly hours rose slightly, and the workforce in exposed occupations became older and more educated — effects appearing in the composition of the workforce rather than in the number of jobs.
            </p>
            <p style="font-size: 11px; line-height: 1.45; color: #1c2e24; margin-bottom: 4px;">
              <strong>The authors' own caveats do most of the work here.</strong> They state that they “refrain from interpreting the estimated coefficients as causal effects”. They warn that standard errors are likely understated, because the public-use survey lacks the identifiers needed for design-based corrections, and advise weighting magnitude and direction over statistical significance. The exposure score measures potential capability, not actual adoption or substitution. They name post-pandemic recovery, interest rates and trade policy as possible confounders.
            </p>
            <div style="font-size: 10px; color: #444;">
              Open: <a href="https://arxiv.org/abs/2507.08244" target="_blank" rel="noopener noreferrer" class="src-link">arXiv:2507.08244</a> — Jacob Dominski and Yong Suk Lee, University of Notre Dame, econ.GN. Preprint, not peer reviewed. Version note: arXiv's own rendered copies carry a v3 stamp dated 10 Nov 2026 and the findings above, while the listing page we retrieved shows only v1 from July 2025, whose reported results differ — an earlier version associated higher exposure with reduced employment. We report the revised version and flag the discrepancy rather than resolving it.
            </div>
          </div>

          <!-- Why a CHRO should care -->
          <div>
            <div class="business-lens-box" style="background: #fdfaf6; border-left: 3px solid #b45309; padding: 8px 12px;">
              <div class="business-lens-label" style="color: #92400e;">OUR SUMMARY · WHY A CHRO SHOULD CARE</div>
              <p style="font-size: 11px; line-height: 1.4; color: #292524; margin-bottom: 4px;">
                Most workforce planning for AI is expressed as a headcount number. If the early effects really do land in composition — hours, age mix, education mix, full-time share — then a headcount forecast can look stable while the shape of the workforce underneath it changes considerably.
              </p>
              <p style="font-size: 11px; line-height: 1.4; color: #292524; margin-bottom: 4px;">
                That is a measurement question you can answer in your own data this quarter, without waiting for the literature to settle: it is the one claim here you do not have to take on trust.
              </p>
              <p style="font-size: 10px; line-height: 1.35; color: #78350f;">
                Given the caveats above, treat this as a hypothesis worth testing internally, not a finding to plan on.
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Section: Infrastructure & Capacity -->
      <section id="sec-infrastructure" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag" style="background: #143826;">02 COST · P7</span>
            <span>INFRASTRUCTURE &amp; CAPACITY</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 3px; padding: 8px 12px; margin-top: 4px; font-size: 11px; line-height: 1.4; color: #1e293b;">
          <p style="margin-bottom: 4px;">
            Siemens Energy reported record quarterly revenue this week, with its chief executive saying he has “no doubt” more data centres will be built in the United States, while noting that gas remains the main driver of generation. Our view: for most businesses this is a cost and siting line rather than a sustainability one — power availability is becoming a constraint on where compute can be bought, and therefore on what it costs. A US federal electricity forecast attributing record consumption partly to AI data centres was also reported this week. Its figures are held back until they can be cited to the agency's own publication.
          </p>
          <div style="font-size: 10px; color: #64748b;">
            Open: <a href="https://www.cnbc.com/2026/11/10/stock-market-today-live-updates.html" target="_blank" rel="noopener noreferrer" class="src-link">CNBC on Siemens Energy, 11 Nov</a>.
          </div>
        </div>
      </section>

      <!-- Caution Note & Signoff -->
      <section id="sec-caution-note" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE · P7</span>
            <span>CAUTION NOTE</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="background: #fdfcf9; border: 1px solid #dcd7ca; border-radius: 3px; padding: 8px 12px; margin-top: 4px; display: flex; flex-direction: column; gap: 4px; font-size: 10.5px; line-height: 1.4; color: #252f2a;">
          <p>
            <strong>CAUTION NOTE · PLEASE READ BEFORE USING ANYTHING HERE</strong><br>
            Data and news in this brief must be independently verified before being used for business purposes. Headlines, summaries, role tips, leadership actions and anything marked “Our view” or “Our summary” are the editor's wording, not the sources'. Every source name in this issue is a link: tap it to open the original and check it yourself. Where accounts disagree — on investor lists, a release date, or a preprint's version — we have said so in the item rather than choosing one. Several items this week are reported from secondary accounts because the issuing body's own page could not be retrieved; each says so where it applies. Research in this issue is a preprint and is not peer reviewed. One survey cited is published by a research firm selling into the market it surveyed, and one security vendor cited sells products in the area it comments on; both are flagged at the point of use. Disclosure: this brief is researched and drafted with the assistance of Claude, an AI assistant made by Anthropic; Anthropic appears in this issue in the model-release table, among the sources for the 60-second summary, and in the investments note, and is reported there on the same basis as any other company.
          </p>
          <p>
            Found this useful? A thumbs up on LinkedIn helps other leaders find it. · <a href="#agenda" class="jump-agenda-btn" style="display: inline-block;">Back to the agenda ↑</a>
          </p>
        </div>
      </section>

      <!-- Page 7 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a> · By Jayaraman (Jay) Ganapathi, People Prime Worldwide</div>
        <div class="page-footer-right">Edition 08 · Page 7 of 7</div>
      </footer>
    </article>

  </main>

  """ + tracking_script + """
</body>
</html>
"""

full_html = head_html + "\n" + body_html
with open('ai-newsletter-issue-08.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Generated ai-newsletter-issue-08.html successfully! Size:", len(full_html))
