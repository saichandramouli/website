import re
import os

print("Building ai-newsletter-issue-07.html...")

# 1. Read base head and styles from ai-newsletter-issue-06.html
with open('ai-newsletter-issue-06.html', 'r', encoding='utf-8') as f:
    content_06 = f.read()

head_match = re.search(r'(<!DOCTYPE html>.*?<style>.*?</style>.*?</head>)', content_06, re.DOTALL)
if not head_match:
    raise ValueError("Could not find head section in issue 06")

head_html = head_match.group(1)

# Update title and meta description
head_html = head_html.replace(
    '<title>The AI Leadership Brief · Issue 06 | People Prime Worldwide</title>',
    '<title>The AI Leadership Brief · Issue 07 | People Prime Worldwide</title>'
)

old_meta_desc_06 = '<meta name="description" content="The AI Leadership Brief (Edition 06 · 26 Oct–1 Nov 2026) — The week’s AI developments that matter to CXOs and senior leaders by Jayaraman (Jay) Ganapathi, People Prime Worldwide. Demand shows up in results, SK hynix & Intel supply, OpenAI GPT-6.1 Terra, Gemini 4 Carbon, agent decision gates, prompt injection trust regions, and FuriosaAI $620M.">'
new_meta_desc_07 = '<meta name="description" content="The AI Leadership Brief (Edition 07 · 2–8 Nov 2026) — The week’s AI developments that matter to CXOs and senior leaders by Jayaraman (Jay) Ganapathi, People Prime Worldwide. Buyers of AI wait for return, AMD & CDW results, Tencent Hy4, OpenAI GPT-6 Cyber, agent architecture cost preprint, OCC bank AI framework, and fal $1.3B Series F.">'

head_html = head_html.replace(old_meta_desc_06, new_meta_desc_07)

# Extract tracking script from issue 06
tracking_match = re.search(r'(<!-- GOOGLE ANALYTICS INTERACTION & READING TRACKING -->.*?)</body>', content_06, re.DOTALL)
tracking_script = tracking_match.group(1) if tracking_match else ""

# Update tracking script issue references if any
tracking_script = tracking_script.replace('Issue 06', 'Issue 07').replace('issue_06', 'issue_07').replace('issue-06', 'issue-07')

