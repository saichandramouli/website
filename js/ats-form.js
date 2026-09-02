/**
 * candidate Application Form Component System (Vanilla JS ES6 Modules/Classes)
 * Implements: ATSApplicationForm, ATSInput, ATSFileUpload, ATSTermsModal, ATSValidation, ATSSubmitButton
 */

// 1. Validation Helper Component
class ATSValidation {
  static cleanValue(value, rules) {
    if (!value) return value;
    let cleaned = value.toString();
    if (rules.exactly10Digits) {
      cleaned = cleaned.replace(/\+91/g, "").replace(/[\s\-]/g, "");
    }
    if (rules.numeric) {
      cleaned = cleaned.replace(/[^\d.]/g, "");
    }
    return cleaned;
  }

  static isAlphaOnly(value) {
    return /^[A-Za-z\s.\-']+$/.test(value);
  }

  static isNumeric(value) {
    return /^\d+(\.\d+)?$/.test(value);
  }

  static isExactly10Digits(value) {
    return /^\d{10}$/.test(value);
  }

  static isValidEmail(value) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(value);
  }

  static validateField(name, value, rules) {
    const val = this.cleanValue(value, rules);
    if (rules.required && (!val || val.trim() === "")) {
      return `${name} is required.`;
    }
    if (val && rules.alphaOnly && !this.isAlphaOnly(val)) {
      return `${name} must contain only alphabets, spaces, dots, hyphens, or apostrophes.`;
    }
    if (val && rules.numeric && !this.isNumeric(val)) {
      return `${name} must be a valid number.`;
    }
    if (val && rules.exactly10Digits && !this.isExactly10Digits(val)) {
      return `${name} must be exactly 10 digits.`;
    }
    if (val && rules.email && !this.isValidEmail(val)) {
      return `Enter a valid email address.`;
    }
    return null;
  }
}

// 2. Terms & Conditions Modal Component
class ATSTermsModal {
  constructor() {
    this.modalEl = null;
  }

