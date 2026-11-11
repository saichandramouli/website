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
      const response = await fetch(`${BASE_API_URL}${jobId}/`, { cache: "no-store" });

      // Handle Closed Job (HTTP 410 Gone)
      if (response.status === 410) {
        let message = "This job is closed and no longer accepting applications.";
        try {
          const errData = await response.json();
          if (errData && errData.message) {
            message = errData.message;
          }
        } catch (_) {
          // Keep default message if json parse fails
        }
        showClosedJobState(message);
        showClosedJobModal(message);
        return;
      }

      // Handle Unavailable Job (HTTP 404 Not Found)
      if (response.status === 404) {
        showError("This job opening is unavailable or has been removed.");
        return;
      }

      // Handle other non-2xx HTTP errors
      if (!response.ok) {
        showError("Unable to load job details at this time. Please try again later.");
        return;
      }

      const job = await response.json();

      // Guard check in case an active 200 payload flags the job as closed
      if (job && (job.is_closed === true || job.code === "JOB_CLOSED" || job.status === "CLOSED")) {
        const message = job.message || "This job is closed and no longer accepting applications.";
        showClosedJobState(message, job);
        showClosedJobModal(message);
        return;
      }

      renderJobDetails(job);
    } catch (error) {
      console.error("Error fetching job details:", error);
      showError("Unable to load job details at this time. Please try again later.");
    }
  }

  // Helper to display dedicated Closed Job Modal popup
  function showClosedJobModal(message = "This job is closed and no longer accepting applications.") {
    // Prevent duplicate popup instances
    const existingModal = document.getElementById("atsClosedJobModal");
    if (existingModal) {
      existingModal.remove();
    }

    const modal = document.createElement("div");
    modal.id = "atsClosedJobModal";
    modal.className = "ats-modal-overlay";
    modal.innerHTML = `
      <div class="ats-modal-container" style="max-width: 520px;">
        <div class="ats-modal-header">
          <h2>Job Closed</h2>
          <button type="button" id="closeClosedJobModal" class="ats-modal-close-btn" aria-label="Close">&times;</button>
        </div>
        <div class="ats-modal-body">
          <p id="closedJobModalMessage" style="margin: 0; font-size: 15px; color: #cbd5e1; line-height: 1.6;"></p>
        </div>
        <div class="ats-modal-footer">
          <button type="button" id="confirmClosedJobModal" class="apply-btn">Understood</button>
        </div>
      </div>
    `;

    // Safely assign text message using textContent to prevent HTML/DOM injection
    const messageEl = modal.querySelector("#closedJobModalMessage");
    if (messageEl) {
      messageEl.textContent = message;
    }

    document.body.appendChild(modal);
    document.body.style.overflow = "hidden"; // Lock background scroll

    const closeModal = () => {
      modal.remove();
      document.body.style.overflow = ""; // Restore background scroll
    };

    modal.querySelector("#closeClosedJobModal").addEventListener("click", closeModal);
    modal.querySelector("#confirmClosedJobModal").addEventListener("click", closeModal);

    // Close on click outside modal container
    modal.addEventListener("click", (e) => {
      if (e.target === modal) {
        closeModal();
      }
    });
  }

  // Attach modal helper to window for cross-module accessibility
  window.showClosedJobModal = showClosedJobModal;

  // Render Closed Job State inside container (keeps candidate on page with disabled apply)
  function showClosedJobState(message, job = null) {
    container.innerHTML = "";

    const backLink = document.createElement("a");
    backLink.href = "activejobs.html";
    backLink.className = "back-to-jobs-btn";
    backLink.innerHTML = `&larr; Back to Active Jobs`;
    container.appendChild(backLink);

    const card = document.createElement("div");
    card.className = "job-detail-card";

    const title = (job && job.position) ? job.position : "Job Opening";
    const jobCode = (job && job.job_code) ? job.job_code : (jobId ? `PPW - ${jobId}` : "PPW-JOB");

    card.innerHTML = `
      <div class="job-detail-header">
        <h1></h1>
        <span class="job-code-badge"></span>
      </div>
      <div class="job-detail-body">
        <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 8px; padding: 24px; margin-bottom: 24px; text-align: center;">
          <h2 style="color: #ffffff; font-size: 20px; margin-bottom: 10px; font-weight: 700;">Job Closed</h2>
          <p id="closedJobStateMessage" style="color: #cbd5e1; font-size: 15px; margin: 0; line-height: 1.6;"></p>
        </div>

        <div class="apply-section">
          <button class="apply-btn" disabled style="opacity: 0.6; cursor: not-allowed; background: #475569; pointer-events: none;">Applications Closed</button>
        </div>
      </div>
    `;

    // Safely assign text content to prevent DOM/XSS injection
    const headerTitleEl = card.querySelector(".job-detail-header h1");
    if (headerTitleEl) headerTitleEl.textContent = title;

    const badgeEl = card.querySelector(".job-code-badge");
    if (badgeEl) badgeEl.textContent = jobCode;

    const stateMsgEl = card.querySelector("#closedJobStateMessage");
    if (stateMsgEl) stateMsgEl.textContent = message;

    container.appendChild(card);
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
    const isClosed = Boolean(job && (job.is_closed === true || job.code === "JOB_CLOSED" || job.status === "CLOSED"));
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
          ${
      isClosed
        ? `<button class="apply-btn" disabled style="opacity: 0.6; cursor: not-allowed; background: #475569; pointer-events: none;">Applications Closed</button>`
        : `<button id="applyNowBtn" class="apply-btn">Apply Now</button>`
    }
        </div >
      </div >
      `;

    container.appendChild(card);

    // Event listener to open candidate application form (only if active)
    if (!isClosed) {
      const applyBtn = card.querySelector("#applyNowBtn");
      if (applyBtn) {
        applyBtn.addEventListener("click", () => {
          openApplicationForm(job.id, title, job);
        });
      }
    }
  }

  // Open candidate application form with closed-job safeguard
  function openApplicationForm(jobId, jobTitle, jobObject) {
    // Enforcement guard: prevent application form from opening for closed jobs
    if (jobObject && (jobObject.is_closed === true || jobObject.code === "JOB_CLOSED" || jobObject.status === "CLOSED")) {
      showClosedJobModal("This job is closed and no longer accepting applications.");
      return;
    }

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
      },
      jobObject
    );
    form.render(container);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  // Render Success Screen
  function renderSuccessState() {
    container.innerHTML = `
      < div class="job-detail-card" style = "padding: 60px 40px; text-align: center;" >
        <div style="font-size: 64px; color: var(--primary-hover); margin-bottom: 24px; animation: scaleUp 0.4s ease-out;">✓</div>
        <h1 style="color: #ffffff; font-size: 32px; font-weight: 800; margin-bottom: 16px;">Application Submitted Successfully</h1>
        <p style="color: var(--text-muted); font-size: 16px; line-height: 1.8; max-width: 600px; margin: 0 auto 32px auto;">
          Thank you for applying. Our recruitment team will review your application and contact you if your profile matches our requirements.
        </p>
        <div style="display: flex; justify-content: center;">
          <a href="activejobs.html" class="apply-btn" style="text-decoration: none;">Back to Jobs</a>
        </div>
      </div >
      `;
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  // State utility functions
  function showLoading() {
    container.innerHTML = `
      < div class="loading-spinner-container" >
        <div class="spinner"></div>
        <p>Loading job details...</p>
      </div >
      `;
  }

  function showError(msg) {
    container.innerHTML = `
      < div style = "max-width: 600px; margin: 40px auto;" >
        <a href="activejobs.html" class="back-to-jobs-btn">&larr; Back to Active Jobs</a>
        <div class="error-message">
          <h3>Could not load details</h3>
          <p>${msg}</p>
        </div>
      </div >
      `;
  }

  // Initial load
  fetchJobDetails();
});