# Construct the body
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
        <span class="issue-btn active">Issue 07 (Current)</span>
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
      <a href="assets/the-ai-leadership-brief-issue-07.pdf" download class="toolbar-btn" title="Download Original PDF">
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
        <a href="ai-newsletter-issue-07.html" class="issues-nav-pill active">
          <strong>Issue 07</strong> · 2 – 8 Nov 2026 (Latest)
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

    <!-- ==================== PAGE 1 OF 6 ==================== -->
    <article id="page-1" class="page-sheet">
      <!-- Issue Header -->
      <div class="issue-top-header">
        <span>W E E K L Y · E D I T I O N 0 7</span>
        <span>2 – 8 N O V 2 0 2 6 · P A G E 1 O F 6</span>
      </div>

      <!-- Masthead -->
      <div class="issue-title-block">
        <h1 class="masthead-title">The AI Leadership Brief</h1>
        <p class="masthead-subtitle">Edition 07 · 2–8 Nov 2026 · By Jayaraman (Jay) Ganapathi, People Prime Worldwide · For CXOs and senior leaders</p>
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
              <img src="assets/newsletters/issue-07-cartoon.png" alt="Cartoon: So where is the return on all this AI? It went up with the forecast, sir." class="cartoon-real-img">
            </div>
            <div class="cartoon-text-side">
              <div class="cartoon-dialogue">
                “This week: of 400 CFOs surveyed, just 10% call their AI returns significant today. 54% expect significant returns within 24 months.”
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
              <li><a href="#sec-lead-results">p2 Lead: the ROI scoreboard</a></li>
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
              <li><a href="#sec-infrastructure">p4 Infrastructure</a></li>
              <li><a href="#sec-investments">p5 Investments ($100M+)</a></li>
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
              <li><a href="#sec-operating-models">p3 Operating models</a></li>
              <li><a href="#sec-workforce-talent">p5 Workforce</a></li>
              <li><a href="#sec-one-year-ago">p6 One year ago</a></li>
              <li><a href="#sec-caution-note">p6 Caution note</a></li>
            </ul>
          </div>
        </div>
      </nav>

      <!-- Agenda Notice Bar -->
      <div class="agenda-notice-bar">
        <span>This issue leads with business impact: what AI earned, what it cost and what it put at risk. Every item carries <em>Ask your leadership team</em> (editor's questions, not claims). A <em>Business lens</em> appears only where we add a reading the source does not state. Data quality section skipped (no qualifying item). <a href="#sec-caution-note" class="pdf-link">Verify before business use.</a></span>
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
              <strong>The significant return is still a forecast.</strong> Of 400 CFOs surveyed, 52% report positive AI returns today but only 10% call them significant; 54% expect significant returns within 24 months. <a href="#sec-lead-results" class="brief-link">›</a>
            </div>
          </div>
          <div class="summary-item-row">
            <div class="summary-num-circle">2</div>
            <div class="summary-text">
              <strong>Two technology suppliers reported fast growth.</strong> AMD Data Center +97% (total revenue +45%); CDW net sales +17.7% with Financial Services +73.2%. Neither release says how much of this is AI. <a href="#sec-lead-results" class="brief-link">›</a>
            </div>
          </div>
          <div class="summary-item-row">
            <div class="summary-num-circle">3</div>
            <div class="summary-text">
              <strong>More agents often cost more and deliver no more.</strong> On benchmark workflows, a preprint reports coordinated agent designs spend 1.4–4.7× the tokens of a single agent for gains “usually small and rarely significant”. <a href="#sec-ai-research" class="brief-link">›</a>
            </div>
          </div>
          <div class="summary-item-row">
            <div class="summary-num-circle">4</div>
            <div class="summary-text">
              <strong>US national bank examiners now have an AI playbook.</strong> The OCC, which supervises national banks, issued a supervisory framework; it says banks are not expected to set separate risk parameters for AI. <a href="#sec-laws-guidance" class="brief-link">›</a>
            </div>
          </div>
          <div class="summary-item-row">
            <div class="summary-num-circle">5</div>
            <div class="summary-text">
              <strong>This week's big rounds funded the layer that runs AI.</strong> Three rounds of $100M+ totalling $1.9B (our sum): inference, revenue agents and petabyte-scale analytics. <a href="#sec-investments" class="brief-link">›</a>
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

        <div class="roles-grid-6" style="margin-top: 6px;">
          <!-- CEO -->
          <div class="role-card">
            <div>
              <div class="role-title">CEO</div>
              <p class="role-desc">49% of 400 surveyed CFOs say their transformation agenda exceeds their organisation's ability to execute.</p>
            </div>
            <a href="#sec-lead-results" class="role-go">›</a>
          </div>

          <!-- CFO -->
          <div class="role-card">
            <div>
              <div class="role-title">CFO</div>
              <p class="role-desc">Among surveyed CFOs whose agenda exceeds capacity, 24% report positive AI returns, against 79% where capacity meets demand. Both self-reported.</p>
            </div>
            <a href="#sec-lead-results" class="role-go">›</a>
          </div>

          <!-- CIO / CTO -->
          <div class="role-card">
            <div>
              <div class="role-title">CIO / CTO</div>
              <p class="role-desc">Preprint: on benchmark tasks, coordinated agent designs run 2.6–5.8× the latency of a single agent.</p>
            </div>
            <a href="#sec-ai-research" class="role-go">›</a>
          </div>

          <!-- CISO / CRO -->
          <div class="role-card">
            <div>
              <div class="role-title">CISO / CRO</div>
              <p class="role-desc">A command-injection flaw in an open-source agent framework was published with a public exploit.</p>
            </div>
            <a href="#sec-vendor-risk" class="role-go">›</a>
          </div>

          <!-- CHRO -->
          <div class="role-card">
            <div>
              <div class="role-title">CHRO</div>
              <p class="role-desc">92% of 595 surveyed US HR professionals say staff could be reskilled for AI roles; the same survey says firms still hire outside more often.</p>
            </div>
            <a href="#sec-workforce-talent" class="role-go">›</a>
          </div>

          <!-- COO -->
          <div class="role-card">
            <div>
              <div class="role-title">COO</div>
              <p class="role-desc">Of 1,100 surveyed financial services firms, 59% are piloting or deploying multi-agent AI; 10% have enterprise-wide orchestration.</p>
            </div>
            <a href="#sec-unsolved-problems" class="role-go">›</a>
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
              <strong>Put a date on the return.</strong> For each AI programme, name the quarter a measured result lands and who signs for it. <a href="#sec-lead-results" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">2</div>
            <div>
              <strong>Test capacity, not just the case.</strong> Rank AI initiatives against delivery capacity before approving the next one. <a href="#sec-lead-results" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">3</div>
            <div>
              <strong>Price the architecture.</strong> Ask for tokens and latency per task, not just accuracy, before approving multi-agent designs. <a href="#sec-ai-research" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">4</div>
            <div>
              <strong>Start simple.</strong> Require a single-agent baseline before any team builds a coordinated one. <a href="#sec-ai-research" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">5</div>
            <div>
              <strong>Inventory agent frameworks.</strong> List the open-source agent software in your stack and in your vendors', with version and owner. <a href="#sec-vendor-risk" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">6</div>
            <div>
              <strong>US national banks: align to the examiner.</strong> Map AI uses in credit, payments, fraud and operations onto your existing risk framework. <a href="#sec-laws-guidance" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">7</div>
            <div>
              <strong>Fix measurement before scaling.</strong> If you cannot show a return on today's agents, do not add more. <a href="#sec-unsolved-problems" class="action-tag-link">›</a>
            </div>
          </div>

          <div class="action-item-card">
            <div class="action-circle-num">8</div>
            <div>
              <strong>Look inside first.</strong> Before hiring for an AI role, ask which current employees could be redeployed into it. <a href="#sec-workforce-talent" class="action-tag-link">›</a>
            </div>
          </div>
        </div>
      </section>

      <!-- Page 1 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 07 · Page 1 of 6</div>
      </footer>
    </article>


    <!-- ==================== PAGE 2 OF 6 ==================== -->
    <article id="page-2" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>2–8 NOV 2026 · PAGE 2 OF 6</span>
      </div>

      <!-- Section: Lead: The ROI Scoreboard -->
      <section id="sec-lead-results">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag">01 GROWTH &amp; REVENUE · P2</span>
            <span>LEAD: THE ROI SCOREBOARD</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <div style="font-size: 10px; font-weight: 800; color: #1e3a5f; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px;">
            CFO SURVEY AND COMPANY RESULTS · 2–4 NOV 2026 · NORTH AMERICA, GLOBAL
          </div>
          <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 15.5px; font-weight: 800; line-height: 1.25; color: #122119; margin-bottom: 6px;">
            Buyers of AI are still waiting for the return; two technology suppliers posted fast growth in the same week — and the survey points at execution capacity
          </h2>
          <p style="font-size: 11.5px; line-height: 1.45; color: #1c2e24; margin-bottom: 6px;">
            RGP surveyed 400 CFOs and equivalent finance leaders at organisations with annual revenue of $250M or more. 52% report positive AI returns today, but just 10% describe them as significant; 54% expect significant positive returns within 24 months. 89% are positive about their organisation's financial outlook for the next 12 months, while 49% say their transformation agenda exceeds their organisation's ability to execute. The split is worth a board discussion: among CFOs whose agenda exceeds capacity, 24% report positive AI returns, against 79% among those whose capacity meets or exceeds demand. Both halves of that comparison are the same respondent's own assessment, so it shows an association, not a cause, and the survey did not ask about technology. Survey conducted September 2026; respondents in North America, Europe and Asia Pacific, per CFO.com. RGP sells transformation and execution services — the capability its survey finds respondents lack. Open: <a href="https://www.cfo.com/news/cfos-expect-ai-to-pay-off-in-2-years-RGP-survey/873512/" target="_blank" rel="noopener noreferrer" class="src-link">CFO.com report</a> · <a href="https://finviz.com/news/414353/rgp-study-89-of-cfos-report-positive-financial-outlook-yet-nearly-half-say-transformation-demands-exceed-capacity" target="_blank" rel="noopener noreferrer" class="src-link">RGP survey release, syndicated copy</a>
          </p>

          <div class="table-wrap">
            <table class="brief-table">
              <thead>
                <tr>
                  <th style="width: 130px;">COMPANY · DATE</th>
                  <th>WHAT IT REPORTED</th>
                  <th>WHAT THE RELEASE ITSELF SAYS ABOUT AI</th>
                  <th style="width: 70px;">SOURCE</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>AMD</strong><br><span style="font-size: 10px; color: #555;">3 Nov · chips</span></td>
                  <td>Q3 revenue $13.4B, up 45%. Data Center segment $8.5B, up 97%. Q4 outlook about $17B, plus or minus 3% (company forecast).</td>
                  <td>The release attributes Data Center growth to demand for its EPYC processors and the launch of its Instinct MI450 Series GPUs. The cautionary statement lists memory supply among its risks. (CFO Jean Hu on the Q4 outlook is quoted on p6.)</td>
                  <td><a href="https://ir.amd.com/news-events/press-releases/detail/1303/amd-reports-third-quarter-2026-financial-results" target="_blank" rel="noopener noreferrer" class="src-link">release</a></td>
                </tr>
                <tr>
                  <td><strong>CDW</strong><br><span style="font-size: 10px; color: #555;">4 Nov · IT reseller</span></td>
                  <td>Q3 net sales $6,754.5M, up 17.7%. Commercial $3,979.4M, up 20.8%, within which Financial Services $571.5M, up 73.2%. Government +9.9%, Education +7.5%, Healthcare +9.3%.</td>
                  <td>CEO Christine A. Leahy cites “strong momentum in enterprise AI adoption” (per company release). The release's risk factors cite supply disruptions, including capacity limits and cost increases, tied to heightened AI-related demand.</td>
                  <td><a href="https://www.sec.gov/Archives/edgar/data/0001402057/000140205726000113/cdw-2026930earningsrelease.htm" target="_blank" rel="noopener noreferrer" class="src-link">release</a></td>
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
                <div class="stat-bar-label" style="width: 230px;">AMD Data Center segment</div>
                <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 100%; background: #1e3a5f;"></div></div>
                <div class="stat-bar-val" style="width: 60px; color: #1e3a5f;">+97%</div>
              </div>
              <div class="stat-bar-item">
                <div class="stat-bar-label" style="width: 230px;">CDW Financial Services</div>
                <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 75.5%; background: #1e3a5f;"></div></div>
                <div class="stat-bar-val" style="width: 60px; color: #1e3a5f;">+73.2%</div>
              </div>
              <div class="stat-bar-item">
                <div class="stat-bar-label" style="width: 230px;">AMD total revenue</div>
                <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 46.4%; background: #1e3a5f;"></div></div>
                <div class="stat-bar-val" style="width: 60px; color: #1e3a5f;">+45%</div>
              </div>
              <div class="stat-bar-item">
                <div class="stat-bar-label" style="width: 230px;">CDW total net sales</div>
                <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 18.2%; background: #1e3a5f;"></div></div>
                <div class="stat-bar-val" style="width: 60px; color: #1e3a5f;">+17.7%</div>
              </div>
            </div>
            <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 3px;">
              Company figures; measures differ (total vs segment, group vs customer channel). Bars scaled to +97%. Neither release quantifies how much of the growth is AI.
            </div>
          </div>

          <!-- Ask Your Leadership Team box -->
          <div class="ask-team-box" style="margin-top: 6px;">
            <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTIONS</div>
            <ul class="lens-questions-list">
              <li>If our board asked today, which AI programme could we show a measured revenue or cost result for?</li>
              <li>Is our AI agenda larger than our ability to deliver it, and which items would we cut to fix that?</li>
              <li>Our suppliers are reporting AI-led growth. Are we the customer funding it, and what are we getting back?</li>
            </ul>
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
                  <th style="width: 110px;">TYPE</th>
                  <th style="width: 210px;">WHAT WAS RELEASED</th>
                  <th>COST, ACCESS AND RISK (FROM THE SOURCE)</th>
                  <th style="width: 130px;">SOURCES</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>4 Nov</strong></td>
                  <td><span class="badge-tag-clean badge-model">MODEL</span></td>
                  <td><strong>Tencent Hy4</strong>, the full version of a model Tencent had previously released in preview, adding visual understanding and computer-use capability, available across Tencent products and third-party platforms.</td>
                  <td>Standard API price unchanged from the Hy4 preview at $0.834 per million input tokens and $2.501 per million output tokens, with a 50% discount on Tencent Cloud TokenHub to 31 December (as reported by TechNode). Tencent says it plans to release model weights and system cards “in the coming days”, with a focus on cybersecurity and biological safety.</td>
                  <td><a href="https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/" target="_blank" rel="noopener noreferrer" class="src-link">Announcement</a> · <a href="https://technode.com/2026/11/04/tencent-launches-hy4-with-vision-and-computer-use-capabilities/" target="_blank" rel="noopener noreferrer" class="src-link">TechNode</a></td>
                </tr>
                <tr>
                  <td><strong>5 Nov</strong></td>
                  <td><span class="badge-tag-clean badge-model">MODEL</span><br><span class="badge-tag-clean badge-restricted">RESTRICTED</span></td>
                  <td><strong>OpenAI GPT-6 Cyber</strong>, a variant of GPT-6 Astra trained for authorised vulnerability research, reached a select group of approved customers in the “Daybreak Red” tier via the API and Codex.</td>
                  <td>No public price; access is gated and OpenAI says it will extend to all Daybreak Red customers in the coming weeks. OpenAI rated the model “Critical” for cybersecurity under its Preparedness Framework, up from “High” for its predecessor, and says it scored 48.5% on its ExploitGym evaluation against 32.1% for GPT-5.6 Cyber. OpenAI also announced a $1bn grant programme to subsidise access for resource-constrained defenders. All figures are OpenAI's own, as reported by the three sources listed.</td>
                  <td><a href="https://thenextweb.com/news/openai-gpt-6-cyber-launch-firefox-linux-daybreak-red" target="_blank" rel="noopener noreferrer" class="src-link">TNW</a> · <a href="https://cybermagazine.com/news/gpt-6-cyber-openais-frontier-of-aligned-security-agents" target="_blank" rel="noopener noreferrer" class="src-link">Cyber Magazine</a> · <a href="https://fortune.com/2026/11/05/openai-debuts-new-cybersecurity-focused-ai-model-amid-growing-alarm-about-ai-driven-cyber-attacks/" target="_blank" rel="noopener noreferrer" class="src-link">Fortune</a></td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 3px;">
            No other model or patch release in the window met this brief's rule that a first-party announcement or official record be identifiable; tracker sites and model catalogues were not used.
          </div>

          <!-- Business Lens & Ask Your Leadership Team pair -->
          <div class="lens-grid-pair">
            <div class="business-lens-box">
              <div class="business-lens-label">BUSINESS LENS · OUR SUMMARY</div>
              Tencent held Hy4's API price at the preview level while adding vision and computer use. OpenAI gated its new security model to vetted customers and raised its own cyber risk rating to Critical.
            </div>
            <div class="ask-team-box">
              <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTIONS</div>
              <ul class="lens-questions-list">
                <li>If capability rises without a price rise, which of our rejected AI cases become viable?</li>
                <li>Who in our organisation would be approved to use a gated offensive-security model, and under whose authority?</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- Page 2 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 07 · Page 2 of 6</div>
      </footer>
    </article>


    <!-- ==================== PAGE 3 OF 6 ==================== -->
    <article id="page-3" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>2–8 NOV 2026 · PAGE 3 OF 6</span>
      </div>

      <!-- Section: AI Research: What Agent Architecture Costs -->
      <section id="sec-ai-research">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag" style="background: #143826;">02 COST &amp; OUTPUT · P3</span>
            <span>AI RESEARCH: WHAT AGENT ARCHITECTURE COSTS</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <div style="font-size: 10px; font-weight: 800; color: #1e3a5f; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px;">
            PREPRINT · 7 NOV 2026 · AGENT COST AND ACCURACY
          </div>
          <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 15.5px; font-weight: 800; line-height: 1.25; color: #122119; margin-bottom: 6px;">
            Preprint: adding agents to an enterprise-style workflow multiplied the cost and rarely improved the result
          </h2>
          <p style="font-size: 11.5px; line-height: 1.45; color: #1c2e24; margin-bottom: 6px;">
            The authors held the model, tasks and tools fixed and varied only the architecture, comparing four designs in eight arms across 13 enterprise-style standard operating procedures — a benchmark built to resemble the long, branching, tool-heavy workflows companies run. They report that every coordinated arm (multi-agent or skill-augmented) spends 1.4–4.7× the tokens and 2.6–5.8× the latency of a single function-calling agent “for gains that are usually small and rarely significant”, making the single agent, in their words, the efficient default. Quality of implementation mattered more than the design choice: a plausible multi-agent build underperformed the single agent, while a targeted redesign was the only arm to beat the baseline significantly, at 75.6% task success against 67.4% — though the authors also report that no architecture is statistically separable in aggregate, and that added structure only “plausibly” pays off on the most complex procedures, which they call a directional and not yet significant trend. Their stated conclusions are that no architecture is universally best — the right choice depends on the procedure — and that added architectural cost has to be earned by a gain in task success. Authors' own measurements; not peer reviewed. The paper does not name the model held fixed across the arms, so the multiples describe that one setup rather than a general rule.
          </p>
          <div style="font-size: 10.5px; color: #444; margin-bottom: 6px;">
            Nandi S, Arora H, Bai Y, Patel U, Shah C, Kwon H, Zhang W, Chen W, Li CR, Sconfienza A, Goyal A, Lee Y, Xiong M, Ramachandra P. “Agent Architecture Cost-Success Trade-offs: A Controlled Evaluation across Enterprise-Style SOPs.” arXiv preprint v1, 7 Nov 2026. <a href="https://arxiv.org/abs/2611.12953" target="_blank" rel="noopener noreferrer" class="src-link">arxiv.org/abs/2611.12953</a> · DOI 10.48550/arXiv.2611.12953 (arXiv-issued)
          </div>

          <div class="stat-bar-card-clean" style="margin-top: 4px;">
            <div class="stat-bar-title-clean">
              COORDINATED AGENT ARMS vs A SINGLE AGENT (RANGE REPORTED)
            </div>
            <div style="display: flex; flex-direction: column; gap: 4px;">
              <div class="stat-bar-item">
                <div class="stat-bar-label" style="width: 220px;">Token cost</div>
                <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 100%; background: #b45309;"></div></div>
                <div class="stat-bar-val" style="width: 70px; color: #b45309;">1.4–4.7×</div>
              </div>
              <div class="stat-bar-item">
                <div class="stat-bar-label" style="width: 220px;">Latency</div>
                <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 100%; background: #b45309;"></div></div>
                <div class="stat-bar-val" style="width: 70px; color: #b45309;">2.6–5.8×</div>
              </div>
              <div class="stat-bar-item">
                <div class="stat-bar-label" style="width: 220px;">Task success, baseline</div>
                <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 89.1%; background: #2d5a3f;"></div></div>
                <div class="stat-bar-val" style="width: 70px; color: #2d5a3f;">67.4%</div>
              </div>
              <div class="stat-bar-item">
                <div class="stat-bar-label" style="width: 220px;">Task success, best arm</div>
                <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 100%; background: #2d5a3f;"></div></div>
                <div class="stat-bar-val" style="width: 70px; color: #2d5a3f;">75.6%</div>
              </div>
            </div>
            <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 3px;">
              Figures as reported by the authors across 13 enterprise SOPs. Cost and latency bars are scaled to the top of each reported range; success bars are scaled to 75.6%. Cost and success are different measures and are not comparable to each other.
            </div>
          </div>

          <!-- Ask Your Leadership Team box -->
          <div class="ask-team-box" style="margin-top: 6px;">
            <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTIONS</div>
            <ul class="lens-questions-list">
              <li>Do we know the cost per completed task of our agents, or only their accuracy?</li>
              <li>Did anyone compare our multi-agent build against a single-agent baseline before we funded it?</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Section: Vendor & Security Risk -->
      <section id="sec-vendor-risk" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag risk">03 RISK &amp; COMPLIANCE · P3</span>
            <span>VENDOR &amp; SECURITY RISK</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <div style="font-size: 10px; font-weight: 800; color: #7f1d1d; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px;">
            OPEN-SOURCE AGENT FRAMEWORK · CVE RECORD PUBLISHED 5 NOV 2026 · GLOBAL
          </div>
          <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 15.5px; font-weight: 800; line-height: 1.25; color: #122119; margin-bottom: 6px;">
            A command-injection flaw in an open-source agent framework was published with a working exploit already public
          </h2>
          <p style="font-size: 11.5px; line-height: 1.45; color: #1c2e24; margin-bottom: 4px;">
            The national vulnerability record for CVE-2026-123022, published 5 November 2026, describes a flaw in AgentScope up to version 2.0.11. The affected element is the subprocess.Popen function in the framework's MCP Workspace API: manipulating the command argument results in OS command injection, and the record states that the attack may be launched remotely, adding that “The exploit is now public and may be used.” The record carries a CVSS v3.1 score of 7.3, assigned as a secondary metric by a third-party numbering authority rather than the project. The record says nothing about how widely the package is deployed, and we found no reliable figure for it. Our view: the point for a board is the category, not this package — agent frameworks and their connectors are ordinary supply-chain software, installed by teams and by vendors.
          </p>
          <div style="font-size: 11px; color: #444; margin-bottom: 6px;">
            Source: NVD record for CVE-2026-123022, published 5 Nov 2026 — <a href="https://nvd.nist.gov/vuln/detail/CVE-2026-123022" target="_blank" rel="noopener noreferrer" class="src-link">open the record</a>.
          </div>

          <div class="ask-team-box">
            <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTIONS</div>
            <ul class="lens-questions-list">
              <li>Which open-source agent frameworks and connectors run inside our estate, and who patches them?</li>
              <li>Do our AI vendors tell us when a component they embed has a published exploit?</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Section: Operating Models: AI in Industrial Sectors -->
      <section id="sec-operating-models" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE &amp; ACTION · P3</span>
            <span>OPERATING MODELS: AI IN INDUSTRIAL SECTORS</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <div style="font-size: 10px; font-weight: 800; color: #143826; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px;">
            INSURANCE · UNITED STATES · REPORTED 6 NOV 2026 · EARNINGS CALL REMARKS
          </div>
          <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 15.5px; font-weight: 800; line-height: 1.25; color: #122119; margin-bottom: 6px;">
            An insurer says it plans to do business with its customers' AI agents, not only with its customers
          </h2>
          <p style="font-size: 11.5px; line-height: 1.45; color: #1c2e24; margin-bottom: 4px;">
            As reported by CIO Dive, Allstate chief executive Tom Wilson told investors on the company's third-quarter earnings call that personal AI assistants give the insurer an opportunity to serve customers who prefer machines to handle transactions, and that Allstate's goal is to work with those outside agents rather than against them, showing customers branded products as they interact. He said the rollout of the company's own agentic platform, introduced earlier this year to handle agent-to-agent processing, is accelerating. Executives' statements on an earnings call, as reported; not measured results.
          </p>
          <div style="font-size: 11px; color: #444; margin-bottom: 6px;">
            Source: <a href="https://www.ciodive.com/news/insurers-race-capture-value-agentic-ai/874047" target="_blank" rel="noopener noreferrer" class="src-link">CIO Dive</a>, 6 Nov 2026, reporting the Q3 2026 earnings call. Company statements of intent.
          </div>

          <div class="ask-team-box">
            <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTION</div>
            <ul class="lens-questions-list">
              <li>If a customer's AI agent came to buy from us tomorrow, could our systems and terms transact with it?</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Page 3 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 07 · Page 3 of 6</div>
      </footer>
    </article>


    <!-- ==================== PAGE 4 OF 6 ==================== -->
    <article id="page-4" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>2–8 NOV 2026 · PAGE 4 OF 6</span>
      </div>

      <!-- Section: Laws, Rules & Guidance -->
      <section id="sec-laws-guidance">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag risk">03 RISK &amp; COMPLIANCE · P4</span>
            <span>LAWS, RULES &amp; GUIDANCE</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <div style="font-size: 10px; font-weight: 800; color: #7f1d1d; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px;">
            UNITED STATES · 4 NOV 2026 · SUPERVISORY FRAMEWORK, NOT A RULE
          </div>
          <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 15.5px; font-weight: 800; line-height: 1.25; color: #122119; margin-bottom: 6px;">
            US bank regulator issues its first AI framework for examiners — and declines to treat AI as a risk apart
          </h2>
          <p style="font-size: 11.5px; line-height: 1.45; color: #1c2e24; margin-bottom: 4px;">
            The Office of the Comptroller of the Currency, which supervises national banks and federal savings associations, issued Bulletin 2026-54 and a supervisory framework for examiners evaluating banks' use of AI. Note the terminology before searching for it: the document calls the technology “super intelligence”, or SI. Examiners will apply it to SI in normal-course activities including credit decisioning, payments, fraud detection, customer service, operations, risk management and market activities, with particular attention to generative and agentic systems; it sets out 16 supervisory components across six pillars and is described as a living document. Two points matter for a board. Examiners are told not to treat SI as a separate and distinct risk category, and banks need not define a separate SI risk appetite — SI risk belongs inside existing operational, compliance and credit frameworks. And scrutiny follows what a system is permitted to do and the consequences if it fails, not how sophisticated the model is. Status: the framework sets no new supervisory expectations or enforceable standards; Reuters notes it is not legally binding in the way a rule is, though banks typically comply closely with such guidance.
          </p>
          <div style="font-size: 11px; color: #444; margin-bottom: 6px;">
            Sources: <a href="https://www.occ.gov/news-issuances/news-releases/2026/nr-occ-2026-97a.pdf" target="_blank" rel="noopener noreferrer" class="src-link">OCC Bulletin 2026-54 and news release NR 2026-97</a>, 4 Nov 2026 · <a href="https://bankingjournal.aba.com/2026/11/occ-releases-framework-for-supervising-artificial-intelligence/" target="_blank" rel="noopener noreferrer" class="src-link">ABA Banking Journal</a> · <a href="https://srnnews.com/us-bank-regulator-issues-first-ever-ai-guidance-for-examiners/" target="_blank" rel="noopener noreferrer" class="src-link">Reuters (Pete Schroeder)</a> · <a href="https://www.reedsmith.com/articles/occ-issues-supervisory-framework-on-use-of-ai/" target="_blank" rel="noopener noreferrer" class="src-link">Reed Smith analysis</a>
          </div>

          <div class="ask-team-box">
            <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTION</div>
            <ul class="lens-questions-list">
              <li>If an examiner asked tomorrow, could we show where each AI use sits inside our existing risk framework — not beside it?</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Section: Unsolved Problems in AI -->
      <section id="sec-unsolved-problems" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag risk">03 RISK &amp; COMPLIANCE · P4</span>
            <span>UNSOLVED PROBLEMS IN AI</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 6px;">
          <div style="font-size: 10px; font-weight: 800; color: #7f1d1d; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px;">
            INDUSTRY RESEARCH · 5 NOV 2026 · PARIS · FINANCIAL SERVICES
          </div>
          <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 15.5px; font-weight: 800; line-height: 1.25; color: #122119; margin-bottom: 6px;">
            Still unsolved: proving that agentic AI paid for itself
          </h2>
          <p style="font-size: 11.5px; line-height: 1.45; color: #1c2e24; margin-bottom: 4px;">
            The Capgemini Research Institute's World Cloud Report for Financial Services 2027, published 5 November, draws on a survey of 1,100 financial services leaders across 14 markets, fielded June to July 2026, in seven sectors from retail banking to health insurance. It reports that 59% of firms are piloting or deploying multi-agent AI systems, yet only 10% have achieved enterprise-wide orchestration and only 5% have institutionalised the capabilities to run agentic AI at enterprise scale. Roughly half of firms cannot consistently demonstrate a return on agentic AI initiatives. On cost, 90% are using or planning to implement intelligent model routing to optimise performance and manage token costs, and 52% are turning to hyperscalers as their preferred cloud partner to govern multi-agent deployments. The release ties the gap to measurement rather than ambition: firms lack clear frameworks for judging whether initiatives deliver enough value to justify continued investment. It reports eight in ten executives prioritising reduction of technical debt, calls a modernised tech stack a prerequisite for the agentic era, and projects that executives making outcomes their primary AI-funding criterion will rise 141% by 2028 while those focused on efficiency fall 42%. (Ravi Khokhar, Capgemini's Global Head of Cloud for Financial Services, is quoted on p6.)
          </p>
          <div style="font-size: 10.5px; color: #444; margin-bottom: 6px;">
            Source: <a href="https://www.capgemini.com/us-en/news/press-releases/financial-institutions-accelerate-transition-to-multi-agent-ai-in-drive-for-bottom-line-value/" target="_blank" rel="noopener noreferrer" class="src-link">Capgemini press release and</a> <a href="https://www.capgemini.com/us-en/news/press-releases/financial-institutions-accelerate-transition-to-multi-agent-ai-in-drive-for-bottom-line-value/" target="_blank" rel="noopener noreferrer" class="src-link">World Cloud Report for Financial Services 2027</a>, 5 Nov 2026. Survey figures are the publisher's own; projections to 2028 are the report's forecast. Capgemini sells cloud and AI services of the kind the report finds firms need.
          </div>

          <div class="ask-team-box">
            <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTIONS</div>
            <ul class="lens-questions-list">
              <li>Do we have one agreed way of measuring what an agent delivered, or does every unit use its own?</li>
              <li>Are we routing work to the cheapest model that is accurate enough, and can we show the saving?</li>
            </ul>
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

        <div style="margin-top: 6px;">
          <div style="font-size: 10px; font-weight: 800; color: #1e3a5f; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px;">
            UNITED STATES · WYOMING · 5 NOV 2026 · COMPANY ANNOUNCEMENT
          </div>
          <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 15.5px; font-weight: 800; line-height: 1.25; color: #122119; margin-bottom: 6px;">
            Google puts $17 billion behind a first data centre in Wyoming, with the power contracted alongside it
          </h2>
          <p style="font-size: 11.5px; line-height: 1.45; color: #1c2e24; margin-bottom: 4px;">
            In a post by Steve Walter, vice president of global infrastructure and energy, Google said it is building its first data centre in Wyoming, sited in Laramie County and “making a long-term, $17 billion investment in the Cowboy State”. The design is air-cooled, which the company ties to limiting demands on local water. The power is contracted rather than self-built: the project is contracted with AEP for a commercial-scale 702-megawatt fuel-cell development, with the cells made by Bloom Energy, while gas generators run by Tallgrass Energy and Black Hills Energy also supply power. Carbon capture sits with that gas generation, not the fuel cells — Tallgrass is developing a nearby sequestration hub. The announcement gives no construction schedule, and the 702 MW figure is a power figure, not the data centre's capacity. For buyers of compute, the detail to note is the structure rather than the headline number: this announcement pairs the capacity with the power arrangements meant to run it.
          </p>
          <div style="font-size: 10.5px; color: #444; margin-bottom: 6px;">
            Source: <a href="https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/wyoming-data-center/" target="_blank" rel="noopener noreferrer" class="src-link">Google blog post</a>, 5 Nov 2026. Company plans; not measured output. Our summary: here, capacity and power are announced together.
          </div>

          <div class="ask-team-box">
            <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTION</div>
            <ul class="lens-questions-list">
              <li>Do our cloud and AI contracts give us a price and a capacity commitment, or only access?</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Page 4 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 07 · Page 4 of 6</div>
      </footer>
    </article>


    <!-- ==================== PAGE 5 OF 6 ==================== -->
    <article id="page-5" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>2–8 NOV 2026 · PAGE 5 OF 6</span>
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

        <div style="margin-top: 6px;">
          <div class="table-wrap">
            <table class="brief-table">
              <thead>
                <tr>
                  <th style="width: 80px;">COMPANY</th>
                  <th style="width: 75px;">AMOUNT</th>
                  <th style="width: 200px;">STRUCTURE · LEAD(S)</th>
                  <th>BUSINESS PROBLEM IT TARGETS</th>
                  <th style="width: 130px;">CONFIRMED BY</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>fal</strong></td>
                  <td><strong>$1.3B</strong></td>
                  <td>Series F · Bessemer Venture Partners, with Nvidia, Sound Ventures, HOF Capital and T. Rowe Price. Announced alongside a previously closed $350M Series E led by Sequoia Capital; the two rounds total $1.65B.</td>
                  <td>Running generative image, video and audio models for developers and businesses — the inference layer rather than the model itself</td>
                  <td><a href="https://www.bvp.com/news/investing-in-fal-the-generative-media-company" target="_blank" rel="noopener noreferrer" class="src-link">Bessemer announcement</a> · <a href="https://tech.eu/2026/11/04/fal-doubles-valuation-to-16b-after-13b-series-f/" target="_blank" rel="noopener noreferrer" class="src-link">Tech.eu</a>, 3 Nov 2026</td>
                </tr>
                <tr>
                  <td><strong>Nooks</strong></td>
                  <td><strong>$500M</strong></td>
                  <td>Growth capital commitment from General Catalyst's Customer Value Fund. Not an equity round: the fund takes a share of the returns the money generates rather than a stake.</td>
                  <td>AI agents for sales teams; announced with a sales assistant product</td>
                  <td><a href="https://www.prnewswire.com/news-releases/nooks-secures-500-million-from-general-catalyst-and-launches-node-the-first-ai-personal-assistant-for-sales-302928795.html" target="_blank" rel="noopener noreferrer" class="src-link">Company release</a>, 4 Nov 2026</td>
                </tr>
                <tr>
                  <td><strong>Ocient</strong></td>
                  <td><strong>$100M</strong></td>
                  <td>Series C · co-led by BOKA Capital and OCA Ventures. The company says the round takes its total raised to $260M.</td>
                  <td>Analytics on petabyte-scale data for AI agents and human analysts; the company says it expects revenue to more than triple in 2026</td>
                  <td><a href="https://www.blocksandfiles.com/ai-ml/2026/11/05/ai-energized-trillion-row-database-startup-ocient-raises-100-million/5307819" target="_blank" rel="noopener noreferrer" class="src-link">Blocks &amp; Files</a>, 5 Nov 2026</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 3px;">
            Only rounds of $100M or more announced 2–8 Nov 2026. Amounts and leads come from each company's announcement or its lead investor's; where a company's own post was unavailable, a bylined report quoting it is linked instead. Total $1.9B is our sum of the three announced amounts, and the “business problem” column is our short description. The Nooks figure is a financing commitment, not an equity raise, and is not comparable to the other two. No valuations.
          </div>

          <!-- Business Lens & Ask Your Leadership Team pair -->
          <div class="lens-grid-pair">
            <div class="business-lens-box">
              <div class="business-lens-label">BUSINESS LENS · OUR SUMMARY</div>
              All three fund the layer between the model and the business outcome: running models, acting on customers, and querying the data. None of the three is a model maker.
            </div>
            <div class="ask-team-box">
              <div class="ask-team-label">ASK YOUR LEADERSHIP TEAM · EDITOR'S QUESTIONS</div>
              <ul class="lens-questions-list">
                <li>In inference, agents and analytics, are we buying, building or waiting — and is that choice written down?</li>
                <li>Would we accept growth capital priced on a share of returns rather than equity?</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- Section: Workforce & Talent -->
      <section id="sec-workforce-talent" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE &amp; ACTION · P5</span>
            <span>WORKFORCE &amp; TALENT</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div class="two-col-equal" style="margin-top: 6px;">
          <!-- Left Col: Text & Summary -->
          <div>
            <div style="font-size: 10px; font-weight: 800; color: #143826; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px;">
              UNITED STATES · 4 NOV 2026 · PUBLISHED RESEARCH
            </div>
            <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 14.5px; font-weight: 800; line-height: 1.25; color: #122119; margin-bottom: 4px;">
              Employers believe their own staff could do the AI jobs — and hire outside anyway
            </h2>
            <p style="font-size: 11px; line-height: 1.45; color: #1c2e24; margin-bottom: 4px;">
              New research published by Careerminds reports that 92% of US HR professionals and 88% of US people managers believe employees within their organisations could be reskilled for AI-related roles, yet organisations are more likely to hire externally than redeploy workers already on the payroll. The white paper is titled <em>The AI Redeployment Gap: What Companies Lose by Hiring over Reskilling</em>. Survey of 595 US HR professionals and 547 US people managers, aged 25–65, at organisations with 500 to 10,000 or more employees, conducted 15–26 May 2026 with Censuswide.
            </p>
            <div style="font-size: 10px; color: #444;">
              Source: <a href="https://www.prnewswire.com/news-releases/new-research-92-of-hr-professionals-believe-employees-can-be-reskilled-for-ai-jobs-yet-external-hiring-outpaces-redeployment-302927992.html" target="_blank" rel="noopener noreferrer" class="src-link">Careerminds announcement</a>, 4 Nov 2026. Publisher's own survey; Careerminds sells reskilling and outplacement services — the course the survey recommends.
            </div>
          </div>

          <!-- Right Col: Stat Bars & Ask Team -->
          <div>
            <div class="stat-bar-card-clean">
              <div class="stat-bar-title-clean">
                BELIEF THAT EXISTING STAFF COULD BE RESKILLED FOR AI ROLES
              </div>
              <div style="display: flex; flex-direction: column; gap: 4px;">
                <div class="stat-bar-item">
                  <div class="stat-bar-label" style="width: 140px;">HR professionals</div>
                  <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 92%; background: #2d5a3f;"></div></div>
                  <div class="stat-bar-val" style="width: 45px; color: #2d5a3f;">92%</div>
                </div>
                <div class="stat-bar-item">
                  <div class="stat-bar-label" style="width: 140px;">People managers</div>
                  <div class="stat-bar-track"><div class="stat-bar-fill" style="width: 88%; background: #2d5a3f;"></div></div>
                  <div class="stat-bar-val" style="width: 45px; color: #2d5a3f;">88%</div>
                </div>
              </div>
              <div style="font-size: 9px; color: #64748b; font-style: italic; margin-top: 3px;">
                Self-reported belief, not a measure of redeployment actually carried out. The same research reports that external hiring still outpaces redeployment.
              </div>
            </div>

            <div class="ask-team-box" style="margin-top: 6px;">
              <div class="ask-team-label">ASK YOUR TEAM · EDITOR'S QUESTION</div>
              <ul class="lens-questions-list">
                <li>For the last three AI roles we filled from outside, which internal candidates were considered?</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- Section: Regional Index -->
      <section id="sec-regional-index" style="margin-top: 8px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag money">04 CAPITAL &amp; MARKETS · P5</span>
            <span>REGIONAL INDEX</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div style="margin-top: 4px;">
          <table class="regional-index-table">
            <tbody>
              <tr>
                <td style="width: 110px; font-weight: 700; color: #1e3a5f;">North America</td>
                <td>AMD and CDW results · OCC supervisory framework for examiners · Google's Wyoming data centre · fal, Nooks and Ocient rounds · Allstate on customers' AI agents</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #1e3a5f;">Europe &amp; UK</td>
                <td>Capgemini Research Institute's World Cloud Report for Financial Services 2027 (Paris)</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #1e3a5f;">China</td>
                <td>Tencent Hy4, with vision and computer use, at the preview's API price</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #64748b;">India</td>
                <td style="color: #64748b; font-style: italic;">No qualifying item this week — the Global row below carries items that apply in every market.</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #64748b;">Japan</td>
                <td style="color: #64748b; font-style: italic;">No qualifying item this week — the Global row below carries items that apply in every market.</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #64748b;">Australia</td>
                <td style="color: #64748b; font-style: italic;">No qualifying item this week — the Global row below carries items that apply in every market.</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #1e3a5f;">Global</td>
                <td>OpenAI's gated security model · agent architecture cost preprint · agent-framework vulnerability record · US reskilling research</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Page 5 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 07 · Page 5 of 6</div>
      </footer>
    </article>


    <!-- ==================== PAGE 6 OF 6 ==================== -->
    <article id="page-6" class="page-sheet">
      <!-- Top Running Header -->
      <div class="issue-top-header">
        <span>The AI Leadership Brief</span>
        <span>2–8 NOV 2026 · PAGE 6 OF 6</span>
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
                “…accelerating revenue and earnings growth, driven by strong demand across our Data Center portfolio.”
              </div>
              <div class="quote-src-p5">
                Jean Hu, EVP, CFO and Treasurer, AMD · per company release, 3 Nov 2026 · <a href="https://ir.amd.com/news-events/press-releases/detail/1303/amd-reports-third-quarter-2026-financial-results" target="_blank" rel="noopener noreferrer" class="src-link">release</a>
              </div>
            </div>

            <div class="quote-box-p5">
              <div class="quote-text-p5">
                “Yet adoption alone does not create value”
              </div>
              <div class="quote-src-p5">
                Ravi Khokhar, Global Head of Cloud for Financial Services, Capgemini · per company release, Paris, 5 Nov 2026 · <a href="https://www.capgemini.com/us-en/news/press-releases/financial-institutions-accelerate-transition-to-multi-agent-ai-in-drive-for-bottom-line-value/" target="_blank" rel="noopener noreferrer" class="src-link">release</a>
              </div>
            </div>

            <div class="quote-box-p5">
              <div class="quote-text-p5">
                “The 24-month AI promise is now on the record…”
              </div>
              <div class="quote-src-p5">
                RGP, in its CFO Perspectives report · as quoted by <a href="https://www.cfo.com/news/cfos-expect-ai-to-pay-off-in-2-years-RGP-survey/873512/" target="_blank" rel="noopener noreferrer" class="src-link">CFO.com</a>, 3 Nov 2026
              </div>
            </div>

            <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 2px;">
              Quotes come from company announcements and, where marked, from a bylined report quoting the source. CDW's CEO is quoted in the lead (p2).
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
                <div class="stat-val-p5">10%</div>
                <div class="stat-desc-p5">of 400 CFOs call their AI returns significant today (survey)</div>
              </div>
              <a href="#sec-lead-results" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
            </div>

            <div class="stat-card-p5">
              <div>
                <div class="stat-val-p5">54%</div>
                <div class="stat-desc-p5">expect significant AI returns within 24 months (survey)</div>
              </div>
              <a href="#sec-lead-results" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
            </div>

            <div class="stat-card-p5">
              <div>
                <div class="stat-val-p5">+73.2%</div>
                <div class="stat-desc-p5">CDW Financial Services net sales, Q3 year on year (company)</div>
              </div>
              <a href="#sec-lead-results" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
            </div>

            <div class="stat-card-p5">
              <div>
                <div class="stat-val-p5">+97%</div>
                <div class="stat-desc-p5">AMD Data Center segment revenue, Q3 year on year (company)</div>
              </div>
              <a href="#sec-lead-results" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
            </div>

            <div class="stat-card-p5">
              <div>
                <div class="stat-val-p5">4.7×</div>
                <div class="stat-desc-p5">top of the token-cost range for coordinated agents vs one agent (preprint)</div>
              </div>
              <a href="#sec-ai-research" class="pdf-jump" style="font-size: 9.5px; align-self: flex-end;">›</a>
            </div>

            <div class="stat-card-p5">
              <div>
                <div class="stat-val-p5">$1.9B</div>
                <div class="stat-desc-p5">across three rounds of $100M+ (our sum of announced amounts)</div>
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
            <div style="font-size: 10px; color: #64748b; font-style: italic;">Same week in 2025: 2–8 Nov 2025.</div>
            <div class="history-item-p5">
              <div>
                <span class="history-date-p5">3 Nov 2025:</span> AWS and OpenAI announced a multi-year strategic partnership; OpenAI's post described a $38 billion agreement with continued growth over seven years, giving it access to AWS compute comprising hundreds of thousands of NVIDIA GPUs.
              </div>
              <div class="history-src-p5">
                OpenAI: “AWS and OpenAI announce multi-year strategic partnership”, 3 Nov 2025. <a href="https://openai.com/index/aws-and-openai-partnership/" target="_blank" rel="noopener noreferrer" class="src-link">Open original</a>
              </div>
            </div>

            <div class="history-item-p5">
              <div>
                <span class="history-date-p5">6 Nov 2025:</span> Microsoft AI announced the MAI Superintelligence Team, led by Mustafa Suleyman, to pursue what his post called “humanist superintelligence”; the post named medical superintelligence as an area already showing progress.
              </div>
              <div class="history-src-p5">
                Mustafa Suleyman, Microsoft AI: “Towards Humanist Superintelligence”, 6 Nov 2025. <a href="https://microsoft.ai/blog/towards-humanist-superintelligence" target="_blank" rel="noopener noreferrer" class="src-link">Open original</a>
              </div>
            </div>

            <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 2px;">
              A third item considered for this slot was dropped: its only available sources were republished copies.
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
              <div class="event-dates-p5">8–10 Dec 2026</div>
              <div><strong>Expand North Star 2026</strong> (startup and investor event) · Dubai, UAE</div>
            </div>

            <div class="event-item-p5">
              <div class="event-dates-p5">6–9 Jan 2027</div>
              <div><strong>CES 2027</strong> (consumer and enterprise technology) · Las Vegas, United States</div>
            </div>

            <div class="event-item-p5">
              <div class="event-dates-p5">31 Jan–3 Feb 2027</div>
              <div><strong>Web Summit Qatar 2027</strong> · Doha, Qatar</div>
            </div>

            <div style="font-size: 9.5px; color: #64748b; font-style: italic; margin-top: 2px;">
              Dates come from <a href="https://neuronfeed.com/conferences?topic=AI" target="_blank" rel="noopener noreferrer" class="src-link">one public conference listing</a>; so treat the dates as indicative and confirm with the organiser before booking. None of these events was listed in Edition 06, and all begin after publication.
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
            <strong>VERIFY BEFORE BUSINESS USE</strong><br>
            This brief summarises the public sources linked beside each item. Forecasts, plans, preliminary results, survey findings and makers' claims are the sources' own. Business lens blocks appear only where we add a reading the source does not state, and are marked “Our summary”; Ask your leadership team lines are the editor's questions, not facts or advice. Headlines, summaries, role tips and leadership actions are the editor's wording. Survey percentages are the publishers' own and are not independently verified; several publishers sell services in the areas they surveyed. Verify any item, figure or quote independently against the original source before using it for business decisions. Every source is linked: tap a source name to open the original. <a href="#agenda" class="jump-agenda-btn" style="display: inline-block; margin-left: 6px;">↑ Agenda</a>
          </p>
          <p>
            Found this useful? Give it a 👍 on LinkedIn and share it with a colleague.
          </p>
          <p style="font-style: italic; color: #4b5850;">
            AI model makers are named. No company in this issue is anonymised; the vulnerability item names a software package, as the official record does. Every item links to its source.
          </p>
        </div>
      </section>

      <!-- Page 6 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a> · By Jayaraman (Jay) Ganapathi, People Prime Worldwide</div>
        <div class="page-footer-right">Edition 07 · Page 6 of 6</div>
      </footer>
    </article>

  </main>

  """ + tracking_script + """
</body>
</html>
"""

full_html = head_html + "\n" + body_html
with open('ai-newsletter-issue-07.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Generated ai-newsletter-issue-07.html successfully! Size:", len(full_html))