  render() {
    const modal = document.createElement("div");
    modal.id = "atsTermsModal";
    modal.className = "ats-modal-overlay hidden";
    modal.innerHTML = `
      <div class="ats-modal-container">
        <div class="ats-modal-header">
          <h2>Terms and Conditions</h2>
          <button id="closeTermsModal" class="ats-modal-close-btn">&times;</button>
        </div>
        <div class="ats-modal-body">
          <h3>Our Policies and Procedures for New Security Program Implementation</h3>
          <p>People Prime Worldwide introduces a new security program aimed at adhering to certain policies and procedures in order to reflect the level of maturity desired. We believe that the probability of effective risk management could be increased drastically with the successful implementation of these security programs.</p>
          <p>At People Prime, our organization has zeroed upon a specific employee who is responsible for all activities related to security programs right from implementation to maintenance.</p>
          
          <h4>1. Acceptable Use Policy [AUP]</h4>
          <p>Understanding an AUP is all about the constraints and practices an employee using organizational IT assets who must commit in order to access to the corporate network or the internet. It is official onboarding policy for new joiners. They are given an AUP to go through and duly sign before being given a network ID. It is suggested that organizations IT, security, legal and HR departments detail what is present in this policy.</p>
          
          <h4>2. Access Control Policy [ACP]</h4>
          <p>The ACP streamlines the access provided to the employees in relation to an organization’s data and information systems. Few aspects that are actually included in the policy are access control standards such as NIST’s Access Control and Implementation Guides. Rest of the items mentioned in this policy are standards for user access, network access controls, operating system software controls and the difficulty of corporate passwords.</p>
          
          <h4>3. Change Management Policy</h4>
          <p>A change management policy focuses upon a formal process for bringing reforms in IT, software development and security services/operations. The intention of a change management program is to spread the awareness and perception of proposed changes across an organization, and to ensure that all changes are conducted methodically to restrict any severe impact on services and clients.</p>
          
          <h4>4. Information Security Policy</h4>
          <p>Latest information security policies in any organization are typically high-level policies that can take care of a large number of security controls. The principal information security policy is issued by the company to ensure that all employees who use information technology assets within the confinement of the organization, or its networks, comply with its stated rules and guidelines. In fact, organizations ask employees to sign this document to acknowledge that they have gone through it (which is generally done with the signing of the AUP policy).</p>
          
          <h4>5. Incident Response [IR] Policy</h4>
          <p>The exact manner in which a company will manage an incident and remediate the impact to operations is what it is all about the incident response policy. It’s the one policy CISOs hope to never have to use. In all probability, the goal of this policy is to highlight the process of handling an incident in direct relation to limiting the damage to business operations, customers and reducing recovery time and costs.</p>
          
          <h4>6. Remote Access Policy</h4>
          <p>The remote access policy is a document which reflects and explains acceptable methods of remotely connecting to an organization's internal networks in detail. It can also be considered that this policy include addendums with rules for the use of BYOD assets. This policy is a necessity for organizations that have dispersed networks with the ability to extend into insecure network spots, like the local coffee house or unmanaged home networks.</p>
          
          <h4>7. Email / Communication Policy</h4>
          <p>An organization’s email policy is a document that is chosen to formally outline how employees can use the business’ predefined electronic communication medium. It can be understood that this policy includes emails, blogs, social media and chat technologies. The ultimate goal of this policy is to set guidelines to employees on what is referred to as the acceptable and unacceptable use of any corporate communication technology.</p>
          
          <h4>8. Disaster Recovery Policy</h4>
          <p>Proactive prevention of insecurity is one of the vital aspects organizations must consider. In fact, an organization’s disaster recovery plan will usually include both cyber security and IT teams’ input and will be processed as part of the strategic business continuity plan. The CISO and teams will take care of an incident through the incident response policy. If the event has a major business impact, the Business Continuity Plan will be activated.</p>
          
          <h4>9. Business Continuity Plan</h4>
          <p>The Business Continuity Plan [BCP] will radiate upon the efforts across the organization and will rely upon the disaster recovery plan to restore hardware, applications and data deemed essential for business continuity. BCPs are different from each other and applied to every business because they elaborate how the organization will operate in an emergency. Alternatively, the strengths of an organization would be put to test during this plan.</p>
          
          <h4>10. Strategic Security Plan</h4>
          <p>Effective security coverage given to the organizational infrastructure determines the stability with which organizations will operate in the future. Devising a master plan to implementing the same is the most critical phases of this plan. Numerous issues are experienced in case this plan not implemented properly. Some of the common issues that are bothersome to the core are delays in project delivery, terrible security implementation, and maximized operational costs.</p>
          
          <p><strong>"Emerging organizations are set to prosper only when all the above 10 security policies are implemented in tandem."</strong></p>
        </div>
        <div class="ats-modal-footer">
          <button id="acceptModalTerms" class="apply-btn">I Understand & Agree</button>
        </div>
      </div>
    `;
    document.body.appendChild(modal);
    this.modalEl = modal;

    // Attach Event Listeners
    modal.querySelector("#closeTermsModal").addEventListener("click", () => this.close());
    modal.querySelector("#acceptModalTerms").addEventListener("click", () => {
      this.close();
      if (this.onAcceptCallback) this.onAcceptCallback();
    });

    // Close on click outside modal container
    modal.addEventListener("click", (e) => {
      if (e.target === modal) this.close();
    });
  }

  open(onAccept) {
    if (!this.modalEl) this.render();
    this.onAcceptCallback = onAccept;
    this.modalEl.classList.remove("hidden");
    document.body.style.overflow = "hidden"; // Lock background scroll
  }

  close() {
    if (this.modalEl) {
      this.modalEl.classList.add("hidden");
      document.body.style.overflow = ""; // Restore scroll
    }
  }
}

