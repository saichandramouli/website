import re

# Read head from ai-newsletter-issue-05.html
with open('ai-newsletter-issue-05.html', 'r', encoding='utf-8') as f:
    content_05 = f.read()

head_match = re.search(r'(<!DOCTYPE html>.*?<style>.*?</style>.*?</head>)', content_05, re.DOTALL)
if not head_match:
    raise ValueError("Could not find head section")

head_html = head_match.group(1)

head_html = head_html.replace(
    '<title>The AI Leadership Brief · Issue 05 | People Prime Worldwide</title>',
    '<title>The AI Leadership Brief · Issue 06 | People Prime Worldwide</title>'
)

old_meta_desc = '<meta name="description" content="The AI Leadership Brief (Edition 05 · 19–25 October 2026) — The week’s AI developments that matter to CXOs and decision-makers by Jayaraman (Jay) Ganapathi. Frontier models cross cloud lines, llm-d v1.0, agentic intrusions, oversight suppression, Australia data center power gap, and SEC disclosure shadow.">'
new_meta_desc = '<meta name="description" content="The AI Leadership Brief (Edition 06 · 26 Oct–1 Nov 2026) — The week’s AI developments that matter to CXOs and senior leaders by Jayaraman (Jay) Ganapathi, People Prime Worldwide. Demand shows up in results, SK hynix & Intel supply, OpenAI GPT-6.1 Terra, Gemini 4 Carbon, agent decision gates, prompt injection trust regions, and FuriosaAI $620M.">'
head_html = head_html.replace(old_meta_desc, new_meta_desc)

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

