import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ai-newsletter-issue-06.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    # Masthead & Header
    "W E E K L Y · E D I T I O N 0 6",
    "2 6 O C T – 1 N O V 2 0 2 6 · P A G E 1 O F 6",
    "The AI Leadership Brief",
    "Edition 06 · 26 Oct–1 Nov 2026 · By Jayaraman (Jay) Ganapathi, People Prime Worldwide · For CXOs and senior leaders",
    
    # Page 1 Cartoon & Agenda
    "“This week: SK hynix says memory supply is not keeping pace — and even the robots are queuing for AI memory.”",
    "5 THEMES · TAP TO JUMP",
    "Short on time?",
    "60-second summary",
    "Your role",
    "Leadership actions",
    "01 Growth &amp; revenue",
    "02 Cost &amp; output",
    "03 Risk &amp; compliance",
    "04 Capital &amp; markets",
    "05 People &amp; action",
    
    # Page 1 60-second summary
    "Demand is in the numbers.",
    "Supply is on chipmakers' agenda.",
    "One maker cut a model price.",
    "Vendor risk is real.",
    "Four large rounds.",
    
    # Page 1 Roles
    "CEO", "CFO", "CIO / CTO", "CISO / CRO", "CHRO", "COO",
    "Capgemini forecasts 2026 growth",
    "GPT-6.1 Terra standard API: $1 / $5",
    "SK hynix expects memory demand to exceed supply through 2030",
    "Provider's account: it knew of a cache-size mismatch before launch; 155 responses exposed other users' data",
    "SAP India: 2 million people with AI skills by 2030",
    "Hitachi plans a 35,000-person digital company",
    
    # Page 1 Leadership actions
    "Measure value, not activity.",
    "Lock in capacity.",
    "Re-run rejected cases.",
    "Tighten vendor terms.",
    "Gate agent actions.",
    "Confirm patching.",
    "Set a skills target.",
    "India operations:",
    
    # Page 2 Lead story & Models
    "LEAD: DEMAND SHOWS UP IN THE RESULTS",
    "COMPANY RESULTS · 28–30 OCT 2026",
    "SK hynix", "104.6 trillion won", "+328%",
    "Intel", "$16.5B", "+78%",
    "Capgemini", "€6,073M", "+11.7%",
    "NEW LLM RELEASES OR SECURITY PATCH RELEASES",
    "OpenAI GPT-6.1 Terra", "$1 input / $5 output",
    "Google Gemini 4 Carbon", "cybersecurity defenders",
    "vLLM v0.32.0", "SGLang v0.5.22+",
    
    # Page 3 AI research & Vendor risk
    "AI RESEARCH: RELIABILITY AND QUALITY CHECKS",
    "Preprint: a “decision gate” checks what an AI agent is about to do before it acts",
    "JevAct", "τ²-bench",
    "Preprint: AI models caught most planted errors in clinical-trial reports",
    "58–99%", "14–29%",
    "VENDOR &amp; SECURITY RISK",
    "A large cloud provider says 155 responses from one hosted model contained other users' data",
    "SGLang engine",
    
    # Page 4 Unsolved, Laws, Infra
    "UNSOLVED PROBLEMS IN AI",
    "Preprint: where a hidden instruction sits can change whether AI agents obey it",
    "trust region effect",
    "LAWS, RULES &amp; GUIDANCE",
    "MeitY releases a draft handbook for training AI on sensitive data without handing it over",
    "DEPA", "iSPIRT Foundation",
    "INFRASTRUCTURE &amp; CAPACITY",
    "Runware plans an assembly line for factory-built AI data-centre pods",
    "30 MW of data-centre capacity per day by 2028",
    
    # Page 5 Investments, Operating models, Workforce, Regional index
    "INVESTMENTS ($100M AND ABOVE)",
    "FuriosaAI", "$620M",
    "Upwind", "$400M",
    "Serval", "$150M",
    "Hex", "$100M",
    "OPERATING MODELS: AI IN INDUSTRIAL SECTORS",
    "Hitachi to launch a 35,000-person digital services company",
    "WORKFORCE &amp; TALENT",
    "SAP India adds programmes toward 2 million people with AI skills by 2030",
    "REGIONAL INDEX",
    "North America", "Europe &amp; UK", "India", "Japan", "Australia", "South Korea", "Global",
    
    # Page 6 Leaders Said, Numbers, Events, One year ago, Caution
    "LEADERS SAID",
    "Aiman Ezzat", "June Paik", "Manish Prasad",
    "KEY NUMBERS",
    "+78%", "2030", "+9.0–9.5%", "50%", "155", "$1.27B",
    "ONE YEAR AGO",
    "A large online retailer said it would cut about 14,000 corporate jobs",
    "NVIDIA agreed a $1.0B equity investment in Nokia",
    "OpenAI put Aardvark, an “agentic security researcher”, into private beta",
    "UPCOMING EVENTS",
    "SC26", "MEDICA", "The AI Summit New York",
    "CAUTION NOTE",
    "Caution: verify before business use"
]

all_passed = True
for check in checks:
    if check not in html:
        print("FAIL: Missing ->", check)
        all_passed = False

if all_passed:
    print(f"ALL {len(checks)} CONTENT CHECKS PASSED PERFECTLY FOR ISSUE 06!")
