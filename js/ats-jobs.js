document.addEventListener("DOMContentLoaded", () => {
  const BASE_API_URL = "https://ats.people-prime.com/api/public/jobs/";
  
  const jobSearch = document.getElementById("jobSearch");
  const locationSearch = document.getElementById("locationSearch");
  const searchBtn = document.getElementById("searchBtn");
  const jobList = document.getElementById("jobList");
  const jobDetailPanel = document.getElementById("jobDetailPanel");
  const pagination = document.getElementById("pagination");

  const ITEMS_PER_PAGE = 10;
  let currentPage = 1;
  let allUniqueJobs = []; // Stores the full deduplicated list
  let activeJobId = null;  // Tracks currently selected job for split preview

  // Fetch all jobs from API
  async function fetchJobs(searchQuery = "", locationQuery = "") {
    showLoading();
    try {
      let allResults = [];
      let url = `${BASE_API_URL}?page_size=1000`;
      if (searchQuery) {
        url += `&search=${encodeURIComponent(searchQuery)}`;
      }

      while (url) {
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        allResults = allResults.concat(data.results || []);
        url = data.next; // will be null when there are no more pages
      }
      
      // Deduplicate jobs by job_code on the frontend
      let cleanJobs = [];
      const seenCodes = new Set();
      allResults.forEach(job => {
        const rawCode = job.job_code || "";
        const normalizedCode = rawCode.toLowerCase().replace(/\s+/g, "");
        if (normalizedCode) {
          if (!seenCodes.has(normalizedCode)) {
            seenCodes.add(normalizedCode);
            cleanJobs.push(job);
          }
        } else {
          // If there's no job code, include it or maybe skip? We'll include it.
          cleanJobs.push(job);
        }
      });

      // Apply location filter locally if entered
      if (locationQuery) {
        const locQ = locationQuery.toLowerCase();
        cleanJobs = cleanJobs.filter(job => 
          (job.location || "").toLowerCase().includes(locQ)
        );
      }

      allUniqueJobs = cleanJobs;
      currentPage = 1;
      renderActivePage();
    } catch (error) {
      console.error("Error fetching jobs, using mock fallback for testing:", error);
      // Mock Fallback for local testing / CORS bypass
      const mockResults = [
        { 
          id: 18669, 
          job_code: "PPW - 18669", 
          position: "Java Spring Boot Developer", 
          technology: "Java", 
          experience: "5 Years", 
          location: "Bengaluru", 
          job_type: "Contract", 
          work_mode: "Hybrid",
          description: "Design and implement Java-based backend applications using Spring Boot framework.\n\nRequired Skills:\n- Java, Spring Boot, microservices\n- REST APIs development\n- SQL Database"
        },
        { 
          id: 18292, 
          job_code: "PPW - 18292", 
          position: "SAP SAC Consultant", 
          technology: "Sap Sac", 
          experience: "8 Years", 
          location: "Hyderabad", 
          job_type: "Contract", 
          work_mode: "Hybrid",
          description: "Strong experience in SAP HANA development with a preference for working in an SAP HANA XSA environment.\nProficient in designing and developing SAP Calculation Views using both Graphical and SQL Script modeling techniques.\nExtensive experience in developing and optimizing complex SQL Script procedures, functions, and queries.\n\nRequired Skills:\n- SAP Analytics Cloud\n- HANA database design\n- SQL Scripting"
        },
        { 
          id: 18670, 
          job_code: "PPW - 18670", 
          position: "ServiceNow HAM Operation Analyst", 
          technology: "ServiceNow", 
          experience: "6 Years", 
          location: "Bengaluru", 
          job_type: "Contract", 
          work_mode: "Hybrid",
          description: "Responsible for hardware asset lifecycle management operations in ServiceNow.\n\nRequired Skills:\n- ServiceNow Hardware Asset Management (HAM)\n- Asset lifecycle workflows\n- General ServiceNow administration"
        },
        { 
          id: 18559, 
          job_code: "PPW - 18559", 
          position: "Data Engineer with GCP (SQL)", 
          technology: "SQL", 
          experience: "8 Years", 
          location: "Hyderabad", 
          job_type: "Contract", 
          work_mode: "Hybrid",
          description: "Build data pipelines and integrate analytics platforms using Google Cloud Platform.\n\nRequired Skills:\n- GCP Dataflow and BigQuery\n- Structured Query Language (SQL)\n- Python scripting for ETL pipelines"
        },
        { 
          id: 18586, 
          job_code: "PPW - 18586", 
          position: "QA Automation Engineer", 
          technology: "Testing", 
          experience: "5 Years", 
          location: "Hyderabad", 
          job_type: "Contract", 
          work_mode: "Hybrid",
          description: "Develop and execute automated test suites using Selenium/Java.\n\nRequired Skills:\n- Automation testing tools (Selenium, Playwright)\n- Core Java programming\n- CI/CD workflow integration"
        },
        { 
          id: 18560, 
          job_code: "PPW - 18560", 
          position: "Cloud Infrastructure Engineer", 
          technology: "Cloud", 
          experience: "8 Years", 
          location: "Bengaluru", 
          job_type: "Contract", 
          work_mode: "Hybrid",
          description: "Provision and maintain scalable cloud architecture on AWS/Azure.\n\nRequired Skills:\n- Infrastructure as Code (Terraform)\n- AWS/Azure administration\n- CI/CD automation pipelines"
        }
      ];

      // Filter local mock array by keyword search query
      let filteredMock = mockResults;
      if (searchQuery) {
        const query = searchQuery.toLowerCase();
        filteredMock = mockResults.filter(job => 
          job.position.toLowerCase().includes(query) ||
          job.technology.toLowerCase().includes(query) ||
          job.job_code.toLowerCase().includes(query) ||
          job.location.toLowerCase().includes(query)
        );
      }

      // Filter local mock array by location search query
      if (locationQuery) {
        const locQuery = locationQuery.toLowerCase();
        filteredMock = filteredMock.filter(job => 
          (job.location || "").toLowerCase().includes(locQuery)
        );
      }

      allUniqueJobs = filteredMock;
      currentPage = 1;
      renderActivePage();
    }
  }

  // Render a specific slice of deduplicated jobs
  function renderActivePage() {
    jobList.innerHTML = "";
    
    if (allUniqueJobs.length === 0) {
      jobList.innerHTML = `
        <div class="no-jobs" style="padding: 20px;">
          <h3>No Jobs Found</h3>
          <p>Try refining your search keyword or location filter.</p>
        </div>
      `;
      pagination.innerHTML = "";
      return;
    }

    // Slice the array for the current page
    const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
    const endIndex = startIndex + ITEMS_PER_PAGE;
    const pageJobs = allUniqueJobs.slice(startIndex, endIndex);

    pageJobs.forEach(job => {
      const card = document.createElement("div");
      card.className = "job-row";
      
      const tech = job.technology || "General";
      const experience = job.experience || "Not Specified";
      const location = job.location || "Multiple Locations";
      const jobType = job.job_type || "Full-Time";
      const workMode = job.work_mode || "Onsite";
      
      const rawDate = job.posted_date || job.created_at || new Date().toISOString();
      let postedDateStr = "Recently posted";
      if (rawDate) {
        const d = new Date(rawDate);
        postedDateStr = isNaN(d) ? rawDate : d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
      }
      
      card.innerHTML = `
        <div style="width: 100%; padding: 4px 0;">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 4px;">
            <div style="display: flex; align-items: center; gap: 4px;">
              <span style="font-size: 11px; color: var(--text-muted); font-weight: 500;">Posted on: ${postedDateStr}</span>
            </div>
            <button style="background: none; border: none; color: var(--primary-color); cursor: pointer; font-size: 16px; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.2)'" onmouseout="this.style.transform='scale(1)'">
              ♡
            </button>
          </div>
          
          <div style="margin-bottom: 6px;">
            <h3 class="job-row-title" style="margin: 0 0 2px 0; color: var(--primary-color); font-size: 15px;">${job.position || "Untitled Position"}</h3>
            <div class="job-row-company" style="font-size: 12px; color: var(--text-main); font-weight: 600;">People Prime Worldwide</div>
          </div>
          
          <div class="job-row-tags" style="margin-bottom: 8px; display: flex; gap: 6px; flex-wrap: wrap;">
            <span class="job-row-tag" style="background: rgba(255,255,255,0.05); color: var(--text-main); border: none; padding: 4px 8px; border-radius: 12px; font-size: 11px;">${workMode}</span>
            <span class="job-row-tag" style="background: rgba(255,255,255,0.05); color: var(--text-main); border: none; padding: 4px 8px; border-radius: 12px; font-size: 11px;">${jobType}</span>
            <span class="job-row-tag" style="background: rgba(255,255,255,0.05); color: var(--text-main); border: none; padding: 4px 8px; border-radius: 12px; font-size: 11px;">${experience}</span>
          </div>
          
          <div style="display: flex; align-items: center; color: var(--text-muted); font-size: 11px;">
            <svg style="margin-right: 4px; width: 12px; height: 12px; fill: currentColor;" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
            ${location}
          </div>
        </div>
      `;

      card.addEventListener("click", () => {
        window.open(`job-details.html?id=${job.id}`, '_blank');
      });

      jobList.appendChild(card);
    });

    renderLocalPagination();
  }

  // Render Pagination controls
  function renderLocalPagination() {
    pagination.innerHTML = "";
    const totalPages = Math.ceil(allUniqueJobs.length / ITEMS_PER_PAGE) || 1;

    const prevBtn = document.createElement("button");
    prevBtn.className = "pagination-btn";
    prevBtn.disabled = currentPage === 1;
    prevBtn.innerHTML = `&larr; Previous`;
    prevBtn.addEventListener("click", () => {
      if (currentPage > 1) {
        currentPage--;
        renderActivePage();
      }
    });
    pagination.appendChild(prevBtn);

    const infoSpan = document.createElement("span");
    infoSpan.className = "page-info";
    infoSpan.textContent = `Page ${currentPage} of ${totalPages}`;
    pagination.appendChild(infoSpan);

    const nextBtn = document.createElement("button");
    nextBtn.className = "pagination-btn";
    nextBtn.disabled = currentPage === totalPages;
    nextBtn.innerHTML = `Next &rarr;`;
    nextBtn.addEventListener("click", () => {
      if (currentPage < totalPages) {
        currentPage++;
        renderActivePage();
      }
    });
    pagination.appendChild(nextBtn);
  }

  // State utility functions
  function showLoading() {
    jobList.innerHTML = `
      <div class="loading-spinner-container" style="padding: 20px;">
        <div class="spinner"></div>
        <p>Loading jobs...</p>
      </div>
    `;
    pagination.innerHTML = "";
  }

  // Event Listeners for dual search bar
  function handleSearch() {
    const query = jobSearch.value.trim();
    const locQuery = locationSearch.value.trim();
    fetchJobs(query, locQuery);
  }

  searchBtn.addEventListener("click", handleSearch);

  // Debounced input search to load results automatically as they type
  let debounceTimeout;
  const triggerDebouncedSearch = () => {
    clearTimeout(debounceTimeout);
    debounceTimeout = setTimeout(() => {
      handleSearch();
    }, 400);
  };

  jobSearch.addEventListener("input", triggerDebouncedSearch);
  locationSearch.addEventListener("input", triggerDebouncedSearch);

  // Check URL parameters for search queries on load (from categories grid)
  const urlParams = new URLSearchParams(window.location.search);
  const searchParam = urlParams.get("search") || "";
  
  if (searchParam) {
    jobSearch.value = searchParam;
  }

  // Initial Fetch
  fetchJobs(searchParam);
});