tracking_match = re.search(r'(<!-- GOOGLE ANALYTICS INTERACTION & READING TRACKING -->.*?)</body>', content_05, re.DOTALL)
tracking_script = tracking_match.group(1) if tracking_match else ""

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
        <span class="issue-btn active">Issue 06 (Current)</span>
        <a href="ai-newsletter-issue-05.html" class="issue-btn">Issue 05</a>
        <a href="ai-newsletter-issue-04.html" class="issue-btn">Issue 04</a>
        <a href="ai-newsletter-issue-03.html" class="issue-btn">Issue 03</a>
        <a href="ai-newsletter-issue-02.html" class="issue-btn">Issue 02</a>
      </div>
    </div>

    <div class="toolbar-center">
      <div class="page-jump-links" role="navigation" aria-label="Page navigation">
        <span class="jump-label">Jump to:</span>
        <a href="#page-1" class="page-jump-link">
          <span class="page-label-full">Page 1</span>
          <span class="page-label-short">P1</span>
        </a>
        <a href="#page-2" class="page-jump-link">
          <span class="page-label-full">Page 2</span>
          <span class="page-label-short">P2</span>
        </a>
        <a href="#page-3" class="page-jump-link">
          <span class="page-label-full">Page 3</span>
          <span class="page-label-short">P3</span>
        </a>
        <a href="#page-4" class="page-jump-link">
          <span class="page-label-full">Page 4</span>
          <span class="page-label-short">P4</span>
        </a>
        <a href="#page-5" class="page-jump-link">
          <span class="page-label-full">Page 5</span>
          <span class="page-label-short">P5</span>
        </a>
        <a href="#page-6" class="page-jump-link">
          <span class="page-label-full">Page 6</span>
          <span class="page-label-short">P6</span>
        </a>
      </div>
    </div>

    <div class="toolbar-right">
      <a href="assets/the-ai-leadership-brief-issue-06.pdf" download class="toolbar-btn" title="Download Original PDF">
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

  <!-- PUBLICATION CONTENT: 6 PAGE SHEETS -->
  <main class="publication-container">

    <!-- ALL ISSUES ARCHIVE / SELECTOR BANNER -->
    <div class="issues-nav-banner">
      <div class="issues-nav-left">
        <span class="issues-nav-label">ARCHIVE / ISSUES:</span>
        <a href="ai-newsletter-issue-06.html" class="issues-nav-pill active">
          <strong>Issue 06</strong> · 26 Oct – 1 Nov 2026 (Latest)
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

    <!-- ==================== PAGE 1 OF 6 ==================== -->
    <article id="page-1" class="page-sheet">
      <!-- Issue Header -->
      <div class="issue-top-header">
        <span>W E E K L Y · E D I T I O N 0 6</span>
        <span>2 6 O C T – 1 N O V 2 0 2 6 · P A G E 1 O F 6</span>
      </div>

      <!-- Masthead -->
      <div class="issue-title-block">
        <h1 class="masthead-title">The AI Leadership Brief</h1>
        <p class="masthead-subtitle">Edition 06 · 26 Oct–1 Nov 2026 · By Jayaraman (Jay) Ganapathi, People Prime Worldwide · For CXOs and senior leaders</p>
      </div>

      <!-- Cartoon of the Week -->
      <section id="sec-cartoon-week">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE &amp; ACTION · P1</span>
            <span>CARTOON OF THE WEEK</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div class="cartoon-container">
          <div class="cartoon-layout">
            <div class="cartoon-img-wrap">
              <img src="assets/images/ai-leadership-brief-issue-06-cartoon-art.png" alt="Cartoon: AI Memory Sold Out, robots lining up with ticket #4,512" class="cartoon-real-img">
            </div>
            <div class="cartoon-text-side">
              <div class="cartoon-dialogue">
                “This week: SK hynix says memory supply is not keeping pace — and even the robots are queuing for AI memory.”
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Agenda Box -->
      <nav id="agenda" class="agenda-container" aria-label="Newsletter Agenda">
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
            <span class="agenda-badge c1">01 Growth &amp; revenue</span>
            <div class="agenda-subtitle">Where is AI paying?</div>
            <ul class="agenda-links">
              <li><a href="#sec-60-sec-summary">p1 60-second summary</a></li>
              <li><a href="#sec-lead-results">p2 Lead: results &amp; supply</a></li>
              <li><a href="#sec-key-numbers">p6 Key numbers</a></li>
              <li><a href="#sec-leaders-said">p6 Leaders said</a></li>
            </ul>
          </div>

          <!-- Col 2 -->
          <div class="agenda-col">
            <span class="agenda-badge c2">02 Cost &amp; output</span>
            <div class="agenda-subtitle">What gets cheaper?</div>
            <ul class="agenda-links">
              <li><a href="#sec-new-releases">p2 New LLM releases or security patch releases</a></li>
              <li><a href="#sec-ai-research">p3 AI research</a></li>
            </ul>
          </div>

          <!-- Col 3 -->
          <div class="agenda-col">
            <span class="agenda-badge c3">03 Risk &amp; compliance</span>
            <div class="agenda-subtitle">What could hurt us?</div>
            <ul class="agenda-links">
              <li><a href="#sec-vendor-risk">p3 Vendor &amp; security risk</a></li>
              <li><a href="#sec-unsolved-problems">p4 Unsolved problems</a></li>
              <li><a href="#sec-laws-guidance">p4 Laws &amp; guidance</a></li>
            </ul>
          </div>

          <!-- Col 4 -->
          <div class="agenda-col">
            <span class="agenda-badge c4">04 Capital &amp; markets</span>
            <div class="agenda-subtitle">Where is money going?</div>
            <ul class="agenda-links">
              <li><a href="#sec-investments">p5 Investments ($100M+)</a></li>
              <li><a href="#sec-infrastructure">p4 Infrastructure</a></li>
              <li><a href="#sec-regional-index">p5 Regional index</a></li>
              <li><a href="#sec-upcoming-events">p6 Upcoming events</a></li>
            </ul>
          </div>

          <!-- Col 5 -->
          <div class="agenda-col">
            <span class="agenda-badge c5">05 People &amp; action</span>
            <div class="agenda-subtitle">What do we do?</div>
            <ul class="agenda-links">
              <li><a href="#sec-roles-week">p1 Your role</a></li>
              <li><a href="#sec-leadership-actions">p1 Actions</a></li>
              <li><a href="#sec-operating-models">p5 Operating models</a></li>
              <li><a href="#sec-workforce-talent">p5 Workforce</a></li>
              <li><a href="#sec-one-year-ago">p6 One year ago</a></li>
              <li><a href="#sec-caution-note">p6 Caution note</a></li>
            </ul>
          </div>
        </div>
      </nav>

      <!-- Agenda Notice Bar -->
      <div class="agenda-notice-bar">
        <span><strong>New section (p2):</strong> Every item now carries a <em>Business lens</em> (fact from the source unless marked “Our summary”) and <em>Ask your leadership team</em> (editor's questions, not claims). Data quality section skipped (no qualifying item). <a href="#sec-caution-note" class="pdf-link">Verify before business use.</a></span>
      </div>

      <!-- Section: 60-Second Summary -->
      <section id="sec-60-sec-summary">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag">01 GROWTH &amp; REVENUE · P1</span>
            <span>60-SECOND SUMMARY</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div class="summary-list" style="margin-top: 6px;">
          <div class="summary-item-row">
            <div class="summary-num-circle">1</div>
            <div class="summary-text">
              <strong>Demand is in the numbers.</strong> SK hynix revenue +328% (prelim.); Intel Data Center and AI +78% (not attributed to AI by Intel); Capgemini's 2026 forecast raised, partly via acquisitions. <a href="#sec-lead-results" class="brief-link">›</a>
            </div>
          </div>
          <div class="summary-item-row">
            <div class="summary-num-circle">2</div>
            <div class="summary-text">
              <strong>Supply is on chipmakers' agenda.</strong> SK hynix expects memory demand to exceed supply through 2030; Intel's CEO says the priority is to “unlock additional supply”. <a href="#sec-lead-results" class="brief-link">›</a>
            </div>
          </div>
          <div class="summary-item-row">
            <div class="summary-num-circle">3</div>
            <div class="summary-text">
              <strong>One maker cut a model price.</strong> OpenAI priced GPT-6.1 Terra 50% below its predecessor (maker's claim); Google is offering Gemini 4 Carbon first to “a subset of cybersecurity defenders”. <a href="#sec-new-releases" class="brief-link">›</a>
            </div>
          </div>
          <div class="summary-item-row">
            <div class="summary-num-circle">4</div>
            <div class="summary-text">
              <strong>Vendor risk is real.</strong> A cloud provider's hosted model returned 155 responses containing other users' data; provider says it is fixed. <a href="#sec-vendor-risk" class="brief-link">›</a>
            </div>
          </div>
          <div class="summary-item-row">
            <div class="summary-num-circle">5</div>
            <div class="summary-text">
              <strong>Four large rounds.</strong> Four rounds of $100M+ totalling $1.27B (our sum of announced amounts): chips, cloud security, service agents and analytics. <a href="#sec-investments" class="brief-link">›</a>
            </div>
          </div>
        </div>
      </section>

      <!-- Section: This Week For Your Role -->
      <section id="sec-roles-week">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE &amp; ACTION · P1</span>
            <span>THIS WEEK FOR YOUR ROLE</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div class="roles-grid" style="margin-top: 6px;">
          <!-- CEO -->
          <div class="role-card">
            <div>
              <div class="role-title">CEO</div>
              <p class="role-desc">Capgemini forecasts 2026 growth of +9.0–9.5%, about 5 points from acquisitions.</p>
            </div>
            <a href="#sec-lead-results" class="role-go">›</a>
          </div>

          <!-- CFO -->
          <div class="role-card">
            <div>
              <div class="role-title">CFO</div>
              <p class="role-desc">GPT-6.1 Terra standard API: $1 / $5 per million tokens, 50% below its predecessor (maker's claim).</p>
            </div>
            <a href="#sec-new-releases" class="role-go">›</a>
          </div>

          <!-- CIO / CTO -->
          <div class="role-card">
            <div>
              <div class="role-title">CIO / CTO</div>
              <p class="role-desc">SK hynix expects memory demand to exceed supply through 2030 (company outlook).</p>
            </div>
            <a href="#sec-lead-results" class="role-go">›</a>
          </div>

          <!-- CISO / CRO -->
          <div class="role-card">
            <div>
              <div class="role-title">CISO / CRO</div>
              <p class="role-desc">Provider's account: it knew of a cache-size mismatch before launch; 155 responses exposed other users' data.</p>
            </div>
            <a href="#sec-vendor-risk" class="role-go">›</a>
          </div>

          <!-- CHRO -->
          <div class="role-card">
            <div>
              <div class="role-title">CHRO</div>
              <p class="role-desc">SAP India: 2 million people with AI skills by 2030; nearly 13% have taken part (company).</p>
            </div>
            <a href="#sec-workforce-talent" class="role-go">›</a>
          </div>

          <!-- COO -->
          <div class="role-card">
            <div>
              <div class="role-title">COO</div>
              <p class="role-desc">Hitachi plans a 35,000-person digital company with physical AI as a focus from 1 Apr 2027.</p>
            </div>
            <a href="#sec-operating-models" class="role-go">›</a>
          </div>
        </div>
      </section>

      <!-- Section: Leadership Actions This Week -->
      <section id="sec-leadership-actions">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE &amp; ACTION · P1</span>
            <span>LEADERSHIP ACTIONS THIS WEEK</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div class="actions-grid-2" style="margin-top: 6px;">
          <div class="action-item-card">
            <div class="action-circle-num">1</div>
            <div>
              <strong>Measure value, not activity.</strong> Ask each unit for one AI use case with a revenue, cost or cycle-time baseline. <a href="#sec-lead-results" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">2</div>
            <div>
              <strong>Lock in capacity.</strong> Check that cloud and hardware contracts cover the AI capacity your plans assume. <a href="#sec-lead-results" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">3</div>
            <div>
              <strong>Re-run rejected cases.</strong> Re-price AI business cases turned down on cost at this week's lower token prices (per OpenAI). <a href="#sec-new-releases" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">4</div>
            <div>
              <strong>Tighten vendor terms.</strong> Add data separation, incident notice and audit rights to AI vendor contracts. <a href="#sec-vendor-risk" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">5</div>
            <div>
              <strong>Gate agent actions.</strong> Require a check before AI agents move money, data or customer records. <a href="#sec-ai-research" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">6</div>
            <div>
              <strong>Confirm patching.</strong> Ask IT whether self-hosted AI serving software (vLLM, SGLang) is on the fixed versions. <a href="#sec-new-releases" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">7</div>
            <div>
              <strong>Set a skills target.</strong> Publish an AI-skills goal with progress reporting, as SAP India does. <a href="#sec-workforce-talent" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">8</div>
            <div>
              <strong>India operations:</strong> review MeitY's DEPA draft on AI training with partner data; it invites recommendations. <a href="#sec-laws-guidance" class="action-tag-link">›</a>
            </div>
          </div>
        </div>
      </section>

      <!-- Page 1 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 06 · Page 1 of 6</div>
      </footer>
    </article>


    <!-- ==================== PAGE 2 OF 6 ==================== -->
    <article id="page-2" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>26 OCT – 1 NOV 2026 · PAGE 2 OF 6</span>
      </div>

      <!-- Section: Lead: Demand Shows Up In The Results -->
      <section id="sec-lead-results">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag">01 GROWTH &amp; REVENUE · P2</span>
            <span>LEAD: DEMAND SHOWS UP IN THE RESULTS</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <div style="font-size: 10px; font-weight: 800; color: #1e3a5f; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px;">
            COMPANY RESULTS · 28–30 OCT 2026 · SOUTH KOREA, NORTH AMERICA, EUROPE
          </div>
          <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 15.5px; font-weight: 800; line-height: 1.25; color: #122119; margin-bottom: 6px;">
            A memory maker, a processor maker and an IT-services firm report growth; SK hynix says supply is not keeping pace and Intel's CEO prioritises more supply
          </h2>

          <div class="table-wrap">
            <table class="brief-table">
              <thead>
                <tr>
                  <th style="width: 130px;">COMPANY · DATE</th>
                  <th>WHAT IT REPORTED</th>
                  <th>DEMAND AND SUPPLY, IN THE COMPANY'S WORDS</th>
                  <th style="width: 70px;">SOURCE</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>SK hynix</strong><br><span style="font-size: 10px; color: #555;">28 Oct · memory chips</span></td>
                  <td>3Q26 revenue 104.6 trillion won, up 328% year on year; operating margin 80%. Preliminary and unaudited.</td>
                  <td>Supply “is not keeping pace with the growth of the market”; expects “the structure in which demand exceeds supply to persist through 2030” (company outlook, not an independent forecast).</td>
                  <td><a href="https://www.placera.se/pressmeddelanden/sk-hynix-announces-3q26-financial-results-20261028" target="_blank" rel="noopener noreferrer" class="src-link">Release</a><a href="https://www.placera.se/pressmeddelanden/sk-hynix-announces-3q26-financial-results-20261028" target="_blank" class="ref-badge">R1</a></td>
                </tr>
                <tr>
                  <td><strong>Intel</strong><br><span style="font-size: 10px; color: #555;">29 Oct · processors</span></td>
                  <td>3Q26 revenue $16.5B, up 21%; Data Center and AI segment $7.3B, up 78%. Q4 guidance $15.0–16.0B (company forecast).</td>
                  <td>Growth led by the Data Center and AI segment (our reading: the segment added about $3.2B, more than the group's total increase). CEO Lip-Bu Tan: “Our immediate priority is to unlock additional supply to meet extraordinary demand for our Xeon family.” (per company release). The release does not attribute the growth to AI.</td>
                  <td><a href="https://www.intc.com/news-events/press-releases/detail/1786/intel-reports-third-quarter-2026-financial-results" target="_blank" rel="noopener noreferrer" class="src-link">Release</a><a href="https://www.intc.com/news-events/press-releases/detail/1786/intel-reports-third-quarter-2026-financial-results" target="_blank" class="ref-badge">R24</a></td>
                </tr>
                <tr>
                  <td><strong>Capgemini</strong><br><span style="font-size: 10px; color: #555;">30 Oct · IT services</span></td>
                  <td>Q3 revenue €6,073M, up 11.7% at constant currency; bookings €5,401M, up 3.4%. 2026 growth outlook raised to +9.0% to +9.5% (constant currency; company forecast). Growth includes acquisitions (notably WNS and Cloud4C), which the company says had a “material contribution to growth” in North America, UK &amp; Ireland and Asia-Pacific; it estimates about 5 points of 2026 growth is inorganic and gives no Q3 organic figure.</td>
                  <td>CEO Aiman Ezzat: “Clients are now focused on deploying AI at enterprise scale” (per company release). The release cites clients “transforming their business operations with agentic AI”.</td>
                  <td><a href="https://www.capgemini.com/news/press-releases/q3-2026-momentum-drives-upgrade-in-capgeminis-2026-outlook/" target="_blank" rel="noopener noreferrer" class="src-link">Release</a><a href="https://www.capgemini.com/news/press-releases/q3-2026-momentum-drives-upgrade-in-capgeminis-2026-outlook/" target="_blank" class="ref-badge">R25</a></td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Bar chart -->
          <div class="stat-bar-card-clean" style="margin-top: 6px;">
            <div class="stat-bar-title-clean">
              YEAR-ON-YEAR GROWTH REPORTED THIS WEEK
            </div>
            <div style="display: flex; flex-direction: column; gap: 4px;">
              <div class="stat-bar-item">
                <div class="stat-bar-label" style="width: 230px;">SK hynix (prelim., unaudited)</div>
                <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 100%; background: #1e3a5f;"></div></div>
                <div class="stat-bar-val" style="width: 60px; color: #1e3a5f;">+328%</div>
              </div>
              <div class="stat-bar-item">
                <div class="stat-bar-label" style="width: 230px;">Intel Data Center &amp; AI</div>
                <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 23.8%; background: #1e3a5f;"></div></div>
                <div class="stat-bar-val" style="width: 60px; color: #1e3a5f;">+78%</div>
              </div>
              <div class="stat-bar-item">
                <div class="stat-bar-label" style="width: 230px;">Intel total revenue</div>
                <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 6.4%; background: #1e3a5f;"></div></div>
                <div class="stat-bar-val" style="width: 60px; color: #1e3a5f;">+21%</div>
              </div>
              <div class="stat-bar-item">
                <div class="stat-bar-label" style="width: 230px;">Capgemini (incl. acquisitions)</div>
                <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 3.6%; background: #1e3a5f;"></div></div>
                <div class="stat-bar-val" style="width: 60px; color: #1e3a5f;">+11.7%</div>
              </div>
            </div>
            <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 3px;">
              Company figures; measures differ (total vs segment; reported vs constant currency). Bars scaled to +328%.
            </div>
          </div>

          <!-- Business Lens & Ask Your Leadership Team pair -->
          <div class="lens-grid-pair">
            <div class="business-lens-box">
              <div class="business-lens-label">BUSINESS LENS · FROM THE SOURCES</div>
              SK hynix says supply “is not keeping pace” and expects demand to exceed it through 2030; Intel's CEO says the priority is to “unlock additional supply”; and Capgemini's CEO says clients are now focused on deploying AI at enterprise scale.
            </div>
            <div class="ask-team-box">
              <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTIONS</div>
              <ul class="lens-questions-list">
                <li>Have we secured the compute our AI plans assume, at a known price?</li>
                <li>Which of our AI use cases has a measured revenue or cost result we could report?</li>
                <li>Are we still in pilots while clients of our suppliers scale?</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- Section: New LLM Releases or Security Patch Releases -->
      <section id="sec-new-releases" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag" style="background: #143826;">02 COST &amp; OUTPUT · P2</span>
            <span>NEW LLM RELEASES OR SECURITY PATCH RELEASES</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <div class="table-wrap">
            <table class="brief-table">
              <thead>
                <tr>
                  <th style="width: 75px;">DATE</th>
                  <th style="width: 95px;">TYPE</th>
                  <th style="width: 220px;">WHAT WAS RELEASED</th>
                  <th>COST, ACCESS AND RISK (FROM THE SOURCE)</th>
                  <th style="width: 130px;">SOURCES</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>26 Oct</strong></td>
                  <td><span class="badge-tag-clean badge-model">MODEL</span></td>
                  <td><strong>OpenAI GPT-6.1 Terra</strong>, a medium-sized model for computer use and writing; for Plus, Pro, Enterprise and Edu users in ChatGPT Work and Codex, and via the API.</td>
                  <td>$1 input / $5 output per million tokens (standard API price), which the maker says is 50% below its predecessor; it also says tasks finish “over three times faster” than GPT-6 Astra and GPT-6.1 Sol. Maker's claims, as reported by BleepingComputer; OpenAI's page not opened.</td>
                  <td><a href="https://openai.com/index/introducing-gpt-6-1-terra/" target="_blank" rel="noopener noreferrer" class="src-link">Announcement</a><a href="https://openai.com/index/introducing-gpt-6-1-terra/" target="_blank" class="ref-badge">R2</a> · <a href="https://www.bleepingcomputer.com/news/artificial-intelligence/openai-launches-gpt-61-terra-with-3x-faster-ai-agents-50-percent-lower-pricing/" target="_blank" rel="noopener noreferrer" class="src-link">report</a><a href="https://www.bleepingcomputer.com/news/artificial-intelligence/openai-launches-gpt-61-terra-with-3x-faster-ai-agents-50-percent-lower-pricing/" target="_blank" class="ref-badge">R2a</a></td>
                </tr>
                <tr>
                  <td><strong>28 Oct</strong></td>
                  <td><span class="badge-tag-clean badge-model">MODEL</span><br><span class="badge-tag-clean badge-restricted">RESTRICTED</span></td>
                  <td><strong>Google Gemini 4 Carbon</strong>, Google's newest frontier model, for cybersecurity tasks and long-running engineering work.</td>
                  <td>$2 / $10 per million tokens. Offered first to “a subset of cybersecurity defenders” through a dedicated access programme while safeguards are tested (as reported by Reuters). Google's page not opened.</td>
                  <td><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/" target="_blank" rel="noopener noreferrer" class="src-link">Announcement</a><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/" target="_blank" class="ref-badge">R3</a> · <a href="https://www.khaleejtimes.com/business/google-launches-gemini-4-carbon-ai-model-with-cybersecurity-focus-2" target="_blank" rel="noopener noreferrer" class="src-link">Reuters</a><a href="https://www.khaleejtimes.com/business/google-launches-gemini-4-carbon-ai-model-with-cybersecurity-focus-2" target="_blank" class="ref-badge">R3a</a></td>
                </tr>
                <tr>
                  <td><strong>26 Oct</strong></td>
                  <td><span class="badge-tag-clean badge-patch">SECURITY PATCH</span></td>
                  <td><strong>vLLM v0.32.0</strong> and <strong>SGLang v0.5.22+</strong>, open-source engines for running AI models on your own servers.</td>
                  <td>Our view: relevant mainly where your teams or vendors self-host models. vLLM 0.32.0 fixes five advisories published 26 Oct (per CVE records and vulnerability databases; IDs in the Source Register); CISA's enrichment of one record lists no known exploitation (as of 5 Nov 2026). SGLang v0.5.22 or later is advised after the cache incident on p3.</td>
                  <td><a href="https://www.cve.org/CVERecord?id=CVE-2026-115915" target="_blank" rel="noopener noreferrer" class="src-link">CVE</a><a href="https://www.cve.org/CVERecord?id=CVE-2026-115915" target="_blank" class="ref-badge">R4</a> · <a href="https://osv.dev/vulnerability/PYSEC-2026-4349" target="_blank" rel="noopener noreferrer" class="src-link">OSV</a><a href="https://osv.dev/vulnerability/PYSEC-2026-4349" target="_blank" class="ref-badge">R4a</a> · <a href="https://github.com/vllm-project/vllm/releases/tag/v0.32.0" target="_blank" rel="noopener noreferrer" class="src-link">release</a><a href="https://github.com/vllm-project/vllm/releases/tag/v0.32.0" target="_blank" class="ref-badge">R4b</a> · <a href="https://blog.cloudflare.com/kv-cache-exposure-remediation/" target="_blank" rel="noopener noreferrer" class="src-link">report</a><a href="https://blog.cloudflare.com/kv-cache-exposure-remediation/" target="_blank" class="ref-badge">R5</a></td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="lens-grid-pair">
            <div class="business-lens-box">
              <div class="business-lens-label">BUSINESS LENS · FROM THE SOURCES</div>
              OpenAI prices GPT-6.1 Terra 50% below its predecessor (maker's claim). Google is offering Gemini 4 Carbon first to a subset of cybersecurity defenders.
            </div>
            <div class="ask-team-box">
              <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTIONS</div>
              <ul class="lens-questions-list">
                <li>Which AI business cases did we reject on cost that should be re-run now?</li>
                <li>Do we know which AI serving software our vendors run, and who patches it?</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- Page 2 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 06 · Page 2 of 6</div>
      </footer>
    </article>


    <!-- ==================== PAGE 3 OF 6 ==================== -->
    <article id="page-3" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>26 OCT – 1 NOV 2026 · PAGE 3 OF 6</span>
      </div>

      <!-- Section: AI Research: Reliability and Quality Checks -->
      <section id="sec-ai-research">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag" style="background: #143826;">02 COST &amp; OUTPUT · P3</span>
            <span>AI RESEARCH: RELIABILITY AND QUALITY CHECKS</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 6px;">
          <!-- Item 1: JevAct Decision Gate -->
          <div style="background: #fdfcf9; border: 1px solid #dcd7ca; border-radius: 3px; padding: 9px 12px; display: flex; flex-direction: column; gap: 4px;">
            <div style="font-size: 10px; font-weight: 800; color: #143826; text-transform: uppercase; letter-spacing: 0.5px;">PREPRINT · 28 OCT 2026 · AGENT RELIABILITY</div>
            <h3 style="font-size: 13.5px; font-weight: 800; color: #122119;">
              Preprint: a “decision gate” checks what an AI agent is about to do before it acts
            </h3>
            <p style="font-size: 11.5px; line-height: 1.45; color: #252f2a;">
              The authors' framework, JevAct, turns domain policies into checks that run before selected agent actions; a separate decision model scores the structured questions as probabilities, and flagged actions get targeted feedback for a bounded revision. No change to the agent's model or tools is needed. Tested with eleven LLM agents on τ²-bench Airline and Telecom tasks and a function-calling benchmark (BFCL), the authors report reliability gains, most consistent on telecom and BFCL; airline results were “more mixed”. Authors' own measurements; not peer reviewed.
            </p>
            <div style="font-size: 10px; color: #4b5850; font-style: italic; border-top: 1px solid #ede8de; padding-top: 3px;">
              Shoham I, David Y, Akrabi O, Bilgory E, Levy I, Marreed S, Zeltyn S, Shlomov S. “Think Before You Act: Decision Gate for LLM Agents.” arXiv preprint v1, 28 Oct 2026. <a href="https://arxiv.org/abs/2610.38620v1" target="_blank" rel="noopener noreferrer" class="src-link">arxiv.org/abs/2610.38620v1</a><a href="https://arxiv.org/abs/2610.38620v1" target="_blank" class="ref-badge">R10</a> · DOI 10.48550/arXiv.2610.38620 (arXiv-issued)
            </div>

            <div class="lens-grid-pair">
              <div class="business-lens-box">
                <div class="business-lens-label">BUSINESS LENS · FROM THE SOURCE</div>
                The tests use τ²-bench Airline and Telecom tasks and BFCL. The authors report gains were not uniform: airline results were “more mixed”.
              </div>
              <div class="ask-team-box">
                <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTIONS</div>
                <ul class="lens-questions-list">
                  <li>Before our agents act on customers, money or data, what stops a wrong action?</li>
                  <li>Who owns the policies an agent must follow?</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Item 2: Clinical trial reports -->
          <div style="background: #fdfcf9; border: 1px solid #dcd7ca; border-radius: 3px; padding: 9px 12px; display: flex; flex-direction: column; gap: 4px;">
            <div style="font-size: 10px; font-weight: 800; color: #143826; text-transform: uppercase; letter-spacing: 0.5px;">PREPRINT (MEDRXIV) · V2 POSTED 28 OCT 2026 · HEALTHCARE QUALITY ASSURANCE</div>
            <h3 style="font-size: 13.5px; font-weight: 800; color: #122119;">
              Preprint: AI models caught most planted errors in clinical-trial reports, and flagged issues in reports without them
            </h3>
            <p style="font-size: 11.5px; line-height: 1.45; color: #252f2a;">
              The authors inserted methodological errors into randomised clinical-trial reports and asked 15 LLMs (four open-weight) to review them. On 58 trials published in 2026, major-error detection ranged from 58% to 99%, with mean review times of 1.4 to 16.3 minutes. Models “still flagged 14% to 29% of the error types in control reports without inserted errors”. Limits: the human comparison (27% mean detection) comes from an earlier study of three reports; scoring used two blinded LLM judges; four authors are affiliated with ResearchHub Foundation, “whose open-science platform … is implementing AI-assisted review”. Not peer reviewed.
            </p>
            <div style="font-size: 10px; color: #4b5850; font-style: italic; border-top: 1px solid #ede8de; padding-top: 3px;">
              Brian D, Pereira Hernández XI, Yin H, Koury J, Rust R. “Large language models detect methodological errors that human peer review misses in clinical trials.” medRxiv preprint v2, posted 28 Oct 2026; v1 date not confirmed. <a href="https://www.medrxiv.org/content/10.64898/2026.10.25.26366455v2" target="_blank" rel="noopener noreferrer" class="src-link">doi.org/10.64898/2026.10.25.26366455</a><a href="https://www.medrxiv.org/content/10.64898/2026.10.25.26366455v2" target="_blank" class="ref-badge">R11</a>
            </div>

            <!-- Mini stats card -->
            <div class="stat-bar-card-clean" style="margin-top: 2px;">
              <div class="stat-bar-title-clean">ERROR-DETECTION SCORES, 58 TRIALS (2026)</div>
              <div style="display: flex; flex-direction: column; gap: 4px;">
                <div class="stat-bar-item">
                  <div class="stat-bar-label" style="width: 150px;">All models</div>
                  <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 99%; background: #15803d;"></div></div>
                  <div class="stat-bar-val" style="width: 65px; color: #15803d;">58–99%</div>
                </div>
                <div class="stat-bar-item">
                  <div class="stat-bar-label" style="width: 150px;">Open-weight</div>
                  <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 89%; background: #15803d;"></div></div>
                  <div class="stat-bar-val" style="width: 65px; color: #15803d;">66–89%</div>
                </div>
                <div class="stat-bar-item">
                  <div class="stat-bar-label" style="width: 150px;">Control flags</div>
                  <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 29%; background: #b45309;"></div></div>
                  <div class="stat-bar-val" style="width: 65px; color: #b45309;">14–29%</div>
                </div>
              </div>
              <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 3px;">
                Ranges as reported (0–100%). Control flags: share of error types flagged in control reports without inserted errors. 15 models reviewed 3 trials; 12 reviewed the other 55.
              </div>
            </div>

            <div class="lens-grid-pair">
              <div class="business-lens-box">
                <div class="business-lens-label">BUSINESS LENS · FROM THE SOURCE</div>
                Mean review times were 1.4 to 16.3 minutes; in control reports without inserted errors, models still flagged 14% to 29% of error types.
              </div>
              <div class="ask-team-box">
                <div class="ask-team-label">ASK YOUR TEAM · EDITOR'S QUESTION</div>
                Where could AI pre-screening speed our quality or compliance reviews, and who reviews the flags it raises?
              </div>
            </div>
          </div>

          <div style="font-size: 9.5px; color: #64748b; font-style: italic; padding: 2px 4px;">
            No peer-reviewed paper published in the week met this brief's relevance and sourcing rules; both items above are preprints.
          </div>
        </div>
      </section>

      <!-- Section: Vendor & Security Risk -->
      <section id="sec-vendor-risk" style="margin-top: 6px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag risk">03 RISK &amp; COMPLIANCE · P3</span>
            <span>VENDOR &amp; SECURITY RISK</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="background: #fdfcf9; border: 1px solid #dcd7ca; border-radius: 3px; padding: 9px 12px; margin-top: 6px; display: flex; flex-direction: column; gap: 4px;">
          <div style="font-size: 10px; font-weight: 800; color: #82291d; text-transform: uppercase; letter-spacing: 0.5px;">
            CLOUD AI SERVICE · REPORT DATED 26 OCT 2026 · PROVIDER'S OWN ACCOUNT
          </div>
          <h3 style="font-size: 13.5px; font-weight: 800; color: #122119;">
            A large cloud provider says 155 responses from one hosted model contained other users' data
          </h3>
          <p style="font-size: 11.5px; line-height: 1.45; color: #252f2a;">
            In the provider's incident report, a hosted coding model returned 155 responses containing data from other users' sessions between 27 Aug and 9 Sep 2026, all to very long prompts. The model was offered with a larger context window than its cache could hold; the provider says, “We were aware of this mismatch before launch.” A bug in the open-source SGLang engine then let those requests read leftover data from earlier requests. A researcher reported it on 8 Sep; the provider made the model private within about 40 minutes of declaring an incident, found “no evidence of deliberate exploitation”, and says no other hosted model was affected. The provider is not named because the news is negative.
          </p>
          <div style="font-size: 10px; color: #4b5850; border-top: 1px solid #ede8de; padding-top: 3px;">
            Source: <a href="https://blog.cloudflare.com/kv-cache-exposure-remediation/" target="_blank" rel="noopener noreferrer" class="src-link">provider's incident report</a><a href="https://blog.cloudflare.com/kv-cache-exposure-remediation/" target="_blank" class="ref-badge">R5</a>
          </div>

          <div class="lens-grid-pair">
            <div class="business-lens-box">
              <div class="business-lens-label">BUSINESS LENS · FROM THE SOURCE</div>
              Per the provider, the exposure ran from 27 Aug to 9 Sep, was reported by a security researcher through its HackerOne programme, and it knew of the size mismatch before launch.
            </div>
            <div class="ask-team-box">
              <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTIONS</div>
              <ul class="lens-questions-list">
                <li>Do our AI contracts cover data separation, incident notice and audit rights?</li>
                <li>Which sensitive workloads should run on dedicated rather than shared capacity?</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- Page 3 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 06 · Page 3 of 6</div>
      </footer>
    </article>


    <!-- ==================== PAGE 4 OF 6 ==================== -->
    <article id="page-4" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>26 OCT – 1 NOV 2026 · PAGE 4 OF 6</span>
      </div>

      <!-- Section: Unsolved Problems In AI -->
      <section id="sec-unsolved-problems">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag risk">03 RISK &amp; COMPLIANCE · P4</span>
            <span>UNSOLVED PROBLEMS IN AI</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="background: #fdfcf9; border: 1px solid #dcd7ca; border-radius: 3px; padding: 9px 12px; margin-top: 6px; display: flex; flex-direction: column; gap: 4px;">
          <div style="font-size: 10px; font-weight: 800; color: #82291d; text-transform: uppercase; letter-spacing: 0.5px;">PREPRINT · 28 OCT 2026 · PROMPT INJECTION</div>
          <h3 style="font-size: 13.5px; font-weight: 800; color: #122119;">
            Preprint: where a hidden instruction sits can change whether AI agents obey it
          </h3>
          <p style="font-size: 11.5px; line-height: 1.45; color: #252f2a;">
            The authors built three agent testbeds (tool use, coding and daily workflows) and moved the same injected instruction between locations. They report that agents trust some parts of their environment more than others, which they call the “trust region effect”. In one result, an agent powered by OpenAI's GPT-5.4 followed an unsafe instruction placed in a repository documentation file (README or TODO) 2.6 times more often on average than the same instruction placed in a code or data file. Not peer reviewed.
          </p>
          <div style="font-size: 10px; color: #4b5850; font-style: italic; border-top: 1px solid #ede8de; padding-top: 3px;">
            Guo C, Liu X, Yang W, Feng M, Song J, Ma Q, Buractaon C, White C, Li B, Gao J. “Where You Inject Matters: The Trust Region Effect in LLM Agents.” arXiv preprint v1, 28 Oct 2026. <a href="https://arxiv.org/abs/2610.38867" target="_blank" rel="noopener noreferrer" class="src-link">arxiv.org/abs/2610.38867</a><a href="https://arxiv.org/abs/2610.38867" target="_blank" class="ref-badge">R8</a> · DOI 10.48550/arXiv.2610.38867
          </div>

          <div class="lens-grid-pair">
            <div class="business-lens-box">
              <div class="business-lens-label">BUSINESS LENS · FROM THE SOURCE</div>
              In one result, an agent powered by GPT-5.4 followed the same unsafe instruction 2.6 times more often on average in a documentation file than in a code or data file.
            </div>
            <div class="ask-team-box">
              <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTION</div>
              Are our agents allowed to act on instructions they find in documents, emails or tickets?
            </div>
          </div>
        </div>
      </section>

      <!-- Section: Laws, Rules & Guidance -->
      <section id="sec-laws-guidance" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag risk">03 RISK &amp; COMPLIANCE · P4</span>
            <span>LAWS, RULES &amp; GUIDANCE</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="background: #fdfcf9; border: 1px solid #dcd7ca; border-radius: 3px; padding: 9px 12px; margin-top: 6px; display: flex; flex-direction: column; gap: 4px;">
          <div style="font-size: 10px; font-weight: 800; color: #82291d; text-transform: uppercase; letter-spacing: 0.5px;">
            INDIA · LAUNCHED IN BENGALURU, REPORTED 31 OCT 2026 · DRAFT FRAMEWORK
          </div>
          <h3 style="font-size: 13.5px; font-weight: 800; color: #122119;">
            MeitY releases a draft handbook for training AI on sensitive data without handing it over
          </h3>
          <p style="font-size: 11.5px; line-height: 1.45; color: #252f2a;">
            Status: marked “Draft for Discussion”; a framework, not a law. Scope: the handbook on the Data Empowerment and Protection Architecture (DEPA) for AI Training, prepared with the iSPIRT Foundation and steered by MeitY, proposes that training happens where the data sits: in its main design, raw data stays with the training-data provider inside secure data environments and is not exposed to those using it for training. It names roles including training-data providers and consumers and data-exchange platforms. It calls itself a “living resource”, invites “actionable recommendations” and gives no deadline. As reported by ETV Bharat, MeitY Secretary S Krishnan unveiled it at a roundtable.
          </p>
          <div style="font-size: 10.5px; color: #4b5850; border-top: 1px solid #ede8de; padding-top: 3px;">
            Sources: <a href="https://www.meity.gov.in/static/uploads/2026/10/02d8224e4cd6c8c29be5a5198e795158.pdf" target="_blank" rel="noopener noreferrer" class="src-link">MeitY handbook (PDF)</a><a href="https://www.meity.gov.in/static/uploads/2026/10/02d8224e4cd6c8c29be5a5198e795158.pdf" target="_blank" class="ref-badge">R12</a> · <a href="https://www.etvbharat.com/en/bharat/govt-launches-handbook-on-depa-for-ai-training-enn26103101486" target="_blank" rel="noopener noreferrer" class="src-link">ETV Bharat</a><a href="https://www.etvbharat.com/en/bharat/govt-launches-handbook-on-depa-for-ai-training-enn26103101486" target="_blank" class="ref-badge">R12a</a>
          </div>

          <div class="lens-grid-pair">
            <div class="business-lens-box">
              <div class="business-lens-label">BUSINESS LENS · FROM THE SOURCE</div>
              In the draft's main design, raw data stays with its provider and is not exposed to those training on it. The draft invites recommendations.
            </div>
            <div class="ask-team-box">
              <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTION</div>
              If we operate in India, would this model open data partnerships we cannot do today, and should we respond to the draft?
            </div>
          </div>
        </div>
      </section>

      <!-- Section: Infrastructure & Capacity -->
      <section id="sec-infrastructure" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag money">04 CAPITAL &amp; MARKETS · P4</span>
            <span>INFRASTRUCTURE &amp; CAPACITY</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="background: #fdfcf9; border: 1px solid #dcd7ca; border-radius: 3px; padding: 9px 12px; margin-top: 6px; display: flex; flex-direction: column; gap: 4px;">
          <div style="font-size: 10px; font-weight: 800; color: #164b58; text-transform: uppercase; letter-spacing: 0.5px;">
            EUROPE · ROMANIA · 30 OCT 2026 · COMPANY PLANS
          </div>
          <h3 style="font-size: 13.5px; font-weight: 800; color: #122119;">
            Runware plans an assembly line for factory-built AI data-centre pods
          </h3>
          <p style="font-size: 11.5px; line-height: 1.45; color: #252f2a;">
            As reported by TechCrunch, Runware's chief executive says the company plans to scale its Romania factory to 30 MW of data-centre capacity per day by 2028 (“nearly 1 gigawatt per month”), with a second factory due early next year and US expansion to follow. The liquid-cooled pods need power and internet but no water connection. Runware aims to have pods online within 48 hours of delivery (installation and setup, not manufacturing) and cites $1 billion of committed interest covering more than 20 MW. Company plans and claims, not measured output.
          </p>
          <div style="font-size: 10.5px; color: #4b5850; border-top: 1px solid #ede8de; padding-top: 3px;">
            Source: <a href="https://techcrunch.com/2026/10/30/can-ai-data-centers-be-mass-produced-like-cars-and-online-in-48-hours-this-startup-aims-to-find-out/" target="_blank" rel="noopener noreferrer" class="src-link">TechCrunch (Dominic-Madori Davis)</a><a href="https://techcrunch.com/2026/10/30/can-ai-data-centers-be-mass-produced-like-cars-and-online-in-48-hours-this-startup-aims-to-find-out/" target="_blank" class="ref-badge">R6</a>
          </div>

          <div class="lens-grid-pair">
            <div class="business-lens-box">
              <div class="business-lens-label">BUSINESS LENS · FROM THE SOURCE</div>
              Runware aims to bring pods online within 48 hours of delivery and to produce 30 MW of capacity per day by 2028 (company plans, not measured output).
            </div>
            <div class="ask-team-box">
              <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTION</div>
              Would modular, faster-to-deploy capacity change our build, rent or wait decision for AI compute?
            </div>
          </div>
        </div>
      </section>

      <!-- Page 4 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 06 · Page 4 of 6</div>
      </footer>
    </article>


    <!-- ==================== PAGE 5 OF 6 ==================== -->
    <article id="page-5" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>26 OCT – 1 NOV 2026 · PAGE 5 OF 6</span>
      </div>

      <!-- Section: Investments ($100M and Above) -->
      <section id="sec-investments">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag money">04 CAPITAL &amp; MARKETS · P5</span>
            <span>INVESTMENTS ($100M AND ABOVE)</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div class="table-wrap" style="margin-top: 6px;">
          <table class="brief-table">
            <thead>
              <tr>
                <th style="width: 110px;">COMPANY</th>
                <th style="width: 80px;">AMOUNT</th>
                <th style="width: 175px;">SERIES · LEAD(S)</th>
                <th>BUSINESS PROBLEM IT TARGETS</th>
                <th style="width: 210px;">CONFIRMED BY</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>FuriosaAI</strong></td>
                <td><strong style="color: #143826;">$620M</strong></td>
                <td>D · no lead named; largest investor Korea's National Growth Fund ($280M)</td>
                <td>AI inference chips for data centres; plans 20,000 units in 2026 and 40,000+ in 2027</td>
                <td><a href="https://via.tt.se/pressmeddelande/4620607/furiosaai-secures-dollar620-million-series-d-to-meet-surging-enterprise-ai-inference-demand-and-accelerate-next-gen-silicon?lang=en" target="_blank" rel="noopener noreferrer" class="src-link">Company release</a><a href="https://via.tt.se/pressmeddelande/4620607/furiosaai-secures-dollar620-million-series-d-to-meet-surging-enterprise-ai-inference-demand-and-accelerate-next-gen-silicon?lang=en" target="_blank" class="ref-badge">R13</a>, 29 Oct 2026</td>
              </tr>
              <tr>
                <td><strong>Upwind</strong></td>
                <td><strong style="color: #143826;">$400M</strong></td>
                <td>C · Bessemer Venture Partners</td>
                <td>Cloud and AI security</td>
                <td><a href="https://www.investing.com/news/company-news/upwind-closes-400-million-series-c-at-38-billion-valuation-as-revenue-quadruples-in-2026-4980378" target="_blank" rel="noopener noreferrer" class="src-link">Company release</a><a href="https://www.investing.com/news/company-news/upwind-closes-400-million-series-c-at-38-billion-valuation-as-revenue-quadruples-in-2026-4980378" target="_blank" class="ref-badge">R14</a> (not opened; <a href="https://wsau.com/?p=1030739" target="_blank" rel="noopener noreferrer" class="src-link">Reuters copy</a><a href="https://wsau.com/?p=1030739" target="_blank" class="ref-badge">R14a</a>), 28 Oct 2026</td>
              </tr>
              <tr>
                <td><strong>Serval</strong></td>
                <td><strong style="color: #143826;">$150M</strong></td>
                <td>C · Sequoia</td>
                <td>AI agents for enterprise service management</td>
                <td><a href="https://www.businesswire.com/news/home/20261029114967/en/Serval-Raises-%24150M-Series-C-at-%243B-Valuation-Led-by-Sequoia" target="_blank" rel="noopener noreferrer" class="src-link">Company release</a><a href="https://www.businesswire.com/news/home/20261029114967/en/Serval-Raises-%24150M-Series-C-at-%243B-Valuation-Led-by-Sequoia" target="_blank" class="ref-badge">R15</a> (not opened; <a href="https://fortune.com/2026/10/29/serval-servicenow-fight-series-c-3-billion-valuation-sequoia/" target="_blank" rel="noopener noreferrer" class="src-link">Fortune</a><a href="https://fortune.com/2026/10/29/serval-servicenow-fight-series-c-3-billion-valuation-sequoia/" target="_blank" class="ref-badge">R15a</a>), 29 Oct 2026</td>
              </tr>
              <tr>
                <td><strong>Hex</strong></td>
                <td><strong style="color: #143826;">$100M</strong></td>
                <td>Peak XV, 137 Ventures</td>
                <td>AI analytics for people and agents</td>
                <td><a href="https://hex.tech/blog/hex-new-era/" target="_blank" rel="noopener noreferrer" class="src-link">Company blog</a><a href="https://hex.tech/blog/hex-new-era/" target="_blank" class="ref-badge">R16</a> (not opened; <a href="https://dealstreetasia.com/stories/peak-xv-co-anchors-hex-funding-499490" target="_blank" rel="noopener noreferrer" class="src-link">DealStreetAsia</a><a href="https://dealstreetasia.com/stories/peak-xv-co-anchors-hex-funding-499490" target="_blank" class="ref-badge">R16a</a>), 27 Oct 2026</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div style="font-size: 9.5px; color: #4b5850; font-style: italic; margin-top: 4px; line-height: 1.35;">
          Only rounds of $100M or more, announced 26 Oct–1 Nov 2026. Amounts and leads come from each company's announcement; where we could not open it, a bylined report quoting it is linked. Total $1.27B is our sum of the four announced amounts; the “business problem” column is our short description. Counsel note supports only (R16b). No valuations.
        </div>

        <div class="lens-grid-pair">
          <div class="business-lens-box">
            <div class="business-lens-label">BUSINESS LENS · OUR SUMMARY</div>
            Inference chips, cloud and AI security, service-management agents and AI analytics.
          </div>
          <div class="ask-team-box">
            <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTIONS</div>
            In each category, are we buying, building or waiting, and are our current vendors keeping pace?
          </div>
        </div>
      </section>

      <!-- Middle: Operating Models: AI in Industrial Sectors -->
      <section id="sec-operating-models" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE &amp; ACTION · P5</span>
            <span>OPERATING MODELS: AI IN INDUSTRIAL SECTORS</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="background: #fdfcf9; border: 1px solid #dcd7ca; border-radius: 3px; padding: 9px 12px; margin-top: 6px; display: flex; flex-direction: column; gap: 4px;">
          <div style="font-size: 10px; font-weight: 800; color: #2f5223; text-transform: uppercase; letter-spacing: 0.5px;">
            INDUSTRIAL · JAPAN · 28 OCT 2026 · ANNOUNCED PLAN
          </div>
          <h3 style="font-size: 13.5px; font-weight: 800; color: #122119;">
            Hitachi to launch a 35,000-person digital services company with physical AI as a named focus
          </h3>
          <p style="font-size: 11.5px; line-height: 1.45; color: #252f2a;">
            Hitachi plans to launch Hitachi Digital Inc. on 1 April 2027, uniting GlobalLogic and Hitachi Digital Services: about 35,000 professionals in 27 countries serving more than 880 active clients. Named focus areas are physical AI, data and intelligence, cloud and site reliability engineering, and enterprise applications. An announced plan; the company is not yet operating.
          </p>
          <div style="font-size: 10.5px; color: #4b5850; border-top: 1px solid #ede8de; padding-top: 3px;">
            Source: <a href="https://www.hitachids.com/blog/hitachi-launches-digital-services-company/" target="_blank" rel="noopener noreferrer" class="src-link">Hitachi announcement</a><a href="https://www.hitachids.com/blog/hitachi-launches-digital-services-company/" target="_blank" class="ref-badge">R7</a>
          </div>

          <div class="lens-grid-pair">
            <div class="business-lens-box">
              <div class="business-lens-label">BUSINESS LENS · FROM THE SOURCE</div>
              Hitachi is uniting two digital units into one company of about 35,000 people serving more than 880 clients.
            </div>
            <div class="ask-team-box">
              <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTION</div>
              Is our AI capability run as a business with clients and targets, or spread across cost centres?
            </div>
          </div>
        </div>
      </section>

      <!-- Bottom Split: Workforce & Regional Index -->
      <div class="two-col-equal" style="margin-top: 8px;">
        <!-- Left: Workforce & Talent -->
        <section id="sec-workforce-talent">
          <div class="section-banner">
            <div class="section-banner-title">
              <span class="banner-theme-tag act">05 PEOPLE &amp; ACTION · P5</span>
              <span>WORKFORCE &amp; TALENT</span>
            </div>
            <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
          </div>

          <div style="background: #fdfcf9; border: 1px solid #dcd7ca; border-radius: 3px; padding: 9px 12px; margin-top: 6px; display: flex; flex-direction: column; gap: 4px;">
            <div style="font-size: 10px; font-weight: 800; color: #2f5223; text-transform: uppercase; letter-spacing: 0.5px;">
              INDIA · MUMBAI · 28 OCT 2026 · COMPANY PROGRAMME
            </div>
            <h3 style="font-size: 13px; font-weight: 800; color: #122119;">
              SAP India adds programmes toward 2 million people with AI skills by 2030
            </h3>
            <p style="font-size: 11px; line-height: 1.4; color: #252f2a;">
              SAP announced more programmes toward equipping two million people in India with AI-ready skills by 2030, part of a global pledge to help 12 million. SAP India says nearly 13% of the two million have already taken part through certification, student education and community programmes. Target and progress figures are the company's own.
            </p>
            <div style="font-size: 10px; color: #4b5850; border-top: 1px solid #ede8de; padding-top: 3px;">
              Source: <a href="https://news.sap.com/india/2026/10/sap-india-doubles-down-on-ai-skilling-to-prepare-two-million-people-for-the-future-of-work-by-2030/" target="_blank" rel="noopener noreferrer" class="src-link">SAP India News Center</a><a href="https://news.sap.com/india/2026/10/sap-india-doubles-down-on-ai-skilling-to-prepare-two-million-people-for-the-future-of-work-by-2030/" target="_blank" class="ref-badge">R9</a>
            </div>

            <div class="stat-bar-card-clean" style="margin-top: 2px;">
              <div class="stat-bar-title-clean">SAP INDIA AI-SKILLING GOAL</div>
              <div style="display: flex; flex-direction: column; gap: 4px;">
                <div class="stat-bar-item">
                  <div class="stat-bar-label" style="width: 110px;">Taken part</div>
                  <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 13%; background: #15803d;"></div></div>
                  <div class="stat-bar-val" style="width: 50px; color: #15803d;">~13%</div>
                </div>
                <div class="stat-bar-item">
                  <div class="stat-bar-label" style="width: 110px;">Goal by 2030</div>
                  <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 100%; background: #1e3a5f;"></div></div>
                  <div class="stat-bar-val" style="width: 50px; color: #1e3a5f;">2M</div>
                </div>
              </div>
              <div style="font-size: 9px; color: #64748b; font-style: italic; margin-top: 2px;">
                Company-reported progress toward its own target; not independently verified.
              </div>
            </div>

            <div class="ask-team-box" style="margin-top: 3px;">
              <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTION</div>
              What share of our workforce has AI training, and is it tied to changed roles?
            </div>
          </div>
        </section>

        <!-- Right: Regional Index -->
        <section id="sec-regional-index">
          <div class="section-banner">
            <div class="section-banner-title">
              <span class="banner-theme-tag people">04 CAPITAL &amp; MARKETS · P5</span>
              <span>REGIONAL INDEX</span>
            </div>
            <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
          </div>

          <div class="regional-table-card" style="margin-top: 6px;">
            <div class="regional-row">
              <div class="regional-region-name">North America</div>
              <div class="regional-news-list">
                <a href="#sec-lead-results" class="pdf-jump">Intel results</a> · <a href="#sec-investments" class="pdf-jump">Upwind</a> · <a href="#sec-investments" class="pdf-jump">Serval</a> · <a href="#sec-investments" class="pdf-jump">Hex</a> · <a href="#sec-vendor-risk" class="pdf-jump">Cross-tenant cache incident</a>
              </div>
            </div>
            <div class="regional-row">
              <div class="regional-region-name">Europe &amp; UK</div>
              <div class="regional-news-list">
                <a href="#sec-lead-results" class="pdf-jump">Capgemini results (France)</a> · <a href="#sec-infrastructure" class="pdf-jump">Runware pod factory (Romania)</a>
              </div>
            </div>
            <div class="regional-row">
              <div class="regional-region-name">India</div>
              <div class="regional-news-list">
                <a href="#sec-laws-guidance" class="pdf-jump">MeitY DEPA draft</a> · <a href="#sec-workforce-talent" class="pdf-jump">SAP India AI skilling</a>
              </div>
            </div>
            <div class="regional-row">
              <div class="regional-region-name">Japan</div>
              <div class="regional-news-list">
                <a href="#sec-operating-models" class="pdf-jump">Hitachi Digital (physical AI)</a>
              </div>
            </div>
            <div class="regional-row">
              <div class="regional-region-name">Australia</div>
              <div class="regional-news-list" style="color: #64748b; font-style: italic;">
                No AI item met our sourcing and relevance rules this week.
              </div>
            </div>
            <div class="regional-row">
              <div class="regional-region-name">South Korea</div>
              <div class="regional-news-list">
                <a href="#sec-lead-results" class="pdf-jump">SK hynix results and outlook</a> · <a href="#sec-investments" class="pdf-jump">FuriosaAI $620M</a>
              </div>
            </div>
            <div class="regional-row">
              <div class="regional-region-name">Global</div>
              <div class="regional-news-list">
                <a href="#sec-new-releases" class="pdf-jump">New models and patches</a> · <a href="#sec-unsolved-problems" class="pdf-jump">Injection placement</a> · <a href="#sec-ai-research" class="pdf-jump">Agent decision gate</a> · <a href="#sec-ai-research" class="pdf-jump">AI review of trials</a>
              </div>
            </div>
          </div>
        </section>
      </div>

      <!-- Page 5 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 06 · Page 5 of 6</div>
      </footer>
    </article>


    <!-- ==================== PAGE 6 OF 6 ==================== -->
    <article id="page-6" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>26 OCT – 1 NOV 2026 · PAGE 6 OF 6</span>
      </div>

      <!-- Top Split: Leaders Said & Key Numbers -->
      <div class="two-col-equal">
        <!-- Left: Leaders Said -->
        <section id="sec-leaders-said">
          <div class="section-banner">
            <div class="section-banner-title">
              <span class="banner-theme-tag">01 · P6</span>
              <span>LEADERS SAID</span>
            </div>
            <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
          </div>

          <div style="display: flex; flex-direction: column; gap: 6px; margin-top: 6px;">
            <div class="quote-box-p5">
              <div class="quote-text-p5">
                “Capgemini delivered another solid quarter, with growth of +11.7% at constant exchange rates”
              </div>
              <div class="quote-src-p5">
                Aiman Ezzat, CEO, Capgemini · per company release, Paris, 30 Oct 2026 · <a href="https://www.capgemini.com/news/press-releases/q3-2026-momentum-drives-upgrade-in-capgeminis-2026-outlook/" target="_blank" rel="noopener noreferrer" class="src-link">release</a><a href="https://www.capgemini.com/news/press-releases/q3-2026-momentum-drives-upgrade-in-capgeminis-2026-outlook/" target="_blank" class="ref-badge">R25</a>
              </div>
            </div>

            <div class="quote-box-p5">
              <div class="quote-text-p5">
                “This Series D financing marks an important milestone for FuriosaAI and reflects the confidence of investors around the world in our technology and ability to execute.”
              </div>
              <div class="quote-src-p5">
                June Paik, Co-Founder and CEO, FuriosaAI · per company release, 29 Oct 2026 · <a href="https://via.tt.se/pressmeddelande/4620607/furiosaai-secures-dollar620-million-series-d-to-meet-surging-enterprise-ai-inference-demand-and-accelerate-next-gen-silicon?lang=en" target="_blank" rel="noopener noreferrer" class="src-link">release</a><a href="https://via.tt.se/pressmeddelande/4620607/furiosaai-secures-dollar620-million-series-d-to-meet-surging-enterprise-ai-inference-demand-and-accelerate-next-gen-silicon?lang=en" target="_blank" class="ref-badge">R13</a>
              </div>
            </div>

            <div class="quote-box-p5">
              <div class="quote-text-p5">
                “Of the 2 million people we expect to train in AI skills before 2030, nearly 13% have already participated through certification, student education and community programmes.”
              </div>
              <div class="quote-src-p5">
                Manish Prasad, President and Managing Director, SAP Indian Subcontinent · per company release, Mumbai, 28 Oct 2026 · <a href="https://news.sap.com/india/2026/10/sap-india-doubles-down-on-ai-skilling-to-prepare-two-million-people-for-the-future-of-work-by-2030/" target="_blank" rel="noopener noreferrer" class="src-link">release</a><a href="https://news.sap.com/india/2026/10/sap-india-doubles-down-on-ai-skilling-to-prepare-two-million-people-for-the-future-of-work-by-2030/" target="_blank" class="ref-badge">R9</a>
              </div>
            </div>

            <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 2px;">
              All quotes come from company announcements. Intel's CEO quote appears in the lead (p2).
            </div>
          </div>
        </section>

        <!-- Right: Key Numbers -->
        <section id="sec-key-numbers">
          <div class="section-banner">
            <div class="section-banner-title">
              <span class="banner-theme-tag">01 · P6</span>
              <span>KEY NUMBERS</span>
            </div>
            <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
          </div>

          <div class="numbers-grid-6-clean" style="margin-top: 6px;">
            <div class="stat-card-p5">
              <div>
                <div class="stat-val-p5">+78%</div>
                <div class="stat-desc-p5">Intel Data Center and AI revenue, 3Q26 year on year (company)</div>
              </div>
              <a href="#sec-lead-results" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
            </div>

            <div class="stat-card-p5">
              <div>
                <div class="stat-val-p5">2030</div>
                <div class="stat-desc-p5">SK hynix expects memory demand to exceed supply through 2030 (company outlook)</div>
              </div>
              <a href="#sec-lead-results" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
            </div>

            <div class="stat-card-p5">
              <div>
                <div class="stat-val-p5">+9.0–9.5%</div>
                <div class="stat-desc-p5">Capgemini's raised 2026 outlook, constant currency; ~5 pts from acquisitions (company forecast)</div>
              </div>
              <a href="#sec-lead-results" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
            </div>

            <div class="stat-card-p5">
              <div>
                <div class="stat-val-p5">50%</div>
                <div class="stat-desc-p5">lower API price for OpenAI's GPT-6.1 Terra vs its predecessor (maker's claim)</div>
              </div>
              <a href="#sec-new-releases" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
            </div>

            <div class="stat-card-p5">
              <div>
                <div class="stat-val-p5">155</div>
                <div class="stat-desc-p5">responses with other users' data, one hosted model (provider's count)</div>
              </div>
              <a href="#sec-vendor-risk" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
            </div>

            <div class="stat-card-p5">
              <div>
                <div class="stat-val-p5">$1.27B</div>
                <div class="stat-desc-p5">across four rounds of $100M+ (our sum of announced amounts)</div>
              </div>
              <a href="#sec-investments" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
            </div>
          </div>
        </section>
      </div>

      <!-- Lower Split: One Year Ago & Upcoming Events -->
      <div class="two-col-equal" style="margin-top: 6px;">
        <!-- Left: One Year Ago -->
        <section id="sec-one-year-ago">
          <div class="section-banner">
            <div class="section-banner-title">
              <span class="banner-theme-tag act">05 · P6</span>
              <span>ONE YEAR AGO</span>
            </div>
            <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
          </div>

          <div style="display: flex; flex-direction: column; gap: 6px; margin-top: 6px;">
            <div style="font-size: 10px; color: #64748b; font-style: italic;">Same week in 2025: 26 Oct–1 Nov 2025.</div>
            <div class="history-item-p5">
              <div>
                <span class="history-date-p5">28 Oct 2025:</span> A large online retailer said it would cut about 14,000 corporate jobs as it ramped up AI spending (per AP).
              </div>
              <div class="history-src-p5">
                Associated Press: “[Company] cuts 14,000 corporate jobs as spending on artificial intelligence accelerates”, 28 Oct 2025. <a href="https://connecticut.news12.com/amazon-cuts-14000-corporate-jobs-as-spending-on-artificial-intelligence-accelerates" target="_blank" rel="noopener noreferrer" class="src-link">AP copy on News 12</a><a href="https://connecticut.news12.com/amazon-cuts-14000-corporate-jobs-as-spending-on-artificial-intelligence-accelerates" target="_blank" class="ref-badge">R21</a>
              </div>
            </div>

            <div class="history-item-p5">
              <div>
                <span class="history-date-p5">28 Oct 2025:</span> NVIDIA agreed a $1.0B equity investment in Nokia alongside an AI-RAN partnership for mobile networks.
              </div>
              <div class="history-src-p5">
                Nokia stock exchange release: “Inside Information: NVIDIA to make USD 1.0 billion equity investment in Nokia…”, 28 Oct 2025. <a href="https://www.nokia.com/newsroom/inside-information-nvidia-to-make-usd-1-billion-equity-investment-in-nokia-in-addition-to-new-strategic-partnership-nokias-board-resolved-on-directed-share-issuance-to-nvidia/" target="_blank" rel="noopener noreferrer" class="src-link">Open original</a><a href="https://www.nokia.com/newsroom/inside-information-nvidia-to-make-usd-1-billion-equity-investment-in-nokia-in-addition-to-new-strategic-partnership-nokias-board-resolved-on-directed-share-issuance-to-nvidia/" target="_blank" class="ref-badge">R22</a>
              </div>
            </div>

            <div class="history-item-p5">
              <div>
                <span class="history-date-p5">30 Oct 2025:</span> OpenAI put Aardvark, an “agentic security researcher”, into private beta; an archived copy of its page (Mar 2026) says the tool has since been renamed.
              </div>
              <div class="history-src-p5">
                OpenAI launch post: “Introducing Aardvark”, 30 Oct 2025. <a href="https://web.archive.org/web/20260329000702/https://openai.com/index/introducing-aardvark/" target="_blank" rel="noopener noreferrer" class="src-link">Archived original</a><a href="https://web.archive.org/web/20260329000702/https://openai.com/index/introducing-aardvark/" target="_blank" class="ref-badge">R23</a>
              </div>
            </div>
          </div>
        </section>

        <!-- Right: Upcoming Events -->
        <section id="sec-upcoming-events">
          <div class="section-banner">
            <div class="section-banner-title">
              <span class="banner-theme-tag people">04 · P6</span>
              <span>UPCOMING EVENTS</span>
            </div>
            <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
          </div>

          <div style="display: flex; flex-direction: column; gap: 6px; margin-top: 6px;">
            <div class="event-item-p5">
              <div class="event-dates-p5">15–20 Nov 2026</div>
              <div><a href="https://sc26.supercomputing.org/" target="_blank" rel="noopener noreferrer" class="src-link"><strong>SC26</strong> (high-performance computing and AI infrastructure)</a><a href="https://sc26.supercomputing.org/" target="_blank" class="ref-badge">R18</a> · McCormick Place, Chicago</div>
            </div>

            <div class="event-item-p5">
              <div class="event-dates-p5">16–19 Nov 2026</div>
              <div><a href="https://www.medica.de/" target="_blank" rel="noopener noreferrer" class="src-link"><strong>MEDICA</strong> (medical technology and digital health)</a><a href="https://www.medica.de/" target="_blank" class="ref-badge">R19</a> · Messe Düsseldorf <span style="font-size: 10px; color: #64748b; font-style: italic;">(dates per JETRO listing<a href="https://www.jetro.go.jp/en/database/j-messe/tradefair/detail/158547" target="_blank" class="ref-badge">R19a</a>)</span></div>
            </div>

            <div class="event-item-p5">
              <div class="event-dates-p5">9–10 Dec 2026</div>
              <div><a href="https://newyork.theaisummit.com/" target="_blank" rel="noopener noreferrer" class="src-link"><strong>The AI Summit New York</strong></a><a href="https://newyork.theaisummit.com/" target="_blank" class="ref-badge">R20</a> · Javits Center, New York</div>
              <div style="font-size: 10px; color: #64748b; font-style: italic;">(organiser site not opened; dates per event listings)</div>
            </div>

            <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 2px;">
              None of these events was listed in Edition 05.
            </div>
          </div>
        </section>
      </div>

      <!-- Caution Note & Signoff -->
      <section id="sec-caution-note" style="margin-top: 6px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE &amp; ACTION · P6</span>
            <span>CAUTION NOTE</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="background: #fdfcf9; border: 1px solid #dcd7ca; border-radius: 3px; padding: 8px 12px; margin-top: 4px; display: flex; flex-direction: column; gap: 4px; font-size: 11px; line-height: 1.4; color: #252f2a;">
          <p>
            <strong>Caution: verify before business use.</strong> This brief summarises the public sources linked beside each item. Forecasts, plans, preliminary results and maker's claims are the sources' own. Business lens lines restate the linked source unless marked “Our summary”; Ask your leadership team lines are the editor's questions, not facts or advice. Headlines, summaries, role tips and leadership actions are the editor's wording. Verify any item, figure or quote independently against the original source before using it for business decisions. Small red reference numbers (R1, R2…) point to the companion Source Register.
          </p>
          <p>
            Found this useful? Give it a 👍 on LinkedIn and share it with a colleague.
          </p>
          <p style="font-style: italic; color: #4b5850;">
            AI model makers are named; the cloud provider in the incident item is not named because the news is negative. Every item links to its source.
          </p>
        </div>
      </section>

      <!-- Page 6 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a> · By Jayaraman (Jay) Ganapathi, People Prime Worldwide</div>
        <div class="page-footer-right">Edition 06 · Page 6 of 6</div>
      </footer>
    </article>

  </main>

  """ + tracking_script + """
</body>
</html>
"""

full_html = head_html + "\n" + body_html
with open('ai-newsletter-issue-06.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Generated ai-newsletter-issue-06.html successfully! Size:", len(full_html))

