document.addEventListener("DOMContentLoaded", () => {
  const BASE_API_URL = "https://ats.people-prime.com/api/public/jobs/";
  const container = document.getElementById("jobDetailContainer");

  // Get job ID from URL
  const urlParams = new URLSearchParams(window.location.search);
  const jobId = urlParams.get("id");

  if (!jobId) {
    showError("Invalid Job ID. Please return to the active jobs page.");
    return;
  }

  // Fetch job details
  async function fetchJobDetails() {
    showLoading();
    try {
      const response = await fetch(`${BASE_API_URL}${jobId}/`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const job = await response.json();
      renderJobDetails(job);
    } catch (error) {
      console.error("Error fetching job details, using mock fallback for testing:", error);

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

      // Lookup by ID, fallback to SAP if not found
      const activeJob = mockResults.find(j => j.id == jobId) || mockResults[1];
      renderJobDetails(activeJob);
    }
  }

  // Render job detail structure
  function renderJobDetails(job) {
    container.innerHTML = "";

    const backLink = document.createElement("a");
    backLink.href = "activejobs.html";
    backLink.className = "back-to-jobs-btn";
    backLink.innerHTML = `&larr; Back to Active Jobs`;
    container.appendChild(backLink);

    const card = document.createElement("div");
    card.className = "job-detail-card";

    // Prepare variables with defaults
    const title = job.position || "Job Opening";
    const jobCode = job.job_code || "PPW-JOB";
    const tech = job.technology || "General";
    const exp = job.experience || "Not Specified";
    const loc = job.location || "Multiple Locations";
    const type = job.job_type || "Full-Time";
    const mode = job.work_mode || "Onsite";

    // Skills tags formatting
    let skillsHTML = "";
    if (job.required_skills && Array.isArray(job.required_skills) && job.required_skills.length > 0) {
      skillsHTML = `
        <div class="skills-section">
          <h2>Required Skills</h2>
          <div class="skills-list">
            ${job.required_skills.map(skill => `<span class="skill-tag">${skill}</span>`).join("")}
          </div>
        </div>
      `;
    } else if (job.required_skills && typeof job.required_skills === "string") {
      skillsHTML = `
        <div class="skills-section">
          <h2>Required Skills</h2>
          <div class="skills-list">
            <span class="skill-tag">${job.required_skills}</span>
          </div>
        </div>
      `;
    }

    // Apply now email subject template
    const emailSubject = encodeURIComponent(`Application for ${title} (${jobCode})`);
    const emailBody = encodeURIComponent(`Hello HR Team,\n\nI would like to apply for the position of ${title} (${jobCode}).\n\nPlease find attached my resume and details.\n\nBest regards,`);
    const mailtoUrl = `mailto:careers@people-prime.com?subject=${emailSubject}&body=${emailBody}`;

    card.innerHTML = `
      <div class="job-detail-header">
        <h1>${title}</h1>
        <span class="job-code-badge">${jobCode}</span>
      </div>
      
      <div class="job-detail-info-list">
        <p><strong>Job Code:</strong> ${jobCode}</p>
        <p><strong>Technology:</strong> ${tech}</p>
        <p><strong>Experience:</strong> ${exp}</p>
        <p><strong>Location:</strong> ${loc}</p>
        <p><strong>Job Type:</strong> ${type}</p>
        <p><strong>Work Mode:</strong> ${mode}</p>
        <p><strong>Payroll on:</strong> People Prime World Wide</p>
      </div>
      
      <div class="job-detail-body">
        <h2>Job Description</h2>
        <div class="job-description-content">${job.description || "No description provided."}</div>
        
        ${skillsHTML}
        
        <div class="apply-section">
          <button id="applyNowBtn" class="apply-btn">Apply Now</button>
        </div>
      </div>
    `;

    container.appendChild(card);

    // Event listener to open candidate application form
    card.querySelector("#applyNowBtn").addEventListener("click", () => {
      openApplicationForm(job.id, title, job);
    });
  }

  // Open candidate application form
  function openApplicationForm(jobId, jobTitle, jobObject) {
    const form = new ATSApplicationForm(
      jobId,
      jobTitle,
      // Cancel Callback (Return to Job Details Card)
      () => {
        renderJobDetails(jobObject);
      },
      // Submit Success Callback
      (formData) => {
        renderSuccessState();
      }
    );
    form.render(container);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  // Render Success Screen
  function renderSuccessState() {
    container.innerHTML = `
      <div class="job-detail-card" style="padding: 60px 40px; text-align: center;">
        <div style="font-size: 64px; color: var(--primary-hover); margin-bottom: 24px; animation: scaleUp 0.4s ease-out;">✓</div>
        <h1 style="color: #ffffff; font-size: 32px; font-weight: 800; margin-bottom: 16px;">Application Submitted Successfully</h1>
        <p style="color: var(--text-muted); font-size: 16px; line-height: 1.8; max-width: 600px; margin: 0 auto 32px auto;">
          Thank you for applying. Our recruitment team will review your application and contact you if your profile matches our requirements.
        </p>
        <div style="display: flex; justify-content: center;">
          <a href="activejobs.html" class="apply-btn" style="text-decoration: none;">Back to Jobs</a>
        </div>
      </div>
    `;
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  // State utility functions
  function showLoading() {
    container.innerHTML = `
      <div class="loading-spinner-container">
        <div class="spinner"></div>
        <p>Loading job details...</p>
      </div>
    `;
  }

  function showError(msg) {
    container.innerHTML = `
      <div style="max-width: 600px; margin: 40px auto;">
        <a href="activejobs.html" class="back-to-jobs-btn">&larr; Back to Active Jobs</a>
        <div class="error-message">
          <h3>Could not load details</h3>
          <p>${msg}</p>
        </div>
      </div>
    `;
  }

  // Initial load
  fetchJobDetails();
});