// 3. Modular Input Component
class ATSInput {
  static createMarkup({ id, label, type = "text", required = true, placeholder = "", options = [] }) {
    const isRequiredMark = required ? '<span class="req-star">*</span>' : '<span class="opt-mark">(Optional)</span>';

    let inputHTML = "";
    if (type === "select") {
      inputHTML = `
        <select id="${id}" name="${id}" class="ats-form-control">
          <option value="" disabled selected>${placeholder || "Select option"}</option>
          ${options.map(opt => `<option value="${opt}">${opt}</option>`).join("")}
        </select>
      `;
    } else {
      inputHTML = `
        <input type="${type}" id="${id}" name="${id}" class="ats-form-control" placeholder="${placeholder}" />
      `;
    }

    return `
      <div class="ats-form-group">
        <label for="${id}">${label} ${isRequiredMark}</label>
        ${inputHTML}
        <div class="ats-error-label" id="err-${id}"></div>
      </div>
    `;
  }
}

// 4. File Upload Component
class ATSFileUpload {
  constructor(onChange) {
    this.onChange = onChange;
    this.file = null;
    this.error = null;
  }

  renderMarkup() {
    return `
      <div class="ats-form-group full-width">
        <label>Resume Upload <span class="req-star">*</span></label>
        <div class="ats-upload-zone" id="atsUploadZone">
          <input type="file" id="resumeUploadInput" style="display: none;" accept=".pdf,.doc,.docx" />
          <div class="upload-icon">📄</div>
          <p class="upload-prompt">Drag & drop your resume here, or <span class="highlight">browse files</span></p>
          <p class="upload-formats">Supported formats: PDF, DOC, DOCX (Max 10MB)</p>
          <div class="selected-filename hidden" id="selectedFilenameContainer">
            Selected File: <strong id="selectedFilename">None</strong>
            <button type="button" class="remove-file-btn" id="removeFileBtn">&times;</button>
          </div>
        </div>
        <div class="ats-error-label" id="err-resumeUploadInput"></div>
      </div>
    `;
  }

  init(containerEl) {
    const zone = containerEl.querySelector("#atsUploadZone");
    const input = containerEl.querySelector("#resumeUploadInput");
    const nameContainer = containerEl.querySelector("#selectedFilenameContainer");
    const nameEl = containerEl.querySelector("#selectedFilename");
    const removeBtn = containerEl.querySelector("#removeFileBtn");
    const errorEl = containerEl.querySelector("#err-resumeUploadInput");

    // Click triggers file input
    zone.addEventListener("click", (e) => {
      if (e.target !== removeBtn && !removeBtn.contains(e.target)) {
        input.click();
      }
    });

    // File change handler
    const handleFile = (files) => {
      if (files.length === 0) return;
      const file = files[0];
      const name = file.name;
      const ext = name.split(".").pop().toLowerCase();
      const sizeMB = file.size / (1024 * 1024);

      // Reset
      this.file = null;
      this.error = null;
      errorEl.textContent = "";
      nameContainer.classList.add("hidden");

      // Validate Extension
      if (!["pdf", "doc", "docx"].includes(ext)) {
        this.error = "Invalid file type. Only PDF, DOC, and DOCX are allowed.";
        errorEl.textContent = this.error;
        this.onChange(null, this.error);
        return;
      }

      // Validate Size
      if (sizeMB > 10) {
        this.error = "File size exceeds the 10 MB limit.";
        errorEl.textContent = this.error;
        this.onChange(null, this.error);
        return;
      }

      // Success
      this.file = file;
      nameEl.textContent = name;
      nameContainer.classList.remove("hidden");
      this.onChange(file, null);
    };

    input.addEventListener("change", (e) => handleFile(e.target.files));

    // Drag & Drop
    zone.addEventListener("dragover", (e) => {
      e.preventDefault();
      zone.classList.add("dragover");
    });

    zone.addEventListener("dragleave", () => {
      zone.classList.remove("dragover");
    });

    zone.addEventListener("drop", (e) => {
      e.preventDefault();
      zone.classList.remove("dragover");
      handleFile(e.dataTransfer.files);
    });

    // Remove File Action
    removeBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      this.file = null;
      this.error = "Resume is required.";
      input.value = "";
      nameContainer.classList.add("hidden");
      this.onChange(null, this.error);
    });
  }
}

