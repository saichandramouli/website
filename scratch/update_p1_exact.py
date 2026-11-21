import re

with open('ai-newsletter-issue-08.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's replace the extra CSS to add exact Page 1 styles matching the PDF layout
page1_exact_css = """
    /* ===================================================
       PAGE 1 EXACT PDF ALIGNMENT (EDITION 08)
       =================================================== */
    .p1-top-row {
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 16px;
      margin-top: 6px;
      margin-bottom: 12px;
      align-items: stretch;
    }
    .p1-cartoon-col {
      display: flex;
      flex-direction: column;
    }
    .p1-cartoon-frame {
      background: #fffdfa;
      border: 1px solid #dcd7ca;
      border-radius: 3px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0;
      margin-bottom: 8px;
    }
    .p1-cartoon-frame img {
      width: 100%;
      height: auto;
      display: block;
      object-fit: contain;
    }
    .p1-behind-cartoon {
      font-size: 10.5px;
      line-height: 1.45;
      color: #1e293b;
    }
    .p1-summary-col {
      display: flex;
      flex-direction: column;
    }
    .p1-summary-header {
      font-size: 9.5px;
      font-weight: 800;
      letter-spacing: 0.6px;
      text-transform: uppercase;
      color: #0f172a;
      margin-bottom: 6px;
      padding-top: 2px;
    }
    .p1-summary-list {
      display: flex;
      flex-direction: column;
      gap: 7px;
    }
    .p1-summary-item {
      display: flex;
      align-items: flex-start;
      gap: 8px;
      font-size: 11px;
      line-height: 1.4;
      color: #1e293b;
    }
    .p1-summary-num {
      width: 18px;
      height: 18px;
      min-width: 18px;
      background: #991b1b;
      color: #ffffff;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 10px;
      font-weight: 700;
      margin-top: 1px;
    }
    .p1-summary-text {
      flex: 1;
    }

    /* P1 AGENDA */
    .p1-agenda-box {
      background: #0f243a;
      color: #ffffff;
      padding: 10px 14px 12px 14px;
      border-radius: 3px;
      margin-top: 8px;
      margin-bottom: 8px;
    }
    .p1-agenda-top {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      border-bottom: 1px solid rgba(255, 255, 255, 0.15);
      padding-bottom: 6px;
      margin-bottom: 8px;
    }
    .p1-agenda-top-left {
      display: flex;
      align-items: baseline;
      gap: 12px;
    }
    .p1-agenda-title {
      font-family: 'Inter', sans-serif;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 1px;
      color: #ffffff;
    }
    .p1-agenda-tagline {
      font-size: 9.5px;
      font-weight: 600;
      letter-spacing: 0.6px;
      color: #93c5fd;
    }
    .p1-agenda-hint {
      font-size: 10px;
      color: #cbd5e1;
    }
    .p1-agenda-hint a {
      color: #93c5fd;
      text-decoration: underline;
    }
    .p1-agenda-columns {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 10px;
    }
    .p1-agenda-col {
      display: flex;
      flex-direction: column;
    }
    .p1-agenda-num {
      font-size: 9.5px;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      margin-bottom: 2px;
    }
    .p1-agenda-col:nth-child(1) .p1-agenda-num { color: #60a5fa; }
    .p1-agenda-col:nth-child(2) .p1-agenda-num { color: #4ade80; }
    .p1-agenda-col:nth-child(3) .p1-agenda-num { color: #f87171; }
    .p1-agenda-col:nth-child(4) .p1-agenda-num { color: #fbbf24; }
    .p1-agenda-col:nth-child(5) .p1-agenda-num { color: #e879f9; }

    .p1-agenda-question {
      font-size: 10px;
      color: #94a3b8;
      line-height: 1.25;
      margin-bottom: 6px;
      min-height: 24px;
    }
    .p1-agenda-links-list {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .p1-agenda-links-list li a {
      color: #ffffff;
      text-decoration: none;
      font-size: 10px;
      line-height: 1.3;
      display: block;
      transition: color 0.15s ease;
    }
    .p1-agenda-links-list li a:hover {
      color: #93c5fd;
      text-decoration: underline;
    }
    .p1-agenda-notice {
      border-top: 1px solid rgba(255, 255, 255, 0.12);
      padding-top: 6px;
      margin-top: 8px;
      font-size: 9.5px;
      line-height: 1.35;
      color: #94a3b8;
    }
    .p1-agenda-notice a {
      color: #93c5fd;
      text-decoration: underline;
    }

    /* P1 ROLES GRID (6 BOXES) */
    .p1-roles-grid {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 8px;
      margin-top: 6px;
      margin-bottom: 10px;
    }
    .p1-role-box {
      background: #fffdfa;
      border: 1px solid #dcd7ca;
      border-radius: 3px;
      padding: 7px 6px 8px 6px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 110px;
    }
    .p1-role-title {
      font-size: 10px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      margin-bottom: 4px;
    }
    .p1-role-text {
      font-size: 10px;
      line-height: 1.35;
      color: #334155;
      margin: 0;
    }

    /* P1 ACTIONS (8 PLAIN NUMBERED ITEMS IN 2 COLUMNS) */
    .p1-actions-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      column-gap: 24px;
      row-gap: 8px;
      margin-top: 8px;
      margin-bottom: 12px;
    }
    .p1-action-row {
      font-size: 10.5px;
      line-height: 1.45;
      color: #1e293b;
    }
    .p1-action-row strong {
      color: #0f172a;
    }

    @media (max-width: 768px) {
      .p1-top-row {
        grid-template-columns: 1fr;
      }
      .p1-agenda-columns {
        grid-template-columns: 1fr 1fr;
      }
      .p1-roles-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .p1-actions-grid {
        grid-template-columns: 1fr;
      }
    }
"""

html = html.replace('</style>', page1_exact_css + '\n  </style>')

# Now let's craft the exact Page 1 HTML
page1_exact_html = """    <!-- ==================== PAGE 1 OF 7 ==================== -->
    <article id="page-1" class="page-sheet">
      <!-- Issue Top Running Header -->
      <div class="issue-top-header">
        <span>W E E K L Y · E D I T I O N 0 8</span>
        <span>9 – 1 5 N O V 2 0 2 6 · P A G E 1 O F 7</span>
      </div>

      <!-- Masthead -->
      <div class="issue-title-block">
        <h1 class="masthead-title">The AI Leadership Brief</h1>
        <p class="masthead-subtitle">Edition 08 · 9–15 Nov 2026 · By Jayaraman (Jay) Ganapathi, People Prime Worldwide · For CXOs and senior leaders</p>
      </div>

      <!-- Section Banner: CARTOON & TOP NEWS -->
      <div class="section-banner" style="margin-top: 6px;">
        <div class="section-banner-title">
          <span class="banner-theme-tag">01 GROWTH · P1</span>
          <span>CARTOON &amp; TOP NEWS</span>
        </div>
        <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
      </div>

      <!-- Top Row: Cartoon on Left, 60-Second Summary on Right -->
      <div class="p1-top-row">
        <!-- Left: Cartoon Image & Behind the Cartoon -->
        <div class="p1-cartoon-col">
          <div class="p1-cartoon-frame">
            <img src="assets/newsletters/issue-08-cartoon-exact.png" alt="Cartoon: Customer, or bot? Yes.">
          </div>
          <div class="p1-behind-cartoon">
            <strong>Behind the cartoon:</strong> on 11 November an airline barred unauthorised third-party AI agents from completing a purchase on its channels; on 13 November a leading AI developer published what merchants must change before an agent can pay. An agent is a customer and an automated visitor at the same time, and most checkout defences were built to tell those two apart. <a href="#sec-lead-checkout" class="brief-link">Lead story, page 4 ›</a> · <a href="https://skift.com/2026/11/11/united-airlines-moves-to-block-personal-ai-agents-from-booking-flights/" target="_blank" rel="noopener noreferrer" class="src-link">Skift</a> · <a href="https://openai.com/index/introducing-chatgpt-wallet/" target="_blank" rel="noopener noreferrer" class="src-link">Developer’s announcement</a>
          </div>
        </div>

        <!-- Right: 60-Second Summary -->
        <div class="p1-summary-col">
          <div class="p1-summary-header">TOP NEWS THIS WEEK · 60-SECOND SUMMARY</div>
          <div class="p1-summary-list">
            <div class="p1-summary-item">
              <span class="p1-summary-num">1</span>
              <div class="p1-summary-text">
                Nvidia's chief executive resigned and the CFO took over on an interim basis. Its filing speaks directly to customer commitments and the product roadmap. <a href="https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm" target="_blank" rel="noopener noreferrer" class="src-link">NVIDIA 8-K</a>
              </div>
            </div>
            <div class="p1-summary-item">
              <span class="p1-summary-num">2</span>
              <div class="p1-summary-text">
                Five models changed status in four days. One introductory price ends on 30 November, doubling from 1 December. <a href="https://www.anthropic.com/claude-fable-and-mythos-5-2" target="_blank" rel="noopener noreferrer" class="src-link">Anthropic</a> · <a href="https://research.meta.ai/blog/muse-ember" target="_blank" rel="noopener noreferrer" class="src-link">Meta</a> · <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/" target="_blank" rel="noopener noreferrer" class="src-link">Google</a>
              </div>
            </div>
            <div class="p1-summary-item">
              <span class="p1-summary-num">3</span>
              <div class="p1-summary-text">
                The FBI named ten sectors already targeted by an open-source AI intrusion framework, and named partner portals among the entry points. <a href="https://www.infosecurity-magazine.com/news/fbi-growing-abuse-ai-pentesting/" target="_blank" rel="noopener noreferrer" class="src-link">FBI alert</a>
              </div>
            </div>
            <div class="p1-summary-item">
              <span class="p1-summary-num">4</span>
              <div class="p1-summary-text">
                Regulators in four jurisdictions moved on AI in one week, two of them financial. <a href="https://eur-lex.europa.eu/eli/reg_impl/2026/2487/oj/eng" target="_blank" rel="noopener noreferrer" class="src-link">EUR-Lex</a> · <a href="https://finreg-e.com/weekly-regulatory-round-up-15-november-2026/" target="_blank" rel="noopener noreferrer" class="src-link">Regulatory summary</a>
              </div>
            </div>
            <div class="p1-summary-item">
              <span class="p1-summary-num">5</span>
              <div class="p1-summary-text">
                A labour-market preprint puts the early effects of AI in who is employed, not how many. Its authors decline to call it cause and effect. <a href="https://arxiv.org/abs/2507.08244" target="_blank" rel="noopener noreferrer" class="src-link">arXiv preprint</a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Agenda Navy Block -->
      <nav id="agenda" class="p1-agenda-box" aria-label="Newsletter Agenda">
        <div class="p1-agenda-top">
          <div class="p1-agenda-top-left">
            <span class="p1-agenda-title">AGENDA</span>
            <span class="p1-agenda-tagline">5 THEMES · TAP TO JUMP</span>
          </div>
          <div class="p1-agenda-hint">
            Short on time? <a href="#page-1">60-second summary</a> → <a href="#sec-roles-week">Your role</a> → <a href="#sec-leadership-actions">Leadership actions</a>
          </div>
        </div>

        <div class="p1-agenda-columns">
          <!-- 01 GROWTH -->
          <div class="p1-agenda-col">
            <div class="p1-agenda-num">01 GROWTH</div>
            <div class="p1-agenda-question">Where is new revenue coming from?</div>
            <ul class="p1-agenda-links-list">
              <li><a href="#sec-sector-index">P2 Sector index · 22 industries</a></li>
              <li><a href="#sec-lead-checkout">P4 Lead · The checkout decision</a></li>
            </ul>
          </div>

          <!-- 02 COST -->
          <div class="p1-agenda-col">
            <div class="p1-agenda-num">02 COST</div>
            <div class="p1-agenda-question">What does it cost to run?</div>
            <ul class="p1-agenda-links-list">
              <li><a href="#sec-model-releases">P5 Model releases and prices</a></li>
              <li><a href="#sec-infrastructure">P7 Infrastructure &amp; capacity</a></li>
            </ul>
          </div>

          <!-- 03 RISK -->
          <div class="p1-agenda-col">
            <div class="p1-agenda-num">03 RISK</div>
            <div class="p1-agenda-question">What could go wrong?</div>
            <ul class="p1-agenda-links-list">
              <li><a href="#sec-laws-guidance">P6 Laws, rules &amp; guidance</a></li>
              <li><a href="#sec-vendor-risk">P6 Vendor &amp; security risk</a></li>
            </ul>
          </div>

          <!-- 04 CAPITAL -->
          <div class="p1-agenda-col">
            <div class="p1-agenda-num">04 CAPITAL</div>
            <div class="p1-agenda-question">Where is money going?</div>
            <ul class="p1-agenda-links-list">
              <li><a href="#sec-supplier-risk">P5 Supplier &amp; governance risk</a></li>
              <li><a href="#sec-investments">P7 Investments · $100M+</a></li>
            </ul>
          </div>

          <!-- 05 PEOPLE -->
          <div class="p1-agenda-col">
            <div class="p1-agenda-num">05 PEOPLE</div>
            <div class="p1-agenda-question">Who does the work?</div>
            <ul class="p1-agenda-links-list">
              <li><a href="#sec-workforce-talent">P7 Workforce &amp; talent</a></li>
              <li><a href="#sec-leaders-said">P3 Leaders said · One year ago on P3</a></li>
            </ul>
          </div>
        </div>

        <div class="p1-agenda-notice">
          Also in this issue: <a href="#sec-key-numbers">Key numbers</a> · <a href="#sec-regional-index">Regional index</a> · <a href="#sec-caution-note">Caution note</a>. Not in this issue: upcoming events — no date could be confirmed against two independent listings or an organiser's own page. Every source name is a link to the original.
        </div>
      </nav>

      <!-- Section Banner: THIS WEEK FOR YOUR ROLE -->
      <section id="sec-roles-week" style="margin-top: 6px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE · P1</span>
            <span>THIS WEEK FOR YOUR ROLE</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div class="p1-roles-grid">
          <!-- CEO -->
          <div class="p1-role-box">
            <div class="p1-role-title">CEO</div>
            <p class="p1-role-text">Agent traffic at your checkout is a commercial policy question, not an IT one — and it is being decided by default.</p>
          </div>

          <!-- CFO -->
          <div class="p1-role-box">
            <div class="p1-role-title">CFO</div>
            <p class="p1-role-text">One model's introductory price ends on 30 November, doubling from 1 December. Check whether any budget you approved assumes the introductory rate.</p>
          </div>

          <!-- CIO / CTO -->
          <div class="p1-role-box">
            <div class="p1-role-title">CIO / CTO</div>
            <p class="p1-role-text">Five models changed status in four days; one moved from restricted to general availability. Re-check your approved-model list.</p>
          </div>

          <!-- CISO -->
          <div class="p1-role-box">
            <div class="p1-role-title">CISO</div>
            <p class="p1-role-text">The FBI points at partner portals and third-party integrations — the estate you watch least. Some intrusions reached privileged access in under three hours.</p>
          </div>

          <!-- CHRO -->
          <div class="p1-role-box">
            <div class="p1-role-title">CHRO</div>
            <p class="p1-role-text">A preprint finds the early labour effects in composition — hours, age, education — not headcount.</p>
          </div>

          <!-- COO / Sales -->
          <div class="p1-role-box">
            <div class="p1-role-title">COO / Sales</div>
            <p class="p1-role-text">If an agent cannot buy on your site, you may be losing orders you never see. If it can, decide who you refund.</p>
          </div>
        </div>
      </section>

      <!-- Section Banner: LEADERSHIP ACTIONS THIS WEEK -->
      <section id="sec-leadership-actions" style="margin-top: 6px;">
        <div class="section-banner">
          <div class="section-banner-title">
            <span class="banner-theme-tag act">05 PEOPLE · P1</span>
            <span>LEADERSHIP ACTIONS THIS WEEK</span>
          </div>
          <a href="#agenda" class="jump-agenda-btn">↑ Agenda</a>
        </div>

        <div class="p1-actions-grid">
          <!-- Col 1: Items 1 to 4 -->
          <div>
            <div class="p1-action-row" style="margin-bottom: 8px;">
              <strong>1. Decide your agent policy explicitly.</strong> Name the executive who owns whether AI agents may browse, buy and manage accounts on your channels.
            </div>
            <div class="p1-action-row" style="margin-bottom: 8px;">
              <strong>2. Find out what your site does today.</strong> Your firewall and bot rules already answer this question, with no policy behind them.
            </div>
            <div class="p1-action-row" style="margin-bottom: 8px;">
              <strong>3. Write down who you refund</strong> when an agent buys on a customer's behalf and the order is disputed.
            </div>
            <div class="p1-action-row">
              <strong>4. Inventory your partner and supplier portals</strong> against the FBI's list of entry points, not just your main estate.
            </div>
          </div>

          <!-- Col 2: Items 5 to 8 -->
          <div>
            <div class="p1-action-row" style="margin-bottom: 8px;">
              <strong>5. Check every AI line item against current list prices,</strong> including any that are introductory and expire this month.
            </div>
            <div class="p1-action-row" style="margin-bottom: 8px;">
              <strong>6. Ask whether your AI roadmap depends on one supplier's leadership,</strong> and what your contract says about continuity.
            </div>
            <div class="p1-action-row" style="margin-bottom: 8px;">
              <strong>7. If you operate in the EU,</strong> name who would own an AI Act sandbox application ahead of the regulation's 1 December date of effect.
            </div>
            <div class="p1-action-row">
              <strong>8. Ask HR for hours, age and education trends</strong> in your most exposed roles, not just headcount.
            </div>
          </div>
        </div>
      </section>

      <!-- Page 1 Footer -->
      <footer class="page-footer-bar">
        <div class="page-footer-left"><a href="#agenda" class="jump-agenda-btn">↑ Agenda</a></div>
        <div class="page-footer-right">Edition 08 · Page 1 of 7</div>
      </footer>
    </article>"""

# Replace page 1 in html
pattern = r'<!-- ==================== PAGE 1 OF 7 ==================== -->.*?</article>'
html = re.sub(pattern, page1_exact_html, html, flags=re.DOTALL)

with open('ai-newsletter-issue-08.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated Page 1 in ai-newsletter-issue-08.html successfully!")