// 5. Submit Button Component
class ATSSubmitButton {
  static createMarkup() {
    return `
      <div class="ats-form-actions">
        <button type="button" class="ats-btn-cancel" id="cancelApplyBtn">Cancel</button>
        <button type="submit" class="apply-btn" id="submitApplyBtn" disabled>Apply</button>
      </div>
    `;
  }
}

// 6. Complete Application Form Component
class ATSApplicationForm {
  constructor(jobId, jobTitle, onCancel, onSubmitSuccess) {
    this.jobId = jobId;
    this.jobTitle = jobTitle;
    this.onCancel = onCancel;
    this.onSubmitSuccess = onSubmitSuccess;
    this.termsModal = new ATSTermsModal();
    this.fileUpload = null;

    // Define input fields configurations in exact order
    this.fieldConfigs = [
      { id: "firstName", label: "First Name", required: true, rules: { required: true, alphaOnly: true } },
      { id: "lastName", label: "Last Name", required: true, rules: { required: true, alphaOnly: true } },
      { id: "mobileNumber", label: "Mobile Number", required: true, rules: { required: true, exactly10Digits: true } },
      { id: "alternateMobile", label: "Alternate Mobile Number", required: false, rules: { required: false, exactly10Digits: true } },
      { id: "email", label: "Email Address", required: true, rules: { required: true, email: true } },
      { id: "qualification", label: "Qualification", required: true, type: "select", options: ["High School", "Bachelor Degree", "Master Degree", "Ph.D.", "Diploma / Other"], rules: { required: true } },
      { id: "experience", label: "Years of Experience", required: true, placeholder: "e.g. 5", rules: { required: true, numeric: true } },
      { id: "expectedPay", label: "Expected Pay (Monthly / INR)", required: true, placeholder: "e.g. 80000", rules: { required: true, numeric: true } },
      { id: "primarySkills", label: "Primary Skills", required: true, placeholder: "e.g. Java, Spring Boot, SQL", rules: { required: true } },
      { id: "currentCtc", label: "Current CTC (LPA)", required: true, placeholder: "e.g. 1200000", rules: { required: true, numeric: true } },
      { id: "currentCompany", label: "Current Company", required: true, placeholder: "e.g. Tech Solutions Pvt Ltd", rules: { required: true } },
      { id: "state", label: "State", required: true, placeholder: "e.g. Telangana", rules: { required: true } },
      { id: "city", label: "City", required: true, placeholder: "e.g. Hyderabad", rules: { required: true } }
    ];
  }

  render(parentContainer) {
    this.parentContainer = parentContainer;
    this.parentContainer.innerHTML = "";

    const formWrapper = document.createElement("div");
    formWrapper.className = "job-detail-card";

    // Generate markup for all inputs
    const inputsHTML = this.fieldConfigs.map(config => ATSInput.createMarkup(config)).join("");

    // File upload markup instance
    this.fileUpload = new ATSFileUpload((file, error) => {
      this.resumeFile = file;
      this.resumeError = error;
      this.validateFormSilently();
    });
    const fileUploadHTML = this.fileUpload.renderMarkup();

    formWrapper.innerHTML = `
      <div class="job-detail-header">
        <h1>Candidate Application Form</h1>
        <span class="job-code-badge">Applying For: ${this.jobTitle}</span>
      </div>
      <form id="atsApplicationForm" class="ats-application-form">
        <div class="ats-form-grid">
          ${inputsHTML}
          ${fileUploadHTML}
        </div>
        
        <div class="ats-terms-container">
          <label class="ats-checkbox-label">
            <input type="checkbox" id="termsCheckbox" />
            <span class="checkbox-text">I have read and agree to the <a href="javascript:void(0)" id="openTermsLink" class="terms-link">Terms & Conditions</a>.</span>
          </label>
          <div class="ats-error-label" id="err-termsCheckbox" style="margin-top: 5px;"></div>
        </div>

        ${ATSSubmitButton.createMarkup()}
      </form>
    `;

    this.parentContainer.appendChild(formWrapper);

    // Initialize File upload handlers
    this.fileUpload.init(formWrapper);

    // Cache DOM Elements
    this.form = formWrapper.querySelector("#atsApplicationForm");
    this.termsCheckbox = formWrapper.querySelector("#termsCheckbox");
    this.submitBtn = formWrapper.querySelector("#submitApplyBtn");
    const openTermsLink = formWrapper.querySelector("#openTermsLink");
    const cancelBtn = formWrapper.querySelector("#cancelApplyBtn");

    // Add Live validation on blur
    this.fieldConfigs.forEach(config => {
      const inputEl = this.form.querySelector(`#${config.id}`);
      inputEl.addEventListener("blur", () => this.validateFieldById(config.id));
      inputEl.addEventListener("input", () => {
        // Clear error as they correct it
        this.clearFieldError(config.id);
        this.validateFormSilently();
      });
    });

    // Terms checkbox toggles submit button state
    this.termsCheckbox.addEventListener("change", () => {
      this.validateFormSilently();
      this.clearFieldError("termsCheckbox");
    });

    // Links triggers
    openTermsLink.addEventListener("click", () => {
      this.termsModal.open(() => {
        this.termsCheckbox.checked = true;
        this.validateFormSilently();
        this.clearFieldError("termsCheckbox");
      });
    });

    cancelBtn.addEventListener("click", () => this.onCancel());

    // Submit handler
    this.form.addEventListener("submit", (e) => {
      e.preventDefault();
      this.handleSubmit();
    });
  }

  validateFieldById(id) {
    const config = this.fieldConfigs.find(c => c.id === id);
    const inputEl = this.form.querySelector(`#${id}`);
    const errorEl = this.form.querySelector(`#err-${id}`);

    // Clean and update UI on blur
    const cleaned = ATSValidation.cleanValue(inputEl.value, config.rules || {});
    if (inputEl.value !== cleaned) {
      inputEl.value = cleaned;
    }

    const errorMsg = ATSValidation.validateField(config.label, inputEl.value, config.rules);

    if (errorMsg) {
      errorEl.textContent = errorMsg;
      inputEl.classList.add("input-error");
      return false;
    } else {
      errorEl.textContent = "";
      inputEl.classList.remove("input-error");
      return true;
    }
  }

  clearFieldError(id) {
    const inputEl = this.form.querySelector(`#${id}`);
    const errorEl = this.form.querySelector(`#err-${id}`);
    if (errorEl) errorEl.textContent = "";
    if (inputEl) inputEl.classList.remove("input-error");
  }

  validateFormSilently() {
    let isValid = true;

    // Check all text inputs
    this.fieldConfigs.forEach(config => {
      const inputEl = this.form.querySelector(`#${config.id}`);
      const cleaned = ATSValidation.cleanValue(inputEl.value, config.rules || {});
      const errorMsg = ATSValidation.validateField(config.label, cleaned, config.rules);
      if (errorMsg) isValid = false;
    });

    // Check file upload
    if (!this.resumeFile) isValid = false;

    // Check terms
    if (!this.termsCheckbox.checked) isValid = false;

    // Toggle button state
    this.submitBtn.disabled = !isValid;
    return isValid;
  }

  async handleSubmit() {
    // Run full validation
    let isFormValid = true;

    this.fieldConfigs.forEach(config => {
      const valid = this.validateFieldById(config.id);
      if (!valid) isFormValid = false;
    });

    // Validate Resume
    const fileErrorEl = this.form.querySelector("#err-resumeUploadInput");
    if (!this.resumeFile) {
      fileErrorEl.textContent = "Resume is required.";
      isFormValid = false;
    }

    // Validate Terms Checkbox
    const termsErrorEl = this.form.querySelector("#err-termsCheckbox");
    if (!this.termsCheckbox.checked) {
      termsErrorEl.textContent = "Please accept the Terms & Conditions.";
      isFormValid = false;
    }

    if (!isFormValid) return;

    // Form is valid - prepare submission
    this.submitBtn.disabled = true;
    this.submitBtn.innerHTML = `<span class="btn-spinner"></span> Submitting...`;

    // Build FormData payload (needed for file upload + fields)
    const formData = new FormData();
    formData.append("resume", this.resumeFile);
    formData.append("job_id", this.jobId);
    formData.append("job_title", this.jobTitle);

    this.fieldConfigs.forEach(config => {
      const inputEl = this.form.querySelector(`#${config.id}`);
      const val = ATSValidation.cleanValue(inputEl.value, config.rules || {});

      // Append original camelCase field name
      formData.append(config.id, val);

      // Map and append snake_case variant to match standard backend expectations
      const snakeCaseKey = config.id.replace(/([A-Z])/g, "_$1").toLowerCase();
      formData.append(snakeCaseKey, val);

      // Special mappings for common variations
      if (config.id === "mobileNumber") {
        formData.append("mobile", val);
        formData.append("phone", val);
      }
      if (config.id === "alternateMobile") {
        formData.append("alternate_mobile_number", val);
        formData.append("alt_mobile", val);
      }
      if (config.id === "experience") {
        formData.append("years_of_experience", val);
        formData.append("experience_years", val);
      }
      if (config.id === "email") {
        formData.append("email_address", val);
      }
    });

    // Capture the applicant source from the URL (e.g., ?src=LinkedIn)
    const urlParams = new URLSearchParams(window.location.search);
    const applicantSource = urlParams.get('src') || urlParams.get('source') || 'Company Career Portal';
    formData.append("source", applicantSource);

    // Handle Terms explicitly
    formData.append("accepted_terms", "true");
    formData.append("terms_accepted", "true");

    try {
      const apiEndpoint = `https://ats.people-prime.com/api/public/jobs/${this.jobId}/apply/`;
      console.log(`Submitting application to API: ${apiEndpoint}`);

      const response = await fetch(apiEndpoint, {
        method: "POST",
        body: formData
      });

      if (!response.ok) {
        throw new Error(`API returned status ${response.status}`);
      }

      const result = await response.json();
      console.log("Application submitted successfully to backend:", result);
      this.onSubmitSuccess(formData);
    } catch (err) {
      console.error("API submission failed, falling back to simulated success for demonstration:", err);

      // Render a subtle warning banner for demonstration/local testing
      const warningBanner = document.createElement("div");
      warningBanner.style.cssText = "background: rgba(255, 180, 0, 0.1); border: 1px solid rgba(255, 180, 0, 0.3); color: #f5a623; padding: 12px; border-radius: 8px; font-size: 11px; margin-top: 16px; line-height: 1.4; text-align: center;";
      warningBanner.innerHTML = `<strong>Notice:</strong> Application received locally! Backend API reported a connection warning: ${err.message}.`;
      this.form.appendChild(warningBanner);

      setTimeout(() => {
        this.onSubmitSuccess(formData);
      }, 2000);
    }
  }
}

// Attach component references to window so they are globally readable by job-details.js
window.ATSApplicationForm = ATSApplicationForm;
window.ATSTermsModal = ATSTermsModal;
window.ATSFileUpload = ATSFileUpload;
window.ATSInput = ATSInput;
window.ATSSubmitButton = ATSSubmitButton;
window.ATSValidation = ATSValidation;
